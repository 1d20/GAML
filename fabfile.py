from fabric.api import local


def updatedb():
	local('pip install -r requirements.txt')
	local('./manage.py syncdb')
	local('./manage.py migrate')

def clear():
	local('find . -name \*.pyc -delete') #delete all precompiled *.pyc files in project

def all():
	clear()
	updatedb()

def run():
	local('./manage.py runserver --insecure')

def scrap():
	local('music_scrap/music_scrap/scrapy crawl billboard --set FEED_URI=scraped_data.csv --set FEED_FORMAT=csv')
