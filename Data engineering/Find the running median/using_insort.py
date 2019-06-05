#Bisect algorithm is used to find a position in list where an element needs to be inserted to keep the list sorted.
from bisect import insort

#method to find the median of a sorted list
def cal_median(num_list):
    list_len = len(num_list)
    
    mid_point = int(list_len/2)
    # if the Odd length list
	if list_len%2 != 0:
        print(num_list[round(mid_point)])
    
	# if the even length list
	else:
        median = (num_list[mid_point] + num_list[mid_point-1])/2.0
        print(median)

#list
int_list= []
#input the size of a list
n = int(input()) 

#input the size of a list
for i in range(n):
    num = float(input())
	
	# New element is inserted into the list using insort method, which keeps the list sorted.
    insort(int_list,num)
	
	#pass the sorted list to the "cal_median" method to print the median of the list
    cal_median(int_list)