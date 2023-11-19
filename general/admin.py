from django.contrib import admin
from django.contrib.auth.models import Group
from rangefilter.filters import DateRangeFilter
from general.filters import AuthorFilter, PostFilter
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter
from general.models import (
    Post,
    User,
    Comment,
    Reaction,
)


#admin.site.register(User)
admin.site.unregister(Group)

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
        #"friends",
        #"friends",
    )
    #fields = (
    #    "first_name",
    #    "last_name",
    #    "username",
    #    "password",
    #    "email",
    #    "is_staff",
    #    "is_superuser",
    #    "is_active",
    #    "friends",
    #    "date_joined",
    #    "last_login",
    #)
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    fieldsets = (
        (
            "Личные данные", {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            }
        ),
        (
            "Учетные данные", {
                "fields": (
                    "username",
                    "password",
                )
            }
        ),
        (
            "Статусы", {
                "classes": (
                    "collapse",
                ),
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active",
                )
            }
        ),
        (
            None, {
                "fields": (
                    "friends",
                )
            }
        ),
        (
            "Даты", {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            }
        )

    )
    search_fields = (
        "id",
        "username",
        "email",
        "last_name",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        ("date_joined", DateRangeFilter),
    )

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "get_body",
        "created_at",
        "get_comment_count",
    )

    readonly_fields = (
        "created_at",
    )
    search_fields = (
        "id",
        "title",
        "author__username",
    )
    list_filter = (
        AuthorFilter,
        ("created_at", DateRangeFilter),
    )
    def get_body(self, obj):
        max_length = 64
        if len(obj.body) > max_length:
            return obj.body[:61] + "..."
        return obj.body

    get_body.short_description = "body"

    def get_comment_count(self, obj):
        return obj.comments.count()

    get_comment_count.short_description = "comment count"

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("comments")

class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "post",
        "body",
        "created_at",
    )
    list_display_links = (
        "id",
        "body",
    )
    search_fields = (
        #"author__username",
        #"post__title",
        #"author",
        #"post",
        #"body"
    )
    list_filter = (
        PostFilter,
        AuthorFilter,
    )
    raw_id_fields = (
        "author",
    )
    autocomplete_fields = (
        "author",
        "post",
    )

class ReactionModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "post",
        "value",
    )
    list_filter = (
        PostFilter,
        AuthorFilter,
        ("value", ChoiceDropdownFilter),
    )
    autocomplete_fields = (
        "author",
        "post",
    )


admin.site.register(User, UserModelAdmin)
#admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Reaction, ReactionModelAdmin)