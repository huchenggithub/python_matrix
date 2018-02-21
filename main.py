#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Newton_apple time:2018/2/19

import excel
import matrix

# 读取excle表格里的数据，生成矩阵
exc = excel.Excel()
mr = exc.get_matrix()

matr = matrix.MatRix(mr)
matr.get_rank()
matr.get_size()
