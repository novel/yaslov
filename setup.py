from distutils.core import setup

setup(
        name="yaslov",
        version="0.4",
        description="CLI client for https://tech.yandex.ru/dictionary/",
        author="Roman Bogorodskiy",
        author_email="bogorodskiy@gmail.com",
        packages=['yasl'],
        scripts=["yaslov"],
        requires=["pyxdg"],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'License :: Public Domain',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python',
        ]
)
