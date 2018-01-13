from rest_framework import pagination

class StandardResultPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_description = 'page_size'
    max_page_size = 1000