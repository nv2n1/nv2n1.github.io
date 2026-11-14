---
title: "abrt-python(5)"
name: "abrt-python"
section: "5"
letter: "a"
url: "/docs/linux/man/5-abrt-python/"
description: "abrt-python – abrt-python Documentation"
---

<p>abrt-python &#8211; abrt-python Documentation </p>
<p> High-level API for querying, creating and manipulating problems handled by <i>ABRT</i> in Python. </p>
<p> It works on top of low-level DBus or socket API provided by ABRT. Socket API serves only as a fallback option for systems without new DBus problem API as it can only handle the creation of new problems. </p>
<p> This project lives in the <i>abrt repository</i> and is distributed under GPLv2 license. </p>
<p> Contents:</p>
<h2>Usage Examples</h2>
<h3>Creating new problem</h3>
<pre>import problem
prob = problem.Runtime(
 reason='egg_error_message: assertion &quot;error&quot; failed',
 )
prob.add_current_process_data()
prob.add_current_environment()
prob.save()</pre>
<h3>Creating problem for different executable</h3>
<pre>import problem
prob = problem.Selinux(reason='Front fell off')
prob.executable = '/usr/bin/time'
prob.save()</pre>
<h3>Adding custom data</h3>
<pre>import problem
prob = problem.Runtime(
 reason='Error getting devices:'
 'GDBus.Error:org.freedesktop.DBus.Error.UnknownMethod: '
 'No such interface `org.gnome.SettingsDaemon.Power` on object at path '
 '/org/gnome/SettingsDaemon/Power'
 )
prob.add_current_process_data()
prob.custom_data = 'any'
prob['dict_access_example'] = 'works'
print(prob)
print('')
for key, value in prob.items():
 print('{0}={1}'.format(key, value))
print 'Identifier:', prob.save()</pre>
<h3>Querying problems</h3>
<pre>import problem
for prob in problem.list():
 print(prob)
 print(repr(prob.time))
 if hasattr(prob, 'pid'):
 print(prob.pid)</pre>
<h3>Querying all problems</h3>
<p>The <code>list_all</code> method will try to authenticate via <i>polkit</i> to gain access to all problems on the system. </p>
<p> If there is no authentication agent running or authentication is unsuccessful, the list of problems which belong to current user is returned (same as returned by the <code>list</code> method). </p>
<pre>import problem
for prob in problem.list(auth=True):
 print(prob)
 if hasattr(prob, 'username'):
 print('Problem belongs to {0}'.format(prob.username))</pre>
<h3>Editing existing problems</h3>
<pre>import problem
for prob in problem.list():
 if prob.type == problem.JAVA:
 prob.delete()
 if prob.type == problem.CCPP:
 if 'password' in prob.backtrace:
 del prob.backtrace
 prob.save()
 if prob.type == problem.KERNELOOPS:
 prob.backtrace = prob.backtrace.replace(' ?', '')
 prob.save()</pre>
<h3>Watching for new problems</h3>
<pre>import problem
import logging
logging.basicConfig(level=logging.DEBUG)
def monitor(prob):
 print(prob)
 prob.delete()
pwatch = problem.get_problem_watcher()
pwatch.add_callback(monitor)
try:
 pwatch.run()
except KeyboardInterrupt:
 pwatch.quit()</pre>
<h3>Watching for new problems in a thread</h3>
<pre>from __future__ import print_function
import sys
import time
import problem
import threading
class ProblemWatchThread(threading.Thread):
 def __init__(self):
 super(ProblemWatchThread, self).__init__()
 self.pwatch = problem.get_problem_watcher()
 self.pwatch.add_callback(self.handle)
 self.probcount = 0
 def handle(self, prob):
 self.probcount += 1
 print('{0}: {1}'.format(self.probcount, prob))
 # prob.delete()
 def run(self):
 self.pwatch.run()
 def stop(self):
 self.pwatch.quit()
pwt = ProblemWatchThread()
pwt.start()
i = 0
print('Waiting for new problem to appear')
spinner = ['\', '|', '/', '-']
try:
 while True:
 time.sleep(0.1)
 print('{0}'.format(spinner[i]), end='')
 i += 1
 i = i % len(spinner)
 sys.stdout.flush()
except KeyboardInterrupt:
 pwt.stop()
pwt.stop()</pre>
<h3>Getting bug numbers of problems reported to bugzilla</h3>
<pre>import problem
bugs = set()
for prob in problem.list():
 if not hasattr(prob, 'reported_to'):
 continue
 for line in prob.reported_to.splitlines():
 if line.startswith('Bugzilla:'):
 bug_num = int(line.split('=')[-1])
 bugs.add(bug_num)
print(bugs)</pre>
<h2>Stable Api Documentation</h2>
<dl>
<dt><code>class problem.Problem(typ, reason)</code></p>
<dd>Base class for the other problem types. </p>
<p> No need to use this class directly, use one of the specific problem classes.</p>
<dt><code>add_current_environment()</code></p>
<dd>Add environment of current process to this problem object</p>
<dt><code>add_current_process_data()</code></p>
<dd>Add pid, gid and executable of current process to this problem object</p>
<dt><code>delete()</code></p>
<dd>Delete this problem</p>
<dt><code>save()</code></p>
<dd>Create this problem or update modified data </p>
<p> Create or update the project if some of its fields were modified. </p>
<p> Return <code>None</code> in case of modification, identifier if new problem was created.</p>
<dt><code>problem.list(auth=False)</code></p>
<dd>Return the list of the problems </p>
<p> Use <code>auth=True</code> if authentication should be attempted. </p>
<p> If authentication via polkit fails, function behaves as if <code>auth=False</code> was specified (only users problems are returned).</p>
<dt><code>problem.get(identifier, auth=False)</code></p>
<dd>Return problem object matching <code>identifier</code> </p>
<p> Return <code>None</code> in case the problem does not exist. </p>
<p> Use <code>auth=True</code> if authentication should be attempted.</p>
<dt><code>problem.get_problem_watcher(auth=False)</code></p>
<dd>Return <code>ProblemWatcher</code> object which can be used to attach callbacks called when new problem is created </p>
<p> Use <code>auth=True</code> if authentication should be attempted for new problem that doesn&#8217;t belong to current user. If not set such a problem is ignored.</dl>
<h3>Specific problem types</h3>
<dl>
<dt><code>class problem.Ccpp(reason)</code></p>
<dd>C, C++ problem</p>
<dt><code>class problem.Java(reason)</code></p>
<dd>Java problem</p>
<dt><code>class problem.Kerneloops(reason)</code></p>
<dd>Kerneloops problem</p>
<dt><code>class problem.Python(reason)</code></p>
<dd>Python problem</p>
<dt><code>class problem.Runtime(reason)</code></p>
<dd>Runtime problem</p>
<dt><code>class problem.Selinux(reason)</code></p>
<dd>Selinux problem</p>
<dt><code>class problem.Unknown(reason)</code></p>
<dd>Unknown problem</p>
<dt><code>class problem.Xorg(reason)</code></p>
<dd>Xorg problem</dl>
<h3>ProblemWatcher</h3>
<dl>
<dt><code>class problem.watch.ProblemWatcher(auth)</code></p>
<dd>New problem signal handler attached to DBus signal </p>
<p> Use <code>auth=True</code> if authentication should be attempted for new problem that doesn&#8217;t belong to current user. If not set such a problem is ignored.</p>
<dt><code>add_callback(fun)</code></p>
<dd>Add callback to be called when new problem occurs. </p>
<p> Each callback function receives <code>Problem</code> instance</p>
<dt><code>quit()</code></p>
<dd>Stop event listener loop</p>
<dt><code>run()</code></p>
<dd>Start event listener loop</dl>
<h2>Problem Object Properties</h2>
<p>Currently, there is no strict specification of problem properties and you are free to add your own data as you see fit (log files, process data) provided you are planning to use them for reporting. </p>
<p> Mandatory properties required prior saving: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Property </td>
<td> Meaning </td>
<td> Example
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>executable</code> </td>
<td> Executable path of the component which caused the problem. Used by the server to determine <code>component</code> and <code>package</code> data. </td>
<td> <code>&#8216;/usr/bin/time&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Following properties are added by the server when new problem is created: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Property </td>
<td> Meaning </td>
<td> Example
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>component</code> </td>
<td> Component which caused this problem. </td>
<td> <code>&#8216;time&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>hostname</code> </td>
<td> Hostname of the affected machine. </td>
<td> <code>&#8216;fiasco&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>os_release</code> </td>
<td> Operating system release string. </td>
<td> <code>&#8216;Fedora release 17 (Beefy Miracle)&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>uid</code> </td>
<td> User ID </td>
<td> <code>1000</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>username</code> </td>
<td> </td>
<td> <code>&#8216;jeff&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>architecture</code> </td>
<td> Machine architecture string </td>
<td> <code>&#8216;x86_64&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>kernel</code> </td>
<td> Kernel version string </td>
<td> <code>&#8216;3.6.6-1.fc17.x86_64&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>package</code> </td>
<td> Package string </td>
<td> <code>&#8216;time-1.7-40.fc17.x86_64&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>time</code> </td>
<td> Time of the occurence (unixtime) </td>
<td> <code>datetime.datetime(2012, 12, 2, 16, 18, 41)</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>count</code> </td>
<td> Number of times this problem occured </td>
<td> <code>1</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Parsed package data is also available: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Property </td>
<td> Meaning </td>
<td> Example
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pkg_name</code> </td>
<td> Package name </td>
<td> <code>&#8216;time&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pkg_epoch</code> </td>
<td> Package epoch </td>
<td> <code>0</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pkg_version</code> </td>
<td> Package version </td>
<td> <code>&#8216;1.7&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pkg_release</code> </td>
<td> Package release </td>
<td> <code>&#8217;40.fc17&#8242;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pkg_arch</code> </td>
<td> Package architecture </td>
<td> <code>&#8216;x86_64&#8217;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Other common properties (presence differs based on problem type): <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Property </td>
<td> Meaning </td>
<td> Example </td>
<td> Applicable
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>abrt_version</code> </td>
<td> ABRT version string </td>
<td> <code>&#8216;2.0.18.84.g211c&#8217;</code> </td>
<td> Crashes caught by ABRT
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cgroup</code> </td>
<td> cgroup (control group) information for crashed process </td>
<td> <code>&#8216;9:perf_event:/
8:blkio:/
&#8230;&#8217;</code> </td>
<td> C/C++
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>core_backtrace</code> </td>
<td> Machine readable backtrace with no private data </td>
<td> </td>
<td> C/C++, Python, Ruby, Kerneloops
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>backtrace</code> </td>
<td> Original backtrace or backtrace produced by retracing process </td>
<td> </td>
<td> C/C++ (after retracing), Python, Ruby, Xorg, Kerneloops
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>dso_list</code> </td>
<td> List of dynamic libraries loaded at the time of crash </td>
<td> </td>
<td> C/C++, Python
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>maps</code> </td>
<td> Copy of /proc/&lt;pid&gt;/maps file of the problem executable </td>
<td> </td>
<td> C/C++
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cmdline</code> </td>
<td> Copy of /proc/&lt;pid&gt;/cmdline file </td>
<td> <code>&#8216;/usr/bin/gtk-builder-convert&#8217;</code> </td>
<td> C/C++, Python, Ruby, Kerneloops
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>coredump</code> </td>
<td> Coredump of the crashing process </td>
<td> </td>
<td> C/C++
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>environ</code> </td>
<td> Runtime environment of the process </td>
<td> </td>
<td> C/C++, Python
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>open_fds</code> </td>
<td> List of file descriptors open at the time of crash </td>
<td> </td>
<td> C/C++
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pid</code> </td>
<td> Process ID </td>
<td> <code>&#8217;42&#8217;</code> </td>
<td> C/C++, Python, Ruby
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>proc_pid_status</code> </td>
<td> Copy of /proc/&lt;pid&gt;/status file </td>
<td> </td>
<td> C/C++
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>limits</code> </td>
<td> Copy of /proc/&lt;pid&gt;/limits file </td>
<td> </td>
<td> C/C++
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>var_log_messages</code> </td>
<td> Part of the /var/log/messages file which contains crash information </td>
<td> </td>
<td> C/C++
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>suspend_stats</code> </td>
<td> Copy of /sys/kernel/debug/suspend_stats </td>
<td> </td>
<td> Kerneloops
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>reported_to</code> </td>
<td> If the problem was already reported, this item contains URLs of the services where it was reported </td>
<td> </td>
<td> Reported problems
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>event_log</code> </td>
<td> ABRT event log </td>
<td> </td>
<td> Reported problems
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>dmesg</code> </td>
<td> Copy of dmesg </td>
<td> </td>
<td> Kerneloops
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dl>
<dt>&bull;</p>
<dd><i>genindex</i></p>
<dt>&bull;</p>
<dd><i>modindex</i></p>
<dt>&bull;</p>
<dd><i>search</i></dl>
<h2>Author</h2>
<p>Richard Marko</p>
<h2>Copyright</h2>
<p>2012, Richard Marko</p>
