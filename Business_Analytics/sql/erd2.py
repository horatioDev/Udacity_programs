
# Table and Row Object
class Table:
  '''
  A primary key is a unique column in a particular table.
   It is common that the primary key is the first column in our tables in most databases.

  A foreign key is a column in one table that is a primary key
   Ex: region_id, account_id, sales_rep_id
   Each of these is linked to the primary key of another table. 
  '''
  # Count the amount of Tables created
  table_count = 0

  # Constructor method
  def __init__(self, table_name, **kwargs):
      self.table_name = table_name
      self.columns = list(kwargs.keys())
      self.table_rows = []
      for key, val in kwargs.items():
        setattr(self, key, val)
      Table.table_count += 1

  # Add row
  def add_row(self,*row_values):
    if len(row_values) != len(self.columns):
      print('Row length does not match number of Columns')
      print(f'Row/Columns:{row_values}: {len(row_values)}, {self.columns}: {len(self.columns)}')
      return
    row = dict(zip(self.columns, row_values))
    row['pk'] = self.get_row_id()
    # Rearrange pk/id placement
    row = {'pk': row['pk'], **{key: value for key, value in row.items() if key != 'pk'}}
    self.table_rows.append(row)
    
  # Get next available ID
  def get_row_id(self):
    current_ids = [row['pk'] for row in self.table_rows]
    
    if current_ids:
      new_id = max(current_ids) + 1
    else:
      new_id = 1
    return new_id
  
  # Row
  class Row:
    # Constructor method
    def __init__(self, **kwargs):
      for key, val in kwargs.items():
        setattr(self, key, val)


# Data Type converter
def data_converter(column_type, user_input):
  try:
    if column_type == int:
      return int(user_input)
    elif column_type == float:
      return float(user_input)
    elif column_type == bool:
      return bool(user_input)
    else:
      return str(user_input)
  except ValueError:
    return None


# Get correct input type --------------------------------------------------
# Get Integer Input
def get_integer_input(prompt):
  while True:
    try:
      value = int(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a valid integer.")

# Get Positive Integer Input
def get_positive_integer_input(prompt):
  while True:
    try:
      value = int(input(prompt))
      if value <= 0:
        print("Please enter a positive integer.")
      else:
        return value
    except ValueError:
      print("Invalid input. Please enter a valid positive integer.")

# Get Float Input
def get_float_input(prompt):
  while True:
    try:
      value = float(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a valid float.")

# Get Positive Float Input
def get_positive_float_input(prompt):
  while True:
    try:
      value = float(input(prompt))
      if value <= 0:
        print("Please enter a positive float.")
      else:
        return value
    except ValueError:
      print("Invalid input. Please enter a valid positive float.")

# Get String Input
def get_string_input(prompt):
  while True:
    try:
      value = str(input(prompt))
      if value == '':
        value = None
      return value
    except ValueError:
      print("Invalid input. Please enter a valid string.")



# Get user input
def create_table_from_user_input():
  # table_count = get_integer_input('How many Tables will be needed: ')
  table_count = 1
  userTableData = []
  userInputData = []
  row_list = []

  for table in range(table_count):
    columnsData = {}
    while True:
      try:
        # table_name_input = get_string_input(f'Table {table+1} name: ')  
        table_name_input = 'test'
        # columns_count = get_positive_integer_input(f'How many columns for {table_name_input}: ')
        columns_count = 2

        # Get column(s) name and type
        for col in range(columns_count):
          col_input = get_string_input(f"Column {col+1} (e.g., name=type): ")
          column_name, column_type = col_input.split('=')
          columnsData[column_name] = eval(column_type)
          
        table_instance = Table(table_name=table_name_input, **columnsData)
        userTableData.append(table_instance)

        # rows_count = get_integer_input(f'How many rows for {table_name_input}: ')
        rows_count = 1
        # Get row input
        # row_list = []
        for row in range(rows_count):
          row_data = {}
          for column_name, column_type in columnsData.items():
            user_input = input(f'Row {table_instance.get_row_id()} {column_name} input: ')
            converted_input = data_converter(column_type, user_input)
            row_data[column_name] = converted_input
 
          table_instance.add_row(*[row_data[column_name] for column_name in table_instance.columns])    
          
      except Exception as e:
        print(f'Error occurred: {e}')
  return userTableData
  

if __name__ == "__main__":
    d_table = create_table_from_user_input()
    r_inst = d_table[0].table_rows[0]
    table_func = d_table[0].Row(**r_inst)

    print('-' * 40)
    print(f"Table Count: {Table.table_count}")
    print(f"Table Name: {d_table[0].table_name}")
    print(f"Rows: {len(d_table[0].table_rows)}")
    print(f'PK: {table_func.pk} {type(table_func.pk)}')

    for col_name in d_table[0].columns:
        if col_name != 'pk':
            print(f'{col_name}: {getattr(table_func, col_name)} {type(getattr(table_func, col_name))}')
    print('-' * 40)

