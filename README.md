# ToDo_App_DRF
Django Rest Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django applications. It's a third-party package that complements Django by providing additional features and functionality specifically designed for building RESTful APIs.

1. Serialization:
DRF includes a serialization framework that allows you to convert complex data types, such as Django models or querysets, into native Python data types. Serializers also handle converting data back into complex types during deserialization.
2. ViewSets and Views:
DRF introduces the concept of ViewSets, which are classes that provide CRUD (Create, Read, Update, Delete) operations for your API. ViewSets can be easily mapped to URLs using DRF's routers.
3. Routers:
DRF provides routers to automatically generate URL patterns for your API based on the ViewSets you define. This makes it easy to create a RESTful API with minimal boilerplate code.
4. Authentication and Permissions:
DRF includes a variety of authentication classes and permission classes to control access to your API. It supports token-based authentication, session-based authentication, and more.
5. Pagination:
DRF includes built-in support for paginating large result sets. You can easily configure pagination settings to control how many items are returned in a single response.
6. Filters and Query Parameters:
DRF supports filtering and querying data through the use of query parameters. You can filter data based on various criteria, making it easy to implement search functionality.
7. Browsable API:
DRF provides a browsable API, which is a user-friendly interface that allows developers to interact with the API directly from a web browser. It's useful during development for testing and exploring the API.
8. Authentication and Permissions:
DRF includes a variety of authentication classes and permission classes to control access to your API. It supports token-based authentication, session-based authentication, and more.
9. Nested Serializers:
DRF supports nested serializers, allowing you to represent complex relationships between models in your API responses.
10. Serializer:
A Serializer in DRF is a class that defines how data should be converted to a format that can be easily rendered into JSON or other content types. It is used for validation and conversion of complex data types, such as Django models or custom data structures, into Python native data types that can be easily rendered into JSON.
11. ModelSerializer:
A ModelSerializer is a special type of serializer in DRF that is designed to work with Django models. It automatically generates fields based on the model's fields and includes default implementations for common tasks such as creating or updating model instances.

Important Links:-
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
pipenv install djangorestframework
python manage.py startapp apis

The list view of all items is at http://127.0.0.1:8000/apis/v1/
And the DetailView is at http://127.0.0.1:8000/apis/v1/1/
