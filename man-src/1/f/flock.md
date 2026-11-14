---
title: "flock(1)"
name: "flock"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flock/"
description: "flock – manage locks from shell scripts"
---

<h2 class="name">NAME</h2>
<p> flock &#8211; manage locks from shell scripts </p>
<h2>SYNOPSIS</h2>
<p> <code>flock</code> [options] <i>file</i>|<i>directory</i> <i>command</i> [<i>arguments</i>] </p>
<p> <code>flock</code> [options] <i>file</i>|<i>directory</i> <code>-c</code> <i>command</i> </p>
<p> <code>flock</code> [options] <i>number</i></p>
<h2>DESCRIPTION</h2>
<p> This utility manages <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) locks from within shell scripts or from the command line. </p>
<p> The first and second of the above forms wrap the lock around the execution of a <i>command</i>, in a manner similar to <code><a href="/docs/linux/man/1-su/">su</a></code>(1) or <code><a href="/docs/linux/man/1-newgrp/">newgrp</a></code>(1). They lock a specified <i>file</i> or <i>directory</i>, which is created (assuming appropriate permissions) if it does not already exist. By default, if the lock cannot be immediately acquired, <code>flock</code> waits until the lock is available. </p>
<p> The third form uses an open file by its file descriptor <i>number</i>. See the examples below for how that can be used.</p>
<h2>OPTIONS</h2>
<p> <code>-c</code>, <code>&#8211;command</code> <i>command</i></p>
<dl>
<dt>
<dd> Pass a single <i>command</i>, without arguments, to the shell with <code>-c</code>.</dl>
<p> <code>-E</code>, <code>&#8211;conflict-exit-code</code> <i>number</i></p>
<dl>
<dt>
<dd> The exit status used when the <code>-n</code> option is in use, and the conflicting lock exists, or the <code>-w</code> option is in use, and the timeout is reached. The default value is <code>1</code>. The <i>number</i> has to be in the range of 0 to 255.</dl>
<p> <code>-F</code>, <code>&#8211;no-fork</code></p>
<dl>
<dt>
<dd> Do not fork before executing <i>command</i>. Upon execution the flock process is replaced by <i>command</i> which continues to hold the lock. This option is incompatible with <code>&#8211;close</code> as there would otherwise be nothing left to hold the lock.</dl>
<p> <code>-e</code>, <code>-x</code>, <code>&#8211;exclusive</code></p>
<dl>
<dt>
<dd> Obtain an exclusive lock, sometimes called a write lock. This is the default.</dl>
<p> <code>-n</code>, <code>&#8211;nb</code>, <code>&#8211;nonblock</code></p>
<dl>
<dt>
<dd> Fail rather than wait if the lock cannot be immediately acquired. See the <code>-E</code> option for the exit status used.</dl>
<p> <code>-o</code>, <code>&#8211;close</code></p>
<dl>
<dt>
<dd> Close the file descriptor on which the lock is held before executing <i>command</i>. This is useful if <i>command</i> spawns a child process which should not be holding the lock.</dl>
<p> <code>-s</code>, <code>&#8211;shared</code></p>
<dl>
<dt>
<dd> Obtain a shared lock, sometimes called a read lock.</dl>
<p> <code>-u</code>, <code>&#8211;unlock</code></p>
<dl>
<dt>
<dd> Drop a lock. This is usually not required, since a lock is automatically dropped when the file is closed. However, it may be required in special cases, for example if the enclosed command group may have forked a background process which should not be holding the lock.</dl>
<p> <code>-w</code>, <code>&#8211;wait</code>, <code>&#8211;timeout</code> <i>seconds</i></p>
<dl>
<dt>
<dd> Fail if the lock cannot be acquired within <i>seconds</i>. Decimal fractional values are allowed. See the <code>-E</code> option for the exit status used. The zero number of <i>seconds</i> is interpreted as <code>&#8211;nonblock</code>.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Report how long it took to acquire the lock, or why the lock could not be obtained.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>EXIT STATUS</h2>
<p> The command uses &lt;sysexits.h&gt; exit status values for everything, except when using either of the options <code>-n</code> or <code>-w</code> which report a failure to acquire the lock with an exit status given by the <code>-E</code> option, or 1 by default. The exit status given by <code>-E</code> has to be in the range of 0 to 255. </p>
<p> When using the <i>command</i> variant, and executing the child worked, then the exit status is that of the child command.</p>
<h2>EXAMPLES</h2>
<p> Note that &quot;shell&gt; &quot; in examples is a command line prompt. </p>
<p> shell1&gt; flock /tmp -c cat; shell2&gt; flock -w .007 /tmp -c echo; /bin/echo $?</p>
<dl>
<dt>
<dd> Set exclusive lock to directory /tmp and the second command will fail.</dl>
<p> shell1&gt; flock -s /tmp -c cat; shell2&gt; flock -s -w .007 /tmp -c echo; /bin/echo $?</p>
<dl>
<dt>
<dd> Set shared lock to directory /tmp and the second command will not fail. Notice that attempting to get exclusive lock with second command would fail.</dl>
<p> shell&gt; flock -x local-lock-file echo &#8216;a b c&#8217;</p>
<dl>
<dt>
<dd> Grab the exclusive lock &quot;local-lock-file&quot; before running echo with &#8216;a b c&#8217;.</dl>
<p> (; flock -n 9 || exit 1; # &#8230; commands executed under lock &#8230;; ) 9&gt;/var/lock/mylockfile</p>
<dl>
<dt>
<dd> The form is convenient inside shell scripts. The mode used to open the file doesn&#8217;t matter to <code>flock</code>; using <i>&gt;</i> or <i>&gt;&gt;</i> allows the lockfile to be created if it does not already exist, however, write permission is required. Using <i>&lt;</i> requires that the file already exists but only read permission is required. </p>
<p> [ ${FLOCKER} != $0 ] &amp;&amp; exec env FLOCKER=&quot;$0 flock -en $0 $0 $@ ||</p>
<dl>
<dt>
<dd> This is useful boilerplate code for shell scripts. Put it at the top of the shell script you want to lock and it&#8217;ll automatically lock itself on the first run. If the env var <code>$FLOCKER</code> is not set to the shell script that is being run, then execute <code>flock</code> and grab an exclusive non-blocking lock (using the script itself as the lock file) before re-execing itself with the right arguments. It also sets the FLOCKER env var to the right value so it doesn&#8217;t run again.</dl>
</dl>
<p> shell&gt; exec 4&lt;&gt;/var/lock/mylockfile; shell&gt; flock -n 4</p>
<dl>
<dt>
<dd> This form is convenient for locking a file without spawning a subprocess. The shell opens the lock file for reading and writing as file descriptor 4, then flock is used to lock the descriptor.</dl>
<h2>AUTHORS</h2>
<h2>COPYRIGHT</h2>
<p> Copyright © 2003-2006 H. Peter Anvin. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>flock</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
