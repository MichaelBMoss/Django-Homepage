import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def create_list():
    import glob
    all_html_files = glob.glob("templates/*.html")
    pages = []
    import os
    for entry in all_html_files:
        file_path = entry
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        if name_only != 'base':
            pages.append({
            "filename": "content/" + name_only + extension,
            "title": name_only,
            "output": "docs/" + name_only + extension,
            "link_location": name_only + extension,
            "link_box": '{{' + name_only + '_ph}}',
            })
    return pages

def create_links():    
    from jinja2 import Template
    links_template_string = '''
    {% for page in pages %}
        <a href="{{page.link_location}}">
                <span class="link {{page.link_box}}"> {{ page.title }}</span>
            </a>
    {% endfor %}
    '''
    links_template = Template(links_template_string)
    links = links_template.render(
        pages=create_list(),
    )
    return links

def index(request):
    print('called index')
    content_html = open("templates/index.html").read()
    links = create_links()
    context = {
    "content_ph": content_html,
    "links_ph": links,
        }
    return render(request, 'base.html', context)

def bio(request):
    print('called bio')
    content_html = open("templates/bio.html").read()
    links = create_links()
    context = {
    "content_ph": content_html,
    "links_ph": links,
        }
    return render(request, 'base.html', context)

def contact(request):
    print('called contact')
    content_html = open("templates/contact.html").read()
    links = create_links()
    context = {
    "content_ph": content_html,
    "links_ph": links,
        }
    return render(request, 'base.html', context)
    
def github(request):
    print('called github')
    links = create_links()
    response = requests.get('https://api.github.com/users/MichaelBMoss/repos')
    repos = response.json()
    context = {
    "links_ph": links,
    'github_repos': repos,
        }
    return render(request, 'github.html', context)



