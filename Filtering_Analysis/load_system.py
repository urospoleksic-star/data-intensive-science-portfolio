

import numpy as np



def print_matrix(grid, C):
    
    b_disp = ['b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7']
    
    
    grid = grid.round(2)
    C = C.round(2)
    
    eq_num = grid.shape[0]
    m = grid.shape[1]
    
    print("\n\n")
    
    for i in range(0,eq_num):
    
        disp_str = ""
        
        for j in range(0,m):
            
            tmp = grid[i, j]
            
            if tmp != 0:
                if tmp < 0:
                    tmp_str = " " + str(tmp) + "*" + b_disp[j]
                else:
                    tmp_str = " +" + str(tmp) + "*" + b_disp[j]
                
                disp_str += tmp_str
        
        disp_str += " = " + str(C[i])   
        
        print(disp_str)



if __name__ == '__main__':

    print('\nScript to load system of equations. Three arrays. They contain A, b and solution respectively (Linear system: Ax = b).\n')
    
   
    # Load arrays from files:
    A_array = np.load('A_array.npy', allow_pickle=True)
    b_array = np.load('b_array.npy', allow_pickle=True)
    solutions_array = np.load('solutions_array.npy', allow_pickle=True)
    
    print("\nA array shape:", A_array.shape)
    print("b array shape:", b_array.shape)
    print("solutions array shape:", solutions_array.shape)
    
    
    # Get system at index i:
    i = 0

    A = A_array[i]
    b = b_array[i]
    solution = solutions_array[i]
    
    print("\nA shape:", A.shape)
    print("b shape:", b.shape)
    print("Solutions shape:", solution.shape)
    
    print("\n>> A:\n", A)
    print("\n>> b:\n", b)
    print("\n>> solution:\n", solution)
    
    # Print system:
    print_matrix(A, b)
