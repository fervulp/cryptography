from django.shortcuts import render
from .forms import *
from .utils import MyMixin
from django.views.generic import View
from .other import data
# Create your views here.

def home(request):
    context = {'title': 'Главная'}
    return render(request, 'local/empty.html', context)

class Info(MyMixin, View):
    
    def get(self, request, *args, **kwargs):
        context = { 
            "title": 'Справка',
            'list_task': data
        }
        return render(request, 'local/info.html', context)


class Home(MyMixin, View):
    
    def get_context(self):
        context = {
            1 : {'form': ['n1', 'mod1', 'n2', 'mod2', 'n3', 'mod3']},
            2 : {'form': ['p', 'q', 'x', 'y']},
            3 : {'form': ['p', 'x1', 'y1', 'X1']}, 
            4 : {'form': ['p', 'g', 'y', 'M', 'k']},
            5 : {'form': ['p', 'g', 'x', 'r', 's']},
            6 : {'form': ['N1', 'e1', 'N2', 'e2', 'M']},
            7 : {'form': ['N1', 'e1', 'N2', 'e2', 'C', 'p', 'q']},
            8 : {'form': ['N', 'e1', 'e2', 'C1', 'C2']},
            9 : {'form': ['N1', 'N2', 'N3', 'C1', 'C2', 'C3']},
           10 : {'form': ['N']}
        }
        # return cont[self.kwargs['id']] | {'id' : self.kwargs['id'] - 1, 'title': data[self.kwargs['id']-1][1] }
        return context[self.kwargs['id']] | {'id' : self.kwargs['id'], 'title': f"{data[self.kwargs['id']-1][1]}" }
        

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        context['form'] = [ [el, ''] for el in context['form'] ]
        return render(request, 'local/home.html', context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        id = self.kwargs['id']

        task = {
            1 :self.task1,
            2 :self.task2,
            3 :self.task3,
            4 :self.task4,
            5 :self.task5,
            6 :self.task6,
            7 :self.task7,
            8 :self.task8,
            9 :self.task9,
            10: self.task10
        }

        context = self.get_context()
        # context['form'] = context['form'](data)
        array_num =  [ [a, data.get(a, '') ] for a in context['form']]
        context['form'] = array_num

        if len( context['form'] ) == len( [ a for a in context['form'] if a[1] != '' ]  ):
            context['answer'] = task[id](*[ int(a[1]) for a in array_num])
        else:
            context['answer']  = 'СПЕЦИАЛЬНО ДА?'
        return render(request, 'local/home.html', context)