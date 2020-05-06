#! /usr/bin/python3
import requests;
import re;
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

#用于通过正则表达式解析结果
def parse_one_page(html):
	pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S);
	items = re.findall(pattern,html);
	for item in items:
		yield {
			'ranking':item[0],
			'img_src':item[1],
			'name':item[2].strip(),#去除两边空格
			'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
			'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
			'score':item[5].strip() + item[6].strip()
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








