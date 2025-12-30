# Visualizing the trends of matches played in ODI, TEST and T20 formats
plt.figure(figsize=(15,15))
plt.subplot(3,1,1)
sns.lineplot(data=odi['Year'].value_counts().sort_index(), marker='o', color='black')
plt.title("Trend of ODI matches played by Bangladesh each year", fontsize=14, color='black')

plt.subplot(3,1,2)
sns.lineplot(data=test['Year'].value_counts().sort_index(), marker='o', color='green')
plt.title("Trend of TEST matches played by Bangladesh each year", fontsize=14, color='green')

plt.subplot(3,1,3)
sns.lineplot(data=t20['Year'].value_counts().sort_index(), marker='o', color='blue')
plt.title("Trend of T20 matches played by Bangladesh each year", fontsize=14, color='blue')

plt.show()