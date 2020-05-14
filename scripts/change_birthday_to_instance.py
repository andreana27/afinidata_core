from instances.models import AttributeValue
from dateutil import parser
import re

pattern = '(((0[1-9]|[12][0-9]|3[01])([/])(0[13578]|10|12)([/])(\d{4}))|(([0][1-9]|[12][0-9]|30)([/])(0[469]|11)([/])(\d{4}))|((0[1-9]|1[0-9]|2[0-8])([/])(02)([/])(\d{4}))|((29)(\.|-|\/)(02)([/])([02468][048]00))|((29)([/])(02)([/])([13579][26]00))|((29)([/])(02)([/])([0-9][0-9][0][48]))|((29)([/])(02)([/])([0-9][0-9][2468][048]))|((29)([/])(02)([/])([0-9][0-9][13579][26])))'

for av_value in AttributeValue.objects.filter(attribute__name='birthday'):
    r = re.match(pattern, av_value.value)
    if(r):
        date = parser.parse(av_value.value)
        print(av_value.value)
        av_value.value = date
        av_value.save()
        print(av_value.value)
