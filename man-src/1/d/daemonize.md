---
title: "daemonize(1)"
name: "daemonize"
section: "1"
letter: "d"
url: "/docs/linux/man/1-daemonize/"
description: "daemonize – run a program as a Unix daemon"
---

<h2>NAME</h2>
<p> daemonize &#8211; run a program as a Unix daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>daemonize</code> [-a] [-c <i>directory</i>] [-e <i>stderr</i>] [-o <i>stdout</i>] [-p <i>pidfile</i>] [-l <i>lockfile</i>] [-u <i>user</i>] [-v] <i>path [arg] &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>daemonize</code> runs a command as a Unix daemon. As defined in W. Richard Stevens&#8217; 1990 book, <i>Unix Network Programming</i> (Addison-Wesley, 1990), a daemon is &#8220;a process that executes `in the background&#8217; (i.e., without an associated terminal or login shell) either waiting for some event to occur, or waiting to perform some specified task on a periodic basis.&#8221; Upon startup, a typical daemon program will:</p>
<dl>
<dt>o</p>
<dd> Close all open file descriptors (especially standard input, standard output and standard error)</p>
<dt>o</p>
<dd> Change its working directory to the root filesystem, to ensure that it doesn&#8217;t tie up another filesystem and prevent it from being unmounted</p>
<dt>o</p>
<dd> Reset its <i>umask</i> value</p>
<dt>o</p>
<dd> Run in the background (i.e., <i>fork</i>)</p>
<dt>o</p>
<dd> Disassociate from its process group (usually a shell), to insulate itself from signals (such as HUP) sent to the process group</p>
<dt>o</p>
<dd> Ignore all terminal I/O signals</p>
<dt>o</p>
<dd> Disassociate from the control terminal (and take steps not to reacquire one)</p>
<dt>o</p>
<dd> Handle any <font SIZE="-1">SIGCLD</font> signals</dl>
<p> Most programs that are designed to be run as daemons do that work for themselves. However, you&#8217;ll occasionally run across one that does not. When you must run a daemon program that does not properly make itself into a true Unix daemon, you can use <code>daemonize</code> to force it to run as a true daemon.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-a</p>
<dd> Append to the output files, rather than overwriting them (which is the default). Only applicable if <i>-e</i> and/or <i>-o</i> are specified.</p>
<dt>-c <i>directory</i></p>
<dd> Specifies the directory to which to change before running the program. Defaults to &quot;/&quot;. The choice for this option is important. The file system containing the daemon&#8217;s working directory cannot be unmounted while the daemon is running. That&#8217;s why most daemons are careful to use a working directory on the root file system.</p>
<dt>-e <i>stderr</i></p>
<dd> Redirect standard error to the specified file, instead of &quot;/dev/null&quot;. </p>
<p> <code>Warning:</code> Be careful where you redirect the output! The file system containing the open file cannot be unmounted as long as the file is open. For best results, make sure that this output file is on the same file system as the daemon&#8217;s working directory. (See the <i>-c</i> option.)</p>
<dt>-E <i>name=value</i></p>
<dd> Add an environment variable to the environment the daemon will see. The parameter must be of the form <i>name=value.</i> This parameter may be specified multiple times.</p>
<dt>-o <i>stdout</i></p>
<dd> Redirect standard output to the specified file, instead of &quot;/dev/null&quot;. </p>
<p> <code>Warning:</code> Be careful where you redirect the output! The file system containing the open file cannot be unmounted as long as the file is open. For best results, make sure that this output file is on the same file system as the daemon&#8217;s working directory. (See the <i>-c</i> option.)</p>
<dt>-p <i>pidfile</i></p>
<dd> Causes <code>daemonize</code> to write the numeric process ID (PID) of the running daemon to the specified file. This option is useful when the program being daemonized doesn&#8217;t create its own PID file.</p>
<dt>-l <i>lockfile</i></p>
<dd> Single-instance checking. Causes <code>daemonize</code> to ensure that no more than one instance of the daemon is running by placing an exclusive lock on given lockfile. If another process already has a lock on the lockfile, <i>daemonize</i> exits.</dl>
<p> It <i>is </i> possible to use the <i>pidfile</i> as the lock file (e.g., &quot;-p /var/run/foo -l /var/run/foo&quot;), though typical daemons use separate files. </p>
<p> NOTE: If the executed program decides to close all file descriptors, the single-instance locking will not work, since the lock depends on an open file descriptor. (The operating system kernel removes the lock once the process holding the lock closes the file or exits.) Normal processes that do not daemonize themselves do not usually close all file descriptors.</p>
<dl>
<dt>-u <i>user</i></p>
<dd> Run the program as the specified user. This option only works if <code>daemonize</code> is invoked by the superuser. Note: For obvious reasons, it&#8217;s very dangerous to install <code>daemonize</code> as a <i>setuid-to-root</i> executable. For that reason, <code>daemonize</code> will refuse to run if it detects that it has been installed that way.</p>
<dt>-v</p>
<dd> Cause <code>daemonize</code> to write verbose messages to standard error, telling what it&#8217;s doing as it daemonizes the program.</dl>
<h2>NOTES</h2>
<p> If the host operating system provides the <code><a href="/docs/linux/man/3-daemon/">daemon</a></code>(3) library routine, <code>daemonize</code> will use it. Otherwise, <code>daemonize</code> uses its own version of <code><a href="/docs/linux/man/3-daemon/">daemon</a></code>(3). This choice is made at compile time. (BSD 4.4-derived operating systems tend to provide their own <code><a href="/docs/linux/man/3-daemon/">daemon</a></code>(3) routine.) </p>
<p> FreeBSD 5.0 introduced a <code><a href="/docs/linux/man/1-daemon/">daemon</a></code>(1) command that is similar to, but less functional, than <code>daemonize</code>.</p>
<h2>LICENSE</h2>
<p> This program released under a BSD-style license. For more details, consult the LICENSE file accompanying the source distribution, or visit &quot;<a rel="nofollow" href="http://software.clapper.org/daemonize/LICENSE">http://software.clapper.org/daemonize/LICENSE</a>&quot;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-daemon/">daemon</a></code>(3), <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2), <code><a href="/docs/linux/man/2-flock/">flock</a>(2)</code> </p>
<p> <code>daemonize</code> Home Page: <a rel="nofollow" href="http://software.clapper.org/daemonize/">http://software.clapper.org/daemonize/</a></p>
<h2>AUTHOR</h2>
<p> Brian M. Clapper, <i>bmc &lt;at&gt; clapper &lt;dot&gt; org</i></p>
<h2>CONTRIBUTORS</h2>
<p> Support for the <i>-e</i> and <i>-o</i> options is based on a patch submitted by Tim Starling <i>(tstarling &lt;at&gt; wikimedia &lt;dot&gt; org).</i> </p>
<p> Support for the <i>-l</i> option is based on a patch submitted by Yakov Lerner <i>(iler.ml &lt;at&gt; gmail &lt;dot&gt; com).</i> </p>
<h2>Index</h2>
