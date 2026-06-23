from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import ProtectedError

from .models import Category
from items.models import Item

def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
        if Category.objects.filter(creator=request.user, name=request.POST['name']).exists():
            return render(request, 'categories/current.html', {'error': '동일 이름의 카테고리가 존재합니다.'})
        new_category = Category()
        new_category.creator = request.user
        new_category.name = request.POST['name']
        new_category.save()

        return redirect('items:storage')  # 수정 필요
        
def delete(request, category_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    delete_category = get_object_or_404(Category, pk=category_id)

    if delete_category.is_default:
        return redirect('items:storage')  # 수정 필요

    if delete_category.creator != request.user:
        return redirect('items:storage')  # 수정 필요

    try:
        delete_category.delete()
    except ProtectedError:
        return redirect('items:storage')  # 수정 필요

    return redirect('items:storage')  # 수정 필요