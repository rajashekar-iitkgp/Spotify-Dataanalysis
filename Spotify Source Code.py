#This is my first ever project in Data analysis. This is a Exploratory data analysis project guided by Simplify.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_tracks = pd.read_csv("NAME.csv")
df_tracks.head()

#null values
pd.isnull(df_tracks).sum()

df_tracks.info()

sorted_df=df_tracks.sort_values('popularity', ascending = True).head(10)
sorted_df

df_tracks.describe().transpose()

most_popular = df_tracks.query('popularity>90', inplace = False).sort_values('popularity', ascending = False)
most_popular[:10]

df_tracks.set_index("release_date", inplace=True)
df_tracks.index=pd.to_datetime(df_tracks.index)
df_tracks.head()

df_cks[[artists]].iloc[18]

df_tracks["duration"]=df_tracks["duration_ms"].apply(lambda x: round(x/1000))
df_tracks.drop("duration_ms", inplace=True, axis=1)

df_tracks.duration.head()

corr_df=df_tracks.drop(["key", "mode", "explicit"],axis=1, corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True, fmt=".1g",vmin=-1,vmax=1,center=0,cmap="inferno", linewidths=1, linecolor="Black")
heatmap.set_title("Correlation Heatmap Between Variable")
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)

sample_df = df_tracks.sample(int(0.004*len(df_tracks))

print(len(sample_df))

plt.fiure(figsize=(10,6))
sns.replot(data=sample_df, y = "loudness", x= "energy", color='c').set(title="Loudness VS Energy correlation")

plt.figre(figsize=(10,6))//popularity and acousticness
sns.replot(data=sample_df, y = "loudness", x= "energy", color='c').set(title="Loudness VS Energy correlation")

df_tracks['dates']=df_tracks.index.get_level_values('release_date')
df_trakcs.dates=pd.to_datetime(df_trackd.dates)
years=df_tracks.dates.dt.year

#pip install --user seabron==0.11.0

sns.displot(years,discrete=True, aspect=2, height=5, kind="hist").set(title"Number of songs per year")

total_dr=df_trakcs.duration
fi_dims=(18,7)
fi, ax =plt.subplots(figsize=fig_dims)
fig = sns.barplot(x=years, y = total_dr, ax= ax, errwidth=False).set(title="year Vs Duration")
plt.xticks(rotation=90)

total_dr = df_trakcs.duration
sns.set_style(style="whitegrid")
fi_dims=(10,5)
fig, ax = plt.subplots(figsize=fi_dims)
fi=sns.lineplot(x=years, y=total_dr, ax=ax).set(title="Year VS Duration")
plt.xticks(rotation=60)

df_genre=pd.read_csv("NAME.CSV")

df_genre.head()

plt.title("Duration of the songs in Different Genres")
sns.color_palette("rocket",as_cmap=True)
sns.barplot(y="genre", x= "duration_ms",data=df_genre)
plt.xlabel("Duration in milli secponds")
plt.ylaber("Genres")

sns.set_style(style = "darkgrid")
plt.figure(figsize = (10,5))
famous = df_genre.sort_values("popularity", scending = False).head(10)
sns.barplot(y="genre", x= "popularity', data=famous).set(title="Top 5 Genres by Popularity")

