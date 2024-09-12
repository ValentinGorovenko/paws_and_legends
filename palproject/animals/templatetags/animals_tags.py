from django import template

from animals.models import Category

register = template.Library()


@register.inclusion_tag("animals/list_categories.html")
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected}
