from jinja2 import Template


with open("static/blog.html", "r") as my_file:
    template = Template(my_file.read())
with open("new.html", "w") as my_file:
    my_file.write(template.render(title="Title", content="Content"))
