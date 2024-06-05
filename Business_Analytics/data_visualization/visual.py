
# Import Module for Data Manipulation and Analysis ----------------------------
import sys
module_dir = '../../Business_Analytics'
sys.path.append(module_dir)

from descriptive_statistics.descriptive_analysis import *
# -----------------------------------------------------------------------------

# Import for Chart Visualization ----------------------------------------------
import matplotlib.pyplot as plt
from data_visualization.plot import * 
# -----------------------------------------------------------------------------

# Imported Data Validation ----------------------------------------------------
from data_type_validation import *
# -----------------------------------------------------------------------------
try:
    import data_visualization.plot
    print("Module is installed")
except ImportError:
    print("Module is not installed")
# --------------------------------

datasetSize = len(dataset)
# Imported functions ----------------------------------------------------------
# Calculate and analyze data statistics
typeOfData = data_types(dataset)  # Determine the data type (quantitative or categorical)
meanOfData = mean(dataset)  # Calculate the mean
deviationOfData = standard_deviation(dataset, meanOfData)  # Calculate the standard deviation
# lineChart = labeled_line_chart(x,y)
# -----------------------------------------------------------------------------


# ---------------
# Consider we have the following four datasets of x, y pairs.
xDataset = [[10,8,13,9,11,14,6,4,12,7,5],[10,8,13,9,11,14,6,4,12,7,5],[10,8,13,9,11,14,6,4,12,7,5],[8,8,8,8,19,8,8,8,8,8,8]]
yDataset = [[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68],[9.14,8.14,8.74,8.77,9.26,8.1,6.13,3.1,9.13,7.26,4.74],[7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73],[6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.5,5.56,7.91,6.89]]
x_y_ds = list(zip(xDataset, yDataset))
test_data = [[[1,2,3,4,5,6], [3,6,9,12,15,18]]]
test_data = [[[1,2,3,4,5,6], [3,6,9,12,15,18]], [[6,1.5,4,3,2,1], [3.2,6,9,12,15,18]]]
# test_data = ['Pie Chart', 'Normal Quartile Plot', 'Stem and Leaf Plot', 'Box and Whisker']
dataset = x_y_ds
dataset = test_data
# print(x_y_ds, type(x_y_ds), x_y_ds[0])
zDataset = ['Pie Chart', 'Normal Quartile Plot', 'Stem and Leaf Plot', 'Box and Whisker']
# ---------------


# Best Chart Type
def best_chart_type(dataset):
  dataType = data_types(dataset)
  chType = dataType.split(' ')[0]
  quant_visuals = ['Normal Quartile Plot', 'Stem and Leaf Plot', 'Box and Whisker','Histogram']
  cat_visuals = ['Pie Chart', 'Bar Chart', 'Pareto Chart']
  best_chart = ''
  chart_options = None

  if chType == 'Categorical':
    chart_options = cat_visuals
    if 'Bar Chart' in cat_visuals:
      best_chart = 'Bar Chart'
      # return best_chart
    else:
      best_chart = quant_visuals[0]
      # return best_chart
  elif chType == 'Quantitative':
    chart_options = quant_visuals
    if 'Histogram' in quant_visuals:
      best_chart = 'Histogram'
      # return best_chart
    else:
      best_chart = quant_visuals[0]
      # return best_chart
  
  return best_chart, chart_options

best_chart, chart_options = best_chart_type(dataset)
print(f'Best Chart: {best_chart}')

# Columns
def count_columns(dataset):
  if not dataset:
      return 0  # Return 0 if the dataset is empty.
  return len(dataset)  # Return the length of the first row, which represents the number of columns.

num_columns = count_columns(dataset)
print(f"Number of columns: {num_columns}")

# Column variable pairs
def variable_pairs(dataset):
  variables = ['x','y','z','a','b','c','i','j','k']
  numCols = num_columns

  for col in range(numCols):
    curr_column = dataset[col]
    if len(curr_column) == 2: 
      [x, y] = curr_column

    # print(f'idx: {idx_num} | col: {col_inc} | data: {curr_column} | x: {x} | y: {y}')

  return x, y
var_pairs = variable_pairs(dataset)

# Define the function to calculate the mean and standard deviation
def calculate_mean_and_std(data):
  mean_val = mean(data)
  std_dev = standard_deviation(data, mean_val)
  return mean_val, std_dev

# Columns
def columns(dataset):
  col_nums = num_columns

  for col in range(col_nums):
    x, y = var_pairs
    x_mean, x_std = calculate_mean_and_std(x)
    y_mean, y_std = calculate_mean_and_std(y)

    x_data = f'X Mean: {x_mean} | X STD: {x_std}'
    y_data = f'Y Mean: {y_mean} | Y STD: {y_std}'

    print(f'Column {col+1}:')
    print(f'Chart Type: {best_chart}')
    print(f'Chart Options: {chart_options}')
    print(f'Data Type: {typeOfData}')
    print(x_data)
    print(y_data)
    print('-'*40)
  return x, y
col_info = columns(dataset)


# Get user input data type
def input_data_type(user_input):
  for insert in user_input:
    insert_type = type(insert)
    if isinstance(insert, float):
        insert_data_type = 'Continuous'
    elif isinstance(insert, bool):
        insert_data_type = 'Categorical'  # This line is changed
    elif isinstance(insert, int):
        insert_data_type = 'Discrete'
    # You can check if instance is datetime object
    # elif isinstance(insert, datetime):
    #   insert_data_type = 'Date/Time'
    elif isinstance(insert, str):
        insert_data_type = 'Categorical'
    else:
        insert_data_type = 'Unknown'
      
    print(f"{insert} is an example of a {insert_data_type} || Input Type: {insert_type}")
  print(type(insert))
  return insert, insert_data_type

input_data_type([173.57,'f',1, True])
# print(f'{test}')

# Column(s) Data
def column_data(dataset):
  col_data_type = data_types(dataset)
  chartType = best_chart_type(col_data_type)
  for i, data in enumerate(dataset, 1):
    x_val, y_val = data
    x_values = [x_val[i] for i in range(len(x_val))]
    y_values = [y_val[i] for i in range(len(y_val))]
    print(f'Column {i}:')
    print(f'Chart: {chartType}')
    print(f'Values: {x_values}, {y_values}')
    print(f'x: {x_values} || y: {y_values}')
column_data(dataset)

# Univariate Plot
def univariate_plot(col_info):
  x_val = col_info[0]
  y_val = col_info[1]
  print(f'Uni Plot: {x_val} ')
  return x_val, y_val

univariate_plot(['A','B'])
univariate_plot(col_info)

def test(dataset):
  dataset = [['a','b','c'], ['one','two','three']]
  # dataset = ['a','b','c']
  res = data_types(dataset)
  return res
print(f'Test: {test(dataset)}')

