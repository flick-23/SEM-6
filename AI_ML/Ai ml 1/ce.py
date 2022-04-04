

import numpy as np
import pandas as pd
data = pd.DataFrame(data=pd.read_csv('enjoysport.csv'))
concepts = np.array(data.iloc[:,0:-1])
print(concepts)
target = np.array(data.iloc[:,-1])
print(target)

def learn(concepts, target):
      specific_h = concepts[0].copy()
      print("initialization of specific_h and general_h")
      print(specific_h)
      general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
      print(general_h)
      for i, h in enumerate(concepts) :
           if target[i] == "yes":
              for x in range(len(specific_h)):
                   if h[x] != specific_h[x]:
                       specific_h[x] = '?'
                       general_h[x][x] = '?'
                   print(specific_h)
           print(specific_h)
           if target[i] == "no":
              for x in range(len(specific_h)):
                    if h[x] != specific_h[x]:
                        general_h[x][x] = specific_h[x]
                    else:
                        general_h[x][x] = '?'
           print(" steps of Candidate Elimination Algorithm", i+1)
           print(specific_h)
           print(general_h)
      indices = [i for i, val in enumerate(general_h) if  val == [ '?', '?', '?', '?', '?', '?',]]
      for i in indices:
           general_h.remove( [ '?', '?', '?', '?', '?', '?',])
      return specific_h, general_h

s_final, g_final = learn(concepts, target)
print("\n\n")
print("Final Specific_h:", s_final, sep="\n")
print("Final General_h:", g_final, sep="\n")


