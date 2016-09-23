from __future__ import print_function
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 18:45:07 2016

@author: Vivek Patani
"""
import pickle
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
                single_transx.append("age_low")
            elif each_item[single_item] == 1 and single_item == 1:
                single_transx.append("age_mid")
            elif each_item[single_item] == 1 and single_item == 2:
                single_transx.append("age_mature")
                
            elif each_item[single_item] == 1 and single_item == 3:
                single_transx.append("edu_low")
            elif each_item[single_item] == 1 and single_item == 4:
                single_transx.append("edu_int")
            elif each_item[single_item] == 1 and single_item == 5:
                single_transx.append("edu_mid")
            elif each_item[single_item] == 1 and single_item == 6:
                single_transx.append("edu_high")
            
            elif each_item[single_item] == 1 and single_item == 7:
                single_transx.append("hus_edu_low")
            elif each_item[single_item] == 1 and single_item == 8:
                single_transx.append("hus_edu_int")
            elif each_item[single_item] == 1 and single_item == 9:
                single_transx.append("hus_edu_mid")
            elif each_item[single_item] == 1 and single_item == 10:
                single_transx.append("hus_edu_high")
                
            elif each_item[single_item] == 1 and single_item == 11:
                single_transx.append("number_of_children_low")
            elif each_item[single_item] == 1 and single_item == 12:
                single_transx.append("number_of_children_mid")
            elif each_item[single_item] == 1 and single_item == 13:
                single_transx.append("number_of_children_high")
                
            elif each_item[single_item] == 1 and single_item == 14:
                single_transx.append("rel_not_islam")
            elif each_item[single_item] == 1 and single_item == 15:
                single_transx.append("rel_islam")

            elif each_item[single_item] == 1 and single_item == 16:
                single_transx.append("working_wife")
            elif each_item[single_item] == 1 and single_item == 17:
                single_transx.append("not_working_wife")
                
            elif each_item[single_item] == 1 and single_item == 18:
                single_transx.append("occupation_cat_1")
            elif each_item[single_item] == 1 and single_item == 19:
                single_transx.append("occupation_cat_2")
            elif each_item[single_item] == 1 and single_item == 20:
                single_transx.append("occupation_cat_3")
            elif each_item[single_item] == 1 and single_item == 21:
                single_transx.append("occupation_cat_4")
                            
            elif each_item[single_item] == 1 and single_item == 22:
                single_transx.append("stnd_of_living_low")
            elif each_item[single_item] == 1 and single_item == 23:
                single_transx.append("stnd_of_living_int")
            elif each_item[single_item] == 1 and single_item == 24:
                single_transx.append("stnd_of_living_med")
            elif each_item[single_item] == 1 and single_item == 25:
                single_transx.append("stnd_of_living_high")
            
            elif each_item[single_item] == 1 and single_item == 26:
                single_transx.append("media_good")
            elif each_item[single_item] == 1 and single_item == 27:
                single_transx.append("media_not_good")

            elif each_item[single_item] == 1 and single_item == 28:
                single_transx.append("no_conception")
            elif each_item[single_item] == 1 and single_item == 29:
                single_transx.append("long_term_conception")
            elif each_item[single_item] == 1 and single_item == 30:
                single_transx.append("short_term_concept")
            
        transx.append(single_transx)
    
    with open("./data/cmc/transx.csv","w") as output:
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
    
    with open("./data/cmc/transx.p","w") as outputpick:
        pickle.dump(transx,outputpick)
    #print(transx)
    output.close()

def main():
    
    with open("./data/cmc/data.p") as data_dump:
        binToTransx(pickle.load(data_dump))
        
    
if __name__ == "__main__":
    main()