# a = [1,2,3]
# aa = [(i,i+1) for i in a]
# print(aa)

#
# def is_odd(n):
#     return n % 2 == 1
#
#
# tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# newlist = list(tmplist)
# print(newlist)

b = 2
a = [{"id":1,"name":"111111"},{"id":2,"name":"222222"}]
data1 = filter(lambda x: x["id"] == b, a)
print(list(data1)[0])

