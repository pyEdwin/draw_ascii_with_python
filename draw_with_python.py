length = 10
st = '*'

for i in range (length):
    for j in range(length-i):
        print(" ", end ='')
    print(st)
    st +='*'    