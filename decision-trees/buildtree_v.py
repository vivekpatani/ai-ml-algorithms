# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:52:42 2016

@author: Vivek Patani
"""



from buildtree import *


def validation(rows):
    class_dict=group_by_counts(rows)
    #print(class_dict)
    total_error=sum([i for i in error.values() if i!=max(error.values())])
    #print("te is",te)
    global count
    pe=(total_error+ leafs_count*0.5)/float(150)
    return pe


def buildtree_validation(rows,score=entropy):
  

  if len(rows)==0: return node() 
    
    
  current_score=score(rows)

  error
  if count > 2:
        
        if validation_error(rows)<=pes_er:
            pes_er=pessimistic_error(rows)
        else:
            return decisionnode(results=uniquecounts(rows))
    
  

  gain_error=0.0
  best_criteria=None
  best_sets=None
  
  
  column_count=len(rows[0])-1
  for col in range(0,column_count):
    column_values={}
    for row in rows:
       column_values[row[col]]=1
    for value in column_values.keys():
      (part1,part2)=divideset(rows,col,value)
      
      temp = float(len(part1))/len(rows)
      change = current_score-temp*score(part1)-(1-p)*score(part2)
      if change>gain_error and len(part1)>0 and len(part2)>0:
          gain_error=gain
          best_criteria=(col,value)
          best_sets=(part1,part2)
      
      elif best_gain>0:
        trueBranch=buildtree_pessimistic(best_sets[0])
        falseBranch=buildtree_pessimistic(best_sets[1])
        return decisionnode(col=best_criteria[0],value=best_criteria[1],
          tb=trueBranch,fb=falseBranch)
    else:
        return decisionnode(results=group_by_count(rows)) 
