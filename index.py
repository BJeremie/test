a = [8,1,2,4,5,2,7,1,9,4,2]
b = [7,4,2,3,0,6]
c = [1,2,4,5,2,7,1,9,4,2,3,9,9,8]

# Please write a script that prints only the list element values that appear in every list.  For instance, 7 appears in all three lists, so it should be printed, but 6 does not, so it should not be printed.

def common_element(a,b,e): 
    common_elt = [value for value in a if value in b if value in c] 
    return common_elt
  
d=common_element(a,b,c)
print(d)

common_element_set =  list(set(a) & set(b) & set(c))

print ('Common Elements: ',common_element_set)

