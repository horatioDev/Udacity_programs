# Finance Metrics
'''
When you look at the financial metrics, you are focusing on tracking your performance against your company’s financial goal. 
  - How is your revenue comparing to the costs?
  - How are sales trending against sales goals?
  - How are sale and marketing lead metrics comparing against acquisitions?
'''

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

# Profit and Loss
'''

'''
def profit_loss():
  try:
    total_rev = get_positive_float_input('Enter Total Sales Revenue: ')
    cogs = get_positive_float_input('Enter Cost of Goods Sold: ')
    gross_profit = total_rev - cogs

    # Gross Margin
    gross_margin = gross_profit/total_rev
    gm_percent = gross_margin * 100
    gm_dollar = gross_margin

    # # Contribution Margin
    # nogs = get_integer_input('Enter total number of goods sold: ')
    # variable_cost = 0
    # contribution_margin = total_rev - variable_cost
    # contrib_margin_per_unit = contribution_margin/nogs
    
    sgax = get_positive_float_input('Enter Total of Selling, General, and Admin expenses: ')
    total_op_exp = get_positive_float_input('Enter Total of Operating Expenses: ')
    
    # EBIT - Earnings Before Interest and Tax (ebit)
    ebit = gross_profit - total_op_exp
    # Get interest and taxes
    interest = get_float_input('Enter Total sum of interest: ')
    taxes = get_float_input('Enter Total sum of taxes: ')

    if interest != 0 or taxes != 0:
      interest_and_taxes_total = interest + taxes
      net_income = ebit - interest_and_taxes_total
    else:
      net_income = ebit

    income_statement = {
      'Total Revenue': total_rev,
      'COGS': cogs,
      'Gross Profit': gross_profit,
      'SGA Expense': sgax,
      'Total Operating Cost': total_op_exp,
      'Operating Income': ebit,
      'Interest': interest,
      'Taxes': taxes,   
      "Net Income":  round((net_income), 2),
      'Gross Margin in $': gm_dollar,
      'Gross Margin in %': gm_percent
    }
    return income_statement
  
  except Exception as e:
    print(f'An error occured: {e}')
    return None

# Provide user instructions
print("Welcome to the Finance Metrics Calculator.")
print("This tool will help you calculate the profit and loss statement.")
print("Please enter the following financial values when prompted:")
income_statement = profit_loss()
if income_statement is not None:
  print('*' * 18,'Income Statement','*' * 19)
  for k, v in income_statement.items():
    if k == 'Gross Margin in %':
      print(f'{k}: {v}')
    else:
      print(f'{k}: ${v:,.2f}')
  # print(f'Income Statement: {income_statement}')
else:
  print(f'Unable to calculate income statement due to errors.')

print('-'*60)

def contribution_margin():
  total_rev = get_positive_float_input('Enter Total Sales Revenue: ')
  variable_cost = get_positive_float_input('Enter Variable Costs: ')
  nogs = get_positive_integer_input('Enter Number of Goods Sold: ')


  # Contribution Margin
  contribution_margin = total_rev - variable_cost
  contrib_margin_per_unit = contribution_margin/nogs
  contribData = [contribution_margin, round(contrib_margin_per_unit, 2)]
  return contribData
print("Welcome to the Finance Metrics Calculator.")
print("This tool will help you calculate the contribution margin and contribution margin per unit.")
print("Please enter the following financial values when prompted:")
contribData = contribution_margin()
print(f'Contribution Margin: ${contribData[0]:,.2f}, Contribution Margin Per Unit: ${contribData[1]}')
print('-'*60)