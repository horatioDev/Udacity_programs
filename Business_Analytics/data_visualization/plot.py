import matplotlib.pyplot as plt
import numpy as np


# Sample
# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

# Demo Bar Chart
def demo_bar_chart():
  # Sample data for the bar chart
  categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
  values = [10, 15, 7, 12]

  # Create Bar Chart
  plt.bar(categories, values)

  # Add labels and a title
  plt.xlabel('Categories')
  plt.ylabel('Values')
  plt.title('Simple Bar Chart')

  plt.show()


# Demo Line Chart
def line_chart(x,y):
  # Create a line chart
  plt.plot(x, y)

  # Show the chart
  return plt.show()

# Sample data
# x = [1, 2, 3, 4, 5]
# y = [10, 12, 5, 8, 6]
# line_chart(x,y)

# Line Chart - Title, axis labels
def labeled_line_chart(x,y):
  # Sample data
  fig, ax = plt.subplots() # Create a figure containing a single axes.
  ax.set_title('Line Chart') # Add a title to the axes.
  ax.set_xlabel('Variable X') # Add an x-label to the axes.
  ax.set_ylabel('Variable Y')  # Add a y-label to the axes.
  ax.plot(x, y) # Plot some data on the axes.

  plt.show()

# Demo Histogram