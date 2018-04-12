
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
dataframe = pd.read_excel("Sensor_Data.xlsx")
temp = pd.DatetimeIndex(dataframe.iloc[:,2])
dataframe['Date'] = temp.date
dataframe['Time'] = temp.time
#studying chemical Chlorodinine	
Day = 4
Month = 4
Year = 2016
X = None
Y = None

def databyChemical(dataframe, chemical):
    return dataframe[dataframe["Chemical"] == chemical]

def databyDate(dataframe,day,month,year):
    return dataframe[dataframe['Date'] == datetime.date(Year,Month,day)]

def datatoplot(chemicalbyday):
    datedataframe = pd.DataFrame() 
    datedataframe['Monitor'] = chemicalbyday['Monitor'] 
    datedataframe['Reading'] = chemicalbyday['Reading']
    temp = pd.DatetimeIndex(chemicalbyday.iloc[:,2])
    datedataframe['Hour'] = temp.hour
    map_data = list()
    for i in range(10):
        map_data.append(np.zeros(24))
    z = datedataframe.as_matrix()
    for index, row in datedataframe.iterrows():
        map_data[int(row['Monitor'])][int(row['Hour'])] = row['Reading']
    return map_data

def allchemicalsbyDateSurface(dataframe,date,month,year):
    c_442016 = databyDate(dataframe,date,month,year)
    datas = list()
    chemicals = list()
    for i in c_442016.Chemical.unique():
        chemicals.append(i)
        datas.append(
            go.Surface(
                z=datatoplot(databyChemical(c_442016,i))
            )
        )
    return chemicals,datas

def allchemicalsbyDateContour(dataframe,date,month,year):
    c_442016 = databyDate(dataframe,date,month,year)
    datas = list()
    chemicals = list()
    for i in c_442016.Chemical.unique():
        chemicals.append(i)
        datas.append(
            go.Contour(
                z=datatoplot(databyChemical(c_442016,i))
            )
        )
    return chemicals,datas

def isTextValid(text):
    global X
    global Y
    for i in range(1,int(text_input.value)):
        date = i
        chem,datas = allchemicalsbyDateSurface(dataframe,date,1,2016)
        updatemenus = list([
        dict(active=0,
                 buttons=list([   
                    dict(label = chem[0],
                         method = 'update',
                         args = [{'visible': [True, False, False, False]},
                                 {'title': chem[0]}]),
                    dict(label = chem[1],
                         method = 'update',
                         args = [{'visible': [False, True, False, False]},
                                 {'title': chem[1]}]),
                    dict(label = chem[2],
                         method = 'update',
                         args = [{'visible': [False, False, True, False]},
                                 {'title': chem[2]}]),
                    dict(label = chem[3],
                         method = 'update',
                         args = [{'visible': [False, False, False, True]},
                                 {'title': chem[3]}])
                ]),
            ),
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
        layout = go.Layout(
            updatemenus = updatemenus,
            xaxis=dict(
            title='BVVVVV',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='sd,jlhgfodswuoes',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
        )
        X = datas
        Y = layout
        fig = {'data':datas, 'layout':layout}
        plt = py.iplot(fig, filename='elevations-3d-surface')
        plotly.offline.plot(fig, filename = str(date) + '.html', auto_open=False)
    


# In[9]:


c_442016 = databyDate(dataframe,1,1,2016)
chem,datas = allchemicalsbyDateSurface(dataframe,1,1,2016)
layout = go.Layout(
    title='chlorodinine per day',
     xaxis=dict(
        title='x Axis',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )),
    autosize=True,
)


# In[74]:





# In[4]:


from IPython.html import widgets 
button = widgets.Button(description="Submit")

text_input = widgets.Text(
    description='Date of April:',
    value='4',
)

message = widgets.HTML(
    value="",
)

valid = widgets.Valid(
    value=True,
)

# this will be initalize our listener
button.on_click(isTextValid)
container = widgets.HBox(children=[text_input, button, valid, message])
display(container)


# In[88]:


print(X)


# In[13]:


type(datas[0][0])


# In[5]:


Y = list()
X = list()
traces = list()
for i in range(1,10):
    print(i)
    mon = dataframe[dataframe['Monitor']==i]
    l = np.array(mon['Reading'])
    Y.append(l)
    X.append([n for n in range(len(l))])
    traces.append(go.Scatter(
        x = [n for n in range(len(l))],
        y = l,
        mode = 'line',
        name = '0'
    ))
    
u_menus = list([
        dict(active=4,
                 buttons=list([   
                    dict(label = '1',
                         method = 'update',
                         args = [{'visible': [True, False, False, False, False, False, False, False, False]},
                                 {'title': '1'}]),
                    dict(label = '2',
                         method = 'update',
                         args = [{'visible': [False, True, False, False, False, False, False, False, False]},
                                 {'title': '2'}]),
                    dict(label = '3',
                         method = 'update',
                         args = [{'visible': [False, False, True, False, False, False, False, False, False]},
                                 {'title': '3'}]),
                    dict(label = '4',
                         method = 'update',
                         args = [{'visible': [False, False, False, True, False, False, False, False, False]},
                                 {'title': '4'}]),
                     dict(label = '5',
                         method = 'update',
                         args = [{'visible': [False, False, False, False, True, False, False, False, False]},
                                 {'title': '5'}]),
                     dict(label = '6',
                         method = 'update',
                         args = [{'visible': [False, False, False, False, False, True, False, False, False]},
                                 {'title': '6'}]),
                     dict(label = '7',
                         method = 'update',
                         args = [{'visible': [False, False, False, False, False, False, True, False, False]},
                                 {'title': '7'}]),
                     dict(label = '8',
                         method = 'update',
                         args = [{'visible': [False, False, False, False, False, False, False, True, False]},
                                 {'title': '8'}]),
                     dict(label = '9',
                         method = 'update',
                         args = [{'visible': [False, False, False, False, False, False, False, False, True]},
                                 {'title': '9'}])
                     
                     
                ]),
            )])
l_out = go.Layout(
            updatemenus = u_menus,
            yaxis=dict(
                range=[0, 10]
            )
        )
fig = {'data':traces, 'layout':l_out}
plotly.offline.plot(fig, filename = 'sensor_trend.html', auto_open=False)


# In[13]:


len(traces)

