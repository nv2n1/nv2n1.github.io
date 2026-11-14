---
title: "twistd3(1)"
name: "twistd3"
section: "1"
letter: "t"
url: "/docs/linux/man/1-twistd3/"
description: "twistd – run Twisted applications (TACs, TAPs)"
---

<h2 class="name">NAME</h2>
<p> twistd &#8211; run Twisted applications (TACs, TAPs) </p>
<h2>SYNOPSIS</h2>
<p> <code>twistd</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> Read a twisted.application.service.Application out of a file and run it.</p>
<h2>OPTIONS</h2>
<p> <code>-n</code>, <code>&#8211;nodaemon</code> Don&#8217;t daemonize (stay in foreground).</p>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> No-op for backwards compatibility.</p>
<dt><code>-p</code>, <code>&#8211;profile</code> <i>&lt;profile output&gt;</i></p>
<dd> Run the application under the profiler, dumping results to the specified file.</p>
<dt><code>&#8211;profiler</code> <i>&lt;profiler name&gt;</i></p>
<dd> Specify the profiler to use. Defaults to the &#8216;hotshot&#8217; profiler.</p>
<dt><code>&#8211;savestats</code></p>
<dd> Save the Stats object rather than the text output of the profiler.</p>
<dt><code>-b</code>, <code>&#8211;debug</code></p>
<dd> Run the application in the Python Debugger (implies <code>&#8211;nodaemon</code> option). Sending a SIGINT or SIGUSR2 signal to the process will drop it into the debugger.</p>
<dt><code>-e</code>, <code>&#8211;encrypted</code> <i>&lt;file&gt;</i></p>
<dd> The specified tap/aos file is encrypted.</p>
<dt><code>&#8211;euid</code></p>
<dd> Set only effective user-id rather than real user-id. This option has no effect unless the server is running as root, in which case it means not to shed all privileges after binding ports, retaining the option to regain privileges in cases such as spawning processes. Use with caution.</p>
<dt><code>-o</code>, <code>&#8211;no_save</code></p>
<dd> Do not save shutdown state.</p>
<dt><code>&#8211;originalname</code></p>
<dd> Behave as though the specified Application has no process name set, and run with the standard process name (the Python binary in most cases).</p>
<dt><code>-l</code>, <code>&#8211;logfile</code> <i>&lt;logfile&gt;</i></p>
<dd> Log to a specified file, &#8211; for stdout (default: twistd.log). The log file will be rotated on SIGUSR1.</p>
<dt><code>-l</code>, <code>&#8211;logger</code> <i>&lt;fully qualified python name&gt;</i></p>
<dd> A fully-qualified name to a log observer factory to use for the initial log observer. Takes precedence over &#8211;logfile and &#8211;syslog.</p>
<dt><code>&#8211;pidfile</code> <i>&lt;pidfile&gt;</i></p>
<dd> Save pid in specified file (default: twistd.pid).</p>
<dt><code>&#8211;chroot</code> <i>&lt;directory&gt;</i></p>
<dd> Chroot to a supplied directory before running (default: don&#8217;t chroot). Chrooting is done before changing the current directory.</p>
<dt><code>-d</code>, <code>&#8211;rundir</code> <i>&lt;directory&gt;</i></p>
<dd> Change to a supplied directory before running (default: .).</p>
<dt><code>-u</code>, <code>&#8211;uid</code> <i>&lt;uid&gt;</i></p>
<dd> The uid to run as (default: don&#8217;t change).</p>
<dt><code>-g</code>, <code>&#8211;gid</code> <i>&lt;gid&gt;</i></p>
<dd> The gid to run as (default: don&#8217;t change).</p>
<dt><code>&#8211;umask</code> <i>&lt;mask&gt;</i></p>
<dd> The (octal) file creation mask to apply. (default: 0077 for daemons, no change otherwise).</p>
<dt><code>-r</code>, <code>&#8211;reactor</code> <i>&lt;reactor&gt;</i></p>
<dd> Choose which reactor to use. See <code>&#8211;help-reactors</code> for a list of possibilities.</p>
<dt><code>&#8211;help-reactors</code></p>
<dd> List the names of possibly available reactors.</p>
<dt><code>&#8211;spew</code></p>
<dd> Write an extremely verbose log of everything that happens. Useful for debugging freezes or locks in complex code.</p>
<dt><code>-f</code>, <code>&#8211;file</code> <i>&lt;tap file&gt;</i></p>
<dd> Read the given .tap file (default: twistd.tap).</p>
<dt><code>-s</code>, <code>&#8211;source</code> <i>&lt;tas file&gt;</i></p>
<dd> Load an Application from the given .tas (AOT Python source) file.</p>
<dt><code>-y</code>, <code>&#8211;python</code> <i>&lt;python file&gt;</i></p>
<dd> Use the variable &quot;application&quot; from the given Python file. This option overrides <code>-f</code>. This option implies <code>&#8211;no_save</code>.</p>
<dt><code>&#8211;syslog</code></p>
<dd> Log to syslog instead of a file.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>&#8211;prefix</code> <i>&lt;prefix&gt;</i></p>
<dd> Use the specified prefix when logging to logfile. Default is &quot;twisted&quot;.</dl>
<p> Note that if <code>twistd</code> is run as root, the working directory is <i>not</i> searched for Python modules.</p>
<h2>SIGNALS</h2>
<p> A running twistd accepts SIGINT for a clean shutdown and SIGUSR1 to rotate log files.</p>
<h2>AUTHOR</h2>
<p> Written by Moshe Zadka, based on twistd&#8217;s help messages.</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/trac/wiki/TwistedDevelopment#DevelopmentProcess">http://twistedmatrix.com/trac/wiki/TwistedDevelopment#DevelopmentProcess</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2011 Twisted Matrix Laboratories.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
