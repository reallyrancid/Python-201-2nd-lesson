# The goal of this program is to print an grid using "-" , "+" and "|"
# Lesson 2, 2nd program, Use functions
# By Lance Doyle 202201029
def horiz():
    """print the Horizontal lines"""
    print('+ - - - -', '+ - - - -','+')
def vert_block():
    """print the vertical blocks"""
#Vertical lines
    print ('|         '* 2+'|')
    print ('|         '* 2+'|')
    print ('|         '* 2+'|')
    print ('|         '* 2+'|')

#  Do the work
horiz()
vert_block()
horiz()
vert_block()
horiz()
