# from collections import namedtuple

# a = namedtuple('courses', 'name, technology')
# s = a('data science', 'python')
# k = a._make(["ML", 'python'])
# print(s)
# print(k)

#counter
# from collections import Counter
# data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# c = Counter(data)
# print(c)  

# print(c['apple'])  

# print(list(c.elements()))  

# print(c.most_common(3))  


# from collections import defaultdict

# dd = defaultdict(int)

# dd['a'] += 1
# dd['b'] += 2

# print(dd)  
# print(dd['c'])  

# dd_list = defaultdict(list)
# dd_list['a'].append(1)
# dd_list['b'].append(2)
# print(dd_list)  


from collections import deque

dq = deque(['a', 'b', 'c'])

# dq.append('d')  
# dq.appendleft('z')  
# print(dq)  

# dq.pop()  
# dq.popleft()  
# print(dq)  

#dq.rotate(1)  
#print(dq)  

# dq.rotate(-1)  
# print(dq)  
