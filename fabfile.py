from fabric.api import local
from jinja2 import Environment, FileSystemLoader


template_env = Environment(loader=FileSystemLoader('.'))


def build():
    template = template_env.get_template('source/index.html')
    rendered_template = template.render()
    with open('decks/index.html', 'wt') as fh:
        fh.write(rendered_template)
        #fh.write(bytes(rendered_template, 'utf-8'))

def publish():
    build()
    local('ghp-import -p decks')
