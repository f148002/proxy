from lxml import etree
import re

html = etree.parse(r'C:\Users\f1480\Desktop\Proxylist\tmph3fc9_58.html',etree.HTMLParser())
# result = html.xpath('//tr/td/text()')#'//'表示获取当前节点子孙节点，'*'表示所有节点，'//*'表示获取当前节点下所有节点

item = []
ip_list = html.xpath('//tr/td[2]/text()')
port_list=html.xpath('//tr/td[3]/text()')

for i in range(0,len(ip_list)):
    item.append(ip_list[i] + ':' + port_list[i])

for i in item:
    print(i)

# for li in mian:
#     # 找到ip地址
#     print('ip:'+li)
    # # 找到端口：
    # port = li.xpath("/td[3]/text()")[0]
    # print('port:'+port)
    # 将两者连接，并返回给item处理
    # item['addr'] = ip + ':' + port

# for i in item:
#     print(i)

# list1 = html.xpath("//tr")
#
# for item in list1[0]:
#     a = item.xpath("//td[2]/text()")
#     print(a)

# list2 = list1.xpath("//td[2]/text()")
# for i in list2:
#     print(i)

# for node in list1:
#     ip = node.xpath("//td[2]/text()")
#     #     # if paiming is None:
#     #     continue
#     print(ip)
#     # link = node.xpath("./td[@class='team']/a/@href").extract_first()



# for item in mian:
#     match_ip = '((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}'
#     match_port = '([0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{4}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])'
#     if re.search(match_ip,item):
#         print(item)
#     if re.search(match_port, item):
#         print(item)


# for li in mian:
#     # 找到ip地址
#     ip = li.xpath('/td').extract()[1]
#     # 找到端口：
#     port = li.xpath('/td/text()')
#     # 将两者连接，并返回给item处理
#     item['addr'] = ip + ':' + port

#
# for i in item:
#     print(i)