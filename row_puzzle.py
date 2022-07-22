#Author: Eric Daily
#Github Username: edaily00
#date: 6/23/2022
#This program takes a list and uses the element to try to get to the end of the list
def puzzle_helper(pos, nums_list, all_positions):
    """This method is the helper function that holds the positions and all visited positions"""
    length = len(nums_list)-1
    steps = nums_list[pos]
    tru_pos = pos
#The base case is true if position is the end of the list
    if pos == length:
        return True

#The first try statement trys to move left in the list and also checks to see if the position is within the list
#and has not been visited
    try:
        pos += steps
        steps = nums_list[pos]
        if pos in all_positions:
            raise All_Positions_Error
        all_positions.append(pos)
        return puzzle_helper(pos, nums_list, all_positions)
    except IndexError:
        pos -= steps
        pass
    except All_Positions_Error:
        steps = nums_list[tru_pos]
        pos -= steps
#This try statement goes left in the list and makes sure the position is within the list and has not been visited before
    try:
        pos -= steps
        if pos < 0:
            raise IndexError
        steps = nums_list[pos]
        if pos in all_positions:
            raise All_Positions_Error
        all_positions.append(pos)
        return puzzle_helper(pos, nums_list, all_positions)
    except IndexError:
        pos += steps
        pass
    except All_Positions_Error:
        steps = nums_list[tru_pos]
        pos += steps



    if pos in all_positions:
        return False


def row_puzzle(nums_list):
    """This is the recursion function"""

    pos = 0
    all_positions = []
    return puzzle_helper(pos, nums_list, all_positions)

class All_Positions_Error(Exception):
    pass





