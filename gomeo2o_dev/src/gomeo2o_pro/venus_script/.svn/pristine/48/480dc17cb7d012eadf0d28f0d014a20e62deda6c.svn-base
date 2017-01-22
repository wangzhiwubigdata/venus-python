#!/bin/sh

#生产环境
ENV=prd

export JAVA_HOME=/usr/local/jdk1.7.0_75
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$JAVA_HOME/bin:$PATH

BUILD_ID=DONTKILLME
#tomcat位于/user/local下，允许脚本时，变量tomcat名需要传递
TOMCAT_PATH=/usr/local/$3
SERVICE_BASE_URL=http://10.125.201.33:8181

HISTORY=/gomeo2o/data/venus
TMP=/gomeo2o/tmp
PROJECT_NAME=$1
PROJECT_VERSION=$2
SERVICE_NAME=${PROJECT_NAME}
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
	P_ID=`ps -ef | grep -w "${TOMCAT_PATH}" | grep -v "grep" | awk '{print $2}'`
	if [ "$P_ID" == "" ]; then
		echo "stop  tomcat8 finished!"
	else
	    	echo "stop  tomcat8 begin!"
    		kill -9 $P_ID
    		echo "stop  tomcat8 kill!"    
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
	cd ${TMP}

function deploy()
{
	mkdir -p ${TMP}/${SERVICE_NAME}
	cd /${TMP}/${SERVICE_NAME}
	
	#下载war包
	wget ${SERVICE_BASE_URL}/${PROJECT_NAME}/${PROJECT_NAME}-${PROJECT_VERSION}.war
	
	#解压war包
	jar xvf ${PROJECT_NAME}*.war
	rm -f ${PROJECT_NAME}*.war
	
	#替换配置
	mv -f ${TMP}/${ENV}.properties ${TMP}/${SERVICE_NAME}/WEB-INF/classes/app.properties
	mv -f ${TMP}/logback.xml ${TMP}/${SERVICE_NAME}/WEB-INF/classes/logback.xml
	#
	jar cvf ${SERVICE_NAME}.war ./*
	mv ${SERVICE_NAME}.war ${TOMCAT_PATH}/webapps
	
	rm -rf *
	
}
function startService()
{
	if [ "${ENV}" == "pre" ] || [ "${ENV}" == "prd" ]
	then
		${TOMCAT_PATH}/bin/catalina.sh start -Dspring.profiles.active=cluster
	else

		${TOMCAT_PATH}/bin/catalina.sh start
	fi
}
function main()
{
	if [ "${PROJECT_NAME}" == "venus-api-servlet" ]
	then
		SERVICE_NAME="v2"
	fi
	
	check_service_verison
	stopService
	backup_and_clean
	deploy
	startService
}

main

