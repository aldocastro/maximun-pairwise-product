# Created on Apr 24, 2016
# 
# @author: aldobest

import random
from pairwise.product import Product

##### AUTONOMOUS TEST CASE #####
 
while True:
    max_range = 10
    max_value = 100000
    a = []
    n = random.randint(0,max_range) + 2
    print("n:", n)
 
    for i in range(0, n):
        a.append(random.randint(0,max_value))
     
    for i in range(0, n):
        s = str(a[i]) + ' '
        print(s, end='')
     
    print()
     
    pairwiseProduct = Product(n, a)
    res1 = pairwiseProduct.getMaxProduct()
    res2 = pairwiseProduct.getMaxProductFaster()
     
    if res1 != res2:
        print("Wrong Answer:", res1, " ", res2)
        break
    else:
        print("OK")

################################

##### MANUAL TEST #####
# print("introduce length of array")
# n = int(input())
# print("introduce values")
# a = [int(x) for x in input().split()]
# assert(len(a) == n)
#  
# result1 = Product(n, a).getMaxProduct()
# result2 = Product(n, a).getMaxProductFaster()
#  
# print("result1:", result1)
# print("result2:", result2)
#######################

##### DUMMY TEST #####
# n = 200000
# a = []
# for i in range(0, n):
#     a.append(0)
# 
# result = Product(n, a).getMaxProductFaster()
# print(result)
#######################