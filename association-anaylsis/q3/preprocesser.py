"""
Created on Sun Apr 03 19:58:24 2016

@author: Vivek Patani
"""
import json

#-*- coding:utf-8 - *-

def load_raw_data(path,filename,extension,destination):
    
    input_file = open(path+filename+extension)
    lines = input_file.readlines()
    list_categories = []
    sparse_mat = []
    line_c = 0
    #This is pass 1 to collect all the unique categories    
    for each_line in lines:
        for i in range(0,19):
            line_c += 1
            print(line_c)
            sparse_mat.append(0)
        #print(each_line)
        count = 0
        num_c = 0
        words = each_line.split(',')
        for word in words:
            word = word.rstrip()
            if word == "vhigh" and count == 0:
                sparse_mat[0] = 1
                count += 1
            if word == "high" and count == 0:
                sparse_mat[1] = 1
                count += 1
            if word == "med" and count == 0:
                sparse_mat[2] = 1
                count += 1
            if word == "low" and count == 0:
                sparse_mat[3] = 1
            if word == "vhigh" and count == 1:
                sparse_mat[4] = 1
                count += 1
            if word == "high" and count == 1:
                sparse_mat[5] = 1
                count += 1
            if word == "med" and count == 1:
                sparse_mat[6] = 1
                count += 1
            if word == "low" and count == 1:
                sparse_mat[7] = 1
            if word == 2 and num_c == 0:
                sparse_mat[8] = 1
                num_c += 1
            if word == 3 and num_c == 0:
                sparse_mat[9] = 1
                num_c += 1
            if word == 4 and num_c == 0:
                sparse_mat[10] = 1
                num_c += 1
            if word == "5more" and num_c == 0:
                sparse_mat[11] = 1
                num_c += 1
            if word == 2 and num_c == 1:
                sparse_mat[12] = 1
                num_c += 1
            if word == 4 and num_c == 1:
                sparse_mat[13] = 1
                num_c += 1
            if word == "more" and num_c == 1:
                sparse_mat[14] = 1
            if word == "small" and count == 2:
                sparse_mat[15] = 1
                count += 1
            if word == "med" and count == 2:
                sparse_mat[15] = 1
                count += 1
            if word == "big" and count == 2:
                sparse_mat[15] = 1
                count += 1
            if word == "low" and count == 3:
                sparse_mat[16] = 1
            if word == "med" and count == 3:
                sparse_mat[17] = 1
            if word == "high" and count == 3:
                sparse_mat[18] = 1
        list_categories.append(sparse_mat)
    
    print(list_categories)
    output = open(destination+filename+".json",'w')
    json.dump(list_categories,output)
    output.close()

def main():
    load_raw_data("./input/car/","car",".data","./data/car/")

if __name__ == "__main__":
    main()        