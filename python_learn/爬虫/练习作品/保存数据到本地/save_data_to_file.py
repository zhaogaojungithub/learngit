#! /usr/bin/python3
import json;
import csv;

#将结果写入txt文件
def write_to_txtfile(result,filepath):
	with open(filepath,'w',encoding='utf-8') as f:
		f.write(json.dumps(result,ensure_ascii = False) + '\n');

#将结果写入JSON文件
def write_to_jsonfile(result,filepath):
	with open(filepath,'w',encoding = 'utf-8') as f:
		#indent = 2表示缩进单位是2个空格
		#ensure_ascii = False表示关闭ascii编码，防止中文乱码
		f.write(json.dumps(result,indent = 2,ensure_ascii = False));

#将结果写入csv文件
def write_to_csvfile(result,filepath):
	with open(filepath,'w',encoding = 'utf-8') as f:
		fieldnames = ['ranking','name','actor','time','score','img_src'];
		writer = csv.DictWriter(f,fieldnames = fieldnames);
		writer.writeheader();
		writer.writerows(result);

# 根据model信息将result数据存到不同的文件中
# model的值可以是'txt'/'json'/'csv'
# filepath是文件路径
def save_file(result,model,filepath):
	try:
		if model == 'txt':
			write_to_txtfile(result,filepath);
		elif model == 'json':
			write_to_jsonfile(result,filepath);
		elif model == 'csv':
			write_to_csvfile(result,filepath);
		else :
			print('请输入正确的文件后缀（仅支持txt,json,csv）');
			return;
		print('成功保存到文件' + filepath);
	except Exception as e:
		print('保存文件失败');
		print(e);
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
	
