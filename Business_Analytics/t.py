def get_integer_input(prompt):
  while True:
    try:
      value = int(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a valid integer.")

# def conversion_funnel(levels={}):
#     impressions = levels['awareness']
#     conversion_rates = {}
    
#     for key in levels:
#         if key != 'awareness':
#             rate = levels[key] / impressions
#             conversion_rates[key] = round(rate, 3)

#     return conversion_rates

# print(f'Answer the following to calculate the Conversion rates based on impressions & level touch point:')
# levels = {
#     'awareness': get_integer_input('Enter amount of site visits/impressions: '),
#     'interest': get_integer_input('Enter amount of who interacted with site: '),
#     'desire': get_integer_input('Enter amount of who added items to cart: '),
#     'conversion': get_integer_input('Enter amount of who made a purchase: ')
# }

# conversion_rates = conversion_funnel(levels)
# print(f'Conversion Rates: {conversion_rates}')
# print('-' * 80)



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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Total Revenue
def total_revenue():
  total = get_integer_input('Enter Total Sales Revenue: ')
  return total
# totalRevenue = total_revenue()
# print(f'Total Revenue: ${totalRevenue:,}')
# print('-'*60)

# Cost of Goods Sold
def cost_of_goods_sold():
  cogs = get_integer_input('Enter Cost of Goods Sold: ')
  return cogs
# costOfGoodsSold = cost_of_goods_sold()
# print(f'Cost of Goods Sold: ${costOfGoodsSold:,}')
# print('-'*60)

# Gross Profit
def gross_profit():
  totalRev = total_revenue()
  cogs = cost_of_goods_sold()
  profit = totalRev - cogs
  return profit
# grossProfit = gross_profit()
# print(f'Gross Profit: ${grossProfit:,}')
# print('-'*60)

# Research & Development
def research_development():
  rd = get_integer_input('Enter Research & Development Cost: ')
  return rd
# researchDev = research_development()
# print(f'Research & Development: ${researchDev:,}')
# print('-'*60)

# Sales & Marketing
def sales_marketing():
  sm = get_integer_input('Enter Sales and Marketing Expense: ')
  return sm
# salesMarketing = sales_marketing()
# print(f'Sales & Marketing: ${salesMarketing:,}')
# print('-'*60)

# General & Administrative
def general_administrative():
  ga = get_integer_input('Enter General and Administrative Expenses: ')
  return ga
# generalAdministrative = general_administrative()
# print(f'General & Administrative: ${generalAdministrative:,}')
# print('-'*60)

# Total Operating Expenses
def operating_expenses():
  rd = research_development()
  sm = sales_marketing()
  ga = general_administrative()
  opExpenses = (rd + sm + ga)
  return opExpenses
# operatingExpenses = operating_expenses()
# print(f'Total Operating Expenses: ${operatingExpenses:,}')
# print('-'*60)

# Operating Income
def operating_income():
  '''
  Earnings before interest and taxes (EBIT) indicate a company's profitability. EBIT is calculated as revenue minus expenses excluding tax and interest.
  '''
  gp = gross_profit()
  opExp = operating_expenses()
  ebit = gp - opExp
  return ebit
# operatingIncome = operating_income()
# print(f'Operating Income (EBIT): ${operatingIncome:,}')
# print('-'*60)

# Depreciation & Amortization
def depreciation_amortization():
  da = get_integer_input('Enter Depreciation & Amortization: ')
  return da
# depreciationAmortization = depreciation_amortization()
# print(f'Depreciation & Amortization: $ {depreciationAmortization:,}')
# print('-'*60)

# EBITDA
def ebitda():
  '''
  Expenses Before Income Taxes + Depreciation & Amortization
  EBITDA is calculated by adding interest, tax, depreciation, and amortization expenses to net income.
  '''
  opIncome = operating_income()
  da = depreciation_amortization()
  ebitda = opIncome + da  
  return ebitda
# EBITDA = ebitda()
# print(f'EBITDA: ${EBITDA:,}')
# print('-'*60)

# Net Interest Income
def net_interest_income():
  nii = get_integer_input('Enter Net Interest Income: ')
  return nii
# netInterestIncome = net_interest_income()
# print(f'Net Interest Income (Expense): ${netInterestIncome}')
# print('-'*60)

# Income Before Taxes
def income_before_taxes():
  opIncome = operating_income()
  nii = net_interest_income()
  ibt = opIncome + nii
  return ibt
# incomeBeforeTaxes = income_before_taxes()
# print(f'Income Before Tax (EBIT): ${incomeBeforeTaxes}')
# print('-'*60)

# Taxes
def calculate_taxes():
  tax = get_integer_input('Enter Taxes: ')
  return tax
# taxes = calculate_taxes()
# print(f"Total Taxes Payable: ${taxes:.2%}")
# print('-'*60)

def calculate_tax_rate():
  ibt = income_before_taxes()
  taxes = calculate_taxes()
  rate = taxes/ibt
  return rate
# taxRate = calculate_tax_rate()
# print(f'Tax Rate: {taxRate:.2%}')
# print('-'*60)

# Net Income
def net_income():
  # gross_income = gross_profit()
  # total_expenses = operating_expenses()
  # opInc = operating_income()
  # nii = net_interest_income()
  ibt = income_before_taxes()
  taxes = calculate_taxes()
  taxRate = calculate_tax_rate()
  # net = opInc - (nii + (ibt*taxRate))
  # net = ibt - (ibt*taxRate)
  # net2 = ibt + (ibt*taxRate)
  net = ibt - taxes
  return net
# netIncome = net_income()
# print(f'Net Income: ${netIncome:,}')
# print('-'*60)


# Get Historical Financial Data
# def historical_data():

#   yrCount = get_integer_input('How many years will we be analyzing: ')
#   startYr = get_positive_integer_input('Enter Starting Year: ')
#   incomeStatementData = list()
#   print("Please enter the following financial values when prompted:")

#   for yr in range(yrCount):
#     year = startYr + yr
#     incomeStatementData[yr] = year
#     while True:
#       try:
#         # incomeStatementData = dict()
#         # year = startYr + yr
#         print(f'Year {yr+1}: {year}')
#         yearData = {
#           'Year': year,
#           'Revenue': total_revenue(),
#           'Cost of Goods Sold': cost_of_goods_sold(),
#           'Gross Profit': gross_profit(),
#           'Research & Development': research_development(),
#           'Sales & Marketing': sales_marketing(),
#           'General and Admin Expenses': general_administrative(),
#           'Total Operating Expenses': operating_expenses(),
#           'Operating Income (EBIT)': operating_income(),
#           'Depreciation & Amortization': depreciation_amortization(),
#           'EBITDA': ebitda(),
#           'Net Interest Income(Expense)': net_interest_income,
#           'Income Before Taxes': income_before_taxes(),
#           'Taxes': calculate_taxes(),
#           'Tax Rate': calculate_tax_rate(),
#           'Net Income': net_income()
#         }
#         incomeStatementData.append(year)
#         break
#       except Exception as e:
#         print(f'Error occurred {e}')

#     print(f'Year {yr+1}: {yearData}')

  
#   # for yrData in incomeStatementData:
#   #   year = {
#   #     'Year': yrData,
#   #     'Revenue': totalRevenue,
#   #     'Cost of Goods Sold': cogs,
#   #     'Gross Profit': grossProfit,
#   #     # 'Research & Development': resDev,
#   #     # 'Sales & Marketing': salesMkt,
#   #     # 'General and Admin Expenses': ga,
#   #     # 'Total Operating Expenses': opExp,
#   #     # 'Operating Income (EBIT)': opInc,
#   #     # 'Depreciation & Amortization': da,
#   #     # 'EBITDA': EBITDA,
#   #     # 'Net Interest Income(Expense)': netInterestIncome,
#   #     # 'Income Before Taxes': incomeBeforeTaxes,
#   #     # 'Taxes': taxes,
#   #     # 'Tax Rate': taxRate,
#   #     # 'Net Income': netIncome
#   #     }
#   #   print(year, yrData, year['Year'], type(yrData))
#   #   # print(yr, startYr + yr, incomeStatementData, incomeStatementData[yr], type(year), year, type(year))

#   data = incomeStatementData
#   return data 
# historicalData = historical_data()
# print(f'Historical Data: {historicalData}')


# Define functions for getting financial data (same as previous code)
# ...

# Function to collect historical data: Profit & Loss = Income Statement
def income_statement():
    yrCount = get_integer_input('How many years will we be analyzing: ')
    startYr = get_positive_integer_input('Enter Starting Year: ')
    incomeStatementData = []

    print("Please enter the following financial values when prompted:")

    prev_yr_rev = None
    prev_yr_data = None

    for yr in range(yrCount):
      while True:
        try:
          year = startYr + yr
          print(f'Year {yr + 1}: {year}')
          revenue = total_revenue()
          cogs =  cost_of_goods_sold()
          grossProfit = (revenue - cogs)
          resDev = research_development()
          salesMkt = sales_marketing()
          genAdmin = general_administrative()
          opExpenses = (resDev + salesMkt + genAdmin)
          opIncome = (grossProfit - opExpenses)
          depApp = depreciation_amortization()
          EBITDA = (opIncome + depApp)
          netInterest = net_interest_income()
          ebit = (opIncome + netInterest)
          taxes = calculate_taxes()
          taxRate = round((taxes/ebit), 2)
          # netIncome = round((ebit - taxes), 2)
          netIncome = round((ebit + taxes), 2)
          year_data = {
            'Year': year,
            'Revenue': revenue,
            'Cost of Goods Sold': cogs,
            'Gross Profit': grossProfit,
            'Research & Development': resDev,
            'Sales & Marketing': salesMkt,
            'General and Admin Expenses': genAdmin,
            'Total Operating Expenses': opExpenses,
            'Operating Income (EBIT)': opIncome,
            'Depreciation & Amortization': depApp,
            'EBITDA': EBITDA,
            'Net Interest Income(Expense)': netInterest,
            'Income Before Taxes': ebit,
            'Taxes': taxes,
            'Tax Rate': f'{taxRate:.2%}',
            'Net Income': netIncome,
            'Revenue Growth': None
          }

          # Calculate revenue growth for subsequent years
          # if prev_yr_data is not None:
          #   revGrowth = (revenue / prev_yr_data['Revenue']) - 1
          #   year_data['Revenue'] = f'{revGrowth:.2%}'

          if yr > 0:
            prev_year_data = incomeStatementData[-1]
          else:
            prev_year_data = None

          incomeStatementData.append(year_data)
          # prev_yr_rev = revenue
          forecast_results = forecast_IS(year, year_data, prev_yr_data)
          print(f'Forecast for {year}: {forecast_results}')

          prev_yr_data = year_data
          break
        except Exception as e:
          print(f'Error occurred: {e}')

    return incomeStatementData

# Income Statement Forecast
def forecast_IS(year, year_data, prev_yr_data):
  
  
  
  if prev_yr_data is None:
    return {}

  # forecast_data = {
  #   'Year': year,
  #   'Forecasted Revenue Growth': None,
  #   'Forecasted Gross Margin' : None,
  #   'Forecasted Operating Margin': None,
  #   'Forecasted Historical Tax Rate': None,
  #   'Forecasted Historical Interest Rate': None
  # }
  
  yr_over_yr_growth_rates_data = {
    'Year': year,
    # 'Revenue': (year_data['Revenue'] / prev_yr_data['Revenue']) - 1,
    'Revenue': f'{revGrowthRate:.2%}',
    'Gross Profit' : f'{grossProfitRate:.2%}',
    'EBIT': f'{ebitRate:.2%}',
    'Net Income': f'{netIncomeRate:.2%}'
  }

  cogsRatio = (year_data['Cost of Goods Sold'] / year_data['Revenue']) * 100
  grossMarginRatio = (year_data['Cost of Goods Sold'] / year_data['Revenue']) * 100
  rdRatio = (year_data['Research & Development'] / year_data['Revenue']) * 100
  salesRatio = (year_data['Sales & Marketing'] / year_data['Revenue']) * 100
  genAdminRatio = (year_data['General and Admin Expenses'] / year_data['Revenue']) * 100
  depAppRatio = (year_data['Depreciation & Amortization'] / year_data['Revenue']) * 100
  taxRatio = (year_data['Taxes'] / year_data['Operating Income (EBIT)']) * 100

  margin_ratios = {
    'Year': year,
    'COGs': f'{cogsRatio:.2%}',
    'Gross Margin': f'{grossMarginRatio:.2%}',
    'R&D': f'{rdRatio:.2%}',
    'S&M': f'{salesRatio:.2%}',
    'G&A': f'{genAdminRatio:.2%}',
    'D&A': f'{depAppRatio:.2%}',
    'Tax Rate': f'{taxRatio:.2%}'
  }

  # Year Over Year Growth Rates

  # rev_growth_percent = (year_data['Revenue'] / prev_yr_data['Revenue']) - 1
  # gross_margin = 1 - (year_data['Cost of Goods Sold'] / year_data['Revenue'])
  # operating_margin = year_data['Operating Income (EBIT)'] / year_data['Revenue']
  # historical_tax_rate = 0
  # historical_interest_rate = 0
  # forecast_data = 100
  return forecast_data, yr_over_yr_growth_rates_data, margin_ratios

# forecast = forecast_IS(year=, year_data=, prev_yr_data=)
# print(f'Forecast: {forecast}')


# Call the income_statement function to collect data
incomeStatement = income_statement()

# Print the collected data from Income Statement
for year_data in incomeStatement:
    print(year_data)

# Cash Flow
def cash_flow_statement():
  cash_flow = 0
  return cash_flow
# cash_flow_data = cash_flow_statement()
# print(f'Cash Flow Statement: {cash_flow_data}')

# Balance Sheet
def balance_sheet():
  balance = 0
  return balance
# balance_sheet_data = balance_sheet()
# print(f'Balance Sheet: {balance_sheet_data}')


# def financial_modeling():
#   assumptions = 0
#   rev_growth = 0
#   gross_profit = 0
#   ebit = 0
#   net_income = 0
#   cash_flow = 0
#   return assumptions
# model = financial_modeling()
# print(f'Model: {model}')

# Top Down Approach Model: Macro Approach
def top_down_modeling():
  global_economy = 0
  local_economy = 0
  sector = 0
  industry = 0
  spec_business = 0
  top_down = 0
  return top_down
# top_down_approach = top_down_modeling()
# print(f'Top Down Modeling: {top_down_approach}')

# Bottom Up Approach Model: Macro Approach
def bottom_up_modeling():
  global_economy = 0
  local_economy = 0
  sector = 0
  industry = 0
  spec_business = 0
  bottom_up = 0
  return bottom_up
# bottom_up_approach = bottom_up_modeling()
# print(f'Bottom Up Modeling: {bottom_up_approach}')


# Forecast Modeling
def forecast_modeling():
  forecast_input = get_string_input('Type of Forecast (Finance or Sales): ')
  print(f'Forecast Model: {forecast_input}')
  historical_data = 0
  assumptions = 0
  scenarios = 0
  forecasts = 0
  return forecasts
# forecasted_models = forecast_modeling()
# print(f'Forecast Models: {forecasted_models}')

print(f'Finance Modeling')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Python initializer
# if __name__ == "__main__":
#   totalRevenue = total_revenue()
#   print(f'Total Revenue: ${totalRevenue:,}')

#   costOfGoodsSold = cost_of_goods_sold()
#   print(f'Cost of Goods Sold: ${costOfGoodsSold:,}')

#   grossProfit = gross_profit()
#   print(f'Gross Profit: ${grossProfit:,}')

#   researchDev = research_development()
#   print(f'Research & Development: ${researchDev:,}')

#   salesMarketing = sales_marketing()
#   print(f'Sales & Marketing: ${salesMarketing:,}')

#   generalAdministrative = general_administrative()
#   print(f'General & Administrative: ${generalAdministrative:,}')

#   operatingExpenses = operating_expenses()
#   print(f'Total Operating Expenses: ${operatingExpenses:,}')

#   operatingIncome = operating_income()
#   print(f'Operating Income (EBIT): ${operatingIncome:,}')

#   depreciationAmortization = depreciation_amortization()
#   print(f'Depreciation & Amortization: ${depreciationAmortization:,}')

#   EBITDA = ebitda()
#   print(f'EBITDA: ${EBITDA:,}')

#   netInterestIncome = net_interest_income()
#   print(f'Net Interest Income (Expense): ${netInterestIncome}')

#   incomeBeforeTaxes = income_before_taxes()
#   print(f'Income Before Tax (EBIT): ${incomeBeforeTaxes}')

#   taxes = calculate_taxes()
#   print(f"Total Taxes Payable: ${taxes:.2f}")

#   taxRate = calculate_tax_rate()
#   print(f'Tax Rate: {taxRate:.2%}')

#     netIncome = net_income()
#     print(f'Net Income: ${netIncome:,}')