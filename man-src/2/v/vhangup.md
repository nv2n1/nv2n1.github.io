---
title: "vhangup(2)"
name: "vhangup"
section: "2"
letter: "v"
url: "/docs/linux/man/2-vhangup/"
description: "vhangup – virtually hangup the current terminal"
---

<h2 class="name">NAME</h2>
<p> vhangup &#8211; virtually hangup the current terminal </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int vhangup(void);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>vhangup</code>(): </p>
<pre><code>
Since glibc 2.21 : _DEFAULT_SOURCE
                       In glibc 2.19 and
                   2.20 : _DEFAULT_SOURCE ||
    (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE &amp; nbsp; &lt; &amp;nbsp; 500)
        Up to and including glibc 2.19 : _BSD_SOURCE
                                         ||
                                         (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE &amp; nbsp; &lt; &amp;nbsp; 500)
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>vhangup</code>() simulates a hangup on the current terminal. This call arranges for other users to have a &#8220;clean&#8221; terminal at login time.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EPERM</code></p>
<dd> The calling process has insufficient privilege to call <code>vhangup</code>(); the <code>CAP_SYS_TTY_CONFIG</code> capability is required.</dl>
<h2>CONFORMING TO</h2>
<p> This call is Linux-specific, and should not be used in programs intended to be portable.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-init/">init</a></code>(1), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
