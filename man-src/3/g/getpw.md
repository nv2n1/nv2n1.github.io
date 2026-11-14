---
title: "getpw(3)"
name: "getpw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getpw/"
description: "getpw – reconstruct password line entry"
---

<h2 class="name">NAME</h2>
<p> getpw &#8211; reconstruct password line entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pwd.h&gt;
#include &lt;sys/types.h&gt;
int getpw(uid_t uid, char *buf);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>getpw</code>() function reconstructs the password line entry for the given user ID <i>uid</i> in the buffer <i>buf</i>. The returned buffer contains a line of format </p>
<p> <code>name:passwd:uid:gid:gecos:dir:shell</code> </p>
<p> The <i>passwd</i> structure is defined in <i>&lt;pwd.h&gt;</i> as follows: </p>
<p> struct passwd {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;username&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_passwd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user password&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;pw_uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;pw_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_gecos;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_dir;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;home directory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*pw_shell;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;shell program&nbsp;*/ }; </p>
<p> For more information about the fields of this structure, see <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5).</p>
<h2>RETURN VALUE</h2>
<p> The <code>getpw</code>() function returns 0 on success; on error, it returns -1, and <i>errno</i> is set to indicate the error. </p>
<p> If <i>uid</i> is not found in the password database, <code>getpw</code>() returns -1, sets <i>errno</i> to 0, and leaves <i>buf</i> unchanged.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>0</code> or <code>ENOENT</code></p>
<dd> No user corresponding to <i>uid</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>buf</i> is NULL.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to allocate <i>passwd</i> structure.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/passwd</i></p>
<dd> password database file</dl>
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
<td> <code>getpw</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SVr2.</p>
<h2>BUGS</h2>
<p> The <code>getpw</code>() function is dangerous as it may overflow the provided buffer <i>buf</i>. It is obsoleted by <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-endpwent/">endpwent</a></code>(3), <code><a href="/docs/linux/man/3-fgetpwent/">fgetpwent</a></code>(3), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3), <code><a href="/docs/linux/man/3-putpwent/">putpwent</a></code>(3), <code><a href="/docs/linux/man/3-setpwent/">setpwent</a></code>(3), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
