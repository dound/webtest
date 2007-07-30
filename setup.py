from setuptools import setup, find_packages
import sys, os

version = '0.9'

setup(name='WSGITest',
      version=version,
      description="Helper to test WSGI applications",
      long_description="""\
""",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='wsgi test unit tests web',
      author='Ian Bicking',
      author_email='ianb@colorstudy.com',
      url='http://pythonpaste.org/wsgitest/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'wsgiref',
        'WSGIObj',
      ],
      dependency_links=[
        'http://svn.pythonpaste.org/Paste/WSGIObj/trunk#egg=WSGIObj-dev',
      ],
      )
