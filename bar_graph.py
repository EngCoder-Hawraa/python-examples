import matplotlib.pyplot as pyplot
# Set up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5) # provides locations on x axis
sizes = [90, 10, 15, 60, 22]
# Set up the bar chart
pyplot.bar(index, sizes, tick_label=labels)
# Configure the layout
pyplot.ylabel('Usage')
pyplot.xlabel('Programming Languages')
# Display the chart
pyplot.show()