#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Newton's apple    time:2018/2/19
# 科学计算  矩阵

import numpy as np


class MatRix:
	def __init__(self, mat_rix):
		self.mat_rix = mat_rix

	def get_size(self):
		"""获取矩阵的大小，并转化成习惯的方式输出"""
		shape = self.mat_rix.shape        # 是元组对象
		size = str(shape[0]) + ' X ' + str(shape[1])
		print('矩阵的大小是： %s' % size)
		return size

	def get_row(self, row):
		"""获取矩阵的某一行"""
		r = self.mat_rix[row]
		print('第%s行是：%s' % (row, r))
		return r

	def get_column(self, column):
		"""获取矩阵的某一列"""
		c = self.mat_rix[:, column].reshape(-1, 1)
		print('第%s列是：\n %s' % (column, c))
		return c

	def juge(self):
		"""判断是否为方阵"""
		s = self.mat_rix.shape
		if s[0] == s[1]:
			return True
		else:
			return False

	def get_trace(self):
		"""求迹"""
		if self.juge():
			the_trace = np.trace(self.mat_rix)
			print('%s的迹是： %s' % (self.mat_rix, the_trace))
			return the_trace
		else:
			print('不是方阵，不能求迹')

	def get_det(self):
		"""求行列式"""
		if self.juge():
			the_det = np.linalg.det(self.mat_rix)
			print('%s的行列式是： %s' % (self.mat_rix, the_det))
			return the_det
		else:
			print('不是方阵，不能求行列式')

	def get_rank(self):
		"""求矩阵的秩"""
		if self.juge():
			the_rank = np.linalg.matrix_rank(self.mat_rix)
			print('%s的秩是： %s' % (self.mat_rix, the_rank))
			return the_rank
		else:
			print('不是方阵，不能求秩')


if __name__ == '__main__':
	s = '1 2 ; 8 9  '
	b = np.matrix(s)
	print(b)
	a = np.matrix('1 2 3; 4 5 6; 7 5 9')
	matr = MatRix(a)
	matr.get_size()
	matr.get_column(2)
	matr.get_row(1)
	matr.get_trace()
	matr.get_det()
	matr.get_rank()
