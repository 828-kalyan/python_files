#immutable objects. when we try to modify. it wont modify inplace. instead it will create new object and refere to new object
# x = 100
# y= x
# print(x,y)
# print(id(x), id(y))
# y += 1
# print(x,y)
# print(id(x), id(y))

#mutable objects.when we try to change the value. as it is mutable objects. it will modify in place. 
# to avoid this we want to use copy module
# list1 = [1,2,3]
# list2 = list1
# print(list1,list2)
# list2.append(4)
# print(list1,list2)

#shallow copy
#in this it will copy the objects and create new object and then list2 is refere to new object instead of referring to list1 like in above.
# import copy

# list1 = [1,2,3]
# list2 = copy.copy(list1)
# print(list1,list2)
# print(id(list1),id(list2)) #both id's are different. when we modify list1 it will not reflect on list2 as both are reference to different  
# list2.append(4)
# print(list1,list2)
# print(id(list1),id(list2))

#shallow copy dosent work in case of nested loops.so to overcome it we need deep copy
# import copy
# l1 = [[1,2,3],[4,5,6]]
# l2 = copy.copy(l1)
# print(l1,l2)
# print(id(l1),id(l2))   #1840125085632, 1840124934912
# print(id(l1[0]),id(l2[0])) #1840122024320, 1840122024320
# l1[1].append(7)
# print(l1,l2)


#deep copy

# import copy
# l1 = [[1,2,3],[4,5,6]]
# l2 = copy.deepcopy(l1)
# print(l1)  #[[1, 2, 3], [4, 5, 6]] 
# print(l2)  #[[1, 2, 3], [4, 5, 6]]
# print(id(l1),id(l2))   #2414370260928, 2414370110144 
# print(id(l1[0]),id(l2[0])) #2414367199616, 2414370110058
# l1[1].append(7)
# print(l1)  #[[1, 2, 3], [4, 5, 6, 7]] 
# print(l2)  #[[1, 2, 3], [4, 5, 6]]