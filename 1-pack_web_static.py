#!/usr/bin/python3
"""
Write a Fabric script that generates a 
tgz archive from the contents of the web_static folder of your AirBnB Clone repo
, using the function do_pack.
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """ added to the final archive"""
    ate = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    packer = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(packer))
    return packer
