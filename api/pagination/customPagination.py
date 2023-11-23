from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
  
  def get_page_size(self, request):
    self.page_size_query_param = 'page_size'

    if self.page_size_query_param:
      try:
        return request.query_params["page_size"]
      except (KeyError, ValueError):
        pass

    return self.page_size

  def get_paginated_response(self, data):
    return Response({
      'next_page': self.get_next_link(),
      'previous_page': self.get_previous_link(),
      'has_next_page': self.get_next_link() is not None, 
      'has_previous_page': self.get_previous_link() is not None , 
      'total_pages': self.page.paginator.num_pages,
      'current_page': self.page.number,
      'total_of_results': self.page.paginator.count,
      'results': data
    })
      
