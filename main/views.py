from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleForm
from .models import Article
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from .decorators import allowed_groups
from .mixins import AllowedGroupsMixin

# Create your views here.

# Hamma uchun ochiq bo'lgan view
class IndexView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'index.html', {'articles':articles})



#Faqatgina Authorlar kira oladigan view
class ArticleNewView(PermissionRequiredMixin, View):
    permission_required = 'main.add_article'
    permission_denied_message = 'Siz author emassiz!'
    def get(self, request):
        form = ArticleForm()
        return render(request, 'article_new.html', {'form':form})
    
    def post(self, request):
        form = ArticleForm(data=request.POST)
        if form.is_valid:
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', article.id)
        return render(request, 'article_new.html', {'form':form})    



#Faqatgina maqolani ko'rishga ruxsati borlar uchun view
@permission_required(perm='main.view_article', login_url='login')
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article':article})    
 
 
    
#Faqatgina managerlar kira oladigan view
@allowed_groups(['Manager',])
def manager_dashboard(request):
    return render(request, 'manager_dashboard.html')    



#Faqatgina marketologlar kira oladigan view
class MarketologDashboard(AllowedGroupsMixin, View):
    allowed_groups = ['Marketolog',]
    def get(self, request):
        return render(request, 'marketolog_dashboard.html')