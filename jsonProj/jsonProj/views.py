from django.http import HttpResponse
from django.shortcuts import render #used for templates
from django.utils import simplejson #useed to basic json work
import urllib
import json

jsonURL = "http://www.azcentral.com/rss/feeds/fullaccess/ourpicks.json";

#get entire JSON
def getJSON(request):
	raw = urllib.urlopen(jsonURL)
	js = raw.readlines()
	return HttpResponse(js)

#get the headlines
def getHeadlines(request):
	raw = urllib.urlopen(jsonURL)
	js = raw.readlines()
	js_object = json.loads(js[0])

	#filter everything for headlines
	headlines = []
	for item in js_object['headlines']:
		headlines.append(item['headline'])

	return render(request, 'index.html', {'data': json.dumps(json.dumps(headlines))})