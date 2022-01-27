length = 10
st = '*'

for i in range (length):
    for j in range(length-i):
        print(" ", end ='')
    print(st)
    st +='*'  

length -=1
ast_num = (length*2)-1
st = "*"   * ast_num
space = 1
for i in range(length):
    print(" " + space * " " + st)
    ast_num -=2
    st = "*"  * ast_num
    space += 1