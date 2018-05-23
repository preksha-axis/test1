import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
import math
data= pd.read_csv('casino1.csv')
data= data.replace(0.0, np.NaN) 
names_data = pd.read_csv('hotelnames.csv')
percent_value= 0.30
my_hotel_id=998                       #defining threshold for abnormal pricing
hotel_id = [ 998, 615, 617, 1004, 614, 999, 214, 212]
my_hotel_id_index= hotel_id.index(my_hotel_id) 
min_price =[]                               
med_price = []								
hotel = []
high= []
low= []
x = []
index_high=[]
index_low= []
n= len(hotel_id)
date_begin= np.datetime64(np.amin(data.check_in).split('T')[0])

for i in range (n):
			min_price.append(0)
			med_price.append(0)
			hotel.append(0)
			x.append(0)


for i in range(n):
	x[i]= names_data.loc[(names_data.hotel_id) == hotel_id[i]] 	#storing hotel names in x
	
for i in range(n):
    hotel[i]= data.loc[(data.hotel_id) == hotel_id[i]]
    min_price[i]= hotel[i].groupby(['check_in'], sort=True)['total'].min()		#calculating the minimum price of each day of all hotels

for i in range(n):
		replace_nan=np.nanmedian(min_price[i])
		min_price[i]=min_price[i].fillna(0.0)
		min_price[i]=min_price[i].replace(0.0,replace_nan)

m=len(min_price[0])
for i in range (m):
	high.append(0)
	low.append(0)
	index_low.append(0)
	index_high.append(0)

for i in range(n):
	med_price[i] = np.median(min_price[i])     #calculating the median price of a hotel 

for i in range(n):
	if(i != my_hotel_id_index):
		count=0
		for j in range(m):
			if ((min_price[i][j])>((1+percent_value)*med_price[i])):
				print(str(x[i].hotel_name.to_string(index=False))+" is pricing  "+ str(round(((min_price[i][j]-med_price[i])/(med_price[i]))*100))+ " percent more than it's median price on "+str(j+date_begin))
				high[j]+=1
				count=1
			if ((min_price[i][j])<((1-percent_value)*med_price[i])):
				print( str(x[i].hotel_name.to_string(index=False))+" is pricing " + str(round(((min_price[i][j]-med_price[i])/(med_price[i]))*(-100)))+  " percent less than it's median price on "+str(j+date_begin))
				low[j]+= 1
				count=1
		if(count==1):
			print("")


index_high= sorted(xrange(len(high)), key=lambda ix: high[ix], reverse=True)
index_low= sorted(xrange(len(low)), key=lambda ix: low[ix], reverse=True)

for i in range(m):			#printing number of competitors pricing higher than their threshold price for each day
	if(high[index_high[i]]):
		print(str(high[index_high[i]]) + " out of " + str(n-1)+" competitors are pricing " + str((percent_value)*100) + " percent higher than their normal rates on " + str(index_high[i]+date_begin) )
print("")	


for i in range(m):			#printing number of competitors pricing higher than their threshold price for each day
	if(low[index_low[i]]):
		print(str(low[index_low[i]]) + " out of " + str(n-1)+" competitors are pricing " + str((percent_value)*100) + " percent lower than their normal rates on " + str(index_low[i]+date_begin) )
print("")	

# for i in range(m):			#printing number of competitors pricing lower than their threshold price for each day
# 	if(low[index_low[i]]):
# 		print(str(low[index_low[i]]) + " out of " + str(n-1) + " competitors are pricing " + str((percent_value)*100) + " percent lower than their normal rates on " + str(index_low[i]+date_begin) )
# print("")

