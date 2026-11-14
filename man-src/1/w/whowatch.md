---
title: "whowatch(1)"
name: "whowatch"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whowatch/"
description: "whowatch – console, interactive, process and users monitoring tool."
---

<h2>NAME</h2>
<p> whowatch &#8211; console, interactive, process and users monitoring tool.</p>
<h2>DESCRIPTION</h2>
<p> <code>Whowatch</code> is an console, interactive users and process monitoring tool. It displays information about the users currently logged on to the machine, in real-time. Besides standard information (login name, tty, host, user&#8217;s process), the type of the connection (ie. telnet or ssh) is shown. Display of users command line can be switch to tty idle time. Certain user can be selected and his processes tree may be viewed as well as tree of all system processes. Tree may be displayed with additional column that shows owner of each process. In the process tree mode SIGINT and SIGKILL signals can be sent to the selected process. Killing processes is just as simple and fun as deleting lines on the screen. </p>
<p> <code>Whowatch</code> has no command line options or configuration file. All actions are performed in real time by pressing following keys: </p>
<p> Users list mode: </p>
<dl>
<dt><code>&#8216;up&#8217; &#8216;down&#8217;</code></p>
<dd> cursor movement</p>
<dt><code>&#8216;i&#8217;</code></p>
<dd> toggle between user command line and idle time</p>
<dt><code>&#8216;c&#8217;</code></p>
<dd> full command line on/off. Disabling full command line can save CPU time. It can give you also some additional information about process executable.</p>
<dt><code>&#8216;enter&#8217;</code></p>
<dd> view selected user&#8217;s processes tree.</p>
<dt><code>&#8216;t&#8217;</code></p>
<dd> all system processes (init tree)</dl>
<p> Tree mode:</p>
<dl>
<dt><code>&#8216;up&#8217; &#8216;down&#8217;</code></p>
<dd> cursor movement</p>
<dt><code>&#8216;enter&#8217;</code></p>
<dd> go back to users list</p>
<dt><code>&#8216;o&#8217; </code></p>
<dd> show processes owners</p>
<dt><code>&#8216;c&#8217; </code></p>
<dd> full command line on/off. Disabling full command line can save CPU time. It can give you also some additional information about process executable.</p>
<dt><code>&#8216;Ctrl-I&#8217;</code></p>
<dd> send INT signal to selected process</p>
<dt><code>&#8216;Ctrl-K&#8217;</code></p>
<dd> send KILL signal to selected process </p>
</dl>
<h2>PLUGINS</h2>
<p> Whowatch has ability to load plugin during program run. Plugin prints information inside details window. Plugins gives flexibility: if some specific information about process, user or system is needed then separate program could be written to obtain such information. Since there are three kinds of deatils window (process, user and system) maximum three plugins can be loaded. Whowatch has very simple API to write plugins. </p>
<h2>FILES</h2>
<p> Program reads <i>/var/log/wtmp</i>, <i>/var/run/utmp</i>. Under Linux program also reads files from <i>/proc</i> directory. Without read access to these files <code>whowatch</code> funcionality will be limited or program will not even start. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-finger/">finger</a></code>(1) <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-pstree/">pstree</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/1-w/">w</a></code>(1), <code><a href="/docs/linux/man/8-lsof/">lsof</a></code>(8), <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1) <code><a href="/docs/linux/man/1-killall/">killall</a></code>(1) </p>
<h2>BUGS</h2>
<p> Because lack of ut_pid in utmp and wtmp structures in *BSD systems, program tries to obtain pid of a login shell by analizing processes controlling terminal and processes names. Under some conditions it may lead to incorrect results ie. there will be incorrect processes tree associated with user&#8217;s session. </p>
<h2>AUTHOR</h2>
<pre><code>
Michal Suszycki&lt;mike[at] wizard.ae.krakow.pl&gt;,
    http : // wizard.ae.krakow.pl/~mike
           Tree functions written by Jan Bobrowski&lt;jb[at] wizard.ae.krakow.pl&gt;,
           http: // wizard.ae.krakow.pl/~jb
</code></pre>
<h2>Index</h2>
