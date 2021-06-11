#!/usr/bin/env python3

import csv

def randomLine():

    with open("pokedex.txt", "r") as csvfile:
        pokefile= csv.reader(csvfile, delimiter=",")
        name = input("Type in the name of your favorite pokemon character: ").lower()

        for row in pokefile:
            if name in row[1].lower(): # checks for similar name
                filename= "pokedex2.txt" #overwrites the files

                with open(filename, "w") as pkfile:
                    print(f"{row[1]}", file=pkfile)

randomLine()
    

