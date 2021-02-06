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

def listMateri(request,pk):
    ass_data = Assignment.objects.get(id=pk)
    materi_data = Materi.objects.filter(assignment=ass_data) 
    context = {
        'data':ass_data,
        'materi':materi_data
    }
    return render(request, 'dashboard/assignment/list_materi.html',context)

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
        return redirect('list-materi',x.id)

    return render(request,'dashboard/assignment/create_assignment.html')

def addQuestion(request,pk):
    mat_data = Materi.objects.get(id=pk)
    q = Question.objects.filter(materi=mat_data)
    print(request.POST)
    if request.method == 'POST':
        ch = request.POST.getlist('choices')
        answer = request.POST.get('answer')
        question = request.POST.get('question')
        q_type = request.POST.get('q_type')
        if q_type == 'choice':
            for z in ch:
                b = Choice.objects.create(title=z)
            ans = Choice.objects.get(title=answer)
            x=Question.objects.create(materi=mat_data,question=question,q_type=q_type,answer=ans)
            x.choices.add(*Choice.objects.filter(title__in=ch))
            return redirect('add-question',pk)
        elif q_type == 'text':
            ans = Choice.objects.create(title=answer)
            x=Question.objects.create(materi=mat_data,question=question,q_type=q_type,answer=ans)
            return redirect('add-question',pk)
                    
    context = {
        'dt':q,
        'mat':mat_data
    }
    
    return render(request, 'dashboard/assignment/add_question.html',context)
