#coding=utf-8

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]      # 含首不含尾
print list[2:]        # Prints elements starting from 3rd element
print tinylist * 2    # Prints list two times
print list + tinylist    # Prints concatenated lists
print list

#修改list中的元素
# list[0]="python"
# list.append(['yyyy','zzzz'])
# list.extend(['angelababy',66666])
# print(list)

# print(list)


"""
元组测试
"""
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2)
# tinytuple = (123, 'john')
#
# print tuple           # Prints complete list
# print tuple[0]        # Prints first element of the list
# print tuple[1:3]      # Prints elements starting from 2nd till 3rd
# print tuple[2:]       # Prints elements starting from 3rd element
# print tinytuple * 2   # Prints list two times
# print tuple + tinytuple # Prints concatenated lists
# tuple[1]=66666    #会报错，因为元组是不可变列表
# print tuple


# dict = {}
# dict['one'] = "This is one"
# dict[2]     = "This is two"
#
# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
#
#
#
# print dict['one']       # Prints value for 'one' key
# print dict[2]           # Prints value for 2 key
# print tinydict          # Prints complete dictionary
#
# tinydict['mygirl']="angelababy"
#
# print tinydict.keys()   # Prints all the keys
# print tinydict.values() # Prints all the values

