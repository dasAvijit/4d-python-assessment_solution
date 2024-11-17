import pandas as pd
from src.configs.file_configs import CONFIGS
from src.configs.schemas import *

def validate_data(source_name, dataframe):

    clean_rows = pd.DataFrame(columns=dataframe.columns)
    error_rows = pd.DataFrame(columns=dataframe.columns)
    
    if source_name in CONFIGS.keys():
        expected_schema =  CONFIGS[source_name]
    


    return clean_rows, error_rows
