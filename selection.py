import random
import numpy as np

def tournament_selection(population, k, tournsize=9):
    """
    Perform tournament selection on a population.
    Args:
        population (list): A list of individuals, each with a `fitness` attribute that has a `values` attribute.
        k (int): The number of individuals to select.
        tournsize (int): The number of individuals competing in each tournament (default is 9). 
    Returns:
        list: A list of selected individuals from the population.
    """
    chosen = []  

    for _ in range(k):
        # Randomly select 'tournsize' individuals from the population to form a tournament
        aspirants = random.sample(population, tournsize)
        # Select the individual with the lowest fitness value from the tournament
        winner = min(aspirants, key=lambda x: x.fitness.values[0])
        chosen.append(winner)
        
    return chosen


def ranking_selection(population, k):
    """
    Perform ranking selection on a population.
    Args:
        population (list): A list of individuals, each with a `fitness` attribute that has a `values` attribute.
        k (int): The number of individuals to select.   
    Returns:
        list: A list of selected individuals from the population.
    """
    # Sort the population based on their fitness values in ascending order (because it's minimization)
    sorted_pop = sorted(population, key=lambda x: x.fitness.values[0])
    # Calculate the total rank sum (triangular number formula)
    total_rank = sum(range(1, len(population) + 1))
    # Calculate selection probabilities based on rank
    probs = [(len(population) - i) / total_rank for i in range(len(population))]
    # Randomly select k individuals from the population based on the calculated probabilities
    chosen_indices = np.random.choice(len(population), k, p=probs, replace=True)
    
    return [sorted_pop[i] for i in chosen_indices]


def roulette_wheel_selection(individuals, k):
    """
    Perform roulette wheel selection on a population of individuals.
    Since this algorithm is to be applied on a minimization problem, fitnesses are inverted (1/f)
    Args:
        individuals (list): A list of individuals, where each individual has a fitness attribute.
        k (int): The number of individuals to select.
    Returns:
        list: A list of k selected individuals.
    """
    # Calculate the total fitness of the population (sum of inverses of fitness values)
    sum_fits = sum(1 / ind.fitness.values[0] for ind in individuals)
    chosen = []
    
    for i in range(k):
        # Generate a random number in the range [0, sum_fits)
        r = random.random() * sum_fits
        sum_ = 0
        for ind in individuals:
            # Accumulate fitness values
            sum_ += 1 / ind.fitness.values[0]
            # Select the individual if the accumulated sum exceeds the random number r
            if sum_ > r:
                chosen.append(ind)
                break  # Exit the inner loop once an individual is selected
    
    return chosen