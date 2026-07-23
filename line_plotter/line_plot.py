import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("example1.csv", "r") as file :
    reader = csv.reader(file)

    for row in reader:

        #print(len(row))
        if (len(row) > 2) :
            pass

        x += row[0]
        y += row[1]   

    pass
