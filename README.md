print(data.isnull().sum())
    - Shows no null/missing values

line 581 is a duplicate:
    - run: duplicated_data = data[data.duplicated()]
            print(duplicated_data)

print(data.shape)
    - (1338, 7) => (Number of Rows, Number of Columns)

print(data.info())
    - RangeIndex: 1338 entries, 0 to 1337
      Data columns (total 7 columns):
       #   Column    Non-Null Count  Dtype  
      ---  ------    --------------  -----  
       0   age       1338 non-null   int64  
       1   sex       1338 non-null   object 
       2   bmi       1338 non-null   float64
       3   children  1338 non-null   int64  
       4   smoker    1338 non-null   object 
       5   region    1338 non-null   object 
       6   charges   1338 non-null   float64
      dtypes: float64(2), int64(2), object(3)
      memory usage: 73.3+ KB
      None