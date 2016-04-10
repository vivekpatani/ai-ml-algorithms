# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 02:10:39 2016

@author: Vivek Patani
"""
def learner_whitekingfile(path,filename):
    
    first = []
    input_file = open(path+filename)
    input_file = input_file.readlines()
    for each_line in input_file:
        line = each_line.split(",")
        first.append(line[6].rstrip())
    print(max(first))
    print(set(first))
    print(min(first))

def learner_age(path,filename):
    
    first = []
    input_file = open(path+filename)
    input_file = input_file.readlines()
    for each_line in input_file:
        line = each_line.split(",")
        first.append(line[1].rstrip())
    print(max(first))
    print(first+"hey")
    print(min(first))

def main():
    path = "./input/krkopt/"
    filename = "krkopt.data"
    #learner_age(path,filename)
    learner_whitekingfile(path,filename)

if __name__ == "__main__":
    main()