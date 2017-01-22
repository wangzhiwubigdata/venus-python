
#!/bin/sh

BUILD_ID=dontKillMe

# 不同环境时替换 ${ENV}
ENV=pre
export JAVA_HOME=/usr/local/jdk1.7.0_75
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$JAVA_HOME/bin:$PATH

JETTY_PATH=/gomeo2o/mxsev/installed/jetty-$1
SERVICE_BASE_URL=http://10.125.201.33:8181
HISTORY=/home/mxsev/projects/gome/history/$1-history

PROJECT_NAME=$1
PROJECT_VERSION=$2  #1.0-SNAPSHOT
SERVICE_NAME=$1
#TMP=/gomeo2o/tmp
TMP=/home/mxsev/projects/gome/tempDir
PROJECT_HOME=/home/mxsev/projects/gome/$1

set -e

function stopService(){

	${JETTY_PATH}/bin/jetty.sh stop
	P_ID=`ps -ef | grep -w "${JETTY_PATH}" | grep -v "grep" | awk '{print $2}'`
        #P_ID=`ps -ef | grep -w "jetty-$1" | grep -v "grep" | awk '{print $2}'`        
        if [ "${P_ID}" == "" ] ;  then
          echo "jetty is stopped!"
        else
          echo "stop jetty failed!"
          kill -9 ${P_ID}
          echo "jetty process  is killed"
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
        mkdir -p ${PROJECT_HOME}
	cd ${PROJECT_HOME}
	#删除上次的部署
	rm -rf *
	wget ${SERVICE_BASE_URL}/${PROJECT_NAME}/${PROJECT_NAME}-${PROJECT_VERSION}.war
	#解压缩
	jar xvf ${PROJECT_NAME}*.war
	rm -rf ${PROJECT_NAME}*.war
	#替换配置文件
	mv -f ${TMP}/${ENV}.properties ${PROJECT_HOME}/WEB-INF/classes/app.properties
	if [ "venus-settlement-web" == $1 ] ; then
           mv -f ${TMP}/quartz.properties ${PROJECT_HOME}/WEB-INF/classes/quartz.properties
           #mv -f ${TMP}/web.xml ${PROJECT_HOME}/WEB-INF/web.xml
        fi  

	#重新压缩打成venus-pay-web.war
	jar cvf ${SERVICE_NAME}.war *
	#备份
        mkdir -p ${HISTORY}
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










