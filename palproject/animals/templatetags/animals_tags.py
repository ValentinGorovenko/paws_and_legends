from django import template

from animals.models import Category, TagPost

register = template.Library()


@register.inclusion_tag("animals/list_categories.html")
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag("animals/list_tag.html")
def show_all_tags(cat_selected=0):
    return {"tags": TagPost.objects.all()}
