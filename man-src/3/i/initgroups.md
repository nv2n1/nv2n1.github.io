---
title: "initgroups(3)"
name: "initgroups"
section: "3"
letter: "i"
url: "/docs/linux/man/3-initgroups/"
description: "initgroups – initialize the supplementary group access list"
---

<h2 class="name">NAME</h2>
<p> initgroups &#8211; initialize the supplementary group access list </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;grp.h&gt;
#include &lt;sys/types.h&gt;
int initgroups(const char *user, gid_t group);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>initgroups</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>initgroups</code>() function initializes the group access list by reading the group database <i>/etc/group</i> and using all groups of which <i>user</i> is a member. The additional group <i>group</i> is also added to the list. </p>
<p> The <i>user</i> argument must be non-NULL.</p>
<h2>RETURN VALUE</h2>
<p> The <code>initgroups</code>() function returns 0 on success. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to allocate group information structure.</p>
<dt><code>EPERM</code></p>
<dd> The calling process has insufficient privilege. See the underlying system call <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2).</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/group</i></p>
<dd> group database file</dl>
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
<td> <code>initgroups</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getgroups/">getgroups</a></code>(2), <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
