from bottle import route, redirect
import os

modules = []

for filename in os.listdir('.'):
	modulename = address.split('.')[0]
	exec('import '+modulename+'.main as '+modulename)
	exec('import '+modulename+'.description as '+modulename+"_description")
	modules.append(modulename)
	
@route('/web-scraper-2017')
def main_page():
	out = "<li><b>Web Scraper</b></li>"
	for module in modules:
		out += "<li><a href = \"/web-scraper-2017/"+module+"\">"+module.replace("_"," ")+"</a></li>"
	return out
	
@route('/web-scraper-2017/<module>')
def module_page(module):
	description = eval(module+"_description")
	product = eval(module+"()")
	out = "<li><b>"+module.replace('_',' ')+"</b></li>"
	out += "<li>Description: "+description+"</li>"
	out += "<li>Product"+product+"</li>"
	return out