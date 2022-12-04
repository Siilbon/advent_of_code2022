#%%
data_path = 'p1_data.txt'

#%% Functions


def calories_list(data_path):
    '''Builds a list containing all the cal counts of each elf'''
    with open(data_path) as data_file:

        data_lines = data_file.readlines()
        cal_counts = []
        cal_count = 0

        # Build a list of the subtotals
        for line in data_lines:
            try:
                line = int(line)
                cal_count += line
            except ValueError:
                cal_counts.append(cal_count)
                cal_count = 0

        # add the last total to the list
        cal_counts.append(cal_count)

    return cal_counts


def max_calories(data_path, num=1):
    '''Returns total max cal count of a number of elves'''
    cal_counts = calories_list(data_path)
    cal_counts.sort(reverse=True)
    max_cal_count = sum(cal_counts[:num])
    return max_cal_count


#%% Part 01
print(f'D01P1 solution: {max_calories(data_path)}')

#%% Part 02
print(f'D01P2 solution: {max_calories(data_path, 3)}')