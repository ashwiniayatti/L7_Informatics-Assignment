# L7 Informatics Assignment

This is a Django application for managing an ice cream parlor's seasonal flavors, ingredient inventory, and customer suggestions.

## Features

  Seasonal flavor offerings management
  Ingredient inventory tracking
  Customer flavor suggestions and allergy concerns
  Shopping cart functionality
  Search and filter capabilities for flavors
  Allergen management

## Prerequisites

  Python 3.9+
  Docker (optional)

## Installation


### Without Docker

1. Clone the repository:
   ```bash
   git git clone https://github.com/ashwiniayatti/L7_Informatics-Assignment.git
   cd ice_cream_parlor
   
2. Create and activate a virtual environment:
    ```bash
    python  m venv venv

3. Install dependencies:
    ```bash
    pip install  r requirements.txt

4. Run migrations:
    ```bash    
     python manage.py makemigrations
     python manage.py migrate
#### python manage.py createsuperuser(optional)# already created super user username admin password  admin (You can login to admin dashboard with this credential  ex:http://127.0.0.1:8000/admin)

5. Run the development server:
    ```bash
     python manage.py runserver
#### Access the application at http://localhost:8000

### With Docker 
1. Build the Docker image
    ```bash
     docker compose build
2. Run the containers
    ```bash
     docker compose up

## Test Steps

1. Log in using your credentials.(you can also add any user from admin panel in customuser table admin credential is [username:admin ,password:admin](http://127.0.0.1:8000/admin/) add user and come to login page and you can access the other pages )

2. Navigate to the flavors page and browse the list.

3. Use the search bar to filter flavors by name.

4. Add a flavor to your cart.

5. View the cart to confirm items.

6. Submit a new flavor suggestion.

7. Add allergens and confirm they appear in your list.
## ORM Abstractions Used

- `Flavor.objects.all()`: Retrieve all flavors.
- `Cart.objects.get_or_create(user=request.user, flavor_id=flavor_id)`: Add to cart without duplicates.
- `Suggestion.objects.create(...)`: Insert new flavor suggestions.
- `UserAllergy.objects.filter(user=request.user).exists()`: Check for existing allergens.


## Code Structure

- `views.py`: Contains the main application logic (login, flavor list, cart, suggestions).
- `models.py`: Defines `Flavor`, `Suggestion`, `Cart`, `Allergen`, etc.
- `templates/`: HTML templates for rendering views.
- `urls.py`: Maps URL paths to views.


