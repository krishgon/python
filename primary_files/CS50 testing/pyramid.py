def draw(h):
    if h == 0:
        return

    draw(h-1)    

    for i in range(0,h):
        print('#',end='')
    print('')

# taking height
h = input("enter height: ")
int_h = int(h)
draw(int_h)













# j=0

# for i in range(0,int_h):
#     j = j + 1
#     if i != 0:
#         print()
#     for box in range(0,j):
#         print("#",end='')
