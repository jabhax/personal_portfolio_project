from django.shortcuts import render, get_object_or_404
from .models import Project
from blog.models import Blog


projects = Project.objects.all()
blogs = Blog.objects.order_by('-timestamp')[:6]

primary_languages = ['Python', 'Java', 'C/C++', 'JavaScript']
secondary_languages = ['HTML/5', 'CSS/3', 'Bootstrap', 'Materialize']
other_languages = ['XML', 'PHP', 'JSON', 'Unix/Linux/Bash shell scripting', 'MATLAB']

mvc_frameworks = ['Django', 'Flask', 'Angular.js']
js_frameworks = ['JQuery', 'D3.js', 'Nodejs/NPM', 'Express.js']
testing_frameworks = ['Appium', 'Selenium']

dbs = ['PostgreSQL', 'MongoDB', 'MySQL']

testing_envs = ['Eclipse', 'JUnit', 'TestNG', 'unittest (python)']
ci_cd_envs = ['Jenkins', 'Jira', 'Git', 'SVN']
virtual_envs = ['VM/Containers: VirtualBox', 'VMWare', 'Docker Container', 'Kubernetes Pods']
other_envs = ['LaTex', 'Servicenow']


def index(request):
    content = parse_skills_content()
    data_dict = {
        'projects': projects,
        'blogs': blogs,
        'langs': content['languages'],
        'frameworks': content['frameworks'],
        'databases': content['databases'],
        'environments': content['environments']
    }
    
    return render(request, 'portfolio/index.html', data_dict)

def group_items(items):
    rotate_str = ''
    n = len(items)
    for i in range(n-1):
        item = items[i]
        rotate_str += (items[i] + ' | ')
    rotate_str += items[n-1]
    return rotate_str

def parse_skills_content():
    content = {}

    # build primary langs string for text-rotating ul li tags
    langs = ''
    langs += group_items(primary_languages) + ','
    langs += group_items(secondary_languages) + ','
    langs += group_items(other_languages)
    content['languages'] = langs
    print(content['languages'])
   
    # build frameworks string for text-rotating ul li tags
    frameworks = ''
    frameworks += group_items(mvc_frameworks) + ','
    frameworks += group_items(js_frameworks) + ','
    frameworks += group_items(testing_frameworks)
    content['frameworks'] = frameworks
    print(content['frameworks'])

    databases = ''
    databases += group_items(dbs)
    content['databases'] = databases

    # build string for text-rotating ul li tags
    environments = ''
    environments += group_items(testing_envs) + ','
    environments += group_items(ci_cd_envs) + ','
    environments += group_items(virtual_envs) + ','
    environments += group_items(other_envs)
    content['environments'] = environments
    print(content['environments'])
    return content
