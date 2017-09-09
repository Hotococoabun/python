# include <stdio.h>
# 我不需要女朋友
# 2017年9月9日 21:42:05

import requests
from lxml import etree

def ip138(number):
    '''ip138.com'''
    url = 'http://www.ip138.com:8080/search.asp?action=mobile&mobile='+str(number)
    r = requests.get(url )
    r.encoding = 'gbk'
    t = etree.HTML(r.text)
    data = t.xpath("//tr[@class='tdc' and @bgcolor]")[1:]
    s = 'ip138:\n'
    # print (len(data))
    # print (r.text)
    for x in data:
        text = x.xpath('./td/text()')
        s += text[0] + ' : ' + text[1] + '\n'
    return s + '\n'


def supfree(number):
    '''shouji.supfree.net'''
    r = requests.get('http://shouji.supfree.net/fish.asp?cat='+str(number))
    r.encoding = 'gbk'
    t = etree.HTML(r.text)
    response_number = t.xpath('//div[@class="entry"]/div[@class="cdiv"]/h2/text()')[0]
    data = t.xpath('//div[@class="entry"]/div[@class="cdiv"]/p')[:6]
    s = 'supfree:\n手机号: %s\n' % response_number
    data.pop(1)
    for x in [d.xpath('string(.)')+'\n' for d in data]:
        s += x
    return s + '\n'

def best(number):
    '''114best.com'''
    r = requests.get('http://www.114best.com/dh/114.aspx?w='+str(number))
    t = etree.HTML(r.text)#.xpath('//div[@id="detail"]')
    response_number = t.xpath('/html/body/div[4]/div/div[1]/table/tbody/tr[1]/td[2]/text()')[0].replace('\r\n','').replace(' ', '')
    s = '114best:\n查询的电话号码: {}\n'.format(response_number)
    s += "归属地自己打开 我不行了  --> http://www.114best.com{}\n".format(t.xpath('//span[@id="span_gsd"]/img/@src')[0])
    s += t.xpath('//div[@id="detailTitle"]/text()')[0]
    for x in t.xpath('//div[@id="detail"]/p'):
        s += x.xpath('./text()')[0] + ' '
    s += '\n'
    return s



if __name__ == '__main__':
    n = input('请输入要查询的号码: ')
    print ("\n", ip138(n), supfree(n), best(n))
