
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = '/mnt/data/natural_disasters.csv'
natural_disasters_data = pd.read_csv(file_path)

# Rename the last column
natural_disasters_data.rename(columns={'Disasters.1': 'Number_of_Events'}, inplace=True)

# Summary statistics
summary_stats = natural_disasters_data.describe()
missing_values = natural_disasters_data.isnull().sum()

# Distribution of the number of events
plt.figure(figsize=(10, 6))
plt.hist(natural_disasters_data['Number_of_Events'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Number of Events')
plt.xlabel('Number of Events')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Trend of natural disasters over the years
sorted_data = natural_disasters_data.sort_values(by='Year')
plt.figure(figsize=(12, 6))
plt.plot(sorted_data['Year'], sorted_data['Number_of_Events'], color='blue')
plt.title('Trend of Natural Disasters Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Events')
plt.grid(True)
plt.show()

# Trend of natural disasters over the years with a trend line
x = sorted_data['Year']
y = sorted_data['Number_of_Events']
coefficients = np.polyfit(x, y, deg=1)
trend_line = np.poly1d(coefficients)

plt.figure(figsize=(12, 6))
plt.plot(sorted_data['Year'], sorted_data['Number_of_Events'], color='blue', label='Number of Events')
plt.plot(sorted_data['Year'], trend_line(sorted_data['Year']), color='red', linestyle='--', label='Trend Line')
plt.title('Trend of Natural Disasters Over the Years (With Trend Line)')
plt.xlabel('Year')
plt.ylabel('Number of Events')
plt.legend()
plt.grid(True)
plt.show()

# Number of events per year
events_per_year = natural_disasters_data.groupby('Year')['Number_of_Events'].sum()
plt.figure(figsize=(12, 6))
plt.plot(events_per_year.index, events_per_year.values, color='blue', label='Total Number of Events')
plt.title('Total Number of Natural Disaster Events Per Year')
plt.xlabel('Year')
plt.ylabel('Total Number of Events')
plt.legend()
plt.grid(True)
plt.show()

# Average number of events per year
average_events_per_year = natural_disasters_data.groupby('Year')['Number_of_Events'].mean()
plt.figure(figsize=(12, 6))
plt.plot(average_events_per_year.index, average_events_per_year.values, color='green', label='Average Number of Events')
plt.title('Average Number of Natural Disaster Events Per Year')
plt.xlabel('Year')
plt.ylabel('Average Number of Events')
plt.legend()
plt.grid(True)
plt.show()

# Median number of events per year
median_events_per_year = natural_disasters_data.groupby('Year')['Number_of_Events'].median()
plt.figure(figsize=(12, 6))
plt.plot(median_events_per_year.index, median_events_per_year.values, color='purple', label='Median Number of Events')
plt.title('Median Number of Natural Disaster Events Per Year')
plt.xlabel('Year')
plt.ylabel('Median Number of Events')
plt.legend()
plt.grid(True)
plt.show()

# Average and median number of events per year on the same plot
plt.figure(figsize=(12, 6))
plt.plot(average_events_per_year.index, average_events_per_year.values, color='green', label='Average Number of Events')
plt.plot(median_events_per_year.index, median_events_per_year.values, color='purple', label='Median Number of Events')
plt.title('Average and Median Number of Natural Disaster Events Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Events')
plt.legend()
plt.grid(True)
plt.show()

# Boxplot of number of events by year
plt.figure(figsize=(20, 8))
natural_disasters_data.boxplot(column='Number_of_Events', by='Year', grid=True, figsize=(20, 8))
plt.title('Boxplot of Number of Natural Disaster Events by Year')
plt.xlabel('Year')
plt.ylabel('Number of Events')
plt.suptitle('')
plt.xticks(rotation=90)
plt.show()

# Types of disasters
unique_disasters = natural_disasters_data['Disasters'].unique()

# Bar plot of rate of change for each event type
natural_disasters_data['Yearly_Change'] = natural_disasters_data.groupby('Disasters')['Number_of_Events'].diff()
event_type_change = natural_disasters_data.groupby('Disasters')['Yearly_Change'].sum().fillna(0)
plt.figure(figsize=(14, 8))
plt.bar(event_type_change.index, event_type_change.values, color='skyblue')
plt.title('Total Year-over-Year Change in Number of Natural Disaster Events by Type')
plt.xlabel('Event Type')
plt.ylabel('Total Change in Number of Events')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.show()

# Bar plot of percentage of total events for each disaster type
total_events_per_type = natural_disasters_data.groupby('Disasters')['Number_of_Events'].sum()
percent_total_per_type = (total_events_per_type / total_events_per_type.sum()) * 100
average_percentage = percent_total_per_type.mean()
plt.figure(figsize=(14, 8))
plt.bar(percent_total_per_type.index, percent_total_per_type.values, color='lightcoral', label='Percentage of Total Events')
plt.axhline(y=average_percentage, color='blue', linestyle='--', linewidth=3, label=f'Average ({average_percentage:.2f}%)')
plt.title('Percentage of Total Natural Disaster Events by Type with Average Line')
plt.xlabel('Event Type')
plt.ylabel('Percentage of Total Events (%)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.show()

# Stacked bar chart by year with the events stacked
pivot_data = natural_disasters_data.pivot_table(index='Year', columns='Disasters', values='Number_of_Events', aggfunc='sum', fill_value=0)
last_50_years_data = pivot_data[pivot_data.index >= (pivot_data.index.max() - 50)]
last_50_years_data.plot(kind='bar', stacked=True, figsize=(16, 10), colormap='tab20')
plt.title('Number of Natural Disaster Events by Year (Last 50 Years, Stacked)')
plt.xlabel('Year')
plt.ylabel('Number of Events')
plt.legend(title='Disasters', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()

# Line plot for selected disaster types (Extreme_weather, Flood, Drought)
selected_disasters = ['Extreme_weather', 'Flood', 'Drought']
filtered_data = natural_disasters_data[natural_disasters_data['Disasters'].isin(selected_disasters)]
pivot_selected_data = filtered_data.pivot_table(index='Year', columns='Disasters', values='Number_of_Events', aggfunc='sum', fill_value=0)
plt.figure(figsize=(14, 8))
for disaster in selected_disasters:
    plt.plot(pivot_selected_data.index, pivot_selected_data[disaster], label=disaster)
plt.title('Number of Events for Extreme Weather, Flood, and Drought by Year')
plt.xlabel('Year')
plt.ylabel('Number of Events')
plt.legend(title='Disasters')
plt.grid(True)
plt.show()

# Line plot for the remaining disaster types
remaining_disasters = natural_disasters_data[~natural_disasters_data['Disasters'].isin(selected_disasters)]
remaining_disaster_types = remaining_disasters['Disasters'].unique()
pivot_remaining_data = remaining_disasters.pivot_table(index='Year', columns='Disasters', values='Number_of_Events', aggfunc='sum', fill_value=0)
plt.figure(figsize=(14, 8))
for disaster in remaining_disaster_types:
    plt.plot(pivot_remaining_data.index, pivot_remaining_data[disaster], label=disaster)
plt.title('Number of Events for Remaining Disaster Types by Year')
plt.xlabel('Year')
plt.ylabel('Number of Events')
plt.legend(title='Disasters', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()

# Correlation Analysis
correlation_matrix = pivot_all_data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Natural Disaster Events')
plt.show()

# Display Correlation Analysis in a table
correlation_table = correlation_matrix.reset_index()
correlation_table_melted = correlation_table.melt(id_vars='Disasters', var_name='Compared With', value_name='Correlation Coefficient')
