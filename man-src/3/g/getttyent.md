---
title: "getttyent(3)"
name: "getttyent"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getttyent/"
description: "getttyent, getttynam, setttyent, endttyent – get ttys file entry"
---

<h2 class="name">NAME</h2>
<p> getttyent, getttynam, setttyent, endttyent &#8211; get ttys file entry </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;ttyent.h&gt;</code> </p>
<p> <code>struct ttyent *getttyent(void);</code> </p>
<p> <code>struct ttyent *getttynam(const char *</code><i>name</i><code>);</code> </p>
<p> <code>int setttyent(void);</code> </p>
<p> <code>int endttyent(void);</code></p>
<h2>DESCRIPTION</h2>
<p> These functions provide an interface to the file <code>_PATH_TTYS</code> (e.g., <i>/etc/ttys</i>). </p>
<p> The function <code>setttyent</code>() opens the file or rewinds it if already open. </p>
<p> The function <code>endttyent</code>() closes the file. </p>
<p> The function <code>getttynam</code>() searches for a given terminal name in the file. It returns a pointer to a <i>ttyent</i> structure (description below). </p>
<p> The function <code>getttyent</code>() opens the file <code>_PATH_TTYS</code> (if necessary) and returns the first entry. If the file is already open, the next entry. The <i>ttyent</i> structure has the form: </p>
<p> struct ttyent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*ty_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;terminal device name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*ty_getty;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;command to execute, usually getty&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*ty_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;terminal type for termcap&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;ty_status;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;status flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*ty_window;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;command to start up window manager&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*ty_comment;&nbsp;<wbr>&nbsp;/*&nbsp;comment field&nbsp;*/ }; </p>
<p> <i>ty_status</i> can be: </p>
<p> #define TTY_ON 0x01 /* enable logins (start ty_getty program) */ #define TTY_SECURE 0x02 /* allow UID 0 to login */</p>
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
<td> <code>getttyent</code>(), <code>setttyent</code>(), <code>endttyent</code>(), <code>getttynam</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:ttyent
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Not in POSIX.1. Present on the BSDs, and perhaps other systems.</p>
<h2>NOTES</h2>
<p> Under Linux, the file <i>/etc/ttys</i>, and the functions described above, are not used.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ttyname/">ttyname</a></code>(3), <code><a href="/docs/linux/man/3-ttyslot/">ttyslot</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
