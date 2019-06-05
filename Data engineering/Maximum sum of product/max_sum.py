#create a method to calcualte the max sum of contigious sub arrays
def maxSubArraySum(a,size):      
    #this logic is taken from  Kadane’s algorithm ,https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
    max_so_far = 0
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far

#create a method to calcualte the prodcut of contigious sub arrays
def cal_product(n,arr):
    product_arr = []
    for i in range(0,n):
        for j in range(i+1,n):
            product_arr.extend([(arr[i]*arr[j])])
    
    print(product_arr)
    print(maxSubArraySum(product_arr,len(product_arr)))   

#input the array size
n = int(input())
# input the array with size n
arr = list(map(int,input().strip().split(' ')))
cal_product (n,arr)