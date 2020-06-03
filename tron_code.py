import sys
import math
import numpy as np
import random


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

### flood fill

def voroni_diagram(player_dict,my_simulated_location,my_player_key,map_copy,empty_map_field):
    emergency_break = 0
    colours = {}
    player_stack = {}
    n_locs_in_player_stack = 0
    #for each player get closest nodes.
    for player in player_dict:

        player_stack[player] = []
        current_loc = player_dict[player][2:4].copy()

        if player == my_player_key:
            current_loc = my_simulated_location

        
        current_colour = player
        colours[current_colour] = 0
        current_loc_value = map_copy[current_loc[0],current_loc[1]]
        print(["voro current_loc", current_loc,"current_loc_value",current_loc_value,"current_colour]",colours[current_colour]], file=sys.stderr) 
        #get next nodes
        if current_loc_value == empty_map_field:
            map_copy[current_loc[0],current_loc[1]] = current_colour
            colours[current_colour] += 1
            print(["colours", colours], file=sys.stderr) 
            #get next locs for each current loc. 
            player_stack[player].extend(get_legal_locs(current_loc))
            n_locs_in_player_stack += len(player_stack[player])
        else:
            n_locs_in_player_stack += len(player_stack[player])
            player_stack[player].extend(get_legal_locs(current_loc))
        

            #update map for these. 
    #start loop
    while n_locs_in_player_stack > 0:
        emergency_break += 1
        n_locs_in_player_stack = 0
        for player in player_dict:
            #get current player stack
            current_colour = player
            current_player_stack = player_stack[player]
            #reset player stack
            player_stack[player] = []
            if len(current_player_stack) > 0:
                for current_loc in current_player_stack:
                    current_loc_value = map_copy[current_loc[0],current_loc[1]]
                    if current_loc_value == empty_map_field:
                        map_copy[current_loc[0],current_loc[1]] = current_colour
                        colours[current_colour] += 1
                        player_stack[player].extend(get_legal_locs(current_loc))
                        n_locs_in_player_stack += len(player_stack[player])
        if emergency_break > 100:
            return colours[my_player_key]
    return colours[my_player_key]

def voroni_flood_fill_2(current_loc,current_colour,colours,map_copy,empty_map_field):
    #emergency break
    emergency_break = 0
    n_loc_stack = []
    # 1 append neighbours to stack
    n_loc_stack.extend(get_legal_locs(current_loc))
    #node_dict = remove_node(current_loc,node_dict)  
    #start while loop.
    while len(n_loc_stack) >= 1:
        

        emergency_break += 1
        
        #2 get first item in stack
        top_of_stack=n_loc_stack[0]
              

        #3 check if top_of_stack coords are empty.if so give map location current colour and add nodes to stack. 
        if map_copy[top_of_stack[0],top_of_stack[1]] == empty_map_field:
            map_copy[top_of_stack[0],top_of_stack[1]] = current_colour
            colours[current_colour] += 1
            #4 add neighbour nodes to stack.
            for neighbour_loc in get_legal_locs(top_of_stack):#get_neighbour_nodes(top_of_stack,node_dict):
                if neighbour_loc not in n_loc_stack:
                    n_loc_stack.append(neighbour_loc)
            #n_nodes_stack.extend()
        
        #5 remove top of stack from stack:
        n_loc_stack.pop(0)
        

        # check if more than 100 turns. if so reset stack.
        if emergency_break > 200:
            n_loc_stack = []




def flood_fill_2(current_loc,current_colour,colours,map_copy,empty_map_field):
    #emergency break
    emergency_break = 0
    n_loc_stack = []
    # 1 append neighbours to stack
    n_loc_stack.extend(get_legal_locs(current_loc))
    #node_dict = remove_node(current_loc,node_dict)  
    #start while loop.
    while len(n_loc_stack) >= 1:
        

        emergency_break += 1
        
        #2 get first item in stack
        top_of_stack=n_loc_stack[0]
              

        #3 check if top_of_stack coords are empty.if so give map location current colour and add nodes to stack. 
        if map_copy[top_of_stack[0],top_of_stack[1]] == empty_map_field:
            map_copy[top_of_stack[0],top_of_stack[1]] = current_colour
            colours[current_colour] += 1
            #4 add neighbour nodes to stack.
            for neighbour_loc in get_legal_locs(top_of_stack):#get_neighbour_nodes(top_of_stack,node_dict):
                if neighbour_loc not in n_loc_stack:
                    n_loc_stack.append(neighbour_loc)
            #n_nodes_stack.extend()
        
        #5 remove top of stack from stack:
        n_loc_stack.pop(0)
        

        # check if more than 100 turns. if so reset stack.
        if emergency_break > 200:
            n_loc_stack = []


    # 2 for neighbour in neighbours
    # 3 if neighbour == ""
    # 4 map_color = current_colour

def flood_fill(xy_start,map_copy,empty_map_field = ""):
    #how many nodes can be accsesed from that location. 
    #get list neighbour locations
    n_locs_start=get_legal_locs(xy_start)
    #MARK start loc on map.
    map_copy[xy_start[0],xy_start[1]] = "S"
    
    #for each neighbour loc. get the number of available squares.
    loc_colours = [] ## [x,y,colour]
    colours = {"A":0,"B":0,"C":0,"D":0}
    colour_pallet = ["A","B","C","D"]
    
    for n in range(len(n_locs_start)):
        current_loc = n_locs_start[n]
        current_colour = colour_pallet[n]
        current_loc_value = map_copy[current_loc[0],current_loc[1]]
        #check if empty 
        if current_loc_value == empty_map_field:
            map_copy[current_loc[0],current_loc[1]] = current_colour
            colours[current_colour] += 1

            #if empty loc colour == current colour.
            loc_colours.append([current_loc[0],current_loc[1],current_colour])
            #start flood fill 2
            flood_fill_2(current_loc,current_colour,colours,map_copy,empty_map_field)
        elif current_loc_value in colour_pallet:
            loc_colours.append([current_loc[0],current_loc[1],current_loc_value])
            
    print([" loc_colours", loc_colours], file=sys.stderr) 
    #check all starting nodes colours. 
    loc_output = []
    #get maxium colour value. 
    max_col_val = max(colours.values())
    #check node colour. if node colour value == max_col_val.
    for col_loc in loc_colours:
        if colours[col_loc[2]] == max_col_val:
            loc_output.append([col_loc[0],col_loc[1]])
    
    return loc_output # list of adjacent_nodes with biggest floodfill colour. 



def flood_fill_n_squares(xy_start,map_copy,empty_map_field = ""):
    #how many nodes can be accsesed from that location. 
    #get list neighbour locations
    n_locs_start=get_legal_locs(xy_start)
    #MARK start loc on map.
    map_copy[xy_start[0],xy_start[1]] = "S"
    
    #for each neighbour loc. get the number of available squares.
    loc_colours = [] ## [x,y,colour]
    colours = {"A":0,"B":0,"C":0,"D":0}
    colour_pallet = ["A","B","C","D"]
    
    for n in range(len(n_locs_start)):
        current_loc = n_locs_start[n]
        print(["current_loc",current_loc ], file=sys.stderr)    
        current_colour = colour_pallet[n]
        current_loc_value = map_copy[current_loc[0],current_loc[1]]
        #check if empty 
        if current_loc_value == empty_map_field:
            map_copy[current_loc[0],current_loc[1]] = current_colour
            colours[current_colour] += 1

            #if empty loc colour == current colour.
            loc_colours.append([current_loc[0],current_loc[1],current_colour])
            #start flood fill 2
            flood_fill_2(current_loc,current_colour,colours,map_copy,empty_map_field)
        elif current_loc_value in colour_pallet:
            loc_colours.append([current_loc[0],current_loc[1],current_loc_value])
            
    print([" loc_colours", loc_colours], file=sys.stderr) 
    #check all starting nodes colours. 
    loc_output = []
    #get maxium colour value. 
    max_col_val = max(colours.values())
    return max_col_val


def get_legal_locs(xy_loc,width = 30,height = 20):
    x_cie=xy_loc[0]
    y_cie=xy_loc[1]

    legal_locs= []
    #check if right is legal
    if x_cie + 1 < width:
        legal_locs.append([x_cie + 1,y_cie])

    #check if left is legal
    if x_cie - 1 >= 0 :
        legal_locs.append([x_cie - 1,y_cie])

    #check if up is legal
    if y_cie - 1 >= 0:
        legal_locs.append([x_cie,y_cie - 1])

    #check if DOWN is legal
    if y_cie + 1 < height:
        legal_locs.append([x_cie,y_cie + 1])

    
    return legal_locs


### get output
def get_output(current_loc,target_loc):

    #check what command to give to get to target_loc
    if current_loc[0] < target_loc[0]:
        return "RIGHT"

    elif current_loc[0] > target_loc[0]:
        return "LEFT" 
    
    elif current_loc[1] > target_loc[1]:
        return "UP" 
    elif current_loc[1] < target_loc[1]:
        return "DOWN" 


### functions
def update_map_t1(player_dict,current_player_key,game_map):
    x_um = player_dict[current_player_key][0]
    y_um = player_dict[current_player_key][1]
    game_map[x_um,y_um] = current_player_key


def update_map(player_dict,current_player_key,game_map):
    x_um = player_dict[current_player_key][2]
    y_um = player_dict[current_player_key][3]
    game_map[x_um,y_um] = current_player_key


def update_map_dead(current_player_key,game_map):
    game_map[game_map == str(current_player_key)] = empty_fields
 


def get_legal_neighbours(xy_loc,sim_game_map,filled_with):
    x_cie=xy_loc[0]
    y_cie=xy_loc[1]

    legal_locs= []
    #check if right is legal
    if x_cie + 1 < 30:
        if sim_game_map[x_cie + 1,y_cie] == filled_with: 
            legal_locs.append([x_cie + 1,y_cie])

    #check if left is legal
    if (x_cie - 1 >= 0) :
        if sim_game_map[x_cie - 1,y_cie] == filled_with: 
            legal_locs.append([x_cie - 1,y_cie])

    #check if up is legal
    if y_cie - 1 >= 0:
        if sim_game_map[x_cie,y_cie - 1] == filled_with: 
            legal_locs.append([x_cie,y_cie - 1])

    #check if DOWN is legal
    if y_cie + 1 < 20:
        if sim_game_map[x_cie,y_cie + 1] == filled_with: 
            legal_locs.append([x_cie,y_cie + 1])

    
    return legal_locs


def get_legal_moves(player_dict,the_player_key,sim_game_map):
    x_cie=player_dict[the_player_key][2]
    y_cie=player_dict[the_player_key][3]

    legal_moves = []
    #check if right is legal
    if x_cie + 1 < 30:
        if sim_game_map[x_cie + 1,y_cie] == empty_fields: 
            legal_moves.append("RIGHT")

    #check if up is legal
    if y_cie - 1 >= 0:
        if sim_game_map[x_cie,y_cie - 1] == empty_fields: 
            legal_moves.append("UP")

    #check if left is legal
    if (x_cie - 1 >= 0) :
        if sim_game_map[x_cie - 1,y_cie] == empty_fields: 
            legal_moves.append("LEFT")

    #check if DOWN is legal
    if y_cie + 1 < 20:
        if sim_game_map[x_cie,y_cie + 1] == empty_fields: 
            legal_moves.append("DOWN")

    
    return legal_moves




#### initial variables
my_last_move = None
#game map
empty_fields = ""
WIDTH = 30
HEIGHT = 20
game_map = np.full([WIDTH,HEIGHT],empty_fields)

#make dictionary of graph adjacency.
#node_adjacency_dict = get_graph_adjacency_list()

### improvvements
# if possible try to stay 2 away from border. 
# if possible go for move that has most legal moves in future

### make graph of board. 
# each [x,y] is a node. Get all neighbour nodes. 
# every place we go to we mark as visited. 
#  
alive_players ={}
current_turn = 0
# game loop
while True:
    current_turn +=1
    # n: total number of players (2 to 4).
    # p: your player number (0 to 3).
    n, p = [int(i) for i in input().split()]
    #my_player_key = "P"+str(p)
    my_player_key = p
    player_dict = {}
    
    for current_player_key in range(n):
        # x0: starting X coordinate of lightcycle (or -1)
        # y0: starting Y coordinate of lightcycle (or -1)
        # x1: starting X coordinate of lightcycle (can be the same as X0 if you play before this player)
        # y1: starting Y coordinate of lightcycle (can be the same as Y0 if you play before this player)
        x0, y0, x1, y1 = [int(j) for j in input().split()]
        

        
        player_dict[current_player_key] = [x0,y0,x1,y1]
        print(["current player",player_dict[current_player_key]], file=sys.stderr)        
        
        if current_turn == 1:
            update_map_t1(player_dict,current_player_key,game_map)
            alive_players[current_player_key] = "alive"
            
        #check if anyone died. if so. change their values to ""
        if (player_dict[current_player_key][0] == -1) and (alive_players[current_player_key] == "alive"): 
            alive_players[current_player_key] = "dead"
            player_dict.pop(current_player_key,None)
            update_map_dead(current_player_key,game_map)
            print(["game_map",game_map], file=sys.stderr)
        
        if alive_players[current_player_key] == "alive":
            update_map(player_dict,current_player_key,game_map)


    print(["my coords",player_dict[my_player_key]], file=sys.stderr)

       
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line with UP, DOWN, LEFT or RIGHT
    #potential_moves=get_legal_moves(player_dict,my_player_key,game_map)
    #print(["GAME MAP",game_map], file=sys.stderr)
    
   
    my_location = player_dict[my_player_key][2:4]
    
    map_copy = game_map.copy()
    #for players taking turn after me. check if they can box me in. 
    for player_id in player_dict:
        if player_id > my_player_key:
            player_location = player_dict[player_id][2:4]            
            for legal_loc in get_legal_locs(player_location):
                if map_copy[legal_loc[0],legal_loc[1]] == empty_fields:
                    #map_copy[legal_loc[0],legal_loc[1]] = player_id
                    None



    best_adjacent_nodes=flood_fill(my_location,map_copy, "")
    print([" best_adjacent_nodes", best_adjacent_nodes], file=sys.stderr) 


    #for best adjacent nodes choose the one that maximises voroni score. 
    voroni_results={}
    voroni_output =[]
    voroni_winners =[]
    for my_simulated_location in best_adjacent_nodes:
        map_copy = game_map.copy()
        #map_copy[my_simulated_location[0],my_simulated_location[1]] = my_player_key
        voroni_output.append(voroni_diagram(player_dict,my_simulated_location,my_player_key,map_copy,empty_fields))

    for my_simulated_location,voroni_out in zip(best_adjacent_nodes,voroni_output):    
        #for i in range(len(my_simulated_location)):
        #my_simulated_locationp[i]
        #voroni_output[i]
        print([" voroni_out", voroni_out,"voroni_output",voroni_output], file=sys.stderr)
        if voroni_out >=  max(voroni_output):
            voroni_winners.append(my_simulated_location)
            

         
    # check if best adjacent nodes are within 1 space of enemy. whos turn is after mine.  
    # check if any of best adjacent nodes are next to a wall. if so, leave a space. 
    possible_outputs = []

    #for adj_node in best_adjacent_nodes:
    for adj_node in voroni_winners:
        possible_outputs.append(get_output(my_location,adj_node))

    print(["my_last_move",my_last_move,"possible_outputs",possible_outputs], file=sys.stderr) 
    if my_last_move in possible_outputs:
        output = my_last_move

    else:
        output = possible_outputs[0]
        my_last_move=output
    #n=random.randint(0,len(possible_outputs)-1)
    print(["my_last_move",my_last_move,"possible_outputs",possible_outputs], file=sys.stderr) 
    #print(possible_outputs[n])
    print(possible_outputs[0])





