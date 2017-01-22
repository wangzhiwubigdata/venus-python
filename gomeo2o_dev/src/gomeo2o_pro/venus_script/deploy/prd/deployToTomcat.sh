#!/bin/sh
BUILD_ID=DONTKILLME
#生产环境，主要用于部署tomcat服务。
#注意，下载的包名是否就是期望项目名，替换配置是否正确
ENV=prd

export JAVA_HOME=/usr/local/jdk1.7.0_75
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$JAVA_HOME/bin:$PATH

PROJECT_NAME=$1
PROJECT_VERSION=$2
#部署到tomcat下是的名字有可能跟项目名不一样。
SERVICE_NAME=${PROJECT_NAME}
#tomcat位于/user/local下，运行脚本时，变量tomcat名需要传递
TOMCAT_PATH=/usr/local/$3

SERVICE_BASE_URL=http://10.125.201.33:8181
HISTORY=/gomeo2o/data/venus
#生产环境不用tmp
TMP=/gomeo2o/temp

set -e

function check_service_verison()
{
	if [ "${PROJECT_VERSION}" = "" ] || [ "${PROJECT_VERSION}" == " " ]
	then 
		echo "请填写服务版本号"
		exit 1
	fi
}
function stopService()
{
	${TOMCAT_PATH}/bin/catalina.sh stop
	sleep 3
	#有可能一台机器上不上多个tomcat，查询进程号用ps -ef|grep ${TOMCAT_PATH}/ 比较合适
	P_ID=`ps -ef | grep -w "${TOMCAT_PATH}/" | grep -v "grep" | awk '{print $2}'`
	if [ "$P_ID" == "" ]; then
		echo "stop tomcat finished!"
	else
	    	echo "stop  tomcat begin!"
    		kill -9 $P_ID
    		echo "stop  tomcat kill!"    
	fi
}

function backup_and_clean()
{
	mkdir -p ${HISTORY}/${PROJECT_NAME}/history/
	if [ -f ${TOMCAT_PATH}/webapps/${SERVICE_NAME}.war ]
	then
		cp -f ${TOMCAT_PATH}/webapps/${SERVICE_NAME}.war ${HISTORY}/${PROJECT_NAME}/history/${PROJECT_NAME}-`date "+%Y-%m-%d_%H-%M-%S"`.war
	fi
	rm -rf ${TOMCAT_PATH}/webapps/${SERVICE_NAME}*
}

function deploy()
{
	mkdir -p ${TMP}/${SERVICE_NAME}
	cd ${TMP}/${SERVICE_NAME}
	
	#下载war包
	wget ${SERVICE_BASE_URL}/${PROJECT_NAME}/${PROJECT_NAME}-${PROJECT_VERSION}.war
	
	#解压war包
	jar xvf ${PROJECT_NAME}*.war
	rm -f ${PROJECT_NAME}*.war
	
	#【替换公共配置1】:首先，每个app都有app.properties需要替换，特殊的是service.properties。
		#部署项目时需要注意，本脚本只适用于app.profiles的情况
	mv -f ${TMP}/${ENV}.properties ${TMP}/${SERVICE_NAME}/WEB-INF/classes/app.properties
	if [ -f ${TMP}/logback.xml ]
	then
		mv -f ${TMP}/logback.xml ${TMP}/${SERVICE_NAME}/WEB-INF/classes/logback.xml
	fi
    
	#【特殊替换】
    if [ "${PROJECT_NAME}" == "venus-count-web" ]
	then
		mv -f ${TMP}/quartz.properties ${TMP}/${SERVICE_NAME}/WEB-INF/classes/quartz.properties
	fi
	
	if [ "${PROJECT_NAME}" == "venus-audit-web" ]
	then
		mv -f ${TMP}/session.properties ${TMP}/${SERVICE_NAME}/WEB-INF/classes/session.properties
		mv -f ${TMP}/web.xml ${TMP}/${SERVICE_NAME}/WEB-INF/web.xml
	fi
	
	jar cvf ${SERVICE_NAME}.war ./*
	mv ${SERVICE_NAME}.war ${TOMCAT_PATH}/webapps
	
	rm -rf *
}
function startService()
{
	${TOMCAT_PATH}/bin/catalina.sh start
}
function main()
{
	if [ "${PROJECT_NAME}" == "venus-api-servlet" ]
	then
		SERVICE_NAME="v2"
	elif [ "${PROJECT_NAME}" == "venus-badword-web" ]
	then
		SERVICE_NAME="badword"
	elif [ "${PROJECT_NAME}" == "venus-count-web" ]
	then
		SERVICE_NAME="count"
	fi
	
	check_service_verison
	stopService
	backup_and_clean
	deploy
	startService
}

main

