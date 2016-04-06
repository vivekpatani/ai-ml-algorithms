# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 13:10:59 2016

@author: Vivek Patani
"""

import data_load

'''
This is used to generate the candidate itemsets of Size 1
'''
def candidateC1(dataset):
    
    #Prepare a new list of single item set
    candidate_set1 = []
    #Walk through each transaction in the dataset, to find out the unique items
    for each_transx in dataset:
        #Walk through each item in each transaction
        for each_item in each_transx:   
            if not [each_item] in candidate_set1:
                #Only for testing
                #print([each_item])
                candidate_set1.append([each_item])
    
    #Simply Sort it to be sure and that lexicographically appears in order
    candidate_set1.sort()
    return map(frozenset, candidate_set1)
    
'''
Returns the list of candidates which are eligible and the support stats
'''
def dataSetScanner(dataset, candidates, min_support):
    
    #This stores the number of times a certain subset has appeared    
    subset_count = {}
    
    #Walk through each transaction in the dataset
    for each_transx in dataset:
        #Check each candidate in the dataset
        for each_candidate in candidates:
            if each_candidate.issubset(each_transx):
                #Add that subset to the subset count
                subset_count.setdefault(each_candidate, 0)
                #Increment the count by 1
                subset_count[each_candidate] += 1
                
    #Finding the number of the number of transactions
    num_items = float(len(dataset))
    #The list of actual elements which pass the support count condition
    retlist = []
    #Support data is the final set of data with the support count
    support_data = {}
    #Walking through each candidate in the subset count
    for key in subset_count:
        #Fianlly calculation support
        support = subset_count[key] / num_items
        #Only if support is greater than minimum support
        if support >= min_support:
            #Append to the result
            retlist.insert(0, key)
        support_data[key] = support
    return retlist, support_data

'''
Just for testing
'''
def main():
    dataset = data_load.load_test_data()
    output = candidateC1(dataset)
    #print(output)
    
    #print(dataset)
    dataset = map(set,dataset)
    #print(dataset)
    L1, support_data = dataSetScanner(dataset,output,0.3)
    #print(L1)
    #print(support_data)
    
'''
Standard Boiler Plate
'''
if __name__ == "__main__":
    main()