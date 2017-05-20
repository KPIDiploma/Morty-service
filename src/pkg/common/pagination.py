from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'

    def _split_link(self, link):
        link = link.split('?')
        try:
            page_num = link[1].split('page=')[1][0]
        except IndexError:
            return link[0]
        else:
            return '{}?page={}'.format(link[0], page_num)

    def get_paginated_response(self, data):
        next_link = self.get_next_link()
        if next_link:
            next_link = self._split_link(next_link)
        prev_link = self.get_previous_link()
        if prev_link:
            prev_link = self._split_link(prev_link)

        return Response({
            'next': next_link,
            'previous': prev_link,
            'count': self.page.paginator.count,
            'results': data
        })
