import csv
import pandas as pd
import numpy as np     
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


ff=pd.read_csv('overall_freq.csv')
ff=ff.sort_values(by='Count', ascending=False)
word=ff["Word"].to_numpy().tolist()
freq=ff["Count"].to_numpy().tolist()
a=["rate", "inflation", "market", "prices", "unemployment", "purchases", "securities" ,"monetary", "asset","equity"]
cutoff=100
kw=[]
for k in a:
    kw.append(word.index(k))
cc=[freq[i] for i in kw]


fig=make_subplots(rows=1,cols=2,subplot_titles=("Chosen", "Top 10"),y_title="Count")
x=list(range(10))
fig.add_trace(go.Bar(x=x,y=cc,name="Chosen"),row=1,col=1,)
fig.add_trace(go.Bar(x=x,y=freq[0:10],name="Top 10",xaxis="x2",
    yaxis="y2"),row=1,col=2)
fig['layout']['xaxis'].update(tickvals=x,ticktext=a)
fig['layout']['xaxis2'].update(tickvals=x,ticktext=word[0:10])
fig.show()
x2=list(range(cutoff))
fig2=go.Figure(data=go.Scatter(x=x2,y=freq[0:cutoff],hovertext=word[0:cutoff]))
fig2.update_layout(title='Top 500 Words')
fig2.show()


