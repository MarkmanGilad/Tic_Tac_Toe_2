from TicTacToe import TicTacToe
from State import State
from Human_Agent import Human_Agent
from Random_Agent import Random_Agent
from MC_Agent import MC_Agent

PATH = 'Data/Q_3.pth'

env = TicTacToe(State())
player1 = MC_Agent(1, env, graphics=None, Q_table_PATH=PATH, train=False)
player2 = Random_Agent(-1, env,graphics=None)
num = 100

def main ():

    x_win = 0
    o_win = 0
    tie = 0
    player = player1
    player.train=False
    player.load_Q(PATH)
    for n in range(num):
        state = State()
        while not env.end_of_game(state):
            action, reward, state = player.get_state_action(state=state)
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
    print(x_win, o_win, tie) 

def switch_players(player):
    if player == player1:
        return player2
    else:
        return player1

if __name__ == '__main__':
    main()