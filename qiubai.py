# -*- coding:utf-8 -*-
import sys,os,pdb,re,time,random
from spider import SpiderHTML
from bs4 import BeautifulSoup

class QiubaiSpider(SpiderHTML):
	def __init__(self,contentType,pageStart=1, pageEnd=1):
		#super.__init__(self)
		self._contentType = contentType
		self._pageStart = int(pageStart)
		self._pageEnd = int(pageEnd)+1
		self.__url = {'new':'http://www.qiushibaike.com/textnew/page/','hot':'http://www.qiushibaike.com/text/page/'}

	def getJokes(self):
		reqUrl = ''

		if contentType in self.__url:
			reqUrl = self.__url[self._contentType]
		else:
			reqUrl = self.__url['new']
		for i in range(self._pageStart,self._pageEnd):
			pageUrl = reqUrl+str(i)+'/'
			jokes = self.getUrl(pageUrl)
			jokes = jokes.find_all('div',id=re.compile('qiushi_tag_\d+'))
			filepath = os.path.join('E:\\','qiubai','page_'+self._contentType+str(i))
			info = '���ڱ����{page}ҳ�����µ��ļ� {file}.txt'
			print(info.format(page=i,file=filepath))
			for joke in jokes:
				jokeContent = str(joke.find('div',attrs={'class':'content'}))
				jokeContent = re.sub('<div class="content">','',jokeContent)
				jokeContent = re.sub('</div>','',jokeContent)
				jokeContent = re.sub('<!--\d+-->','',jokeContent)
				jokeContent = re.sub('<br>','\n',jokeContent)
				jokeContent = re.sub('<br/>','\n',jokeContent)
				try:
					author = joke.find(attrs={'class':'author clearfix'}).find('h2').string
					upvote = joke.find(attrs={'class':'stats'}).span.i.string
				except AttributeError:
					pass

				joke = '-----------------------------\r\n���ߣ�{author}\r\n{joke}\r\n\r\n{upvote}�˾��ú���\r\n'.format(joke=jokeContent.strip(),author=author,upvote=upvote)
				
				self.saveText(filepath+'.txt',joke,'a')
			if i%2 == 0:		#��ֹ���⣬���ʱ�䳤һ��
				time.sleep(random.random()*3)

if __name__ == '__main__':
	contentType = 'new'
	page = 0
	paramsNum = len(sys.argv)

	#�������ȡ���µ��ܰٻ������ȵ��ܰ�
	#����2,3Ϊ��Ҫ��ȡ��ҳ��
	if paramsNum>=4:
		contentType = sys.argv[1]
		page = sys.argv[2]
		pageEnd = sys.argv[3]
	elif paramsNum>=3:
		contentType = sys.argv[1]
		page = sys.argv[2]
		pageEnd = page
	elif paramsNum == 2:
		contentType = sys.argv[1]
		page,pageEnd = 1,1
	else:
		contentType = 'new'
		page,pageEnd = 1,1

	qiubai = QiubaiSpider(contentType,page,pageEnd)
	qiubai.getJokes()