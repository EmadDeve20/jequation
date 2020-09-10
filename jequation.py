#!/bin/env python3
from math import pow,sqrt

def equation():
    """Solving System of Equation"""
    print("1 - ax+b=0")
    print("2 - a1x + b1 = a2x + b2")

    choice = input("choice: ")
    try:
        choice = int(choice)
    except ValueError:
        choice = 3

    if choice == 1:
        a = input("a = ")
        try:
            a = float(a)
        except ValueError:
            a = 0
        b = input("b = ")
        try:
            b = float(b)
        except ValueError:
            b = 0
        try:
            x = -b/a
            if x == -0:
                x = 0
        except ZeroDivisionError:
            print("a can not zero!")
            quit()

        print(f"x = {x}")

    if choice == 2:
        a1 = input("a1 = ")
        try:
            a1 = float(a1)
        except ValueError:
            a1 = 0

        b1 = input("b1 = ")
        try:
            b1 = float(b1)
        except ValueError:
            b1 = 0

        a2 = input("a2 = ")
        try:
            a2 = float(a2)
        except ValueError:
            a2 = 0

        b2 = input("b2 = ")
        try:
            b2 = float(b2)
        except ValueError:
            b2 = 0

        try:
            x = (b2-b1)/(a1-a2)
            print(f"x = {x}")
        except ZeroDivisionError:
            print("(a1 - a2 = 0) this equation has no answer")

    if choice == 3:
        return 0


def equation2():
    """Solving System of Second Degree Equation"""
    print("ax^2+bx+c = 0")
    a = input("a = ")
    try:
        a = float(a)
    except ValueError:
        a = 0
    b = input("b = ")
    try:
        b = float(b)
    except ValueError:
        b = 0
    c = input("c = ")
    try:
        c = float(c)
    except ValueError:
        c = 0

    delta = pow(b , 2) - 4*(a*c)
    print(f"delta = {delta}")

    if delta > 0:
        try:
            answer1 =((b*-1)+sqrt(delta)) /(2*a)
            answer2 = ((b*-1)-sqrt(delta)) / (2*a)
        except ZeroDivisionError:
            print("a can not zero!")
            quit()
        print(f"answer1 = {answer1} and answer2 = {answer2}")

    elif delta == 0:
        try:
            answer = (b * -1) / (2*a)
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

    #a1,a2,b1,b2 can not zero!
    """)

    a1 = input("a1 = ")
    try:
        a1 = float(a1)
        if a1 == 0:
            while a1 == 0:
                a1 = input("a1 = ")
                try:
                    a1 = float(a1)
                except:
                    a1 = 0
    except ValueError:
        a1 = 0

    b1 = input("b1 = ")
    try:
        b1 = float(b1)
        if b1 == 0:
            while b1 == 0:
                b1 = input("b1 = ")
                try:
                    b1 = float(b1)
                except:
                    b1 = 0
    except:
        b1 = 0

    c1 = input("c1 = ")
    try:
        c1 = float(c1)
    except:
        c1 = 0


    a2 = input("a2 = ")
    try:
        a2 = float(a2)
        if a2 == 0:
            while a2 == 0:
                a2 = input("a2 = ")
                try:
                    a2 = float(a2)
                except:
                    a2 = 0
    except:
        a2 = 0

    b2 = input("b2 = ")
    try:
        b2 = float(b2)
        if b2 == 0:
            while b2 == 0:
                b2 = input("b2 = ")
                try:
                    b2 = float(b2)
                except:
                    b2 = 0
    except:
        b2 = 0



    c2 = input("c2 = ")
    try:
        c2 = float(c2)
    except:
        c2 = 0



    exit = False
    for i in range(2,12,1):
        for j in range(2,12,1):
            if (a1 * i) % (a2 * j) == 0:
                b = (b1*i) - (b2*j)
                c = (c1*i) - (c2*j)
                x = c / b
                if x == -0:
                    x = 0
                y = (c2-(a2*x)) / b2
                if y == -0:
                    y = 0
                print(f"x = {x} , y = {y} => ({a1}*{x}) + ({b1}*{y}) = {a1*x+b1*y} = ({b2}*{y}) + ({a2}*{x}) = {a2*x+b2*y}")
                exit = True
                break


            if (a1 * j) / (a2 * i) == 1:
                b = (b1*j) - (b2*i)
                c = (c1*j) - (c2*i)
                x = c / b
                if x == -0:
                    x = 0
                y = (c1-(a1*x)) / b1
                if y == -0:
                    y = 0
                print(f"x = {x} , y = {y} => ({a1}*{x}) + ({b1}*{y}) = {a1*x+b1*y} = ({b2}*{y}) + ({a2}*{x}) = {a2*x+b2*y}")
                exit = True
                break

        if exit == True:
            break

def menu():
    print("""
What Equation do you need solve?:
    1 - First Degree Equation
    2 - Second Degree Equation
    3 - Equation With Two Unkonwn(demo)
    4 - close (cansel)
    """
    )

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
