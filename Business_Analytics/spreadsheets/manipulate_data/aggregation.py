def sum(data):
  pass

# Notation/Summation for Mean Calculation
'''
We know that the mean is calculated as the sum of all our values divided by the number of values in our dataset.

In our current notation, adding all of our values together can be extremely tedious. If we want to add 3 values of some random variable together, we would use the notation:

x1+x2+x3 

If we want to add 6 values together, we would use the notation:

x1+x2+x3+x4+x5+x6

To extend this to add one hundred, one thousand, or one million values would be ridiculous! How can we make this easier to communicate?!

Summation:

Aggregations
An aggregation is a way to turn multiple numbers into fewer numbers (commonly one number).

Summation is a common aggregation. The notation used to sum our values is a greek symbol called sigma Σ.

Example 1
Imagine we are looking at the amount of time individuals spend on our website. We collect data from nine individuals:

x1=10, x2=20, x3=45, x4=12, x5=8,x6=12, x7=3, x8=68,x9=5

If we want to sum the first three values together in our previous notation, we write:

x1+x2+x3 

In our new notation, we can write:
 .

Notice, our notation starts at the first observation (

summation:
i=1, start=i, end=len(dataset)-1, stop=x-1

i=1) and ends at 3 (the number at the top of our summation).

So all of the following are equal to one another:

summation = x1+x2+x3 = 10 + 20 + 45 = 75
summation = i=1, x=3, start=i, end=len(dataset)-1, stop=x-1

Example 2
Now, imagine we want to sum the last three values together.

x7+x8+x9x

In our new notation, we can write:

summation = x1+x2+x3 = 3 + 68 + 5 = 76
summation = i=1, x=3, start=i, end=len(dataset)-1, stop=x-1

Notice, our notation starts at the seventh observation (i=7) and ends at 9 (the number at the top of our summation).
'''
def summation(dataset, i, n):
  dsSize = len(dataset)
  dataMean = 0
  dataSum = 0
  num=1
  start = i
  end = n

  if(end>dsSize or start<1):
    try:
      raise Exception("Invalid Entry: Check start or end input")
    except Exception as e:
      dataMean = e
  else:
    log = 0
    firstObservation = dataset[start - num]
    lastObservation = dataset[end - num]
    observations = range(start - num, end)
    
    for obs in observations:
      log += 1
      observation = dataset[obs]
      dataSum += observation
      dataMean = round(dataSum/dsSize, 1)
    
      observationData = f'Log: {log} | Start: {start} | End: {end} | Data Size: {dsSize} | Observations: First: {firstObservation} | Last: {lastObservation} | Summation: {dataSum} | Mean: {dataMean}'
    # print(observationData)
  
  summationData = [dataSum, dataMean]
  return summationData
# summationOfData = summation(dataset, i=2, n=7)
# print(f'Summation | Mean: {summationOfData}')