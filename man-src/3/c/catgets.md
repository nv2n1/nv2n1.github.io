---
title: "catgets(3)"
name: "catgets"
section: "3"
letter: "c"
url: "/docs/linux/man/3-catgets/"
description: "catgets – get message from a message catalog"
---

<h2 class="name">NAME</h2>
<p> catgets &#8211; get message from a message catalog </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nl_types.h&gt;
char *catgets(nl_catd catalog, int set_number, int message_number,
              const char *message);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>catgets</code>() reads the message <i>message_number</i>, in set <i>set_number</i>, from the message catalog identified by <i>catalog</i>, where <i>catalog</i> is a catalog descriptor returned from an earlier call to <code><a href="/docs/linux/man/3-catopen/">catopen</a></code>(3). The fourth argument, <i>message</i>, points to a default message string which will be returned by <code>catgets</code>() if the identified message catalog is not currently available. The message-text is contained in an internal buffer area and should be copied by the application if it is to be saved or modified. The return string is always terminated with a null byte (&#8216;\0&#8217;).  </p>
<h2>RETURN VALUE</h2>
<p> On success, <code>catgets</code>() returns a pointer to an internal buffer area containing the null-terminated message string. On failure, <code>catgets</code>() returns the value <i>message</i>.  </p>
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
<td> <code>catgets</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.  </p>
<h2>NOTES</h2>
<p> The <code>catgets</code>() function is available only in libc.so.4.4.4c and above. The Jan 1987 X/Open Portability Guide specifies a more subtle error return: <i>message</i> is returned if the message catalog specified by <i>catalog</i> is not available, while an empty string is returned when the message catalog is available but does not contain the specified message. These two possible error returns seem to be discarded in SUSv2 in favor of always returning <i>message</i>.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-catopen/">catopen</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
