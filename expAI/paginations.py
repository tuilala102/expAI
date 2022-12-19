from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    max_page_size = 10000
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('totalPages',self.page.paginator.num_pages),
            ('previous', self.get_previous_link()),
            ('results', data)

        ]))

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    max_page_size = 1000