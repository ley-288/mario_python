from cs50 import get_int

while True: # we're in a loop
    h = get_int ("Height: ") # get height
    if h >= 1 and h <= 8: # if height less than one and more than 8..
        break

for i in range(h): # for a sequence use range of height
    print((h - 1 - i) * ' ', end='') #print a space for every n-1-row number. THE FIRST PYRAMID NEEDS SPACES.
    print((i + 1) * "#", end='') #print a hash for every i + 1. 0+1 =1, 1+1=2 etc..
    print(' ' * 2, end='') #print a space of 2 between every row
    print((i + 1) * "#", end='') #row + 1 print a hash. 0+1 = 1, hash, 1+1 = 2, hash. etc..
    print(end='\n') #dont need spaces at the end of the second pyramid, only a prompt to move to the next line.


# in python.. * will mean multiply if two ints either side 4*4=16, but if a number and an int, * will mean print char, int times. 4*a = aaaa.
# ***(\n comes automatically in python, so to remove \n we must type end='')***

#AT FIRST WE MUST CALCULATE A PYRAMID TO STAND OPPOSITE DIRECTION. THE SECOND PYRAMID IS UNOPPOSING, SO WE SIMPLY REVERSE THE NUMBER FROM THE FIRST PYRAMID FORMULA.
#h = 4. 4-1 (=3) -i = row.. so first row 4-1-1 = 2. 4-1-2 = 1
#i is going to 0 from n-1


#3 > n-1 - i 3.     4-1-3=0 4th row  'print a space'
#2 > n-2            4-1-2=1 3rd row
#1 > n-3            4-1-1=2 2nd row
#0 > n-4            4-1-0=3 Row 0 ie 1st row

#row +1 = #
#1 + 1 = 2