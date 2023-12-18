from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    data= {'author': 'John', 'age':25, 'lst':['Monday', 'Tuesday', 'Wednesday'], 'Birthday': datetime.datetime.now(), 'val': 20, 'data': 'Rasel', 'name': 'Python is Fun', 'value': [
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
], 'val': '<p>This <em>should be</em> fun!</p>', 'data' : ['Apple', 'Mango', 'Orange'], 'nm': ['Apple', 'Mango', 'Orange'], 'len' : ['Apple', 'Mango', 'Orange'], 'line' : 'Arnold'
'Brandy'
'Caleb'
'Dexter', 'lower' : 'I Am Rasel sarker', 'upper' : 'I Am Rasel sarker', 'title' : 'Django rest framework', 'ran' : ['Banana', 'Mango', 'Orange'], 'some_list' : ['Banana', 'Mango', 'Orange'], 'value' : '10:30:00.000123+02:00', 'trun' : 'Django template filters', 'word' : 'Django template filters', 'truncat' : 'You can python and Django', 'strip' : '<b>I</b> <button>love</button> <span>Bangladesh</span>', 'str' : 'programming hero', 'adsls' : 'geeks for geeks', 'cap': 'jai', 'cnt': 'jai', 'div': '21', 'file': '123456789'}
    return render(request, 'home.html', data)