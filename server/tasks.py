import yaml
import os
from invoke import task


def format_yaml(template, config):
    # Replace in ${ENV_VAR} in template with value:
    formatted = template
    for k, v in config.items():
        formatted = formatted.replace('${%s}' % k, v)
    return formatted

@task
def templater(ctx, config, template='kubernetes/templates/all-in-one.yaml'):
    """ Creates deployment setup for given config file"""

    if config[-5:] != '.yaml':
        config += '.yaml'

    # Get path of tasks.py file to allow independence from CWD
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if not os.path.isabs(config):
        config = os.path.join(dir_path, config)
    if not os.path.isabs(template):
        template = os.path.join(dir_path, template)

    with open(config, 'r') as stream:
        config_dict = yaml.load(stream)

    with open(template, 'r') as myfile:
        template_str = myfile.read()

    formatted = format_yaml(template_str, config_dict)
    output_dir = os.path.join(dir_path, 'kubernetes', config_dict['NAMESPACE'])
    output_path = os.path.join(output_dir, 'all-in-one.yaml')
    if os.path.isfile(output_path):
        print('Deployment config already exists. Aborting.')
    else:
        os.mkdir(output_dir)
        with open(output_path, 'w') as myfile:
            myfile.write(formatted)