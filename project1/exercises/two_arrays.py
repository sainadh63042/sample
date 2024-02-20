# import pandas as pd
#
# series = pd.Series([10, 20, 30, 40])
#
# data = {'Name': ['sai', 'raja', 'krish', 'sindhu'],
#         'Age': [23, 30, 35, 23]}
# df = pd.DataFrame(data)
#
# print("Series:")
# print(series)
# print("\nDataFrame:")
# print(df)
#
#
import pandas as pd

df = pd.read_csv('../matplot_dir/name_height.csv')
print(df.head())
print(df.tail())
print(df)




# import pandas as pd
#
# array1 = [1, 2, 3, 4, 5]
# array2 = [3, 4, 5, 6, 7]
#
# series1 = pd.Series(array1)
# # print(series1)
# series2 = pd.Series(array2)
# # print(series2)
#
# matching_numbers = series1[series1.isin(series2)]
#
# print("Matching Numbers:")
# print(matching_numbers)
