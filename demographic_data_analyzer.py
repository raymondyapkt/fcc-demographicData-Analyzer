import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    q1 = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    q2 = df['salary'] == '>50K'

    higher_education_rich = round((q1 & q2).sum() / q1.sum() * 100, 1)
    lower_education_rich = round((~q1 & q2).sum() / (~q1).sum() * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    q1 = df['hours-per-week'] == min_work_hours

    rich_percentage = round((q1 & q2).sum() / q1.sum() * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    p = (df[q2]['native-country'].value_counts() \
                                / df['native-country'].value_counts() * 100).sort_values(ascending=False)

    highest_earning_country = p.index[0]
    highest_earning_country_percentage = round(p.iloc[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & q2] \
                          ['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
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
  df50k = df.loc[df['salary'] == ">50K"]
  higher = ['Bachelors', 'Masters', 'Doctorate']
  df50h = df50k.loc[df50k['education'].isin(higher)]

  higher_education = len(df50h)
  lower_education = len(df50k) - len(df50h)

  # percentage with salary >50K
  higher_education_rich = higher_education / len(df50k)
  lower_education_rich = lower_education / len(df50k)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  df50kminh = df50k.loc[df50k['hours-per-week'] <= 40,
                        ['hours-per-week', 'salary']]

  num_min_workers = len(df50kminh)

  rich_percentage = len(df50kminh) / len(df)

  # What country has the highest percentage of people that earn >50K?

  df50khc = df50k['native-country'].value_counts()
  dfhc = df['native-country'].value_counts()
  dfPercent = df50khc / dfhc
  hPercent = dfPercent.max().round(decimals=3) * 100
  idx = dfPercent.idxmax()
  dfPercent.loc[idx]

  highest_earning_country = idx
  highest_earning_country_percentage = hPercent

  # Identify the most popular occupation for those who earn >50K in India.
  df50k = df.loc[df['salary'] == ">50K"]
  df50kIo = df50k.loc[df50k['native-country'] == "India", ['occupation']]
  oID50kImax = df50kIo.value_counts().idxmax()

  import re
  # top_IN_occupation = re.sub(r',(?=\))', '', str(oID50kImax))
  top_IN_occupation = str(oID50kImax)
  # DO NOT MODIFY BELOW THIS LINE

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
