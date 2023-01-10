from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse
)
from .models import (
    Products,
    User,
    Banner,
    ProductCategory,
    ProductOrder,
    ProductFeedback,
    ShopingCart
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import(
    AddProduct,
    UpdateProductForm,
    UpdateFeedbackForm
)
from django.http import HttpResponseRedirect
from userProfileApp.forms import (
    UserProfileUpdateForm,
    ProfilePictureUpdateForm,
)
from django.db.models import Q

# Create your views here.
def AllProducts(request):
    allProducts = Products.objects.all()
    context = {
        "allProducts":allProducts,
        "TotalProduct":allProducts.count
    }
    return render(request, 'products.html', context)



#product details =============================================================
def ProductDetails(request,pk):
    productDetails = get_object_or_404(Products, pk=pk)

    user_has_bought_product = False
    if request.user.is_authenticated:
        products_bought_by_user = Products.objects.filter(ProductOrderProductRelatedName__user=request.user)
        
        if productDetails in products_bought_by_user:
            user_has_bought_product = True 
        else:
            user_has_bought_product = False
    

    AllFeedbackOfAProduct = productDetails.ProducTFeedbackProductRelatedName.all()
    TotalProductsFeedback = AllFeedbackOfAProduct.count()
    TotalRatings = 0
    AverageRating = 0
    AllOneStar = AllTwoStar = AllThreeStar = AllFourStar = AllFiveStar = 0
    OneStarAveragePercentage = TwoStarAveragePercentage = ThreeStarAveragePercentage = FourStarAveragePercentage = FiveStarAveragePercentage = 0
    
    if TotalProductsFeedback !=0 :
        AllOneStar = productDetails.ProducTFeedbackProductRelatedName.filter(rating=1).count()
        AllTwoStar = productDetails.ProducTFeedbackProductRelatedName.filter(rating=2).count()
        AllThreeStar = productDetails.ProducTFeedbackProductRelatedName.filter(rating=3).count()
        AllFourStar = productDetails.ProducTFeedbackProductRelatedName.filter(rating=4).count()
        AllFiveStar = productDetails.ProducTFeedbackProductRelatedName.filter(rating=5).count()


        OneStarAveragePercentage = round((productDetails.ProducTFeedbackProductRelatedName.filter(rating=1).count() / TotalProductsFeedback)*100,1)
        TwoStarAveragePercentage = round((productDetails.ProducTFeedbackProductRelatedName.filter(rating=2).count() / TotalProductsFeedback)*100,1)
        ThreeStarAveragePercentage = round((productDetails.ProducTFeedbackProductRelatedName.filter(rating=3).count() / TotalProductsFeedback)*100,1)
        FourStarAveragePercentage = round((productDetails.ProducTFeedbackProductRelatedName.filter(rating=4).count() / TotalProductsFeedback)*100,1)
        FiveStarAveragePercentage = round((productDetails.ProducTFeedbackProductRelatedName.filter(rating=5).count() / TotalProductsFeedback)*100,1)

    for ProductRating in AllFeedbackOfAProduct:
        rating = ProductRating.rating # rating = field name of ProductREVIEWS model
        if rating:
            TotalRatings += rating
            AverageRating = round(TotalRatings/TotalProductsFeedback,1)
    context = {
        "productDetails":productDetails,
        "user_has_bought_product":user_has_bought_product,
        "AllFeedbackOfAProduct":AllFeedbackOfAProduct,
        "AllOneStar":AllOneStar,
        "AllTwoStar":AllTwoStar,
        "AllThreeStar":AllThreeStar,
        "AllFourStar":AllFourStar,
        "AllFiveStar":AllFiveStar,
        "OneStarAveragePercentage":OneStarAveragePercentage,
        "TwoStarAveragePercentage":TwoStarAveragePercentage,
        "ThreeStarAveragePercentage":ThreeStarAveragePercentage,
        "FourStarAveragePercentage":FourStarAveragePercentage,
        "FiveStarAveragePercentage":FiveStarAveragePercentage,
        "AverageRating":AverageRating,
        "TotalProductsFeedback":TotalProductsFeedback
    }
    return render(request, 'product_details.html', context)


@login_required(login_url='siungIn')  
def MyProducts(request):
    MyProducts = request.user.productsRelatedName.all()

    context = {
        "MyProducts":MyProducts,
        "TotalMyProduct":MyProducts.count
    }
    return render(request, "my_products.html", context)

@login_required(login_url='siungIn')
def addProduct(request):
    submitted = False
    if request.method == "POST":
        form = AddProduct(request.POST)
        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user

            if form.instance !='':
                form.save()
                messages.success(request,"Successfully product added.")
                return redirect("addProduct")
        else:
            form = AddProduct()
            if 'submitted' in request.GET:
                submitted = True


    form = AddProduct
    context = {
        "form":form 
    }

    return render(request, "add_product.html", context)


#update product==========================================================
@login_required(login_url='siungIn')
def UpdateProduct(request,pk):
    product = Products.objects.get(pk=pk)
    form = UpdateProductForm(request.POST or None, instance=product)
    
    if form.is_valid() and request.method == 'POST':
        if product.user==request.user or request.user.is_superuser:
            form = UpdateProductForm(request.POST, request.FILES, instance=product)
            
            form.save()
            print(form.errors)
            messages.success(request,"Successfully product information updated.")
            # return redirect("MyProducts")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

    context = {
        'product':product,
        "form":form
    }
    
    return render(request, "update_product.html", context)

#delete product==========================================================
@login_required(login_url='siungIn')
def DeleteProduct(request,pk):
    Products.objects.get(pk=pk).delete()
    messages.success(request,"Successfully product deleted.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 


#user's product for admin================================================
@login_required(login_url='siungIn')
def UserProductsForAdmin(request):
    AllUserProducts = Products.objects.all()

    context = {
        "AllUserProducts":AllUserProducts,
        "TotalUserProduct":AllUserProducts.count,
    }
    return render(request, 'all_sllers_product_for_admin.html', context)

@login_required(login_url='siungIn')
def AllUsers(request):
    #from django.contrib.auth.models import User
    AllUsers = User.objects.filter(is_superuser=False)
    context = {
        "AllUsers":AllUsers,
    
    }

    return render(request, 'all_sellers.html', context)


#user profile================================================
@login_required(login_url='siungIn')  
def SellerProfile(request, pk):
    UserDetails = get_object_or_404(User, pk=pk)


    #profile info ====================
    form = UserProfileUpdateForm(instance=UserDetails)
    if request.method == "POST":
        if request.user.pk != UserDetails.pk:
            redirect("/")
        form = UserProfileUpdateForm(request.POST, instance=UserDetails)  

        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated.")
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        else:
            #messages.warning(request, form.errors)
            print(form.errors)


    #profile picture ====================


    context = {
        "UserDetails":UserDetails,
        "form":form,
        "AllSellers":User.objects.filter(is_superuser=False).count
    }

    return render(request, 'seller_profile.html', context)

@login_required(login_url='siungIn')
def ProfilePictureChngeForAdmin(request, pk):
    UserDetails = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = ProfilePictureUpdateForm(request.POST, request.FILES)
        if form.is_valid():

            image = request.FILES['profile_image']
            user = get_object_or_404(User, pk=UserDetails.pk)
            

            # if request.user.is_superuser :
            #     return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

            user.profile_image = image
            user.save()
            messages.success(request,"Profile picture update success!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





@login_required(login_url='siungIn')
def SpecificUsersProductForAdmin(request,pk):
    user = get_object_or_404(User, pk=pk)
    SpecificUserProductsForAdmin = user.productsRelatedName.all()
    context = {
        "user":user,
        "SpecificUserProductsForAdmin":SpecificUserProductsForAdmin
    }
    return render(request, 'specific_user_product_for_admin.html', context)



#home___________________________________________________
def Home(request):

    #banners__________________________
    banners = Banner.objects.all()
    total_banners = banners.count()
    list = []
    
    for i in range(0,total_banners):
        list.append(i)
    
    #all products_____________________
    AllProducts = Products.objects.all()
    Categories = ProductCategory.objects.all()

    context = {
        "banners":banners,
        "banner_range":list,
        "AllProducts":AllProducts,
        "Categories":Categories
    }
    return render(request, 'home.html', context)


#cetegory based product__________________________________
def CategoryBasedProduct(request,pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    CategoryBasedProduct = category.ProductsCategoryRelatedName.all()
    context = {
        "CategoryBasedProduct":CategoryBasedProduct,
        "category":category,
    }
    return render(request, 'category_product.html', context)


#search product____________________________________________
def SearchProducts(request):
    searchKey = request.GET.get('search', None)
    context = {}

    searchProducts = Products.objects.filter(
        Q(title__icontains=searchKey)|
        Q(description__icontains=searchKey)|
        Q(price__icontains=searchKey)

    ).distinct()

    if searchProducts.count() !=0:

        context = {
            "searchProducts":searchProducts,
            "searchKey":searchKey,
        }
        return render(request, 'search_product.html', context)

    else:
        messages.warning(request,"No Product")
        return render(request, 'search_product.html', context)


#add feedback_______________________________________ 
@login_required(login_url='siungIn')
def productOrder(request, pk):
    OrderProduct = get_object_or_404(Products, pk=pk)
    
    if request.method == "POST" and request.user.is_authenticated: 
        ProductOrder.objects.create(
            user = request.user,
            Title = OrderProduct.title,
            Product = OrderProduct,
            Image = OrderProduct.image,
            Quantity = request.POST.get('qty'),
            Price = request.POST.get('price'),
            CustomerName = request.POST.get('full_name'),
            Email = request.POST.get('email'),
            PostOffice = request.POST.get('post_office'),
            Thana = request.POST.get('thana'),
            District = request.POST.get('district'),
            Zipcode = request.POST.get('zipcode'),
        )

        messages.success(request,"Thanks for your order.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        "OrderProduct":OrderProduct
    }
    return render(request, 'product_order.html', context)



#add feedback_______________________________________ 
@login_required(login_url='siungIn')
def ProductFeedBack(request,pk):
    product = get_object_or_404(Products, pk=pk)

    if request.method == "POST" and request.user.is_authenticated:
        try:
            ProductFeedback.objects.create(
                user=request.user,
                product=product,
                feedBACK=request.POST.get('product_experience'),
                rating=request.POST.get('product_rating'), 
            )
            messages.success(request,"Thanks for your feedback.")
            return redirect('ProductDetails', pk)
        except:
            messages.warning(request,"You've already given feedback.")
            return redirect('ProductDetails', pk)

    else:
        messages.warning(request,"Sorry we can't take your feedback.")
        return redirect('ProductDetails', pk)


#update feedback_____________________________________
def UpdateFeedback(request, pk):

    feedback = ProductFeedback.objects.get(pk=pk)
    product_id = feedback.product.id
    reviewers = feedback.user

    if request.method == "POST":
        form = UpdateFeedbackForm(request.POST)

        if form.is_valid():
            if request.user.is_superuser or reviewers.id == request.user.id:
            
                feedBACK = request.POST.get('UpdateFeedBACK')
                UpdateRating = request.POST.get('UpdateRating')

                feedback.feedBACK = feedBACK
                feedback.rating = UpdateRating
                
                feedback.save()
                messages.success(request, "Feedback is updated")

    return redirect('ProductDetails', product_id)

#feedback delete
def DeleteFeedback(request,pk):
    feedback = ProductFeedback.objects.get(pk=pk)
    product_id = feedback.product.id
    reviewers = feedback.user

    feedback = ProductFeedback.objects.get(pk=pk)
    product_id = feedback.product.id

    feedback.delete()
    messages.success(request,"Successfully your feedback deleted.")
    return redirect('ProductDetails', product_id)

#shopping cart
def ShoppingCart(request,pk):
    product = get_object_or_404(Products, pk=pk)
    try:
        if request.user.is_authenticated:
            ShopingCart.objects.create(
                User = request.user,
                Product = product
            )
            messages.success(request,"Successfully your product added to the cart.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        messages.warning(request,"You already added this product.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#my buy
def MyOrder(request):
    context = {}
    
    return render(request, 'my_order.html', context)

#customer order
def CustomerOrder(request):
    CustomerOrder = ProductOrder.objects.all()
    context = {
        "CustomerOrder":CustomerOrder
    }
    return render(request, 'customer_order.html', context)

#order tracking
def OrderTracking(request):
    OrderId = request.GET.get('orderTracking')
    if request.method=="GET":
        TrackingOrder=ProductOrder.objects.get(pk=OrderId)
        context = {
            "TrackingOrder":TrackingOrder,
        }
        return render(request, 'order_tracking_info.html',context)

    
    
    
