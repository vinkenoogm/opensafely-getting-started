import pandas as pd

data = pd.read_csv("output/dataset.csv")

fig = data.age.plot.hist().get_figure()
fig.savefig("output/report.png")
