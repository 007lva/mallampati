# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 22:14:43 2015

@author: raoul
"""

from flask import request

class detect_platform:
    MOBILE_PLATFORMS = ('android', 'ipad', 'ios')
    #get user agent
    def os_platform_not_desktop(self):
        '''
        uses werkzeug classes to detect OS. I used that because I do not
        want android & iOS devices to get the default photobooth.
        Use browser capability detection such as modernizer for anything else.
        '''
        self.platform = request.user_agent.platform
        return self.platform in detect_platform.MOBILE_PLATFORMS

    def get_os_string(self):
        try:
            self.os_string = request.user_agent.platform
            return self.os_string
        except ValueError:
            print ("Error while detecting your os, value returned as "\
                + self.os_string + " of type " + type(self.os_string))
