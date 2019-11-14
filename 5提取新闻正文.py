import  urllib
import urllib.request
import lxml
import lxml.etree

url="http://news.sina.com.cn/o/2017-10-25/doc-ifymzksi1619274.shtml"
data=urllib.request.urlopen(url).read().decode("utf-8")
mytree=lxml.etree.HTML(data)
title=mytree.xpath("//h1[@id=\"artibodyTitle\"]/text()")
print(title)
content=mytree.xpath("//div[@id=\"artibody\"]//p/text()")
for line in content:
    print(line)

