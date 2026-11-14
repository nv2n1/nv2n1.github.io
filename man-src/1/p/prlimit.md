---
title: "prlimit(1)"
name: "prlimit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prlimit/"
description: "prlimit – get and set process resource limits"
---

<h2 class="name">NAME</h2>
<p> prlimit &#8211; get and set process resource limits </p>
<h2>SYNOPSIS</h2>
<p> <code>prlimit</code> [options] [<code>&#8211;resource</code>[=<i>limits</i>]] [<code>&#8211;pid</code> <i>PID</i>] </p>
<p> <code>prlimit</code> [options] [<code>&#8211;resource</code>[=<i>limits</i>]] <i>command</i> [<i>argument</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Given a process ID and one or more resources, <code>prlimit</code> tries to retrieve and/or modify the limits. </p>
<p> When <i>command</i> is given, <code>prlimit</code> will run this command with the given arguments. </p>
<p> The <i>limits</i> parameter is composed of a soft and a hard value, separated by a colon (:), in order to modify the existing values. If no <i>limits</i> are given, <code>prlimit</code> will display the current values. If one of the values is not given, then the existing one will be used. To specify the unlimited or infinity limit (<code>RLIM_INFINITY</code>), the -1 or &#8216;unlimited&#8217; string can be passed. </p>
<p> Because of the nature of limits, the soft limit must be lower or equal to the high limit (also called the ceiling). To see all available resource limits, refer to the RESOURCE OPTIONS section. </p>
<dl>
<dt>
<dd> &bull; <i>soft</i>:_hard_ Specify both limits.</dl>
<dl>
<dt>
<dd> &bull; <i>soft</i>: Specify only the soft limit.</dl>
<dl>
<dt>
<dd> &bull; :<i>hard</i> Specify only the hard limit.</dl>
<dl>
<dt>
<dd> &bull; <i>value</i> Specify both limits to the same value.</dl>
<h2>GENERAL OPTIONS</h2>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>&#8211;noheadings</code></p>
<dl>
<dt>
<dd> Do not print a header line.</dl>
<p> <code>-o, &#8211;output</code> <i>list</i></p>
<dl>
<dt>
<dd> Define the output columns to use. If no output arrangement is specified, then a default set is used. Use <code>&#8211;help</code> to get a list of all supported columns.</dl>
<p> <code>-p, &#8211;pid</code></p>
<dl>
<dt>
<dd> Specify the process id; if none is given, the running process will be used.</dl>
<p> <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Use the raw output format.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose mode.</dl>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<h2>RESOURCE OPTIONS</h2>
<p> <code>-c, &#8211;core</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum size of a core file.</dl>
<p> <code>-d, &#8211;data</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum data size.</dl>
<p> <code>-e, &#8211;nice</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum nice priority allowed to raise.</dl>
<p> <code>-f, &#8211;fsize</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum file size.</dl>
<p> <code>-i, &#8211;sigpending</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum number of pending signals.</dl>
<p> <code>-l, &#8211;memlock</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum locked-in-memory address space.</dl>
<p> <code>-m, &#8211;rss</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum Resident Set Size (RSS).</dl>
<p> <code>-n, &#8211;nofile</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum number of open files.</dl>
<p> <code>-q, &#8211;msgqueue</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum number of bytes in POSIX message queues.</dl>
<p> <code>-r, &#8211;rtprio</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum real-time priority.</dl>
<p> <code>-s, &#8211;stack</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum size of the stack.</dl>
<p> <code>-t, &#8211;cpu</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> CPU time, in seconds.</dl>
<p> <code>-u, &#8211;nproc</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum number of processes.</dl>
<p> <code>-v, &#8211;as</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Address space limit.</dl>
<p> <code>-x, &#8211;locks</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Maximum number of file locks held.</dl>
<p> <code>-y, &#8211;rttime</code>[=<i>limits</i>]</p>
<dl>
<dt>
<dd> Timeout for real-time tasks.</dl>
<h2>NOTES</h2>
<p> The <code>prlimit</code> system call is supported since Linux 2.6.36, older kernels will break this program.</p>
<h2>EXAMPLES</h2>
<p> <code>prlimit &#8211;pid 13134</code></p>
<dl>
<dt>
<dd> Display limit values for all current resources.</dl>
<p> <code>prlimit &#8211;pid 13134 &#8211;rss &#8211;nofile=1024:4095</code></p>
<dl>
<dt>
<dd> Display the limits of the RSS, and set the soft and hard limits for the number of open files to 1024 and 4095, respectively.</dl>
<p> <code>prlimit &#8211;pid 13134 &#8211;nproc=512:</code></p>
<dl>
<dt>
<dd> Modify only the soft limit for the number of processes.</dl>
<p> <code>prlimit &#8211;pid $$ &#8211;nproc=unlimited</code></p>
<dl>
<dt>
<dd> Set for the current process both the soft and ceiling values for the number of processes to unlimited.</dl>
<p> <code>prlimit &#8211;cpu=10 sort -u hugefile</code></p>
<dl>
<dt>
<dd> Set both the soft and hard CPU time limit to ten seconds and run &#8216;sort&#8217;.</dl>
<h2>AUTHORS</h2>
<p> &#8211; In memory of Dennis M. Ritchie.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/1p-ulimit/">ulimit</a></code>(1p), <code><a href="/docs/linux/man/2-prlimit/">prlimit</a></code>(2)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>prlimit</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
