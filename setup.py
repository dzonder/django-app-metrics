import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='django-app-metrics',
    version='0.9.0dz',
    description='django-app-metrics is a reusable Django application for tracking and emailing application metrics (this is a fork)',
    long_description=readme,
    author='Frank Wiles',
    author_email='frank@revsys.com',
    url='https://github.com/dzonder/django-app-metrics',
    packages=find_packages(),
    package_data={
        'app_metrics': [
            'templates/app_metrics/*',
        ]
    },
    install_requires = [
        'celery',
        'django-celery',
    ],
    tests_require = ['mock', 'django-coverage', 'coverage'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

