#!/bin/sh

#环境
ENV=prd
WORK_PATH=/gomeo2o

export JAVA_HOME=/usr/local/jdk1.7.0_75
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$JAVA_HOME/bin:$PATH

BUILD_ID=DONTKILLME

#tomcat目录
TOMCAT_PATH=/usr/local/$3
SERVICE_BASE_URL=http://10.125.201.33:8181


#PROJECT_NAME=${JOB_NAME}
#PROJECT_VERSION=${VERSION}

HISTORY=${WORK_PATH}/data/venus
PROJECT_NAME=$1
PROJECT_VERSION=$2
SERVICE_NAME=${PROJECT_NAME}

set -e

function check_service_verison()
{
	if [ "${PROJECT_VERSION}" = "" ] || [ "${PROJECT_VERSION}" == " " ]
	then 
		echo "版本号不能为空"
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

function deploy()
{
	mkdir -p ${WORK_PATH}/tmp/${SERVICE_NAME}
	cd ${WORK_PATH}/tmp/${SERVICE_NAME}
	
	#下载war包
	wget ${SERVICE_BASE_URL}/${PROJECT_NAME}/${PROJECT_NAME}-${PROJECT_VERSION}.war
	
	#解压war
	jar xvf ${PROJECT_NAME}*.war
	rm -f ${PROJECT_NAME}*.war
	
	#替换配置文件
	if [ "${SERVICE_NAME}" == "v2" ]
	then 
		mv -f ${WORK_PATH}/tmp/${ENV}.properties ${WORK_PATH}/tmp/${SERVICE_NAME}/WEB-INF/classes/app.properties
	else
		mv -f ${WORK_PATH}/tmp/api_logback.xml ${WORK_PATH}/tmp/${SERVICE_NAME}/WEB-INF/classes/logback.xml
		mv -f ${WORK_PATH}/tmp/api_app.properties ${WORK_PATH}/tmp/${SERVICE_NAME}/WEB-INF/classes/app.properties
		mv -f ${WORK_PATH}/tmp/${ENV}.api.properties ${WORK_PATH}/tmp/${SERVICE_NAME}/WEB-INF/classes/service.properties
	fi
	
	jar cvf ${SERVICE_NAME}.war ./*
	mv ${SERVICE_NAME}.war ${TOMCAT_PATH}/webapps
	cd ..
	
	rm -rf ${WORK_PATH}/tmp/${SERVICE_NAME}
}

function startService()
{
	if [ "${ENV}" == "pre" ] || [ "${ENV}" == "prd" ]
	then
		echo "redis开启动集群模式"
		env JAVA_OPTS='-Dspring.profiles.active=cluster' /usr/local/tomcat/bin/catalina.sh start
		#${TOMCAT_PATH}/bin/catalina.sh start -Dspring.profiles.active=cluster
		echo "tomcat启动成功"
	else

		${TOMCAT_PATH}/bin/catalina.sh start
	fi
}
function change_service_name()
{
	if [ "${PROJECT_NAME}" == "venus-api-servlet" ]
	then
                SERVICE_NAME="v2"
        fi
        if [ "${PROJECT_NAME}" == "venus-api" ]
	then
		SERVICE_NAME="api"
	fi
}
function main()
{
	change_service_name
	check_service_verison
	stopService
	backup_and_clean
	deploy
	startService
}

main

