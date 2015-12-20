#!/usr/bin/env python
# -*- coding: utf-8 -*-

from recaptcha.client import captcha

from paste.httpexceptions import HTTPUnauthorized

from zope.interface import implements
from repoze.who.interfaces import IAuthenticator

import webob

class RecaptchaPlugin(object):

    implements(IAuthenticator)

    def __init__(self, private_key, form_handler):
        self.private_key = private_key
        self.handler = form_handler

    def authenticate(self, environ, identity):
        log = environ['repoze.who.logger']

        if environ.get('__RECAPTCHA_DONE'):
            log.debug('recaptcha validation has already been done.')
            return None
        else:
            environ['__RECAPTCHA_DONE'] = True

        # check if validation is needed
        if self.handler:
            if environ['PATH_INFO'] not in self.handler.split():
                log.debug('no recapcha validation needed.')
                return None

        form = webob.Request(environ).str_POST

        # get form data
        captcha_challenge = form.get('recaptcha_challenge_field')
        captcha_response = form.get('recaptcha_response_field')

        # make a request
        recaptcha_result = captcha.submit(
                            private_key                = self.private_key,
                            remoteip                   = environ['REMOTE_ADDR'],
                            recaptcha_challenge_field  = captcha_challenge,
                            recaptcha_response_field   = captcha_response
                           )

        if recaptcha_result.is_valid:
            log.debug('recaptcha is valid.')
            return None

        else:
            log.debug('recaptcha failed: ' + recaptcha_result.error_code)
            environ['repoze.who.error'] = recaptcha_result.error_code
            environ['repoze.who.application'] = HTTPUnauthorized()
            return None

def make_authentication_plugin(private_key=None, form_handler=None):

    if private_key is None:
        raise ValueError('private_key must be provided for recaptcha API.')

    return RecaptchaPlugin(private_key, form_handler)
