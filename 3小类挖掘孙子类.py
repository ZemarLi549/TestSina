import  urllib
import urllib.request
import lxml
import lxml.etree

url="http://news.sina.com.cn/china/"
data=urllib.request.urlopen(url).read().decode("utf-8")
print(data)
mytree=lxml.etree.HTML(data)
links=mytree.xpath('//div[@id="subShowContent1_static"]//*')
print(links)
for line in links:
    print(line.xpath("./h2/a/@href"),line.xpath(".h2/a/text()"))

