#! /usr/bin/python3
from selenium import webdriver;
from selenium.webdriver.common.by import By; 
import time;
from save_data_to_file import save_file;

browser = webdriver.Chrome();
browser.get('https://www.epwk.com/task/');
input_search = browser.find_element(By.XPATH,'//div[@class="header-search-input"]//input[@name="k"]');
input_search.send_keys('python3爬虫');
button_search = browser.find_element(By.XPATH,'//*[@id="header-search"]//div[@class="f_l"]//button[@class="button red"]');
button_search.click();

moneys = browser.find_elements(By.XPATH,'//div[@class="task_class_list_li"]//div[@class="task_class_list_li_box"]//div[@class="wrid1"]//b[@class="red"]');
titles = browser.find_elements(By.XPATH,'//div[@class="task_class_list_li"]//div[@class="task_class_list_li_box"]//div[@class="wrid1"]//a[@urlshare="urlshare"]');
peoples = browser.find_elements(By.XPATH,'//div[@class="task_class_list_li"]//div[@class="task_class_list_li_box"]//div[@class="wrid1"]//samp[@class="c999"]');
status = browser.find_elements(By.XPATH,'//div[@class="task_class_list_li"]//div[@class="task_class_list_li_box"]//div[@class="wrid2"]');

datas = [];
for index in range(len(moneys)):
	data = '任务标题：'+titles[index].text+';\n';
	data += '金额：' + moneys[index].text + ';\n'; 
	data += '竞标情况：' + peoples[index].text.replace('\n','-') + ';\n'; 
	data += '任务状态：' + status[index].text.replace('\n','-') + ';\n'; 
	data += '详情查看：' + titles[index].get_attribute('href').replace('\n','-') + ';\n'; 
	if not status[index].text.startswith('直接雇佣'):
		datas.append(data);
#关闭浏览器	
browser.close();

save_file(datas,'txt','result.txt');

