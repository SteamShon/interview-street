#! /usr/bin/python
from random import random
from math import log, ceil
P = 0.5
"""
SKIP LIST
ftp://ftp.cs.umd.edu/pub/skipLists/skiplists.pdf

naive implementation for basic indexable skip list
and running median using it
"""
class Node(object):
	def __init__(self, value, forward, width):
		self.value, self.forward, self.width = value, forward, width

class EndNode(object):
	def __cmp__(self, other):
		return 1

class SkipList:
	def __init__(self, N=1000):
		self.size = 0
		self.max_levels = int(1 + log(N, 2))
		self.head = \
		Node('Head', [Node(EndNode(), [], [])] * self.max_levels, \
		[1] * self.max_levels)
	
	def find(self, ith):
		node = self.head
		ith += 1
		for level in reversed(range(self.max_levels)):
			while node.width[level] < ith:
				ith -= node.width[level]
				node = node.forward[level]
		return node.value
	
	def insert(self, value):
		visited = [None] * self.max_levels
		steps = [0] * self.max_levels
		node = self.head
		
		for level in reversed(range(self.max_levels)):
			while node.forward[level].value <= value:
				node = node.forward[level]
				steps[level] += node.width[level]
			visited[level] = node
		# now node.forward[0] > value
		height = 1
		while random() < P and height < self.max_levels:
			height += 1

		new_node = Node(value, [None] * height, [None] * height)
		st = 0
		for h in range(height):
			prev_node = visited[h]
			new_node.forward[h] = prev_node.forward[h]
			prev_node.forward[h] = new_node
			new_node.width[h] = prev_node.width[h] - st
			prev_node.width[h] = st + 1
			st += steps[h]
		for h in range(height, self.max_levels):
			visited[h].width[h] += 1
		self.size += 1
		return True

	def remove(self, value):
		visited = [None] * self.max_levels
		node = self.head
		for level in reversed(range(self.max_levels)):
			while node.forward[level].value < value:
				node = node.forward[level]
			visited[level] = node
		# remove only when we found value
		if visited[0].forward[0].value != value:
			return False
		# remove
		next_height = len(visited[0].forward[0].forward)
		for h in range(next_height):
			prev_node = visited[h]
			prev_node.width[h] += prev_node.forward[h].width[h] - 1
			prev_node.forward[h] = prev_node.forward[h].forward[h]
		for h in range(next_height, self.max_levels):
			visited[h].width[h] -= 1
		self.size -= 1
		return True

	def __iter__(self):
		node = self.head.forward[0]
		while node is not Node(EndNode(), [], []) and len(node.forward) > 0:
			yield node.value
			node = node.forward[0]

if __name__ == "__main__":
	lt = SkipList()
	# running median
	N = int(raw_input())
	s, x = [], []
	for i in range(N):
		tmp = raw_input()
		a, b = [xx for xx in tmp.split(' ')]
		b = int(b)
		s.append(a)
		x.append(b)
		if a == "a":
			lt.insert(b)
		elif a == "r":
			if lt.remove(b) == False:
				print "Wrong!"
				continue
		if lt.size == 0:
			print "Wrong!"
		else:
			sz = lt.size - 1
			if sz % 2 == 1:
				print (lt.find(sz / 2 + 1) + lt.find(sz / 2 + 2)) / 2.0
			else:
				print lt.find(sz / 2 + 1)
