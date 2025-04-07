from invoke import task

@task
def start(ctx):
    ctx.run("python src/app.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task
def lint(ctx):
    ctx.run("pylint src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")