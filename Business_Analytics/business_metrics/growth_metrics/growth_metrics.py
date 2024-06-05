# Growth/Engagement Metrics
'''
Measuring your company's growth

Growth for a website or app is counted in the number of users.

Are we seeing the number of people actually using the site increasing or decreasing?
If you see your website use as high, are they unique users or the same people coming back?

  - Active users:
    - Engagement metrics are used to define the number of active users within a specific time period (ranging from daily, weekly to monthly).
    - Monthly Active Users: Number of unique active users in the previous month
    - Daily Active Users: Number of unique active users the previous day

  - Stickiness:
    - Daily Active Users/ Monthly Active Users
  - Churn rate:
    - (Customers beginning of usage interval - Customers end of usage interval) / Customers beginning of usage interval

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

# Get Positive Float Integer
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


# Get Active Users: Daily - Monthly
# def active_users():
    '''    
    # Gather and return a list of active user data for multiple months.
    # Each entry in the list is a dictionary containing month, DAU, and MAU data.
    # '''
    # num_of_months = get_positive_integer_input('Enter number of months to analyze: ')
    # print('-'*60)

    # # List to store user data
    # users_data = list()

    # for m in range(num_of_months):
    #   month_input = get_string_input(f'Enter month {m+1}: ').capitalize()
    #   while True:
    #     try:
    #       DAU_input = get_positive_integer_input(f'Enter daily active users for {month_input}: ')
    #       MAU_input = get_positive_integer_input(f'Enter monthly active users for {month_input}: ')
    #       month_data = {'month': month_input, 'DAU': DAU_input, 'MAU': MAU_input}
    #       users_data.append(month_data)
    #       break
    #     except ValueError:
    #       print("Invalid input. Please enter a valid number.")
    #       print('-' * 60)
      # print(f'Month: {m+1}')
      # DAU = get_integer_input(f'Enter daily active users for {month}: ')
      # MAU = get_integer_input(f'Enter monthly active users for {month}: ')
    #   print('-'*60)
    # return users_data
# print(f'Answer the following to calculate the Daily Active Users, Monthly Active Users & Stickiness Rate:')
# users = active_users()
# print('\nActive Users:')
# for user_data in users:
#   print(f"Month: {user_data['month']}, DAU: {user_data['DAU']}, MAU: {user_data['MAU']}")
print('-'*85)


# Get Stickiness Ratio
'''
Stickiness = Daily Active Users/ Monthly Active Users
It is a useful KPI for management and investors. It tells the management what is their company's growth rate. Investors want to know if this online app or website has the potential to make money in the future. For example, if the plan is to introduce advertising into the app, the potential valuation will depend on whether the app has a large number of users that keep coming back to it.
'''
def stickiness(dau, mau):
    ratio = dau / mau
    if mau == 0:
      return 0.0
    return ratio
# users = active_users()
# print('\nActive Users:')
# for user_data in users:
#   dau = user_data['DAU']
#   mau = user_data['MAU']
#   stickiness_ratio = stickiness(dau, mau)

#   print(f"Month: {user_data['month']}, DAU: {user_data['DAU']}, MAU: {user_data['MAU']}, Stickiness: {stickiness_ratio:.2%}")
print('-'*85) 

# Churn Rate
'''
To calculate the customer churn rate you need 2 simple things:
  - Customers at the beginning of usage interval
  - Customers at the end of the usage interval

Important note: We only want to calculate the churn rate based on the customers we started the time interval with. When getting the number of customers at the end of the interval, we do NOT add the customers who converted during the interval. The churn rate should only tell you whether the current customers have left or stayed.

Usage Interval: This time period should make sense for the service or product the customers are using. It can range from a day, a week, to a month or quarter. It depends on the service or product the company is providing and how often you would expect a customer to be active on the website.

As you calculate your annual churn rate, keep in mind a few other "data assumptions" that you need to watch out for.
  - Select a time interval during which you calculate the churn rate that is consistent with the company's subscription or usage model. There is no ideal usage interval - the usage interval depends on the length of time the company expects the user to be active at least once.
  - Pay attention to different customer segments, especially if they have different churn rates (e.g., by region).
  - Make sure your data does not include new customers gained during the time interval. Churn rate is focusing on customers who stayed or are active vs. stop being active on the website.

Churn Rate = (Customers at start of usage interval - Customers at end of usage interval) / Customers at start of usage interval

  - Churn rate is a measure of declining growth. Business need to make sure that they are acquiring new customers at a rate faster than their "churn rate"
  - Growth rate is a measure of new customers being added in the usage interval.
'''
def churn_rate():
  num_of_months = get_integer_input('Number of months to analyze: ')
  print('-'*60)

  churn_data = list()

  for m in range(num_of_months):
    month_input = get_string_input(f'Enter month {m+1}: ')
    start_usage = get_positive_integer_input(f'Customers at start of interval: ')
    end_usage = get_positive_integer_input(f'Customers at start of interval: ')

    try:
      churn_rate_data = round((start_usage - end_usage) / start_usage, 2)
    except ZeroDivisionError:
      churn_rate_data = 0

    churn_data.append({
        'Month': month_input.capitalize(),
        'Start Usage': start_usage,
        'End Usage': end_usage,
        'Churn Rate': churn_rate_data
    })
    print('-'*60)
    print(f'Month {m+1}: {month_input.capitalize()}, Beginning: {start_usage} | End: {end_usage} | Churn Rate: {churn_rate_data}')
    print('-'*60)

  return churn_data
    
print(f'Answer the following to calculate the Churn Rate:')
rate = churn_rate()
print(f'Churn Rate Data:')
for entry in rate:
  print(entry)
print('-'*85)