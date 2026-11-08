from django.shortcuts import render


def about(request):
    """Страница о проекте."""
    return render(
        request,
        'pages/about.html'
    )


def rules(request):
    """Правила пользования."""
    return render(
        request,
        'pages/rules.html'
    )
