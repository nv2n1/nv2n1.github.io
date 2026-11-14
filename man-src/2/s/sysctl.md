---
title: "sysctl(2)"
name: "sysctl"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sysctl/"
description: "sysctl – read/write system parameters"
---

<h2 class="name">NAME</h2>
<p> sysctl &#8211; read/write system parameters </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/sysctl.h&gt;
#include &lt;unistd.h&gt;
int _sysctl(struct __sysctl_args *args);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>This system call no longer exists on current kernels!</code> See NOTES. </p>
<p> The <code>_sysctl</code>() call reads and/or writes kernel parameters. For example, the hostname, or the maximum number of open files. The argument has the form </p>
<p> struct __sysctl_args {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;integer vector describing variable&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nlen;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;length of this vector&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;*oldval;&nbsp;<wbr>&nbsp;/*&nbsp;0 or address where to store old value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;*oldlenp;&nbsp;/*&nbsp;available room for old value,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;overwritten by actual size of old value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;*newval;&nbsp;<wbr>&nbsp;/*&nbsp;0 or address of new value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;newlen;&nbsp;<wbr>&nbsp;/*&nbsp;size of new value&nbsp;*/ }; </p>
<p> This call does a search in a tree structure, possibly resembling a directory tree under <i>/proc/sys</i>, and if the requested item is found calls some appropriate routine to read or modify the value.</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>_sysctl</code>() returns 0. Otherwise, a value of -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code>, <code>EPERM</code></p>
<dd> No search permission for one of the encountered &quot;directories&quot;, or no read permission where <i>oldval</i> was nonzero, or no write permission where <i>newval</i> was nonzero.</p>
<dt><code>EFAULT</code></p>
<dd> The invocation asked for the previous value by setting <i>oldval</i> non-NULL, but allowed zero room in <i>oldlenp</i>.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>name</i> was not found.</dl>
<h2>VERSIONS</h2>
<p> This system call first appeared in Linux 1.3.57. It was removed in Linux 5.5; glibc support was removed in version 2.32.</p>
<h2>CONFORMING TO</h2>
<p> This call is Linux-specific, and should not be used in programs intended to be portable. It originated in 4.4BSD. Only Linux has the <i>/proc/sys</i> mirror, and the object naming schemes differ between Linux and 4.4BSD, but the declaration of the <code>sysctl</code>() function is the same in both.</p>
<h2>NOTES</h2>
<p> Use of this system call was long discouraged: since Linux 2.6.24, uses of this system call result in warnings in the kernel log, and in Linux 5.5, the system call was finally removed. Use the <i>/proc/sys</i> interface instead. </p>
<p> Note that on older kernels where this system call still exists, it is available only if the kernel was configured with the <code>CONFIG_SYSCTL_SYSCALL</code> option. Furthermore, glibc does not provide a wrapper for this system call, necessitating the use of <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>BUGS</h2>
<p> The object names vary between kernel versions, making this system call worthless for applications. </p>
<p> Not all available objects are properly documented. </p>
<p> It is not yet possible to change operating system by writing to <i>/proc/sys/kernel/ostype</i>.</p>
<h2>EXAMPLES</h2>
<p> #define _GNU_SOURCE #include &lt;unistd.h&gt; #include &lt;sys/syscall.h&gt; #include &lt;string.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;linux/sysctl.h&gt; </p>
<p> int _sysctl(struct __sysctl_args *args ); </p>
<p> #define OSNAMESZ 100 </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;__sysctl_args args;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char osname[OSNAMESZ];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t osnamelth;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int name[]&nbsp;=&nbsp;{&nbsp;CTL_KERN, KERN_OSTYPE&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(&amp;args, 0, sizeof(args));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;args.name&nbsp;=&nbsp;name;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;args.nlen&nbsp;=&nbsp;sizeof(name)/sizeof(name[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;args.oldval&nbsp;=&nbsp;osname;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;args.oldlenp&nbsp;=&nbsp;&amp;osnamelth; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;osnamelth&nbsp;=&nbsp;sizeof(osname); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(syscall(SYS__sysctl,&nbsp;&amp;args)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;_sysctl&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;This machine is running&nbsp;%*s
&quot;, osnamelth, osname);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
