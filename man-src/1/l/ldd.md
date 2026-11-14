---
title: "ldd(1)"
name: "ldd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldd/"
description: "ldd – print shared object dependencies"
---

<h2 class="name">NAME</h2>
<p> ldd &#8211; print shared object dependencies </p>
<h2>SYNOPSIS</h2>
<p> <code>ldd</code> [<i>option</i>]&#8230; <i>file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>ldd</code> prints the shared objects (shared libraries) required by each program or shared object specified on the command line. An example of its use and output (using <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1) to trim leading white space for readability in this page) is the following: </p>
<p> $ <code>ldd /bin/ls | sed &#8216;s/^ */ /&#8217;</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;linux-vdso.so.1&nbsp;(0x00007ffcc3563000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;libselinux.so.1&nbsp;=&gt;&nbsp;/lib64/libselinux.so.1&nbsp;(0x00007f87e5459000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;libcap.so.2&nbsp;=&gt;&nbsp;/lib64/libcap.so.2&nbsp;(0x00007f87e5254000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;libc.so.6&nbsp;=&gt;&nbsp;/lib64/libc.so.6&nbsp;(0x00007f87e4e92000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;libpcre.so.1&nbsp;=&gt;&nbsp;/lib64/libpcre.so.1&nbsp;(0x00007f87e4c22000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;libdl.so.2&nbsp;=&gt;&nbsp;/lib64/libdl.so.2&nbsp;(0x00007f87e4a1e000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/lib64/ld-linux-x86-64.so.2&nbsp;(0x00005574bf12e000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;libattr.so.1&nbsp;=&gt;&nbsp;/lib64/libattr.so.1&nbsp;(0x00007f87e4817000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;libpthread.so.0&nbsp;=&gt;&nbsp;/lib64/libpthread.so.0&nbsp;(0x00007f87e45fa000) </p>
<p> In the usual case, <code>ldd</code> invokes the standard dynamic linker (see <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)) with the <code>LD_TRACE_LOADED_OBJECTS</code> environment variable set to 1. This causes the dynamic linker to inspect the program&#8217;s dynamic dependencies, and find (according to the rules described in <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)) and load the objects that satisfy those dependencies. For each dependency, <code>ldd</code> displays the location of the matching object and the (hexadecimal) address at which it is loaded. (The <i>linux-vdso</i> and <i>ld-linux</i> shared dependencies are special; see <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7) and <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8).)</p>
<h3>Security</h3>
<p> Be aware that in some circumstances (e.g., where the program specifies an ELF interpreter other than <i>ld-linux.so</i>), some versions of <code>ldd</code> may attempt to obtain the dependency information by attempting to directly execute the program, which may lead to the execution of whatever code is defined in the program&#8217;s ELF interpreter, and perhaps to execution of the program itself. (In glibc versions before 2.27, the upstream <code>ldd</code> implementation did this for example, although most distributions provided a modified version that did not.) </p>
<p> Thus, you should <i>never</i> employ <code>ldd</code> on an untrusted executable, since this may result in the execution of arbitrary code. A safer alternative when dealing with untrusted executables is: </p>
<p> $ <code>objdump -p /path/to/program | grep NEEDED</code> </p>
<p> Note, however, that this alternative shows only the direct dependencies of the executable, while <code>ldd</code> shows the entire dependency tree of the executable.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the version number of <code>ldd</code>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print all information, including, for example, symbol versioning information.</p>
<dt><code>-u</code>, <code>&#8211;unused</code></p>
<dd> Print unused direct dependencies. (Since glibc 2.3.4.)</p>
<dt><code>-d</code>, <code>&#8211;data-relocs</code></p>
<dd> Perform relocations and report any missing objects (ELF only).</p>
<dt><code>-r</code>, <code>&#8211;function-relocs</code></p>
<dd> Perform relocations for both data objects and functions, and report any missing objects or functions (ELF only).</p>
<dt><code>&#8211;help</code></p>
<dd> Usage information.</dl>
<h2>BUGS</h2>
<p> <code>ldd</code> does not work on a.out shared libraries. </p>
<p> <code>ldd</code> does not work with some extremely old a.out programs which were built before <code>ldd</code> support was added to the compiler releases. If you use <code>ldd</code> on one of these programs, the program will attempt to run with <i>argc</i> = 0 and the results will be unpredictable.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pldd/">pldd</a></code>(1), <code><a href="/docs/linux/man/1-sprof/">sprof</a></code>(1), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8), <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
