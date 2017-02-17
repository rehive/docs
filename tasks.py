from invoke import task
import yaml
import semver
from server.tasks import *

@task
def prepare(ctx):
    """
    Builds docs HTML
    """
    # check if container exists:
    result = ctx.run('echo $(docker ps -q -f name=docs_middleman_1)')
    if not result.stdout.strip():
        # build middle man if it doesn't exist
        ctx.run('docker-compose build middleman', echo=True)
    # build html
    ctx.run('docker run --rm -v $PWD/source:/usr/src/app/source -v $PWD/build:/usr/src/app/build '
            '-w /usr/src/app docs_middleman bundle exec middleman build --clean', echo=True)

@task
def build(ctx, tag):
    """
    Build project's docker image
    """
    prepare(ctx)
    cmd = 'docker build -f server/Dockerfile -t %s .' % tag
    ctx.run(cmd, echo=True)

@task
def run(ctx, image, port):
    """
    Run specified docker image on specified port
    """

    cmd = 'docker run -p {}:{} {}'.format(port, 80, image)
    ctx.run(cmd, echo=True)

@task
def push(ctx, config, version_tag):
    """
    Build, tag and push docker image
    """
    with open(config, 'r') as stream:
        config_dict = yaml.load(stream)

    image_name = config_dict['IMAGE'].split(':')[0]
    image = '{}:{}'.format(image_name, version_tag)

    build(ctx, image)
    ctx.run('docker push %s' % image, echo=True)

@task
def version(ctx, bump='patch'):
    """
    Returns incremented version number by looking at git tags
    """
    # Get latest git tag:
    result = ctx.run('git tag --sort=-v:refname', hide='both')
    latest_tag = result.stdout.split('\n')[0][1:]

    increment = {'prerelease': semver.bump_prerelease,
                 'patch': semver.bump_patch,
                 'minor': semver.bump_minor,
                 'major': semver.bump_major}

    incremented = increment[bump](latest_tag)
    print(incremented)

    return incremented


@task
def release(ctx, config, bump='patch'):
    """
    Bump version, push git tag, push docker image
    N.B. Commit changes first
    """

    if config[-5:] != '.yaml':
        config += '.yaml'

    # Use /server as base path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    server_dir_path = os.path.join(dir_path, 'server/')
    if not os.path.isabs(config):
        config = os.path.join(server_dir_path, config)

    with open(config, 'r') as stream:
        config_dict = yaml.load(stream)

    bumped_version = version(bump=bump)
    tag = 'v' + bumped_version
    comment = 'Version ' + bumped_version

    # Create an push git tag:
    ctx.run("git tag %s -m %s" % (tag, comment), echo=True)
    ctx.run("git push origin %s" % tag, echo=True)

    image_name = config_dict['IMAGE'].split(':')[0]

    push(ctx, config, tag)
    print('Release Info:\n'
          'Tag: {}\n'
          'Image: {}\n'.format(tag, image_name))

@task
def deploy(ctx, config, version_tag):
    """
    Updates kubernetes deployment to use specified version
    """

    if config[-5:] != '.yaml':
        config += '.yaml'

    # Use /server as base path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    server_dir_path = os.path.join(dir_path, 'server/')
    if not os.path.isabs(config):
        config = os.path.join(server_dir_path, config)

    with open(config, 'r') as stream:
        config_dict = yaml.load(stream)

    image_name = config_dict['IMAGE'].split(':')[0]
    image = '{}:{}'.format(image_name, version_tag)

    ctx.run('kubectl set image deployment/{} '
            'docs-server={} --namespace={}'.format(config_dict['PROJECT_NAME'],
                                                   image,
                                                   config_dict['NAMESPACE']), echo=True)
