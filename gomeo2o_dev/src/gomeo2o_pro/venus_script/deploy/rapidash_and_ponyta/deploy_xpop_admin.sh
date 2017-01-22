#!/bin/sh



WORKSPACE=`pwd`
PROJ_NAME=$1
TAG_NAME=$2
#dev pre prd
env=$3
NGINX_URL=http://10.125.2.12:8181/${PROJ_NAME}/${PROJ_NAME}_${TAG_NAME}.tar.gz

if [ ${env} == "prd" ]
then
    NGINX_URL=http://10.125.4.90/${PROJ_NAME}/${PROJ_NAME}_${TAG_NAME}.tar.gz
fi

set -e

rm -f *.tar.gz
mkdir -p temp
cd temp
wget ${NGINX_URL}

if [ ${env} == "dev" ]
then
    mv -f ${PROJ_NAME}_${TAG_NAME}.tar.gz ../${PROJ_NAME}.tar.gz
    rm -rf ../temp
    exit
fi

if [ ${PROJNAME} == "ponyta" ]
then 
    mv -f ${PROJ_NAME}_${TAG_NAME}.tar.gz ../${PROJ_NAME}.tar.gz
    rm -rf ../temp
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
elif [ ${env} == "prd"  ]
then
   sed -i 's#photohref: http://www.gome.com#photohref: http://mxman.gomeo2omx.cn#g' public/front_config.yaml
   sed -i 's#main: http://www.gome.com#main: http://mxman.gomeo2omx.cn#g' public/front_config.yaml
   sed -i 's#login: http://admin.gome.com/login#login: http://mxman.gomeo2omx.cn/login#g' public/front_config.yaml
   sed -i 's#mainHref: http://www.gome.com#mainHref: http://mxman.gomeo2omx.cn#g' public/front_config.yaml
fi
rm -f ${PROJ_NAME}_${TAG_NAME}.tar.gz
tar -zcvf ${PROJ_NAME}.tar.gz  public
pwd
ls -l
mv -f ${PROJ_NAME}.tar.gz ../../
# 删除创建的目录
rm -rf ../temp



