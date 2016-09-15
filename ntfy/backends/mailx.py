# encoding=utf-8

"""
Notify by send message with `mailx`.
"""

import tempfile
import os
import subprocess
import sys


def notify(title, message, receivers, retcode=None):
    tfd, tfpath = tempfile.mkstemp()
    os.write(tfd, message)
    cmd = 'mailx -s "{subject}" {receivers} < {content_file}'.format(
        subject=title,
        receivers=receivers,
        content_file=tfpath
    )
    os.close(tfd)
    execute_cmd(cmd)
    os.unlink(tfpath)


def execute_cmd(cmd):
    """
    Execute a command in subprocess.
    :param cmd: str, command
    :return: (boolean, str), (success_flag, errmsg)
    """
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    exit_code = os.waitpid(p.pid, 0)[1]
    stdout, stderr = p.communicate()
    if exit_code:
        return False, stderr
    return True, None


if __name__ == '__main__':
    notify([sys.argv[1]], sys.argv[2], sys.argv[3])