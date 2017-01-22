#!/bin/sh

BUILD_ID=dontKillMe

#生产环境
ENV=prd

export JAVA_HOME=/usr/local/jdk1.7.0_75
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$JAVA_HOME/bin:$PATH

JETTY_PATH=/usr/local/jetty-$1   #admin
SERVICE_BASE_URL=http://10.125.201.33:8181

HISTORY=/gomeo2o/history/$1-history

PROJECT_NAME=venus-$1
PROJECT_VERSION=$2  #1.0-SNAPSHOT
SERVICE_NAME=venus-$1
TMP=/gomeo2o/temp
PROJECT_HOME=/gomeo2o/projects/venus-$1
set -e

function stopService(){
	${JETTY_PATH}/bin/jetty.sh stop
	P_ID=`ps -ef | grep -w "/usr/local/jetty-$1" | grep -v "grep" | awk '{print $2}'`
	if [ "$P_ID" == "" ]; then
			echo "stop jetty-8 finished!"
	else
		echo "stop jetty-8 error!"
			kill -9 $P_ID
		echo "stop jetty-8.1.16 kill!"
	fi
}
#删除旧的生成
function cleanWorkSpace(){
	cd ${PROJECT_HOME}
	rm -rf *
}
function download_properties(){

	mkdir -p ${TMP}/${PROJECT_NAME}
	
}

#部署
function deploy(){
	
	cd ${PROJECT_HOME}
	#删除上次wget
	rm -rf ${PROJECT_NAME}-${PROJECT_VERSION}.war
	rm -rf *
	wget ${SERVICE_BASE_URL}/${PROJECT_NAME}/${PROJECT_NAME}-${PROJECT_VERSION}.war
	#解压缩
	jar xvf ${PROJECT_NAME}*.war
	rm -rf venus-*.war
	#替换配置文件
	if [ "$1" == "schedule" ]
	then
		mv -f ${TMP}/${ENV}.properties ${PROJECT_HOME}/WEB-INF/classes/app.properties
		mv -f ${TMP}/${ENV}_quartz.properties ${PROJECT_HOME}/WEB-INF/classes/quartz.properties
		mv -f ${TMP}/${ENV}_web.xml ${PROJECT_HOME}/WEB-INF/web.xml
		mv -f ${TMP}/logback.xml ${PROJECT_HOME}/WEB-INF/classes/logback.xml
	else
		mv -f ${TMP}/${ENV}.properties ${PROJECT_HOME}/WEB-INF/classes/app.properties
 	      	mv -f ${TMP}/href.properties ${PROJECT_HOME}/WEB-INF/classes/href.properties
		mv -f ${TMP}/session.properties ${PROJECT_HOME}/WEB-INF/classes/session.properties
		mv -f ${TMP}/logback.xml ${PROJECT_HOME}/WEB-INF/classes/logback.xml
		if [ "$1" == "web" ]
		then
			mv -f ${TMP}/xpop.gomeplus.com.perm ${PROJECT_HOME}/WEB-INF/classes/xpop.gomeplus.com.perm
			mv -f ${TMP}/${ENV}_xpop_web.xml ${PROJECT_HOME}/WEB-INF/web.xml
		else
			mv -f ${TMP}/mxman.gomeo2omx.cn.perm ${PROJECT_HOME}/WEB-INF/classes/mxman.gomeo2omx.cn.perm
			mv -f ${TMP}/${ENV}_admin_web.xml ${PROJECT_HOME}/WEB-INF/web.xml
		fi
	fi
	
	jar cvf ${SERVICE_NAME}.war *
	
	#备份
	mv -f ${PROJECT_HOME}/${SERVICE_NAME}.war ${HISTORY}/${PROJECT_NAME}-`date "+%Y-%m-%d_%H-%M-%S"`.war
}
#启动
function startService()
{	
	${JETTY_PATH}/bin/jetty.sh start >/dev/null 2>&1 &
}

function main()
{
	stopService $1 $2
	cleanWorkSpace $1
	download_properties
	deploy $1 $2
	startService $1
}
main $1 $2










