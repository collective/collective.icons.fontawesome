# -*- coding: utf-8 -*-
"""Installer for the collective.icons.fontawesome package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='collective.icons.fontawesome',
    version='1.0a1',
    description="Font Awesome Icons for Plone 6",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS',
    author='Stefan Antonelli',
    author_email='stefan.antonelli@operun.de',
    url='https://github.com/collective/collective.icons.fontawesome',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/collective.icons.fontawesome',
        'Source': 'https://github.com/collective/collective.icons.fontawesome',
        'Tracker': 'https://github.com/collective/collective.icons.fontawesome/issues',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.icons'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7, >=3.6",
    install_requires=[
        'setuptools',
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.restapi',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.icons.fontawesome.locales.update:update_locale
    """,
)
