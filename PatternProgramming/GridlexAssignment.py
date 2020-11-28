string=input("Enter some string : ")
if (string.isalnum() is False) :
    print("Please do not  enter special characters!!\nit accepts only alphabets or numericals or alphanumerical combo")
else:
    l=[]
    for i in range(len(string)):
        l.append([[" " for i in range(6)] for j in range(7)])
    for i in range(len(string)):
        if string[i]=='A':
            for row in range(7):
                for col in range(6):
                    if(((col==0 or col==5) and row!=0) or (row==3) or (row==0 and (col!=0 and col!=5))):
                        l[i][row][col]='#'
        elif string[i]=='B':
            for row in range(7):
                for col in range(6):
                    if col==0 or ((row==3 or row==0 or row==6) and col!=5) or (col==5 and(row!=3 and row!=0 and row!=6)):
                        l[i][row][col]='#'
        elif string[i]=='C':
            for row in range(7):
                for col in range(6):
                    if (col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and col!=0):
                        l[i][row][col]='#'
        elif string[i]=='D':
            for row in range(7):
                for col in range(6):
                    if col==0 or (col==5 and (row!=0 and row!=6)) or (row==0 and col!=5) or (row==6 and col!=5):
                        l[i][row][col]='#'
        elif string[i]=='E':
            for row in range(7):
                for col in range(6):
                    if col==0 or row==3 or row==0 or row==6:
                        l[i][row][col]='#'
        elif string[i]=='F':
            for row in range(7):
                 for col in range(6):
                     if col==0 or row==3 or row==0:
                         l[i][row][col]='#'
        elif string[i]=='G':
            for row in range(7):
                for col in range(6):
                     if (col==0 and (row!=0 and row!=6)) or \
        ((row==0 or row==6) and col!=0)\
        or (col==5 and (row==4 or row==5 or row==3))\
        or (row==3 and (col==3 or col==4)):
                         l[i][row][col]='#'
        elif string[i]=='H':
            for row in range(7):
                for col in range(6):
                    if col==0 or col==5 or row==3:
                        l[i][row][col]='#'
        elif string[i]=='I':
            for row in range(7):
                for col in range(6):
                    if col==2 or((row==0 or row==6) and col!=5):
                        l[i][row][col]='#'
        elif string[i]=='J':
            for row in range(7):
                for col in range(6):
                    if col==3 or(row==0 and col!=5) or (row==6 and col<3) or (row==5 and col==0):
                        l[i][row][col]='#'
        elif string[i]=='K':
            for row in range(7):
                for col in range(6):
                    if col==0 or row+col==3 or row-col==3:
                        l[i][row][col]='#'
        elif string[i]=='L':
            for row in range(7):
                for col in range(6):
                    if col==0 or row==6:
                        l[i][row][col]='#'
        elif string[i]=='M':
            for row in range(7):
                for col in range(6):
                    if col==0 or col==5 or (row==col and col<3) or (col+row==5 and row<3):
                        l[i][row][col]='#'
        elif string[i]=='N':
            for row in range(7):
                for col in range(6):
                    if col==0 or col==5 or row==col:
                        l[i][row][col]='#'
        elif string[i]=='O':
            for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and (row!=0 and row!=6))\
       or(row==0 and (col!=0 and col!=5))\
       or (row==6 and (col!=0 and col!=5)):
                        l[i][row][col]='#'
        elif string[i]=='P':
            for row in range(7):
                for col in range(6):
                    if col==0 or (col==5 and (row>0 and row<3)) or ((row==0 or row==3)):
                        l[i][row][col]='#'
        elif string[i]=='Q':
            for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and (row!=0 and row<6))or(row==0 and (col!=0 and col!=5))or(row==6 and col!=0):
                        l[i][row][col]='#'
        elif string[i]=='R':
            for row in range(7):
                for col in range(6):
                    if col==0 or (col==5 and (row==1 or row==2)) or\
       (row==0 and col!=5) or (row==3 and col<4) or row-col==1 and row>2\
       :
                         l[i][row][col]='#'
        elif string[i]=='S':
            for row in range(7):
                for col in range(6):
                    if row==0 and col>0 or row==3  and col>0 or row==6 and col<5 or \
       (col==0 and (row==1 or row==2))or (col==5 and (row==4 or row==5)):
                         l[i][row][col]='#'
        elif string[i]=='T':
            for row in range(7):
                for col in range(6):
                    if col==2 or row==0:
                        l[i][row][col]='#'
        elif string[i]=='U':
            for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and row!=6) or (row==6 and (col!=0 and col!=5)):
                        l[i][row][col]='#'
        elif string[i]=='V':
            for row in range(7):
                for col in range(6):
                    if ((col==0 or col==4) and row<5) or (row-col==4 and row>4) or\
       (row-col==2 and row==5):
                         l[i][row][col]='#'
        elif string[i]=='W':
            for row in range(7):
                for col in range(6):
                    if col==0 or col==4 or (row+col==6 and row>3) or (row+col==8 and (row>3 and row!=6)):
                        l[i][row][col]='#'
        elif string[i]=='X':
            for row in range(7):
                 for col in range(6):
                     if row==col or row+col==5:
                         l[i][row][col]='#'
        elif string[i]=='Y':
            for row in range(7):
                 for col in range(6):
                     if (col==2 and row>2) or ((row==col or row+col==4) and row<3):
                         l[i][row][col]='#'
        elif string[i]=='Z':
            for row in range(7):
                 for col in range(6):
                     if row==0 or row==5 or row+col==5:
                         l[i][row][col]='#'
        elif string[i]=='a':
            for row in range(7):
                for col in range(6):
                    if (row==3 and 0<col<5) or (row==6 and 0<col<6)or \
       (col==0 and (row==4 or row==5)) or (col==5 and\
       (row==4 or row==5)):
                        l[i][row][col]='#'
        elif string[i]=='b':
            for row in range(7):
                for col in range(6):
                    if (row==3 and 0<col<5) or (row==6 and 0<col<5)or \
       (col==0) or (col==5 and\
       (row==4 or row==5)):
                        l[i][row][col]='#'
        elif string[i]=='c':
            for row in range(7):
                for col in range(6):
                    if (row==3 and 0<col<5) or (row==6 and 0<col<5)or \
       (col==0 and (row==4 or row==5)):
                        l[i][row][col]='#'
        elif string[i]=='d':
            for row in range(7):
                for col in range(6):
                    if col==5 or (row==3 and 0<col<5) or (row==6 and 0<col<5)or \
       (col==0 and (row==4 or row==5)):
                        l[i][row][col]='#'
        elif string[i]=='e':
            for row in range(7):
                for col in range(6):
                    if (row==3 and 0<col<5) or (row==6 and 0<col<6)or \
       (col==0 and (row==4 or row==5))or row==4 and (col>1):
                        l[i][row][col]='#'
        elif string[i]=='f':
            for row in range(7):
                for col in range(6):
                    if (col==2 and row>0) or \
       row==0 and (col==3 or col==4)\
       or (row==3 and (col==1 or col==3)):
                        l[i][row][col]='#'
        elif string[i]=='g':
            for row in range(7):
                for col in range(6):
                    if col==5 and (row!=0 and row!=6) or (col==0 and(row!=0 and row!=6  and row!=4)) or\
      ((row==0 or row==6) and (col!=0)) or row==3:
                        l[i][row][col]='#'
        elif string[i]=='h':
            for row in range(7):
                for col in range(6):
                    if (row==3 and 0<col<5) or (row==6 and (col==0 or col==5))or \
       (col==0) or (col==5 and\
       (row==4 or row==5)):
                        l[i][row][col]='#'
        elif string[i]=='i':
            for row in range(7):
                for col in range(6):
                    if (col==2 and row>1) or \
       row==0 and col==2 :
                        l[i][row][col]='#'
        elif string[i]=='j':
            for row in range(7):
                for col in range(6):
                    if (col==3 and 6>row>1) or \
       row==0 and col==3 or (row==6 and col==2) or\
       (row==6 and col==1):
                        l[i][row][col]='#'
        elif string[i]=='k':
            for row in range(7):
                for col in range(6):
                    if col==0  or row-col==3 or row+col==5 and 1<row<4:
                        l[i][row][col]='#'
        elif string[i]=='l':
            for row in range(7):
                for col in range(6):
                    if (col==2 ) :
                        l[i][row][col]='#'
        elif string[i]=='m':
            for row in range(7):
                for col in range(6):
                    if (col==0 and row>2) or (col==5 and row>2)\
       or (row==4 and (col==1 or col==4)) or\
       (row==5 and (col==2 or col==3)):
                        l[i][row][col]='#'
        elif string[i]=='n':
            for row in range(7):
                for col in range(6):
                    if (row==3 and (1<col<5 or col==0)) or (col==5 and\
       (row>3))or (col==1 and row>3):
                        l[i][row][col]='#'
        elif string[i]=='o':
            for row in range(7):
                for col in range(6):
                    if (row==3 and 1<col<5) or (col==5 and\
       (6>row>3))or (col==1 and 6>row>3) or (row==6 and 1<col<5):
                        l[i][row][col]='#'
        elif string[i]=='p':
            for row in range(7):
                for col in range(6):
                    if row==1 and 5>col>1 or (row==4 and 1<col<5) or\
       (col==0) or (col==5 and (row==2 or row==3)):
                        l[i][row][col]='#'
        elif string[i]=='q':
            for row in range(7):
                for col in range(6):
                    if (row==3 and 1<col<5) or (col==5 and\
       (6>row>3))or \
          row==5 and col>2 or (col==1 and 6>row>3) or (row==6 and 1<col<6):
                        l[i][row][col]='#'
        elif string[i]=='r':
            for row in range(7):
                for col in range(6):
                    if (row==3 and (1<col<3)) or (col==1 and row>1) or row==2 and col==3:
                        l[i][row][col]='#'
        elif string[i]=='s':
            for row in range(7):
                for col in range(6):
                    if (row==2 and 0<col<6) or (row==6 and 0<=col<5)or \
       (col==0 and row==3) or (col==5 and\
       (row==5 )) or row==4 and 0<col<5:
                        l[i][row][col]='#'
        elif string[i]=='t':
            for row in range(7):
                for col in range(6):
                    if (col==3 and 6>row>0) or (row==6 and col==5) or\
       (row==6 and col==4) or (row==3 and 1<col<5):
                        l[i][row][col]='#'
        elif string[i]=='u':
            for row in range(7):
                for col in range(6):
                    if (col==5 and\
       (6>row>2))or (col==1 and 6>row>2) or (row==6 and 1<col<6):
                        l[i][row][col]='#'
        elif string[i]=='v':
            for row in range(7):
                for col in range(6):
                    if (row-col==4 and row>3) or\
       (row-col==2 and row==5) or col==row==4:
                        l[i][row][col]='#'
        elif string[i]=='w':
            for row in range(7):
                for col in range(6):
                    if col==0 and row>2 or col==4 and row>2 or (row+col==6 and row>3) or (row+col==8 and (row>3 and row!=6)):
                        l[i][row][col]='#'
        elif string[i]=='x':
            for row in range(7):
                for col in range(6):
                    if row==col and 0<row<6 or row+col==6 and row<6:
                        l[i][row][col]='#'
        elif string[i]=='y':
            for row in range(7):
                for col in range(6):
                    if (col==3 and row>3)\
       or (row==3 and (col==2 or col==4)) or (row==2 and (col==1 or col==5)):
                        l[i][row][col]='#'
        elif string[i]=='z':
            for row in range(7):
                for col in range(6):
                    if row==2 and col<5 or row==5 and col<5 or row+col==6 and 1<row<6:
                        l[i][row][col]='#' 
        
                   
        elif string[i]=='0':
            for row in range(7):
                for col in range(6):
                     if((col==0 or col==5) and (row!=0 and row!=6)) or ((row==0 or row==6) and (col!=0 and col!=5)):
                         l[i][row][col]='#'
            
        elif string[i]=='1':
            for row in range(7):
                 for col in range(6):
                     if col==3 or row==6 or((row+col==2)and col<3):
                         l[i][row][col]='#'
        elif string[i]=='2':
            for row in range(7):
                 for col in range(6):
                     if row==6 or(col==5 and (row==1 or row==2)) or\
       row==col==3 or(row==0 and col!=5) or (row>3 and col==0):
                         l[i][row][col]='#'
        elif string[i]=='3':
            for row in range(7):
                 for col in range(6):
                     if row==0  or row==3  or row==6  or \
       (col==5 and (row==1 or row==2))or (col==5 and (row==4 or row==5)):
                          l[i][row][col]='#'
        elif string[i]=='4':
            for row in range(7):
                for col in range(6):
                    if  row==3  or \
       ((col==5 or col==0) and (row==0 or row==1 or row==2))or (col==5 and (row==4 or row==5 or row==6)):
                       l[i][row][col]='#'
        elif string[i]=='5':
            for row in range(7):
                for col in range(6):
                    if (row==0 and col>0) or (row==3 and col!=5)  and col>0 or row==6 and col<5 or \
       (col==0 and row<4)or (col==5 and (row==4 or row==5)):
                        l[i][row][col]='#'
        elif string[i]=='6':
            for row in range(7):
                for col in range(6):
                    if row==0 and col>0 or row==3 or (row==6 and 0<col<5)or \
       (col==0 and 6>row>0) or (col==5 and (row==4 or row==5)):
                         l[i][row][col]='#'
        elif string[i]=='7':
            for row in range(7):
                for col in range(6):
                    if row==0 or row+col==5:
                        l[i][row][col]='#'
        elif string[i]=='8':
            for row in range(7):
                for col in range(6):
                    if row==0 and 5>col>0 or (row==3 and 0<col<5) or (row==6 and 0<col<5)or \
       (col==0 and (row!=3 and row!=0 and row!=6)) or (col==5 and\
       (row!=3 and row!=0 and row!=6)):
                         l[i][row][col]='#'
        elif string[i]=='9':
            for row in range(7):
                for col in range(6):
                    if  row==3  or row==0 or \
       ((col==5 or col==0) and (row==0 or row==1 or row==2))or \
       (col==5 and (row==4 or row==5 or row==6)):
                        l[i][row][col]='#'
        
    
    for i in range(7):
	    for j in range(len(string)):
		    for k in range(6):
			    print(l[j][i][k],end=" ")
		    print(end=" ")
	    print()

