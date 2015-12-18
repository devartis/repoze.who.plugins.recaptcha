from setuptools import setup, find_packages
import sys, os

version = '0.2'

desc = """**repoze.who.recaptcha** implements server side of the recaptcha API. This ``IAuthenticator`` plugin examines environment for recaptcha form values and requests verification. 

**repoze.who.recaptcha** works based on form_handler condition:

* if form_handler parameter is not given, always perform authentication.
* if form_handler parameter is given, perform authentication only when one of the form_handler values (separated by space) matches the absolute URL where the form is processed.

If the validation succeeds, no action is taken. Otherwise error is passed to ``environ['repoze.who.error']`` and ``HTTPUnauthorzied(401)`` is triggered.

.. _bitbucket.org: http://www.bitbucket.org/iElectric/repozewhorecaptcha/

Public Mercurial repo is avaliable at bitbucket.org_ ::

    # sample .ini configuration

    [plugin:recaptcha]
    use = repoze.who.plugins.captcha:make_authentication_plugin
    private_key = si3di5ndlam3x44d
    #optional
    form_handler = /process /login /admin

    [authenticators]
    plugins =
	    recaptcha
"""

setup(name='repoze.who.plugins.recaptcha',
      version=version,
      description="recaptcha repoze.who plugin implementation",
      long_description='\n\n'.join([desc, open('CHANGES.txt', 'r').read()]),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
	"Development Status :: 3 - Alpha"
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='repoze.who captcha',
      author='Domen "iElectric" Kozar',
      author_email='domen@dev.si',
      url='',
      license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose', 'repoze.who'],
      namespace_packages = ['repoze', 'repoze.who', 'repoze.who.plugins'],
      install_requires=[
      	'setuptools',
          # -*- Extra requirements: -*-
	'recaptcha-client>=1.0.2'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
