# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 23:03:23 2016

@author: Vivek Patani
"""
import data_load
import apriori as apr
import misc_max_closed as misc
import ruleGen as rule
import csv

def calling(dataset,minsupport,minconf):
    
    #Converting the dataset to set to eliminate any duplicates    
    dataset = map(set,dataset)
    count = 0
    L, support_data, minsupport = apr.apriori(dataset,minsupport)
    for each_item in range(len(L)):
        for other_item in range(len(L[each_item])):
            count += 1
    print(len(support_data),"This is Candidate")
    print(count,"This is Frequent Candidate")
    
    max_set, count_max = misc.maximal_frequent_itemsets(L)
    print(count_max,"This is Max Freq Set")
    min_set, count_min = misc.closed_frequent_itemsets(L,support_data)
    print(count_min,"This is Closed Freq Set")
    
    final,count = rule.generateRules(L, support_data, minconf)
    print(count)
    resultFile = open("./result/nursery/output_conf_"+str(minsupport)+"_"+str(minconf)+"lift"+".csv",'wb')
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(final)
    #with open("./result/nursery/rule.csv","w") as rule_file:
    #    rule_file.write(final)
    

def main():
    
    minsupport = 0.10
    minconf = 0.25
    
    #The data is loaded at this point, this data is clean    
    dataset = data_load.load_data("./data/nursery/","transx.p","./result/")
    #dataset = data_load.load_data("./data/car/","transx.p","./result/")
    #dataset = data_load.load_data("./data/cmc/","transx.p","./result/")
#    for i in range(3):
#        for j in range(3):
#            calling(dataset,minsupport,minconf)
    
    #Converting the dataset to set to eliminate any duplicates    
    dataset = map(set,dataset)
    count = 0
    L, support_data, minsupport = apr.apriori(dataset,minsupport)
    for each_item in range(len(L)):
        for other_item in range(len(L[each_item])):
            count += 1
    print(len(support_data),"This is Candidate")
    print(count,"This is Frequent Candidate")
    
    max_set, count_max = misc.maximal_frequent_itemsets(L)
    print(count_max,"This is Max Freq Set")
    min_set, count_min = misc.closed_frequent_itemsets(L,support_data)
    print(count_min,"This is Closed Freq Set")
    
    final,count = rule.generateRules(L, support_data, minconf)
    print(count)
    resultFile = open("./result/nursery/output_conf_"+str(minsupport)+"_"+str(minconf)+"lift"+".csv",'wb')
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(final)
    #with open("./result/nursery/rule.csv","w") as rule_file:
    #    rule_file.write(final)
    
if __name__ == "__main__":
    main()