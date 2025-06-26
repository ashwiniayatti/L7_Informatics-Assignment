from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from .models import Flavor, Ingredient, Suggestion, Cart, UserAllergy, Allergen
from django.contrib.auth.decorators import login_required
@login_required
def flavor_list(request):
    flavor = Flavor.objects.all()
    search = request.GET.get("search")
    if search:
        flavors = flavor.filter(name__icontains=search)
    return render(request, 'flavor_list.html', {'flavors': flavors})

@login_required
def add_to_cart(request, flavor_id):
    Cart.objects.get_or_create(user=request.user, flavor_id=flavor_id)
    return redirect('cart')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def suggest_flavor(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['description']
        Suggestion.objects.create(user=request.user, name=name, description=desc)
        messages.success(request, "Flavor suggestion submitted successfully!")

    my_suggestions = Suggestion.objects.filter(user=request.user)
    return render(request, 'suggestion.html', {
        'suggestions': my_suggestions
    })

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            messages.success(request, 'Login successful!')
            return redirect('flavor_list')  
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'login.html')
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, 'Logged out successfully.')
    return redirect('login') 
@login_required
def add_allergen(request):
    if request.method == 'POST':
        allergen_name = request.POST['name'].strip().capitalize()
        allergen_obj, created = Allergen.objects.get_or_create(name=allergen_name)
        
        if not UserAllergy.objects.filter(user=request.user, allergen=allergen_obj).exists():
            UserAllergy.objects.create(user=request.user, allergen=allergen_obj)
            messages.success(request, "Allergen added to your profile.")
        else:
            messages.info(request, "This allergen is already in your list.")

    my_allergens = UserAllergy.objects.filter(user=request.user)
    return render(request, 'cafe/add_allergen.html', {'my_allergens': my_allergens})
