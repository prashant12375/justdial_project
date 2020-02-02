from django.shortcuts import render
import pandas as pd
# Create your views here.

def show_data(request):
    if not True:#request.user.is_authenticated:
        return "<h2>ERROR</h2>"
    else:
        path = 'C://Users//PRASHANT//Desktop//export_dataframe.csv'
        return render(request,"page.html",get_csv_ashtml(path))

def get_csv_ashtml(path):
    df = pd.read_csv(path)
    contenxt = {'data':df.to_html()}
    return contenxt