#! /usr/bin/python
"""
calculate all pair distance(O(N^2) failed because N is large).
I can`t prove that following approach is correct but at least it passed testcases.
O(N)

PASSED
1. find mean point(using arithmetic mean)
2. find center point which has minimum euclidian distance from mean point
3. calculate sum of distances from center point to others
"""
import math
def dist_euc(a, b):
	return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

def dist(a, b):
	return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
		
N = int(raw_input())
datas = []
x_sum, y_sum = 0, 0
for i in range(N):
	line = raw_input()
	x, y = line.split()
	x, y = int(x), int(y)
	datas.append((x, y))
	x_sum += x
	y_sum += y
mean = (x_sum / N, y_sum / N)
min_dist = dist_euc(mean, datas[0])
min_dist_idx = 0
for i in range(1, len(datas)):
	data = datas[i]
	d = dist_euc(mean, data)
	if min_dist > d:
		min_dist = d
		min_dist_idx = i
center = datas[min_dist_idx]
ret = 0
for i in range(len(datas)):
	if i == min_dist_idx: continue
	ret += dist(datas[i], center)

print ret
