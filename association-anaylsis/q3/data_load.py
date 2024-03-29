# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 13:03:54 2016

This is used to preprocess the incoming data.

@author: Vivek Patani
"""

'''
Method used to load the data the converted/cleaned data file for implementation
'''

import pickle
def load_data(path,filename,destination):
    
    with open(path+filename) as input_data:
        data = pickle.load(input_data)
    return data

'''
Loading basic sample data
'''
def load_test_data():
    #Returns a data frame, sample of what the large dataset would be like
    #return [['A','B','C'],['A','B','C','D','E'],['A','C','D'],['A','C','D','E'],['A','B','C','D']]
    return [[1, 3, 4],
            [2, 3, 5],
            [1, 2, 3, 5],
            [2, 5]]
    #return [["Bread","Milk"],["Bread","Diapers","Beer","Egg"],["Milk","Diapers","Beer","Cola"],["Bread","Milk","Diapers","Beer"],["Bread","Milk","Diapers","Cola"]]

'''
Just for testing
'''
def main():
    load_data("./data/nursery/","transx.p","./result/")

if __name__ == "__main__":
    main()