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


# Click Through Rate (CTR)
'''
As potential customers view the ads, some of those potential customers will click the ad and be taken to the website for the company. To be counted at this level, the user needs to click through the ad and the metric we use here is Click Through Rate.

  - Click Through Rate (CTR) is the ratio of users clicking on a link or an ad to the number of total users who received the link or saw the ad.

  - CTR measures the success of an advertising or email campaign.

  - When the CTR increases, it is an indicator of effective and interesting content in your ad campaign, and that maybe you should increase the number of impressions for that ad.

  - In general, a 2% CTR is good, however, the rate will vary by industry.

Click Through Rate (CTR) = (Clicks / Impressions) * 100
'''
def click_through_rate():
  impressions = get_integer_input('Enter amount of Impressions: ')
  clicks = get_integer_input('Enter amount of Clicks: ')

  ctr = round((clicks/impressions) * 100, 2)
  return ctr

print(f'Answer the following to calculate the Click Through Rate (CTR):')
# CTR = click_through_rate()
# print(f'Click Through Rate: {CTR}%')
print('-'*80)

# Cost Per Click
'''
Cost Per Click (CPC) refers to the cost to get a click on your ad. It helps us gauge the cost of advertising on the specific platform, so we can see which platform is generating more leads.

  - CPC is an indicator of the cost-effectiveness of the ad platform and a useful tool to compare and strategize about which marketing platform is yielding a higher impression and reach and resulting in potential leads.

  - Different ad platforms cost differently and it is important to remember that while one platform might be cheaper it may not necessarily deliver you as many potential customers as another platform. This is an important trade-off that analysts and marketing teams have to consider.

  - Some marketing channels or platforms convert amazing results but they are small and may not generate as many customers. While you may decide to continue using them, you will also need to identify marketing channels that deliver more potential leads.

Cost Per Click (CPC) = Cost of Advertising on Source Platform / Number of Viewers who Clicked on the Ad
'''
def cost_per_click():
  ad_investment = get_integer_input('Enter cost of Advertisement: ')
  clicks = get_integer_input('Enter amount of Clicks: ')

  cpc= round(ad_investment/clicks, 2)
  return cpc

print(f'Answer the following to calculate the Cost Per Click (CPC):')
# CPC = cost_per_click()
# print(f'Cost Per Click: ${CPC}')
print('-'*80)

# Cost Per Lead
'''
Remember, a lead is when a potential customer visits your website and does something on the website in response to a prompt, such as share their email , or download a document, create an account. Once the viewer takes that action, we know the viewer is showing some interest for the product or service, and this could possibly lead to a sale. With Cost Per Lead we are tracking whether the potential customer turned into a lead within a given time period, that could be a 30-day window or 60-day window.

We are calculating the cost of generating interest and nurturing the interest of the potential customer and figuring out how much did it cost us to get them to get to this level? The metric we calculate is the Cost Per Lead.

  - CPL is an indicator of the cost-effectiveness of the ad platform and a useful tool to compare and strategize about which marketing platforms yielded more leads. A low cost per lead means more of this particular type of person is likely to be interested in the product.

  - At the same time, Facebook also generated fewer clicks, so we need to consider if we need to tweak the ad for the Facebook platform or consider other platforms that can generate the same or higher number of clicks for a comparable price.

Cost Per Lead (CPL) = Cost of Advertising on Source Platform / Total Number of Leads
​
 

'''
def cost_per_lead():
  ad_investment = get_integer_input('Enter cost of Advertisement: ')
  leads = get_integer_input('Enter amount of Visits to Site: ')

  cpl = round(ad_investment/leads, 2)
  return cpl

print(f'Answer the following to calculate the Cost Per Lead (CPL):')
# CPL = cost_per_lead()
# print(f'Cost Per lead: ${CPL}')
print('-'*80)

# Customer Acquisition Cost (CAC)
'''
Customer Acquisition Cost (CAC) is the metric used in the last step of the marketing funnel and tells us what the cost is to acquire a paying customer.

This is the point where a lead, or potential customer, has become a customer by buying something on the website (a product or service). Most companies try to get that number under 25%.

The ultimate goal is to increase the lead-to-customer conversions at the bottom of the funnel. Considering the fact that customer shopping cart abandonment is over 60%, each company's goal is to get higher levels of conversions for the minimum cost of sales and marketing. This leads to the concept of optimizing the marketing funnel.

Customer Acquisition Cost (CAC) = Total sales & marketing costs / Number of converted customers
'''
def customer_acquisition_cost():
  marketing_cost = get_float_input('Enter Marketing Costs: ')
  sales_salaries = get_float_input('Enter Sales & Marketing Costs: ')
  overhead_cost = get_float_input('Enter Overhead costs for Sales andMarketing: ')
  paid_customers = get_float_input('Enter Number of Paid Customers: ')

  total_sales_marketing = (marketing_cost + sales_salaries + overhead_cost)
  cac = round((total_sales_marketing/paid_customers), 2)
  print(f'Total Sales & Marketing Costs: ${total_sales_marketing}')
  return cac

print(f'Answer the following to calculate the Customer Acquisition Cost (CAC):')
# CAC = customer_acquisition_cost()  
# print(f'Customer Acquisition Cost: ${CAC}')
print('-'*80)

def modified_cac(priorMonth={}, currMonth={}):
  marketing_cost = priorMonth['marketing_cost']
  priorWAC = 0.5*(priorMonth['sales_salaries'] + priorMonth['overhead_cost'])
  currWAC = 0.5*(currMonth['sales_salaries'] + currMonth['overhead_cost'])
  paid_customers = currMonth['paid_customers']
  mod_CAC = (marketing_cost + priorWAC + currWAC) / paid_customers
  return round(mod_CAC, 2)

print(f'Answer the following to calculate the Modified Customer Acquisition Cost (CAC):')
# priorMonth={
#   'marketing_cost': get_float_input('Enter Prior Month Marketing Costs: '),
#   'sales_salaries': get_float_input('Enter Prior Month Sales & Marketing Costs: '),
#   'overhead_cost': get_float_input('Enter Prior Month Overhead costs for Sales and Marketing: ')
# }

# currMonth={
  # 'sales_salaries': get_float_input('Enter Current Sales & Marketing Costs: '),
  # 'overhead_cost': get_float_input('Enter Current Overhead costs for Sales and Marketing: '),
  # 'paid_customers':get_float_input('Enter Paid Customers in Current month: ')
# }

# CAC_2 = modified_cac(priorMonth, currMonth)
# print(f'Modified Customer Acquisition Costs: ${CAC_2}')
print('-'*80)

# Cost Per Acquisition
'''
The impact of marketing campaigns can also be measured in terms of revenue using metrics that capture the financial cost.

CPA: cost per acquisition:
  - Focuses on sales and marketing costs, including the cost of supplies, labor, marketing, overhead, and sales that it took to convert a non-paying customer(called an acquisition) into a paying customer.

What is the difference between CPA and CAC?

  - CPA: is focused on the marketing and sales cost, including overhead and salaries, with a focus on sales leads—not actual paying customers

  - CAC: is focused on actual new customers who have made a purchase

Cost Per Acquisition provides insight into whether or not the marketing campaigns are successful from a business perspective. For the purposes of calculating the CPA, the cost of the marketing campaigns should not be restricted to the cost of developing the ad, but also other costs of labor and overhead. In other words, CPA allows a business to gauge whether the marketing campaign is generating enough potential leads to cover a broader range of costs other than just direct advertisement costs.

Total Sales and Marketing Cost = (marketing costs + Sales and Marketing salaries + overhead costs for Sales and Marketing)

Cost Per Acquisition (CPA) = Total Sales and Marketing Cost / Number of Leads
'''
def cost_per_acquisition():
  marketing_cost = get_integer_input('Enter Marketing Costs: ')
  sales_salaries = get_integer_input('Enter Sales & Marketing Costs: ')
  overhead_cost = get_integer_input('Enter Overhead costs for Sales and Marketing: ') 
  num_of_leads = get_integer_input('Enter Number of Leads: ')
  
  total_sales_marketing_cost = (marketing_cost + sales_salaries + overhead_cost)
  print(f'Total Sales & Marketing Cost: ${total_sales_marketing_cost}')
  cpa = round(total_sales_marketing_cost / num_of_leads, 2)
  return cpa

print(f'Answer the following to calculate the Cost Per Acquisition (CPA):')
# CPA = cost_per_acquisition()
# print(f'Cost Per Acquisition: ${CPA}')
print('-'*80)


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
def conversion_funnel(levels={}):
  impression_conversion = {}
  touchpoint_conversion = {}

  previous_step = 'awareness'
  for key in levels:
    if key != 'awareness':
      impression_rate = levels[key] / levels['awareness']
      touchpoint_rate = levels[key] / levels[previous_step]
      
      impression_conversion[key] = round(impression_rate, 3)
      touchpoint_conversion[key] = round(touchpoint_rate, 2)
      
      previous_step = key
  
  return impression_conversion, touchpoint_conversion

print(f'Answer the following to calculate the Conversion rates based on impressions & level touch point:')
# levels = {
#   'awareness': get_integer_input('Enter amount of site visits/impressions: '),
#   'interest': get_integer_input('Enter amount of who interacted with site: '),
#   'desire': get_integer_input('Enter amount of who added items to cart: '),
#   'conversion': get_integer_input('Enter amount of who made a purchase: ')
# }

# impression_rates, touchpoint_rates = conversion_funnel(levels)
# print(f'Conversion Rates (Impressions): {impression_rates}')
# print(f'Conversion Rates (Touchpoint): {touchpoint_rates}')
print('-' * 80)

# Lifetime Value
'''
When deciding how to spend the marketing budget, you want to focus on some of your best customers – those that will stay for the long-term and continue to generate revenue for the company.

  - These are your high-value customers and you want to bring in more of them.

Your goal should be for every dollar spent on marketing efforts. It should provide a higher rate of return and generate revenue multiple times over.

Purchase Cycle:
  - The time increment adopted for business calculations

Total Sale Revenue Per Cycle: 
  - Revenue earned from a customer per purchase cycle

Number of Sales Per Purchase Cycle:
  - Number of times customer buys during the purchase cycle

Cost Per Acquisition:
  - (Cost of marketing and sales)/ number of new leads

Expected Retention Time:
  - Amount of time (measured in purchasing cycles) you expect to retain the customer.

Average Sale Revenue:
  - (Total customer revenue/ Number of purchases in the cycle) OR Average revenue received from the customer per transaction during the cycle

Profit Margin Per Customer:
  - ((Average Sale - Average Cost of Sale) / Average Sale)

Lifetime Value (LTV) = Average Sale⋅Number of Repeat Sales ⋅Expected Retention Time / Average Sale
'''
def lifetime_value():
  purchase_cycle = get_positive_integer_input('Enter purchase cycle/frequency: ')
  total_sales_revenue_cycle = get_positive_float_input('Enter total revenue per cycle: ')
  num_of_sales_cycle = get_positive_integer_input('Enter amount of purchases made per cycle: ')
  cpa = get_positive_float_input('Enter amount of Cost Per Acquisition: ')
  expected_retention = get_positive_float_input('Enter estimated expected retention time: ')

  weeks = 52 / purchase_cycle
  total_sales_revenue_cycle *= num_of_sales_cycle
  avg_sale = total_sales_revenue_cycle / num_of_sales_cycle
  expected_retention *= weeks
  profit_margin = (avg_sale - cpa) / avg_sale
  lt_value = round(avg_sale * num_of_sales_cycle * expected_retention * profit_margin)
  return lt_value

print(f'Answer the following to calculate the Lifetime Value:')
LTV = lifetime_value()
print(f'Lifetime value: ${LTV}')
print('-'*80)
