from bottle import route, redirect, run
import os
import sys

modules = []

ignore = ["README.md","loadall.py", "__pycache__", "Web Scraper.ipynb", "Youtube Web Scraper.ipynb"]

for filename in os.listdir('.'):
        if filename in ignore:
                continue
        modulename = filename.split('.')[0]
        if modulename == "": continue
        print(modulename)
        exec('from '+modulename+' import main as '+modulename)
        exec('from '+modulename+' import description as '+modulename+"_description")
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
        out += "<li>Description: "+str(description)+"</li>"
        try:out += "<li>Product"+product+"</li>"
        except:out += "<li>No Product</li>"
        return out
	
if __name__ == "__main__":
	host = "0.0.0.0"
	port = 1234
	run(host = host, port = port)
