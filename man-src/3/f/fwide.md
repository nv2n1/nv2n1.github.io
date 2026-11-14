---
title: "fwide(3)"
name: "fwide"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fwide/"
description: "fwide – set and determine the orientation of a FILE stream"
---

<h2 class="name">NAME</h2>
<p> fwide &#8211; set and determine the orientation of a FILE stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
int fwide(FILE *stream, int mode);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fwide</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 || _ISOC99_SOURCE ||<br />
 _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> When <i>mode</i> is zero, the <code>fwide</code>() function determines the current orientation of <i>stream</i>. It returns a positive value if <i>stream</i> is wide-character oriented, that is, if wide-character I/O is permitted but char I/O is disallowed. It returns a negative value if <i>stream</i> is byte oriented&#8212;that is, if char I/O is permitted but wide-character I/O is disallowed. It returns zero if <i>stream</i> has no orientation yet; in this case the next I/O operation might change the orientation (to byte oriented if it is a char I/O operation, or to wide-character oriented if it is a wide-character I/O operation). </p>
<p> Once a stream has an orientation, it cannot be changed and persists until the stream is closed. </p>
<p> When <i>mode</i> is nonzero, the <code>fwide</code>() function first attempts to set <i>stream</i>&#8216;s orientation (to wide-character oriented if <i>mode</i> is greater than 0, or to byte oriented if <i>mode</i> is less than 0). It then returns a value denoting the current orientation, as above.</p>
<h2>RETURN VALUE</h2>
<p> The <code>fwide</code>() function returns the stream&#8217;s orientation, after possibly changing it. A positive return value means wide-character oriented. A negative return value means byte oriented. A return value of zero means undecided.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> Wide-character output to a byte oriented stream can be performed through the <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3) function with the <code>%lc</code> and <code>%ls</code> directives. </p>
<p> Char oriented output to a wide-character oriented stream can be performed through the <code><a href="/docs/linux/man/3-fwprintf/">fwprintf</a></code>(3) function with the <code>%c</code> and <code>%s</code> directives.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/3-fwprintf/">fwprintf</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
