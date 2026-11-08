from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category, Location


def index(request):
    """Отображает главную страницу блога."""
    post_list = (
        Post.objects
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        )
        .select_related('author', 'category', 'location')
        .order_by('-pub_date')[:5]
    )

    context = {
        'post_list': post_list,
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post_detail(request, post_id):
    """Отображает детали постов."""
    post = get_object_or_404(
        Post.objects.select_related(
            'location',
            'category',
            'author',
        ),
        pk=post_id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )
    context = {
        'post': post,
        'detail': {
            'title': (
                f"{post.location.name}. {post.created_at}"
                if post.location else str(post.created_at)
            ),
        },
    }

    return render(
        request,
        'blog/detail.html',
        context
    )


def category_posts(request, category_slug):
    """Отображает публикации выбранной категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = (
        Post.objects
        .filter(
            category=category,
            is_published=True,
            pub_date__lte=timezone.now(),
        )
        .select_related('author', 'category', 'location')
        .order_by('-pub_date')
    )

    context = {
        'category': category,
        'post_list': post_list
    }

    return render(
        request,
        'blog/category.html',
        context
    )
