#!/usr/bin/python3
# Generates a .tgz archive from
# the contents of the web_static folder


from fabric.api import local
from datetime import datetime


def do_pack():
    """folder to .tgz file"""
    mydate = datetime.now()
    myfile = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        mydate.year,
        mydate.month,
        mydate.day,
        mydate.hour,
        mydate.minute,
        mydate.second
    )
    local('mkdir -p versions')
    answer = local('tar -cvzf ' + myfile + ' web_static')
    if answer.succeeded:
        return myfile
    return None
