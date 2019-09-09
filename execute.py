#coding=utf8
from eventlet import greenthread
import shlex
import signal
import os
from oslo_config import cfg
from eventlet.green import subprocess
import eventlet
import sys
import time

CONF = cfg.CONF

class WaitTimeout(Exception):
    pass

def _subprocess_setup():
    # Python installs a SIGPIPE handler by default. This is usually not what
    # non-Python subprocesses expect.
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

def subprocess_popen(args, stdin=None, stdout=None, stderr=None, shell=False,
                     env=None, close_fds=True,
                     preexec_fn=_subprocess_setup):
    return subprocess.Popen(args, shell=shell, stdin=stdin, stdout=stdout,
                            stderr=stderr, preexec_fn=preexec_fn,
                            close_fds=close_fds, env=env)

def addl_env_args(addl_env):
    """Build arguments for adding additional environment vars with env"""

    # NOTE (twilson) If using rootwrap, an EnvFilter should be set up for the
    # command instead of a CommandFilter.
    if addl_env is None:
        return []
    return ['env'] + ['%s=%s' % pair for pair in addl_env.items()]

def create_process(cmd, root_helper=None, addl_env=None,
                   std_in=subprocess.PIPE, std_out=subprocess.PIPE, std_err=subprocess.PIPE):

    cmd = list(map(str, addl_env_args(addl_env) + cmd))
    if root_helper:
        if not isinstance(root_helper, list):
            root_helper = shlex.split(str(root_helper))
        cmd = root_helper + cmd
    obj = subprocess_popen(cmd, shell=False,
                           stdin=std_in,
                           stdout=std_out,
                           stderr=std_err)

    return obj, cmd


def execute(cmd, root_helper=None, process_input=None, addl_env=None,
            check_exit_code=True, show_stderr=False, run_as_root=False):
    try:

        if not isinstance(cmd, list):
            cmd = shlex.split(str(cmd))

        if run_as_root:
            root_helper = CONF.root_helper
        print "["
        obj, cmd = create_process(cmd, root_helper=root_helper, addl_env=addl_env)
        print "[1"
        _stdout, _stderr = obj.communicate() or (process_input and obj.communicate(process_input))
        print "??"
        obj.stdin.close()

        _msg = '\nCommand: %(cmd)s\nExit code: %(code)s\nStdout: %(stdout)s\nStdErr: %(stderr)s\n' \
                % {'cmd': cmd, 'code': obj.returncode, 'stdout': _stdout, 'stderr': _stderr}
        if obj.returncode and check_exit_code:
            raise RuntimeError(_msg)

    finally:
        greenthread.sleep(0)
    print "]"
    return show_stderr and (_stdout, _stderr) or _stdout

def find_child_pids(pid, recursive=False):
    try:
        raw_pids = execute(['ps', '--ppid', str(pid), '-o', 'pid='])
    except Exception:
        return []

    child_pids = [x.strip() for x in raw_pids.split('\n') if x.strip()]
    if recursive:
        for child in child_pids:
            child_pids = child_pids + find_child_pids(child, True)
    return child_pids

def wait_until_true(predicate, timeout=60, sleep=1, exception=None):

    try:
        with eventlet.Timeout(timeout):
            while not predicate():
                eventlet.sleep(sleep)
    except eventlet.Timeout:
        if exception is not None:
            #pylint: disable=raising-bad-type
            raise exception
        raise WaitTimeout("Timed out after %d seconds" % timeout)

def add_namespace_to_cmd(cmd, namespace=None):
    """Add an optional namespace to the command."""

    return ['ip', 'netns', 'exec', namespace] + cmd if namespace else cmd

def get_cmdline_from_pid(pid):
    if not process_is_running(pid):
        return []
    with open('/proc/%s/cmdline' % pid, 'r') as f:
        return f.readline().split('\0')[:-1]

def process_is_running(pid):
    return pid and os.path.exists('/proc/%s' % pid)

class ProcessExecutionError(RuntimeError):
    def __init__(self, message, returncode):
        super(ProcessExecutionError, self).__init__(message)
        self.returncode = returncode

def cmd_matches_expected(cmd, expected_cmd):
    abs_cmd = remove_abs_path(cmd)
    abs_expected_cmd = remove_abs_path(expected_cmd)
    if abs_cmd != abs_expected_cmd:
        abs_cmd = remove_abs_path(abs_cmd[1:])
    return abs_cmd == abs_expected_cmd

def remove_abs_path(cmd):
    if cmd and os.path.isabs(cmd[0]):
        cmd = list(cmd)
        cmd[0] = os.path.basename(cmd[0])

    return cmd
def pid_invoked_with_cmdline(pid, expected_cmd):
    cmd = get_cmdline_from_pid(pid)
    return cmd_matches_expected(cmd, expected_cmd)


def get_root_helper_child_pid(pid, expected_cmd, run_as_root=False):
    pid = str(pid)
    if run_as_root:
        while True:
            try:
                # We shouldn't have more than one child per process
                # so keep getting the children of the first one
                pid = find_child_pids(pid)[0]
            except IndexError:
                return  # We never found the child pid with expected_cmd

            # If we've found a pid with no root helper, return it.
            # If we continue, we can find transient children.
            if pid_invoked_with_cmdline(pid, expected_cmd):
                break
    return pid

def kill_process(pid, signal, run_as_root=False):
    """Kill the process with the given pid using the given signal."""
    try:
        execute(['kill', '-%d' % signal, pid], run_as_root=run_as_root)
        # print "1.2" yes
    except Exception:
        if process_is_running(pid):
            raise
    # print "1.3" yes

def p1():
    # for i in range(3):
    #     sys.stdout.write('p1 {}\n'.format(i))
    #     sys.stdout.flush()
    #     eventlet.sleep(1)
    print "p1"
    eventlet.sleep()

def p2():
    # for i in range(3):
    #     sys.stdout.write('p2 {}\n'.format(i))
    #     sys.stdout.flush()
    #     eventlet.sleep()
    print "p2"
    eventlet.sleep()

def test1():
    for func in (p1, p2):
        eventlet.spawn(func)
    obj, cmd = create_process(["echo", "1"], std_out=None)
    obj.communicate() #阻塞直到子进程完成，这时候协程可以开始执行了,把所有的协程执行一遍才会看这个
    print "end"

test1()
