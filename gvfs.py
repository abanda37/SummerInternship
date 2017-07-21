import click


@click.group()
def cli():
    pass

# ############################################ Things to check on ######################################################
# DONE - Make sure to go back and check if required or default is needed - in all arguments of the commands.
# DONE - For the Help command, can I simply make a variable to hold all of helps output and use it when needed?

# DO-LATER - Ask if I should add the help option to all commands, more specifically how to edit it. (Also Google it.)
# Ask if 'Repository URL' and 'Enlistment Root Path' would be arguments and how to implement them.
# For version, where will I be getting the version from?

# Should is_flag=True come before default and required?
# Should I still do comments? Since it is mostly already documented. 
# Should I leave Repository URL and Enlistment Root Path?
# Should I set default to 'Informational' and 'Any' for the other defaults - 'Informational' is actually a choice
# ######################################################################################################################


# Clone command and its options
@cli.command(help='Clone a Git repo and mount it as a GVFS virtual repo')
@click.option('--cache-server-url', required=False, default='',
              help='(Default: ) Defines the url of the cache server.')
@click.option('-b', '--branch', required=True,
              help='Branch to checkout after clone.')
@click.option('--single-branch', is_flag=True, required=False, default=False,
              help='(Default: false) Use this option to only download metadata for the branch that will be checked out')
@click.option('--no-mount', is_flag=True, required=False, default=False,
              help='(Default: false) Use this option to only clone, but not mount the repo')
@click.option('--no-prefetch', is_flag=True, required=False, default=False,
              help='(Default: false) Use this option to not prefetch commits after clone')
@click.option('--version', is_flag=True, required=False,
              help='Display version information.')  # Add a default
# @click.argument('Repository URL', default='', required=True,)
# @click.argument('Enlistment Root Path', default='', required=True)
def clone(cache_server_url, branch, single_branch, no_mount, no_prefetch, version):
    if cache_server_url:
        click.echo('clone cache')
    if branch:
        click.echo('clone branch')
    if single_branch:
        click.echo('clone single branch')
    if no_mount:
        click.echo('clone no mount')
    if no_prefetch:
        click.echo('clone no prefetch')
    if version:
        click.echo('clone version')
    # if repository:
    #     click.echo('clone repository URL')


# Dehydrate command and its options
@cli.command(help='EXPERIMENTAL FEATURE - Fully dehydrate a GVFS repo')
@click.option('--confirm', is_flag=True, required=False, default=False,
              help='(Default: false) Pass in this flag to actually do the dehydrate')
@click.option('--no-status', is_flag=True, required=False, default=False,
              help='(Default: false) Skip git status before dehydrating')
@click.option('--version', is_flag=True, required=False,
              help='Display version information.')  # Add a default
def dehydrate(confirm, no_status, version):
    if confirm:
        click.echo('dehydrate confirm')
    if no_status:
        click.echo('dehydrate no-status')
    if version:
        click.echo('dehydrate version')


# Diagnose command and its options
@cli.command(help='Diagnose issues with a GVFS repo')
@click.option('--version', is_flag=True, required=False,
              help='Display version information.')  # Add a default
def diagnose(version):
    if version:
        click.echo('diagnose version')


# Log command and its options
@cli.command(help='Show the most recent GVFS log')
@click.option('--version', is_flag=True, required=False,
              help='Display version information.')  # Add a default
def log(version):
    if version:
        click.echo('log version')


# Mount command and its options
@cli.command(help='Mount a GVFS virtual repo')
@click.option('-v', '--verbosity', required=False, default=False,   # change default to Informational
              help='(Default: Informational) Sets the verbosity of console logging. Accepts Verbose, Informational, '
                   'Warning, Error')
@click.option('-k', '--keywords', required=False, default=False,    # change default to Any
              help='(Default: Any) A CSV list of logging filter keywords. Accepts: Any, Network')
@click.option('-d', '--debug-window', is_flag=True, required=False, default=False,
              help='(Default: false) Show the debug window. By default, all output is written to a log file and no '
                   'debug window is shown.')
@click.option('--version', is_flag=True, required=False,
              help='Display version information.')  # Add a default
def mount(verbosity, keywords, debug_window, version):
    if verbosity:
        click.echo('log verbosity')
    if keywords:
        click.echo('log keywords')
    if debug_window:
        click.echo('log debug-window')
    if version:
        click.echo('log version')


# Prefetch command and its options
@cli.command(help='Prefetch remote objects for the current head')
@click.option('-f', '--folders', required=False, default='',
              help='(Default: ) A semicolon-delimited list of paths to fetch')
@click.option('--folders-list', required=False, default='',
              help='(Default: ) A file containing line-delimited list of paths to fetch')
@click.option('-c', '--commits', is_flag=True, required=False, default=False,
              help='(Default: false) Prefetch the latest set of commit and tree packs')
@click.option('--verbose', is_flag=True, required=False, default=False,
              help='(Default: false) Show all outputs on the console in addition to writing them to a log file')
@click.option('--version',  is_flag=True, required=False,
              help='Display version information.')  # Add a default
def prefetch(folders, folders_list, commits, verbose, version):
    if folders:
        click.echo('prefetch folders')
    if folders_list:
        click.echo('prefetch folders-list')
    if commits:
        click.echo('prefetch commits')
    if verbose:
        click.echo('prefetch verbose')
    if version:
        click.echo('prefetch version')


# Status command and its options
@cli.command(help='Get the status of the GVFS virtual repo')
@click.option('--version', is_flag=True, required=False,
              help='Display version information.')  # Add a default
def status(version):
    if version:
        click.echo('status version')


# Unmount command and its options
@cli.command(help='Unmount a GVFS virtual repo')
@click.option('--version', is_flag=True, required=False,
              help='Display version information.')  # Add a default
def unmount(version):
    if version:
        click.echo('unmount version')


# Help command and its options
@cli.command(help='Display more information on a specific command ')
@click.pass_context
def help(ctx):
    click.echo(ctx.parent.get_help())


# Version command
@cli.command(help='Display version information ')
def version():
    click.echo('This will print the version info.')


if __name__ == '__main__':
    cli()