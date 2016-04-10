from __future__ import print_function
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 00:19:54 2016

@author: Vivek Patani
"""
import apriori as apr
count_12 = 0

'''
Used to generate the Association Rules
Input as Freq Set, Support Data
'''
def generateRules(L, support_data, min_confidence=0.7):
    
    finalRules = []
    
    #Walk through each row of the frequent itemset table
    for i in range(1,len(L)):
        
        #For each item in that row of frequent itemset
        for freq_set in L[i]:
            
            #Split each item into its individual elements but as lists
            individual_elements = [frozenset([single_item]) for single_item in freq_set]
            #print ("freqSet", freqSet, 'H1', individual_elements)
            
            #If size is greater than 1 then there is scope to merge
            if (i > 1):
                
                #The generation of rules from antecedant to consequent
                rules_from_conseq(freq_set, individual_elements, support_data, finalRules, min_confidence)
            else:
                
                #Calculate the confidence or the lift
                calc_confidence(freq_set, individual_elements, support_data, finalRules, min_confidence)
    return finalRules,count_12


'''
Once the possible combinations are generated we want to see which rules are important and which are not.
We also call lift from here
'''
def calc_confidence(freqSet, H, support_data, rules, min_confidence=0.7):
    pruned_H = []
    global count_12
    for conseq in H:
        count_12 += 1
        #Use confidence when you want to and life when you want to, just comment out the things
        #conf = conf_calculation(freqSet, H, support_data, rules, conseq, min_confidence)
        
        #Lift Calculation, while using this please comment the confidence line
        conf = lift_calculation(freqSet, H, support_data, rules, conseq, min_confidence)
        
        if conf >= min_confidence:
            #print (freqSet - conseq, '--->', conseq, 'conf:', conf)
            rules.append((freqSet - conseq, conseq, conf))
            pruned_H.append(conseq)
    return pruned_H

'''
Just to calculate confidence
'''   
def conf_calculation(freqSet, H, support_data, rules, conseq, min_confidence=0.7):
    
    conf = support_data[freqSet] / support_data[freqSet - conseq]
    return conf

'''
Just to calculate Lift
'''       
def lift_calculation(freqSet, H, support_data, rules, conseq, min_confidence=0.7):
    
    lift = support_data[freqSet]/(support_data[freqSet-conseq]*support_data[conseq])
    return lift

'''
This is used to generate a possible combination of candidate set of rules
'''
def rules_from_conseq(freq_set, H, support_data, rules, min_confidence=0.7):
    #Consider the size of this set    
    m = len(H[0])
    
    #print(H,"This is funny")
    #print(H[0],"This is not funny")
    if (len(freq_set) > (m + 1)):
        #print(len(freq_set),"len",m+1,"m")
        Hmp1 = apr.aprioriGenF_K_1(H, m + 1)
        #print(Hmp1,"Hmp1")
        Hmp1 = calc_confidence(freq_set, Hmp1,  support_data, rules, min_confidence)
        if len(Hmp1) > 1:
            rules_from_conseq(freq_set, Hmp1, support_data, rules, min_confidence)