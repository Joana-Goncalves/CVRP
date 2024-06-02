import random
import numpy as np


def swap_mutation(_individual, both_chromo=False):
    """
    Perform swap mutation on either client or vehicle lists of one individual.
    The individual is modified in place.
    Args:
        _individual (list): List representing the individual. It has two nested lists: [[clients], [vehicles]]
        both_chromo (bool): If True, randomly (p=0.5) perform mutation on one of the two chromosomes (clients and vehicles). Default is False.
    """  
    if both_chromo:
        # Generate two distinct random indices
        cut1, cut2 = random.sample(range(len(_individual[0])), 2)
        # Randomly decide whether to swap elements in the client list or the vehicle list
        if random.random() < 0.5:
            # Swap the elements in the client list
            _individual[0][cut1], _individual[0][cut2] = _individual[0][cut2], _individual[0][cut1]
        else:
            # Swap the elements in the vehicle list
            _individual[1][cut1], _individual[1][cut2] = _individual[1][cut2], _individual[1][cut1]
    else:
        # Generate two distinct random indices
        cut1, cut2 = random.sample(range(len(_individual)), 2)
        # Swap the elements in the list
        _individual[cut1], _individual[cut2] = _individual[cut2], _individual[cut1]


def shuffle_mutation(_individual, both_chromo = False):
    """
    Perform shuffle mutation on either client or vehicle lists of one individual.
    The individual is modified in place.
    Args:
        _individual (list): List representing the individual. It has two nested lists: [[clients], [vehicles]]
        both_chromo (bool): If True, randomly (p=0.5) perform mutation on one of the two chromosomes (clients and vehicles). Default is False.
    """  
    if both_chromo:
        # Generate two distinct random indices
        cut1, cut2 = sorted(random.sample(range(len(_individual[0])), 2))
        # Randomly decide whether to shuffle part of clients or vehicles
        if np.random.rand() < 0.5:
            subset = _individual[0][cut1:cut2] # Extract the subsequence from _chromo[0]
            np.random.shuffle(subset) # Shuffle the subsequence
            _individual[0][cut1:cut2] = subset # Place the shuffled subsequence back into _chromo[0]
        else:
            # Same as before but for vehicle list
            subset = _individual[1][cut1:cut2]
            np.random.shuffle(subset)
            _individual[1][cut1:cut2] = subset
    
    else:
        cut1, cut2 = sorted(random.sample(range(len(_individual)), 2))
        subset = _individual[cut1:cut2]
        random.shuffle(subset)
        _individual[cut1:cut2] = subset


def random_resetting_mutation(vehicles):
    """
    Perform random resetting mutation on the vehicle list of the individual.
    The individual is modified in place.
    Args:
        vehicles (list): List representing the vehicles part of the individual.
    """ 
    # Select a random position in the vehicles list   
    pos = random.randint(0, len(vehicles) - 1)
    # Assign a new random value (between 0 and 4 - because we have 5 vehicles) to the selected position
    vehicles[pos] = random.randint(0, 4)


# Combinations of the different mutations
def mutate1(individual):
    swap_mutation(individual[0])
    random_resetting_mutation(individual[1])

def mutate2(individual):
    swap_mutation(individual[0])
    shuffle_mutation(individual[1])

def mutate3(individual):
    shuffle_mutation(individual[0])
    random_resetting_mutation(individual[1])

def mutate4(individual):
    shuffle_mutation(individual[0])
    swap_mutation(individual[1])

def mutate5(individual):
    if np.random.rand() < 0.5:
        swap_mutation(individual, both_chromo=True)
    else:
        shuffle_mutation(individual, both_chromo=True)

def mutate6(individual):
    if np.random.rand() < 0.5:
        swap_mutation(individual, both_chromo=True)
        random_resetting_mutation(individual[1])
    else:
        shuffle_mutation(individual, both_chromo=True)
        random_resetting_mutation(individual[1])