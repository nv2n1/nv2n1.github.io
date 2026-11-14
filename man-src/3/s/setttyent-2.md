---
title: "setttyent-2(3)"
name: "setttyent-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setttyent-2/"
description: "getttyent, getttynam, setttyent, endttyent – get ttys file entry"
---

<p>getttyent, getttynam, setttyent, endttyent &#8211; get ttys file entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ttyent.h&gt;
struct ttyent *getttyent(void);
struct ttyent *getttynam(const char *name);
int setttyent(void);
int endttyent(void);</code></pre>
<h2>Description</h2>
<p>These functions provide an interface to the file <code>_PATH_TTYS</code> (e.g., <i>/etc/ttys</i>). The function <code>setttyent</code>() opens the file or rewinds it if already open. The function <code>endttyent</code>() closes the file. The function <code>getttynam</code>() searches for a given terminal name in the file. It returns a pointer to a <i>ttyent</i> structure (description below). The function <code>getttyent</code>() opens the file <code>_PATH_TTYS</code> (if necessary) and returns the first entry. If the file is already open, the next entry. The <i>ttyent</i> structure has the form: #define TTY_ON     0x01  /* enable logins (start ty_getty program) */<br />
#define TTY_SECURE 0x02  /* allow UID 0 to login */ <i>ty_status</i> can be: </p>
<pre><code>#define TTY_ON     0x01  /* enable logins (start ty_getty program) */
#define TTY_SECURE 0x02  /* allow UID 0 to login */</code></pre>
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
<td> <code>getttyent</code>(), <code>setttyent</code>(), <code>endttyent</code>(), <code>getttynam</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:ttyent
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>Not in POSIX.1. Present on the BSDs, and perhaps other systems.</p>
<h2>Notes</h2>
<p>Under Linux, the file <i>/etc/ttys</i>, and the functions described above, are not used.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ttyname/">ttyname</a></code>(3), <code><a href="/docs/linux/man/3-ttyslot/">ttyslot</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
