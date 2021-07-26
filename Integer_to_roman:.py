class Solution:
    def intToRoman(self, num: int) -> str:

        string = str(num)
        initial_array = [char for char in string]
        array = [int(numeric_string) for numeric_string in initial_array]
        
        decimal_places = len(array) ##decimal_places will be max 4
        roman_arr = [None] * decimal_places

        flag = 0 ##FOR ENTERING DIFFERENT DECIMAL LEVELS
        
        if decimal_places == 1:
            if array[0] == 1 or array[0] == 2 or array[0] == 3:
                roman_arr[0] = 'I'* array[0] 
            elif array[0] == 4:
                roman_arr [0] = 'IV'
            elif array[0] == 5:  
                roman_arr [0] ='V'
            elif array[0] == 6 or array[0] ==  7 or array[0] ==  8:
                roman_arr [0] = 'V' + 'I'* (array[0]-5)
            else:
                roman_arr[0] = 'IX'
        
        elif decimal_places == 2:
            for i in range(0,1):
                if flag == 0:
                    if array[1] == 1 or array[1] == 2 or array[1] == 3:
                        roman_arr[1] = 'I'* array[1] 
                        flag = 1
                    elif array[1] == 4:
                        roman_arr [1] = 'IV'
                        flag = 1
                    elif array[1] == 5:  
                        roman_arr[1] ='V'
                        flag = 1
                    elif array[1] == 6 or array[1] ==  7 or array[1] ==  8:
                        roman_arr [1] = 'V' + 'I'* (array[1]-5)
                        flag = 1
                    elif array[1] == 0:
                        roman_arr[1] = ''
                        flag = 1
                    else:
                        roman_arr[1] = 'IX'
                        flag = 1

                if flag == 1:
                    ##CASA2:
                    if array[0] == 1 or array[0] == 2 or array[0] == 3:
                        roman_arr[0] = 'X' * array[0] 
                        print(roman_arr)
                    elif array[0] == 4:
                        roman_arr[0] = 'XL'
                    elif array[0] == 5:
                        roman_arr[0] = 'L'
                    elif array[0] == 6 or array[0] == 7 or array[0] == 8:
                        roman_arr[0] = 'L' + 'X'*(array[0]-5)
                    elif array[0] == 0:
                        roman_arr[1] = ''
                    else:
                        roman_arr[0] = 'XC'
                        
        elif decimal_places == 3:
            for i in range(0,2):
                if flag == 0:
                    if array[2] == 1 or array[2] == 2 or array[2] == 3:
                        roman_arr[2] = 'I'* array[2] 
                        flag = 1
                    elif array[2] == 4:
                        roman_arr [2] = 'IV'
                        flag = 1
                    elif array[2] == 5:  
                        roman_arr[2] ='V'
                        flag = 1
                    elif array[2] == 6 or array[2] ==  7 or array[2] ==  8:
                        roman_arr [2] = 'V' + 'I'* (array[2]-5)
                        flag = 1
                    elif array[2] == 0:
                        roman_arr[2] = ''
                        flag = 1
                    else:
                        roman_arr[2] = 'IX'
                        flag = 1

                if flag == 1:
                    ##CASA2:
                    if array[1] == 1 or array[1] == 2 or array[1] == 3:
                        roman_arr[1] = 'X' * array[1] 
                        flag = 2
                    elif array[1] == 4:
                        roman_arr[1] = 'XL'
                        flag = 2
                    elif array[1] == 5:
                        roman_arr[1] = 'L'
                        flag = 2
                    elif array[1] == 6 or array[1] == 7 or array[1] == 8:
                        roman_arr[1] = 'L' + 'X'*(array[1]-5)
                        flag = 2
                    elif array[1] == 0:
                        roman_arr[1] = ''
                        flag = 2
                    else:
                        roman_arr[1] = 'XC'
                        flag = 2
                        
                if flag == 2:
                    ##CASA3:
                    if array[0] == 1 or array[0] == 2 or array[0] == 3:
                        roman_arr[0] = 'C' * array[0] 
                    elif array[0] == 4:
                        roman_arr[0] = 'CD'
                    elif array[0] == 5:
                        roman_arr[0] = 'D'
                    elif array[0] == 6 or array[0] == 7 or array[0] == 8:
                        roman_arr[0] = 'D' + 'C'*(array[0]-5)
                    elif array[0] == 0:
                        roman_arr[0] = ''
                    else:
                        roman_arr[0] = 'CM'
                        
        elif decimal_places == 4:
            for i in range(0,3):
                if flag == 0:
                    if array[3] == 1 or array[3] == 2 or array[3] == 3:
                        roman_arr[3] = 'I'* array[3] 
                        flag = 1
                    elif array[3] == 4:
                        roman_arr [3] = 'IV'
                        flag = 1
                    elif array[3] == 5:  
                        roman_arr[3] ='V'
                        flag = 1
                    elif array[3] == 6 or array[3] ==  7 or array[3] ==  8:
                        roman_arr [3] = 'V' + 'I'* (array[3]-5)
                        flag = 1
                    elif array[3] == 0:
                        roman_arr[3] = ''
                        flag = 1
                    else:
                        roman_arr[3] = 'IX'
                        flag = 1

                if flag == 1:
                    ##CASA2:
                    if array[2] == 1 or array[2] == 2 or array[2] == 3:
                        roman_arr[2] = 'X' * array[2] 
                        flag = 2
                    elif array[2] == 4:
                        roman_arr[2] = 'XL'
                        flag = 2
                    elif array[2] == 5:
                        roman_arr[2] = 'L'
                        flag = 2
                    elif array[2] == 6 or array[2] == 7 or array[2] == 8:
                        roman_arr[2] = 'L' + 'X'*(array[2]-5)
                        flag = 2
                    elif array[2] == 0:
                        roman_arr[2] = ''
                        flag = 2
                    else:
                        roman_arr[2] = 'XC'
                        flag = 2
                        
                if flag == 2:
                    ##CASA3:
                    if array[1] == 1 or array[1] == 2 or array[1] == 3:
                        roman_arr[1] = 'C' * array[1] 
                        flag = 3
                    elif array[1] == 4:
                        roman_arr[1] = 'CD'
                        flag = 3
                    elif array[1] == 5:
                        roman_arr[1] = 'D'
                        flag = 3
                    elif array[1] == 6 or array[1] == 7 or array[1] == 8:
                        roman_arr[1] = 'D' + 'C'*(array[1]-5)
                        flag = 3
                    elif array[1] == 0:
                        roman_arr[1] = ''
                        flag = 3
                    else:
                        roman_arr[1] = 'CM'
                        flag = 3
            
                if flag == 3:
                        ##CASA4:
                        if array[0] == 1 or array[0] == 2 or array[0] == 3:
                            roman_arr[0] = 'M' * array[0] 
                        
        ###TO GET FROM ARRAY TO STRING. HAVE TO PRINT IT BACKWARDS!
        final_roman = ''
        counter = decimal_places -1
        print(roman_arr)    
        if roman_arr[0] == 'X' and len(roman_arr) == 1:
            final_roman = roman_arr[0]
        
        elif roman_arr[0] == 'C' and len(roman_arr) == 1:
            final_roman = roman_arr[0]
        
        elif roman_arr[0] == 'M' and len(roman_arr) == 1:
            final_roman = roman_arr[0]
        
        else:
            while counter >= 0:
                final_roman = roman_arr[counter] + final_roman 
                counter = counter -1
        
        return(final_roman)
        
        

