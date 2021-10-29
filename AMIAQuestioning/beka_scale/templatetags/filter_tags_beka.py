from django import template

register = template.Library()


@register.filter(name='results_beka')
def results_beka(value, arg):
    return value.filter(beka_scale_id=arg)