
import numpy as np
import pandas as pd



def label_ewine_dataset(f_path):
    
    df_list = []    
        
    for i in range(1, 8):
        
        f = f_path + str(i) + ".csv"
        
        df_tmp = pd.read_csv(f)
        df_list.append(df_tmp)
    
    #df_list = [df1, df2, df3, df4, df5, df6, df7]
    df = pd.concat(df_list, ignore_index=True)
    
    print("\ne-wine num of rows (data instances):", df.shape[0])
    print("e_wine num of columns:", df.shape[1])
    
    
    ## Ensure NLOS labels are integers:
    df['NLOS'] = df['NLOS'].astype(int)
    
  
    ## Insert 'DOMAIN' column between columns 'PRFR and 'CIR0':
    col_index = df.columns.get_loc("CIR0")
    df.insert(col_index, "DOMAIN", 1)
    
    ##new_df.to_csv('e-wine.csv', index=False)          # Save dataframe to CSV file
    
    
    return df
    
    
    
    



def label_industrial_dataset(f_path):
    
    df_list = []    
    
    ## These lists contain the set of LOS anchors for each CSV file, e.g. for CSV file 'exportloc10IQ.csv' the LOS anchors are [11,15,20]
    los_anc_sets = [ [-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[11,15,20],[11,15,20], [5,11,14,15,20,21],
                   [11,15,20], [10,18,21,26,31], [10,18,21,26,31], [10,18,21,26,31], [5,10,18,21,26,31], 
                   [10,18,21,26,29,31,33], [5,6,7,8,26,29,31,33], [11,15,20,26,29,31,33], [3,4,6,16,24,26,29,31,33], 
                   [5,7,8], [5,7,8,26] ]
               
    
    ## Only use 'exportloc10IQ' to 'exportloc23IQ' as these are the only files that have LOS/NLOS labels
    ## Ignore files 'exportloc1IQ' to 'exportloc9IQ'
    for i in range(10, 24):
        
        f = f_path + str(i) + "IQ.csv"
        
        df_tmp = pd.read_csv(f)
        df_list.append(df_tmp)

        df_tmp["LOS"] = (~df_tmp["anchorNumber"].isin(los_anc_sets[i])).astype(int)

    #df_list = [df1, ..., df23]
    df = pd.concat(df_list, ignore_index=True)


    print("\nIndustrial num of rows (data instances):", df.shape[0])
    print("Industrial num of columns:", df.shape[1])
    
    
    ## CIR in this dataset is in complex format (A + jB), so compute magnitude, i.e. M = np.sqrt(A^2 + B^2) for all CIR elements (CIR0 to CIR1015)
    cir_cols = [f'CIR{i}' for i in range(1016)]
    ##df[cir_cols] = df[cir_cols].map(lambda x: abs(complex(x)))        ## Works in newer versions of Pandas
    df[cir_cols] = df[cir_cols].applymap(lambda x: abs(complex(x)))     ## Works in older version of Pandas
    

    
    ## Load e-wine dataset just to extract format of columns:
    new_df = pd.read_csv(r"e-wine/uwb_dataset_part1.csv" )
    print("\nnew_df columns:", new_df.columns )
    
    ## Fill dataframe with empty rows (same number of rows as Industrial dataset). This dataframe will be populated with the
    ## the data from the Industrial dataset, but columns will be assigned to that they match the e-wine column layout
    
    new_df = new_df.iloc[0:0] 
    empty_rows = pd.DataFrame(-1.0, index=range(df.shape[0]), columns=new_df.columns)
    new_df = pd.concat([new_df, empty_rows], ignore_index=True)
    
    ## Now, make it match e_wine columns. Columns that do not exist in Industrial are assigned the value -1.0:
        
    ## e-wine columns:
    #0. NLOS
    #1. RANGE
    #2. FP_IDX
    #3. FP_AMP1
    #4. FP_AMP2
    #5. FP_AMP3
    #6. STDEV_NOISE
    #7. CIR_PWR
    #8. MAX_NOISE
    #9. RXPACC
    #10. CH
    #11. FRAME_LEN
    #12. PREAM_LEN
    #13. BITRATE
    #14. PRFR
    #15. CIR0
    #16. CIR1
    #.
    #.
    #.
    #1029. CIR1014
    #1030. CIR1015

    
    
    new_df['NLOS'] = df['LOS'].astype(int)              ## Column with NLOS labels
    new_df['RANGE'] = df['estimated_range']/1000.0      ## Convert mm to m
    new_df['FP_IDX'] = df['fpindex']/64                 ## Convert to values in the 730 to 760 range similar to e-wine
    new_df['FP_AMP1'] = df['fp_ampl1']
    new_df['FP_AMP2'] = df['fp_ampl2']
    new_df['FP_AMP3'] = df['fp_ampl3']
    new_df['STDEV_NOISE'] = df['std_noise']
    new_df['CIR_PWR'] = df['CIRpower']
    new_df['MAX_NOISE'] = -1.0
    new_df['RXPACC'] = df['RXPACC']
    new_df['CH'] = -1.0
    new_df['FRAME_LEN'] = -1.0
    new_df['PREAM_LEN'] = -1.0
    new_df['BITRATE'] = -1.0
    new_df['PRFR'] = -1.0

    print("\n\n")
    
    for i in range(0, 1016):
        cir_col = 'CIR' + str(i)
        new_df[cir_col] = df[cir_col]  
    
    ## Insert 'DOMAIN' column just before 'CIR0':
    col_index = new_df.columns.get_loc("CIR0")
    new_df.insert(col_index, "DOMAIN", 2)
    
    ##new_df.to_csv('industrial.csv', index=False)          # Save dataframe to CSV file
   
    return new_df




def label_poxyz_dataset(f_path):
    
    df = pd.read_csv(f)
    
    print("\nPoxyz num of rows (data instances):", df.shape[0])
    print("Poxyz num of columns:", df.shape[1])
    
    ## Load e-wine dataset just to extract format of columns:
    new_df = pd.read_csv(r"e-wine/uwb_dataset_part1.csv" )
    print("\nnew_df columns:", new_df.columns )
    
    ## Fill dataframe with empty rows (same number of rows as Poxyz dataset)
    
    new_df = new_df.iloc[0:0] 
    empty_rows = pd.DataFrame(-1.0, index=range(df.shape[0]), columns=new_df.columns)
    new_df = pd.concat([new_df, empty_rows], ignore_index=True)

    
    ## Now, make it match e_wine columns. Columns that do not exist in Pozyx are assigned the value -1.0:
        
    ## e-wine columns:
    #0. NLOS
    #1. RANGE
    #2. FP_IDX
    #3. FP_AMP1
    #4. FP_AMP2
    #5. FP_AMP3
    #6. STDEV_NOISE
    #7. CIR_PWR
    #8. MAX_NOISE
    #9. RXPACC
    #10. CH
    #11. FRAME_LEN
    #12. PREAM_LEN
    #13. BITRATE
    #14. PRFR
    #15. CIR0
    #16. CIR1
    #.
    #.
    #.
    #1029. CIR1014
    #1030. CIR1015
    
    new_df['NLOS'] = df['nlos'].astype(int)      ## Column with NLOS labels
    new_df['RANGE'] = df['range']
    new_df['FP_IDX'] = -1.0
    new_df['FP_AMP1'] = -1.0
    new_df['FP_AMP2'] = -1.0
    new_df['FP_AMP3'] = -1.0
    new_df['STDEV_NOISE'] = -1.0
    new_df['CIR_PWR'] = df['cirPower']
    new_df['MAX_NOISE'] = -1.0
    new_df['RXPACC'] = -1.0
    new_df['CH'] = -1.0
    new_df['FRAME_LEN'] = -1.0
    new_df['PREAM_LEN'] = -1.0
    new_df['BITRATE'] = -1.0
    new_df['PRFR'] = -1.0
    
    for i in range(0, 1016):
        cir_col = 'CIR' + str(i)
        new_df[cir_col] = df[cir_col]
          
    
    ## Insert 'DOMAIN' column just before 'CIR0':
    col_index = new_df.columns.get_loc("CIR0")
    new_df.insert(col_index, "DOMAIN", 3)
    
    #new_df.to_csv('pozyx.csv', index=False)            # Save dataframe to CSV file
    
    return new_df





if __name__ == '__main__':
    
    
    ## 1) e-wine: 
    f = r".\e-wine\uwb_dataset_part"    
    ewine_df = label_ewine_dataset(f)
    
    print("\ne-wine df shape:", ewine_df.shape )
    print("\ne-wine df head:\n", ewine_df.head() )

    

    ## 2) Industrial:
    f = r".\industrial\exportloc"
    industrial_df = label_industrial_dataset(f)

    print("\nIndustrial shape:", industrial_df.shape )
    print("\nIndustrial df head:\n", industrial_df.head() )



    ## 3) Pozyx:
    f = r".\pozyx\pozyx_uwb_dataset.csv"
    poxyz_df = label_poxyz_dataset(f)
    
    print("\nPoxyz shape:", poxyz_df.shape )
    print("\nPoxyz df head:\n", poxyz_df.head() )
    
    
    ## Concatenate all three dataframes into one:
    labeled_df = pd.concat([ewine_df, industrial_df, poxyz_df], ignore_index=True)  
    
    print("\nFull dataset shape:", labeled_df.shape)
    
    labeled_df.to_csv('full_dataset.csv', index=False)            # Save dataframe to CSV file
    
    
    print('\nDone.')
