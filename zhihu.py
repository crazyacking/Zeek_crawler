# -*- coding:utf-8 -*-

from spider import SpiderHTML
import sys,urllib,http,os,random,re,time
__author__ = 'crazyacking'
'''
ʹ���˵���������� BeautifulSoup4�������а�װ
��ҪĿ¼�µ�spider.py�ļ�
���л�����python3.4,windows7
'''

#�ղؼеĵ�ַ
url = 'https://www.zhihu.com/collection/69135664'  #page������Ϊ�������

#���ش�ŵ�·��,�����ڻ��Զ�����
store_path = 'E:\\zhihu\�ղؼ�\\�������ƵĴ������������'

class zhihuCollectionSpider(SpiderHTML):
	def __init__(self,pageStart, pageEnd, url):
		self._url = url
		self._pageStart = int(pageStart)
		self._pageEnd = int(pageEnd)+1
		self.downLimit = 0						#���ڴ���ͬ�Ĵ𰸲���¼

	def start(self):
		for page in range(self._pageStart,self._pageEnd):		#�ղؼе�ҳ��
			url = self._url + '?page='+str(page)
			content = self.getUrl(url)
			questionList = content.find_all('div',class_='zm-item')
			for question in questionList:						#�ղؼе�ÿ������
				Qtitle = question.find('h2',class_='zm-item-title')
				if Qtitle is None:								#����г��
					continue

				questionStr = Qtitle.a.string
				Qurl = 'https://www.zhihu.com'+Qtitle.a['href']	#������Ŀ
				Qtitle = re.sub(r'[\\/:*?"<>]','#',Qtitle.a.string)			#windows�ļ�/Ŀ¼����֧�ֵ��������
				print('-----���ڻ�ȡ����:'+Qtitle+'-----')		#��ȡ����������Ӻͱ��⣬����ץȡ
				Qcontent = self.getUrl(Qurl)
				answerList = Qcontent.find_all('div',class_='zm-item-answer  zm-item-expanded')
				self._processAnswer(answerList,Qtitle)						#��������Ĵ�
				time.sleep(5)


	def _processAnswer(self,answerList,Qtitle):
		j = 0			
		for answer in answerList:
			j = j + 1
			
			upvoted = int(answer.find('span',class_='count').string.replace('K','000')) 	#��ô˴���ͬ��
			if upvoted < 100:
				continue
			authorInfo = answer.find('div',class_='zm-item-answer-author-info')				#��ȡ������Ϣ
			author = {'introduction':'','link':''}
			try:
				author['name'] = authorInfo.find('a',class_='author-link').string 			#������ߵ�����
				author['introduction'] = str(authorInfo.find('span',class_='bio')['title']) #������ߵļ��
			except AttributeError:
				author['name'] = '�����û�'+str(j)
			except TypeError:  																#���Ϊ�յ����
				pass
	
			try:
				author['link'] = authorInfo.find('a',class_='author-link')['href']
			except TypeError:  																#�����û�û������
				pass
	
			file_name = os.path.join(store_path,Qtitle,'info',author['name']+'_info.txt')
			if os.path.exists(file_name):							#�Ѿ�ץȡ��
				continue
	
			self.saveText(file_name,'{introduction}\r\n{link}'.format(**author))			#�������ߵ���Ϣ
			print('���ڻ�ȡ�û�`{name}`�Ĵ�'.format(**author))
			answerContent = answer.find('div',class_='zm-editable-content clearfix')
			if answerContent is None:								#���ٱ����û�û�д�����
				continue
	
			imgs = answerContent.find_all('img')
			if len(imgs) == 0:										#��û����ͼ
				pass
			else:
				self._getImgFromAnswer(imgs,Qtitle,**author)


	#��¼ͼƬ
	def _getImgFromAnswer(self,imgs,Qtitle,**author):
		i = 0
		for img in imgs:
			if 'inline-image' in img['class']:					#��ץȡ֪����Сͼ
				continue
			i = i + 1
			imgUrl = img['src']
			extension = os.path.splitext(imgUrl)[1]
			path_name = os.path.join(store_path,Qtitle,author['name']+'_'+str(i)+extension)
			try:
				self.saveImg(imgUrl,path_name)					#�������ͼƬ�쳣�����̲��ж�
			except ValueError:									
				pass
			except urllib.error.HTTPError as e:
				pass
			except KeyError as e:
				pass
			except http.client.IncompleteRead:
				pass
	#��¼����
	def _getTextFromAnswer(self):
		pass

#����zhihu.py 1 5   ��ȡ1��5ҳ������
if __name__ == '__main__':
	page, limit, paramsNum= 1, 0, len(sys.argv)
	if paramsNum>=3:
		page, pageEnd = sys.argv[1], sys.argv[2]
	elif paramsNum == 2:
		page = sys.argv[1]
		pageEnd = page
	else:
		page,pageEnd = 1,1

	spider = zhihuCollectionSpider(page,pageEnd,url)
	spider.start()

