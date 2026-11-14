---
title: "renice(1)"
name: "renice"
section: "1"
letter: "r"
url: "/docs/linux/man/1-renice/"
description: "renice – alter priority of running processes"
---

<h2 class="name">NAME</h2>
<p> renice &#8211; alter priority of running processes </p>
<h2>SYNOPSIS</h2>
<p> <code>renice</code> [<code>-n</code>] <i>priority</i> [<code>-g</code>|<code>-p</code>|<code>-u</code>] <i>identifier</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>renice</code> alters the scheduling priority of one or more running processes. The first argument is the <i>priority</i> value to be used. The other arguments are interpreted as process IDs (by default), process group IDs, user IDs, or user names. <code>renice</code>&#8216;ing a process group causes all processes in the process group to have their scheduling priority altered. <code>renice</code>&#8216;ing a user causes all processes owned by the user to have their scheduling priority altered.</p>
<h2>OPTIONS</h2>
<p> <code>-n</code>, <code>&#8211;priority</code> <i>priority</i></p>
<dl>
<dt>
<dd> Specify the scheduling <i>priority</i> to be used for the process, process group, or user. Use of the option <code>-n</code> or <code>&#8211;priority</code> is optional, but when used it must be the first argument.</dl>
<p> <code>-g</code>, <code>&#8211;pgrp</code></p>
<dl>
<dt>
<dd> Interpret the succeeding arguments as process group IDs.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code></p>
<dl>
<dt>
<dd> Interpret the succeeding arguments as process IDs (the default).</dl>
<p> <code>-u</code>, <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Interpret the succeeding arguments as usernames or UIDs.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>FILES</h2>
<p> <i>/etc/passwd</i></p>
<dl>
<dt>
<dd> to map user names to user IDs</dl>
<h2>NOTES</h2>
<p> Users other than the superuser may only alter the priority of processes they own. Furthermore, an unprivileged user can only <i>increase</i> the &quot;nice value&quot; (i.e., choose a lower priority) and such changes are irreversible unless (since Linux 2.6.12) the user has a suitable &quot;nice&quot; resource limit (see <code><a href="//www.systutorials.com/docs/linux/man/1p-ulimit/">ulimit</a></code>(1p) and <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)). </p>
<p> The superuser may alter the priority of any process and set the priority to any value in the range -20 to 19. Useful priorities are: 19 (the affected processes will run only when nothing else in the system wants to), 0 (the &quot;base&quot; scheduling priority), anything negative (to make things go very fast).</p>
<h2>HISTORY</h2>
<p> The <code>renice</code> command appeared in 4.0BSD.</p>
<h2>EXAMPLES</h2>
<p> The following command would change the priority of the processes with PIDs 987 and 32, plus all processes owned by the users daemon and root: </p>
<p> <code>renice +1 987 -u daemon root -p 32</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-chrt/">chrt</a></code>(1), <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>renice</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
