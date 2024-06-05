# Table and Row Object
class Table:
    table_count = 0  # Class-level variable to count the number of tables created

    def __init__(self, table_name, **kwargs):
        self.table_name = table_name
        self.columns = list(kwargs.keys())
        self.table_rows = []

        for key, val in kwargs.items():
            setattr(self, key, val)

        Table.table_count += 1

    def add_row(self, *row_values):
        if len(row_values) != len(self.columns):
            print('Error: Row length does not match the number of Columns')
            print(f'Row/Columns: {row_values}: {len(row_values)}, {self.columns}: {len(self.columns)}')
            return
        row = dict(zip(self.columns, row_values))
        row['pk'] = self.get_row_id()
        row = {'pk': row['pk'], **{key: value for key, value in row.items() if key != 'pk'}}
        self.table_rows.append(row)

    def get_row_id(self):
        current_ids = [row['pk'] for row in self.table_rows]

        if current_ids:
            new_id = max(current_ids) + 1
        else:
            new_id = 1
        return new_id


class Row:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


def data_converter(col_type, user_input):
    try:
        if col_type == int:
            return int(user_input)
        elif col_type == float:
            return float(user_input)
        elif col_type == bool:
            return bool(user_input)
        else:
            return str(user_input)
    except ValueError:
        return None


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


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


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid float.")


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


def get_string_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():  # Check if the input is not empty
            return value
        print("Invalid input. Please enter a non-empty string.")


def create_table_from_user_input():
    table_count = get_positive_integer_input('How many Tables will be needed: ')
    userTableData = []

    for table in range(table_count):
        table_name_input = get_string_input(f'Table {table + 1} name: ')
        columns_count = get_positive_integer_input(f'How many columns for {table_name_input}: ')
        columnsData = {}

        # Get column(s) name and type
        for col in range(columns_count):
            while True:
                col_input = get_string_input(f"Column {col + 1} (e.g., name=type): ")
                col_name, col_type = col_input.split('=')
                if col_type in ('int', 'float', 'str', 'bool'):
                    columnsData[col_name] = eval(col_type)
                    break
                else:
                    print("Invalid column type. Please use 'int', 'float', 'str', or 'bool'.")

        table_instance = Table(table_name=table_name_input, **columnsData)
        userTableData.append(table_instance)

        rows_count = get_positive_integer_input(f'How many rows for {table_name_input}: ')

        for _ in range(rows_count):
            row_data = {}
            for col_name, col_type in columnsData.items():
                user_input = input(f'Row {table_instance.get_row_id()} {col_name} input: ')
                converted_input = data_converter(col_type, user_input)
                row_data[col_name] = converted_input

            table_instance.add_row(*[row_data[col_name] for col_name in table_instance.columns])

    return userTableData


# if __name__ == "__main__":
#     d_table = create_table_from_user_input()
#     r_inst = d_table[0].table_rows[0]
#     table_func = d_table[0].Row(**r_inst)

#     print('-' * 40)
#     print(f"Table Count: {Table.table_count}")
#     print(f"Table Name: {d_table[0].table_name}")
#     print(f"Rows: {len(d_table[0].table_rows)}")
#     print(f'PK: {table_func.pk} {type(table_func.pk)}')
#     for col_name, col_type in d_table[0].columns.items():
#         if col_name != 'pk':
#             print(f'{col_name}: {getattr(table_func, col_name)} {type(getattr(table_func, col_name))}')
#     print('-' * 40)
