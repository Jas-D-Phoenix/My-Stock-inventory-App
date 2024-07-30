from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
import csv
from .forms import *
from django.contrib import messages


def home(request):
    title = "Home Page"
    context = {
        "title": title
    }
    return render(request, "home.html", context)


def stock_list(request):
    stock = Stock.objects.all()
    form = SearchForm(request.POST or None)
    context = {
         "form": form,
         "stock": stock
    }
    if request.method == 'POST':
        category = form['category'].value()
        stock = Stock.objects.filter(
                                     stock_name__icontains=form['stock_name'].value())
        if category != ():
            stock = stock.filter(category_id=category)

        if form['export_to_csv'].value()==True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename = "Available Stocks.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'STOCK NAME', 'QUANTITY'])
            instance = stock
            for stock in instance:
                writer.writerow([stock.category, stock.stock_name, stock.quantity])
            return response
        context = {
            "stock": stock,
            "form": form,
        }
    return render(request, "stock_list.html", context)


def add_stock(request):
    form = StockForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Stock Has Been Added Successfully")
        return redirect('/stock_list')
    context = {
        "form": form
    }
    return render(request, "add_stock.html", context)


def update_stock(request, pk):
    stock = Stock.objects.get(id=pk)
    form = StockUpdate(instance=stock)
    if request.method == "POST":
        form = StockUpdate(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock Has Been Updated Successfully")
            return redirect('stock_list')
    context = {
         "form": form
    }
    return render(request, 'stock_update.html', context)


def delete_stock(request, pk):
    stock = Stock.objects.get(id=pk)
    if request.method == "POST":
        stock.delete()
        messages.success(request, "Stock Has Been Deleted Successfully")
        return redirect('stock_list')
    return render(request, 'delete_stock.html')


def stock_info(request, pk):
    stock = Stock.objects.get(id=pk)
    context = {
        "stock": stock
    }
    return render(request, 'stock_info.html', context)


def sale_stock(request, pk):
    stock = Stock.objects.get(id=pk)
    form = StockSell(request.POST or None, instance=stock)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity -= instance.quantity_sold
        messages.success(request,
                         "sale successful, " + str(instance.quantity) + " " + str(instance.stock_name) + " remaining")
        instance.save()
        return redirect("/stock_info/"+str(instance.id))
    context = {
        "stock": stock,
        "form": form
    }
    return render(request, 'add_stock.html',context)


def purchase_stock(request, pk):
    stock = Stock.objects.get(id=pk)
    form = StockPurchase(request.POST or None, instance=stock)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity += instance.quantity_purchased
        instance.save()
        return redirect("/stock_info/"+str(instance.id))
    context = {
        "stock": stock,
        "form": form
    }
    return render(request, 'add_stock.html',context)


def reorder_level(request, pk):
    stock = Stock.objects.get(id=pk)
    form = ReorderLevel(request.POST or None, instance=stock)
    if form.is_valid():
        stock = form.save(commit=False)
        stock.save()
        messages.success(request, "Reorder Level for "+ str(stock.stock_name)+" has been updated to "+ str(stock.reorder_level))
        return redirect("stock_list")
    context = {
        "stock": stock,
        "form": form
    }
    return render(request, "add_stock.html", context)


def stock_details(request):
    stock = StockDetails.objects.all()
    form = StockDetailsDateFilter(request.POST or None)
    context = {
        "stock": stock,
        "form": form
    }
    if request.method == 'POST':
        category = form['category'].value()
        stock = StockDetails.objects.filter(
            stock_name__icontains=form['stock_name'].value(),
            last_updated__range=[
                form['start_date'].value(),
                form['stop_date'].value()
            ]
        )
        if category != '':
            stock = stock.filter(category_id=category)
        context = {
            "stock": stock,
            "form": form
        }
    return render(request, 'stock_details.html', context)

