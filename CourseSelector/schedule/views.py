import django.http
from django.shortcuts import render
from django.views.generic import View

from schedule.models import  Schedule
from students.models import OpenCoursesForYou
class HomeView(View):

    def get(self, request):

        user=request.user
        schedule_display=OpenCoursesForYou.objects.filter(student=user).filter(schedule__id="1")
        qs = OpenCoursesForYou.objects.filter(student=user).exclude(grade__contains='D')
        dep_qs=OpenCoursesForYou.objects.filter(student=user).exclude(elective=None)


        context = {}
        context['schedule']=schedule_display
        context['courses'] = qs
        context['dep']=dep_qs

        return render(self.request, 'schedule.html', context)


class scheduleUpdateView(View):

    def post(self,request):
        user = request.user
        name = request.POST.get('short_name', None)
        schedule_qs=OpenCoursesForYou.objects.filter(short_name=name, student=user)

        if schedule_qs.exists():

             item = schedule_qs.first()
             print("denemee::",item.day_hour)
             # CONVERT DATE FOR SCHEDULE
             a = self.convert_course_date(item.day_hour)
             print("converted date:", a)
            
             return django.http.JsonResponse({'short_name':item.short_name, 'place_in_schedule':a})




    def convert_course_date(self,date):

        test = date.split(" ", 1)
        a = test[0]
        b = test[1]
        g = list(map(str, a))
        i = 0
        while i < len(g)-1:
            if g[i] == 'T' and g[i + 1] == 'h':
                g[i] = g[i] + g[i + 1]
                g.pop(i + 1)
            else:
                i += 1

        schedule_place = ''
        for i in range(0, len(g)):
            schedule_place = schedule_place + g[i] + b[i]

        return schedule_place

class update_schedule(View):

    def get(self, request):
        schedule_display=Schedule.objects.all()
        qs = OpenCoursesForYou.objects.all()
        context = {}
        context['courses'] = qs
        context['schedule']=schedule_display
        return render(self.request, 'schedule.html', context)

class add_course_in_schedule(View):



    def post(self,request):
        user = request.user
        course_name= request.POST.get('course_name', None)
        qs = OpenCoursesForYou.objects.filter(short_name=course_name, student=user)
        s1 = Schedule.objects.get(id=1)

        if qs.exists():
            item = qs.first()
            a = self.convert_course_date(item.day_hour)
            s1.place_in_schedule = a
            s1.save()
            item.schedule.add(s1)
            item.save()

            print(s1.place_in_schedule,"oldu")

            print("denemee buraya eklenicek bro::", item.day_hour)
            # CONVERT DATE FOR SCHEDULE



            return django.http.JsonResponse({})

    def convert_course_date(self,date):

        test = date.split(" ", 1)
        a = test[0]
        b = test[1]
        g = list(map(str, a))
        i = 0
        while i < len(g)-1:
            if g[i] == 'T' and g[i + 1] == 'h':
                g[i] = g[i] + g[i + 1]
                g.pop(i + 1)
            else:
                i += 1

        schedule_place = ''
        for i in range(0, len(g)):
            schedule_place = schedule_place + g[i] + b[i]

        return schedule_place