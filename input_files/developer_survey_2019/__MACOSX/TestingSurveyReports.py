{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "pd.set_option('display.max_rows', None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('C:/Users/N2517/Desktop/developer_survey_2019/survey_results_public.csv', index_col='Respondent')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pandas.core.groupby.generic.DataFrameGroupBy object at 0x05739640>"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_grp = df.groupby(['Country'])\n",
    "country_grp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Country\n",
       "Afghanistan             0\n",
       "Antigua and Barbuda     0\n",
       "Argentina               2\n",
       "Armenia                 0\n",
       "Australia              13\n",
       "Name: LanguageWorkedWith, dtype: int64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())\n",
    "country_uses_python.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "United States     253\n",
       "India              88\n",
       "United Kingdom     63\n",
       "Germany            54\n",
       "Canada             43\n",
       "Name: Country, dtype: int64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_respondents = df['Country'].value_counts()\n",
    "country_respondents.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Country</th>\n",
       "      <th>LanguageWorkedWith</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>United States</th>\n",
       "      <td>253</td>\n",
       "      <td>131</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>India</th>\n",
       "      <td>88</td>\n",
       "      <td>37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>United Kingdom</th>\n",
       "      <td>63</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Germany</th>\n",
       "      <td>54</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Canada</th>\n",
       "      <td>43</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Country  LanguageWorkedWith\n",
       "United States       253                 131\n",
       "India                88                  37\n",
       "United Kingdom       63                  29\n",
       "Germany              54                  26\n",
       "Canada               43                  19"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "python_df = pd.concat([country_respondents, country_uses_python], axis='columns', sort=False)\n",
    "python_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>NumRespondents</th>\n",
       "      <th>NumKnowsPython</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>United States</th>\n",
       "      <td>253</td>\n",
       "      <td>131</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>India</th>\n",
       "      <td>88</td>\n",
       "      <td>37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>United Kingdom</th>\n",
       "      <td>63</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Germany</th>\n",
       "      <td>54</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Canada</th>\n",
       "      <td>43</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                NumRespondents  NumKnowsPython\n",
       "United States              253             131\n",
       "India                       88              37\n",
       "United Kingdom              63              29\n",
       "Germany                     54              26\n",
       "Canada                      43              19"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "python_df.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True)\n",
    "python_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>NumRespondents</th>\n",
       "      <th>NumKnowsPython</th>\n",
       "      <th>PercentKnowsPython</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Bahrain</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Colombia</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>100.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Peru</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Armenia</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Antigua and Barbuda</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     NumRespondents  NumKnowsPython  PercentKnowsPython\n",
       "Bahrain                           1               0                 0.0\n",
       "Colombia                          1               1               100.0\n",
       "Peru                              1               0                 0.0\n",
       "Armenia                           1               0                 0.0\n",
       "Antigua and Barbuda               1               0                 0.0"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "python_df['PercentKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents']) * 100\n",
    "python_df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age1stCode</th>\n",
       "      <th>CompTotal</th>\n",
       "      <th>ConvertedComp</th>\n",
       "      <th>WorkWeekHrs</th>\n",
       "      <th>CodeRevHrs</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>988.000000</td>\n",
       "      <td>6.480000e+02</td>\n",
       "      <td>6.450000e+02</td>\n",
       "      <td>737.000000</td>\n",
       "      <td>588.000000</td>\n",
       "      <td>905.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>15.243927</td>\n",
       "      <td>6.626023e+05</td>\n",
       "      <td>1.292668e+05</td>\n",
       "      <td>42.193691</td>\n",
       "      <td>4.690986</td>\n",
       "      <td>30.147956</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>5.320928</td>\n",
       "      <td>4.990838e+06</td>\n",
       "      <td>2.878622e+05</td>\n",
       "      <td>21.247168</td>\n",
       "      <td>3.849582</td>\n",
       "      <td>8.674765</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>12.000000</td>\n",
       "      <td>2.100000e+04</td>\n",
       "      <td>2.948400e+04</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>24.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>6.500000e+04</td>\n",
       "      <td>5.957900e+04</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>29.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>1.210000e+05</td>\n",
       "      <td>1.031170e+05</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>35.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>85.000000</td>\n",
       "      <td>8.500000e+07</td>\n",
       "      <td>2.000000e+06</td>\n",
       "      <td>385.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>67.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Age1stCode     CompTotal  ConvertedComp  WorkWeekHrs  CodeRevHrs  \\\n",
       "count  988.000000  6.480000e+02   6.450000e+02   737.000000  588.000000   \n",
       "mean    15.243927  6.626023e+05   1.292668e+05    42.193691    4.690986   \n",
       "std      5.320928  4.990838e+06   2.878622e+05    21.247168    3.849582   \n",
       "min      5.000000  0.000000e+00   0.000000e+00     1.000000    0.000000   \n",
       "25%     12.000000  2.100000e+04   2.948400e+04    40.000000    2.000000   \n",
       "50%     15.000000  6.500000e+04   5.957900e+04    40.000000    4.000000   \n",
       "75%     18.000000  1.210000e+05   1.031170e+05    45.000000    6.000000   \n",
       "max     85.000000  8.500000e+07   2.000000e+06   385.000000   30.000000   \n",
       "\n",
       "              Age  \n",
       "count  905.000000  \n",
       "mean    30.147956  \n",
       "std      8.674765  \n",
       "min      1.000000  \n",
       "25%     24.000000  \n",
       "50%     29.000000  \n",
       "75%     35.000000  \n",
       "max     67.000000  "
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0AED41D8>"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "age1stcode_group = df.groupby(['Age1stCode'])\n",
    "age1stcode_group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "age1stcode_group_country1 = age1stcode_group['Country'].value_counts().keys().tolist()\n",
    "age1stcode_group_country2 = age1stcode_group['Country'].value_counts().tolist()\n",
    "#for i in range(len(age1stcode_group_country1)):\n",
    "    #print(age1stcode_group_country1[i],age1stcode_group_country2[i])\n",
    "#print(age1stcode_group_country1)\n",
    "#print(age1stcode_group_country2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0AED4E80>"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_group = df.groupby(['Employment'])\n",
    "emp_group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Employed full-time','I am a developer by profession','635'],\n",
      "['Employed full-time','I am not primarily a developer, but I write code sometimes as part of my work','57'],\n",
      "['Employed full-time','I used to be a developer by profession, but no longer am','10'],\n",
      "['Employed full-time','I am a student who is learning to code','9'],\n",
      "['Employed full-time','I code primarily as a hobby','3'],\n",
      "['Employed part-time','I am a developer by profession','32'],\n",
      "['Employed part-time','I am a student who is learning to code','24'],\n",
      "['Employed part-time','I am not primarily a developer, but I write code sometimes as part of my work','5'],\n",
      "['Employed part-time','I code primarily as a hobby','4'],\n",
      "['Employed part-time','I used to be a developer by profession, but no longer am','1'],\n",
      "['Independent contractor, freelancer, or self-employed','I am a developer by profession','75'],\n",
      "['Independent contractor, freelancer, or self-employed','I am not primarily a developer, but I write code sometimes as part of my work','9'],\n",
      "['Independent contractor, freelancer, or self-employed','I am a student who is learning to code','8'],\n",
      "['Independent contractor, freelancer, or self-employed','I code primarily as a hobby','6'],\n",
      "['Independent contractor, freelancer, or self-employed','I used to be a developer by profession, but no longer am','2'],\n",
      "['Not employed, and not looking for work','I am a student who is learning to code','24'],\n",
      "['Not employed, and not looking for work','I code primarily as a hobby','7'],\n",
      "['Not employed, and not looking for work','I am a developer by profession','1'],\n",
      "['Not employed, and not looking for work','I used to be a developer by profession, but no longer am','1'],\n",
      "['Not employed, but looking for work','I am a student who is learning to code','36'],\n",
      "['Not employed, but looking for work','I am a developer by profession','10'],\n",
      "['Not employed, but looking for work','I code primarily as a hobby','6'],\n",
      "['Not employed, but looking for work','I am not primarily a developer, but I write code sometimes as part of my work','5'],\n",
      "['Not employed, but looking for work','I used to be a developer by profession, but no longer am','2'],\n",
      "['Retired','I code primarily as a hobby','1'],\n",
      "['Retired','I used to be a developer by profession, but no longer am','1'],\n"
     ]
    }
   ],
   "source": [
    "MainBranch_emp_group1 = emp_group['MainBranch'].value_counts().keys().tolist()\n",
    "MainBranch_emp_group2 = emp_group['MainBranch'].value_counts().tolist()\n",
    "for i in range(len(MainBranch_emp_group1)):\n",
    "    print(\"['{}','{}','{}'],\".format(MainBranch_emp_group1[i][0],MainBranch_emp_group1[i][1],MainBranch_emp_group2[i]))\n",
    "    #print(*MainBranch_emp_group1[i],MainBranch_emp_group2[i])\n",
    "#print(MainBranch_emp_group1)\n",
    "#print(MainBranch_emp_group2)\n",
    "#print(len(MainBranch_emp_group1))\n",
    "#print(len(MainBranch_emp_group2))\n",
    "#print(MainBranch_emp_group1)\n",
    "#print(MainBranch_emp_group2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
