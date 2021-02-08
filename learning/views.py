from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def dashboardView(request):

    return render(request,'dashboard/index.html')

def assignmentView(request):
    ass_data = Assignment.objects.all().order_by('-created_at')
    context = {
        'assignment':ass_data
    }

    return render(request,'dashboard/assignment/assignment.html',context)

def listQuestion(request,pk):
    as_data = Assignment.objects.get(id=pk)
    q = Question.objects.filter(assignment=as_data)
    context = {
        'dt': q,
        'ad': as_data
    }
    return render(request,'dashboard/assignment/list_question.html',context)


def addMateri(request,pk):
    ass_data = Assignment.objects.get(id=pk)
    if request.method == 'POST':
        print(request.POST)
        img = request.FILES.get('image-materi')
        mat = request.POST.get('materi')
        tit = request.POST.get('title')
        if img != None:
            x = ImageMateri.objects.create(img = img)
            b = Materi.objects.create(assignment=ass_data,materi=mat,title=tit)
            b.gambar.add(x)
            return redirect('list-materi',pk)
        b = Materi.objects.create(assignment=ass_data,materi=mat,title=tit)
        return redirect('list-materi', pk)

    context = {
        'data': ass_data
    }
    return render(request,'dashboard/assignment/add_materi.html',context)

def createAssignment(request):
    if request.method == 'POST' and request.POST.get('assignment_tittle') is not None:
        title = request.POST.get('assignment_tittle')
        x = Assignment.objects.create(title=title,teacher=request.user.data_teacher)
        return redirect('add-question',x.id)

    return render(request,'dashboard/assignment/create_assignment.html')

def addQuestion(request,pk):
    mat_data = Assignment.objects.get(id=pk)
    q = Question.objects.filter(assignment=mat_data)
    print(request.POST)
    if request.method == 'POST':
        ch = request.POST.getlist('choices')
        answer = request.POST.get('answer')
        question = request.POST.get('question')
        img = request.FILES.get('image-materi')
        q_type = request.POST.get('q_type')
        if q_type == 'choice' and img != None:
            for z in ch:
                b = Choice.objects.create(title=z)
            gbr = ImageMateri.objects.create(img=img)
            ans = Choice.objects.get(title=answer)
            x=Question.objects.create(assignment=mat_data,question=question,q_type=q_type,answer=ans)
            x.choices.add(*Choice.objects.filter(title__in=ch))
            x.img.add(gbr)
            return redirect('list-question',pk)

        elif q_type == 'choice' and img == None:
            for z in ch:
                b = Choice.objects.create(title=z)
            ans = Choice.objects.get(title=answer)
            x=Question.objects.create(assignment=mat_data,question=question,q_type=q_type,answer=ans)
            x.choices.add(*Choice.objects.filter(title__in=ch))
            return redirect('list-question',pk)

        elif q_type == 'text' and img != None:
            ans = Choice.objects.create(title=answer)
            gbr = ImageMateri.objects.create(img=img)
            x=Question.objects.create(assignment=mat_data,question=question,q_type=q_type,answer=ans)
            x.img.add(gbr)
            return redirect('list-question',pk)
        elif q_type == 'text' and img == None:
            ans = Choice.objects.create(title=answer)
            x = Question.objects.create(assignment=mat_data, question=question, q_type=q_type, answer=ans)
            return redirect('list-question', pk)
                    
    context = {
        'dt':q,
        'mat':mat_data
    }
    
    return render(request, 'dashboard/assignment/add_question.html',context)
