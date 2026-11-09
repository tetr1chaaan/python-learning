import sys
nums = [int(x) for x in sys.stdin.read().split()]
print(nums)
menin_lisytm = ["abdu"]
print(menin_lisytm)
a = list((1,2,3))
print(a[0])
a.append(4)
print(a[3])
a.insert(1,3)
print(a[1])
a.pop(1)
print(a[1])
a.clear()
print(a)
a.extend([2,3])
print(a)
a.clear()
for i in range (0,5):
    a.extend([i])
print(a)
a[1] = 5
print(a)
for i in range (2,4):
    a.remove(i)
print(a)
nums = []
