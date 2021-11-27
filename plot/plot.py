import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from datetime import datetime

x = []
y = []

with open('test.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='	')

    # Skip header
    next(plots)

    for row in plots:
        x.append(datetime.fromisoformat(row[1]))
        y.append(float(row[2]))

plt.plot(x, y, color='black', linestyle='solid',
         label="Voltage")

# Major ticks every half year, minor ticks every month,
# plt.gca().get_xaxis().set_major_locator(mdates.HourLocator())
plt.gca().get_xaxis().set_major_locator(mdates.MinuteLocator())
# plt.gca().get_xaxis().set_minor_locator(mdates.SecondLocator())
plt.grid(True)

plt.subplots_adjust(bottom=0.2)
plt.xticks(rotation=25)
# plt.gcf().autofmt_xdate()

plt.xlabel('Time')
plt.ylabel('Voltage AC')
plt.title('AC Voltage in House')
plt.legend()
plt.show()
