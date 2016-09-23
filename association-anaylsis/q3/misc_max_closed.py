from __future__ import print_function
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 18:32:43 2016
    
@author: Vivek Patani
"""

'''
Used to generate the maximal frequent itemset
Takes input as the set of frequent itemsets
'''
def maximal_frequent_itemsets(freq_set):
    
    #A List to store the maximal result
    maximal_result = []
    
    #To maintaint the count of maximal result since it would be difficult to unload each item and count
    count = 0
    
    #For each level in the Lattice
    for i in range(len(freq_set)):
        
        #For each item in that level of lattice
        for each_item in freq_set[i]:
            
            #Set a flag to check whether if it is a subset or not
            flag = 1
            
            #For each item in the next level or the superset level of the previous one
            for next_itemset in freq_set[i+1]:
                
                #Check whether if it is a subset
                if each_item.issubset(next_itemset):
                    
                    #If subset set flag to 0 so that it is not added to result
                    flag=0
                    
            #If the flag is 1 then go ahead and append because it never was a subset and is a maximal freq itemset
            if flag:
                maximal_result.append(each_item)
                #Increment count
                count += 1
    return maximal_result,count

'''
Used to generate the closed frequent itemset
Takes inputas the set of frequent itemsets
'''
def closed_frequent_itemsets(freq_set,support_data):
    
    #A List to store the maximal result
    closed_result = []
    
    #To maintaint the count of closed result since it would be difficult to unload each item and count
    count = 0
    
    #For each item in that level of lattice
    for i in range(len(freq_set)):
        
        #For each item in that level of lattice
        for each_item in freq_set[i]:
            
            #Set a flag to check whether if it is has equal support or not
            flag = 1
            
            #For each item in the next level or the superset level of the previous one
            for next_item in freq_set[i+1]:
                
                #If equal then flag to 0 so that it is not added to result
                if support_data[each_item] == support_data[next_item]:
                    
                    #If support is equal then set flag to 0 so that it is not added to result
                    flag = 0
                    
            #If the flag is 1 then go ahead and append because it was not equal and is a closed freq itemset       
            if flag:
                closed_result.append(each_item)
                #increment count
                count += 1
                
    return closed_result,count