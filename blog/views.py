from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
from django.views.generic import ListView,\
    DetailView,\
    CreateView,\
    UpdateView, DeleteView
# Данная библиотека позволяет просматривать
# содержимое сайта только зарегистрированным пользователям
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.staticfiles.views import serve


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def getfile(request):
   return serve(request, 'File')


# Создаем класс для обработки всех постов
# В качестве обработки используем файл home.html
# В качестве модели Post
# Так как нам нужно посредством цикла выводить
# все посты, мы должны использовать objects_list,
# вместо это используем posts.
# Мы изменили имя цикла, посредством переменной context_object_name
# Далее мы разбиваем главную страницу на 2 поста на одной странице
# ListView-нужна для перечисления всех постов

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 2
    login_url = 'login'



# Создаем класс для обработки созданных постов каждым пользователем.
# В качестве обработки используем файл user_posts.html
# В качестве модели Post
# Так как нам нужно посредством цикла выводить
# все посты, мы должны использовать objects_list,
# вместо это используем posts.
# Мы изменили имя цикла, посредством переменной context_object_name
# Далее мы разбиваем главную страницу на 2 поста на одной странице
# ListView-нужна для перечисления всех постов

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2
    login_url = 'login'

    # Вызвали функцию get_queryset- чтобы работать с базой данных.
    # Выводим все посты созданные пользователем
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)




class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    login_url = 'login'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content', 'file']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title','content','file']


    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'


def about(request):
    return render(request,'blog/about.html', {'title':'About'})
