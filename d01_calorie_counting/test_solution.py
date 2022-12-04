#%%
from solution import max_calories


#%% Part 01
def test_max_calories():
    assert max_calories('test_data.txt') == 24000


#%% Part 02
def test_3_max_calories():
    assert max_calories('test_data.txt', 3) == 45000