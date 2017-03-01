#!/bin/sh

WORKSPACE=`pwd`
PROJ_NAME=$1
TAG_NAME=$2
#dev test pre prd
env=$3
NGINX_URL=http://10.125.136.44/${PROJ_NAME}/${PROJ_NAME}_${TAG_NAME}.tar.gz
TMP_DIR_NAME=temp

set -e

rm -f *.tar.gz
mkdir -p ${TMP_DIR_NAME}
cd ${TMP_DIR_NAME}
wget ${NGINX_URL}

if [ ${env} == "dev" ]
then
    mv -f ${PROJ_NAME}_${TAG_NAME}.tar.gz ../../gome/${PROJ_NAME}.tar.gz
    rm -rf ../${TMP_DIR_NAME}
    
    cd /gomeo2o/duandian/assets/gome
    mkdir -p /gomeo2o/duandian/assets/gome/${PROJ_NAME}
    
    rm -rf ${PROJ_NAME}
    tar -zvxf ${PROJ_NAME}.tar.gz
    mv ./public  ${PROJ_NAME}
    rm -rf ${PROJ_NAME}_bak.tar.gz
    mv ${PROJ_NAME}.tar.gz ${PROJ_NAME}_bak.tar.gz
    
    exit
fi


tar -zxvf ${PROJ_NAME}_${TAG_NAME}.tar.gz
pwd
if [ ${env} == "pre"  ]
then
   sed -i 's#photohref: http://www.gome.com#photohref: http://xpop-pre.gomeplus.com/#g' public/front_config.yaml
   sed -i 's#main: http://www.gome.com#main: http://xpop-pre.gomeplus.com#g' public/front_config.yaml
   sed -i 's#login: http://admin.gome.com/login#login: http://admin-pre.gomeplus.com/login#g' public/front_config.yaml
   sed -i 's#mainHref: http://www.gome.com#mainHref: http://admin-pre.gomeplus.com#g' public/front_config.yaml
elif [ ${env} == "test"  ]   
   then
   sed -i 's#photohref: http://www.gome.com#photohref: http://xpop-test.gomeplus.com/#g' public/front_config.yaml
   sed -i 's#main: http://www.gome.com#main: http://xpop-test.gomeplus.com#g' public/front_config.yaml
   sed -i 's#login: http://admin.gome.com/login#login: http://admin-test.gomeplus.com/login#g' public/front_config.yaml
   sed -i 's#mainHref: http://www.gome.com#mainHref: http://admin-test.gomeplus.com#g' public/front_config.yaml
elif [ ${env} == "prd"  ]
then
   sed -i 's#photohref: http://www.gome.com#photohref: http://mxman.gomeo2omx.cn#g' public/front_config.yaml
   sed -i 's#main: http://www.gome.com#main: http://mxman.gomeo2omx.cn#g' public/front_config.yaml
   sed -i 's#login: http://admin.gome.com/login#login: http://mxman.gomeo2omx.cn/login#g' public/front_config.yaml
   sed -i 's#mainHref: http://www.gome.com#mainHref: http://mxman.gomeo2omx.cn#g' public/front_config.yaml
elif [ ${env} == "fusion"  ]
then
   sed -i 's#photohref: http://www.gome.com#photohref: http://admin.fusion.intra.gomeplus.com#g' public/front_config.yaml
   sed -i 's#main: http://www.gome.com#main: http://admin.fusion.intra.gomeplus.com#g' public/front_config.yaml
   sed -i 's#login: http://admin.gome.com/login#login: http://admin.fusion.intra.gomeplus.com/login#g' public/front_config.yaml
   sed -i 's#mainHref: http://www.gome.com#mainHref: http://admin.fusion.intra.gomeplus.com#g' public/front_config.yaml
fi
rm -f ${PROJ_NAME}_${TAG_NAME}.tar.gz
tar -zcvf ${PROJ_NAME}.tar.gz  public
pwd
ls -l
mv -f ${PROJ_NAME}.tar.gz ../
# 删除创建的目录
rm -rf ../${TMP_DIR_NAME}

if [ ${env} == "pre"  ] || [ ${env} == "prd"  ] || [ ${env} == "test"  ] || [ ${env} == "fusion"  ]
then 
   rm -rf /gomeo2o/assets/${PROJ_NAME}
   cd /gomeo2o/assets/temp
   tar -zvxf ${PROJ_NAME}.tar.gz
   mv ./public ../${PROJ_NAME}
   rm -rf /gomeo2o/assets/temp/${PROJ_NAME}.tar.gz
fi


