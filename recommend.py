"""
Created on Sat Mar  2 15:59:01 2019

@author: Babita
Task A 
1) Develop a program to create recommendation system to recommend products to a customer on any e-commerce website. 
    Recommendations should be based on the products consumer has searched on other sites like Google or Amazon. 
2) You can use any programming language to do this 
3) Create a sample data set for implementing the feature. 
4) Drive information by analysing the data set you have made and present valuable information from it in a presentable format.
"""

import pandas as pd

df = pd.read_csv('itemsearch.csv')
df.head()
#Get list of unique items
listItem=list(set(df["ItemId"].tolist()))

#Get count of users
countUsers=len(set(df["ItemId"].tolist()))

#Create an empty data frame to store merged item scores for items.
merge_Item= pd.DataFrame(columns=('item1', 'item2', 'score'))
rowCount=0

#For each item in the list, compare with other items.
for i in range(len(listItem)):
    
    #Get list of users who bought this item 1.
    item1Users = df[df.ItemId==listItem[i]]["UserId"].tolist()
    
    #Get item 2 - items that are not item 1 or those that are not analyzed already.
    for j in range(i, len(listItem)):
        
        if ( i == j):
            continue
       
        #Get list of users who bought item 2
        item2Users=df[df.ItemId==listItem[j]]["UserId"].tolist()
        
        #Find score. Find the common list of users and divide it by the total users.
        common_users= len(set(item1Users).intersection(set(item2Users)))
        score=common_users / countUsers

        #Add a score for item 1, item 2
        merge_Item.loc[rowCount] = [listItem[i],listItem[j],score]
        rowCount +=1
        #Add a score for item2, item 1. The same score would apply irrespective of the sequence.
        merge_Item.loc[rowCount] = [listItem[j],listItem[i],score]
        rowCount +=1
        
#Check final result
merge_Item.head()
item_Search=5003
recoginze_List=merge_Item[merge_Item.item1==item_Search]\
        [["item2","score"]]\
        .sort_values("score", ascending=[0])
        
print("Recommendations for item 5003\n", recoginze_List)