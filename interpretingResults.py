import csv
import pandas as pd
import plotly.express as px

rows = []

with open('final_data.csv', 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        rows.append(i)

headers = rows[0]
star_data_rows = rows[1:]

starName = []
starMass = []
starRadius = []
starDistance = []
starGravity = []

for star_data in star_data_rows:
    starName.append(star_data[1])
    starMass.append(star_data[3])
    starRadius.append(star_data[4])
    starDistance.append(star_data[2])
    starGravity.append(star_data[5])

fig = px.bar(x=starName, y=starMass, title="Star Masses")
fig.show()

fig = px.bar(x=starName, y=starRadius, title="Star Radii")
fig.show()

fig = px.bar(x=starName, y=starDistance, title="Star Distance")
fig.show()

fig = px.bar(x=starName, y=starGravity, title="Star Gravity")
fig.show()
