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
                single_transx.append("parents_usual")
            elif each_item[single_item] == 1 and single_item == 1:
                single_transx.append("parents_pretentious")
            elif each_item[single_item] == 1 and single_item == 2:
                single_transx.append("parents_great_pret")
                
            elif each_item[single_item] == 1 and single_item == 3:
                single_transx.append("has_nurs_proper")
            elif each_item[single_item] == 1 and single_item == 4:
                single_transx.append("has_nurs_less_proper")
            elif each_item[single_item] == 1 and single_item == 5:
                single_transx.append("has_nurs_improper")
            elif each_item[single_item] == 1 and single_item == 6:
                single_transx.append("has_nurs_critical")
            elif each_item[single_item] == 1 and single_item == 7:
                single_transx.append("has_nurs_very_crit")
                
            elif each_item[single_item] == 1 and single_item == 9:
                single_transx.append("form_complete")
            elif each_item[single_item] == 1 and single_item == 10:
                single_transx.append("form_completed")
            elif each_item[single_item] == 1 and single_item == 11:
                single_transx.append("form_incomplete")
            elif each_item[single_item] == 1 and single_item == 12:
                single_transx.append("form_foster")

            elif each_item[single_item] == 1 and single_item == 13:
                single_transx.append("children_1")
            elif each_item[single_item] == 1 and single_item == 14:
                single_transx.append("children_2")
            elif each_item[single_item] == 1 and single_item == 15:
                single_transx.append("children_3")
            elif each_item[single_item] == 1 and single_item == 16:
                single_transx.append("children_more")

            elif each_item[single_item] == 1 and single_item == 17:
                single_transx.append("housing_conv")
            elif each_item[single_item] == 1 and single_item == 18:
                single_transx.append("housing_less_conv")
            elif each_item[single_item] == 1 and single_item == 19:
                single_transx.append("housing_critical")
                
            elif each_item[single_item] == 1 and single_item == 20:
                single_transx.append("finance_conv")
            elif each_item[single_item] == 1 and single_item == 21:
                single_transx.append("finance_inconv")
            
            elif each_item[single_item] == 1 and single_item == 22:
                single_transx.append("social_non_prob")
            elif each_item[single_item] == 1 and single_item == 23:
                single_transx.append("social_slightly_prob")
            elif each_item[single_item] == 1 and single_item == 24:
                single_transx.append("social_problematic")
                
            elif each_item[single_item] == 1 and single_item == 25:
                single_transx.append("health_recommend")
            elif each_item[single_item] == 1 and single_item == 26:
                single_transx.append("health_priority")
            elif each_item[single_item] == 1 and single_item == 27:
                single_transx.append("health_not_recom")

            elif each_item[single_item] == 1 and single_item == 28:
                single_transx.append("class_not_recom")
            elif each_item[single_item] == 1 and single_item == 29:
                single_transx.append("class_recommend")
            elif each_item[single_item] == 1 and single_item == 30:
                single_transx.append("class_priority")
            elif each_item[single_item] == 1 and single_item == 31:
                single_transx.append("spec_prior")
            
        transx.append(single_transx)
    
    with open("./data/nursery/transx.csv","w") as output:
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
    
    with open("./data/nursery/transx.p","w") as outputpick:
        pickle.dump(transx,outputpick)
    #print(transx)
    output.close()

def main():
    
    with open("./data/nursery/data.p") as data_dump:
        binToTransx(pickle.load(data_dump))
        
    
if __name__ == "__main__":
    main()