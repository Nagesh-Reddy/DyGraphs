from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from pytrends.request import TrendReq
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from django.http import HttpResponse

def reports(request):
    try:
        df = pd.read_csv(r"C:\mysite\input_files\developer_survey_2019\survey_results_public.csv")
        #df = pd.read_csv(request.GET['Upload_File'])#"C:\Users\N2517\Desktop\developer_survey_2019\survey_results_public.csv")#(file_name) # 
        rs = df.groupby("Age1stCode")["Age1stCode"].value_counts()
        pd.set_option('display.max_columns', 85)
        pd.set_option('display.max_rows', 85)
        categories = list(rs.index)
        values = list(rs.values)
        table_content = df.to_html(index=None)
        table_content = table_content.replace("","")
        table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
        table_content = table_content.replace('border="1"',"")
        context = {"categories": categories, 'values': values, 'table_data':table_content}
    except:
        context = {"categories": 'No data', 'values': 'No values', 'table_data':'Please provide the file path'}
    return render(request, 'pages/reports.html', context=context)
    
def design(request):
    #file_name = request.GET #['Upload_File']
    try:
        df = pd.read_csv(request.GET['Upload_File'])    #"C:\mysite\input_files\car_sales.csv"
        rs = df.groupby("Engine size")["Sales in thousands"].agg("sum")
        categories = list(rs.index)
        values = list(rs.values)
        table_content = df.to_html(index=None)
        table_content = table_content.replace("","")
        table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
        table_content = table_content.replace('border="1"',"")

        a = df.loc[(df['VehicleType']=='Car'),['Width','Length']]
        a = list(a.values)
        car = []
        for i in a:
            car.append([int(i[1]),int(i[0])])
        print(car)
        b = df.loc[(df['VehicleType']=='Passenger'),['Width','Length']]
        b = list(b.values)
        passenger = []
        for i in b:
            passenger.append([int(i[1]),int(i[0])])
        print(passenger)
        coulmn_chart = 'The above chart is of Column Chart type. This chart is showing Car Sales in Thouisand dollars per Engine.'
        scattered_chart = 'The above chart is of Scattered Chart type. This chart is showing indivdual private/passenger cars width and lenght combinations '

        context = {"categories": categories, 'values': values, 'table_data':table_content, 'car':car, 'passenger':passenger, "coulmn_chart":coulmn_chart, "scattered_chart":scattered_chart}
    except:
        context = {"categories": 'No data', 'values': 'No values', 'table_data':'Please provide the file path'}    
    return render(request, 'pages/design.html', context=context)

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Nagesh Reddy'
    args = {'name': name, 'numbers': numbers}
    return render(request, 'pages/home.html', args)

def profile(request):
    name = 'Nagesh Reddy'
    args = {'name': name}
    return render(request, 'pages/profile.html', args)