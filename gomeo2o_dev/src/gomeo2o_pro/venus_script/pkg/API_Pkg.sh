#!/bin/bash

BASE_PATH=$PWD
SVN_URL=`svn info|grep URL|awk '{print $NF}'`
PROJECT_NAME=${JOB_NAME}
NGINX_FILE_PATH=/gomeo2o/project/${PROJECT_NAME}
WORK_BRANCH=${SUBFIELD}
PROJECT_VERSION=""
TAR_VERSION=""

TEMP=/tmp/mvn_pkg-`date +%Y%m%d%H%M%S`.log
echo "">${TEMP}
FTP_URL=http://10.125.201.33:8181

function check_property_snapshot()
{
	echo "正在检查依赖...."
	verions_arr=$(mvn versions:display-property-updates |fgrep venus|fgrep [INFO]|fgrep -v Building|awk '{ print $4}')
	for  v_arr in $verions_arr
	do
		if [[ "${v_arr}" =~ -SNAPSHOT$ ]]
		then
			echo "=^【-!-】^=:发布release版本不能有snapshot的依赖，请修改后重试==="
			echo "##################################BEGIN####################################"
			mvn versions:display-property-updates |fgrep venus|fgrep SNAPSHOT | grep -v Building
			echo "###################################END#####################################"
			exit 1
		fi
	done	
	echo "========依赖检查通过=========="
}

function pushPkgToRemote()
{
    TAR_NAME=${PROJECT_NAME}-${TAR_VERSION}.tar.gz
    set -e
    echo "--------maven--打包成功，准备tar.gz,并放入nginx文件服务器目录-------"
    cd ${BASE_PATH}/${WORK_BRANCH}/target/jsw
    tar zcvf ${TAR_NAME} venus-service/
    mkdir -p ${NGINX_FILE_PATH}/${HISTORY_PATH}
    mv -f ${TAR_NAME} ${NGINX_FILE_PATH}
    echo "====最后:==把服务发布包上传到nginx文件服务${FTP_URL}/${PROJECT_NAME}">>${TEMP}
}
#获取项目版本号
function get_project_version()
{
    cd ${WORK_BRANCH}
    echo ${PROJECT_NAME}
    PROJECT_VERSION=`mvn clean|fgrep "Building ${PROJECT_NAME}"|awk '{print $NF}'`
    echo "当前pom.xml中项目快照版本为:${PROJECT_VERSION}"
    if [[ "${PROJECT_VERSION}" =~ -SNAPSHOT$ ]]
    then
            :
    else
            echo "[ERROR]:给出的打release的分支版本不带SNAPSHOT，请修改后重试"
            exit 1
    fi
    echo "====*====:原项目版本号为:${PROJECT_VERSION}--------">>${TEMP}
}
function display_property_updates()
{
	echo "=========:此版本对其他项目依赖和最新版本对比==================">>${TEMP}
	mvn versions:display-property-updates |grep venus | grep "\\$">>${TEMP}
	echo "==============================================================">>${TEMP}
}
#错误回滚
function error_rollback()
{
    echo "====出错===="
    svn up
    mvn clean
    mvn versions:set -DnewVersion=${PROJECT_VERSION} -e
    svn ci -m "恢复到打包之前的snapshot版本"
    echo "===打包失败，回滚成功==="
    exit 1
}
#release打包
function release_mvn_pkg()
{
    RELESE_VERSION=${PROJECT_VERSION%-SNAPSHOT}
    TAR_VERSION=${RELESE_VERSION}
    echo "准备发布的release版本为：【${RELESE_VERSION}】"
    echo "====*====:发布版本号为:${RELESE_VERSION}-------">>${TEMP}
    if [ -d ${BASE_PATH}/tags/${RELESE_VERSION} ]
    then
	    echo "==【-!-】==tags已经存在${RELESE_VERSION}，请检查是否已有对于release版本"
    fi
    mvn versions:set -DnewVersion=${RELESE_VERSION} -e || exit 1
    SVN_VERSION=`svn ci ${BASE_PATH}/${WORK_BRANCH} -m "release:${RELESE_VERSION}" | fgrep 'Committed revision'|awk '{print $NF}'`
    if [ $? -eq 0 ]
    then
            echo "svn commit success,this svn version is ${SVN_VERSION}"
    else
            mvn versions:set -DnewVersion=${PROJECT_VERSION} -e
            echo "svn commit failed"
            exit 1
    fi
    #升snapshot版本号
    NEW_SNAPSHOT=`snapshot_Incr ${RELESE_VERSION}`"-SNAPSHOT"
    echo "准备更新snapshot版本号为:${NEW_SNAPSHOT}"
    echo "====*====:开发版本被更新为:${NEW_SNAPSHOT}-------">>${TEMP}
    mvn versions:set -DnewVersion=${NEW_SNAPSHOT} -e || error_rollback
    svn up
    svn ci ${BASE_PATH}/${WORK_BRANCH} -m "${NEW_SNAPSHOT}" || error_rollback

    #对上一个版本打包
    svn up -r${SVN_VERSION%.}
    if [[ "${PROJECT_NAME}" =~ -servlet$ ]]
    then 
	    mvn clean deploy -e -Ppkg -Dmaven.test.skip=true || error_rollback
    else    
    	mvn clean deploy -e -Dmaven.test.skip=true || error_rollback
    fi
    echo "----deploy到私服成功--------"
    echo "====*====:发版版本jar包上传私服成功:${RELESE_VERSION}-------">>${TEMP}
    display_property_updates
    #分支提交到tags
    svn cp --parents ${BASE_PATH}/${WORK_BRANCH} ${BASE_PATH}/tags/${RELESE_VERSION} || error_rollback
    svn ci ${BASE_PATH}/tags/${RELESE_VERSION} -m "cp ${RELESE_VERSION} to tags" || error_rollback
    echo "====*====:发版版本打tag成功-------">>${TEMP}
}
#工具函数
function snapshot_Incr()
{
        arr=()
    i=0
    var=${RELESE_VERSION//./ }
    for element in $var
    do
            arr[(i++)]=$element
    done
    len=${#arr[@]}
    arr[$len -1]=`expr "${arr[$len-1]}" + "1"`
    vs=""
    for str in ${arr[@]}
    do
            vs=${vs}"."${str}
    done
    echo ${vs#.}
}
#快照打包
function snapshot_mvn_pkg()
{       
	TAR_VERSION=${PROJECT_VERSION}
	if [[ "${PROJECT_NAME}" =~ -servlet$ ]]
	then
		mvn deploy -e -U -Ppkg -e -Dmaven.test.skip=true || exit 1
		echo "servlet项目打包"
	else
		mvn deploy -e -U -Dmaven.test.skip=true || exit 1
	fi
	display_property_updates
	echo "====*====:SNAPSHOT版本jar包上传私服成功:${PROJECT_VERSION}-------">>${TEMP}
}

function check_already_packaged()
{
	if [ `svn info ${BASE_PATH}/${WORK_BRANCH} | fgrep 'Last Changed Author' | awk '{print $NF}'` == 'mxsev' ]
	then
		echo "!!! 这个包应该已经打过了 !!!"
		exit 1
	fi
}

function main()
{
    get_project_version
    if [ "${PKTYPE}" == "release" ]
    then
	    check_already_packaged
	    check_property_snapshot
            release_mvn_pkg
            #pushPkgToRemote ${TAR_VERSION}
    else
            snapshot_mvn_pkg
            #pushPkgToRemote ${TAR_VERSION}
    fi
    cat ${TEMP}
    
    #删除日志文件
    if [ -f "${TEMP}" ]
    then
	    rm -f ${TEMP}
    fi
}

main


