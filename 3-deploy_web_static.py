#!/usr/bin/python3
""" distributes an archive to a web server """
from fabric.api import *
from fabric.operations import run, put, sudo
import os.path

env.hosts = ['34.73.233.204', '34.73.89.226']


def do_deploy(archive_path):
    """ distributes an archive to a web server """
    if (os.path.exists(archive_path) is False):
        return False

    try:
        i = archive_path.split("/")[-1]
        j = ("/data/web_static/releases/" + i.split(".")[0])

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(j))
        run("sudo tar -xzf /tmp/{} -C {}".format(i, j))
        run("sudo rm /tmp/{}".format(i))
        run("sudo mv {}/web_static/* {}/".format(j, j))
        run("sudo rm -rf {}/web_static".format(j))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(j))
        return True
    except Exception:
        return False


def deploy():
    """ creates and distributes an archive to a web servers """
    try:
        address = do_pack()
        v = do_deploy(address)
        return v
    except Exception:
        return False
