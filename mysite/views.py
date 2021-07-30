from django.shortcuts import redirect, render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

def rrredirect(request):
    return redirect("/basep")

