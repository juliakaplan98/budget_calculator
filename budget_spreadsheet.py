import pandas as pd
import numpy as np
from pandasgui import show

# category list  
categories =  ['Household Items', 'Toiletries', 'Transportation', 'Clothing', 'Dry Cleaning', 'Groceries', 'Dining Out', 'Pet', 'Entertainment'] 

# empty dataframe with column names
budget_df = pd.DataFrame(columns = categories, index=(['12/01/2023','12/02/2023','12/03/2023','12/04/2023','12/05/2023','12/06/2023','12/07/2023',
                                                       '12/08/2023','12/09/2023','12/10/2023','12/11/2023','12/12/2023','12/13/2023','12/14/2023',
                                                       '12/15/2023','12/16/2023','12/17/2023','12/18/2023','12/19/2023','12/20/2023','12/21/2023',
                                                       '12/22/2023','12/23/2023','12/24/2023','12/25/2023','12/26/2023','12/27/2023','12/28/2023',
                                                       '12/29/2023','12/30/2023','12/31/2023'])) 

# display dataframe 
print(budget_df)