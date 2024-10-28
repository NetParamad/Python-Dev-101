import plotly.graph_objects as go

# Create Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["Finance", "HR", "IT", "Marketing",
                "Operations", "Project A", "Project B", 
                "Project C", "Project D", "Project E"],
        color=["red", "green", "blue", "orange", 
               "purple", "pink", "lightblue", "lightgreen", 
               "lightcoral", "gold"]
    ),
    link=dict(
        source=[0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4],  # Finance, HR, IT, etc.
        target=[5, 6, 7, 8, 5, 6, 7, 8, 9, 5, 9],  # Projects A-E
        value=[70000, 40000, 30000, 20000, 15000, 
               25000, 50000, 45000, 25000, 30000,
               40000]
    ))])

# Update layout for title and font size
fig.update_layout(title_text="Comprehensive Budget ", font_size=10)
fig.show()


import plotly.express as px
import pandas as pd

# Sample data: population of Thailand over the years
data = {
    'year': [2000, 2005, 2010, 2015, 2020, 2025],
    'pop': [56000000, 68000000, 70000000,
            62000000, 70000000, 80000000]  # Population in millions
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create bar chart for Thailand's population by year
fig = px.bar(df, x='year', y='pop',
             labels={'pop':'Population of Thailand'},
             title="Population of Thailand by Year",
             height=400)

fig.show()


import plotly.graph_objects as go

# Labels and values for gases in the atmosphere
labels = ['Oxygen', 'Hydrogen', 'Carbon Dioxide', 'Nitrogen']
values = [4500, 2500, 1053, 500]

# Create a donut chart using a pie chart with a hole
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

# Update layout to add a title
fig.update_layout(title_text="Composition of Gases in the Atmosphere")

fig.show()


import plotly.graph_objects as go

# Create a new figure
fig = go.Figure()

# Data for City A
fig.add_trace(go.Bar(
    y=['2018', '2019', '2020'],
    x=[1200, 1150, 1300],
    name='Male Births',
    orientation='h',
    marker=dict(
        color='rgba(35, 110, 253, 0.5)',
        line=dict(color='rgba(35, 110, 253, 1.0)', width=3)
    )
))

# Data for City B
fig.add_trace(go.Bar(
    y=['2018', '2019', '2020'],
    x=[1100, 1050, 1250],
    name='Female Births',
    orientation='h',
    marker=dict(
        color='rgba(220, 52, 69, 0.5)',
        line=dict(color='rgba(220, 52, 69, 1.0)', width=3)
    )
))

# Update layout to make it stacked
fig.update_layout(
    barmode='stack',
    title="Male and Female Births Comparison",
    xaxis_title="Number of Births",
    yaxis_title="Year"
)

fig.show()


import plotly.express as px
import pandas as pd

# Sample project timeline data
df = pd.DataFrame([
    dict(Task="Planning", Start='2023-01-01', Finish='2023-02-15'),
    dict(Task="Design", Start='2023-02-16', Finish='2023-04-30'),
    dict(Task="Development", Start='2023-05-01', Finish='2023-08-31'),
    dict(Task="Testing", Start='2023-09-01', Finish='2023-10-15'),
    dict(Task="Deployment", Start='2023-10-16', Finish='2023-11-30')
])

# Create a Gantt chart (timeline chart) using plotly express
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task",
                      title="Project Timeline")

# Reverse the Y-axis to show tasks in a logical order
fig.update_yaxes(autorange="reversed")

# Show the chart
fig.show()