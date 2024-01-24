from django import forms

from blogs.models import Blogs


class ModeratorBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title', 'body', 'on_published',)


class AdminBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('__all__')


class ModeratorOwnerBlogForm(forms. ModelForm):
    class Meta:
        model = Blogs
        exclude = ('count_view', 'user', 'slug',)


class OwnerBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        exclude = ('on_published', 'count_view', 'user', 'slug')





