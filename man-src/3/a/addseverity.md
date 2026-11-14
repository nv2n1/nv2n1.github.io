---
title: "addseverity(3)"
name: "addseverity"
section: "3"
letter: "a"
url: "/docs/linux/man/3-addseverity/"
description: "addseverity – introduce new severity classes"
---

<h2 class="name">NAME</h2>
<p> addseverity &#8211; introduce new severity classes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fmtmsg.h&gt;
int addseverity(int severity, const char *s);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>addseverity</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> This function allows the introduction of new severity classes which can be addressed by the <i>severity</i> argument of the <code><a href="/docs/linux/man/3-fmtmsg/">fmtmsg</a></code>(3) function. By default, that function knows only how to print messages for severity 0-4 (with strings (none), HALT, ERROR, WARNING, INFO). This call attaches the given string <i>s</i> to the given value <i>severity</i>. If <i>s</i> is NULL, the severity class with the numeric value <i>severity</i> is removed. It is not possible to overwrite or remove one of the default severity classes. The severity value must be nonnegative.</p>
<h2>RETURN VALUE</h2>
<p> Upon success, the value <code>MM_OK</code> is returned. Upon error, the return value is <code>MM_NOTOK</code>. Possible errors include: out of memory, attempt to remove a nonexistent or default severity class.</p>
<h2>VERSIONS</h2>
<p> <code>addseverity</code>() is provided in glibc since version 2.1.</p>
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
<td> <code>addseverity</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is not specified in the X/Open Portability Guide although the <code><a href="/docs/linux/man/3-fmtmsg/">fmtmsg</a></code>(3) function is. It is available on System V systems.</p>
<h2>NOTES</h2>
<p> New severity classes can also be added by setting the environment variable <code>SEV_LEVEL</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fmtmsg/">fmtmsg</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
