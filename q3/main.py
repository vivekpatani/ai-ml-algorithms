# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 23:03:23 2016

@author: Vivek Patani
"""
import data_load
import apriori as apr

def main():
    
    minsupport = 0.5
    
    #The data is loaded at this point, this data is clean    
    dataset = data_load.load_test_data()
    
    #Converting the dataset to set to eliminate any duplicates    
    dataset = map(set,dataset)
    
    L, support_data, minsupport = apr.apriori(dataset,minsupport)
    print(minsupport)
    
if __name__ == "__main__":
    main()