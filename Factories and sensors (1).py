
# coding: utf-8

# In[2]:


from plotly.offline import init_notebook_mode, iplot
import plotly.offline
from IPython.display import display, HTML
import numpy as np
import pandas as pd
import datetime
import plotly.graph_objs as go
from plotly.grid_objs import Grid, Column
import plotly.plotly as py
import plotly.graph_objs as go
init_notebook_mode(connected=True)
import pandas as pd
from IPython.html import widgets
dataframe = pd.read_excel("s_f.xlsx")


# In[3]:


factorylocation = dataframe.iloc[0:4,:]
sensorlocation = dataframe.iloc[4:,:]


# In[4]:


factoryinfo = factorylocation['X']
np.array(factoryinfo)


# In[5]:


trace_factories = go.Scatter(
    x = np.array(factorylocation['X']),
    y = np.array(factorylocation['Y']),
    mode = 'markers',
    name = 'Factories',
    text = list(factorylocation['loc']),
    marker = dict(
        size = 10,
        color = 'rgba(255, 182, 193, .9)',
        line = dict(
            width = 2,
        )
    )
)
trace_sensors = go.Scatter(
    x = np.array(sensorlocation['X']),
    y = np.array(sensorlocation['Y']),
    mode = 'markers',
    name = 'sensor_locations',
    text = list(sensorlocation['loc']),
    marker = dict(
        size = 10,
        color = 'rgba(0, 0, 255, .9)',
    )
)


# In[6]:


updatemenus = list([
    dict(active=2,
             buttons=list([   
                dict(label = 'Factories',
                     method = 'update',
                     args = [{'visible': [True, False]},
                             {'title': 'Factories'}]),
                dict(label = 'Sensors',
                     method = 'update',
                     args = [{'visible': [False, True]},
                             {'title': 'Sensors'}]),
                dict(label = 'Both',
                     method = 'update',
                     args = [{'visible': [True]},
                             {'title': 'Both'}])
            ]),
        )
])
layout = go.Layout(
    updatemenus=updatemenus
)
data = [trace_factories, trace_sensors]
fig = {'data':data, 'layout':layout} 
plotly.offline.plot(fig, filename ='s_fac.html', auto_open=False)


# In[7]:


sensorlocation

