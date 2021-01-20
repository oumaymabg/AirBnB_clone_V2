#!/usr/bin/python3
"""Compress before sending """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ added to the final archive"""
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    packer = "versions/web_static_{}.tgz".format(date)
    local("sudo tar -cvzf versions/web_static_{}.tgz web_static/".format(date))
    return packer
