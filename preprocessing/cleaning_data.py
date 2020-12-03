import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


<<<<<<< HEAD

=======
def preprocess(url):
    data = pd.read_csv(url)
    df = data.drop(['source', 'garden', 'terrace', 'basement'], axis=1)

    df = df[df['price'].notna()]        # remove some records with null values
    df = df[df['area'].notna()]         # df = df[df['rooms_number'].notna()]
    df = df[df['building_state_agg'].notna()]

    def price_area(df1):    
        df1['coeff'] = np.where(df1['land_surface'] + df1['garden_area'] < 250, 2, np.where(df1['land_surface'] + df1['garden_area'] < 1000, 4, np.where(df1['land_surface'] + df1['garden_area'] < 5000, 8, np.where(df1['land_surface'] + df1['garden_area'] < 10000, 12, 16))))        
        df1['divisor'] = df1['area'] + df1['terrace_area'] + df1['garden_area'] / df1['coeff'] + df1['land_surface']/df1['coeff']
        df1['price_area'] = df1['price']/df1['divisor']
        f = ['open_fire', 'swimming_pool_has', 'furnished', 'equipped_kitchen_has']
        c = [-5000, -15000, -10000, -5000]
        for i in range(len(f)):
            df1['price_area'] += np.where(df1[f[i]] == True, c[i]/df1['divisor'], 0)
        factors = ['AS_NEW', 'JUST_RENOVATED', 'TO_RENOVATE', 'TO_RESTORE']
        rate = [-600, -300, 300, 600]
        for i in range(len(factors)):
            df1['price_area'] += np.where(df1['building_state_agg'] == factors[i],
                                (rate[i]*(df1['area'] + df1['terrace_area'])/df1['divisor']), 0)
        return df1


    df = price_area(df)
    df = df[df['price_area']<20000]     # outliers for price_area

    df2 = df[(df['price_area'] > 500) & (df['price_area']<5500) & (df['rooms_number']<6)   & (df['area']<500)]

    final_df = df2.dropna()




    return final_df.shape
>>>>>>> 5df2c6d63826e2176a7d96208928431615df6a23
