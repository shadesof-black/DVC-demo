import pandas as pd


Data = [
    {"name": "rahul", "age": 30, "city": "New York"},
    {"name": "rahul.raj", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

pd.DataFrame(Data)

Data = pd.DataFrame(Data)
Data.to_csv("data.csv", index=False)