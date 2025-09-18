def is_this_a_shape(a,b):
     return a==b

def perimeter(a,b):
    if a==b:
        return int(2*a)
    else:
        return int(2*(a+b))

print(is_this_a_shape(5,5))
print(perimeter(5,5))