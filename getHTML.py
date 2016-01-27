#!/url/bin/env python
# -*- coding:utf-8 -*-
__author__='crazyacking'

import os,re,codecs,urllib
from urllib import request
from bs4 import BeautifulSoup

class getHTML(object):
    # open web page
    def getUrl(self,url,coding='utf-8'):
        req=request.request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
        with request.urlopen(req) as response:
            return BeautifulSoup(response.read().decode(coding))


    #storage text to locale
    def saveText(self,filename,content,mode='w'):
        self._checkPath(filename)
        with codecs.open(filename,encoding='utf-8',mode=mode)as f:
            f.write(content)

    # save image
    def saveImg(self,imgUrl,imgName):
        data=request.urlopen(imgUrl).read()
        self._checkPath(imgName)
        with open(imgName,'wb') as f:
            f.write(data)

    #create dir folder
    def _checkPath(self,path):
        dirname=os.path.dirname(path.strip())
        if not os.path.exists(dirname):
            os.makedirs(dirname)
