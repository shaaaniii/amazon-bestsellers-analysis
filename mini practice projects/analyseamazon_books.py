import pandas as pd
df = pd.read_csv('bestsellers.csv')

# get the first 5 rows of the dataframe
print(df.head())

#get the shape of the spreadsheet
print(df.shape)

#get the column names of the spreadsheet
print(df.columns)

#get the summary statistics for each of the column
print(df.describe())

#these functions will give overview of the data including
#size, column , summary of each column etc.

# check for duplicate rows 
df.drop_duplicates(inplace=True)
#by setting inplace to true, we are modifying the original dataframe

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#convert the price column to float to make it easier to work with
df['Price'] = df['Price'].astype(float)

# count the number of maximum books by author 
author_Counts = df["Author"].value_counts()
print(author_Counts)


avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

#Export top selling books to a CSV file
author_Counts.head(10).to_csv("top_authors.csv")

#export average rating by genre to a csv file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")