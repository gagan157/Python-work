# Problem Statement:-
#  Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
# Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
# So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
# Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
# Note: Rohan’s function returns a list of numbers like this
# Rohan Das’s Function Input:
# rohanMultiplication(6)
# Rohan’s function returns this output:
# [6, 12, 18, 26, …., 60]
# You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None


def Rohan_das(number):
    tableli=[]
    for tab in range(1,10+1):
        if tab==4:
            table=(number*tab)+2
            tableli.append(table)
            continue
        table=number*tab      
        tableli.append(table)
    return tableli


def iscorrect(rohan_table,num):
    mytable=[]
    for tab in range(1,10+1):
        table=num*tab
        mytable.append(table)

    if rohan_table==mytable:
        print("Table is Correct")
    else:
        for count in range(len(mytable)):
            if mytable[count]!=rohan_table[count]:
                print(f"Wrong table {num}*{count+1}={rohan_table[count]}")
                print(f"Correct Awnser {num}*{count+1}={mytable[count]}")

                




if __name__=="__main__":
    # num=int(input("Which table you want:"))    
    rohantable=Rohan_das(6)
    print(rohantable)
    iscorrect(rohantable,6)        