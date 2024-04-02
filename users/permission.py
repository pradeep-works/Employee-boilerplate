from rest_framework.permissions import IsAuthenticated

class IsAdminOnly(IsAuthenticated):
    '''
    Allow only Admin to do actions
    '''
    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()