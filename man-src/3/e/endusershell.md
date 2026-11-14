---
title: "endusershell(3)"
name: "endusershell"
section: "3"
letter: "e"
url: "/docs/linux/man/3-endusershell/"
description: "getusershell, setusershell, endusershell – get permitted user shells"
---

<h2 class="name">NAME</h2>
<p> getusershell, setusershell, endusershell &#8211; get permitted user shells </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
char *getusershell(void);
void setusershell(void);
void endusershell(void);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getusershell</code>(), <code>setusershell</code>(), <code>endusershell</code>(): </p>
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
<p> The <code>getusershell</code>() function returns the next line from the file <i>/etc/shells</i>, opening the file if necessary. The line should contain the pathname of a valid user shell. If <i>/etc/shells</i> does not exist or is unreadable, <code>getusershell</code>() behaves as if <i>/bin/sh</i> and <i>/bin/csh</i> were listed in the file. </p>
<p> The <code>setusershell</code>() function rewinds <i>/etc/shells</i>. </p>
<p> The <code>endusershell</code>() function closes <i>/etc/shells</i>.</p>
<h2>RETURN VALUE</h2>
<p> The <code>getusershell</code>() function returns NULL on end-of-file.</p>
<h2>FILES</h2>
<p> <i>/etc/shells</i></p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>getusershell</code>(), <code>setusershell</code>(),<br />
 <code>endusershell</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-shells/">shells</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
