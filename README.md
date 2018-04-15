# simplesite
Simple lightweight static site generator, Powered by Python 3 &amp; Jninja2

# ToDo:
* Improve the code
* Serve Online Editor (Wysiwyg to Markdown)
* Multiple Themes & Templates
* Auto build for Linux
* Add support to other markup languages
* Tags & Categories

# Dependencies:
* markdown2
* Jinja2
* Flask (Not Currently)

# Usage:
Simply open contents folder, create a new md file
#### New Article:
If you want to write a new article, name the file something like "YYYY-DD-MM-Topic-Or-Title.md"
And start the file with this: 

    <!-- Title: The Title Of My Article -->
	
Then write your content in markdon format (other formats will be supported soon)
You can add subtitles using:

	<!-- Subtitle: Subtitle For My Article -->

If you want to set a new author start the file with:

	<!-- Author: Jhon Doe -->

#### New Page:
Now if you want to create a new page (example of about.html in my blog)
Create a new md file , something like about.html , or contact.html
And start it with the following: 

	<!-- Page: Page Title -->
	
Know that Page Title will be displayed in the navbar, so make sure to choose a meaningful small page title.
You can also set Subtitles , Just like articles using:

	<!-- Subtitle: Subtitle For My Page -->
	
#### Github , Facebook, Twitter, Footer and Blog Information: 
Edit config.json

Then Run statify.py :)