# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 14:49:56 2022

@author: Lenovo
"""
INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")
CORRECT_ANSWER="John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

def fix_text(mystr):

    liste=mystr.split(" ")
    mystr=""
    for j in range(len(liste)):
        if ("(" in liste[j]) and (")" in liste[j]):            
         if j+1<len(liste) and liste[j+1][0] == " ":
             if ("(" in liste[j]) and (")" in liste[j]): 
              if ("((" in liste[j]):
                 liste[j]=liste[j].replace("((" , "(")
                 liste[j]=liste[j].replace(")", "")

                 mystr+=liste[j]
              elif ("))" in liste[j]): 
                 liste[j]=liste[j].replace("(" , "")

                 liste[j]=liste[j].replace("))", ")")
                 mystr+=liste[j]
              else:
                  liste[j]=liste[j].replace("(" , "")
                  liste[j]=liste[j].replace(")", "")
                  mystr+=liste[j]  

         else:
                
            if ("(" in liste[j]) and (")" in liste[j]): 
             if ("((" in liste[j]):
                liste[j]=liste[j].replace("((" , "(")
                liste[j]=liste[j].replace(")", " ")

                mystr+=liste[j]
             elif ("))" in liste[j]): 
                liste[j]=liste[j].replace("(" , "")

                liste[j]=liste[j].replace("))", ")")
                mystr+=liste[j]
             else:
                 liste[j]=liste[j].replace("(" , "")
                 liste[j]=liste[j].replace(")", " ")
                 mystr+=liste[j]  
        else:
            if j+1<len(liste) and liste[j+1][0] == " ":
                stringlength=len(liste[j]) 
                liste[j]=liste[j][stringlength::-1]
            else:
                stringlength=len(liste[j]) 
                liste[j]=liste[j][stringlength::-1]
                mystr+=liste[j]+" "
    mystr=mystr[:-1]

    return mystr
if __name__ == "__main__":
        print("Correct!" if fix_text(INPUT)==CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
    
        
    
    