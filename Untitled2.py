
# coding: utf-8

# In[3]:


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
dataframe = pd.read_excel("january_trends.xlsx")


# In[26]:


data = dataframe.as_matrix()
updatemenus = list([
             dict(
                buttons=list([   
                    dict(
                        args=['type', 'surface'],
                        label='3d Surface',
                        method='restyle'
                    ),
                    dict(
                        args=['type', 'heatmap'],
                        label='Heatmap',
                        method='restyle'
                    ),  
                    dict(
                        args=['type', 'contour'],
                        label='Contour',
                        method='restyle'
                    )                     
                ]),pad = {'l': 100, 't': 50})

        ])

datas = [
    go.Surface(
        z=x
    )
]
layout = go.Layout(
            updatemenus = updatemenus
)
fig = {'data':datas,'layout':layout}
#plt = py.iplot(datas, filename='elevations-3d-surface')
plotly.offline.plot(fig, filename = 'trends.html', auto_open=False)


# In[21]:


x = list()
for i in data:
    x.append(list(i))


# In[22]:


x

