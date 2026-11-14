---
title: "ipcs(1)"
name: "ipcs"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipcs/"
description: "ipcs – show information on IPC facilities"
---

<h2 class="name">NAME</h2>
<p> ipcs &#8211; show information on IPC facilities </p>
<h2>SYNOPSIS</h2>
<p> <code>ipcs</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>ipcs</code> shows information on System V inter-process communication facilities. By default it shows information about all three resources: shared memory segments, message queues, and semaphore arrays.</p>
<h2>OPTIONS</h2>
<p> <code>-i</code>, <code>&#8211;id</code> <i>id</i></p>
<dl>
<dt>
<dd> Show full details on just the one resource element identified by <i>id</i>. This option needs to be combined with one of the three resource options: <code>-m</code>, <code>-q</code> or <code>-s</code>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<h3>Resource options</h3>
<p> <code>-m</code>, <code>&#8211;shmems</code></p>
<dl>
<dt>
<dd> Write information about active shared memory segments.</dl>
<p> <code>-q</code>, <code>&#8211;queues</code></p>
<dl>
<dt>
<dd> Write information about active message queues.</dl>
<p> <code>-s</code>, <code>&#8211;semaphores</code></p>
<dl>
<dt>
<dd> Write information about active semaphore sets.</dl>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Write information about all three resources (default).</dl>
<h3>Output formats</h3>
<p> Of these options only one takes effect: the last one specified. </p>
<p> <code>-c</code>, <code>&#8211;creator</code></p>
<dl>
<dt>
<dd> Show creator and owner.</dl>
<p> <code>-l</code>, <code>&#8211;limits</code></p>
<dl>
<dt>
<dd> Show resource limits.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code></p>
<dl>
<dt>
<dd> Show PIDs of creator and last operator.</dl>
<p> <code>-t</code>, <code>&#8211;time</code></p>
<dl>
<dt>
<dd> Write time information. The time of the last control operation that changed the access permissions for all facilities, the time of the last <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2) and <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2) operations on message queues, the time of the last <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) and <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2) operations on shared memory, and the time of the last <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) operation on semaphores.</dl>
<p> <code>-u</code>, <code>&#8211;summary</code></p>
<dl>
<dt>
<dd> Show status summary.</dl>
<h3>Representation</h3>
<p> These affect only the <code>-l</code> (<code>&#8211;limits</code>) option. </p>
<p> <code>-b</code>, <code>&#8211;bytes</code></p>
<dl>
<dt>
<dd> Print sizes in bytes.</dl>
<p> <code>&#8211;human</code></p>
<dl>
<dt>
<dd> Print sizes in human-readable format.</dl>
<h2>CONFORMING TO</h2>
<p> The Linux <code>ipcs</code> utility is not fully compatible to the POSIX <code>ipcs</code> utility. The Linux version does not support the POSIX <code>-a</code>, <code>-b</code> and <code>-o</code> options, but does support the <code>-l</code> and <code>-u</code> options not defined by POSIX. A portable application shall not use the <code>-a</code>, <code>-b</code>, <code>-o</code>, <code>-l</code>, and <code>-u</code> options.</p>
<h2>NOTES</h2>
<p> The current implementation of <code>ipcs</code> obtains information about available IPC resources by parsing the files in <i>/proc/sysvipc</i>. Before util-linux version v2.23, an alternate mechanism was used: the <code>IPC_STAT</code> command of <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2), <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2), and <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2). This mechanism is also used in later util-linux versions in the case where <i>/proc</i> is unavailable. A limitation of the <code>IPC_STAT</code> mechanism is that it can only be used to retrieve information about IPC resources for which the user has read permission.</p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipcmk/">ipcmk</a></code>(1), <code><a href="/docs/linux/man/1-ipcrm/">ipcrm</a></code>(1), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>ipcs</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
