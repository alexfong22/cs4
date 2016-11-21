####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 10'
strategy_name = 'Collude 90% unless betrayed within last 10 rounds.'
strategy_description = '''
Betray if ever betrayed.
If I haven't been betrayed yet, I'll betray starting with the 100th round.
'''

import random
    
def move(my_history,their_history='',my_score='',their_score='',result=''):
    length_of_history = len(their_history)
    
    if length_of_history >= 10:
        recent_history = their_history[-10:]
        probability_of_b_mid_term = float(recent_history.count('b')) / 10
        
    else:
        probability_of_b_mid_term = 1
        
    even_more_recent_history = their_history[-5:]
    probability_of_b_short_term = float(even_more_recent_history.count('b')) / 5

    do_betray = (probability_of_b_mid_term*.4)+(.6*probability_of_b_short_term) # combine short and long term weighting
    
    #print do_betray,'===probability of betrayal===='
    
    if len(their_history) >= 5:
        rvhb = int(do_betray*100)
        rvhc = 100-rvhb
        weighted_list = ['b'] * rvhb + ['c'] * rvhc
        return random.choice(weighted_list)
        
    if len(their_history) < 5:
        if random.random() > 0.5:
            return 'c'
        else:
            return 'b'
        
print move('bbbbbbbbbbbbbbbbbbbbbbcbbbbbc')

    
    
    