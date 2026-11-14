---
title: "pldd(1)"
name: "pldd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pldd/"
description: "pldd – display dynamic shared objects linked into a process"
---

<h2 class="name">NAME</h2>
<p> pldd &#8211; display dynamic shared objects linked into a process </p>
<h2>SYNOPSIS</h2>
<pre>
<code>pldd </code><i>pid</i>
<code>pldd</code><i> option</i>
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>pldd</code> command displays a list of the dynamic shared objects (DSOs) that are linked into the process with the specified process ID (PID). The list includes the libraries that have been dynamically loaded using <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Display a help message and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Display a short usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display program version information and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, <code>pldd</code> exits with the status 0. If the specified process does not exist, the user does not have permission to access its dynamic shared object list, or no command-line arguments are supplied, <code>pldd</code> exists with a status of 1. If given an invalid option, it exits with the status 64.</p>
<h2>VERSIONS</h2>
<p> <code>pldd</code> is available since glibc 2.15.</p>
<h2>CONFORMING TO</h2>
<p> The <code>pldd</code> command is not specified by POSIX.1. Some other systems have a similar command.</p>
<h2>NOTES</h2>
<p> The command </p>
<p> lsof -p PID </p>
<p> also shows output that includes the dynamic shared objects that are linked into a process. </p>
<p> The <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1) <i>info shared</i> command also shows the shared libraries being used by a process, so that one can obtain similar output to <code>pldd</code> using a command such as the following (to monitor the process with the specified <i>pid</i>): </p>
<p> $ <code>gdb -ex &quot;set confirm off&quot; -ex &quot;set height 0&quot; -ex &quot;info shared&quot; \</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-ex&nbsp;&quot;quit&quot;&nbsp;-p&nbsp;$pid | grep&nbsp;&#8216;ha0x.*0x&#8217;</code></p>
<h2>BUGS</h2>
<p> From glibc 2.19 to 2.29, <code>pldd</code> was broken: it just hung when executed. This problem was fixed in glibc 2.30, and the fix has been backported to earlier glibc versions in some distributions.</p>
<h2>EXAMPLES</h2>
<p> $ <code>echo $$</code> # Display PID of shell 1143 $ <code>pldd $$</code> # Display DSOs linked into the shell 1143: /usr/bin/bash linux-vdso.so.1 /lib64/libtinfo.so.5 /lib64/libdl.so.2 /lib64/libc.so.6 /lib64/ld-linux-x86-64.so.2 /lib64/libnss_files.so.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/1-lsof/">lsof</a></code>(1), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
