from django import template

register = template.Library()


@register.filter(name='results_big')
def results_big(value, arg):
    return value.filter(questionary_id=arg)