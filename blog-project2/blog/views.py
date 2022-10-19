from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from .form import CommentForm
from .models import Post, Comment, Category


# Create your views here.
def post_list(request, category=None):
    posts = Post.published.all()      #Post.odject.all()
    categories = Category.objects.all()

    if category:       # or (if category is not None)
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category)
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts':posts,
        'page':page,
        'categories':categories,
        'category':category
    }

    return render(request, "blog/post/list.html", context)

def post_detail(request, year:int, month:int, day:int, slug: str):
    """ first methode of try-exception
    try:
        post= Post.objects.get(slug=slug)

    except Post.DoesNotExist:
        raise ("THis post doesnot exist")
    """
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = Comment.objects.filter(post=post.pk)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()


    else:
        comment_form = CommentForm()

    return render(request, "blog/post/detail.html", {"post":post,
                                                     'comments':comments,
                                                     'new_comment':new_comment,
                                                     'comment_form':comment_form
                                                     })