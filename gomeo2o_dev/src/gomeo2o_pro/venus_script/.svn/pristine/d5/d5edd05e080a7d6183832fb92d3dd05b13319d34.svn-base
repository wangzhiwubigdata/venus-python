#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import os
import urllib2
import tarfile
import zipfile
import shutil
import re
import config


class TarUtil:
    def __init__(self):
        self.tmp_dir = config.configs['tmp_dir']
        self.nginx_path = config.configs['nginx_url']

    def get_project(self, project, version):
        if os.path.exists(self.tmp_dir + project):
            shutil.rmtree(self.tmp_dir + project)
        os.makedirs(self.tmp_dir + project)
        os.chdir(self.tmp_dir + project)
        tar_url = self.nginx_path + project + '/' + project + '-' + version + '.tar.gz'
        war_url = self.nginx_path + project + '/' + project + '-' + version + '.war'
        base_name = project + '-' + version
        temp_dir = self.tmp_dir + project

        if urllib.urlopen(tar_url).getcode() == 200:
            zip_name = base_name + '.tar.gz'
            self.downloadfile(tar_url, zip_name)
            self.extract_tar_war(self.tmp_dir + project + '/' + zip_name, base_name, temp_dir)
        elif urllib.urlopen(war_url).getcode() == 200:
            self.downloadfile(war_url, base_name + '.war')
            self.extract_tar_war(temp_dir + '/' + base_name + '.war', base_name, temp_dir)
        else:
            print base_name + '项目不存在'

    def extract_tar_war(self, path, zipname, targetpath):
        if re.match(r'.*\.tar\.gz', path):
            # tar.gz
            print '路径：' + path
            t = tarfile.open(path)
            names = t.getnames()
            t.extractall(path=targetpath)
            for name in names:
                # .jar
                if name.find(zipname + '.jar') != -1:
                    self.unzip(name, targetpath)
            t.close()

        if re.match(r'.*\.war', path):
            servlet_jar = self.unzip(path, targetpath)
            if len(servlet_jar) > 0:
                map(lambda x: self.unzip(x, targetpath), servlet_jar)

    @staticmethod
    def downloadfile(file_url, targetname):
        print '下载文件:' + file_url
        f = urllib2.urlopen(file_url)
        data = f.read()
        with open(targetname, "wb") as code:
            code.write(data)
        print '下载完成'

    @staticmethod
    def unzip(filename, targetpath):
        servlet_jar = []
        r = zipfile.is_zipfile(filename)
        if r:
            z = zipfile.ZipFile(filename, mode='r')
            for warfile in z.namelist():
                if re.match(r'.*venus-.*-servlet-.*\.jar', warfile):
                    servlet_jar.append(targetpath + '/' + warfile)
                z.extract(warfile, targetpath)
            z.close()
        return servlet_jar
