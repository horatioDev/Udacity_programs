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

        Table.table_count += 1
        # self.column_count += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    # Add row
    def add_row(self, *row_values):
        if len(row_values) != len(self.columns):
            # raise ValueError('Row length does not match number of Columns')
            print('Row length does not match the number of Columns')
            return
        row = dict(zip(self.columns, row_values))
        row['id'] = self.get_row_id()
        # Rearrange id placement
        row = {'id': row['id'], **{key: value for key, value in row.items() if key != 'id'}}
        self.table_rows.append(row)

    # Row Id: Generate id for each row
    def get_row_id(self):
        current_ids = [row['id'] for row in self.table_rows]

        if current_ids:
            new_id = max(current_ids) + 1
        else:
            new_id = 1
        return new_id

    class Row:
        '''
        '''

        # Constructor method
        def __init__(self, table_instance):
            self.table_instance = table_instance


# # table_name_input = input('Enter Table Name: ')
table_name_input = 'erd table'

# Table Instance
# table_instance = Table(table_name_input,'account_id', 'occurred_at', 'channel')
table_instance = Table(table_name_input, account_id=int, occurred_at=str, channel=str)
table_instance.table_name = table_name_input

# Row Instance
row_instance = Table.Row(table_instance=table_instance)
# table_instance.add_row(1001, '2023-10-10', 'Web')
table_instance.add_row(1301, '2023-10-09', 'App')

print('-' * 40)
print(f'Table Count: {table_instance.table_count} | Table Name: {table_instance.table_name} | Column(s) Count: {len(table_instance.columns)} | Table Row(s) Count: {len(table_instance.table_rows)}')
print('')
print(f'Table Name: {table_instance.table_name}')
print(f'Columns: {table_instance.columns}')
print(f'Rows: {table_instance.table_rows}')
print('-' * 40)

# Web Events
# web_events = Table('account_id', 'occurred_at', 'channel')
web_events = Table(table_name='web_events', account_id=int, occurred_at=str, channel=str)
web_events.add_row(1001, '2023-10-10', 'Web')

print('-' * 40)
print(f'Table Count: {web_events.table_count} | Table Name: {web_events.table_name} | Column(s) Count: {len(web_events.columns)} | Table Row(s) Count: {len(web_events.table_rows)}')
print('')
print(f'Table Name: {web_events.table_name}')
print(f'Columns: {web_events.columns}')
print(f'Rows: {web_events.table_rows}')
print('-' * 40)

# Accounts Table
accounts = Table(table_name='accounts', id=int, name=str, website=str, lat=float, long=float, primary_poc=str, sales_rep_id=int)
accounts.add_row(1001, 'Walmart', 'www.walmart.com', 40.23849561, -75.10329704, 'Tamara Tuma', 321500)

print('-' * 40)
print(f'Table Count: {accounts.table_count} | Table Name: {accounts.table_name} | Column(s) Count: {len(accounts.columns)} | Table Row(s) Count: {len(accounts.table_rows)}')
print('')
print(f'Table Name: {accounts.table_name}')
print(f'Columns: {accounts.columns}')
print(f'Rows: {accounts.table_rows}')
print('-' * 40)

# # Orders Table
# orders = Table(table_name='orders', account_id=int, standard_qty=int, poster_qty=int, gloss_qty=int, occurred_at=str, standard_amt_usd=int, gloss_amt_usd=int, poster_amt_usd=int, total_amt_usd=int)

# # Sales Reps Table
# sales_reps = Table(table_name='sales_reps', name=str, region_id=int)

# # Region Table
# region = Table(table_name='region', name=str)

print('-' * 20)
print(f'{web_events.id} {accounts.id}')
print('-' * 20)
