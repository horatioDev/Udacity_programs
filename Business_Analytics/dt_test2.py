def data_types(dataset):
  quantDataType = 'Quantitative'
  continuousDataType = 'Continuous'
  discreteDataType = 'Discrete'
  categoricalDataType = 'Categorical'
  mixedDataType = ''
  dataType = ''
  # most_common_type = ''

  # Initialize counters for each data type
  num_continuous = 0
  num_discrete = 0
  num_categorical = 0

  for pt in dataset:
    if isinstance(pt, int):
      num_discrete += 1
    elif isinstance(pt, float):
      num_continuous += 1
    elif isinstance(pt, str):
        num_categorical += 1

  if num_continuous == len(dataset):
      dataType = continuousDataType
  elif num_categorical == len(dataset):
      dataType = categoricalDataType
  elif num_discrete == len(dataset):
      dataType = discreteDataType
  else:
    dataType = quantDataType
    # Check if data type is mixed
  #   if dataType == quantDataType:
  #     counts = {'Continuous': num_continuous, 'Discrete': num_discrete, 'Categorical': num_categorical}
  #     most_common_type = max(counts, key=counts.get)
  #     most_common_count = counts[most_common_type]
  #     if all(count == most_common_count for count in counts.values()):
  #       print(f'All data types have equal counts ({most_common_count}).')
        
  #       for i, col_variable in enumerate(dataset):
  #         if isinstance(col_variable, list) and len(dataset) >= 1:
  #           input_len = len(col_variable)
  #           output_len = len(set([str(x) for x in col_variable]))
  #           first_input = col_variable[i]
  #           if (isinstance(first_input, int)):
  #             most_common_type = discreteDataType
  #             print(f'First: {first_input} {most_common_type}')
  #           elif (isinstance(first_input, float)):
  #             most_common_type = continuousDataType
  #             print(f'First: {first_input} {most_common_type}')
  #           elif (isinstance(first_input, str)):
  #             most_common_type = categoricalDataType
  #             print(f'First: {first_input} {most_common_type}')
            
  #           print(f'il: {input_len} dl: {len(dataset)} ol: {output_len} inp: {first_input}')

  #           if most_common_type == continuousDataType and len(dataset) > 1:
  #             x_val, y_val = col_variable
  #             first_x_val = x_val[0]
  #             first_y_val = y_val[0]
  #               # Chart func here...

  #             if (isinstance(first_x_val, int) or isinstance(first_y_val, int)):
  #               most_common_type = discreteDataType
  #               print(f'First: {first_x_val} || {first_y_val} || {most_common_type}')
  #             elif (isinstance(first_x_val, float) or isinstance(first_y_val, float)):
  #               most_common_type = continuousDataType
  #               print(f'First: {first_x_val} || {first_y_val} || {most_common_type}')
  #             elif (isinstance(first_x_val, str) or isinstance(first_y_val, str)):
  #               most_common_type = categoricalDataType
  #               print(f'First: {first_x_val} || {first_y_val} || {most_common_type}')
  #               print(f'Insert: {x_val} || {y_val}')
              
  #         else:
  #           if (num_categorical == num_continuous and num_continuous == num_discrete and num_discrete == num_categorical):
  #             first_input = dataset[0]
  #             print(first_input)
  #             if (isinstance(first_input, int)):
  #               most_common_type = discreteDataType
  #               print(f'First: {first_input} || {most_common_type} || dis')
  #             elif (isinstance(first_input, float)):
  #               most_common_type = continuousDataType
  #               print(f'First: {first_input} || {most_common_type} || cont')
  #             elif (isinstance(first_input, str)):
  #               most_common_type = categoricalDataType
  #               print(f'First: {first_input} || {most_common_type} || cat ')

  #         # print(f'Item {dataset[i]} {most_common_type} not a list')
  #         return most_common_type
  #     else:
  #       print(f'The most common data type is {most_common_type} with {most_common_count} occurrences.')
    
  #       return most_common_type       
  #     print(f'{quantDataType}: {most_common_type}')
  #   print(f'{quantDataType}: {most_common_type}')
    
  # print(f'Continuous')

  # print(f'cat: {num_categorical} cont: {num_continuous} dis: {num_discrete} {num_categorical == num_continuous and num_continuous == num_discrete and num_discrete == num_categorical} {dataset[0]} {num_continuous} {len(dataset)}')
    if dataType == quantDataType:
      counts = {'Continuous': num_continuous, 'Discrete': num_discrete, 'Categorical': num_categorical}
      most_common_type = max(counts, key=counts.get)
      most_common_count = counts[most_common_type]
      if all(count == most_common_count for count in counts.values()):
          print(f'All data types have equal counts ({most_common_count}).')
          
          for i, col_variable in enumerate(dataset):
              if isinstance(col_variable, list) and len(dataset) >= 1:
                  input_len = len(col_variable)
                  output_len = len(set([str(x) for x in col_variable]))
                  first_input = col_variable[0]  # Retrieve the first element

                  # Determine the data type of the first element
                  if isinstance(first_input, int):
                      most_common_type = discreteDataType
                  elif isinstance(first_input, float):
                      most_common_type = continuousDataType
                  elif isinstance(first_input, str):
                      most_common_type = categoricalDataType

                  print(f'il: {input_len} dl: {len(dataset)} ol: {output_len} inp: {first_input}')

                  if most_common_type == continuousDataType and len(dataset) > 1:
                      x_val, y_val = col_variable
                      first_x_val, first_y_val = x_val[0], y_val[0]

                      # Determine the data type of the first values in x_val and y_val
                      if isinstance(first_x_val, int) or isinstance(first_y_val, int):
                          most_common_type = discreteDataType
                      elif isinstance(first_x_val, float) or isinstance(first_y_val, float):
                          most_common_type = continuousDataType
                      elif isinstance(first_x_val, str) or isinstance(first_y_val, str):
                          most_common_type = categoricalDataType

                      print(f'Insert: {x_val} || {y_val}')
              else:
                  if num_categorical == num_continuous and num_continuous == num_discrete and num_discrete == num_categorical:
                      first_input = dataset[0]
                      print(first_input)
                      if isinstance(first_input, int):
                          most_common_type = discreteDataType
                          print(f'First: {first_input} || {most_common_type} || dis')
                      elif isinstance(first_input, float):
                          most_common_type = continuousDataType
                          print(f'First: {first_input} || {most_common_type} || cont')
                      elif isinstance(first_input, str):
                          most_common_type = categoricalDataType
                          print(f'First: {first_input} || {most_common_type} || cat')
          
          # Print the final result after iterating through the dataset
          print(f'The most common data type is {most_common_type} with {most_common_count} occurrences.')
          return most_common_type
      else:
          print(f'{quantDataType}: {most_common_type}')
          return most_common_type
  print(f'{quantDataType}: {most_common_type}')
    
  print(f'pt: {pt}')
  print(f'DT: {dataType}  ')
  return dataType, 

#