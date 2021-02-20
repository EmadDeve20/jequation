#!/bin/env python3

"""
this is first my project. 
this is not standard but I save it and I never change it.
because this is my first step and my story.

{
    Feb 20 2021    
}

##########################
* We Have A Fine Life :D *
##########################

Note: Don't Send PL About this Code!

"""


from math import pow, sqrt

def equation():
    """Solving System of Equation"""
    print("1 - ax+b=0")
    print("2 - a1x + b1 = a2x + b2")
    print("3 - close")

    choice = input("choice: ")
    try:
        choice = int(choice)
    except ValueError:
        choice = 3

    if choice == 1:
        a_num = input("a = ")
        try:
            a_num = float(a_num)
        except ValueError:
            a_num = 0
        b_num = input("b = ")
        try:
            b_num = float(b_num)
        except ValueError:
            b_num = 0
        try:
            x_num = -b_num/a_num
            if x_num == -0:
                x_num = 0
        except ZeroDivisionError:
            print("a can not zero!")
            quit()

        print(f"x = {x_num}")

    if choice == 2:
        a1_num = input("a1 = ")
        try:
            a1_num = float(a1_num)
        except ValueError:
            a1_num = 0

        b1_num = input("b1 = ")
        try:
            b1_num = float(b1_num)
        except ValueError:
            b1_num = 0

        a2_num = input("a2 = ")
        try:
            a2_num = float(a2_num)
        except ValueError:
            a2_num = 0

        b2_num = input("b2 = ")
        try:
            b2_num = float(b2_num)
        except ValueError:
            b2_num = 0

        try:
            x_num = (b2_num-b1_num)/(a1_num-a2_num)
            print(f"x = {x_num}")
        except ZeroDivisionError:
            print("(a1 - a2 = 0) this equation has no answer")

    if choice == 3:
        return 0

def equation2():
    """Solving System of Second Degree Equation"""
    print("ax^2+bx+c = 0")
    a_num = input("a = ")
    try:
        a_num = float(a_num)
    except ValueError:
        a_num = 0
    b_num = input("b = ")
    try:
        b_num = float(b_num)
    except ValueError:
        b_num = 0
    c_num = input("c = ")
    try:
        c_num = float(c_num)
    except ValueError:
        c_num = 0

    delta = pow(b_num, 2) - 4*(a_num*c_num)
    print(f"delta = {delta}")

    if delta > 0:
        try:
            answer1 = ((b_num*-1)+sqrt(delta)) / (2*a_num)
            answer2 = ((b_num*-1)-sqrt(delta)) / (2*a_num)
        except ZeroDivisionError:
            print("a can not zero!")
            quit()
        print(f"answer1 = {answer1} and answer2 = {answer2}")

    elif delta == 0:
        try:
            answer = (b_num*-1) / (2*a_num)
        except ZeroDivisionError:
            print("a can not zero!")
            quit()
        print(f"answer = {answer}")

    else:
        print("this equation has no answer")

def equation3():
    """Solving Systems of Equations with Two Unknowns"""
    print(
        """
        a1x+b1y=c1
        a2x+b2y=c2

        a1,a2,b1,b2 can not zero!"""
    )

    a1_num = input("a1 = ")
    try:
        a1_num = float(a1_num)
        if a1_num == 0:
            while a1_num == 0:
                a1_num = input("a1 = ")
                try:
                    a1_num = float(a1_num)
                except:
                    a1_num = 0
    except ValueError:
        a1_num = 0

    b1_num = input("b1 = ")
    try:
        b1_num = float(b1_num)
        if b1_num == 0:
            while b1_num == 0:
                b1_num = input("b1 = ")
                try:
                    b1_num = float(b1_num)
                except:
                    b1_num = 0
    except:
        b1_num = 0

    c1_num = input("c1 = ")
    try:
        c1_num = float(c1_num)
    except:
        c1_num = 0


    a2_num = input("a2 = ")
    try:
        a2_num = float(a2_num)
        if a2_num == 0:
            while a2_num == 0:
                a2_num = input("a2 = ")
                try:
                    a2_num = float(a2_num)
                except:
                    a2_num = 0
    except:
        a2_num = 0

    b2_num = input("b2 = ")
    try:
        b2_num = float(b2_num)
        if b2_num == 0:
            while b2_num == 0:
                b2_num = input("b2 = ")
                try:
                    b2_num = float(b2_num)
                except:
                    b2_num = 0
    except:
        b2_num = 0



    c2_num = input("c2 = ")
    try:
        c2_num = float(c2_num)
    except:
        c2_num = 0



    exit = False
    for i in range(2, 12, 1):
        for j in range(2, 12, 1):
            if (a1_num * i) % (a2_num * j) == 0:
                b_num = (b1_num*i) - (b2_num*j)
                c_num = (c1_num*i) - (c2_num*j)
                x_num = c_num / b_num
                if x_num == -0:
                    x_num = 0
                y_num = (c2_num-(a2_num*x_num)) / b2_num
                if y_num == -0:
                    y_num = 0
                if ((a1_num*x_num) + (b1_num*y_num)) == a1_num*x_num+b1_num*y_num:
                    print(f"x = {x_num} , y = {y_num} => ({a1_num}*{x_num}) + ({b1_num}*{y_num}) = {a1_num*x_num+b1_num*y_num}", end=' ')
                if (b2_num*y_num) + (a2_num*x_num) == a2_num*x_num+b2_num*y_num:
                    print(f"=> ({b2_num}*{y_num}) + ({a2_num}*{x_num}) = {a2_num*x_num+b2_num*y_num}")
                exit = True
                break


            if (a1_num * j) / (a2_num * i) == 1:
                b_num = (b1_num*j) - (b2_num*i)
                c_num = (c1_num*j) - (c2_num*i)
                x_num = c_num / b_num
                if x_num == -0:
                    x_num = 0
                y_num = (c1_num-(a1_num*x_num)) / b1_num
                if y_num == -0:
                    y_num = 0
                if ((a1_num*x_num) + (b1_num*y_num)) == a1_num*x_num+b1_num*y_num:
                    print(f"x = {x_num} , y = {y_num} => ({a1_num}*{x_num}) + ({b1_num}*{y_num}) = {a1_num*x_num+b1_num*y_num} ")
                if (b2_num*y_num) + (a2_num*x_num) == a2_num*x_num+b2_num*y_num:
                    print(f" => ({b2_num}*{y_num}) + ({a2_num}*{x_num}) = {a2_num*x_num+b2_num*y_num}")
                exit = True
                break

        if exit == True:
            break

def menu():
    print("""
What Equation do you need solve?:
    1 - First Degree Equation
    2 - Second Degree Equation
    3 - Equation With Two Unkonwn
    4 - close (cansel)
    
    """)

    choice_mode = input("choice (number): ")
    try:
        choice_mode = int(choice_mode)
    except:
        choice_mode = 4

    if choice_mode == 1:
        equation()
        menu()
    if choice_mode == 2:
        equation2()
        menu()
    if choice_mode == 3:
        equation3()
        menu()
    else:
        quit()

if __name__ == "__main__":
    menu()
