# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 00:33:33 2016

@author: Vivek Patani
"""

from __future__ import print_function
# -*- coding: utf-8 -*-
import pickle
def nursery_process_data(path,filename):
    
    input_file = open(path+filename)
    unique_count = {}
    input_data = input_file.readlines()
    binary_mat= [ [ 0 for i in range(31) ] for j in range(1474) ]
    row_count = 0
    for each_line in input_data:
        each_word = each_line.split(",")
        col_count = 0
        print()
        for each in each_word:
            each = each.rstrip()
            each = int(each)
            if each in unique_count:
                unique_count[each] += 1
            else:
                unique_count[each] = 0

            if col_count == 0:
                print(col_count, end = " ")
                if each < 24:
                    binary_mat[row_count][0] = 1
                    col_count += 1
                elif each >= 24 and each <36:
                    binary_mat[row_count][1] = 1
                    col_count += 1
                elif each >= 36:
                    binary_mat[row_count][2] = 1
                    col_count += 1
                    
            elif col_count == 1:
                print(col_count, end = " ")
                if each == 1:
                    binary_mat[row_count][3] = 1
                    col_count += 1
                elif each == 2:
                    binary_mat[row_count][4] = 1
                    col_count += 1
                elif each == 3:
                    binary_mat[row_count][5] = 1
                    col_count += 1
                elif each == 4:
                    binary_mat[row_count][6] = 1
                    col_count += 1
                    
            #print(col_count, end = " ")
            elif col_count == 2:
                print(col_count, end = " ")
                if each == 1:
                    binary_mat[row_count][7] = 1
                    col_count += 1
                elif each == 2:
                    binary_mat[row_count][8] = 1
                    col_count += 1
                elif each == 3:
                    binary_mat[row_count][9] = 1
                    col_count += 1
                elif each == 4:
                    binary_mat[row_count][10] = 1
                    col_count += 1
                
            #print(col_count, end = " ")
            elif col_count == 3:
                print(col_count, end = " ")
                if each < 3:
                    binary_mat[row_count][11] = 1
                    col_count += 1
                elif each >= 3 and each <5:
                    binary_mat[row_count][12] = 1
                    col_count += 1
                elif each >= 5:
                    binary_mat[row_count][13] = 1
                    col_count += 1
                    
            
            elif col_count == 4:
                print(col_count, end = " ")                
                if each == 0:
                    #print(each)
                    binary_mat[row_count][14] = 1
                    col_count += 1
                elif each == 1:
                    binary_mat[row_count][15] = 1
                    col_count += 1
                    
            elif col_count == 5:
                if each == 0:
                    binary_mat[row_count][16] = 1
                    col_count += 1
                elif each == 1:
                    binary_mat[row_count][17] = 1
                    col_count += 1
                    
            elif col_count == 6:
                if each == 1:
                    binary_mat[row_count][18] = 1
                    col_count += 1
                elif each == 2:
                    binary_mat[row_count][19] = 1
                    col_count += 1
                elif each == 3:
                    binary_mat[row_count][20] = 1
                    col_count += 1
                elif each == 4:
                    binary_mat[row_count][21] = 1
                    col_count += 1
                    
            elif col_count == 7:
                print(col_count, end = " ")
                if each == 1:
                    binary_mat[row_count][22] = 1
                    col_count += 1
                elif each == 2:
                    binary_mat[row_count][23] = 1
                    col_count += 1
                elif each == 3:
                    binary_mat[row_count][24] = 1
                    col_count += 1
                elif each == 4:
                    binary_mat[row_count][25] = 1
                    col_count += 1
            
            elif col_count == 8:
                print(col_count, end = " ")
                if each == 0:
                    binary_mat[row_count][26] = 1
                    col_count += 1
                elif each == 1:
                    binary_mat[row_count][27] = 1
                    col_count += 1
                    
            elif col_count == 9:
                print(col_count, end = " ")
                if each == 1:
                    binary_mat[row_count][28] = 1
                    col_count += 1
                elif each == 2:
                    binary_mat[row_count][29] = 1
                    col_count += 1
                elif each == 3:
                    binary_mat[row_count][30] = 1
                    col_count += 1

            print(col_count,end = " ")
        row_count += 1
    print(row_count)
    with open("./data/cmc/output.csv", 'w') as f:
        for s in binary_mat:
            f.write(str(s))
            f.write("\n")
    with open("./data/cmc/data.p", "w") as pick:
        pickle.dump(binary_mat,pick)

def main():
    
    nursery_process_data("./input/cmc/","cmc.data")
    
if __name__ == "__main__":
    main()