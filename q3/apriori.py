from __future__ import print_function
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 14:46:41 2016

@author: Vivek Patani
"""
'''
The generation of joint transaction from the candidate sets
'''
import candidate_generator as cdgen
import data_load as data

'''
Used to actually generate the union of elements of possible transaction
Using F_k-1 * F_k-1
'''
def aprioriGenF_K_1(freq_sets, k):
    retList = []
    
    #Length of the frequent sets
    lenLk = len(freq_sets)
    
    #Used to build all the possible combinations
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            #Select the Frequent Itemsets, only k-2 elements are selected to save computations
            L1 = list(freq_sets[i])[:k - 2]
            #Select the Frequent Itemsets, only k-2 elements are selected to save computations
            L2 = list(freq_sets[j])[:k - 2]
            #Sort to compare their equality
            L1.sort()
            L2.sort()
            #Sorting and now comparing them
            if L1 == L2:
                #If the k-2 elements are equal combine the complete set
                retList.append(freq_sets[i] | freq_sets[j])
                print(retList,"retList")
    return retList

'''
Used to actually generate the union of elements of possible transaction
Using F_k-1 * F_1
'''
def aprioriGenF_1(freq_sets, L1set, k):
    retList = []
    
    #Length of the frequent sets
    lenLk = len(freq_sets)
    lenL1 = len(L1set)
    
    #Used to build all the possible combinations
    for i in range(lenLk):
        for j in range(lenL1):
            #Select the Frequent Itemsets, only k-2 elements are selected to save computations
            L1 = list(freq_sets[i])[:k - 2]
            #Select the Frequent Itemsets, only k-2 elements are selected to save computations
            L2 = list(L1set[j])[:1]
            #print(L2,"Hello")
            #Sort to compare their equality
            L1.sort()
            L2.sort()
            #Sorting and now comparing them
            if L2 not in L1:
                retList.append(freq_sets[i] | L1set[j])
            print(retList,"retList")
    return retList

'''
Method used to generate a list of candidate items for each k
It executes a while loop
'''

def apriori(dataset, minsupport):
    print("========================Iteration k=0 Started=====================================")
    print("========================Iteration k=0 Ended=====================================")
    
    #Candidate Set is generated to find the items above support count
    candidate_set1 = cdgen.candidateC1(dataset)
    D = map(set, dataset)
    
    #Support Data contains the values of support count of each candidate
    #L1 is the set with eligible candidates, k=1
    L1, support_data = cdgen.dataSetScanner(D,candidate_set1,minsupport)
    
    L = [L1]
    k = 2
    i = 0
    while (len(L[k - 2]) > 0):
        print("========================Iteration k="+str(k-1)+" Started=====================================")
        #Ck = aprioriGenF_K_1(L[k - 2], k)
        Ck = aprioriGenF_1(L[k - 2], L[0], k)
        
        Lk, supK = cdgen.dataSetScanner(D, Ck, minsupport)
        support_data.update(supK)
        L.append(Lk)
        print("Lk = ",end = " ")
        print(L[i])
        i = i + 1
        print("========================Iteration k="+str(k-1)+" Ended=========================================")
        k += 1

    return L, support_data, minsupport

'''
Just for testing
'''
def main():
    aprioriGenF_1(data.load_test_data(),[[frozenset([1]), frozenset([3]), frozenset([2]), frozenset([5])]],2)

if __name__ == "__main__":
    main()