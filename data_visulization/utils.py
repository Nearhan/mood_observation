import json
import time



def json_serilize_graph_data(queryset):
    data = []
    for o in queryset:
        x = time.mktime(o.date.timetuple())
        y = o.mood_value
        points = { 'x' : x, 'y': y}
        data.append(points)

    return json.dumps(data)
