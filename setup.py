from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Benoit Bovy",
    maintainer="Benoit Bovy",
    name='django-wpadmin-bootstrapped',
    version='0.1.0',
    description='Bootstrap based SB Admin 2 theme for Django administration',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/benbovy/django-wpadmin-bootstrapped',
    license='Apache Software License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
            'setuptools',
            'Django>=1.8',
            'django-admin-bootstrapped',
        ],
    #test_suite='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
