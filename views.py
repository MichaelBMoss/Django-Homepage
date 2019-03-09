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
    links = create_links()
    index_links = links.replace("{{index_ph}}", 'box')
    context = {
    "links_ph": index_links,
        }
    return render(request, 'index.html', context)

def bio(request):
    print('called bio')
    links = create_links()
    bio_links = links.replace("{{bio_ph}}", 'box')
    context = {
    "links_ph": bio_links,
        }
    return render(request, 'bio.html', context)

def contact(request):
    print('called contact')
    links = create_links()
    contact_links = links.replace("{{contact_ph}}", 'box')
    context = {
    "links_ph": contact_links,
        }
    return render(request, 'contact.html', context)
    
def github(request):
    print('called github')
    links = create_links()
    github_links = links.replace("{{github_ph}}", 'box')
    response = requests.get('https://api.github.com/users/MichaelBMoss/repos')
    repos = response.json()
    context = {
    "links_ph": github_links,
    'github_repos': repos,
        }
    return render(request, 'github.html', context)



