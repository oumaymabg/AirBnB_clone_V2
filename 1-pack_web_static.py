#!/usr/bin/python3
"""Compress before sending """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ added to the final archive"""
    ate = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    packer = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(packer))
    return packer
