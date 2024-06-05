import numpy as np

def generate_bin_sizes(data, num_bins, method='auto'):
    """
    Generate bin sizes for histogram/binning.

    Parameters:
    data (array-like): The input data for which bins need to be generated.
    num_bins (int): The desired number of bins.
    method (str): Method for calculating bin sizes. Options: 'auto', 'sqrt', 'sturges', 'rice', 'scott', 'fd'.

    Returns:
    bin_sizes (list): List of bin sizes based on the chosen method.
    """

    if method == 'auto':
        bin_sizes = 'auto'
    elif method == 'sqrt':
        bin_sizes = int(np.sqrt(len(data)))
    elif method == 'sturges':
        bin_sizes = int(np.ceil(np.log2(len(data)) + 1))
    elif method == 'rice':
        bin_sizes = int(2 * len(data) ** (1/3))
    elif method == 'scott':
        bin_sizes = int((max(data) - min(data)) / (3.5 * np.std(data) * len(data) ** (-1/3)))
    elif method == 'fd':
        iqr = np.percentile(data, 75) - np.percentile(data, 25)
        bin_sizes = int(2 * iqr * len(data) ** (-1/3))
    else:
        raise ValueError("Invalid method. Supported methods: 'auto', 'sqrt', 'sturges', 'rice', 'scott', 'fd'.")

    return bin_sizes

# Example usage
data = [12, 15, 18, 21, 23, 25, 27, 29, 32, 35, 38, 41, 44]
num_bins = 5
method = 'sturges'
bin_sizes = generate_bin_sizes(data, num_bins, method)
print("Generated bin sizes:", bin_sizes)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# Marketing Funnel Metrics
'''
The marketing funnel is the process of tracking and analyzing each step of the customer journey with data.

Impressions & Reach: building brand and product awareness using ad platforms and search engine optimization (SEO).

  - Impressions: an instance of an advertisement appearing on a website when it is viewed by a visitor.

Lead generation: measures how many visits are made to the website.

  - Click: every time a website visitor views the ad and clicks it

  - Click Thru Rate: number of users that clicked an ad or clicked a link sent via email

  - Cost Per Click

  - Cost Per Lead: indicates a user has become a potential customer or lead because they have expressed interest in the company by downloading a document, creating an account, or providing an email address.

Conversion: when a lead converts to a paid customer
  - Customer Acquisition Cost

Loyalty:
  To grow their revenue and company profits, companies don’t just want their customers to buy once from them, but to come back to their website. Especially if the product is not a high-priced product. That customer loyalty allows you to track how many revisits a customer is making after their first purchase, or how many of the customers have continued shopping after their first purchase.

  Metrics: Some commonly used metrics include Repeat Purchase Rate and Net Promoter Score. We will not be going in-depth with these, but please do check out the resources below to learn more about them.

Advocacy:
  Another level companies sometimes track is whether their customer is advocating for their company. That is, saying good things about the product and services. Leaning on social media provides a great opportunity to do just that.

  Metrics: Some commonly used metrics include Customer Referrals and Leads from Social Media. For example, as the paid customer tweets about the company, likes the product on FB, provides a good rating on Amazon or the company website, analysts can use those metrics, such as ratings and likes to show how many of the customers serve as advocates.

'''

# impressions = int(input('Enter amount of Impressions: '))
# ad_investment = int(input('Enter cost of Advertisement: ')) 
# clicks = int(input('Enter amount of Clicks: ')) 
# leads = int(input('Enter amount of Visits to Site: '))

# Click Through Rate (CTR)
'''
As potential customers view the ads, some of those potential customers will click the ad and be taken to the website for the company. To be counted at this level, the user needs to click through the ad and the metric we use here is Click Through Rate.

  - Click Through Rate (CTR) is the ratio of users clicking on a link or an ad to the number of total users who received the link or saw the ad.

  - CTR measures the success of an advertising or email campaign.

  - When the CTR increases, it is an indicator of effective and interesting content in your ad campaign, and that maybe you should increase the number of impressions for that ad.

  - In general, a 2% CTR is good, however, the rate will vary by industry.

Click Through Rate (CTR) = (Clicks / Impressions) * 100
'''
def click_through_rate(impressions, clicks):
  ctr = round((clicks/impressions) * 100, 2)
  return ctr
CTR = click_through_rate(impressions=int(input('Enter amount of Impressions: ')), clicks=int(input('Enter amount of Clicks: ')) )
print(f'Click Through Rate: {CTR}%')
print('-'*60)

# Cost Per Click
'''
Cost Per Click (CPC) refers to the cost to get a click on your ad. It helps us gauge the cost of advertising on the specific platform, so we can see which platform is generating more leads.

  - CPC is an indicator of the cost-effectiveness of the ad platform and a useful tool to compare and strategize about which marketing platform is yielding a higher impression and reach and resulting in potential leads.

  - Different ad platforms cost differently and it is important to remember that while one platform might be cheaper it may not necessarily deliver you as many potential customers as another platform. This is an important trade-off that analysts and marketing teams have to consider.

  - Some marketing channels or platforms convert amazing results but they are small and may not generate as many customers. While you may decide to continue using them, you will also need to identify marketing channels that deliver more potential leads.

Cost Per Click (CPC) = Cost of Advertising on Source Platform / Number of Viewers who Clicked on the Ad
'''
def cost_per_click(ad_investment, clicks):
  cpc= round(ad_investment/clicks, 2)
  return cpc
CPC = cost_per_click(ad_investment=int(input('Enter cost of Advertisement: ')), clicks=int(input('Enter amount of Clicks: ')) )
print(f'Cost Per Click: ${CPC}')
print('-'*60)

# Cost Per Lead
'''
Remember, a lead is when a potential customer visits your website and does something on the website in response to a prompt, such as share their email , or download a document, create an account. Once the viewer takes that action, we know the viewer is showing some interest for the product or service, and this could possibly lead to a sale. With Cost Per Lead we are tracking whether the potential customer turned into a lead within a given time period, that could be a 30-day window or 60-day window.

We are calculating the cost of generating interest and nurturing the interest of the potential customer and figuring out how much did it cost us to get them to get to this level? The metric we calculate is the Cost Per Lead.

  - CPL is an indicator of the cost-effectiveness of the ad platform and a useful tool to compare and strategize about which marketing platforms yielded more leads. A low cost per lead means more of this particular type of person is likely to be interested in the product.

  - At the same time, Facebook also generated fewer clicks, so we need to consider if we need to tweak the ad for the Facebook platform or consider other platforms that can generate the same or higher number of clicks for a comparable price.

Cost Per Lead (CPL) = Cost of Advertising on Source Platform / Total Number of Leads
​
 

'''
def cost_per_lead(ad_investment, leads):
  cpl = round(ad_investment/leads, 2)
  return cpl
CPL = cost_per_lead(ad_investment=int(input('Enter cost of Advertisement: ')), leads=int(input('Enter amount of Visits to Site: ')))
print(f'Cost Per lead: ${CPL}')
print('-'*60)

# Customer Acquisition Cost (CAC)
'''
Customer Acquisition Cost (CAC) is the metric used in the last step of the marketing funnel and tells us what the cost is to acquire a paying customer.

This is the point where a lead, or potential customer, has become a customer by buying something on the website (a product or service). Most companies try to get that number under 25%.

The ultimate goal is to increase the lead-to-customer conversions at the bottom of the funnel. Considering the fact that customer shopping cart abandonment is over 60%, each company's goal is to get higher levels of conversions for the minimum cost of sales and marketing. This leads to the concept of optimizing the marketing funnel.

Customer Acquisition Cost (CAC) = Total sales & marketing costs / Number of converted customers
'''
def customer_acquisition_cost(marketing_cost, sales_salaries, overhead_cost, paid_customers):
  total_sales_marketing = (marketing_cost + sales_salaries + overhead_cost)
  cac = round((total_sales_marketing/paid_customers), 2)
  print(f'Total Sales & Marketing Costs: ${total_sales_marketing}')
  return cac
CAC = customer_acquisition_cost(marketing_cost=int(input('Enter Marketing Costs: ')), sales_salaries=int(input('Enter Sales & Marketing Costs: ')), overhead_cost=int(input('Enter Overhead costs for Sales and Marketing: ')), paid_customers=int(input('Enter Number of Paid Customers: ')))  
# print(f'Customer Acquisition Cost: ${CAC}')
print('-'*60)

def modified_cac(priorMonth={}, currMonth={}):
  marketing_cost = priorMonth['marketing_cost']
  priorWAC = 0.5*(priorMonth['sales_salaries'] + priorMonth['overhead_cost'])
  currWAC = 0.5*(currMonth['sales_salaries'] + currMonth['overhead_cost'])
  paid_customers = currMonth['paid_customers']
  mod_CAC = (marketing_cost + priorWAC + currWAC) / paid_customers
  return round(mod_CAC, 2)
CAC_2 = modified_cac(
  priorMonth={
    'marketing_cost': int(input('Enter Prior Month Marketing Costs: ')),
    'sales_salaries': int(input('Enter Prior Month Sales & Marketing Costs: ')),
    'overhead_cost': int(input('Enter Prior Month Overhead costs for Sales and Marketing: '))
  }, 
  currMonth={
    'sales_salaries': int(input('Enter Current Sales & Marketing Costs: ')),
    'overhead_cost': int(input('Enter Current Overhead costs for Sales and Marketing: ')),
    'paid_customers':int(input('Enter Paid Customers in Current month: '))
  }
)
print(f'Modified Customer Acquisition Costs: ${CAC_2}')
print('-'*60)

# Conversion Funnel
'''
Optimizing the funnel requires identifying at what level of the funnel your customer loss is the greatest. In other words, are you losing the most customers at the awareness and interest age, or is it when you are converting them into leads?

If you're losing many of them in the early stages of awareness, you need to focus on the types of ads you're creating, or the ad platforms you're choosing to reach your potential customers.

If you're losing many of them at the conversion stage, you need to look at your website or online app. It's possible the site is not easy to navigate, and that's why not many customers are converting to paid customers.

Conversion rates based on impressions
  - Basically, at each touchpoint, we'll divide the number of people at each touchpoint divided by the total number of customers.

Conversion rates based on each touchpoint
  - Another metric is to calculate the conversion rates based on the Call to Action at the previous level in the funnel, as opposed to the initial impression number as we did above.

  - So now we divide by the number of people who actually took the call to action of the previous step.
'''
def conversion_funnel():
  pass
conversion_rates = conversion_funnel()
print(f'Conversion Rate: {conversion_rates}%')
print('-'*60)


def marketing_funnel(da):
  pass

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
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

# Total Bookings
'''
Bookings are the most important sales metric. Booking is a won deal that is signed or where the purchaser is committed to buying the product. Once you have the sales bookings value, you can track it across specific time periods and even product lines.

**Total Bookings is the sum of all closed deals **
'''
def bookings():
    total_bookings = 0
    total_num_of_bookings = 0
    books = dict()
    num_of_accounts = int(input('How Many Accounts: '))
    print('-' * 30)

    for acct in range(num_of_accounts):
      try:
        accountName = input(f'Account Name {acct+1}: ')
        num_of_bookings = int(input(f'How Many Bookings for {accountName}: '))
        bookingCost_input = input(f'Cost of Booking: $')
        if bookingCost_input == '':
            bookingCost = 0.0  # Set the default cost to 0 if input is empty
        else:
            bookingCost = float(bookingCost_input)
        print('-' * 30)
      except ValueError:
        print('Invalid input. Skipping this account...')
        print('-' * 30)
        continue

      if accountName not in books:
        books[accountName] = bookingCost

      total_bookings += bookingCost

    for k, v in books.items():
      print(f'Account Name: {k}, Booking Cost: ${v}')

    return total_bookings

print(f'Answer the following to calculate the Total Bookings:')
closed_deal = bookings()
print(f'Total Bookings: ${closed_deal}')
print('-' * 60)


# Average Deal Size (in $)
'''
Another important metric to keep in mind is the Average Deal Size. This refers to the average deal size in dollars of all of the won deals. Reminder, a won deal is when the account buyer has committed to making the purchase.

As an analyst, you want to keep an eye out on the size of the deals you are winning, as any deal that is above this average deal size may involve more risk. The win rate for such sale prospects that are higher than the average deal size is usually low, but that doesn’t mean your sales rep shouldn’t pursue it. Rather these deals should be considered carefully for sales forecasting. Instead, if you see the historical data shows your average deal size is increasing, your sales team can explore and go after lead generation efforts for larger deals. It is also a reminder for the team to understand what is bringing these larger deals into your pipeline.

Average Deal Size = Total Sale Value of all Bookings / Total Number of Bookings
'''
# def avg_deal_size():
#     # total_bookings = 0
#     total_num_of_bookings = 0
#     books = dict()
#     num_of_accounts = int(input('How Many Accounts: '))

#     for acct in range(num_of_accounts):
#       accountName = input(f'Enter account name for account {acct + 1}: ')
#       num_of_bookings = int(input(f'How Many Bookings for {accountName}: '))
#       account_total = 0

#       for booking in range(num_of_bookings):
#         try:
#           while True:
#             booking_input = input(f'Cost of book {booking + 1}: $')
#             if booking_input == '':
#                 print("Booking input cannot be empty. Please enter a value.")
#                 continue
#             bookingCost = float(booking_input)
#             account_total += bookingCost
#             total_num_of_bookings += 1
#             break  # Exit the while loop if valid input is received
#         except ValueError:
#             print(f'Invalid booking value')
#             print('-' * 30)

#       if accountName not in books:
#         books[accountName] = account_total

#     print(f'Books: {books}')

#     for account, cost in books.items():
#        print(f'Total Bookings: {account} - ${cost}')

#     # if total_num_of_bookings == 0:
#     #     return 0.0  # Avoid division by zero
#     # return total_bookings / total_num_of_bookings

# print(f'Answer the following to calculate the Average Deal Size:')
# deal_size = avg_deal_size()
# print(f'Average Deal Size: ${deal_size}')


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



levels={
    'prospects',
    'leads',
    'qualified_leads',
    'conversion_bookings'
}

print(1910000/3)
print(f'Sales Funnel')