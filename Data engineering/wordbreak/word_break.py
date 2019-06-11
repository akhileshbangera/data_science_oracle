from string import ascii_lowercase

global word_dict

word_dict = { alphabet:[] for alphabet in ascii_lowercase }
dict = ['i','and', 'like','cherry','love' ,'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']

for word in dict:
    word_dict[word[0]].extend([word])

def print_possile_sentances(word_list,org_str):
    cpy_str = org_str
    
    for k in range(len(word_list)):
        new_str = ''
        org_str = cpy_str
        for recs in word_list[k]:
            
            if recs == org_str[0:len(recs)]:
                org_str = org_str[len(recs):]              
                new_str = new_str + recs + ' '

        if len(cpy_str) == len(new_str.replace(' ','')):

            print('Possible sentance:',new_str) 

def break_words_list(org_string):
    cr_string = ''
    word_len = 0
    matched = 0
    matched_words = [[]]
    temp_word_list =[]

    for i in range(0,len(org_string)):
        matched = 0
        first_letter = org_string[i]
        list_words = word_dict[first_letter]
       
        for word in list_words:

            word_len = len(word)
            if word == org_string[i:word_len+i] or word == org_string[i:word_len+1]:

                matched = matched + 1
               
                if matched > 1:

                    if len(matched_words) != matched:

                        temp_word_list = matched_words[matched-2][:]

                        temp_word_list.pop()

                        temp_word_list.extend([word])

                        matched_words.extend([temp_word_list])

                    else:               
                        matched_words[matched-1].extend([word])
                else:

                    for k in range(len(matched_words)):

                        matched_words[k].extend([word])

                cr_string = cr_string + word + ' '               
    #print('--------------------------------------------')
    #print('Sentence using matched words in dict:',cr_string)  
    #print('list of matched words:',matched_words)
    print_possile_sentances(matched_words,org_string)
    
test_str= 'ilovesamsung'

break_words_list(test_str)