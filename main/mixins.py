from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class AllowedGroupsMixin(LoginRequiredMixin, UserPassesTestMixin):
    alllowed_groups = []
    
    def test_func(self):
        groups = self.request.user.groups.all()
        for group in groups:
            if group.name in self.allowed_groups:
                return True
        return False    

