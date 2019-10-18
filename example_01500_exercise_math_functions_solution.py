#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# definierte 4 funktionen addieren , subtrahieren, dividieren und multiplizieren mit den jeweiligen
# rueckgabe werten und printe sie aus
# main function

def addieren(number1=2, number2=6):
    return int(number1) + int(number2)


def subtrahieren(number1=2, number2=6):
    return int(number1) - int(number2)


def multiplizieren(number1=2, number2=6):
    return int(number1) * int(number2)


def dividieren(number1=2, number2=6):
    if number2 == 0:
        return 'Termination - Division by Zero - No Result'
    else:
        return int(number1) / int(number2)


if __name__ == "__main__":
    print(addieren())
    print(subtrahieren())
    print(dividieren())
    print(multiplizieren())
    print('')
    print('')
    print('')
    print('')

# b) mit input
number_one = int(input("Zahl 1: "))
number_two = int(input("Zahl 2: "))
print(addieren(number_one, number_two))
print(subtrahieren(number_one, number_two))
print(dividieren(number_one, number_two))
print(multiplizieren(number_one, number_two))
