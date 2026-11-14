---
title: "ionice(1)"
name: "ionice"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ionice/"
description: "ionice – set or get process I/O scheduling class and priority"
---

<h2 class="name">NAME</h2>
<p> ionice &#8211; set or get process I/O scheduling class and priority </p>
<h2>SYNOPSIS</h2>
<p> <code>ionice</code> [<code>-c</code> <i>class</i>] [<code>-n</code> <i>level</i>] [<code>-t</code>] <code>-p</code> <i>PID</i> </p>
<p> <code>ionice</code> [<code>-c</code> <i>class</i>] [<code>-n</code> <i>level</i>] [<code>-t</code>] <code>-P</code> <i>PGID</i> </p>
<p> <code>ionice</code> [<code>-c</code> <i>class</i>] [<code>-n</code> <i>level</i>] [<code>-t</code>] <code>-u</code> <i>UID</i> </p>
<p> <code>ionice</code> [<code>-c</code> <i>class</i>] [<code>-n</code> <i>level</i>] [<code>-t</code>] <i>command</i> [argument] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> This program sets or gets the I/O scheduling class and priority for a program. If no arguments or just <code>-p</code> is given, <code>ionice</code> will query the current I/O scheduling class and priority for that process. </p>
<p> When <i>command</i> is given, <code>ionice</code> will run this command with the given arguments. If no <i>class</i> is specified, then <i>command</i> will be executed with the &quot;best-effort&quot; scheduling class. The default priority level is 4. </p>
<p> As of this writing, a process can be in one of three scheduling classes: </p>
<p> <code>Idle</code></p>
<dl>
<dt>
<dd> A program running with idle I/O priority will only get disk time when no other program has asked for disk I/O for a defined grace period. The impact of an idle I/O process on normal system activity should be zero. This scheduling class does not take a priority argument. Presently, this scheduling class is permitted for an ordinary user (since kernel 2.6.25).</dl>
<p> <code>Best-effort</code></p>
<dl>
<dt>
<dd> This is the effective scheduling class for any process that has not asked for a specific I/O priority. This class takes a priority argument from <i>0-7</i>, with a lower number being higher priority. Programs running at the same best-effort priority are served in a round-robin fashion. </p>
<p> Note that before kernel 2.6.26 a process that has not asked for an I/O priority formally uses &quot;<code>none</code>&quot; as scheduling class, but the I/O scheduler will treat such processes as if it were in the best-effort class. The priority within the best-effort class will be dynamically derived from the CPU nice level of the process: io_priority = (cpu_nice + 20) / 5. </p>
<p> For kernels after 2.6.26 with the CFQ I/O scheduler, a process that has not asked for an I/O priority inherits its CPU scheduling class. The I/O priority is derived from the CPU nice level of the process (same as before kernel 2.6.26).</dl>
<p> <code>Realtime</code></p>
<dl>
<dt>
<dd> The RT scheduling class is given first access to the disk, regardless of what else is going on in the system. Thus the RT class needs to be used with some care, as it can starve other processes. As with the best-effort class, 8 priority levels are defined denoting how big a time slice a given process will receive on each scheduling window. This scheduling class is not permitted for an ordinary (i.e., non-root) user.</dl>
<h2>OPTIONS</h2>
<p> <code>-c</code>, <code>&#8211;class</code> <i>class</i></p>
<dl>
<dt>
<dd> Specify the name or number of the scheduling class to use; 0 for none, 1 for realtime, 2 for best-effort, 3 for idle.</dl>
<p> <code>-n</code>, <code>&#8211;classdata</code> <i>level</i></p>
<dl>
<dt>
<dd> Specify the scheduling class data. This only has an effect if the class accepts an argument. For realtime and best-effort, <i>0-7</i> are valid data (priority levels), and 0 represents the highest priority level.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code> <i>PID</i>&#8230;</p>
<dl>
<dt>
<dd> Specify the process IDs of running processes for which to get or set the scheduling parameters.</dl>
<p> <code>-P</code>, <code>&#8211;pgid</code> <i>PGID</i>&#8230;</p>
<dl>
<dt>
<dd> Specify the process group IDs of running processes for which to get or set the scheduling parameters.</dl>
<p> <code>-t</code>, <code>&#8211;ignore</code></p>
<dl>
<dt>
<dd> Ignore failure to set the requested priority. If <i>command</i> was specified, run it even in case it was not possible to set the desired scheduling priority, which can happen due to insufficient privileges or an old kernel version.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-u</code>, <code>&#8211;uid</code> <i>UID</i>&#8230;</p>
<dl>
<dt>
<dd> Specify the user IDs of running processes for which to get or set the scheduling parameters.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<h2>NOTES</h2>
<p> Linux supports I/O scheduling priorities and classes since 2.6.13 with the CFQ I/O scheduler.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; # <code>ionice</code> -c 3 -p 89</dl>
<p> Sets process with PID 89 as an idle I/O process. </p>
<dl>
<dt>
<dd> &bull; # <code>ionice</code> -c 2 -n 0 bash</dl>
<p> Runs &#8216;bash&#8217; as a best-effort program with highest priority. </p>
<dl>
<dt>
<dd> &bull; # <code>ionice</code> -p 89 91</dl>
<p> Prints the class and priority of the processes with PID 89 and 91.</p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioprio_set/">ioprio_set</a></code>(2)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>ionice</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
