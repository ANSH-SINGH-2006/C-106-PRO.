import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df, x="days", y="marks")
        fig.show()

def getDataSource(data_path):
    marks=[]
    days=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            marks.append(float(row["marks"]))
            days.append(float(row["days"]))
    return {"x": days, "y": marks}

def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("Corelation between days present VS marks is: ", corelation[0,1])

def setup():
    data_path="student.csv"
    dataSource=getDataSource(data_path)
    findCorelation(dataSource)
    plotFigure(data_path)

setup()