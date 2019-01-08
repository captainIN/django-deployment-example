from django import template

register = template.Library()

def cut(string, arg):
    return string.replace(arg, '')

register.filter('cut', cut)
