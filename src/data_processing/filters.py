import pandas as pd
import numpy as np

def select_bien(df):
    
    try:
        print("Filtering property types...")

        # Keep 'Ventes' transactions
        df = df[df['nature_mutation'] == 'Vente']
        # Keep the 'Maison' and 'Appartement' properties
        df = df.loc[df['type_local'].isin(['Maison', 'Appartement'])]
        # Keep only properties with known locations
        # our analysis heavily relies on property location
        df = df[(df['latitude'].notna()) & (df['longitude'].notna())]

        return df

    except Exception as e:
        print(f"Error: {e}")
        return None


def filtre_dur(df, bati, piece, local, metropole_name=None):
    """
    Filter out outlier values for a given metropolitan area and property type.

    Parameters:
    df (pd.DataFrame): Input dataset.
    bati (int): Maximum allowed building surface.
    piece (int): Maximum allowed number of rooms.
    local (str): Type of property ('Maison' or 'Appartement').
    metropole_name (str, optional): Name of the metropolitan area to be filtered.

    Returns:
    pd.DataFrame: The filtered dataset.
    
    """
    try:
        # if a metropole name is given, filter data for the given local in that metropole
        if metropole_name:
            print(f"Filtering data for '{local}' in '{metropole_name}'...")

            df_metropole = df[(df['type_local'] == local) & (df['LIBEPCI'] == metropole_name)]
            df_other_metropoles = df[(df['LIBEPCI'] != metropole_name) | ((df['LIBEPCI'] == metropole_name) & (df['type_local'] != local))]
        else:
            # if no metropole name is given, filter data for the given local across all metropoles
            print(f"Filtering data for '{local}'")
            df_metropole = df[df['type_local'] == local]
            df_other_metropoles = df[df['type_local'] != local]

        # filter data based on given bati and piece constraints
        df_metropole = df_metropole[(df_metropole['surface_reelle_bati'] <= bati) &
                                    (df_metropole['nombre_pieces_principales'] <= piece)]

        # merge filtered data for the given local in metropole with data for other metropoles
        filtered_df = pd.concat([df_metropole, df_other_metropoles])

        return filtered_df
    
    except Exception as e:
        print(f"Error occurred in filtre_dur(): {str(e)}")
        return None


def filtre_prix(df, metric_prix, quantile_nv = 0.99):
    """ 
    Compute the 99th percentile for each city (more precise than EPCI) and property type (Appartement, Maison)
    Filter properties based on their price per square meter being below the 99th percentile

    ++++++ Be careful to use the discounted price ++++++

    Parameters:
    df (pd.DataFrame): Input dataset.
    metric_prix (str): Name of the column with the price data.
    quantile_nv (float, optional): The quantile value to compute (default is 0.99).

    Returns:
    pd.DataFrame: The filtered dataset.

    """
    try:
        print('Filtering prices...')

        # Remove properties with prices below 1000 euros per square meter or above 20000 euros per square meter
        df = df[(df[metric_prix] >= 1000) & (df[metric_prix] <= 20000)]

        # Compute the 99th percentile for each city and property type
        quantile_per_city_type = (
                df.groupby(['nom_commune', 'type_local'])
                .agg({metric_prix: lambda x: np.quantile(x, quantile_nv)})
                .reset_index()
                .rename(columns={metric_prix: 'quantile_prix'})
            )

        # Merge the 99th percentile values with the original DataFrame
        df = df.merge(quantile_per_city_type, on=['nom_commune', 'type_local'], how='left')
        # Filter out properties with prices per square meter above the 99th percentile
        filterd_df = df[df[metric_prix] < df['quantile_prix']]

        return filterd_df

    except Exception as e:
        print(f"Error in filtre_prix: {str(e)}")
        return None