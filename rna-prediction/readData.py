# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:57:43 2016

@author: Rohan
"""
import ast
import pandas as pd

def read_movesets_pid(moveset_file,pid): # get data from puzzle ID
  moveset_dataFrame = pd.read_csv(moveset_file, sep=" ", header="infer", delimiter='\t')
  puzzles_pid = moveset_dataFrame.loc[moveset_dataFrame['pid'] == pid]
  plist = list(puzzles_pid['move_set'])
  ulist = list(puzzles_pid['uid'])
  plist_dict = []
  for i in plist:
    s1 = (ast.literal_eval(i))
    s2 = s1['moves']
    plist_dict.append(s2)
  
  return plist_dict, ulist

def read_movesets_uid(moveset_file,uid): # get data from user ID
  moveset_dataFrame = pd.read_csv(moveset_file, sep=" ", header="infer", delimiter='\t')
  puzzles_uid = moveset_dataFrame.loc[moveset_dataFrame['uid'] == uid]
  plist = list(puzzles_uid['move_set'])
  pidList = list(puzzles_uid['pid'])
  plist_dict = []
  for i in plist:
    s1 = (ast.literal_eval(i))
    s2 = s1['moves']
    plist_dict.append(s2)
  
  return plist_dict, pidList

def read_movesets_uid_pid(moveset_file,uid,pid,df='list'): # get data from user ID
  moveset_dataFrame = pd.read_csv(moveset_file, sep=" ", header="infer", delimiter='\t')
  puzzles1 = moveset_dataFrame.loc[moveset_dataFrame['uid'] == uid]
  puzzles2 = puzzles1.loc[puzzles1['pid'] == pid]
  if df == "list":
    return list(puzzles2['move_set'])
  elif df == "df":
    return puzzles2
  '''
  plist = list(puzzles2)
  plist_dict = []
  for i in plist:
    s1 = (ast.literal_eval(i))
    s2 = s1['moves']
    plist_dict.append(s2)
  
  return plist_dict
  '''
'''
def read_movesets_v0(moveset_file):
  moveset_dataFrame = pd.read_csv(moveset_file, sep=" ", header="infer", delimiter='\t')
  movesets = [] # a list of dictionaries containing the movesets
  for i in range(len(moveset_dataFrame)): # 102 total moveset solutions in epicfalcon.txt
      step1 = moveset_dataFrame[['move_set']].ix[[i]] # str of pid, sol_id, uid, and moveset
      step2 = step1.to_dict() # dictionary of data
      step3 = step2['move_set'] # selecting only moveset data
      step4 = step3[i] # getting rid of labels
      step5 = ast.literal_eval(step4) # converting movesets to dictionary
      movesets.append(step5['moves']) # adding each moveset to list
      
  return movesets
'''
def puzzle_attributes(moveset_file, attribute):
  moveset_dataFrame = pd.read_csv(moveset_file, sep=" ", header="infer", delimiter='\t')
  attribute_list = []
  for i in range(101):
    step1 = moveset_dataFrame[[attribute]].ix[[i]]
    step2 = step1[attribute]
    step3 = step2[i]
    step4 = str(step3)
    step5 = int(step4)
    attribute_list.append(step5)
    
  return attribute_list

def read_structure(puzzle_data):
  puzzle_structure = pd.read_csv(puzzle_data, sep=" ", header='infer', delimiter='\t')
  
  return puzzle_structure


'''
complete = os.getcwd() + '/movesets/move-set-11-14-2016.txt'
complete = pd.read_csv(complete, sep=" ", header='infer', delimiter='\t')
puzzles_6892344 = complete.loc[complete['pid'] == 6892344]
#print puzzles_6892344['move_set']
plist = list(puzzles_6892344['move_set'])
print type(plist[0])
plist_dict = []
for i in plist:
  s1 = (ast.literal_eval(i))
  s2 = s1['moves']
  plist_dict.append(s2)
  
print (plist_dict[25])
'''

'''taking pid and making a list of all the puzzle ID's in a list with indexes corresponding to movesets
epicfalcon = os.getcwd() + '\movesets\epicfalcon.txt'
epicfalcon_dataframe = pd.read_csv(epicfalcon, sep=' ', header='infer', delimiter='\t')
a = epicfalcon_dataframe[['pid']].ix[[1]]
b = a['pid']
print b
c = b[1]
print c
d = str(c)
e = int(d)
print (type(e))
'''

''' example of converting moveset data to dictionary
ms1 = epicfalcon[['move_set']].ix[[1]]
# ms1 is moveset for pid 6502951
ms2 = ms1.to_dict()
# ms2 is dictionary of ms1
ms3 = (ms2['move_set'])
# ms3 is moveset of ms2
ms4 = ms3[1]
# ms4 is ms3 w/o labels


ms5 = ast.literal_eval(ms4)
#print (ms5['moves'])
# ms5 is dict of ms4
# can now be indexed like a normal dictionary
'''

'''
f = os.getcwd() + '\movesets\puzzle-structure-data.txt'
puzzle_structure = pd.read_csv(f, sep=" ", header='infer', delimiter='\t')

print puzzle_structure['pid'][10]
'''
'''
ms1 = puzzle_structure[['structure']].ix[[0]]
# ms1 is moveset for pid 6502951
ms2 = ms1.to_dict()
# ms2 is dictionary of ms1
ms3 = (ms2['structure'])
# ms3 is moveset of ms2
ms4 = ms3[0]
# ms4 is ms3 w/o labels


ms5 = ast.literal_eval(ms4)
#print (ms5['moves'])
'''