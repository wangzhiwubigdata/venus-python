#!/bin/sh

PROJ_NAME=$1    # ponyta
TAG_NAME=$2     # 20160727_bugfix
SVN_VERSION=$3  # HEAD
SUBFIELD=$4
BRANCHNAME=$5
SVN_URL=https://svn.gomeo2o.cn:8443/gomeo2o_dev/src/gomeo2o_terminus/${PROJ_NAME}
TAG_URL=https://svn.gomeo2o.cn:8443/gomeo2o_dev/src/gomeo2o_terminus_tags/${PROJ_NAME}_tags/${TAG_NAME}
RUBY_HOME=/usr/local/ruby/bin
BASEPATH=`pwd`
TAG_DIR=/gomeo2o/tags/${PROJ_NAME}_tags
NGINX_DIR=/gomeo2o/tags/nginx_dir/${PROJ_NAME}


#LOGFILE=/gomeo2o/tags/logs/${PROJ_NAME}_pkg-`date +%Y%m%d%H%M%S`.log

set -e

function create_tag(){
    if [ ${SUBFIELD} != ${PROJ_NAME} ] 
    then
       SVN_URL=https://svn.gomeo2o.cn:8443/gomeo2o_dev/src/gomeo2o_terminus/${PROJ_NAME}_branches/${BRANCHNAME}
    fi
    svn cp -r ${SVN_VERSION} ${SVN_URL} ${TAG_URL} -m "tag ${TAG_NAME}"
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

function compress_and_move(){
    echo "============  compress begin  =============="
    tarName=${PROJ_NAME}_${TAG_NAME}.tar.gz
    tar -zcvf ${tarName} public
    
    #if [ -d ${NGINX_DIR} ] then
    #    mkdir -p ${NGINX_DIR}
    #fi
    
    mkdir -p ${NGINX_DIR}
    mv -f  ${tarName} ${NGINX_DIR}
    echo "============  compress end    =============="
    echo "================== svn tag目录  https://svn.gomeo2o.cn:8443/gomeo2o_dev/src/gomeo2o_terminus_tags/${PROJ_NAME}_tags/${TAG_NAME}   ==========================="
    echo "===========  打好的包可到  http://10.125.2.12:8181/${PROJ_NAME}  进行下载   ============="
   
}

function main(){
    
    create_tag
    checkout_svn_code
    compile_by_ruby
    compress_and_move
}


main
