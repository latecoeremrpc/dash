from django.shortcuts import render
import datetime
from home.models import Organisation
from home.models import Profit_center
from home.models import Division
from home.models import Range



# Create your views here.
""" def home(request):
    print('i m here')
    return render(request, r'home\filter.html')
 """
def home(request):
   
    divisions = Division.objects.all()
    weeks_range = Range.objects.first()
    organisations = Organisation.objects.all()
    profits = Profit_center.objects.all()

    current_week=datetime.datetime.now().isocalendar().week
    current_year=datetime.datetime.now().isocalendar().year
    
    #Get 12 week from now
    range_date=[str(current_week)+'_'+str(current_year)]

    for i in range(abs(weeks_range.weeks_number)):
        current_week=current_week-1
        if current_week==0:
            current_year-=1
            current_week=52
        range_date.append( str(current_week)+'_'+str(current_year))
    
    if request.method=='POST':
        weeks_input=request.POST.getlist('weeks')
        divisions_input=request.POST.getlist('divisions')
        organisations_input=request.POST.getlist('organisations')
        profits_input=request.POST.getlist('profit_center')

        print(weeks_input)
        print(divisions_input)
        print(organisations_input)
        print(profits_input)


    context={'organisations': organisations, 'profits':profits,'divisions':divisions,'range_date':range_date}
    return render(request,'home/index.html', context)


