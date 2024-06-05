
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
      return value
    except ValueError:
      print("Invalid input. Please enter a valid string.")



# Get user input
def get_user_input():
  table_count = get_integer_input('How many Tables will be needed: ')
  print(f'Tables: {table_count}')
  


# # table_name_input = input('Enter Table Name: ')
table_name_input = 'erd table'

# Table Instance -------------------------------------------
table_instance = Table(table_name=table_name_input, account_id=int, occurred_at=str, channel=str)
# table_instance.table_name = table_name_input

# Row Instance -------------------------------------------
table_instance.add_row(1001, '2023-10-10', 'Web')
table_instance.add_row(1301, '2023-10-9', 'App')

# Access Attributes -------------------------------------------
row_instance = table_instance.table_rows[0]
demo_table = table_instance.Row(**row_instance)

print('-'*40)
print(f"Table: {Table.table_count}")
print(f"Table name: {table_instance.table_name}")
print(f"Rows: {len(table_instance.table_rows)}")
print(f'Id: {demo_table.pk}')
print(f'Account Id: {demo_table.account_id}')
print(f'Occurred at: {demo_table.occurred_at}')
print(f'Channel: {demo_table.channel}')
print('-'*40)

# Web Events Table -------------------------------------------
web_events_table = Table(table_name='web_events', account_id=int, occurred_at=str, channel=str)
web_events_table.add_row(1001, '2023-10-10', 'Facebook')
web_events_table.add_row(1001, '2023-10-08', 'Facebook')
web_events_table.add_row(1001, '2023-10-06', 'Facebook')
web_events_table.add_row(1001, '2023-10-03', 'Facebook')
web_events_table.add_row(1001, '2023-10-09', 'Facebook')

row_instance = web_events_table.table_rows[0]
web_events = web_events_table.Row(**row_instance)

print('-'*40)
print(f"Table: {Table.table_count}")
print(f"Table name: {web_events_table.table_name}")
print(f"Rows: {len(web_events_table.table_rows)}")
print(f'id: {web_events.pk}')
print(f'account_id: {web_events.account_id}')
print(f'occurred_at: {web_events.occurred_at}')
print(f'Channel: {web_events.channel}')
print('-'*40)

# Accounts Table -------------------------------------------
accounts_table = Table(table_name='accounts', id=int, name=str, website=str, lat=float, long=float, primary_poc=str, sales_rep_id=int)
accounts_table.add_row(1001, 'Walmart', 'www.walmart.com', 40.23849561, -75.10329704, 'Tamara Tuma', 321500)
accounts_table.add_row(1011, 'Exxon Mobil', 'www.exxonmobil.com', 41.16915630, -73.84937379, 'Sung Shields', 321510)
accounts_table.add_row(1021, 'Apple', 'www.apple.com', 42.29049481, -76.08400942, 'Jodee Lupo', 321520)
accounts_table.add_row(1031, 'Berkshire Hathaway', 'www.berkshirehathaway.com', 40.94902131, -75.76389759, 'Serafina Banda', 321530)
accounts_table.add_row(1041, 'McKesson', 'www.mckesson.com', 42.21709326, -75.28499823, 'Angeles Crusoe', 321540)

row_instance = accounts_table.table_rows[0]
accounts = accounts_table.Row(**row_instance)

print('-'*40)
print(f"Table: {Table.table_count}")
print(f"Table name: {accounts_table.table_name}")
print(f"Rows: {len(accounts_table.table_rows)}")
print(f'Id: {accounts.id}')
print(f"Name: {accounts.name}")
print(f'Website: {accounts.website}')
print(f'Lat: {accounts.lat}')
print(f'Long: {accounts.long}')
print(f'Primary Poc: {accounts.primary_poc}')
print(f'Sales Rep Id: {accounts.sales_rep_id}')
print('-'*40)

# Orders Table -------------------------------------------
orders_table = Table(table_name='orders', account_id=int, occurred_at=str, standard_qty=int, gloss_qty=int, poster_qty=int, total=int, standard_amt_usd=int, gloss_amt_usd=int, poster_amt_usd=int, total_amt_usd=int)
orders_table.add_row(1001, '2015-10-06', 123, 22, 24, 169, 613.77, 164.78, 194.88, 973.43)
orders_table.add_row(1001, '2015-11-05', 190, 41, 57, 288, 948.10, 307.09, 462.84, 1718.03)
orders_table.add_row(1001, '2015-12-04', 85, 47, 0, 132, 424.15, 352.03, 0.00, 776.18)
orders_table.add_row(1001, '2016-01-02', 144, 32, 0, 176, 718.56, 239.68, 0.00, 958.24)
orders_table.add_row(1001, '2016-02-01', 108, 29, 28, 165, 538.92, 217.21, 227.36, 983.49)

row_instance = orders_table.table_rows[0]
orders = orders_table.Row(**row_instance)

print('-'*40)
print(f"Table: {Table.table_count}")
print(f"Table name: {orders_table.table_name}")
print(f"Rows: {len(orders_table.table_rows)}")
print(f'id: {orders.pk}')
print(f'account_id: {orders.account_id}')
print(f"standard_qty: {orders.standard_qty}")
print(f'poster_qty: {orders.poster_qty}')
print(f'gloss_qty: {orders.gloss_qty}')
print(f'occurred_at: {orders.occurred_at}')
print(f'standard_amt_usd: {orders.standard_amt_usd}')
print(f'gloss_amt_usd: {orders.gloss_amt_usd}')
print(f'poster_amt_usd: {orders.poster_amt_usd}')
print(f'total_amt_usd: {orders.total_amt_usd}')
print('-'*40)

# Sales Reps Table -------------------------------------------
sales_reps_table = Table(table_name='sales_reps', id=int, name=str, region_id=int)
sales_reps_table.add_row(321500, 'Samuel Racine', 1)
sales_reps_table.add_row(321510, 'Eugena Esser', 1)
sales_reps_table.add_row(321520, 'Michel Averette', 1)
sales_reps_table.add_row(321530, 'Renetta Carew', 1)
sales_reps_table.add_row(321540, 'Cara Clarke', 1)

row_instance = sales_reps_table.table_rows[0]
sales_reps = sales_reps_table.Row(**row_instance)

print('-'*40)
print(f"Table: {Table.table_count}")
print(f"Table name: {sales_reps_table.table_name}")
print(f'id: {sales_reps.id}')
print(f'name: {sales_reps.name}')
print(f'region_id: {sales_reps.region_id}')
print('-'*40)

# Region Table -------------------------------------------
region_table = Table(table_name='region', id=int, name=str)
region_table.add_row(1, 'Northeast')
region_table.add_row(2, 'Midwest')
region_table.add_row(3, 'Southeast')
region_table.add_row(4, 'West')

row_instance = region_table.table_rows[0]
region = region_table.Row(**row_instance)

print('-'*40)
print(f"Table: {Table.table_count}")
print(f"Table name: {region_table.table_name}")
print(f'id: {region.id}')
print(f'name: {region.name}')
print('-'*40)