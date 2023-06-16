from invoke import task

@task
def run(c, port):
    c.run("python manage.py runserver " + port)


@task
def updatereqs(c):
    c.run("pip install -r ../requirements.txt")


@task
def savereqs(c):
    c.run("pipreqs --savepath ../requirements.txt --ignore ~jango")


@task
def flake(c):
    #c.run("flake8 .")
    c.run("flake8 --format=pylint --output-file=../code_analysis.txt .")




