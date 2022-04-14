from re import X
import urllib
from django.shortcuts import  render
from contents.models import Content
import requests

def get_contents(request):
    all_contents = {}
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        keyword = urllib.parse.quote(keyword)
        api_key = '6%2B5mrhfOlLaSxBRdUTJHl8Y7e7yURzgyJWjob%2BXgC%2BJgdjZCYrHb%2Fro6Fv61BA6ngjv6lzwoq8XCh660UfLdOQ%3D%3D'

        url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchKeyword?serviceKey=" + api_key + "&MobileApp=AppTest&MobileOS=ETC&pageNo=1&numOfRows=" + '10' + "&listYN=Y&arrange=A&contentTypeId=12&keyword=" + keyword + "&_type=json"

        response = requests.get(url)
        data = response.json()
        print(data)
        contents = data['response']['body']['items']['item']

        for i in contents:
            try:
                content_data = Content(
                    title = i['title'],
                    addr1 = i['addr1'],
                    firstimage = i['firstimage'],
                    mapx = i['mapx'],
                    mapy = i['mapy']
                )
            except KeyError:
                content_data = Content(
                    title = i['title'],
                    addr1 = i['addr1'],
                )
            content_data.save()
        all_contents = Content.objects.all().order_by('-id')

    return render (request, 'get_content.html', { "all_contents": all_contents })

def content_detail(request, id):
    content = Content.objects.get(id = id)
    print(content)
    return render (request, 'content_detail.html', {'content': content})