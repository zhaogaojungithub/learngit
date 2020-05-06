#! /usr/bin/python3
import requests;
from pyquery import PyQuery as pq;
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

#通过BeautifulSoup模块提取有用信息
def parse_one_page(text):
	doc = pq(text);
	indexs = doc('i')('.board-index').text();
	indexs = indexs.split(' ');
	img_tags = doc('img')('.board-img');
	img_srcs = [];
	for item in img_tags.items():
		img_srcs.append(item.attr('data-src'));
	names = doc('p')('.name').text();
	names = names.split(' ');
	actor_tags = doc('p')('.star');
	actors = [];
	for item in actor_tags.items():
		actors.append(item.text()[3:] if (len(item.text()) > 3) else '');
	time_tags = doc('p')('.releasetime');
	times = [];
	for item in time_tags.items():
		times.append(item.text()[5:] if (len(item.text()) > 5) else '');
	score_tags_integer = doc('p')('.score')('i')('.integer').text();
	score_tags_fraction = doc('p')('.score')('i')('.fraction').items();
	scores = score_tags_integer.split(' ');
	index = 0;
	for item in score_tags_fraction:
		scores[index] += item.text();
		index += 1;
	del index;
	for index in range(len(indexs)):
		yield {
			'ranking':indexs[index],
			'img_src':img_srcs[index],
			'name':names[index].strip(),#去除两边空格
			'actor':actors[index],
			'time':times[index],
			'score':scores[index]
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






