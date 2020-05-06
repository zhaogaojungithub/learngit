#!/bin/bash
echo "请输入第一个数：";
read x;
echo "请输入第二个数：";
read y;
echo "两数之和是:";
z=`expr $x + $y`;
echo ${z};
