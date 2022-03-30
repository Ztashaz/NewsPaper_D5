from django import template

register = template.Library()

@register.filter(name='censor')

def censor(value):
    censor_list = ['bbb', 'ttt', 'zzz', 'lake', 'part', 'sport']

    for word in censor_list:
        value = value.replace(word[1:], '*' * (len(word)-1))
    return value
