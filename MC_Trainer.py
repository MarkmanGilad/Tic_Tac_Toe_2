from TicTacToe import TicTacToe
from State import State
from Human_Agent import Human_Agent
from Random_Agent import Random_Agent
from MC_Agent import MC_Agent

PATH = 'Data/Q_3.pth'

env = TicTacToe(State())
player1 = MC_Agent(1, env, graphics=None, Q_table_PATH=None)
player2 = Random_Agent(-1, env,graphics=None)

gamma = 0.9

def main ():
    player = player1    
    epochs = 100000
    alpha = 0.1
    
    for epoch in range(epochs):
        episode = Generate_episode(player, epoch)
        G = 0
        episode.pop()
        for t in range(len(episode)):
            state, action, reward = episode.pop() # LIFO - Stack
            G = gamma* G + reward
            if (state, action) in player.Q:
                Q_value = player.Q[(state, action)]
            else:
                Q_value = 0
            player.Q[(state, action)] = Q_value + alpha * (G - Q_value)
        print(epoch, end="\r")
    
    player.save_Q(PATH)
    print(test(100))

def Generate_episode (player, epoch):
    episode = []
    state = State()
    while not env.end_of_game(state):
        action = player.get_action(state=state, epoch=epoch)
        next_state, reward = env.next_state(state,action)
        step = state, action, reward
        episode.append(step)
        state = next_state
        player = switch_players(player)

    episode.append((state,))
    return episode

def test (num):
    x_win = 0
    o_win = 0
    tie = 0
    player = player1
    player.train=False
    player.load_Q(PATH)
    for n in range(num):
        state = State()
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
    return x_win, o_win, tie

def print_episodes (episode):
    for i, e in enumerate(episode):
        print(f'\n i= {i} player = {e[0].player} ')
        for i in e:
            print (i, end=" ")

def switch_players(player):
    if player == player1:
        return player2
    else:
        return player1

if __name__ == '__main__':
    # main()
    print(test(100))