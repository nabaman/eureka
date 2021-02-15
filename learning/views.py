from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def dashboardView(request):

    context = {
        'ttl':Question.objects.all().count()
    }

    return render(request,'dashboard/index.html',context)

def assignmentView(request):
    ass_data = Question.objects.all().order_by('-created_at')
    context = {
        'soal':ass_data
    }

    return render(request,'dashboard/assignment/list_soal.html',context)

def detailSoal(reques,pk):
    q = Question.objects.get(id=pk)
    context = {
        'q':q
    }

    return render(reques,'dashboard/assignment/detail_soal.html',context)

def listQuestion(request):
    # as_data = Assignment.objects.get(id=pk)
    q = Question.objects.all()
    context = {
        'soal':q
        # 'ad': as_data
    }
    return render(request,'dashboard/assignment/list_question.html',context)

def listMateri(request):
    materi = Materi.objects.all()

    context = {
        'materi':materi
    }
    return render(request,'dashboard/materi/list_materi.html',context)

def detailMateri(request,pk):
    mt = Materi.objects.get(id=pk)
    context = {
        'mt':mt
    }
    return render(request,'dashboard/assignment/detail_materi.html',context)




def addMateri(request):
    if request.method == 'POST':
        img = request.FILES.get('image-materi')
        mat = request.POST.get('materi')
        tit = request.POST.get('title')
        if img != None:
            x = ImageMateri.objects.create(img = img)
            b = Materi.objects.create(materi=mat,title=tit)
            b.gambar.add(x)
            return redirect('list-materi')
        b = Materi.objects.create(materi=mat,title=tit)
        return redirect('list-materi')

    context = {
        # 'data': ass_data
    }
    return render(request,'dashboard/materi/add_materi.html',context)

def createKategori(request):
    if request.method == 'POST':
        kat = request.POST.get('kategori')
        Question_Kategori.objects.create(sub_kategori_name=kat)
        return redirect('list-kategori')
    return render(request,'dashboard/assignment/tambah_kategori.html')

def listSubKategori(request,pk):
    kat = Question_Kategori.objects.get(id=pk)
    context = {
        'kat':kat,
        'subkat':Question_Kategori.objects.filter(parent=kat)
    }
    return render(request,'dashboard/assignment/list_subkategori.html',context)

def createSubKategori(request,pk):
    par = Question_Kategori.objects.get(id=pk)
    if request.method == 'POST':
        Question_Kategori.objects.create(sub_kategori_name = request.POST.get('subkategori'),parent = par)
        return redirect('list-sub-kategori',pk)
    context = {
        'kat':par
    }
    return render(request,'dashboard/assignment/tambah_subkategori.html',context)

def listKategori(request):
    context = {
        'kt':Question_Kategori.objects.filter(parent=None)
    }

    return render(request,'dashboard/assignment/list_kategori.html',context)


def createAssignment(request):
    if request.method == 'POST' and request.POST.get('assignment_tittle') is not None:
        title = request.POST.get('assignment_tittle')
        x = Assignment.objects.create(title=title,teacher=request.user.data_teacher)
        return redirect('add-question',x.id)

    return render(request,'dashboard/assignment/create_assignment.html')

def ajaxSubKategori(request):
    data = request.GET.get('kategori')
    x = Question_Kategori.objects.filter(parent__sub_kategori_name=data)
    context = {
        'data':x

    }
    return render(request, 'dashboard/assignment/sub_kategori.html',context)

def addQuestion(request):
    # mat_data = Assignment.objects.get(id=pk)
    # q = Question.objects.filter(assignment=mat_data)
    kategori = Question_Kategori.objects.filter(parent=None)
    print(request.POST)
    if request.method == 'POST':
        ch = request.POST.getlist('choices')
        answer = request.POST.get('answer')
        question = request.POST.get('question')
        kat = request.POST.get('sub_kategori')
        img = request.FILES.get('image-materi')
        q_type = request.POST.get('q_type')
        level = request.POST.get('level')
        kat_instance = Question_Kategori.objects.get(sub_kategori_name=kat)
        if q_type == 'choice' and img != None:
            for z in ch:
                b = Choice.objects.get_or_create(title=z)
            gbr = ImageMateri.objects.create(img=img)
            ans = Choice.objects.get(title=answer)
            x=Question.objects.create(question=question,q_type=q_type,answer=ans,q_kategori=kat_instance,level=level)
            x.choices.add(*Choice.objects.filter(title__in=ch))
            x.img.add(gbr)
            return redirect('kumpulan-soal')

        elif q_type == 'choice' and img == None:
            for z in ch:
                b = Choice.objects.get_or_create(title=z)
            ans = Choice.objects.get(title=answer)
            x=Question.objects.create(question=question,q_type=q_type,answer=ans,q_kategori=kat_instance,level=level)
            x.choices.add(*Choice.objects.filter(title__in=ch))
            return redirect('kumpulan-soal')

        elif q_type == 'text' and img != None:
            ans,st = Choice.objects.get_or_create(title=answer)
            gbr = ImageMateri.objects.create(img=img)
            x=Question.objects.create(question=question,q_type=q_type,answer=ans,q_kategori=kat_instance,level=level)
            x.img.add(gbr)
            return redirect('kumpulan-soal')
        elif q_type == 'text' and img == None:
            ans,st = Choice.objects.get_or_create(title=answer)
            x = Question.objects.create(question=question, q_type=q_type, answer=ans,q_kategori=kat_instance,level=level)
            return redirect('kumpulan-soal')
                    
    context = {
        'kat':kategori,
    }
    
    return render(request, 'dashboard/assignment/add_question.html',context)
