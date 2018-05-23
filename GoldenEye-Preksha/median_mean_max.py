import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
data= pd.read_csv('casino1.csv')
data= data.replace(0.0, np.NaN) 
names_data = pd.read_csv('hotelnames.csv')
my_hotel_id=998
hotel_id = [ 998, 615, 617, 1004, 614, 999, 214, 212]
my_hotel_id_index= hotel_id.index(my_hotel_id)
n= len(hotel_id)
min_price=[]
max_price=[]
med_price=[]
hotel=[]
x=[]
count=0

for i in range (n):
	min_price.append(0)
	med_price.append(0)
	hotel.append(0)
	x.append(0)
	max_price.append(0)

for i in range(n):
	x[i]= names_data.loc[(names_data.hotel_id) == hotel_id[i]]		#storing hotel names in x
	
for i in range(n):
    hotel[i]= data.loc[(data.hotel_id) == hotel_id[i]]
    min_price[i]= hotel[i].groupby(['check_in'], sort=True)['total'].min()		#calculating the minimum price of each day of all hotels
    		

for i in range(n):
		replace_nan=np.nanmedian(min_price[i])
		min_price[i]=min_price[i].fillna(0.0)
		min_price[i]=min_price[i].replace(0.0,replace_nan)

m=len(min_price[my_hotel_id_index])
min= np.min(min_price[my_hotel_id_index])
max= np.max(min_price[my_hotel_id_index])
print("")
print("Your hotel's price ranges from (" + str(min) + "," +str(max) + ") in this " + str(m) + " days period")

for i in range(n):
	if(i != my_hotel_id_index):
		med_price[i]= np.median(min_price[i])
median= float(sum(med_price))/float(len(med_price))		#average of the median price of compset

for j in range (m):
	if((min_price[my_hotel_id_index][j])>(median)):
		count+=1

print("Compset median is " + str(median))
print("Your hotel is above the compset median on " + str(count) + " out of " + str(m) + " days " )
print("")




