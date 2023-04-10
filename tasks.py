from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
<<<<<<< HEAD

@task
def format(ctx):  # pylint: disable=redefined-builtin
    ctx.run("autopep8 --in-place --recursive src", pty=True)
=======
    
@task
def test(ctx):
    ctx.run("pytest src", pty=True)

>>>>>>> 72eb2cc3fcb7796b496cbc8ac08949d812478352

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
<<<<<<< HEAD
=======


@task
def format(ctx):  # pylint: disable=redefined-builtin
    ctx.run("autopep8 --in-place --recursive src", pty=True)
>>>>>>> 72eb2cc3fcb7796b496cbc8ac08949d812478352
