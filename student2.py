import pandas as pd
import csv
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
student2df = df.loc[df["student_id"]=="TRL_xyz"]
print(student2df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = student2df.groupby("level")["attempt"].mean(),
    y= ["Level 1","Level 2","Level 3","Level 4"],orientation = "h")
)
fig.show()
