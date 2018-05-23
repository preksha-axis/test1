import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#data= pd.read_csv('vivanta.csv')
data= pd.read_csv('sterling.csv')
names_data = pd.read_csv('hotelnames.csv')   
my_hotel_id = 1 
# my_hotel_id= 18213
hotel_id = [ 1,2,3,4,5]  
# hotel_id=[18213, 22188, 22189, 22190, 22191]
my_hotel_id_index= hotel_id.index(my_hotel_id)  
n= len(hotel_id)  
date_begin= np.datetime64(np.amin(data.check_in).split('T')[0])

data = data.replace(0.0, np.NaN)    
hotel=[]
min_price=[]
var=[]
x= []

for i in range(n):
    hotel.append(0)
    min_price.append(0)
    var.append(0)
    x.append(0)


for i in range(n):
	x[i]= names_data.loc[(names_data.hotel_id) == hotel_id[i]] 		#assigning hotel names to corresponding hotel ids

for i in range(n):
    hotel[i]= data.loc[(data.hotel_id) == hotel_id[i]]
    min_price[i]= hotel[i].groupby(['check_in'], sort=True)['total'].min(axis=1) 	#calculating the minimum price of each day of all hotels

m=len(min_price[0]) 
for j in range(m):
    var.append(0)     


for i in range(n):
    min_price[i]=min_price[i].fillna(0.0)
print("")

for i in range(n):
    if(i != my_hotel_id_index):
        for j in range(m):
            if(min_price[i][j]==0.0):
        	   print(str(x[i].hotel_name.to_string(index=False))+ " is sold out on all OTAs on" + str(j+date_begin))
        	   var[j]+=1
print("")

for j in range(m):
	if(min_price[my_hotel_id_index][j]==0.0):
		print( "Your hotel is sold out on all OTAs on " + str(j+date_begin))	

for i in range(m):
 	if(var[i]):
 		print(str(var[i])+ " out of " + str(n-1)+" competitors are sold out on " + str(i+date_begin))
print("")

