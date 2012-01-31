from django import template

register = template.Library()

#@register.filter(name="team1_result")
def team1_result(obj, quart):
    result = 0
    quarts = ['quart_1_d1', 'quart_2_d1', 'quart_3_d1', 'quart_4_d1']
    for loop in range(len(quarts)):
        if loop >= quart:
            break
        quart_result = getattr(obj, quarts[loop])
        if quart_result == None:
            continue
        result += quart_result
    return result    

def team2_result(obj, quart):
    result = 0
    quarts = ['quart_1_d2', 'quart_2_d2', 'quart_3_d2', 'quart_4_d2']
    for loop in range(len(quarts)):
        if loop >= quart:
            break
        quart_result = getattr(obj, quarts[loop])
        if quart_result == None:
            continue
        result += quart_result
    return result 

register.filter('team1_result', team1_result)
register.filter('team2_result', team2_result)
