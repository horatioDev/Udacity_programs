import sys
module_dir = '../../Business_Analytics'
sys.path.append(module_dir)

from descriptive_statistics.descriptive_analysis import *

try:
    import data_visualization.plot
    print("Module is installed")
except ImportError:
    print("Module is not installed")

# Call the function to get the data type
# typeOfData = data_types(dataset)

def data_types(dataset):
  quantDataType = 'Quantitative'
  continuousDataType = 'Continuous'
  discreteDataType = 'Discrete'
  categoricalDataType = 'Categorical'
  mixedDataType = ''
  dataType = ''

  # Initialize counters for each data type
  num_continuous = 0
  num_discrete = 0
  num_categorical = 0
  most_common_type = None  # Initialize most_common_type variable

  for pt in dataset:
    if isinstance(pt, int):
        num_discrete += 1
    elif isinstance(pt, float):
        num_continuous += 1
    elif isinstance(pt, str):
        num_categorical += 1

  if num_continuous == len(dataset):
      most_common_type = continuousDataType
  elif num_categorical == len(dataset):
      most_common_type = categoricalDataType
  elif num_discrete == len(dataset):
      most_common_type = discreteDataType
  else:
    most_common_count = max(num_continuous, num_discrete, num_categorical)

    if most_common_count == num_continuous:
      most_common_type = continuousDataType
    elif most_common_count == num_discrete:
      most_common_type = discreteDataType
    elif most_common_count == num_categorical:
      most_common_type = categoricalDataType
    else:
      most_common_type = mixedDataType

  # Output the results
  if most_common_type == quantDataType:
    print(f"{quantDataType}: {most_common_type}")
    print(f"Most common data type: {most_common_type}")
    print(f"Counts - Continuous: {num_continuous}, Discrete: {num_discrete}, Categorical: {num_categorical}")

    return most_common_type


  
        # Check if data type is mixed
    # if dataType == quantDataType:
    #   counts = {'Continuous': num_continuous, 'Discrete': num_discrete, 'Categorical': num_categorical}
    #   most_common_type = max(counts, key=counts.get)
    #   most_common_count = counts[most_common_type]
    #   if all(count == most_common_count for count in counts.values()):
    #     print(f'All data types have equal counts ({most_common_count}).')
        
    #     for i, col_variable in enumerate(dataset):
    #       if isinstance(col_variable, list) and len(dataset) >= 1:
    #         input_len = len(col_variable)
    #         output_len = len(set([str(x) for x in col_variable]))
    #         first_input = col_variable[i]
    #         if (isinstance(first_input, int)):
    #           most_common_type = discreteDataType
    #           print(f'First: {first_input} {most_common_type}')
    #         elif (isinstance(first_input, float)):
    #           most_common_type = continuousDataType
    #           print(f'First: {first_input} {most_common_type}')
    #         elif (isinstance(first_input, str)):
    #           most_common_type = categoricalDataType
    #           print(f'First: {first_input} {most_common_type}')
            
    #         print(f'il: {input_len} dl: {len(dataset)} ol: {output_len} inp: {first_input}')

    #         if most_common_type == continuousDataType and len(dataset) > 1:
    #           x_val, y_val = col_variable
    #           first_x_val = x_val[0]
    #           first_y_val = y_val[0]
    #             # Chart func here...

    #           if (isinstance(first_x_val, int) or isinstance(first_y_val, int)):
    #             most_common_type = discreteDataType
    #             print(f'First: {first_x_val} || {first_y_val} || {most_common_type}')
    #           elif (isinstance(first_x_val, float) or isinstance(first_y_val, float)):
    #             most_common_type = continuousDataType
    #             print(f'First: {first_x_val} || {first_y_val} || {most_common_type}')
    #           elif (isinstance(first_x_val, str) or isinstance(first_y_val, str)):
    #             most_common_type = categoricalDataType
    #             print(f'First: {first_x_val} || {first_y_val} || {most_common_type}')
    #             print(f'Insert: {x_val} || {y_val}')
              
    #       else:
    #         if (num_categorical == num_continuous and num_continuous == num_discrete and num_discrete == num_categorical):
    #           first_input = dataset[0]
    #           print(first_input)
    #           if (isinstance(first_input, int)):
    #             most_common_type = discreteDataType
    #             print(f'First: {first_input} || {most_common_type} || dis')
    #           elif (isinstance(first_input, float)):
    #             most_common_type = continuousDataType
    #             print(f'First: {first_input} || {most_common_type} || cont')
    #           elif (isinstance(first_input, str)):
    #             most_common_type = categoricalDataType
    #             print(f'First: {first_input} || {most_common_type} || cat ')

    #       # print(f'Item {dataset[i]} {most_common_type} not a list')
    #       return most_common_type
    #   else:
    #     print(f'The most common data type is {most_common_type} with {most_common_count} occurrences.')
    
    #     return most_common_type       
    #   print(f'{quantDataType}: {most_common_type}')
    # print(f'{quantDataType}: {most_common_type}')
    
  print(f'Continuous')

  # print(f'cat: {num_categorical} cont: {num_continuous} dis: {num_discrete} {num_categorical == num_continuous and num_continuous == num_discrete and num_discrete == num_categorical} {dataset[0]} {num_continuous} {len(dataset)}')
    
  print(f'pt: {pt}')
  print(f'DT: {dataType}  ')
  return most_common_type, 

# Example dataset with mixed data types
dataset = [1, 2, 3.5, 'string', 5] #Quantitative/Mixed
dataset = [1, 2, 3, 4, 5] #Discrete
dataset = [1.5, 2.0, 3.14, 4.9, 5.75] #Continuous
dataset = ['1', 'two', '3', 'four', '5'] #Categorical
# dataset = [1, 2, 2.2, 3.5, 'apple', 'banana']
# dataset = [[1.0,2.2,3.6]]
# dataset = [[[1,2,3,4,5,6], [3,6,9,12,15,18]], [[6,1.5,4,3,2,1], [3.2,6,9,12,15,18]]] #Discrete
# dataset = [[[1.0,2.6,4.3,4.6,5.5,4.6], [3.2,6.0,9.2,12.10,1.5,18.2]], [[6,1.5,4,3,2,1], [3.2,6,9,12,15,18]]] #Continuous
# Call the function to get the data type
# typeOfData = data_types(dataset)

# Print the result
print(f'Data Type: {dataset} {typeOfData} ')
print('*'*40)

def data_types(dataset):
    quantDataType = 'Quantitative'
    continuousDataType = 'Continuous'
    discreteDataType = 'Discrete'
    categoricalDataType = 'Categorical'
    mixedDataType = 'Mixed'

    # First input
    first_input = dataset[0]

    # Initialize counters for each data type
    num_continuous = 0
    num_discrete = 0
    num_categorical = 0

    most_common_type = None  # Initialize most_common_type variable

    for pt in dataset:
        if isinstance(pt, int):
            num_discrete += 1
        elif isinstance(pt, float):
            num_continuous += 1
        elif isinstance(pt, str):
            num_categorical += 1

    #  Check if .... ----------------------------------------------------------
    if num_continuous == len(dataset):
        most_common_type = continuousDataType
    elif num_categorical == len(dataset):
        most_common_type = categoricalDataType
    elif num_discrete == len(dataset):
        most_common_type = discreteDataType
    else:
        most_common_count = max(num_continuous, num_discrete, num_categorical)

        if most_common_count == num_continuous:
            most_common_type = continuousDataType
        elif most_common_count == num_discrete:
            most_common_type = discreteDataType
        elif most_common_count == num_categorical:
            most_common_type = categoricalDataType
        else:
            most_common_type = mixedDataType
            return most_common_type
    # -------------------------------------------------------------------------
        
    # Check if first_input is a list/column -----------------------------------
    if (isinstance(first_input, list)):
      if len(first_input) == 2:
        x_vals, y_vals = first_input
        print(f'Column has two variables: X - {x_vals} || Y - {y_vals}')
      else:
        print('This is not a column')

      for insert in first_input:
         print(f'ins: {insert}')

      print(f"{quantDataType}: {most_common_type} || {first_input} || FIl: {len(first_input)}")
    # -------------------------------------------------------------------------

    # Output the results ---------------------------------------------------
    print(f"Most common data type: {most_common_type}")
    print(f"Counts - Continuous: {num_continuous}, Discrete: {num_discrete}, Categorical: {num_categorical}")
    print(f'QT: {quantDataType} || MCT: {most_common_type}')
    print(f'First Ins: {first_input} || FIl: || Column: {isinstance(first_input, list)} || DS: {dataset} || Dl: {len(dataset)} ')
    # ------------------------------------------------------------------------ 
    
    print('-'*30)

    # Check if all counts are equal
    # if (num_continuous == num_discrete == num_categorical) or (isinstance(first_input, list)):
    #   print(f'All data types have equal counts ({num_continuous}) and first input is a list/column.')
    #   first_input = dataset[0]
    #   print(first_input)

      # if (isinstance(first_input, int)):
      #   most_common_type = discreteDataType
      #   print(f'First: {first_input} || {most_common_type} || dis')
      # elif (isinstance(first_input, float)):
      #   most_common_type = continuousDataType
      #   print(f'First: {first_input} || {most_common_type} || cont')
      # elif (isinstance(first_input, str)):
      #   most_common_type = categoricalDataType
      #   print(f'First: {first_input} || {most_common_type} || cat ')
    
    # Handle cases when most_common_type is already set
    # if most_common_type:
    #   print(f'The most common data type is {most_common_type} with {most_common_count} occurrences.')


      # return most_common_type

    # if most_common_type == quantDataType:
    #   counts = {'Continuous': num_continuous, 'Discrete': num_discrete, 'Categorical': num_categorical}
    #   most_common_type = max(counts, key=counts.get)
    #   most_common_count = counts[most_common_type]
    #   most_common_count = max(counts.values())
    #   print(f'MCT: {most_common_type} || MCC: {most_common_count}')
      

      # if all(count == most_common_count for count in counts.values()):
      #   print(f'All data types have equal counts ({most_common_count}).')
        
      # for i, col_variable in enumerate(dataset):
      #   if isinstance(col_variable, list) and len(dataset) >= 1:
      #     input_len = len(col_variable)
      #     # output_len = len(set([str(x) for x in col_variable]))
      #     output_len = len(set(map(str, col_variable)))
      #     first_input = col_variable[i]
      #     print(f'First: {first_input} {first_input} {most_common_type}')

      #     if (isinstance(first_input, int)):
      #       most_common_type = discreteDataType
      #       print(f'First: {first_input} {most_common_type}')
      #     elif (isinstance(first_input, float)):
      #       most_common_type = continuousDataType
      #       print(f'First: {first_input} {most_common_type}')
      #     elif (isinstance(first_input, str)):
      #       most_common_type = categoricalDataType
      #       print(f'First: {first_input} {most_common_type}')
          
      #     print(f'il: {input_len} dl: {len(dataset)} ol: {output_len} inp: {first_input}')

      #     if most_common_type == continuousDataType and len(dataset) > 1:
      #       x_val, y_val = col_variable
      #       first_x_val, first_y_val = x_val[0], y_val[0]
      #       print(x_val, y_val, first_x_val,first_y_val)
            
      #       # Chart func here...

      #       if (isinstance(first_x_val, int) or isinstance(first_y_val, int)):
      #         most_common_type = discreteDataType
      #         print(f'First: {first_x_val} || {first_y_val} || {most_common_type}')
      #       elif (isinstance(first_x_val, float) or isinstance(first_y_val, float)):
      #         most_common_type = continuousDataType
      #         print(f'First: {first_x_val} || {first_y_val} || {most_common_type}')
      #       elif (isinstance(first_x_val, str) or isinstance(first_y_val, str)):
      #         most_common_type = categoricalDataType
      #         print(f'First: {first_x_val} || {first_y_val} || {most_common_type}')

      #         print(f'Insert: {x_val} || {y_val}')
            
      #   else:
      #     if (num_categorical == num_continuous  == num_discrete):
      #       first_input = dataset[0]
      #       print(first_input)

      #       if (isinstance(first_input, int)):
      #         most_common_type = discreteDataType
      #         print(f'First: {first_input} || {most_common_type} || dis')
      #       elif (isinstance(first_input, float)):
      #         most_common_type = continuousDataType
      #         print(f'First: {first_input} || {most_common_type} || cont')
      #       elif (isinstance(first_input, str)):
      #         most_common_type = categoricalDataType
      #         print(f'First: {first_input} || {most_common_type} || cat ')

      #   # print(f'Item {dataset[i]} {most_common_type} not a list')
      #   print(f'The most common data type is {most_common_type} with {most_common_count} occurrences.')
      #   print('-'*30)
       
    return most_common_type

# Example datasets with mixed data types
dataset1 = [1, 2, 3.5, 'string', 5]  # Quantitative/Mixed - Discrete
dataset2 = [1, 2, 3, 4, 5]  # Discrete
dataset3 = [1.5, 2.0, 3.14, 4.9, 5.75]  # Continuous
dataset4 = ['1', 'two', '3', 'four', '5']  # Categorical
dataset5 = [[[1,2,3,4,5,6], [3,6,9,12,15,18]], [[6,1.5,4,3,2,1], [3.2,6,9,12,15,18]]] #Discrete
dataset6 = [[[1.0,2.6,4.3,4.6,5.5,4.6], [3.2,6.0,9.2,12.10,1.5,18.2]], [[6,1.5,4,3,2,1], [3.2,6,9,12,15,18]]] #Continuous
dataset7 = [['1','2','3']]

# Call the function for each dataset
typeOfData1 = data_types(dataset1)
typeOfData2 = data_types(dataset2)
typeOfData3 = data_types(dataset3)
typeOfData4 = data_types(dataset4)
typeOfData5 = data_types(dataset5)
typeOfData6 = data_types(dataset6)
typeOfData7 = data_types(dataset7)
print('-'*40)