magician = ['ujjwal','Houdini','Mr.X','laudu_lalit']
great_magician=[]
def show_magician(great_magician):
    print('Following are the magicains: ')
    for ma in great_magician:
        print(ma)

def make_great(magician):
     while magician:
         current=magician.pop()
         great_magician.append('Great '+current)
     return great_magician     

make_great(magician[:])
show_magician(magician)
show_magician(great_magician)