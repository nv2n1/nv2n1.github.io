---
title: "flockfile(3)"
name: "flockfile"
section: "3"
letter: "f"
url: "/docs/linux/man/3-flockfile/"
description: "flockfile, ftrylockfile, funlockfile – lock FILE for stdio"
---

<h2 class="name">NAME</h2>
<p> flockfile, ftrylockfile, funlockfile &#8211; lock FILE for stdio </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
void flockfile(FILE *filehandle);
int ftrylockfile(FILE *filehandle);
void funlockfile(FILE *filehandle);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> All functions shown above:</p>
<dl>
<dt>
<dd> /* Since glibc 2.24: */ _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.23:&nbsp;*/&nbsp;_POSIX_C_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The stdio functions are thread-safe. This is achieved by assigning to each <i>FILE</i> object a lockcount and (if the lockcount is nonzero) an owning thread. For each library call, these functions wait until the <i>FILE</i> object is no longer locked by a different thread, then lock it, do the requested I/O, and unlock the object again. </p>
<p> (Note: this locking has nothing to do with the file locking done by functions like <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) and <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3).) </p>
<p> All this is invisible to the C-programmer, but there may be two reasons to wish for more detailed control. On the one hand, maybe a series of I/O actions by one thread belongs together, and should not be interrupted by the I/O of some other thread. On the other hand, maybe the locking overhead should be avoided for greater efficiency. </p>
<p> To this end, a thread can explicitly lock the <i>FILE</i> object, then do its series of I/O actions, then unlock. This prevents other threads from coming in between. If the reason for doing this was to achieve greater efficiency, one does the I/O with the nonlocking versions of the stdio functions: with <code><a href="/docs/linux/man/3-getc_unlocked/">getc_unlocked</a></code>(3) and <code><a href="/docs/linux/man/3-putc_unlocked/">putc_unlocked</a></code>(3) instead of <code><a href="/docs/linux/man/3-getc/">getc</a></code>(3) and <code><a href="/docs/linux/man/3-putc/">putc</a></code>(3). </p>
<p> The <code>flockfile</code>() function waits for <i>*filehandle</i> to be no longer locked by a different thread, then makes the current thread owner of <i>*filehandle</i>, and increments the lockcount. </p>
<p> The <code>funlockfile</code>() function decrements the lock count. </p>
<p> The <code>ftrylockfile</code>() function is a nonblocking version of <code>flockfile</code>(). It does nothing in case some other thread owns <i>*filehandle</i>, and it obtains ownership and increments the lockcount otherwise.</p>
<h2>RETURN VALUE</h2>
<p> The <code>ftrylockfile</code>() function returns zero for success (the lock was obtained), and nonzero for failure.</p>
<h2>ERRORS</h2>
<p> None.</p>
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
<td> <code>flockfile</code>(), <code>ftrylockfile</code>(), <code>funlockfile</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008. </p>
<p> These functions are available when <code>_POSIX_THREAD_SAFE_FUNCTIONS</code> is defined.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
