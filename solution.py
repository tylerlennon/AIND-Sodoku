assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

#def cross(A, B):
#   "Cross product of elements in A and elements in B."
def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

# define unit lists
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'], ['A9', 'B8', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2', 'I1']]
unitlist = row_units + column_units + square_units + diagonal_units

# define unit dictionarys
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
unitsRow = dict((s, [u for u in row_units if s in u]) for s in boxes)
unitsCol = dict((s, [u for u in column_units if s in u]) for s in boxes)
unitsSqr = dict((s, [u for u in square_units if s in u]) for s in boxes)

# define peer dictionarys
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
peersRow = dict((s, set(sum(unitsRow[s],[]))-set([s])) for s in boxes)
peersCol = dict((s, set(sum(unitsCol[s],[]))-set([s])) for s in boxes)
peersSqr = dict((s, set(sum(unitsSqr[s],[]))-set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    pass

    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    pass

    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    
    return

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    
    Notes:
        undoubtably there is a more elegant way to code this solution
    
    """

    # Find all instances of naked twins
    # Eliminate the naked twins in their peers

    pass
    
    # define twin peers lists
    twin_values_row = {}
    twin_values_col = {}
    twin_values_sqr = {}

    # get list of two digit values
    two_values = [box for box in values.keys() if len(values[box]) == 2]
    
    # iterate all two digit values and determine if they have a twin in their peers
    for box in two_values:
        digit = values[box]
        
        # find twin in row peers
        for peer in peersRow[box]:
            if (values[peer] == digit and peer != box):
                twin_values_row[peer] = digit;
        # find twin in column peers
        for peer in peersCol[box]:
            if (values[peer] == digit and peer != box):
                twin_values_col[peer] = digit;        
        # find twin in square peers
        for peer in peersSqr[box]:
            if (values[peer] == digit and peer != box):
                twin_values_sqr[peer] = digit;

    # remove twins values from row peers
    for box in twin_values_row:
        digit = values[box]
        if len(digit) == 2:
            digit1 = digit[0];
            digit2 = digit[1];
            for peer in peersRow[box]:
                if len(values[peer]) > 1 and values[peer] != digit:
                    assign_value(values, peer, values[peer].replace(digit1,''))   
                    assign_value(values, peer, values[peer].replace(digit2,''))
     
    # remove twins values from column peers
    for box in twin_values_col:
        digit = values[box]
        if len(digit) == 2:
            digit1 = digit[0];
            digit2 = digit[1];
            for peer in peersCol[box]:
                if len(values[peer]) > 1 and values[peer] != digit:
                    assign_value(values, peer, values[peer].replace(digit1,''))   
                    assign_value(values, peer, values[peer].replace(digit2,''))
    
    # remove twins values from square peers
    for box in twin_values_sqr:
        digit = values[box]
        if len(digit) == 2:
            digit1 = digit[0];
            digit2 = digit[1];
            for peer in peersSqr[box]:
                if len(values[peer]) > 1 and values[peer] != digit:
                    assign_value(values, peer, values[peer].replace(digit1,''))   
                    assign_value(values, peer, values[peer].replace(digit2,''))

    return values
    

def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    pass

    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            assign_value(values, peer, values[peer].replace(digit,''))
    
    return values


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """         
    pass
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                assign_value(values, dplaces[0], digit)
    return values;

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    stalled = False
    while not stalled:
        
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        
        # Use the Eliminate Strategy
        values = eliminate(values)

        # Use the Only Choice Strategy
        values = only_choice(values)

        # Use the Naked Twins Strategy
        values = naked_twins(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    
    return values


def search(values):
    pass
    # Using depth-first search and propagation, try all possible values.
    # First, reduce the puzzle using the previous function

    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt;

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    pass 

    return search(grid_values(grid))

if __name__ == '__main__':

    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    test1_sudoku_grid = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
    test2_sudoku_grid = '6.5.3.4.....59.......16...5........1...3......7.6859......53....5............6.5.'
    test3_sudoku_grid = '.....8..1..1............5.......3...6.3..52.....2....3.3...4....6.51....9........'

    display(solve(test3_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
