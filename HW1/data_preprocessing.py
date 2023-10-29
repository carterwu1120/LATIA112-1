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

# 1.2012-2015哪幾個國家有上榜
country = df['country'].unique()  # 不重複提取'country'這一欄
print("Q1:2012-2015哪幾個國家有上榜:", country)

# # 2.2012-2015有幾個國家有上榜
# num_country = df['country'].nunique()   # 不重複計算'country'這一欄國家的個數
# print("Q2:2012-2015有幾個國家有上榜:", num_country)

# # 3.2012-2015年各國學校上榜幾次
# sum_country = df.groupby('country').size().reset_index(name='count')    # 計算同一個國家出現過幾次
# num_bars = len(sum_country)
# random_colors = [plt.cm.viridis(random.random()) for _ in range(num_bars)]  # 隨機賦予顏色
# plt.figure(figsize=(12, 12))  # 圖的大小
# sns.barplot(y='country', x='count', data=sum_country, palette=random_colors)    # 作圖
# plt.ylabel('Country')   # y-axis的標題
# plt.xlabel('Count')     # x-axis的標題
# plt.title('Q3:How many school were on the list from 2012 to 2015')     # 圖的標題
# plt.show()      # 出現圖片
# plt.pause(1)    # 暫停一秒
# plt.close()     # 關閉圖片

# # 4.2012-2015上榜最多間的國家
# maxmum = 0
# for i in sum_country.index:
#     if sum_country['count'][i]>maxmum:
#         maxmum = sum_country['count'][i]
#         max_country = sum_country['country'][i]
# print("Q4:2012-2015上榜最多間的國家:",max_country)

# # 5.2012-2015上榜次數最多的學校
# sum_institution = df.groupby('institution').size().reset_index(name='count')
# maxmum = 0
# for i in sum_institution.index:
#     if sum_institution['count'][i]>maxmum:
#         maxmum = sum_institution['count'][i]
#         max_institution = sum_institution['institution'][i]
# print("Q5:2012-2015上榜次數最多的學校:",max_institution)

# df_2015=df[df['year']==2015]    # 2015的資料

# # 6.2015有哪幾個國家有上榜
# country_2015=df_2015['country'].unique()
# print("Q6:2015有哪幾個國家有上榜:",country_2015)


# # 7.2015年每個國家的最高排名為多少
# rank_2015 = df_2015[['world_rank', "institution", 'country']].copy()
# rank_2015=rank_2015.sort_values(['country','world_rank']).reset_index()     # 以country遞增排序，若country相同，以ranking遞增排序
# new_rank_2015 = pd.DataFrame()
# tmp_country=''
# for idx ,row in rank_2015.iterrows():
#     if(tmp_country!=row['country']):
#         tmp_country=row['country']
#         new_rank_2015 = new_rank_2015.append(row)
# new_rank_2015=new_rank_2015.reset_index()
# num_bars = len(new_rank_2015)
# random_colors = [plt.cm.viridis(random.random()) for _ in range(num_bars)]  # 隨機賦予顏色
# plt.figure(figsize=(12, 12))  # 圖的大小
# sns.barplot(y='country', x='world_rank', data=new_rank_2015, palette=random_colors)    # 作圖
# plt.ylabel('Country')   # y-axis的標題
# plt.xlabel('World_Rank')     # x-axis的標題
# plt.title('Q7:The hightest ranking for each countries at 2015')     # 圖的標題
# plt.show()      # 出現圖片
# plt.pause(1)    # 暫停一秒
# plt.close()     # 關閉圖片
# # print(new_rank_2015[['world_rank', 'country']])

# # 8.2015年每個國家的最高排名的學校
# print("Q8:2015年每個國家的最高排名的學校")
# print(new_rank_2015[['world_rank', 'institution']])

# # 9.2015年各國有幾間上榜
# sum_country = df_2015.groupby('country').size().reset_index(name='count')
# plt.figure(figsize=(12, 12))  # 圖的大小
# sns.barplot(y='country', x='world_rank', data=new_rank_2015, palette=random_colors)    # 作圖
# plt.ylabel('Country')   # y-axis的標題
# plt.xlabel('World_Rank')     # x-axis的標題
# plt.title('Q9:The hightest ranking for each countries at 2015')     # 圖的標題
# plt.show()      # 出現圖片
# plt.pause(1)    # 暫停一秒
# plt.close()     # 關閉圖片
# # print("Q9:2015年各國有幾間上榜")
# # print(sum_country)

# 10.2012-2015 美國的上榜數
listUSA=[]
listyear=[]
df_USA=df[df['country']=="USA"]
for i in range(2012, 2016):
    df_tmp=df_USA[df_USA['year']==i]
    listUSA.append(len(df_tmp))
    listyear.append(i)
plt.figure()  # 圖的大小
plt.suptitle('Q10:The number of rankings in the United States from 2012 to 2015.')
# plt.title("Q10:The number of rankings in the United States from 2012 to 2015.", loc="right")
plt.subplot(121)    # 總共1row 2col的圖上建立第一張圖
plt.pie(listUSA, labels=listyear, autopct='%1.1f%%')    # 作圖
plt.title("The annual percentage for each year from 2012 to 2015.")
plt.subplot(122)    # 建立第二張圖
plt.plot(listyear, listUSA, marker='o', linestyle='-')
for i, j in zip(listyear, listUSA):
    plt.text(i, j, f'{j}', ha='left', va='bottom')  # 在曲線圖的每個點顯示數值
plt.title("The annual growth curve from 2012 to 2015.")

plt.show()      # 出現圖片
plt.pause(1)    # 暫停一秒
plt.close()     # 關閉圖片












