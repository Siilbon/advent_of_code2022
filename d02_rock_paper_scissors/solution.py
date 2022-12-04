#%%
import pandas as pd

# Files
data_path = 'p1_data.txt'
test_data_path = 'test_data.txt'

# Conversion Dictionaries
opponent_dict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
your_dict = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
p2outcome_dict = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
shape_score_dict = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
outcome_score_dict = {'Lose': 0, 'Draw': 3, 'Win': 6}


#%% Functions
class strategy_df:

    def __init__(self, data_path, part):
        self.path = data_path
        self.part = part
        self.df = self.build_df()

    def build_df(self):
        df = pd.read_csv(self.path, sep=' ', names=['opponent_move', 1])
        df['opponent_move'] = df['opponent_move'].map(opponent_dict)

        # determine outcome for part 1
        if self.part == 1:
            df = df.rename(columns={1: 'your_move'})
            df['your_move'] = df['your_move'].map(your_dict)
            df['outcome'] = df.apply(lambda row: rock_paper_scissors(
                opponent_move=row['opponent_move'], your_move=row['your_move'
                                                                  ]),
                                     axis=1)

        # determine your move for part 2
        if self.part == 2:
            df = df.rename(columns={1: 'outcome'})
            df['outcome'] = df['outcome'].map(p2outcome_dict)
            df['your_move'] = df.apply(lambda row: rock_paper_scissors_move(
                opponent_move=row['opponent_move'], outcome=row['outcome']),
                                       axis=1)

        df['shape_score'] = df['your_move'].map(shape_score_dict)
        df['outcome_score'] = df['outcome'].map(outcome_score_dict)
        df['round_score'] = df['shape_score'] + df['outcome_score']
        return df


def rock_paper_scissors(opponent_move, your_move):
    '''takes an opponent move and your move and finds the outcome'''
    if opponent_move == your_move:
        return 'Draw'
    elif opponent_move == 'Rock':
        if your_move == 'Paper':
            return 'Win'
        elif your_move == 'Scissors':
            return 'Lose'
    elif opponent_move == 'Paper':
        if your_move == 'Scissors':
            return 'Win'
        elif your_move == 'Rock':
            return 'Lose'
    elif opponent_move == 'Scissors':
        if your_move == 'Rock':
            return 'Win'
        elif your_move == 'Paper':
            return 'Lose'
    else:
        return 'ERROR'


def rock_paper_scissors_move(opponent_move, outcome):
    '''takes an opponent move and outcome and finds your move'''
    if outcome == 'Lose':
        return {
            'Rock': 'Scissors',
            'Paper': 'Rock',
            'Scissors': 'Paper'
        }[opponent_move]

    elif outcome == 'Draw':
        return opponent_move

    elif outcome == 'Win':
        return {
            'Rock': 'Paper',
            'Paper': 'Scissors',
            'Scissors': 'Rock'
        }[opponent_move]

    else:
        return 'ERROR'


def total_score(data_path, part=1):
    df = strategy_df(data_path=data_path, part=part).df
    total_score = sum(df['round_score'])
    return total_score


#%% Part 01
print(f'D02P1 solution: {total_score(data_path=data_path)}')

# %%
print(f'D02P2 solution: {total_score(data_path=data_path, part=2)}')
