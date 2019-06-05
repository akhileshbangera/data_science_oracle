import numpy as np

def cal_median(num_list):
    list_len = len(num_list)
    np.sort(num_list)
    mid_point = int(list_len/2)
    if list_len%2 != 0:
        print(num_list[round(mid_point)])
    else:
        median = (num_list[mid_point] + num_list[mid_point-1])/2
        print(median)

int_list= []
my_array = np.array([])
n = int(input())

for i in range(n):

    num = int(input())

    int_list.extend([num])
    my_array = np.array(int_list)
    

    cal_median(int_list)