# Cite: Function descriptive text is from Udacity Nanodegree Business Analytics course ...

# dataInput = input('Please insert data: ex: 1,2,3: ')
# dataset = list(map(int, dataInput.split(",")))
# datasetSize = len(dataset)
# print(f'Data: {dataset} Data Size: {datasetSize}')

# dataset =[4,2,5,3,6,1,4] #lsk
# dataset =[4,2,2,1,3,2,3] #rsk
# dataset =[4,3,4,3,4,6,4] #ssk
# dataset =[57,57,57,58,63,66,66,67,67,68,69,70,70,70,70,72,73,75,75,76,76,78,79,81] #lsk/no-outliers
# dataset =[52,57,57,58,63,66,66,67,67,68,69,70,70,70,70,72,73,75,75,76,76,78,79,89] #lsk/outliers l:52 h:89
dataset = [1.5,2.3,2,3,4,5,6,7,0.8,9]
datasetSize = len(dataset)
# print(f'Data: {dataset} Data Size: {datasetSize}')

# Data Types
'''
Quantitative data takes on numeric values that allow us to perform mathematical operations

Data Types		
  Quantitative:
    Continuous - Height, Age, Income
    Discrete - Pages in a Book, Trees in Yard, Dogs at a Coffee Shop
  
  Categorical:
    Ordinal - Letter Grade, Survey Rating
    Nominal - Gender, Marital Status, Breakfast Items

Quantitative variables as either continuous or discrete. 
  Continuous data can be split into smaller and smaller units, and still a smaller unit exists. An example of this is the age of the dog - we can measure the units of the age in years, months, days, hours, seconds, but there are still smaller units that could be associated with the age.

  Discrete data only takes on countable values. The number of dogs we interact with is an example of a discrete data type.

Four main aspects used to describe quantitative variables:

Measures of Center
Measures of Spread
Shape of the Distribution
Outliers
'''
def data_types(dataset): 
  quantDataType  = 'Quantitative'
  continuousData = 'Continuous'
  contCt = 0
  discreteData = 'Discrete'
  discCt = 0
  categoricalDataType  = 'Categorical'
  nominalData ='Ordinal'
  ordinalData ='Nominal'
  dataType = ''

  for pt in dataset:
    if all(isinstance(pt, int) for pt in dataset):
      dataType = f'{discreteData}'
      # return 'Discrete'
      return dataType
    elif all(isinstance(pt, float) for pt in dataset):
      dataType = f'{continuousData}'
        # return 'Continuous'
      return dataType
    elif all(isinstance(pt, str) for pt in dataset):
      dataType = f'{categoricalDataType}'
        # return 'Categorical'
      return dataType
    else:
      dataType = f'{quantDataType} - Mixed'
      return dataType

  return dataType
typeOfData = data_types(dataset)
# print(f'Data Type: {typeOfData}')



# Frequency distribution
def frequency(dataset):
  frequencyDict = dict()
  # Create frequency dictionary
  for value in dataset:
    if value not in frequencyDict:
      frequencyDict[value] = 1
    else:
      frequencyDict[value] += 1

  return frequencyDict
dataFrequency = frequency(dataset)
# print(f'Frequency Dist.: {dataFrequency}')
# print('-'*60)
# -----------------------------------------------------------------------------

# Get the Mean
'''
The mean is often called the average or the expected value in mathematics. We calculate the mean by adding all of our values together and dividing by the number of values in our dataset.
'''
def mean(dataset):
  total = sum(dataset)
  datasetSize = len(dataset)
  mean = round(total/datasetSize)
  return mean
meanOfData = mean(dataset)
# print(f'Mean: {meanOfData}')

# Get the Median
'''
The median splits our data so that 50% of our values are lower and 50% are higher.

How we calculate the median depends on if we have an even number of observations or an odd number of observations.

Median for Odd Values
If we have an odd number of observations, the median is simply the number in the direct middle.

Median for Even Values
If we have an even number of observations, the median is the average of the two values in the middle.

Note: Whether we use the mean or median to describe a dataset is largely dependent on the shape of our dataset and if there are any outliers. 
'''
def median(dataset):
  sortedData = sorted(dataset)
  firstHalf = sortedData[:round(datasetSize/2)]
  secondHalf = sortedData[round(datasetSize/2):]
  if datasetSize % 2 == 0:
    pt1 = firstHalf[-1]
    pt2 = secondHalf[0]
    total = pt1 + pt2
    median = total / 2 
  else:
    median = sortedData[int(datasetSize/2)]
  return median
medianOfData = median(dataset)
# print(f'Median: {medianOfData}')

# Get the Mode
'''
The Mode
The mode is the most frequently observed value in our dataset.

There might be multiple modes for a particular dataset or no mode at all.

No Mode
If all observations in our dataset are observed with the same frequency, there is no mode. If we have the dataset:

1, 1, 2, 2, 3, 3, 4, 4

There is no mode because all observations occur the same number of times.

If two (or more) numbers share the maximum value, then there is more than one mode. If we have the dataset:

1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9
'''
def mode(dataset):
  dataset.sort()
  maxFrequency = dataset.count(dataset[0])
  modes = set()
  modeData = None
  
  # Get maximum frequency
  for pt in dataset:
    currentMax = dataset.count(pt) 
    # Get Max count
    if currentMax > maxFrequency:
      maxFrequency = currentMax
    # Get Mode(s)
  for pt in dataset:
    if (dataset.count(pt) == maxFrequency):
      modes.add(pt)
      modeData = modes
      # Check if same values/No Mode
      if (dataset.count(pt) == currentMax) and (currentMax == maxFrequency):
        modes.remove(pt)
        modeData = None 
  return modeData
modeOfData = mode(dataset)
# print(f'Mode: {modeOfData}')
# print('-'*60)

# Measure of Center
'''
Means
Medians
Modes
'''
def measure_of_center(dataset):
  m1 = meanOfData
  m2 = medianOfData
  m3 = modeOfData
  center = [m1, m2, m3]
  return center
measureOfCenter = measure_of_center(dataset)
# print(f'Measure of Center: {measureOfCenter}')
# print('-'*60)
# -----------------------------------------------------------------------------

# Get Range
def data_range(dataset):
  dataset.sort()
  minVal = int(min(dataset))
  maxVal = int(max(dataset))
  rangeValue = maxVal - minVal
  return rangeValue
rangeOfData = data_range(dataset)
# print(f'Range: {rangeOfData}')

# Get Interquartile  Range
def quartile_range(dataset):
  dataset.sort()
  # Get Minimum / Maximum
  minimum = int(min(dataset))
  maximum = int(max(dataset))
  global q1 
  q1 = 0
  global q2
  q2 = median(dataset)
  global q3
  q3 = 0
  firstHalf = dataset[:round(datasetSize/2)]
  secondHalf = dataset[round(datasetSize/2):]
  oddHalves = len(firstHalf) != len(secondHalf)
  bigFirstHalf = len(firstHalf) > len(secondHalf)
  bigSecondHalf = len(firstHalf) < len(secondHalf)

  # Get Range: the difference between the maximum and the minimum
  spreadRange = rangeOfData

  if oddHalves:
    if bigFirstHalf:
      fh = firstHalf[:-1]
      firstHalf = fh
      if len(firstHalf) % 2 == 0:
        fh_dataset = firstHalf
        fh = fh_dataset[:round(len(fh_dataset)/2)]
        sh = fh_dataset[round(len(fh_dataset)/2):]
        pt1 = fh[-1]
        pt2 = sh[0]
      else:
        q1 = firstHalf[int(len(firstHalf)/2)]
        q3 = secondHalf[int(len(secondHalf)/2)]
    elif bigSecondHalf:
      sh = secondHalf[1:]
      secondHalf = sh
      
      if len(secondHalf) % 2 == 0:
        # Second Half: 1st set
        fh_dataset = firstHalf
        fh1 = fh_dataset[:round(len(fh_dataset)/2)]
        sh1 = fh_dataset[round(len(fh_dataset)/2):]
        pt1 =fh1[-1]
        pt2 = sh1[0]
        fh_sum = pt1 + pt2
        q1 = fh_sum/2

        # Second Half: 2nd set
        sh_dataset = secondHalf
        fh2 = sh_dataset[:round(len(sh_dataset)/2)]
        sh2 = sh_dataset[round(len(sh_dataset)/2):]
        pt3 = fh2[-1]
        pt4 = sh2[0]
        sh_sum = pt3 + pt4
        q3 = sh_sum/2
        
    else:
      q1 = firstHalf[int(len(firstHalf)/2)]
      q3 = sh_dataset[int(len(secondHalf)/2)]
      # print(f'q3: {q3}')

  if not oddHalves and datasetSize % 2 == 0:
    # fh = firstHalf[:-1]
    # sh = secondHalf[1:]
    # firstHalf, secondHalf = fh, sh
    # print(f'fh:{fh} sh: {sh}')
    if len(firstHalf) and len(secondHalf) % 2 == 0:
      # First Half
      fh_dataset = firstHalf
      fh1 = fh_dataset[:round(len(fh_dataset)/2)]
      sh1 = fh_dataset[round(len(fh_dataset)/2):]
      pt1 =fh1[-1]
      pt2 = sh1[0]
      fh_sum = pt1 + pt2
      q1 = fh_sum/2

      # Second Half
      sh_dataset = secondHalf
      fh2 = sh_dataset[:round(len(sh_dataset)/2)]
      sh2 = sh_dataset[round(len(sh_dataset)/2):]
      pt3 = fh2[-1]
      pt4 = sh2[0]
      sh_sum = pt3 + pt4
      q3 = sh_sum/2

      # print(len(fh), len(sh), len(fh) and len(sh) % 2 == 0, len(firstHalf), len(secondHalf), len(firstHalf) and len(secondHalf) % 2 == 0 )
    else:
      q1 = firstHalf[int(len(firstHalf)/2)]
      q3 = secondHalf[int(len(secondHalf)/2)]

  # Inter-quartile Range
  iqr = q3 - q1

  summaryOfData = f'Min:{minimum}|Q1:{q1}|Q2:{q2}|Q3:{q3}|Max:{maximum}|Range:{spreadRange}|IQR:{float(iqr)}'
  five_number_summary = [minimum, q1, q2, q3, maximum, iqr]
  # print(f'Five Number Summary: {summaryOfData}')

  return five_number_summary
quartileRangeOfData = quartile_range(dataset)
# print(f'Interquartile: {quartileRangeOfData}')

# Get variance and standard deviation
'''
The standard deviation is one of the most common measures for talking about the spread of data. It is defined as the average distance of each observation from the mean.

Standard deviation is a common metric used to compare the spread of two datasets. The benefits of using a single metric instead of the 5 number summary are:

It simplifies the amount of information needed to give a measure of spread
It is useful for inferential statistics

Important Final Points
The variance is used to compare the spread of two different groups. A set of data with higher variance is more spread out than a dataset with lower variance. Be careful though, there might just be an outlier (or outliers) that is increasing the variance when most of the data are actually very close.

**When comparing the spread between two datasets, the units of each must be the same.*

When data are related to money or the economy, higher variance (or standard deviation) is associated with higher risk.

The standard deviation is used more often in practice than the variance because it shares the units of the original dataset.

**HIGHER STANDARD DEVIATION IS ASSOCIATED w/ HIGHER RISK**
'''
# Get StandardDeviation
def standard_deviation(dataset, mean):
    datasetSize = len(dataset)
    variance = 0

    for pt in dataset:
        diff_from_mean = round((pt - mean) ** 2, 2)
        variance += diff_from_mean

    variance /= datasetSize - 1  # Corrected the denominator
    stdDev = round(variance ** 0.5, 2)
    return stdDev

meanOfData = mean(dataset)
deviationOfData = standard_deviation(dataset, meanOfData)
# print(f'Standard Deviation: {deviationOfData}')

# Get Variance
def data_variance(dataset):
  # Get mean
  std_mean = meanOfData
  varianceTotal = 0
  
  # Calculate distance from each observation and square the results
  for pt in dataset:
    diff_from_mean = round((pt - std_mean) ** 2, 2)
    varianceTotal += float(diff_from_mean / datasetSize)
  return round(varianceTotal, 1)
varianceOfData = data_variance(dataset)
# print(f'Variance: {varianceOfData}')
# print('-'*60)

# Measures of Spread
'''
5 Number Summary
  For datasets that are not symmetric, the five-number summary and a corresponding box plot are a great way to get started with understanding the spread of your data.

Variance and Standard Deviation
  Two additional measures of spread that are used all the time are the variance and standard deviation.

  The variance is calculated by taking the average squared difference from each data point in the dataset (x-bar). The square root of this value gives you.


'''
# Get the Spread
def measure_of_spread(dataset):
  # rangeData = rangeOfData
  qRange = quartileRangeOfData
  stdDev = deviationOfData
  variance = varianceOfData
  deviation = [stdDev, variance]
  spread = qRange
  spread.append(deviation)

  spreadSummary = f'Min:{spread[0]} | Q1:{spread[1]} | Q2:{spread[2]} | Q3:{spread[3]} | Max:{spread[4]} | IQR:{spread[5]} | Deviation:{stdDev} | Variance:{variance}'
  # print(f'Summary: {spreadSummary}')

  spreadData = spread
  return spreadData 
spreadOfData = measure_of_spread(dataset)
# print(f'Measure of Spread: {spreadOfData}')
# print('-'*60)

# -----------------------------------------------------------------------------

# Shape
'''
We learned that the distribution of our data is frequently associated with one of the three shapes:

1. Right-skewed
    Shape |	Mean vs. Median	| Real-World Applications
    Right-skewed | Mean greater than Median | Amount of drug remaining in a bloodstream, Time between phone calls at a call center, Time until light bulb dies, Distribution of Wealth, Athletic Abilities
2. Left-skewed
    Shape |	Mean vs. Median	| Real-World Applications
    Left-skewed |	Mean less than Median |	Grades as a percentage in many universities, Age of death, Asset price changes
3. Symmetric (frequently normally distributed)
    Shape |	Mean vs. Median	| Real-World Applications
    Symmetric (Normal) | Mean equals Median |	Height, Weight, Errors, Precipitation, Scores
'''
def shape(dataset):
  shapeMean = float(round(meanOfData, 1))
  shapeMedian = float(round(medianOfData, 1))
  shapeMode = modeOfData
  isLeftSkew = (shapeMean < shapeMedian)
  isRightSkew = (shapeMean > shapeMedian)
  isSymmetricSkew = (shapeMean == shapeMedian)
  shapeData = ''
  lSkApp = 'Left-skewed: | Applications: Age, Income, BMI, Heart Rate, Temperature, Cholesterol, Glucose Level'
  sSkApp = 'Symmetric(Normal): | Applications: Height, Weight, Errors, Precipitation'
  rSkApp ='Right-skewed: | Applications: Fat Mass Index, Body Mass Index, Pulse Pressure, Respiratory Rate, Skin Thickness, Length of Stay in Hospital, Number of Prescriptions per day, Total Cost, Number Of Children, Fuel Consumption Per City Mile, Population Density'

  if(isLeftSkew):
    shape = 'Left-Skewed'
    shapeData = f'{lSkApp}'
  elif(isRightSkew):
    shape = 'Right-Skewed'
    shapeData = f'{rSkApp}'
  else:
    shape = 'Symmetrical(Normal)'
    shapeData = f'{sSkApp}'
  
  # print(shapeData)
  return shape
shapeOfData = shape(dataset)
# print(f'Shape: {shapeOfData}')
# -----------------------------------------------------------------------------

# Outliers
'''
We learned that outliers are points that fall very far from the rest of our data points. This influences measures like the mean and standard deviation much more than measures associated with the five-number summary.

Common Techniques
When outliers are present we should consider the following points.
  1. Noting they exist and the impact on summary statistics.
  2. If typo - remove or fix
  3. Understanding why they exist, and the impact on questions we are trying to answer about our data.
  4. Reporting the 5 number summary values is often a better indication than measures like the mean and standard deviation when we have outliers.
  5. Be careful in reporting. Know how to ask the right questions.

Outliers Advice
Below are my guidelines for working with any column (random variable) in your dataset.
  1. Plot your data to identify if you have outliers.
  2. Handle outliers accordingly via the previous methods.
  3. If no outliers and your data follow a normal distribution - use the mean and standard deviation to describe your dataset, and report that the data are normally distributed.

How to Find Outliers in a Data Set
  Sample Data (n=10) // length of dataset
  27, 2, 22, 29, 19, 30, 32, 59, 52, 35


Step 1:
  Arrange the data in order from smallest to largest.

  2, 19, 22, 27, 29, 30, 32, 35, 52, 59

Step 2
  Find the first quartile, Q1.

  To find Q1, multiply 25/100 by the total number of data points (n). This will give you a locator value, L. If L is a whole number, take the average of the Lth value of the data set and the (L+1)th value. The average will be the first quartile. If L is not a whole number, round L up to the nearest whole number and find the corresponding value in the data set. That will be the first quartile.

  L = (25/100)(n)= (0.25)(10) = 2.5
  **2.5 is not a whole number, so round up the nearest whole number to get 3. The 3rd value in the data set is 22. Q1 = 22
  
​​Step 3:
  Find the third quartile, Q3.

  To find Q3, use the same method used to find Q1, except this time, multiply 75/100 by n to get the locator value, L.

  L = (75.100)(n) = (0.75)(10) = 7.5
  **7.5 is not a whole number, so round up the nearest whole number to get 8. The 8th value in the data set is 35. Q3 = 35

Step 4:
  Find the interquartile range, IQR.

  Remember, the interquartile range is the difference between Q3 and Q1.

  IQR = Q3 - Q1 = 35 - 22 = 13

Step 5:
  Find the upper boundary.

  Upper boundary = Q3 + 1.5 IQR = 35 + (1.5)(13) = 54.5
Step 6:
  Find the lower boundary.

  Lower boundary = Q1 - 1.5 IQR = 22 - (1.5)(13) = 2.5

Step 7:
  Identify the outliers.

  The outliers are any data points that lie above the upper boundary or below the lower boundary. In this case, the outliers are 2 and 59.
'''

# Find Outliers
def find_outliers(dataset, q1, q3):
  # Find IQR
  outLierQ1 = q1
  outLierQ2 = q2
  outLierQ3 = q3
  iqr = round(q3 - q1)
  num = 1.5
  lowerOutliers = list()
  upperOutliers = list()
  outliers = [lowerOutliers, upperOutliers]

  # Get upper / lower fence
  global lowerLimit
  lowerLimit = outLierQ1 - (1.5 * iqr)
  global upperLimit
  upperLimit = outLierQ3 + (1.5 * iqr)
   
  for pt in dataset:
    dataPoint = float(pt)
    # print('dp', dataPoint, pt, lowerLimit, upperLimit)
    if(dataPoint < lowerLimit):
      lowerOutliers.append(dataPoint)
    elif (dataPoint > upperLimit):
      upperOutliers.append(dataPoint)
    else:
      pass

  outlierBoundaries = f'Low: {lowerLimit}, High: {upperLimit}'
  # print(f'Fences: {outlierBoundaries}')
  
  return outliers
outliersData = find_outliers(dataset, q1, q3)
# print(f'Outliers: {outliersData}')

# Box Plots
'''
Box plots are useful for quickly comparing the spread of two data sets across some key metrics, like quartiles, maximum, and minimum.

How do we create the box plot?
  The beginning of the line to the left of the box and the end of the line to the right of the box represent the minimum and maximum values in a dataset.
  
  The visual distance between these markings is an indication of the range of the values.
  
  The box itself represents the IQR. The box begins at the Q1 value, ends at the Q3 value, and Q2, or the median, is represented by a line within the box.

However, instead of depending on a visual of the 5 number summary to compare our data, in the next lesson, we will learn about using a single value to compare the two distribution spreads - standard deviation
'''

# Get Bin and Bin width
def bins(dataset, lowerLimit, upperLimit):
    # Count the number of data points / Number of bins
    countDataPoints = len(dataset)
    binCount = round(countDataPoints**(0.5))
  
    # Upper / Lower Specification Limit
    usl = upperLimit
    lsl = lowerLimit

    # Find minimum / maximum value from the set
    minValue = min(dataset)
    maxValue = max(dataset)
    binMin = round(minValue)
    binMax = round(maxValue)

    # Range / Tolerance
    dataRange = maxValue - minValue 
    dataTolerance = round(usl - lsl, 2)
  
    # Tolerance / Bin width
    binSize = dataRange / binCount
    tolerance = round((dataTolerance / binCount), 1)

    # Choose bin size / boundaries
    binBoundaries = []
  
    # Choose bin size
    if minValue == int(minValue) and maxValue == int(maxValue):
        binSize = round(dataRange / binCount)
        for bin in range(binCount):
            boundary = [int((bin * binSize) + 1), int(((bin + 1) * binSize))]
            binBoundaries.append(boundary)
    else:
        maxValue = binMax
        minValue = binMin
        binSize = round(dataRange / binCount)

        for bin in range(binCount):
            boundary = [int((bin * binSize) + 1), int(((bin + 1) * binSize))]
            binBoundaries.append(boundary)

    binSpecs = f'Bins: {binCount} | Size: {binSize} | Min: {minValue} | Max: {maxValue} | Range: {dataRange} | Data Pts: {countDataPoints} | LSL: {lsl} - USL: {usl} | Tol: {tolerance} | Boundaries: {binBoundaries}'
    # print(binSpecs)

    return binCount, binSize, binBoundaries
binData = bins(dataset, lowerLimit, upperLimit)
# print(f'Bin: {binData}')

# Extract bin boundaries from binData
bin_boundaries = binData[2]

# Convert bin boundaries to tuples
bin_boundaries_tuples = [tuple(bin_boundary) for bin_boundary in bin_boundaries]

def count_values_in_bins(dataset, bin_boundaries):
    bin_counts = {bin_boundary: 0 for bin_boundary in bin_boundaries}
    
    for value in dataset:
        for bin_boundary in bin_boundaries:
            lower_boundary, upper_boundary = bin_boundary
            if lower_boundary <= value <= upper_boundary:
                bin_counts[bin_boundary] += 1
                break  # Once a bin is found, move to the next value
                
    return bin_counts

bin_counts = count_values_in_bins(dataset, bin_boundaries_tuples)

for bin_boundary, count in bin_counts.items():
    lower_boundary, upper_boundary = bin_boundary
    # print(f'Bin {lower_boundary}-{upper_boundary}: Count = {count}')

# print('-'*60)
# Get Z-score
def z_score(dataset, eval):
  obs = eval
  zMean = meanOfData 
  stdDev = deviationOfData
  zScore = (obs - zMean)/stdDev
  return zScore
zScoreData = z_score(dataset, eval=1.5)
# print(f'Z-Score: {zScoreData}')
# print('-'*60)


# Quantitative Data Analysis
def quantitativeAnalysis(dataset):
  quantCenter = measureOfCenter
  quantSpread = spreadOfData
  quantShape = shapeOfData
  quantOutliers = outliersData
  qData = f' Measure of Center: {quantCenter} \n Measure of Spread: {quantSpread} \n Shape of Dist: {quantShape} \n Outliers: {quantOutliers}'
  # print(qData)

quantitativeData = quantitativeAnalysis(dataset)
# print(f'Quantitative Data: {quantitativeData}')

# -----------------------------------------------------------------------------
# Plotting the data
# -----------------------------------------------------------------------------
if __name__ == "__main__":
  # Calculate the data type (quantitative or categorical)
  typeOfData = data_types(dataset)

  # Calculate the frequency distribution of the dataset
  dataFrequency = frequency(dataset)

  # Calculate the mean of the dataset
  meanOfData = mean(dataset)

  # Calculate the median of the dataset
  medianOfData = median(dataset)

  # Calculate the mode of the dataset
  modeOfData = mode(dataset)

  # Calculate measures of center (mean, median, mode)
  measureOfCenter = measure_of_center(dataset)

  # Calculate the range of the dataset
  rangeOfData = data_range(dataset)

  # Calculate the interquartile range
  quartileRangeOfData = quartile_range(dataset)

  # Calculate the standard deviation
  deviationOfData = standard_deviation(dataset, meanOfData)

  # Calculate the variance
  varianceOfData = data_variance(dataset)

  # Calculate measures of spread (range, IQR, standard deviation, variance)
  spreadOfData = measure_of_spread(dataset)

  # Determine the shape of the dataset (right-skewed, left-skewed, symmetric)
  shapeOfData = shape(dataset)

  # Identify outliers in the dataset
  outliersData = find_outliers(dataset, q1, q3)

  # Calculate bin data and boundaries for data visualization
  binData = bins(dataset, lowerLimit, upperLimit)

  # Count values within each bin for data visualization
  bin_counts = count_values_in_bins(dataset, bin_boundaries_tuples)

  # Calculate the Z-score for a specific evaluation value
  zScoreData = z_score(dataset, eval=1.5)

  # Perform quantitative data analysis and create a summary
  quantitativeData = quantitativeAnalysis(dataset)

