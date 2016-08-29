# Your boss ask you to code a piece of code, such that for any 
# length list with floating or int type elements, your function
# can sort them from bigger to smaller.
#
# e.g. If your boss give a list:
#
#		[8,2,4,6,1,9,0,3,5,7],
#
# your function should return
#
#		[9,8,7,6,5,4,3,2,1,0],
#
#


def bubbleSort(list):
	length = len(list)
	for i in range(length - 1, 0, -1):
		for j in range(0, i):
			if list[j] < list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]

	return list


def selectionSort(list):
	length = len(list)
	for i in range(0, length - 1, 1):
		min_index = i
		for j in range(i + 1, length):
			if list[j] < list[min_index]:
				min_index = j

		if min_index != i:
			list[min_index], list[i] = list[i], list[min_index]

	return list


def insertSort(list):
	length = len(list)
	if length == 1:
		return list

	for i in range(1, length):
		temp = list[i]
		j = i - 1
		while j >= 0 and temp > list[j]:
			list[j + 1] = list[j]
			j -= 1

		list[j + 1] = temp

	return list


testlist = [8,2,4,6,1,9,0,3,5,7]
print('final:', insertSort(testlist))




