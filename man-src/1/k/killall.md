---
title: "killall(1)"
name: "killall"
section: "1"
letter: "k"
url: "/docs/linux/man/1-killall/"
description: "killall – kill processes by name"
---

<h2 class="name">NAME</h2>
<p> killall &#8211; kill processes by name </p>
<h2>SYNOPSIS</h2>
<p> <code>killall</code> [<code>-Z</code>,<code>&nbsp;&#8211;context</code> <i>pattern</i>] [<code>-e</code>,<code>&nbsp;&#8211;exact</code>] [<code>-g</code>,<code>&nbsp;&#8211;process-group</code>] [<code>-i</code>,<code>&nbsp;&#8211;interactive</code>] [<code>-n</code>,<code>&nbsp;&#8211;ns</code> <i>PID</i>] [<code>-o</code>,<code>&nbsp;&#8211;older-than</code> <i>TIME</i>] [<code>-q</code>,<code>&nbsp;&#8211;quiet</code>] [<code>-r</code>,<code>&nbsp;&#8211;regexp</code>] [<code>-s</code>,<code>&nbsp;&#8211;signal</code> <i>SIGNAL</i>,&nbsp;<code>&#8211;</code><i>SIGNAL</i>] [<code>-u</code>,<code>&nbsp;&#8211;user</code> <i>user</i>] [<code>-v</code>,<code>&nbsp;&#8211;verbose</code>] [<code>-w</code>,<code>&nbsp;&#8211;wait</code>] [<code>-y</code>,<code>&nbsp;&#8211;younger-than</code> <i>TIME</i>] [<code>-I</code>,<code>&nbsp;&#8211;ignore-case</code>] [<code>-V</code>,<code>&nbsp;&#8211;version</code>] [<code>&#8212;</code>] <i>name</i> &#8230;<br />
 <code>killall</code> -l<br />
 <code>killall</code> <code>-V</code>,<code>&nbsp;&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>killall</code> sends a signal to all processes running any of the specified commands. If no signal name is specified, SIGTERM is sent. </p>
<p> Signals can be specified either by name (e.g. <code>-HUP</code> or <code>-SIGHUP</code>) or by number (e.g. <code>-1</code>) or by option <code>-s</code>. </p>
<p> If the command name is not regular expression (option <code>-r</code>) and contains a slash (<code>/</code>), processes executing that particular file will be selected for killing, independent of their name. </p>
<p> <code>killall</code> returns a zero return code if at least one process has been killed for each listed command, or no commands were listed and at least one process matched the <code>-u</code> and <code>-Z</code> search criteria. <code>killall</code> returns non-zero otherwise. </p>
<p> A <code>killall</code> process never kills itself (but may kill other <code>killall</code> processes).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code>, <code>&#8211;exact</code></dt>
<dd> Require an exact match for very long names. If a command name is longer than 15 characters, the full name may be unavailable (i.e. it is swapped out). In this case, <code>killall</code> will kill everything that matches within the first 15 characters. With <code>-e</code>, such entries are skipped. <code>killall</code> prints a message for each skipped entry if <code>-v</code> is specified in addition to <code>-e</code>.</dd>
<dt><code>-I</code>, <code>&#8211;ignore-case</code></dt>
<dd> Do case insensitive process name match.</dd>
<dt><code>-g</code>, <code>&#8211;process-group</code></dt>
<dd> Kill the process group to which the process belongs. The kill signal is only sent once per group, even if multiple processes belonging to the same process group were found.</dd>
<dt><code>-i</code>, <code>&#8211;interactive</code></dt>
<dd> Interactively ask for confirmation before killing.</dd>
<dt><code>-l</code>, <code>&#8211;list</code></dt>
<dd> List all known signal names.</dd>
<dt><code>-n</code>, <code>&#8211;ns</code></dt>
<dd> Match against the PID namespace of the given PID. The default is to match against all namespaces.</dd>
<dt><code>-o</code>, <code>&#8211;older-than</code></dt>
<dd> Match only processes that are older (started before) the time specified. The time is specified as a float then a unit. The units are s,m,h,d,w,M,y for seconds, minutes, hours, days, weeks, months and years respectively.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Do not complain if no processes were killed.</dd>
<dt><code>-r</code>, <code>&#8211;regexp</code></dt>
<dd> Interpret process name pattern as a POSIX extended regular expression, per <code><a href="/docs/linux/man/3-regex/">regex</a></code>(3).</dd>
<dt><code>-s</code>, <code>&#8211;signal</code>, <code>&#8211;</code><i>SIGNAL</i></dt>
<dd> Send this signal instead of SIGTERM.</dd>
<dt><code>-u</code>, <code>&#8211;user</code></dt>
<dd> Kill only processes the specified user owns. Command names are optional.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Report if the signal was successfully sent.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Display version information.</dd>
<dt><code>-w</code>, <code>&#8211;wait</code></dt>
<dd> Wait for all killed processes to die. <code>killall</code> checks once per second if any of the killed processes still exist and only returns if none are left. Note that <code>killall</code> may wait forever if the signal was ignored, had no effect, or if the process stays in zombie state.</dd>
<dt><code>-y</code>, <code>&#8211;younger-than</code></dt>
<dd> Match only processes that are younger (started after) the time specified. The time is specified as a float then a unit. The units are s,m,h,d,w,M,y for seconds, minutes, hours, days, weeks, Months and years respectively.</dd>
<dt><code>-Z</code>, <code>&#8211;context</code></dt>
<dd> Specify security context: kill only processes having security context that match with given extended regular expression pattern. Must precede other arguments on the command line. Command names are optional.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>/proc</dt>
<dd> location of the proc file system</dd></dl>
<h2>KNOWN BUGS</h2>
<p> Killing by file only works for executables that are kept open during execution, i.e. impure executables can&#8217;t be killed this way. </p>
<p> Be warned that typing <code>killall</code> <i>name</i> may not have the desired effect on non-Linux systems, especially when done by a privileged user. </p>
<p> <code>killall -w</code> doesn&#8217;t detect if a process disappears and is replaced by a new process with the same PID between scans. </p>
<p> If processes change their name, <code>killall</code> may not be able to match them correctly. </p>
<p> <code>killall</code> has a limit of names that can be specified on the command line. This figure is the size of an unsigned long integer multiplied by 8. For most 32 bit systems the limit is 32 and similarly for a 64 bit system the limit is usually 64.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/1-fuser/">fuser</a></code>(1), <code><a href="/docs/linux/man/1-pgrep/">pgrep</a></code>(1), <code><a href="/docs/linux/man/1-pidof/">pidof</a></code>(1), <code><a href="/docs/linux/man/1-pkill/">pkill</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/3-regex/">regex</a></code>(3). </p>
<h2>Index</h2>
