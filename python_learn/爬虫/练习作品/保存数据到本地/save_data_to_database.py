#! /usr/bin/python3
import pymysql;
from redis import StrictRedis;
import chardet;#用于检验数据编码
import json;


#将结果写入MySQL数据库
def write_to_mysql(result):
	mysql = pymysql.connect(host = 'localhost',user = 'root',password = 'root',port = 3306);
	cursor = mysql.cursor();
	table = 'spiders_learn.popular_movies';
	keys = [];
	values = '';
	item_values = [];
	sql = '';
	update = '';
	try:
		for item in result:
			keys = item.keys();
			values = ','.join(['%s']*len(item));
			sql = 'insert into {table}({keys}) values({values}) on duplicate key update '.format(table = table,keys = ','.join(keys),values = values);
			update = ','.join(['{key} = %s'.format(key = k) for k in keys]);
			sql += update;
			item_values = [];	
			for k in keys:
				item_values.append(item[k]);
			item_values = tuple(item_values);
			if cursor.execute(sql,item_values*2):
				print('保存成功');
		mysql.commit();
	except Exception as e:
		print('系统异常');
		print(e);
		mysql.rollback();
	mysql.close();

#保存数据到redis数据库
def write_to_redis(result):
	redis = StrictRedis(host = 'localhost',port = 6379,db = 0,password = 'root');
	redis.set('popular_movies',json.dumps(result,ensure_ascii = False));
	print('保存成功');

# 保存数据到数据库
# model是数据库类别，其值可以是'mysql','redis';
def save_data(result,model):
	try:
		if model == 'mysql':
			write_to_mysql(result);
		elif model == 'redis':
			write_to_redis(result);
		else :
			print('请输入正确的数据库类别(目前仅支持mysql,redis)');
			return;
		print('成功保存到' + model + '数据库');
	except Exception as e:
		print('保存失败');
		print(e);

