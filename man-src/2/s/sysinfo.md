---
title: "sysinfo(2)"
name: "sysinfo"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sysinfo/"
description: "sysinfo – return system information"
---

<h2 class="name">NAME</h2>
<p> sysinfo &#8211; return system information </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/sysinfo.h&gt;</code> </p>
<p> <code>int sysinfo(struct sysinfo *</code><i>info</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>sysinfo</code>() returns certain statistics on memory and swap usage, as well as the load average. </p>
<p> Until Linux 2.3.16, <code>sysinfo</code>() returned information in the following structure: </p>
<p> struct sysinfo {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long uptime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Seconds since boot&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long loads[3];&nbsp;<wbr>&nbsp;/*&nbsp;1, 5, and 15 minute load averages&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long totalram;&nbsp;<wbr>&nbsp;/*&nbsp;Total usable main memory size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long freeram;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Available memory size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long sharedram;&nbsp;/*&nbsp;Amount of shared memory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long bufferram;&nbsp;/*&nbsp;Memory used by buffers&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long totalswap;&nbsp;/*&nbsp;Total swap space size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long freeswap;&nbsp;<wbr>&nbsp;/*&nbsp;Swap space still available&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short procs;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of current processes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;_f[22];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pads structure to 64 bytes&nbsp;*/ }; </p>
<p> In the above structure, the sizes of the memory and swap fields are given in bytes. </p>
<p> Since Linux 2.3.23 (i386) and Linux 2.3.48 (all architectures) the structure is: </p>
<p> struct sysinfo {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long uptime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Seconds since boot&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long loads[3];&nbsp;<wbr>&nbsp;/*&nbsp;1, 5, and 15 minute load averages&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long totalram;&nbsp;<wbr>&nbsp;/*&nbsp;Total usable main memory size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long freeram;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Available memory size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long sharedram;&nbsp;/*&nbsp;Amount of shared memory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long bufferram;&nbsp;/*&nbsp;Memory used by buffers&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long totalswap;&nbsp;/*&nbsp;Total swap space size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long freeswap;&nbsp;<wbr>&nbsp;/*&nbsp;Swap space still available&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short procs;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of current processes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long totalhigh;&nbsp;/*&nbsp;Total high memory size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long freehigh;&nbsp;<wbr>&nbsp;/*&nbsp;Available high memory size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int mem_unit;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Memory unit size in bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;_f[20-2*sizeof(long)-sizeof(int)];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Padding to 64 bytes&nbsp;*/ }; </p>
<p> In the above structure, sizes of the memory and swap fields are given as multiples of <i>mem_unit</i> bytes.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sysinfo</code>() returns zero. On error, -1 is returned, and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>info</i> is not a valid address.</dl>
<h2>VERSIONS</h2>
<p> <code>sysinfo</code>() first appeared in Linux 0.98.pl6.</p>
<h2>CONFORMING TO</h2>
<p> This function is Linux-specific, and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> All of the information provided by this system call is also available via <i>/proc/meminfo</i> and <i>/proc/loadavg</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
