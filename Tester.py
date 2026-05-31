from TicTacToe import TicTacToe
from State import State
from Human_Agent import Human_Agent
from Random_Agent import Random_Agent
from AI_Agent import AI_Agent
from Random_Agent_Advanced import Random_Agent_Advanced

PATH = "Data/Q_MC_2026_2.pth"

env = TicTacToe(State())
player1 = AI_Agent(1, env, graphics=None, Q_table_PATH=PATH, train=False)
# player1 = Random_Agent(1, env,graphics=None)
# player2 = Random_Agent(-1, env,graphics=None)
# player2 = AI_Agent(-1, env, graphics=None, Q_table_PATH=PATH, train=False)
player2 = Random_Agent_Advanced(-1, env=env, graphics=None)
num = 1000

def main ():

    x_win = 0
    o_win = 0
    tie = 0
        
    for n in range(num):
        state = State()
        player = player1
        while not env.end_of_game(state):
            action = player.get_action(state=state)
            state, _ = env.next_state(state,action)
            player = switch_players(player)
        if state.end_of_game == 1:
            x_win +=1
        elif state.end_of_game == -1:
            o_win += 1
        else:
            tie +=1
        state.reset()    
        print(n, end = "\r")
    print()
    print(f"x_win: {x_win}, tie: {tie}, o_win: {o_win}") 

def switch_players(player):
    if player == player1:
        return player2
    else:
        return player1

if __name__ == '__main__':
    main()