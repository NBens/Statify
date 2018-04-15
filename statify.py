import os
import markdown2
import re
import json

from jinja2 import Template

with open ("config.json", "r") as my_file:
    config = json.loads(my_file.read())
    
with open("static/post.html", "r") as my_file:
    template = Template(my_file.read())

with open("static/page.html", "r") as my_file:
    pageTemplate = Template(my_file.read())


i = 0
finals = []
for page in os.listdir("./content"):
    i += 1
    if (page[-3:] == ".md"):
        content = markdown2.markdown_path("./content/"+page)
        found = re.findall('<!--(.*?)-->', content)
        splitted = [[j.strip(" ") for j in t.split(":")] for t in found]
        ###############################
        title = ""
        subtitle = ""
        author = config["author"]
        footer = config["footer"]
        pages = []
        pageOrNot = 0
        blogName = config["blog-name"]

        ###############################
        for item in splitted:
            if item[0] == "Title":
                title = item[1]
                dateList = str(page)
                dateList = dateList.split("-")
                fileName = list(dateList[3:])
                fileName = "-".join(fileName)
                fileName = fileName[:-3]
                date = dateList[0] + "-" + dateList[1] + "-" + dateList[2]
            elif item[0] == "Author":
                author = item[1]
            elif item[0] == "Subtitle":
                subtitle = item[1]
            elif item[0] == "Page":
                pageOrNot = 1
                pageTitle = item[1]
                pageHref = page[:-3] + ".html"
                pages.append({"title": pageTitle, "href": pageHref})
        if (pageOrNot == 0):
            dependencies = "../../../../"
            if not os.path.exists("output/Posts/" + dateList[0] + "/" + dateList[2] + "/" + fileName):
                os.makedirs("output/Posts/" + dateList[0] + "/" + dateList[2] + "/" + fileName)
            with open("output/Posts/" + dateList[0] + "/" + dateList[2] + "/" + fileName + "/index.html", "w") as my_file:
                my_file.write(template.render(footer=footer, dependencies = dependencies, blogName = blogName, title=title, subtitle=subtitle, content=content, author=author, date=date, facebook = config["facebook"], twitter = config["twitter"], github = config["github"]))
            finals.append("output/Posts/" + dateList[0] + "/" + dateList[2] + "/" + fileName + "/index.html")
        else:
            dependencies = ""
            with open("output/" + page[:-3] + ".html", "w") as my_file:
                my_file.write(pageTemplate.render(footer=footer, dependencies = dependencies, blogName = blogName, title=pageTitle, subtitle=subtitle, content=content, facebook = config["facebook"], twitter = config["twitter"], github = config["github"]))
            finals.append("output/" + page[:-3] + ".html")
    if (i == len(os.listdir("./content"))):
        toWrite = ""
        toWrite2 = ""
        for pageito in pages:
            toWrite += '\t\t\t<li class="nav-item">\n\t\t\t\t<a class="nav-link" href="{}">{}</a>\n\t\t\t</li>'.format(pageito["href"], pageito["title"])
            toWrite2 += '\t\t\t<li class="nav-item">\n\t\t\t\t<a class="nav-link" href="../../../../{}">{}</a>\n\t\t\t</li>'.format(pageito["href"], pageito["title"])
        for file in finals:
            with open (file, 'r') as myFy:
                data = myFy.read()
            with open (file, 'w') as myFy:
                if (len(file.split("/")) == 2):
                    myFy.write(data.replace("[NAV-BAR]", toWrite))
                else:
                    myFy.write(data.replace("[NAV-BAR]", toWrite2))
        

