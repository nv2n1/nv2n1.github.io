---
title: "ulimit(3)"
name: "ulimit"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ulimit/"
description: "ulimit – get and set user limits"
---

<p>ulimit &#8211; get and set user limits</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ulimit.h&gt;
long ulimit(int cmd, long newlimit);</code></pre>
<h2>Description</h2>
<p>Warning: this routine is obsolete. Use <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), and <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3) instead. For the shell command <code>ulimit</code>(), see <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1). </p>
<p> The <code>ulimit</code>() call will get or set some limit for the calling process. The <i>cmd</i> argument can have one of the following values.</p>
<dl>
<dt><code>UL_GETFSIZE</code></p>
<dd>Return the limit on the size of a file, in units of 512 bytes.</p>
<dt><code>UL_SETFSIZE</code></p>
<dd>Set the limit on the size of a file.</p>
<dt><code>3</code></p>
<dd>(Not implemented for Linux.) Return the maximum possible address of the data segment.</p>
<dt><code>4</code></p>
<dd>(Implemented but no symbolic constant provided.) Return the maximum number of files that the calling process can open.</dl>
<h2>Return Value</h2>
<p>On success, <code>ulimit</code>() returns a nonnegative value. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EPERM</code></p>
<dd>An unprivileged process tried to increase a limit.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ulimit</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>SVr4, POSIX.1-2001. POSIX.1-2008 marks <code>ulimit</code>() as obsolete.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
