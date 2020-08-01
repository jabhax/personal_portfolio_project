from django.shortcuts import render, get_object_or_404
from .models import Project
from blog.models import Blog


SKILLS = {
    'prog_langs': {
        'primary': ['Python', 'Java', 'C/C++', 'JavaScript'],
        'secondary': ['HTML/5', 'CSS/3', 'Bootstrap', 'Materialize'],
        'other': ['XML', 'PHP', 'JSON', 'Unix/Linux/Bash', 'MATLAB']
   },
    'frameworks': {
        'mvc': ['Django', 'Flask', 'Angular.js'],
        'js': ['JQuery', 'D3.js', 'Nodejs/npm', 'Express.js'],
        'testing': ['Appium', 'Selenium']
    },
    'databases': {
        'primary': ['PostgreSQL', 'MongoDB'],
        'secondary': ['MySQL']
    },
    'environments': {
        'testing': ['JUnit', 'TestNG', 'unittest (python)'],
        'ci-cd': ['Jenkins', 'Jira', 'Git', 'SVN'],
        'virtual': ['VM/Containers: VirtualBox', 'VMWare', 'Docker Container', 'Kubernetes Pods'],
        'other': ['Vi/Vim', 'Eclipse', 'Sublime', 'Atom', 'LaTex']
    }
}

projects = Project.objects.all()
projects_2 = projects[6:] 
blogs = Blog.objects.order_by('-timestamp')[:6]

def index(request):
    content = parse_skills_content()
    data_dict = {
        'projects': projects,
        'projects_2': projects_2,
        'blogs': blogs,
        'langs': content['languages'],
        'frameworks': content['frameworks'],
        'databases': content['databases'],
        'environments': content['environments']
    }
    return render(request, 'portfolio/index.html', data_dict)

def all_blogs(request):
    blogs = Blog.objects.order_by('-timestamp')
    data_dict = {
        'blogs': blogs
    }
    return render(request, 'portfolio/blogs.html', data_dict)

def group_items(items):
    rotate_str = ''
    n = len(items)
    if n == 1:
        return items[0]
    for i in range(n-1):
        item = items[i]
        rotate_str += (items[i] + ' | ')
    rotate_str += items[n-1]
    return rotate_str

def parse_langs():
    langs = ''
    langs += group_items(SKILLS['prog_langs']['primary']) + ','
    langs += group_items(SKILLS['prog_langs']['secondary']) + ','
    langs += group_items(SKILLS['prog_langs']['other'])
    return langs

def parse_frameworks():
    frameworks = ''
    frameworks += group_items(SKILLS['frameworks']['mvc']) + ','
    frameworks += group_items(SKILLS['frameworks']['js']) + ','
    frameworks += group_items(SKILLS['frameworks']['testing'])
    return frameworks

def parse_envs():
    environments = ''
    environments += group_items(SKILLS['environments']['testing']) + ','
    environments += group_items(SKILLS['environments']['ci-cd']) + ','
    environments += group_items(SKILLS['environments']['virtual']) + ','
    environments += group_items(SKILLS['environments']['other'])
    return environments

def parse_dbs():
    databases = ''
    databases += group_items(SKILLS['databases']['primary']) + ','
    databases += group_items(SKILLS['databases']['secondary']) + ','
    return databases

def parse_skills_content():
    content = {}
    # build primary langs string for text-rotating ul li tags
    content['languages'] = parse_langs()
    # build frameworks string for text-rotating ul li tags
    content['frameworks'] = parse_frameworks()
    # build environments string for text-rotating ul li tags
    content['environments'] = parse_envs()
    # build databases string for text-rotating ul li tags
    content['databases'] = parse_dbs()
    return content
