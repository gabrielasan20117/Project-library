from django.urls import path

from .views import (
    BooksList,
    BooksDashboard,
    AuthorList,
    CategoriesList,
    EditorialList,
    GenderList,
    ShelvesList,
)

urlpatterns = [
    path("books/dashboard/", BooksList.as_view(), name="books_bashboard"),
    path("books/", BooksDashboard.as_view(), name="books_list"),
    path("author/", AuthorList.as_view(), name="author_list"),
    path("category/", CategoriesList.as_view(), name="category_list"),
    path("editorial/", EditorialList.as_view(), name="editorial_list"),
    path("shelves/", ShelvesList.as_view(), name="shelves_list"),
    path("gender/", GenderList.as_view(), name="gender_list"),
]