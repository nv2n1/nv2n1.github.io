---
title: "posix_openpt(3)"
name: "posix_openpt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-posix_openpt/"
description: "posix_openpt – open a pseudoterminal device"
---

<p>posix_openpt &#8211; open a pseudoterminal device</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;fcntl.h&gt;
#include &lt;stdlib.h&gt;

int posix_openpt(int flags);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>posix_openpt</code>(): _XOPEN_SOURCE&nbsp;&gt;=&nbsp;600</p>
<h2>Description</h2>
<p>The <code>posix_openpt</code>() function opens an unused pseudoterminal master device, returning a file descriptor that can be used to refer to that device. </p>
<p> The <i>flags</i> argument is a bit mask that ORs together zero or more of the following flags:</p>
<dl>
<dt><code>O_RDWR</code></p>
<dd>Open the device for both reading and writing. It is usual to specify this flag.</p>
<dt><code>O_NOCTTY</code></p>
<dd>Do not make this device the controlling terminal for the process.</dl>
<h2>Return Value</h2>
<p>On success, <code>posix_openpt</code>() returns a file descriptor (a nonnegative integer) which is the lowest numbered unused file descriptor. On failure, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<h2>Versions</h2>
<p>Glibc support for <code>posix_openpt</code>() has been provided since version 2.2.1.</p>
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
<td> <code>posix_openpt</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>posix_openpt</code>() is part of the UNIX 98 pseudoterminal support (see <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4)).</p>
<h2>Notes</h2>
<p>Some older UNIX implementations that support System V (aka UNIX 98) pseudoterminals don&#8217;t have this function, but it can be easily implemented by opening the pseudoterminal multiplexor device: </p>
<pre><code>int posix_openpt(int flags)
{
    return open(&quot;/dev/ptmx&quot;, flags);
}</code></pre>
<p> Calling <code>posix_openpt</code>() creates a pathname for the corresponding pseudoterminal slave device. The pathname of the slave device can be obtained using <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3). The slave device pathname exists only as long as the master device is open.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-getpt/">getpt</a></code>(3), <code><a href="/docs/linux/man/3-grantpt/">grantpt</a></code>(3), <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3), <code><a href="/docs/linux/man/3-unlockpt/">unlockpt</a></code>(3), <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
