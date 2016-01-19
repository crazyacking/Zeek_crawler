# import os
# from urllib.request import urlopen
#
# import bs4
# from bs4 import BeautifulSoup
#
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# file=open(r'/home/crazyacking/Code_Fantasy/Zeek_crawler/webfile/cnblogs.html','r',1)
# html=file.read()
# # print(html)
#
# soup = BeautifulSoup(html, "lxml")
# urllib=urlopen('www.baidu.com')
# print(type(urllib))
# print(soup.prettify())
# print(soup.head)
# print(soup.head)
# print(type(soup.a))
# print(soup.name)
# print(soup.head.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.p.get('class'))
# soup.p['class']='newClass'
# print(soup.p)
# print(soup.p['name'][:])
# print(soup.p)

# print(soup.p)
# print(soup.p.string)
# print(type(soup.p.string))
# print(type(soup.name))
# print(soup.name)
# print(soup.attrs)

# print(soup.a)
# print(soup.a.string)
# print(type(soup.a.string))
# if type(soup.a.stirng)==bs4.element.Comment:
#     print(soup.a.string)
#     print('faf')

# print(soup.head.contents)
# print(type(soup.head.contents))
# print(soup.head.children)
# for child in soup.p.children:
#     print(child)

# for child in soup.descendants:
#     print(child)

# for string in soup.strings:
#     print(repr(string))

# for string in soup.stripped_strings:
#     print(string)

# pp=soup.p
# print(pp.parent.name)
# bb=pp.parent.name

# content =soup.head.title.string
# for parent in content.parents:
#     print(parent.name)

# print(soup.p.next_sibling.next_sibling)

# find_all(name,attrs,)


# with open(r'/home/crazyacking/Code_Fantasy/Zeek_crawler/webfile/cnblogs.html','r',1) as input_file:
    # content=input_file.read()
    # print(input_file.readline())
    # for i in range(10):
    #     print(i,input_file.readline(),end='')


