from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


urlpatterns = [
    path('',login_required(dashboardView,login_url='login'), name='dashboard'),
    path('kumpulan-soal/',login_required(assignmentView,login_url='login'), name='kumpulan-soal'),
    path('detail-soal/<int:pk>/',detailSoal,name='detail-soal'),
    path('buat-soal/',addQuestion, name='buat-soal'),
    path('list-question/',listQuestion,name='list-question'),
    path('list-materi/', listMateri, name='list-materi'),
    path('detail-materi/<int:pk>/', detailMateri, name='detail-materi'),
    path('add-materi/', addMateri, name='add-materi'),
    path('add-question/',addQuestion, name='add-question'),
    path('list-kategori/',listKategori,name='list-kategori'),
    path('list-sub-kategori/<int:pk>/', listSubKategori, name='list-sub-kategori'),
    path('tambah-kategori/', createKategori, name='tambah-kategori'),
    path('tambah-sub-kategori/<int:pk>/', createSubKategori, name='tambah-sub-kategori'),
    path('sub-kategori/',ajaxSubKategori,name='ajax-sub-kategori')
]

