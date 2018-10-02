#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    
    crashList = []
    with open('airplane_crashes.csv') as f:
        csv_reader = csv.reader(f, delimiter = ',')
        airplane_data = list(csv_reader)
        

        for row in airplane_data:
            time = row[1]
            if time is not None:
                if len(time) == 5:
                    i = 0
                    while i < int(time[0,2]):
                        crashList.append(0)
                        i += 1
                crashList.append(1)
        return crashList



def weigh_pokemons(filename, weight):
    #json file
    myList = []
    
    weightString = String(weight) + " kg"
    
    with open(filename, 'r') as fp:
        pokemonData = json.load(fp)

        for pokemon in pokemonData:
            if pokemon['weight'] is not None:
                if pokemon['weight'] == weightString:
                    myList.append(pokemon)
    return myList




def single_type_candy_count(filename):
    count = 0
    with open(filename, 'r') as fp:
        pokemonData = json.load(fp)
        for pokemon in pokemonData:
            if pokemon['candy_count'] is not None:
                count += pokemon['candy_count']
    return count



def reflections_and_projections(points):
    flip(points, y=1)
    R = [cos(math.pi/4) -sin(math.pi/4); sin(math.pi/4) cos(math.pi/4)][flip(points, y=1)]


    

def normalize(image):
    if image is None:
        return -1
    
    max = image[0][0]
    min = image[0][0]
    for x in np.image(a, order='F'):
        if x > max:
            max = x
        if x < min:
            min = x
    for x in np.image(a, order='F'):
        x =  (255 / (max - min)) * (x - min)

    return image



def sigmoid_normalize(image):
    pass
