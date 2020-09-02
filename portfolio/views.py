from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Project
from blog.models import Blog


SKILLS = {
    'prog_langs': {
        'primary': ['<b>Python</b>', '<b>Java</b>', 'JavaScript (ES6+)', 'C/C++'],
        'secondary': ['<b>HTML/5</b>', '<b>CSS/3</b>', 'Bootstrap', 'Materialize'],
        'other': ['XML', 'PHP', 'JSON', 'Unix/Linux/<b>Bash</b>', 'MATLAB']
   },
    'frameworks': {
        'mvc': ['<b>Angular/Angular.js</b>', '<b>Django</b>', 'Flask', 'React'],
        'js': ['<b>TypeScript</b>', 'JQuery', 'D3.js', 'Nodejs/npm', 'Express.js'],
        'testing': ['Appium', 'Selenium']
    },
    'databases': {
        'primary': ['PostgreSQL', 'MongoDB', 'Firebase'],
        'secondary': ['MySQL', 'SQLite']
    },
    'environments': {
        'testing': ['JUnit', 'TestNG', 'unittest (python)'],
        'ci-cd': ['Jenkins', 'Jira', 'Git', 'SVN'],
        'virtual': ['VM/Containers: VirtualBox', 'VMWare', '<b>Docker Container</b>', 'Kubernetes Pods'],
        'other': ['<b>Vi/Vim</b>', 'Eclipse', 'Sublime', '<b>Atom</b>', 'LaTex']
    }
}

EXPERIENCES = [
    {
        'title': 'Software Engineer',
        'company_name': 'Datera, Inc.',
        'start_date': 'April 2017',
        'end_date': 'Present',
        'responsibilities': [
            ('Development for internal framework APIs to communicate with '
             'clusters/storage nodes.'),
            ('Owned 2-3 core product features from a QA & Release standpoint; '
             'Point-of-Contact for the life-cycle of nodes/clusters and '
             'node-data mappings.'),
            ('Enforced good ethics & clean coding standards using PEP-8, '
             'Flake8, Pylint, and TDD; daily peer-code review, bug '
             'regression/triaging & automation, OOP & architectural design '
             'within internal product libraries.'),
            ('Proficient in iSCSI, cloud clusters, iops, replication, and '
             'application/data driven practices; worked in various development'
             ' stacks, data layers, OS-level architectures, Cloud-related '
             'infrastructures: clusters, storage nodes, iops, iSCSI layer, '
             'data-inconsistencies, data-replication, and data-orchestration.')
        ]
    },
    {
        'title': 'Software Developer',
        'company_name': 'Wells Fargo Bank',
        'start_date': 'July 2016',
        'end_date': 'March 2017',
        'responsibilities': [
            ('Design, architect, and develop an automation testing framework '
             'from the ground-up using Java/EE, Appium, Selenium, JUnit, '
             'TestNG, SVN, Maven.'),
            ('Leveraged the framework being developed to create and '
             'continuously integrate automated scripts on browsers, Android, '
             'iOS, Windows mobile devices for the Wells Fargo banking app.'),
            ('Helped Wells Fargo cut down on manual QA cost through the Testing'
             '& Automation Framework.'),
            ('Joined with one other junior member and expanded the team from '
             'size two to ten by the end.')
        ]
    },
    {
        'title': 'Developer Intern',
        'company_name': 'Xactly Corp.',
        'start_date': 'January 2016',
        'end_date': 'June 2016',
        'responsibilities': [
            ('Developed a full-stack web-based application for form creation, '
             'management, submission, and result visualization which features '
             'a dynamic UI form generator; designed to meet the demands of '
             'Xactly Administrators, Managers, and Employees.'),
            ('Agile development using MEAN stack with JQuery, MySQL.'),
            ('Expedited development process using Agile, scrum and burn-up '
             'charts under Xactly’s mentorship.')
        ]
    },
    {
        'title': 'Technician Lead & Supervisor',
        'company_name': 'ResNet (UCSC)',
        'start_date': 'September 2013',
        'end_date': 'April 2016',
        'responsibilities': [
            ('Worked as a full-time student to interview, train, and manage '
             '20+ university staff members in IT computer repair, network '
             'troubleshooting, and customer relationship management.'),
            ('Expedited and delegated the repairs of dozens of computers '
             'within the office with various issues including virus '
             'infections, re-formats, and replacing malfunctioning hardware '
             'on a daily basis.'),
            ('Effectively resolved hundreds of campus wide network outages '
             'using tools and skills that identified disruptive network '
             'behaviors.')
        ]
    }
];


all_projects = Project.objects.all()
projects = None
projects2 = all_projects[:6] 
blogs = Blog.objects.order_by('-timestamp')[:6]

def index(request):
    content = parse_skills_content()
    paginator = Paginator(all_projects, 6) # Show 3 projects per page
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projects = paginator.page(paginator.num_pages)

    data_dict = {
        'projects': projects,
        'projects2': projects2,
        'blogs': blogs,
        'langs': content['languages'],
        'frameworks': content['frameworks'],
        'databases': content['databases'],
        'environments': content['environments'],
        'experiences': EXPERIENCES[:2],
        'experiences2': EXPERIENCES[2:]
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
