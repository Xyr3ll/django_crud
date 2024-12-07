# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import ItemForm

# List view
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

# Create view
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list') 
    else:
        form = ItemForm()

    return render(request, 'item_form.html', {'form': form, 'item': None}) 

# Update view
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk) 
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()  # Save the updated item
            return redirect('item_list') 
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form, 'item': item})


# Delete view
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})
