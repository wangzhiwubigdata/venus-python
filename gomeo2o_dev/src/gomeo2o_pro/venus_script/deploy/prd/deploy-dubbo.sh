#!/bin/sh
BUILD_ID=DONTKILLME
set -e
#ENV=prd 生成环境
ENV=prd

export JAVA_HOME=/usr/local/jdk1.7.0_75
export PATH=$JAVA_HOME/bin:$PATH

SERVICE_BASE_PATH=/gomeo2o
SERVICE_NAME=${1}
SERVICE_BASE_URL=http://10.125.201.33:8181
VERSION=${1}-${2}.tar.gz
SCRIPT_PATH=/gomeo2o/script

##停止服务
function stopService(){
	if [ ! -e ${SERVICE_BASE_PATH}/${SERVICE_NAME}/history ]
	then
		mkdir -p ${SERVICE_BASE_PATH}/${SERVICE_NAME}/history
	fi
	if [ ! -e ${SERVICE_BASE_PATH}/${SERVICE_NAME}/logs ]
        then
                mkdir -p ${SERVICE_BASE_PATH}/${SERVICE_NAME}/logs
        fi
	if [ ! -e ${SERVICE_BASE_PATH}/${SERVICE_NAME}/temp ]
        then
                mkdir -p ${SERVICE_BASE_PATH}/${SERVICE_NAME}/temp
        fi
	if [ -e ${SERVICE_BASE_PATH}/${SERVICE_NAME}/bin ]
	then
		${SERVICE_BASE_PATH}/${SERVICE_NAME}/bin/venus-service stop
	fi
}

##发布服务
function deploy(){
	cd ${SERVICE_BASE_PATH}/${SERVICE_NAME}/temp
	rm -rf *
	#从nginx下载服务
	wget ${SERVICE_BASE_URL}/${SERVICE_NAME}/${VERSION}
	tar zxvf ./*.tar.gz
	rm -rf venus-service/logs
	mv ./venus-service/*  ../
	chmod +x ${SERVICE_BASE_PATH}/${SERVICE_NAME}/bin/*
	cd ../etc
	#为服务添加配置文件，配置文件分环境各不相同
	mv -f ${SERVICE_BASE_PATH}/tmp/${ENV}.properties app.properties
	sed -i 's/Dspring.profiles.active=default/Dspring.profiles.active=cluster/g' wrapper.conf
}


##备份
function backup(){
	cd  ${SERVICE_BASE_PATH}/${SERVICE_NAME}
	if [ -e ${SERVICE_BASE_PATH}/${SERVICE_NAME}/bin ]
	then	
		TIMESTAMP=`date "+%Y-%m-%d_%H-%M-%S"`
		tar -czvf ${SERVICE_NAME}_${TIMESTAMP}.tar.gz  ./bin ./etc ./lib 
		mv ./*_*.tar.gz ./history/
		rm -rf ${SERVICE_BASE_PATH}/${SERVICE_NAME}/bin
		rm -rf ${SERVICE_BASE_PATH}/${SERVICE_NAME}/lib
		rm -rf ${SERVICE_BASE_PATH}/${SERVICE_NAME}/etc
		#rm -rf ${SERVICE_BASE_PATH}/${SERVICE_NAME}/logs
	fi
}


##启动服务
function startService(){

	${SERVICE_BASE_PATH}/${SERVICE_NAME}/bin/venus-service start
	echo ">>>正在启动dubbo,请稍等 ... "
	sleep 10
	tail  ${SERVICE_BASE_PATH}/${SERVICE_NAME}/logs/wrapper.log
}

function main(){
	stopService
	backup
	deploy
	startService
}
main
