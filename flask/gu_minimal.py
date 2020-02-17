#!/usr/bin/python3

loglevel = 'info' #debug, info or critical
errorlog = '/home/ec2-user/logs/minimal.log'
accesslog = '/home/ec2-user/logs/minimal_access.log'

bind = '0.0.0.0:5000' #port 5000, make sure this is in range of what you set in sec-groups
workers = 3

timeout = 3 * 60  # 3 minutes

capture_output = True
