from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category


# HOME
def home(request):

    categories = Category.objects.all().order_by('name')

    return render(request, 'home.html', {
        'categories': categories
    })


def note_list(request):

    notes = Note.objects.all().order_by('-created_at')
    categories = Category.objects.all().order_by('name')

    return render(request, 'notes.html', {
        'notes': notes,
        'categories': categories
    })


# ADD NOTE
def add_note(request):

    categories = Category.objects.all().order_by('name')

    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')

        Note.objects.create(
            title=title,
            content=content,
            category=category
        )

        return redirect('note_list')

    return render(request, 'add_note.html', {
        'categories': categories
    })


# VIEW NOTE
def view_note(request, id):

    note = get_object_or_404(Note, id=id)

    return render(request, 'view_note.html', {
        'note': note
    })


# EDIT NOTE
def edit_note(request, id):

    note = get_object_or_404(Note, id=id)

    categories = Category.objects.all().order_by('name')

    if request.method == 'POST':

        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.category = request.POST.get('category')

        note.save()

        return redirect('note_list')

    return render(request, 'edit_note.html', {
        'note': note,
        'categories': categories
    })


# DELETE NOTE
def delete_note(request, id):

    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':

        note.delete()

        return redirect('note_list')

    return render(request, 'delete_note.html', {
        'note': note
    })


# CATEGORY NOTES
def category_notes(request, category):

    notes = Note.objects.filter(
        category=category
    ).order_by('-created_at')

    return render(request, 'category_notes.html', {
        'notes': notes,
        'category': category
    })


# ADD NEW LANGUAGE
def add_category(request):

    if request.method == 'POST':

        name = request.POST.get('name').strip()

        if name:
            Category.objects.get_or_create(name=name)

        return redirect('home')

    return render(request, 'add_category.html')

