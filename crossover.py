import random


def pmx_xo(parent1, parent2):
    """
    Perform partially mapped crossover on parents' first list (customers).
    The two individuals are modified in place and both keep their original length.
    Args:
        parent1 (list): The first parent, a list containing two sublists.
        parent2 (list): The second parent, a list containing two sublists.
    """
    # Extract the customer lists from the parents
    sub1 = parent1[0]
    sub2 = parent2[0]
    size = len(sub1)
    p1, p2 = [0] * size, [0] * size
    # Generate crossover points
    cut1, cut2 = sorted(random.sample(range(size), 2))
    # Initialize the position of each index in the sublists
    for i in range(size):
        p1[sub1[i] - 1] = i
        p2[sub2[i] - 1] = i
    # Apply crossover between cut points
    for i in range(cut1, cut2 + 1):
        # Keep track of the selected values
        temp1 = sub1[i] - 1
        temp2 = sub2[i] - 1
        # Swap the matched value
        sub1[i], sub1[p1[temp2]] = temp2 + 1, temp1 + 1
        sub2[i], sub2[p2[temp1]] = temp1 + 1, temp2 + 1
        # Position bookkeeping
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]


def cycle_xo(parent1, parent2):
    """
    Perform cycle crossover on the parents' first list (customers).
    The two individuals are modified in place and both keep their original length.
    Args:
        parent1 (list): The first parent, a list containing two sublists.
        parent2 (list): The second parent, a list containing two sublists.
    """
    # Extract the customer lists from the parents
    p1 = parent1[0]
    p2 = parent2[0]
    # Initialize offspring with None
    _offspring1 = [None] * len(p1)
    _offspring2 = [None] * len(p1)
    # Perform cycle crossover until all positions are filled
    while None in _offspring1:
        index = _offspring1.index(None) # Start the cycle from the first None position
        val1 = p1[index]
        val2 = p2[index]
        # Copy the cycle elements from parent1 to offspring1 and parent2 to offspring2
        while val1 != val2:
            _offspring1[index] = p1[index]
            _offspring2[index] = p2[index]
            val2 = p2[index]
            index = p1.index(val2)
        # After completing the cycle, fill the remaining None positions
        for element in _offspring1:
            if element is None:
                index = _offspring1.index(None)
                if _offspring1[index] is None:
                    _offspring1[index] = p2[index]
                    _offspring2[index] = p1[index]


def two_point_xo(parent1, parent2):
    """
    Perform two-point crossover on the parents' second list (vehicles).
    The two individuals are modified in place and both keep their original length.
    Args:
        parent1 (list): The first parent, a list containing two sublists.
        parent2 (list): The second parent, a list containing two sublists.
    """
    # Extract the vehicle lists from the individuals
    p1 = parent1[1]
    p2 = parent2[1]
    size = len(p1)
    # Select two crossover points
    cxpoint1 = random.randint(1, size)
    cxpoint2 = random.randint(1, size - 1)
    
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:  # Swap the two crossover points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1
    # Perform the two-point crossover on the vehicle lists
    p1[cxpoint1:cxpoint2], p2[cxpoint1:cxpoint2] = p2[cxpoint1:cxpoint2], p1[cxpoint1:cxpoint2]


def swap_genes(parent1, parent2):
    """
    Swap genes between the second lists (vehicles) of two parents.
    This function does not perform a traditional crossover; it only swaps genes within the vehicles lists.
    Args:
        parent1 (list): The first parent, a list containing two sublists.
        parent2 (list): The second parent, a list containing two sublists.
    """
    # Extract the vehicles lists
    p1 = parent1[1]
    p2 = parent2[1]
    num_clients = len(p1)
    # Generate two random cut points within the range of the vehicles list
    cut1 = random.randrange(num_clients + 1)
    cut2 = random.randrange(num_clients + 1)
    # Ensure cut1 is less than or equal to cut2
    if cut1 > cut2:
        cut1, cut2 = cut2, cut1
    # Perform the gene swap between the two cut points
    tmp = p1[cut1:cut2]        
    p1[cut1:cut2] = p2[cut1:cut2]  
    p2[cut1:cut2] = tmp 


# Combinations of crossover

def xo_1(parent1, parent2):
    pmx_xo(parent1, parent2)
    two_point_xo(parent1, parent2)


def xo_2(parent1, parent2):
    pmx_xo(parent1, parent2)
    swap_genes(parent1, parent2)


def xo_3(parent1, parent2):
    cycle_xo(parent1, parent2)
    two_point_xo(parent1, parent2)


def xo_4(parent1, parent2):
    cycle_xo(parent1, parent2)
    swap_genes(parent1, parent2)