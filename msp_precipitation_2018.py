import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'msp_may_rain_2019.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Take precipitation averages and store them in a list
    precip_averages, dates = [], []
    for row in reader:
        precip = float(row[17])
        date = datetime.strptime(row[0], '%m/%d/%Y')
        precip_averages.append(precip)
        dates.append(date)
        
# Plot the data in a plot
plt.plot(dates, precip_averages)
plt.show()
