from django.contrib import admin
from .models import BoxReturn
from profiles.models import UserProfile
from .models import Feedback


@admin.register(BoxReturn)
class BoxReturnAdmin(admin.ModelAdmin):
    list_display = ('user', 'number_of_boxes_returned', 'status', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ['user__user__username']
    actions = ['approve_box_returns', 'reject_box_returns']

    def approve_box_returns(self, request, queryset):
        for box_return in queryset:
            if box_return.status == 'approved':
                # Skip already approved box returns
                continue
            
            # Update the status to 'approved'
            box_return.status = 'approved'
            box_return.save()

            user = box_return.user.user  # Access the user_profile associated with the box return            
            self.message_user(request, f'Successfully approved {box_return.number_of_boxes_returned} box returns for {user.username}.')
    
    def reject_box_returns(self, request, queryset):
        for box_return in queryset:
            if box_return.status == 'rejected':
                # Skip already rejected box returns
                continue
            
            # Update the status to 'rejected'
            box_return.status = 'rejected'
            box_return.save()
            
            self.message_user(request, f'Successfully rejected {box_return.number_of_boxes_returned} box returns.')



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'created_at', 'resolved')
    list_filter = ('resolved', 'created_at')
    search_fields = ['user__username', 'subject']
    actions = ['mark_resolved', 'mark_unresolved']

    def mark_resolved(self, request, queryset):
        queryset.update(resolved=True)
        self.message_user(request, f'Marked {queryset.count()} feedback submissions as resolved.')

    def mark_unresolved(self, request, queryset):
        queryset.update(resolved=False)
        self.message_user(request, f'Marked {queryset.count()} feedback submissions as unresolved.')
