places=['Norway','Dubai','Japan','Europe','Lativa']
places[:] = [p.lower() for p in places] 
print(places)
print(sorted(places))
print(sorted(places,reverse=True))
places.reverse()
print("\n",places)
places.reverse()
print(places)
places.sort()
print('\n',places)
places.sort(reverse=True)
print([places])
