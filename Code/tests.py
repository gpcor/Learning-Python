import json
import pprint
from urllib.request import urlopen

with urlopen('https://api.openweathermap.org/data/2.5/onecall?lat=36.85&lon=-76.35&exclude=hourly,minutely&units=imperial&appid=f473a02c2be1f952c67244c76c093f9e') as url:
    http_info = url.info()
    raw_data = url.read().decode(http_info.get_content_charset())
project_info = json.loads(raw_data)
result = {'headers': http_info.items(), 'body': project_info}
