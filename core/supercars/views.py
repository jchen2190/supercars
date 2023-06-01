from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
def get_homepage(request):
    if request.method == "GET":
        context = {"message": "Welcome!"}
        return render(request, "homepage.html", context)
    else:
        return HttpResponse("Invalid, only GET method is allowed")
    
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "allposts"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "object"

class PostCreateView(CreateView):
    model = Post
    fields = [ "make", "model", "description", "max_speed", "image"]
    template_name = "post_create.html"
    success_url = reverse_lazy("posts-all")

class PostUpdateView(UpdateView):
    model = Post
    fields = [ "make", "model", "description", "max_speed", "image"]
    template_name = "post_update.html"
    def get_success_url(self):
        return reverse_lazy("posts-detail", kwargs={"pk": self.object.pk})
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("posts-all")