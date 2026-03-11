list = ['apple', 'ball','cat','dog','elephant','fish','gun','hen','ice','joker','king','lion','man','nest','onion','pen','queen','rose','sun','time','ujjwal','van','wise','x-ray','yawn','zebra']
print(list[0:3])
print(list[-3:])
print(list[len(list)//2:(len(list)//2)+3])

list2=list[:]
list.append('aeroplane')
list2.append('arrow')
for li in list:
     print(li)
print('\n')     
for lis in list2:
     print(lis)

