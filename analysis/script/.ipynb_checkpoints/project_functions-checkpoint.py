import pandas as pd
def load_and_process(url_or_directory):
    
    df2 = (
        
        pd.read_csv(url_or_directory, encoding="unicode-escape")
        .drop('Unnamed: 11', axis = 1)
        .rename(columns = {'Model' : 'Model_Year', 'Model.1' : 'Model_Name', 'Fuel Consumption' : 'Fuel_Consumption_City', 'Unnamed: 9' : 'Fuel_Consumption_Hwy','Unnamed: 9' : 'Fuel_Consumption_Hwy', 'Unnamed: 10' : 'Fuel_Consumption_Comb', 'CO2' : 'CO2_Rating', 'Smog': 'Smog_Rating'})
        .dropna(axis = 0).reset_index()
        .drop('index', axis = 1)
    )
    
    return df2