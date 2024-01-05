import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  average_age_men = (df.loc[df['sex'] == "Male",
                            ["age", "sex"]])['age'].mean().round(decimals=1)

  # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = round(
    (len(df.loc[df['education'] == "Bachelors", ['education']]) / len(df)) *
    100, 1)

  # What percentage of people 
    #   with advanced education (`Bachelors`, `Masters`, or `Doctorate`) 
    #   make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
 
  higher = ['Bachelors', 'Masters', 'Doctorate']
  df50h  = df['education'].isin(higher)
  df50ks = df['salary'] == ">50K"

  #higher_education = len(df50h)
  #lower_education  = len(df50ks) - len(df50h)

  higher_education_rich = round((df50h & df50ks).sum() / df50h.sum() * 100, 1)
  lower_education_rich  = round((~df50h & df50ks).sum() / (~df50h).sum() * 100, 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()
 

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

  q1 = df['hours-per-week'] == min_work_hours
  q2 = df['salary'] == '>50K'

  #print (len(q1) , len(q2) )


  dfMinHr = df['hours-per-week'] == min_work_hours
  df50ks  = df['salary'] == ">50K"
  rich_percentage = round((dfMinHr & df50ks).sum() / dfMinHr.sum() * 100, 1)

  df50k = df.loc[df['salary'] == ">50K"]
  df50kminh = df50k.loc[df50k['hours-per-week'] <= 40,
                        ['hours-per-week', 'salary']]

  num_min_workers = len(df50kminh)



  # What country has the highest percentage of people that earn >50K?
  df50k = df.loc[df['salary'] == ">50K"]
  df50khc = df50k['native-country'].value_counts()
  dfhc = df['native-country'].value_counts()
  dfPercent = df50khc / dfhc
  hPercent = dfPercent.max().round(decimals=3) * 100
  idx = dfPercent.idxmax()
  dfPercent.loc[idx]

  highest_earning_country = idx
  highest_earning_country_percentage = hPercent

  # Identify the most popular occupation for those who earn >50K in India.
  df50ks = df['salary'] == ">50K"
  dfIndia = df['native-country'] == "India"

  # import re
  # top_IN_occupation = re.sub(r',(?=\))', '', str(oID50kImax))
  # top_IN_occupation = oID50kImax
  # DO NOT MODIFY BELOW THIS LINE

  top_IN_occupation = df[ dfIndia & df50ks ] \
                          ['occupation'].value_counts().index[0]

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich': higher_education_rich,
    'lower_education_rich': lower_education_rich,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }
