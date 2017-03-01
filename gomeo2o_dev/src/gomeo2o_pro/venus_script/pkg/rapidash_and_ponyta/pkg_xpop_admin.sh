#!/bin/sh

PROJ_NAME=$1    # ponyta
SVN_VERSION=$2  # HEAD
SUBFIELD=$3
BRANCHNAME=$4
TAG_NAME=""     
NEXT_VERSION=""
SVN_URL=https://svn.gomeo2o.cn:8443/gomeo2o_dev/src/gomeo2o_terminus/${PROJ_NAME}
TAG_URL=""
RUBY_HOME=/usr/local/ruby/bin
BASEPATH=`pwd`
TAG_DIR=/gomeo2o/tags/${PROJ_NAME}_tags
TAG_MANAGE_DIR=${TAG_DIR}/version_manage/${PROJ_NAME}
NGINX_DIR=/gomeo2o/tags/nginx_dir/${PROJ_NAME}


set -e

# 参数校验
function check_params(){
    if [ "" == ${SVN_VERSION} ] 
    then
        echo "SVN版本号不能为空"
        exit 1
    fi
}

# 获取tag版本号
function obtain_tag_version(){
    if [ ${SUBFIELD} != ${PROJ_NAME} ] 
    then
       SVN_URL=https://svn.gomeo2o.cn:8443/gomeo2o_dev/src/gomeo2o_terminus/${PROJ_NAME}_branches/${BRANCHNAME}
    fi
    
    if [ `svn info -r ${SVN_VERSION} ${SVN_URL} | fgrep 'Last Changed Author' | awk '{print $NF}'` == 'mxsev' ]
	then
		echo "!!! 这个包应该已经打过了 !!!"
		exit 1
	fi
    
    
    TAG_NAME=`svn cat ${SVN_URL}/.tagmanage`
    echo "==========即将发布的tag版本号为  ${TAG_NAME}=========="
    TAG_URL=https://svn.gomeo2o.cn:8443/gomeo2o_dev/src/gomeo2o_terminus_tags/${PROJ_NAME}_tags/${TAG_NAME}
    NEXT_VERSION=`snapshot_Incr`
    echo "==========分支版本号将被提升为 ${NEXT_VERSION}=========="
}

#工具函数 copied from admin_pkg_sh
function snapshot_Incr()
{
    arr=()
    i=0
    var=${TAG_NAME//./ }
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

# 打tag
function create_tag(){
    # 创建svn tag路径
	svn cp -r ${SVN_VERSION} ${SVN_URL} ${TAG_URL} -m "tag ${TAG_NAME}" || exit 1
	# 升tag版本号
    mkdir -p ${TAG_MANAGE_DIR}
    cd ${TAG_MANAGE_DIR}
    rm -f .tagmanage
    svn checkout ${SVN_URL}
    if [ ${SUBFIELD} != ${PROJ_NAME} ]
    then
        echo ${NEXT_VERSION} > ${BRANCHNAME}/.tagmanage
        svn commit ${BRANCHNAME}/.tagmanage -m "tag ${TAG_NAME}" || exit 1
        rm -rf ${BRANCHNAME}
    else
        echo ${NEXT_VERSION} > ${PROJ_NAME}/.tagmanage
        svn commit ${PROJ_NAME}/.tagmanage -m "tag ${TAG_NAME}" || exit 1
        rm -rf ${PROJ_NAME}
    fi
    
}

function checkout_svn_code(){
     cd ${TAG_DIR}
     svn co https://svn.gomeo2o.cn:8443/gomeo2o_dev/src/gomeo2o_terminus_tags/${PROJ_NAME}_tags/${TAG_NAME}
}

function compile_by_ruby(){
     cd  ${TAG_DIR}/${TAG_NAME}
     echo "============   compile begin  =============="
     ${RUBY_HOME}/linner v
     ${RUBY_HOME}/linner b
     echo "============   compile end    =============="
}

function check_css_js(){
     CSS_DIR=${TAG_DIR}/${TAG_NAME}/public/assets/styles
     JS_DIR=${TAG_DIR}/${TAG_NAME}/public/assets/scripts
     find ${CSS_DIR} -type f|egrep -v -- '-[0-9a-zA-Z]{32}' && echo "有未编译的css，请修改config.yml" && exit 1
     set +e
     find ${JS_DIR} -type f|fgrep -v assets/scripts/templates.js|egrep -v -- '-[0-9a-zA-Z]{32}' && echo "有未编译的js，请修改config.yml" && exit 1
     set -e
}

function compress_and_move(){
    echo "============  compress begin  =============="
    tarName=${PROJ_NAME}_${TAG_NAME}.tar.gz
    tar -zcvf ${tarName} public
    mkdir -p ${NGINX_DIR}
    sudo mv -f  ${tarName} ${NGINX_DIR}
    #rsync -av  /gomeo2o/project/${PROJ_NAME} pkguser@10.125.136.44::pkg/ --password-file=/etc/rsyncd.user.pkguser
    echo "============  compress end    =============="
    echo "==== 本次发布的tag版本号为${TAG_NAME} ===="
    echo "==== svn tag目录  https://svn.gomeo2o.cn:8443/gomeo2o_dev/src/gomeo2o_terminus_tags/${PROJ_NAME}_tags/${TAG_NAME} ===="
    echo "==== 打好的包可到  http://10.125.136.44/${PROJ_NAME}  进行下载   ====" 
    #打包完成后清除文件
    rm -rf ${TAG_DIR}
}

function main(){
    check_params
    obtain_tag_version
    create_tag
    checkout_svn_code
    compile_by_ruby
    check_css_js
    compress_and_move
}


main
