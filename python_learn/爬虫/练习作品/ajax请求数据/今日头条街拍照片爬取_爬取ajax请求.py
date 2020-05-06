#! /usr/bin/python3
import requests;
import os;
from urllib.parse import urlencode;


# 从今日头条街拍页面爬取ajax请求获取的街拍照片
# offset是分页显示的偏移量
def get_one_page(offset):
	print('开始');
	params = {
		'offset':offset,
		'format':'json',
		'keyword':'街拍',
		'autoload':'true',
		'count':'20',
		'cur_tab':'1',
		'app_name':'web_search',
		'aid':'24',
		'en_qc':'1',
		'from':'search_tab',
		'pd':'synthesis'
	};
	headers = {
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
		'cookie':'tt_webid=6821153415981975048; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6821153415981975048; csrftoken=4322cefe682ef68d967af21aa847a05c; ttcid=3be34fe6ba8c4a4aa8ddc0b0cadca1a338; SLARDAR_WEB_ID=9aa1ec5c-61a5-41e6-8cac-14eca9ce3f95; s_v_web_id=verify_k9meawak_uc8oC8Hy_gbE0_4kz7_AvrG_6dSOjxTfxCW0; tt_scid=hPLs-OmQZtSD75mvrs7wkcey.5.uSZtlcgUs2c.AoH32eYlhmxu5PZmxhV.-gf3U0cb3'
	};
	url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params);
	try:
		response = requests.get(url,headers = headers);
		if response.status_code == 200:
			return response.json();
	except Exception as e:
		print('异常');
		print(e);
		return None;


# 从结果中解析出图片地址和图片标题
def get_imgurl_and_title_from_response(response):
	if response.get('data'):
		for item in response.get('data'):
			title = item.get('title');
			images = item.get('image_list');
			yield {
				'title':title,
				'images':images
			};


# 先根据结果中的title字段建立文件夹，
# 然后将图片保存到相应的文件夹下
def save_image(item):
	if not os.path.exists('./今日头条街拍照片爬取结果/'):
		os.mkdir('今日头条街拍照片爬取结果');
	if not item.get('title'):
		return;
	if not os.path.exists('./今日头条街拍照片爬取结果/' + item.get('title')):
		os.mkdir('今日头条街拍照片爬取结果/' + item.get('title'));
	try:
		index = 1;
		for image in item.get('images'):
			if image.get('url'):
				response = requests.get(image.get('url'));
				if response.status_code == 200:
					file_path = './今日头条街拍照片爬取结果/{0}/{1}.{2}'.format(item.get('title'),item.get('title')+str(index),'jpg');
					print('正在保存:\n'+file_path);
					if not os.path.exists(file_path):
						with open(file_path,'wb') as f:
							f.write(response.content);
							index += 1;
					else:
						print('该文件已下载: '+image.get('url'));
	except Exception as e:
		print('下载图片异常');
		print(e);

def main(offset):
	response = get_one_page(offset);
	data = get_imgurl_and_title_from_response(response);
	for item in data:
		save_image(item);
	

main(0);
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
