---
title: "times(2)"
name: "times"
section: "2"
letter: "t"
url: "/docs/linux/man/2-times/"
description: "times – get process times"
---

<h2 class="name">NAME</h2>
<p> times &#8211; get process times </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/times.h&gt;</code> </p>
<p> <code>clock_t times(struct tms *</code><i>buf</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>times</code>() stores the current process times in the <i>struct tms</i> that <i>buf</i> points to. The <i>struct tms</i> is as defined in <i>&lt;sys/times.h&gt;</i>: </p>
<p> struct tms {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clock_t tms_utime;&nbsp;<wbr>&nbsp;/*&nbsp;user time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clock_t tms_stime;&nbsp;<wbr>&nbsp;/*&nbsp;system time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clock_t tms_cutime;&nbsp;/*&nbsp;user time of children&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clock_t tms_cstime;&nbsp;/*&nbsp;system time of children&nbsp;*/ }; </p>
<p> The <i>tms_utime</i> field contains the CPU time spent executing instructions of the calling process. The <i>tms_stime</i> field contains the CPU time spent executing inside the kernel while performing tasks on behalf of the calling process. </p>
<p> The <i>tms_cutime</i> field contains the sum of the <i>tms_utime</i> and <i>tms_cutime</i> values for all waited-for terminated children. The <i>tms_cstime</i> field contains the sum of the <i>tms_stime</i> and <i>tms_cstime</i> values for all waited-for terminated children. </p>
<p> Times for terminated children (and their descendants) are added in at the moment <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) or <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) returns their process ID. In particular, times of grandchildren that the children did not wait for are never seen. </p>
<p> All times reported are in clock ticks.</p>
<h2>RETURN VALUE</h2>
<p> <code>times</code>() returns the number of clock ticks that have elapsed since an arbitrary point in the past. The return value may overflow the possible range of type <i>clock_t</i>. On error, <i>(clock_t)&nbsp;-1</i> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>tms</i> points outside the process&#8217;s address space.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> The number of clock ticks per second can be obtained using: </p>
<p> sysconf(_SC_CLK_TCK); </p>
<p> In POSIX.1-1996 the symbol <code>CLK_TCK</code> (defined in <i>&lt;time.h&gt;</i>) is mentioned as obsolescent. It is obsolete now. </p>
<p> In Linux kernel versions before 2.6.9, if the disposition of <code>SIGCHLD</code> is set to <code>SIG_IGN</code>, then the times of terminated children are automatically included in the <i>tms_cstime</i> and <i>tms_cutime</i> fields, although POSIX.1-2001 says that this should happen only if the calling process <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2)s on its children. This nonconformance is rectified in Linux 2.6.9 and later. </p>
<p> On Linux, the <i>buf</i> argument can be specified as NULL, with the result that <code>times</code>() just returns a function result. However, POSIX does not specify this behavior, and most other UNIX implementations require a non-NULL value for <i>buf</i>. </p>
<p> Note that <code><a href="/docs/linux/man/3-clock/">clock</a></code>(3) also returns a value of type <i>clock_t</i>, but this value is measured in units of <code>CLOCKS_PER_SEC</code>, not the clock ticks used by <code>times</code>(). </p>
<p> On Linux, the &quot;arbitrary point in the past&quot; from which the return value of <code>times</code>() is measured has varied across kernel versions. On Linux 2.4 and earlier, this point is the moment the system was booted. Since Linux 2.6, this point is <i>(2^32/HZ) &#8211; 300</i> seconds before system boot time. This variability across kernel versions (and across UNIX implementations), combined with the fact that the returned value may overflow the range of <i>clock_t</i>, means that a portable application would be wise to avoid using this value. To measure changes in elapsed time, use <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) instead.</p>
<h3>Historical</h3>
<p> SVr1-3 returns <i>long</i> and the struct members are of type <i>time_t</i> although they store clock ticks, not seconds since the Epoch. V7 used <i>long</i> for the struct members, because it had no type <i>time_t</i> yet.</p>
<h2>BUGS</h2>
<p> A limitation of the Linux system call conventions on some architectures (notably i386) means that on Linux 2.6 there is a small time window (41 seconds) soon after boot when <code>times</code>() can return -1, falsely indicating that an error occurred. The same problem can occur when the return value wraps past the maximum value that can be stored in <code>clock_t</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-time/">time</a></code>(1), <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/3-clock/">clock</a></code>(3), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
