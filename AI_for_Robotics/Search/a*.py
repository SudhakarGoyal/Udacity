import sys
import numpy as np

mat = np.array([[0,0,0,0,0,0],
                [0,1,1,1,1,0],
                [0,1,0,0,0,0],
                [0,1,0,0,0,0],
                [0,1,0,0,1,0]])
src_x = 0     #starting point row
src_y = 0     #starting pint col
r_max = np.shape(mat)[0]   #grid size row
c_max = np.shape(mat)[1]   #grid size col
inc_rows = np.array([-1,0,0,1])  #we search for path around the current grid. We have four cells one above, one at bottom and two in the sides
inc_cols = np.array([0,-1,1,0])

action = np.array([[-1 for i in range(np.shape(mat)[1])] for j in range(np.shape(mat)[0])]) # store action on the basis of inc_rows and inc_cols line inc_rows[0] and inc_cols[0] represent going up
action_grid = np.array(['^','<','>','v'])  #representation of action taken
current_grid = []
visited = np.zeros([np.shape(mat)[0], np.shape(mat)[1]])# 1 if the grid point is visited else 0

heuristic = np.zeros([np.shape(mat)[0], np.shape(mat)[1]])
for i in range(np.shape(mat)[0]):
    for j in range( np.shape(mat)[1]):
        heuristic[i][j] = np.shape(mat)[0] + np.shape(mat)[1] -(i+j) -2 # -2 because shape is row+1,col+1
        
def search(src_x, src_y, dest_x, dest_y):
   
    found = False
    
    curr_i = src_x
    curr_j = src_y
    
    dist = np.zeros([np.shape(mat)[0] ,np.shape(mat)[1]]) #matrix to store distance of every grid cell for starting point
    current_grid.append([curr_i,curr_j])
    final_dist =  np.zeros([np.shape(mat)[0] ,np.shape(mat)[1]])
    visited[curr_i,curr_j] =1   # make the strating point  visited


    final_hue = []
    final_path = []
    final_hue.append([dist[src_x,src_y],src_x,src_y])
# =============================================================================
#     print(np.shape(current_grid))
# =============================================================================
    while(np.shape(current_grid)[0]>0 or (curr_i!=dest_x and curr_j!=dest_y)):
    
# =============================================================================
#         curr_i, curr_j = current_grid.pop(0) # pop the first elt in the vector
# =============================================================================
        final_hue.sort()
        
        temp_dist,curr_i, curr_j = final_hue.pop(0)
        print('final_hue',final_hue)
        print(curr_i, curr_j)
        
        
        #if wew have reached the destination
        
        if((curr_i == dest_x) and (curr_j == dest_y)): #if reached destination
            found=True
            return dist, final_dist, final_path  
                          
        print(curr_i, curr_j)
        for i in range(0,4): #check the surrounding four grid cells of the current grid cell
            row_ = 0
            col_ = 0
            row_ = curr_i + inc_rows[i]
            col_ = curr_j + inc_cols[i]
        #the row number computed need to be within the grid limits and the grid should not have been visited
            if(row_ >=0 and row_<r_max and col_>=0 and col_ <c_max and visited[row_, col_]==0 and mat[row_][col_]==0 & found==False ):
                visited[row_, col_] = 1      

                dist[row_,col_] = dist[curr_i,curr_j] + 1
                final_dist[row_,col_] = dist[row_,col_] + heuristic[row_,col_]
                final_hue.append([final_dist[row_,col_],row_,col_])                
                #append action taken like right, down etc
                action[row_,col_] = i                      
             
 #destination    
dest_x = 4
dest_y = 5
dist_, final_dist_, final_path = (search(src_x, src_y, dest_x,dest_y))
# =============================================================================
# print(action)
# =============================================================================
print(dist_)
print(final_dist_)
print("final_path is ",final_path)

# =============================================================================
# print(found_)
# =============================================================================
print('shortest path dist is',(dist_[dest_x,dest_y]))
shortest_path = []
distance = int(dist_[dest_x,dest_y])



