#!/bin/bash
#个人练习脚本
name="zgj";
echo "hello ${name}";

echo 'hello '$name'';

echo "该字符串的长度是：${#name} ";

string="zhaogaojun";
echo ${string:4:6};

echo "字母g首次出现的位置是:" `expr index "${string}" g`;

array=(1 2 3);
echo "数组array的第二个元素是："${array[1]};

echo "数组array的所有元素是:" ${array[@]};

echo "数组的长度是:" ${#array[@]};

echo "数组array的第一个元素的长度是:" ${#array[2]};
