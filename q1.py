#dataset : https://www.kaggle.com/datasets/mylesoneill/world-university-rankings/
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import random
data_dir = 'archive'
data_file='cwurData.csv'
dataset_path = os.path.join(data_dir, data_file)
df = pd.read_csv(dataset_path)

# # 1.2012-2015哪幾個國家有上榜
# country = df['country'].unique()
# print("2012-2015哪幾個國家有上榜")
# print(country)

# # 2.2012-2015有幾個國家有上榜
# num_country = df['country'].nunique()
# print("2012-2015有幾個國家有上榜")
# print(num_country)

# 3.2012-2015年各國有幾間上榜
sum_country = df.groupby('country').size().reset_index(name='count')
# print("2012-2015年各國有幾間上榜")
# print(sum_country)

num_bars = len(sum_country)
random_colors = [plt.cm.viridis(random.random()) for _ in range(num_bars)]
plt.figure(figsize=(12, 12))  # Adjust the figure size if needed
sns.barplot(y='country', x='count', data=sum_country, palette=random_colors)
plt.ylabel('Country')
plt.xlabel('Count')
plt.title('How many countries were on the list from 2012 to 2015?')
plt.show()

# # 4.2012-2015上榜最多間的國家
# maxmum = 0
# for i in sum_country.index:
#     if sum_country['count'][i]>maxmum:
#         maxmum = sum_country['count'][i]
#         max_country = sum_country['country'][i]
# print("2012-2015上榜最多間的國家:",max_country)
# print(maxmum)

# # 5.2012-2015上榜次數最多的學校
# sum_institution = df.groupby('institution').size().reset_index(name='count')
# maxmum = 0
# for i in sum_institution.index:
#     if sum_institution['count'][i]>maxmum:
#         maxmum = sum_institution['count'][i]
#         max_institution = sum_institution['institution'][i]
# print("2012-2015上榜次數最多的學校:",max_institution)

df_2015=df[df['year']==2015]

# # 6.2015有哪幾個國家有上榜
# country_2015=df_2015['country'].unique()
# print("2015有哪幾個國家有上榜")
# print(country_2015)

# # 7.2015年每個國家的最高排名為多少
# rank_2015 = df_2015[['world_rank', "institution", 'country']].copy()
# rank_2015=rank_2015.sort_values(['country','world_rank']).reset_index()
# new_rank_2015 = pd.DataFrame()
# tmp_country=''
# for idx ,row in rank_2015.iterrows():
#     if(tmp_country!=row['country']):
#         tmp_country=row['country']
#         new_rank_2015 = new_rank_2015.append(row)
# new_rank_2015=new_rank_2015.reset_index()
# print(new_rank_2015[['world_rank', 'country']])

# # 8.2015年每個國家的最高排名的學校
# print(new_rank_2015[['world_rank', 'institution']])

# # 9.2015年各國有幾間上榜
# sum_country = df_2015.groupby('country').size().reset_index(name='count')
# print("2015年各國有幾間上榜")
# print(sum_country)

# # 10.2015年上榜最多間的國家
# maxmum = 0
# for i in sum_country.index:
#     if sum_country['count'][i]>maxmum:
#         maxmum = sum_country['count'][i]
#         max_country = sum_country['country'][i]
# print("2015上榜最多間的國家:",max_country)
# print(maxmum)






