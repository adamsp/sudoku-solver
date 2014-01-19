'''
Created on 19/01/2014

@author: Adam Speakman

@contact: https://github.com/adamsp

@license: Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import sys
import re

DEBUG = True

def unique(values):
    unique_values = ''.join(set(values))
    # We allow any number of 0's as placeholders, so we check that the unique length without 0's
    # is the same as the original length without 0's - if it is, then original input is unique :)
#    uv_len = len(unique_values)
#    uv_0 = unique_values.count('0')
#    uv_len = uv_len - uv_0
#    val_len = len(values)
#    val_0 = values.count('0')
#    val_len = val_len - val_0
#    result = 
    return (len(unique_values) - unique_values.count('0')) == (len(values) - values.count('0'))

def col(input_grid, index):
    column = ''
    for col in input_grid:
        column += col[index]
    return column

def row(input_grid, index):
    return input_grid[index]

def top_left(input_grid):
    return input_grid[0][:3] + input_grid[1][:3] + input_grid[2][:3]

def top_mid(input_grid):
    return input_grid[0][3:6] + input_grid[1][3:6] + input_grid[2][3:6]    
    
def top_right(input_grid):
    return input_grid[0][6:] + input_grid[1][6:] + input_grid[2][6:]
    
def cen_left(input_grid):
    return input_grid[3][:3] + input_grid[4][:3] + input_grid[5][:3]
    
def cen_mid(input_grid):
    return input_grid[3][3:6] + input_grid[4][3:6] + input_grid[5][3:6]
    
def cen_right(input_grid):
    return input_grid[3][6:] + input_grid[4][6:] + input_grid[5][6:]
    
def bot_left(input_grid):
    return input_grid[6][:3] + input_grid[7][:3] + input_grid[8][:3]
    
def bot_mid(input_grid):
    return input_grid[6][3:6] + input_grid[7][3:6] + input_grid[8][3:6]
    
def bot_right(input_grid):
    return input_grid[6][6:] + input_grid[7][6:] + input_grid[8][6:]
    
def validate_user_input_grid(input_grid):
    if not unique(top_left(input_grid)):
        print "Your top left 3x3 has duplicate entries."
    elif not unique(top_mid(input_grid)):
        print "Your top middle 3x3 has duplicate entries."
    elif not unique(top_right(input_grid)):
        print "Your top right 3x3 has duplicate entries."
    elif not unique(cen_left(input_grid)):
        print "Your center left 3x3 has duplicate entries."
    elif not unique(cen_mid(input_grid)):
        print "Your center middle 3x3 has duplicate entries."
    elif not unique(cen_right(input_grid)):
        print "Your center right 3x3 has duplicate entries."
    elif not unique(bot_left(input_grid)):
        print "Your bottom left 3x3 has duplicate entries."
    elif not unique(bot_mid(input_grid)):
        print "Your bottom middle 3x3 has duplicate entries."
    elif not unique(bot_right(input_grid)):
        print "Your bottom right 3x3 has duplicate entries."
    else: # Nothing invalid! Yay!
        return True
    return False

input_invalid_line_pattern = re.compile("[^0-9]")
def validate_user_input_line(input_grid, user_input):
    if len(user_input) != 9:
        print("Invalid user_input - requires 9 digits.")
    elif input_invalid_line_pattern.match(user_input):
        print("Invalid user_input - numbers 0 through 9 only.")
    elif not unique(user_input):
        print("Invalid user_input - no duplicate entries allowed, except 0 as placeholder.")
    else: 
        return True
    return False

def read_input_grid():
    count = 0
    input_grid = []
    while count < 9:
        user_input = raw_input("Enter line " + str((count + 1)) + ", or 0 to exit: ")
        if user_input == '0':
            print("Exiting.")
            sys.exit()
        elif validate_user_input_line(input_grid, user_input):
            # Have to make an array out of the string here, cos we can't directly update an index later if we don't.
            input_row = []
            for i in user_input:
                input_row.append(i)
            input_grid.append(input_row)
            count += 1
    # And finally a check on 3x3 grids and vertical columns
    if validate_user_input_grid(input_grid):
        return input_grid
    else:
        read_input_grid()
        
def finished(input_grid):
    for line in input_grid:
        if line.count('0') > 0:
            return False
    return True

def missing_entries(values):
    missing = ''
    if values.count('1') == 0:
        missing += '1'
    if values.count('2') == 0:
        missing += '2'
    if values.count('3') == 0:
        missing += '3'
    if values.count('4') == 0:
        missing += '4'
    if values.count('5') == 0:
        missing += '5'
    if values.count('6') == 0:
        missing += '6'
    if values.count('7') == 0:
        missing += '7'
    if values.count('8') == 0:
        missing += '8'
    if values.count('9') == 0:
        missing += '9'
    return missing        

# Merges potential values for a cell from its row, column and grid potentials, into a single set of
def merge_potentials(vals_1, vals_2, vals_3):
    results = ''
    for val in vals_1:
        if vals_2.count(val) == 0 and vals_3.count(val) == 0:
            results += val
    for val in vals_2:
        if vals_1.count(val) == 0 and vals_3.count(val) == 0:
            results += val
    for val in vals_3:
        if vals_1.count(val) == 0 and vals_2.count(val) == 0:
            results += val
    # We may not have any unique entries. In this case, any of these is a potential.
    results = ''.join(set(vals_1 + vals_2 + vals_3))
    return results        
            

input_grid = read_input_grid()
print("Input:")
print(input_grid)
sys.stdout.write("Processing...")
while not finished(input_grid):
    sys.stdout.write(".")
    # Build a collection of missing elements for each row, column and 3x3 'grid'
    row_potentials = []
    for row_index in range(0,9):
        # These are the missing entries for this row
        row_potentials.append(missing_entries(row(input_grid, row_index)))
    col_potentials = []
    for col_index in range(0,9):
        # These are the missing entries for this column
        col_potentials.append(missing_entries(col(input_grid, col_index)))
    grid_potentials = []
    # These are the missing entries for each 3x3 grid
    grid_potentials.append(missing_entries(top_left(input_grid)))
    grid_potentials.append(missing_entries(top_mid(input_grid)))
    grid_potentials.append(missing_entries(top_right(input_grid)))
    grid_potentials.append(missing_entries(cen_left(input_grid)))
    grid_potentials.append(missing_entries(cen_mid(input_grid)))
    grid_potentials.append(missing_entries(cen_right(input_grid)))
    grid_potentials.append(missing_entries(bot_left(input_grid)))
    grid_potentials.append(missing_entries(bot_mid(input_grid)))
    grid_potentials.append(missing_entries(bot_right(input_grid)))
    
    # Each cell has a set of 'potential' entries for its row, and for its column, and for its grid.
    # Must remove any that don't match.
    # For example if an element matched 1,4,5 in its row, 1,4,6 in its column and 1,3,5 in its grid,
    # then it has to be 1 - since 3,4,5,6 are all cancelled out (each of those already exists in some
    # other area)
    potentials_grid = []
    for row_index in range(0,9):
        row_individual_potentials = []
        for col_index in range(0,9):
            cell_potentials = ''
            if input_grid[row_index][col_index] != '0':
                # This cell has already been populated. This is the only potential entry in this cell.
                cell_potentials = input_grid[row_index][col_index]
            else:
                grid_index = (col_index % 3) + 3 * (row_index % 3)
                cell_potentials = merge_potentials(row_potentials[row_index], col_potentials[col_index], grid_potentials[grid_index])
            row_individual_potentials.append(cell_potentials)
        potentials_grid.append(row_individual_potentials)
        
    # Now we have our set of potential entries for each cell. Can we cancel out any more? Sure!
    # If a cell is the only cell in its row, column, or grid which contains a given potential element,
    # then that element must be the entry for that cell.
    # For example if a cell contains potentials [3,5,7] and no other cell in its row, column or grid
    # contains 3 in its potentials, then this cells entry must be the value 3.
    for row_index in range(0,9):
        for col_index in range(0,9):
            if len(potentials_grid[row_index][col_index]) == 1:
                # This cell only has 1 possible entry.
                continue
            for potential in potentials_grid[row_index][col_index]:
                potential_found = False
                # Check other entries in row
                row_potentials = row(potentials_grid, row_index)
                for other_potential in row_potentials[:col_index]:
                    # Entries before the current column
                    if other_potential == potential:
                        potential_found = True
                        break
                if potential_found: # No point checking for more - there's > 1 possible places for this entry.
                    break
                for other_potential in row_potentials[col_index:]:
                    # Entries after the current column
                    if other_potential == potential:
                        potential_found = True
                        break
                if potential_found: # No point checking for more - there's > 1 possible places for this entry.
                    break
                
                # Check other entries in column
                col_potentials = col(potentials_grid, col_index)
                for other_potential in col_potentials[:row_index]:
                    # Entries before the current row
                    if other_potential == potential:
                        potential_found = True
                        break
                if potential_found: # No point checking for more - there's > 1 possible places for this entry.
                    break
                for other_potential in col_potentials[row_index:]:
                    # Entries after the current row
                    if other_potential == potential:
                        potential_found = True
                        break
                if potential_found: # No point checking for more - there's > 1 possible places for this entry.
                    break
                
                # Check other entries in 3x3 grid
                grid_index = (col_index % 3) + 3 * (row_index % 3)
                grid_potentials = []
                if grid_index == 0:
                    grid_potentials = top_left(potentials_grid)
                elif grid_index == 1:
                    grid_potentials = top_mid(potentials_grid)
                elif grid_index == 2:
                    grid_potentials = top_right(potentials_grid)
                elif grid_index == 3:
                    grid_potentials = cen_left(potentials_grid)
                elif grid_index == 4:
                    grid_potentials = cen_mid(potentials_grid)
                elif grid_index == 5:
                    grid_potentials = cen_right(potentials_grid)
                elif grid_index == 6:
                    grid_potentials = bot_left(potentials_grid)
                elif grid_index == 7:
                    grid_potentials = bot_mid(potentials_grid)
                else: # grid_index == 8:
                    grid_potentials = bot_right(potentials_grid)
                
                current_grid_index = (col_index % 3) + 3 * (row_index % 3)
                for other_potential in grid_potentials[:current_grid_index]:
                    # Entries before the current column
                    if other_potential == potential:
                        potential_found = True
                        break
                if potential_found: # No point checking for more - there's > 1 possible places for this entry.
                    break
                for other_potential in grid_potentials[current_grid_index:]:
                    # Entries after the current column
                    if other_potential == potential:
                        potential_found = True
                        break
                if potential_found: # No point checking for more - there's > 1 possible places for this entry.
                    break
                
                # We have not found this potential in any other set of potentials for other elements in its
                # row, column or grid. This is the one!
                potentials_grid[row_index][col_index] = potential
                
    # Finally, we go through our potentials grid and find every potentials list of length 1. This is the entry
    # for that cell, so we put it into our input grid and then go through again until we've found them all.
    for row_index in range(0,9):
        for col_index in range(0,9):
            if len(potentials_grid[row_index][col_index]) == 1:
                input_grid[row_index][col_index] = str(potentials_grid[row_index][col_index])
    
    if DEBUG:
        print input_grid

print("\nDone.")
print("Result:")
print(input_grid)
            

            
