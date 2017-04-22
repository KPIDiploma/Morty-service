from rest_framework import filters


class IsAuthorFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own patients.
    """

    def filter_queryset(self, request, queryset, view):
        return queryset.get(email=request.user.email).patients
        # return queryset.filter(email=request.user.email)