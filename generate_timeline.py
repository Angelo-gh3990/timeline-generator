# Define the start date for the project as the 1st of April of the current year
start_date = datetime(datetime.now().year, 4, 1)

# Define the timeline in months, with tasks and their durations
timeline = {
    'Example1': (start_date, start_date + timedelta(days=60)),
    'Example2': (start_date + timedelta(days=30), start_date + timedelta(days=90)),
    'Example3': (start_date + timedelta(days=60), start_date + timedelta(days=120)),
    'Example4': (start_date + timedelta(days=90), start_date + timedelta(days=150)),
    'Example5': (start_date + timedelta(days=120), start_date + timedelta(days=180)),
    'Example6': (start_date + timedelta(days=135), start_date + timedelta(days=195)),
}

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 5))

# List to hold the y-tick labels
labels = []

# Iterate over the tasks and their start/end dates
for i, (task, (start, end)) in enumerate(timeline.items()):
    ax.hlines(y=i, xmin=start, xmax=end, color='blue', linestyles='-', lw=25)  # Draw the timeline for the task
    labels.append(task)  # Append the task to the labels list

# Set the y-ticks to be the tasks
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)

# Format the dates on the x-axis
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# Set some padding so the labels aren't cut off
ax.margins(y=0.1)
ax.grid(True)

# Rotate and align the tick labels so they look better
fig.autofmt_xdate()

# Set the title and show the plot
plt.title('Title Timeline (Start: 1st April)')
plt.show()
