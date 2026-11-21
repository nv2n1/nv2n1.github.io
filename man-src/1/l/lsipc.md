---

title: "lsipc(1)"
name: "lsipc"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsipc/"
description: "lsipc – show information on IPC facilities currently employed in the system"
---

<p> lsipc - show information on IPC facilities currently employed in the system </p>
<h2>SYNOPSIS</h2>
<p> <code>lsipc</code> [options]  </p>
<h2>DESCRIPTION</h2>
<p> <code>lsipc</code> shows information on the System V inter-process communication facilities for which the calling process has read access.  </p>
<h2>OPTIONS</h2>
<p> <code>-i</code>, <code>--id</code> <i>id</i> </p>
<dl>
<dd> <p> Show full details on just the one resource element identified by <i>id</i>. This option needs to be combined with one of the three resource options: <code>-m</code>, <code>-q</code> or <code>-s</code>. It is possible to override the default output format for this option with the <code>--list</code>, <code>--raw</code>, <code>--json</code> or <code>--export</code> option. </p>
 </dd></dl>
<p> <code>-g</code>, <code>--global</code> </p>
<dl>
<dd> <p> Show system-wide usage and limits of IPC resources. This option may be combined with one of the three resource options: <code>-m</code>, <code>-q</code> or <code>-s</code>. The default is to show information about all resources. </p>
 </dd></dl>
<p> <code>-h</code>, <code>--help</code> </p>
<dl>
<dd> <p> Display help text and exit. </p>
 </dd></dl>
<p> <code>-V</code>, <code>--version</code> </p>
<dl>
<dd> <p> Display version information and exit. </p>
 </dd></dl>
<h3>Resource options</h3>
<p> <code>-m</code>, <code>--shmems</code> </p>
<dl>
<dd> <p> Write information about active shared memory segments. </p>
 </dd></dl>
<p> <code>-q</code>, <code>--queues</code> </p>
<dl>
<dd> <p> Write information about active message queues. </p>
 </dd></dl>
<p> <code>-s</code>, <code>--semaphores</code> </p>
<dl>
<dd> <p> Write information about active semaphore sets. </p>
 </dd></dl>
<h3>Output formatting</h3>
<p> <code>-c</code>, <code>--creator</code> </p>
<dl>
<dd> <p> Show creator and owner. </p>
 </dd></dl>
<p> <code>-e</code>, <code>--export</code> </p>
<dl>
<dd> <p> Produce output in the form of key=&quot;value&quot; pairs. All potentially unsafe value characters are hex-escaped (\x&lt;code&gt;). </p>
 </dd></dl>
<p> <code>-J</code>, <code>--json</code> </p>
<dl>
<dd> <p> Use the JSON output format. </p>
 </dd></dl>
<p> <code>-l</code>, <code>--list</code> </p>
<dl>
<dd> <p> Use the list output format. This is the default, except when <code>--id</code> is used. </p>
 </dd></dl>
<p> <code>-n</code>, <code>--newline</code> </p>
<dl>
<dd> <p> Display each piece of information on a separate line. </p>
 </dd></dl>
<p> <code>--noheadings</code> </p>
<dl>
<dd> <p> Do not print a header line. </p>
 </dd></dl>
<p> <code>--notruncate</code> </p>
<dl>
<dd> <p> Don&#8217;t truncate output. </p>
 </dd></dl>
<p> <code>-o</code>, <code>--output</code> <i>list</i> </p>
<dl>
<dd> <p> Specify which output columns to print. Use <code>--help</code> to get a list of all supported columns. </p>
 </dd></dl>
<p> <code>-b</code>, <code>--bytes</code> </p>
<dl>
<dd> <p> Print size in bytes rather than in human readable format. </p>
 </dd></dl>
<p> <code>-r</code>, <code>--raw</code> </p>
<dl>
<dd> <p> Raw output (no columnation). </p>
 </dd></dl>
<p> <code>-t</code>, <code>--time</code> </p>
<dl>
<dd> <p> Write time information. The time of the last control operation that changed the access permissions for all facilities, the time of the last <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2) and <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2) operations on message queues, the time of the last <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) and <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2) operations on shared memory, and the time of the last <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) operation on semaphores. </p>
 </dd></dl>
<p> <code>--time-format</code> <i>type</i> </p>
<dl>
<dd> <p> Display dates in short, full or iso format. The default is short, this time format is designed to be space efficient and human readable. </p>
 </dd></dl>
<p> <code>-P</code>, <code>--numeric-perms</code> </p>
<dl>
<dd> <p> Print numeric permissions in PERMS column. </p>
 </dd></dl>
<h2>EXIT STATUS</h2>
<p> 0 </p>
<dl>
<dd> <p> if OK, </p>
 </dd></dl>
<p> 1 </p>
<dl>
<dd> <p> if incorrect arguments specified, </p>
 </dd></dl>
<p> 2 </p>
<dl>
<dd> <p> if a serious error occurs. </p>
 </dd></dl>
<h2>HISTORY</h2>
<p> The <code>lsipc</code> utility is inspired by the <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1) utility.  </p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipcmk/">ipcmk</a></code>(1), <code><a href="/docs/linux/man/1-ipcrm/">ipcrm</a></code>(1), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)  </p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.  </p>
<h2>AVAILABILITY</h2>
<p> The <code>lsipc</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
