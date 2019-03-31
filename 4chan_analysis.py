import pandas as pd
import matplotlib.pyplot as plti

df = pd.read_json(open('overall_analysis.json', 'r'))

df.set_index('date', inplace=True)

plt.style.use('seaborn-darkgrid')

fig, ax = plt.subplots(figsize=(20, 10))

ax.bar(df.index, df['overall_sentiment'], color='#5DAF83')

ax.set_ylabel = 'Sentiment'

plt.yticks(fontsize='x-large')
plt.xticks(rotation=60, ha='right', fontsize='x-large', rotation_mode='anchor')

plt.title('4chan Overall Sentiment Value', fontsize='xx-large')
plt.show()
