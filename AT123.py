
# coding: utf-8

# bi dictionary geliyor..  key: value.. value lar list değil, normal sayı, str vs.. bunu dataframe e ceviriyosun.. 
# sonra aynı saturdan 4 tane daha ekliyosun altına.. sonra da çift indexli satırların
# son sutunundaki value'ları değiştirip (rasgele) bu frame'in son halini tekrar dic'e donusturuyosun
# 

# In[55]:


import pandas as pd

firstdict={'pickup_zip': '11510',
 'dropoff_zip': '33433',
 'ship_via_id': '1',
 'vehicle_runs': '1',
 'vehicles': {'1': {'make': 'Mercedes',
   'model': 'CLS AMG',
   'year': '2015',
   'type': 'Car',
   'price': 150},
  '2': {'make': 'Mercedes',
   'model': 'CLS AMG',
   'year': '2015',
   'type': 'Car',
   'price': 100},
  '3': {'make': 'Mercedes',
   'model': 'CLS AMG',
   'year': '2015',
   'type': 'Car',
   'price': 300}},
 'diesel_price': 2.788,
 'estimated_ship_date': '2018-10-18'}

firstdict


# In[57]:


firstdf=pd.DataFrame(firstdict)
firstdf


# In[31]:


firstdf.info()


# In[53]:


#for i in range (0,2):
    #firstdf=firstdf.append(firstdf[0],ignore_index=True)

firstdf.columns
#firstdf=firstdf.drop(firstdf.index[7:12])
df2=firstdf.iloc[[0]]

firstdf


# In[54]:


#newdf = newdf.reset_index(drop=True)

secdf = pd.concat([firstdf, df2,df2,df2,df2], ignore_index=True)
(list(secdf.vehicles))
secdf


# In[34]:


sublistkeys=list(secdf.vehicles[0].keys())

sublistkeys


# In[59]:



sublistkeys=list(secdf.vehicles[0].keys())
n=7
myvehicle={}

pricelist={}

listofprice=[]

for i in range(0,n):
    
    pricelist[i] = secdf.vehicles[i]
    
    listofprice.append(list(pricelist[i].values()))
        
    if i%2 == 0:
        
        listofprice[i][4] = 999 
        
for i in range (0,n):
    
    loggi= (dict(zip(sublistkeys,listofprice[i])))
    
    myvehicle[i]=loggi


myvehicle=pd.DataFrame(myvehicle)



# In[397]:


secdf


# In[430]:


firstdf["vehicles"][0] = firstdf["vehicles"][0].map(myvehicle[0])


# In[58]:







dictlist = [myvehicle.values() for x in range(1)]

