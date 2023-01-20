#!/usr/bin/env python
# coding: utf-8

# In[2]:


# RUN THIS CELL FIRST or the notebook won't work
#!pip install geopandas
import numpy as np
import pandas as pd
import geopandas as gpd
from IPython.display import display
import matplotlib.pyplot as plt

# These help the maps display nicely in the notebook
#get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = [30, 20]

# This line tells iPython to not display warnings.
import warnings
warnings.filterwarnings('ignore')


# In[556]:


ri = gpd.read_file('tl_2020_44_tract')
ri.info()


# In[557]:


pvdCounty = ri[ri.COUNTYFP=='007']
pvdCounty.info()


# In[558]:


pvdCounty['NAME']= pvdCounty['NAME'].astype(str).astype(float)


# In[559]:


pvd = pvdCounty[pvdCounty.NAME < 40]


# In[ ]:





# In[560]:


#get_ipython().system('pip install altair')
#get_ipython().system('pip install gpdvega')
#get_ipython().system('pip install altair vega_datasets')


# In[561]:



# Create the pandas DataFrame
current = pd.read_csv('vendors.csv')

current[['lat', 'long']] = current['Lat/Lon'].str.split(',', expand=True)
 
# print dataframe.
current


# In[562]:



# Create the pandas DataFrame
proposed = pd.read_csv('proposed.csv')

proposed = proposed[:44]


proposed[['lat', 'long']] = proposed['Lat/Lon'].str.split(',', expand=True)
 
# print dataframe.
proposed


# In[563]:



# Create the pandas DataFrame
current_ICERM = pd.read_csv('vendors_ICERM.csv')

current_ICERM[['lat', 'long']] = current_ICERM['Lat/Lon'].str.split(',', expand=True)
 
# print dataframe.
current_ICERM


# In[564]:


import altair as alt
#import gpdvega 




bg = alt.Chart(pvd).mark_geoshape(
).encode( 
).properties( 
    width=800,
    height=500
)


points = alt.Chart(current).mark_circle(color='#ffffff').encode(
    latitude='lat:Q',
    longitude='long:Q',
    size=alt.value(50),


)

bg + points


# In[565]:


income = pd.read_csv('income.csv', index_col = [0])


# In[566]:


income


# In[567]:


income['GEOID']= income['GEOID'].astype(str).astype(str)


# In[568]:


income.count()


# In[569]:


income = income[income['GEOID'].str.len()>10]


# In[570]:


income


# In[571]:


income.rename(index = {"geometry": 'income_geometry'}, inplace = True)
pvd_income = pvd.merge(income, how = 'left', on = 'GEOID')


# In[572]:



gpd_pvd_income = gpd.GeoDataFrame(
    pvd_income[['variable','geometry_x','estimate', 'GEOID']], geometry='geometry_x')


# In[573]:


gpd_pvd_income


# In[579]:


import altair as alt
#import gpdvega 

current_ICERM = current_ICERM[:-1]

gpd_pvd_income['estimate']= gpd_pvd_income['estimate'].astype(int)
bg = alt.Chart(gpd_pvd_income).mark_geoshape(
).encode( color = 'estimate'
).properties( 
    width=800,
    height=800
)


AMS = alt.Chart(current).mark_circle(color='#ffffff',opacity=1).encode(
    latitude='lat:Q',
    longitude='long:Q',
    size=alt.value(50),
    tooltip=["Name:N"]
)


ICERM = alt.Chart(current_ICERM).mark_circle(color='red').encode(
    latitude='lat:Q',
    longitude='long:Q',
    size=alt.value(50),
    tooltip=["Name:N"]
)

proposed_vendors = alt.Chart(proposed).mark_circle(color='black').transform_fold( ['Horsepower', 'Miles_per_Gallon'], as_=['Measure', 'Value'] ).encode(
    latitude='lat:Q',
    longitude='long:Q',
    size=alt.value(50),
    tooltip=["Name:N"]
)

# import random

# proposed_vendors_text = proposed_vendors.mark_text(color='black',align='left',baseline='middle').encode(
#     text='Name:N',

# )




(bg  +  proposed_vendors + ICERM ).save('index.html')


# In[578]:



(bg  +  proposed_vendors + ICERM )


# In[ ]:




current_ICERM
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




