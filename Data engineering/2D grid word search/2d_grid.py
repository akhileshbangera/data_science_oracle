def check_word_exists(grid,word,cols,rows,i, j,index):

    if index >= len(word):
        return False

    if ( i < 0 or j < 0 or i >= cols or j >= rows ):
        return False
  
    if word[index] == grid [i][j]:

        if index == len(word)-1:
            return True
       
        result = (check_word_exists(grid,word,cols,rows,i+1,j,index+1)|
                  check_word_exists(grid,word,cols,rows,i-1,j,index+1)|
                  check_word_exists(grid,word,cols,rows,i,j+1,index+1)|
                  check_word_exists(grid,word,cols,rows,i,j-1,index+1))

        return result
    
    else:
        return False

grid = ['axmy', 'bgdf','xeet','raks']
word = 'geek'
rows = 4
cols = 4
is_found = []

for i in range(rows):
    
    for j in range(cols):
        
        if word[0] == grid[i][j]:
            
            if index_found and check_word_exists(grid,word,cols,rows,i,j, 0):
                is_found.extend(['Yes'])
            else:
                is_found.extend(['No'])
                
               
if 'Yes' in is_found:
    print('Yes')
else:
    print('No')