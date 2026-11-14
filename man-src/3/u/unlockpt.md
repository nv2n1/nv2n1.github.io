---
title: "unlockpt(3)"
name: "unlockpt"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unlockpt/"
description: "unlockpt – unlock a pseudoterminal master/slave pair"
---

<p>unlockpt &#8211; unlock a pseudoterminal master/slave pair</p>
<h2>Synopsis</h2>
<pre><code>#define _XOPEN_SOURCE

#include &lt;stdlib.h&gt;
int unlockpt(int fd);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>unlockpt</code>(): </p>
<dl>
<dd>Since glibc 2.24:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(_XOPEN_SOURCE&nbsp;&amp;&amp;&nbsp;_XOPEN_SOURCE_EXTENDED)<br />
 Glibc 2.23 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE</dl>
<h2>Description</h2>
<p>The <code>unlockpt</code>() function unlocks the slave pseudoterminal device corresponding to the master pseudoterminal referred to by the file descriptor <i>fd</i>. </p>
<p> <code>unlockpt</code>() should be called before opening the slave side of a pseudoterminal.</p>
<h2>Return Value</h2>
<p>When successful, <code>unlockpt</code>() returns 0. Otherwise, it returns -1 and sets <i>errno</i> appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd>The <i>fd</i> argument is not a file descriptor open for writing.</p>
<dt><code>EINVAL</code></p>
<dd>The <i>fd</i> argument is not associated with a master pseudoterminal.</dl>
<h2>Versions</h2>
<p><code>unlockpt</code>() is provided in glibc since version 2.1.</p>
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
<td> <code>unlockpt</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-grantpt/">grantpt</a></code>(3), <code><a href="/docs/linux/man/3-posix_openpt/">posix_openpt</a></code>(3), <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3), <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
