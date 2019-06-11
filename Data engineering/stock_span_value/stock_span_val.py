def get_span_val(stock_arr):
    total_days= len(stock_arr)
    span_values = [0]*total_days
    span_val = 1
    for i in range(0,len(stock_arr)):
        if i == 0:
            span_values[i] = 1
        else:
            curr_stock = stock_arr[i]
            for stock_val in stock_arr[0:i]:
                if stock_val < curr_stock:
                    span_val= span_val+1
            span_values[i] =  span_val  
            span_val = 1
    print(span_values)    
    
def main():
    stock_arr = list(map(int,input().split(',')))
    get_span_val(stock_arr)
    
main()    