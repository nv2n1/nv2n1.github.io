---
title: "gethostid(3)"
name: "gethostid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gethostid/"
description: "gethostid, sethostid – get or set the unique identifier of the current host"
---

<h2 class="name">NAME</h2>
<p> gethostid, sethostid &#8211; get or set the unique identifier of the current host </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>long gethostid(void);</code><br />
 <code>int sethostid(long </code><i>hostid</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>gethostid</code>():</p>
<dl>
<dt>
<dd> _BSD_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
<p> <code>sethostid</code>(): </p>
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
<p> <code>gethostid</code>() and <code>sethostid</code>() respectively get or set a unique 32-bit identifier for the current machine. The 32-bit identifier was intended to be unique among all UNIX systems in existence. This normally resembles the Internet address for the local machine, as returned by <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), and thus usually never needs to be set. </p>
<p> The <code>sethostid</code>() call is restricted to the superuser.</p>
<h2>RETURN VALUE</h2>
<p> <code>gethostid</code>() returns the 32-bit identifier for the current host as set by <code>sethostid</code>(). </p>
<p> On success, <code>sethostid</code>() returns 0; on error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> <code>sethostid</code>() can fail with the following errors:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The caller did not have permission to write to the file used to store the host ID.</p>
<dt><code>EPERM</code></p>
<dd> The calling process&#8217;s effective user or group ID is not the same as its corresponding real ID.</dl>
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
<td> <code>gethostid</code>() </td>
<td>Thread safety</td>
<td>MT-Safe hostid env locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>sethostid</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe const:hostid
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.2BSD; these functions were dropped in 4.4BSD. SVr4 includes <code>gethostid</code>() but not <code>sethostid</code>(). </p>
<p> POSIX.1-2001 and POSIX.1-2008 specify <code>gethostid</code>() but not <code>sethostid</code>().</p>
<h2>NOTES</h2>
<p> In the glibc implementation, the <i>hostid</i> is stored in the file <i>/etc/hostid</i>. (In glibc versions before 2.2, the file <i>/var/adm/hostid</i> was used.) </p>
<p> In the glibc implementation, if <code>gethostid</code>() cannot open the file containing the host ID, then it obtains the hostname using <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2), passes that hostname to <code><a href="/docs/linux/man/3-gethostbyname_r/">gethostbyname_r</a></code>(3) in order to obtain the host&#8217;s IPv4 address, and returns a value obtained by bit-twiddling the IPv4 address. (This value may not be unique.)</p>
<h2>BUGS</h2>
<p> It is impossible to ensure that the identifier is globally unique.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-hostid/">hostid</a></code>(1), <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
