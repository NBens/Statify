import os
import markdown2
import re
import json

from jinja2 import Template

with open ("config.json", "r") as my_file:
    config = json.loads(my_file.read())

    
def loadTemplate(page):
    templatePath = "static/{}.html".format(page)
    with open(templatePath, "r") as my_file:
        template = Template(my_file.read())
    return template


def extractMeta(text):
    found = re.findall('<!--(.*?)-->', text)
    splitted = [[j.strip(" ") for j in t.split(":", 1)] for t in found]
    return splitted


def contentFiles():
    files = []
    for page in os.listdir("./content"):
        if (page[-3:] == ".md"):
            files.append(page)
    return files


def readFile(path):
    with open(path, 'r') as my_file:
        return my_file.read()


def writeFile(path, text):
    with open(path, 'w') as my_file:
        return my_file.write(text)


def dateFromFileName(file):
    r = re.search("([0-9]{4}\-([0-9]{2}|[0-9]{1})\-([0-9]{2}|[0-9]{1}))", file)
    return r.group(0)
    

def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)


files = contentFiles()
contents = []

for file in files:
    content = markdown2.markdown_path("./content/"+file)
    meta = extractMeta(content)

    ####
    title = ""
    subtitle = ""
    date = ""
    contentType = ""
    author = config["author"]
    ###
    for m in meta:
        if (m[0] == "Page"):
            title = m[1]
            contentType = "page"
            href = file[:-3] + ".html"
        elif (m[0] == "Subtitle"):
            subtitle = m[1]
        elif (m[0] == "Author"):
            author = m[1]
        elif (m[0] == "Title"):
            title = m[1]
            contentType = "blog"
            date = dateFromFileName(file)
            href = file.replace(date,date.replace("-", "/"), 1)
            href = href.replace("-", "/", 1)
            href = href[:-3]
            href = "Posts/" + href
    contents.append({"type": contentType, "title": title, "subtitle": subtitle, "author": author, "date": date, "href": href, "content": content})


indexTemplate = loadTemplate("index")
writeFile("output/index.html", indexTemplate.render(blogs = contents, config=config, dependencies=""))

postTemplate = loadTemplate("post")
pageTemplate = loadTemplate("page")

for c in contents:
    if (c.get("type") == "blog"):
        dependencies = "../../../../../"
        filePath = "output/" + c.get("href")
        makedir(filePath)
        writeFile(filePath + "/index.html", postTemplate.render(blog = c, blogs=contents, config=config, dependencies=dependencies))
    elif (c.get("type") == "page"):
        dependencies = ""
        filePath = "output/" + c.get("href")
        writeFile(filePath, pageTemplate.render(content = c, blogs = contents, config=config, dependencies=dependencies))
