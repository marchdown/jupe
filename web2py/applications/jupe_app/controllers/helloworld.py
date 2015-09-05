def helloworld():
    return "Hello World!"

def hello1():
    """ simple page without template """

    return 'Hello World'


def hello2():
    """ simple page without template but with internationalization """

    return T('Hello World')


def hello3():
    """ page rendered by template simple_examples/index3.html or generic.html"""

    return dict(messagele='fie foo fukm')
