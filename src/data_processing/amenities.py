"""
This module contains functions for aggregating and manipulating data related to amenities and equipment 
in different geographic areas of France. 
"""
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from utils.common import read_equi


liste_equipements = [
                ['A203'],['A206'],
                ['B101','B102','B103','B201','B202','B203','B204','B205','B206'],
                ['C101','C102','C104','C105'],
                ['C201','C301','C302','C303','C304','C305'],['D201'],['E107','E108','E109'],['F303'],['F307'],['F313']
            ]

def equipements_prep(liste_iris):
    """
    Aggregate the number of equipment for selected categories at the IRIS level.

    Args:
        liste_iris (list): list of IRIS to include in the aggregation.

    Returns:
        pd.DataFrame: dataframe containing the aggregated number of equipment for the selected 
        categories at the IRIS level.
    
    Raises:
        ValueError: If the input list of IRIS is empty.
    """
    
    print("Adding amenities...")
    
    # Read amenities file
    amenities = read_equi()
    
    # Filter the amenities dataframe to only include IRIS of interest
    amenities = amenities[amenities['DCIRIS'].isin(liste_iris)]
    amenities_df = []

    for equipement in liste_equipements:
        # Filter the amenities dataframe to only include the current equipment category
        amenities_temp = amenities[amenities['TYPEQU'].isin(equipement)]

        # Group the amenities dataframe by DCIRIS and TYPEQU, count the number of occurrences and 
        #store the result in a dataframe
        amenities_temp = amenities_temp.groupby('DCIRIS')['TYPEQU'].value_counts().to_frame()

        # Group the amenities dataframe by DCIRIS, sum the number of equipment and rename the 
        #column to the first equipment name in the list
        amenities_temp = amenities_temp.groupby('DCIRIS').sum()
        amenities_temp = amenities_temp.rename(columns={"TYPEQU": equipement[0]})

        # Append the amenities dataframe to the amenities list
        amenities_df.append(amenities_temp)

    # Concatenate the amenities dataframes in the amenities list, fill the missing values with 0, 
    #and reset the index
    amenities_df = pd.concat(amenities_df).fillna(0)
    amenities_df['DCIRIS'] = amenities_df.index
    amenities_df = amenities_df.reset_index(drop=True)
    
    # drop duplicates and group by IRIS
    amenities_df = amenities_df.drop_duplicates()
    amenities_df = amenities_df.groupby(["DCIRIS"], as_index=False).sum()

    return amenities_df
