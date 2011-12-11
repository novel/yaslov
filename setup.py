try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name = "yaslov",
        version = "0.1",
        description="CLI client for slovari.yandex.ru",
        author = "Roman Bogorodskiy",
        author_email = "bogorodskiy@gmail.com",
        scripts = ["yaslov"],
)
