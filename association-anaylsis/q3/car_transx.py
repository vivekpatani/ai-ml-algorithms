from __future__ import print_function
# -*- coding: utf-8 -*-
import pickle
"""
Created on Sat Apr 09 00:28:01 2016

@author: Vivek Patani
"""

def binToTransx(binary_list):
    
    count = 0
    transx= []
    single_transx = []
    for each_item in binary_list:
        single_transx = []
        count += 1
        #print(count)
        for single_item in range(len(each_item)):

            if each_item[single_item] == 1 and single_item == 0:
                single_transx.append("buying_vhigh")
            elif each_item[single_item] == 1 and single_item == 1:
                single_transx.append("buying_high")
            elif each_item[single_item] == 1 and single_item == 2:
                single_transx.append("buying_med")
            elif each_item[single_item] == 1 and single_item == 3:
                single_transx.append("buying_low")
                
            elif each_item[single_item] == 1 and single_item == 4:
                single_transx.append("maint_vhigh")
            elif each_item[single_item] == 1 and single_item == 5:
                single_transx.append("maint_high")
            elif each_item[single_item] == 1 and single_item == 6:
                single_transx.append("maint_med")
            elif each_item[single_item] == 1 and single_item == 7:
                single_transx.append("maint_low")
                
            elif each_item[single_item] == 1 and single_item == 8:
                single_transx.append("doors_2")
            elif each_item[single_item] == 1 and single_item == 9:
                single_transx.append("doors_3")
            elif each_item[single_item] == 1 and single_item == 10:
                single_transx.append("doors_4")
            elif each_item[single_item] == 1 and single_item == 11:
                single_transx.append("doors_5_more")

            elif each_item[single_item] == 1 and single_item == 12:
                single_transx.append("persons_2")
            elif each_item[single_item] == 1 and single_item == 13:
                single_transx.append("persons_4")
            elif each_item[single_item] == 1 and single_item == 14:
                single_transx.append("persons_more")
                
            elif each_item[single_item] == 1 and single_item == 15:
                single_transx.append("lug_boot_small")
            elif each_item[single_item] == 1 and single_item == 16:
                single_transx.append("lug_boot_med")
            elif each_item[single_item] == 1 and single_item == 17:
                single_transx.append("lug_boot_big")
                
            elif each_item[single_item] == 1 and single_item == 18:
                single_transx.append("safety_low")                
            elif each_item[single_item] == 1 and single_item == 19:
                single_transx.append("safety_med")
            elif each_item[single_item] == 1 and single_item == 20:
                single_transx.append("safety_high")
            
            elif each_item[single_item] == 1 and single_item == 21:
                single_transx.append("class_unacc")
            elif each_item[single_item] == 1 and single_item == 22:
                single_transx.append("class_acc")
            elif each_item[single_item] == 1 and single_item == 23:
                single_transx.append("class_good")
            elif each_item[single_item] == 1 and single_item == 24:
                single_transx.append("class_v_good")

        transx.append(single_transx)
    
    with open("./data/car/transx.csv","w") as output:
        for each_row in range(len(transx)):
            output.write("[")
            temp = 0
            for each_item in transx[each_row]:
                if temp == 0:
                    output.write(each_item)
                    temp += 1
                else:
                    output.write(","+each_item)
            output.write("]")
            output.write("\n")
    
    with open("./data/car/transx.p","w") as outputpick:
        pickle.dump(transx,outputpick)
    #print(transx)
    output.close()

def main():
    
    with open("./data/car/data.p") as data_dump:
        binToTransx(pickle.load(data_dump))
        
    
if __name__ == "__main__":
    main()