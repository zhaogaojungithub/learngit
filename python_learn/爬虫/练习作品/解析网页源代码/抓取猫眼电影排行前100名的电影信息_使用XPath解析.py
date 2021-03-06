#! /usr/bin/python3
import requests;
from lxml import etree;
import json;
from requests.exceptions import RequestException;
import time;
from save_data_to_file import save_file;
from save_data_to_database import save_data;

#用于爬取url指定的资源
def get_one_page(url):
	try:
		headers = {
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
		};
		response = requests.get(url,headers = headers);
		if response.status_code == 200:
			return response.text;
		return None;
	except RequestException as e:
		print(e);
		return None;

#通过lxml模块提取有用信息
def parse_one_page(text):
	html = etree.HTML(text);
	#获取电影排名信息	
	indexs = html.xpath('//dd/i/text()');
	#获取电影封面图片地址
	img_srcs = html.xpath('//dd/a/img[2]/@data-src');
	#获取电影名称
	names = html.xpath('//dd//p[@class="name"]/a/text()');
	#获取电影主演
	actors = html.xpath('//dd//p[@class="star"]/text()');
	#获取上映时间
	times = html.xpath('//dd//p[@class="releasetime"]/text()');
	#获取电影评分
	integers = html.xpath('//dd//p[@class="score"]/i[1]/text()');
	points = html.xpath('//dd//p[@class="score"]/i[2]/text()');
	for index in range(10):
		yield {
			'ranking':indexs[index],
			'img_src':img_srcs[index],
			'name':names[index].strip(),#去除两边空格
			'actor':actors[index].strip()[3:] if len(actors[index]) > 3 else '',
			'time':times[index].strip()[5:] if len(times[index]) > 5 else '',
			'score':integers[index].strip() + points[index].strip()
		}

#获取一组标签的内容
#tag-->list，里面的元素是Tag对象
#attr-->string，标签元素需要获取的属性，'content'表示获取该标签的文本值
def get_values_from_tag(tag,attr):
	result = [];
	for item in tag:
		if attr == 'content':
			result.append(item.string);
		else:
			result.append(item[attr]);
	return result;

#主函数
def main(offset):
	url = 'http://maoyan.com/board/4?offset=' + str(offset);
	html = get_one_page(url);
	result = parse_one_page(html);
	results = [];
	for item in result:
		results.append(item);
	save_file(results,'txt','result.txt');	
	save_file(results,'json','result.json');	
	save_file(results,'csv','result.csv');
	save_data(results,'mysql');
	save_data(results,'redis');		
	
#当该模块自身在运行的时候执行的代码块
if __name__ == '__main__':
	for i in range(1):
		main(i*10);
		time.sleep(1);#防止反爬虫机制中访问过快的情况下拒绝服务的情况







