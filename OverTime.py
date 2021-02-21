import csv
import pandas as pd
import numpy as np     
import plotly.express as px
import plotly.graph_objects as go


ff=pd.read_csv('yearly_freq.csv')
ff=ff.sort_values(by='Year', ascending=True)
word=ff["Word"].to_numpy().tolist()
freq=ff["Count"].to_numpy().tolist()
year=ff["Year"].to_numpy().tolist()
a=["rate", "inflation", "market", "prices", "unemployment", "purchases", "securities" ,"monetary", "asset","equity"]

timedict={}
figar=[]

fig=go.Figure()
for val in a:
    idx = [i for i, x in enumerate(word) if x ==val ]
    fq=[freq[i] for i in idx]
    yr=[year[i] for i in idx]
    timedict[val]=[fq,yr]
    fig.add_trace(go.Scatter(x=yr,y=fq,name=val))

fig.update_layout(xaxis = dict(tickmode = 'array',
        tickvals = year,
        ticktext = year),title="FOMC Trends")
fig.show()



