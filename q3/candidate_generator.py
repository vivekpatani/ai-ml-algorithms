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
                candidate_set1.append([each_item])
    
    #Simply Sort it to be sure and that lexicographically appears in order
    candidate_set1.sort()
    return map(frozenset, candidate_set1)

'''
Just for testing
'''
def main():
    dataset = data_load.load_test_data()
    output = candidateC1(dataset)
    print(output)

'''
Standard Boiler Plate
'''
if __name__ == "__main__":
    main()