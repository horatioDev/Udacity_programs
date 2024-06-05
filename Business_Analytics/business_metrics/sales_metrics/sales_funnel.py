# Sales Funnel
'''
Sales Lead: 
  - A sales lead refers to the number of potential customers who have shown interest or have been identified by the sales team member as being potentially interested in the product.

Qualified Lead:
  - A potential lead who has been vetted by the sales team as meeting key requirements of an ideal buyer. Sales teams check to see if the product offering is within the lead’s budget that will make them a viable buyer.

Booking:
  - Booking is a closed deal when the qualified buyer has committed to making the purchase. It is a key metric for tracking the success of the sales team.

Sales Pipeline:
  - Refers to the collection of steps a sales representative takes while navigating incoming leads or prospects through to making the final purchase. It is also used to track how well individual sales representatives are meeting their sales quota.

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

# Total Bookings
'''
Bookings are the most important sales metric. Booking is a won deal that is signed or where the purchaser is committed to buying the product. Once you have the sales bookings value, you can track it across specific time periods and even product lines.

**Total Bookings is the sum of all closed deals **
'''
def bookings():
    total_num_of_bookings = 0
    booking_accounts = dict()
    total_bookings = list()
    num_of_accounts = get_integer_input('How Many Accounts: ')
    num_of_bookings = get_integer_input(f'How Many Bookings: ')
    print('-' * 30)

    for acct in range(num_of_accounts):
      accountName = input(f'Account Name {acct + 1}: ')
      account_total = 0
      books = {}  # Create an empty dictionary to store booking details

      for booking in range(num_of_bookings):
        try:
          while True:
            booking_input = get_float_input(f'Cost of book {booking + 1}: $')

            if booking_input == '':
              print("Booking input cannot be empty. Please enter a value.")
              continue
            bookingCost = float(booking_input)
            account_total += bookingCost
            total_num_of_bookings += 1
            if booking + 1 in books:
              books[booking + 1] += bookingCost  # Summing the values for each book
            else:
              books[booking + 1] = bookingCost  # Store booking details
            break  # Exit the while loop if valid input is received
        except ValueError:
          print(f'Invalid booking value')
          print('-' * 30)

      booking_accounts[accountName] = {'total': account_total, 'books': books}  # Store the total and books in booking_accounts
      print(f'Account Total: {account_total}')
      print('-' * 30)

    print('\nBooking Details:')
    book_totals = {}
    for account, account_data in booking_accounts.items():
        account_total = account_data['total']
        books = account_data['books']
        print(f'Account: {account}, Total Booking: ${account_total:.2f}')
        for book, cost in books.items():
            print(f'  Book {book}: ${cost:.2f}')
            if book in book_totals:
                book_totals[book] += cost
            else:
                book_totals[book] = cost

    print('\nTotal Booking Costs per Book:')
    for book, total_cost in book_totals.items():
      total_bookings.append(total_cost)
      print(f'Total Bookings {book}: ${total_cost:.2f}')

    return total_bookings

# Provide user instructions
print(f'Welcome to the Sales Metrics Calculator.')
print(f'This tool will help you calculate total bookings for different accounts.')
print(f'Please enter the following financial values when prompted:')
# total_bookings = bookings()
# print(f'Total Number of Bookings: {total_bookings}')
print('-' * 60)

# Close Ratio
'''
xxx
'''
def close_ratio():
  ratio = 0
  return ratio

# Provide user instructions
print(f'Welcome to the Sales Metrics Calculator.')
print(f'This tool will help you calculate total bookings for different accounts.')
print(f'Please enter the following financial values when prompted:')
# closeRatio = close_ratio()
# print(f'Close Ratio {closeRatio}')
print('-' * 60)


# Average Deal Size (in $)
'''
Another important metric to keep in mind is the Average Deal Size. This refers to the average deal size in dollars of all of the won deals. Reminder, a won deal is when the account buyer has committed to making the purchase.

As an analyst, you want to keep an eye out on the size of the deals you are winning, as any deal that is above this average deal size may involve more risk. The win rate for such sale prospects that are higher than the average deal size is usually low, but that doesn’t mean your sales rep shouldn’t pursue it. Rather these deals should be considered carefully for sales forecasting. Instead, if you see the historical data shows your average deal size is increasing, your sales team can explore and go after lead generation efforts for larger deals. It is also a reminder for the team to understand what is bringing these larger deals into your pipeline.

Average Deal Size = Total Sale Value of all Bookings / Total Number of Bookings
'''
def avg_deal_size():
  avg_deal = []  # List to store average deal sizes
  booking_accounts = dict()
  num_of_accounts = get_integer_input('How Many Accounts: ')
  num_of_bookings = get_integer_input('How Many Bookings: ')
  print('-' * 30)

  for acct in range(num_of_accounts):
    accountName = get_string_input(f'Name for account {acct + 1}: ')
    booking_list = []  # Create an empty list to store booking details
    account_total = 0

    # Get Booking Data
    print(f' Books for {accountName}:')
    for booking in range(num_of_bookings):
        try:
          while True:
            booking_input = get_float_input(f'  Cost of book {booking + 1}: $')
            if booking_input == '':
                print("Booking input cannot be empty. Please enter a value.")
                continue
            bookingCost = booking_input
            booking_list.append(bookingCost)  # Store booking details
            account_total += bookingCost
            break  # Exit the while loop if valid input is received
        except ValueError:
          print(f'Invalid booking value')
          print('-' * 30)
    print('-' * 30)

    deals = []  # Create an empty list to store deal details
    account_deals_total = 0
    num_of_deals = num_of_bookings

    # Get Deals Data
    print(f' Number of Deals for {accountName}')
    
    for deal in range(num_of_deals):
        try:
          while True:
            deal_input = get_integer_input(f' Deal Number for book {deal + 1}: ')
            if deal_input == '':
                print('Deal input cannot be empty. Please enter a value.')
                continue
            dealNum = int(deal_input)
            deals.append(dealNum)  # Store deal details
            account_deals_total += dealNum
            break
        except ValueError:
          print(f'Invalid deal value')
          print('-' * 30)
    print('-' * 30)

    # Store the data in the booking_accounts dictionary
    booking_accounts[accountName] = {
      'booking_list': booking_list,
      'total_bookings': account_total,
      'deals': deals,
      'total_deals': account_deals_total,
      'avg_deal_size': round(account_total / account_deals_total, 2) if account_deals_total != 0 else 0.0
    }

  print('\nBooking Details:')
  for account, data in booking_accounts.items():
    avg_deal.append(data['avg_deal_size'])
    print(f'Account: {account}')
    print(f'  Average Deal Size: ${data["avg_deal_size"]:.2f}')
    print('-' * 30)

  return avg_deal

# Provide user instructions
print(f'Welcome to the Sales Metrics Calculator.')
print(f'This tool will help you calculate the average deal size for different accounts.')
print(f'Please enter the following financial values when prompted:')
# ADS = avg_deal_size()
# print(f'Average Deal Size(s): {ADS}')
print('-' * 60)

# Average Time to Close
'''
The average time to close the deal is the average number of days it takes a member of the sales team to close the deal from the prospect stage to a closed deal.

This metric can be calculated for each sales team member, product, or lead source. The lead source refers to whether the prospect inquired through the website or had an inbound inquiry. On the other hand, outbound methods refer to cold-calling through email lists or phone calls. This means the customer has lower intent to purchase, to begin with, and this lengthens the time to close the deal.

Terminology:
  - Sum of Total number of days from the first contact to closing the deal for all closed deals
  - The average number of days for typical Sales Cycle = Sum(Total number of days to close the deal) for all closed deals / Number of closed deals

Calculation:
  - Step 1. Sum (Total number of days from the first contact to closing the deal) for ALL closed deals.

  - Step 2. The average number of days for typical Sales Cycle = Sum (Total number of days from the first contact to closing the deal) for ALL closed deals / Number of deals

COUNTA = Allows you to count the number of non-empty cells within an array
'''
def avg_close_time():
  close_times = []
  total_num_of_days = 0
  num_of_accounts = get_integer_input('How Many Accounts: ')
  print('-' * 60)

  for acct in range(num_of_accounts):
    accountName = get_string_input(f'Name of account {acct + 1}: ')
    while True:
      try:
        num_of_days_input = get_integer_input(f'Enter number of days from first contact to closing {accountName}: ')
        if num_of_days_input == '':
          print("Number of days input cannot be empty. Please enter a value.")
          continue
        num_of_days = int(num_of_days_input)
        account_total = num_of_days
        print('-' * 60)
        total_num_of_days += num_of_days
        break  # Exit the loop if valid input is received
      except ValueError:
        print("Invalid input. Please enter a valid number.")
        print('-' * 60)

  avg_close = total_num_of_days / num_of_accounts
  close_times.append(avg_close)
  return close_times

# Provide user instructions
print(f'Welcome to the Sales Metrics Calculator.')
print(f'This tool will help you calculate the average time it takes to close deals for different accounts.')
print(f'Please enter the following financial values when prompted:')
# ACT = avg_close_time()
# print(f'Average Close Time: {ACT}')
print('-'*60)


