---
title: "mbsinit(3)"
name: "mbsinit"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbsinit/"
description: "mbsinit – test for initial shift state"
---

<h2 class="name">NAME</h2>
<p> mbsinit &#8211; test for initial shift state </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
int mbsinit(const mbstate_t *ps);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Character conversion between the multibyte representation and the wide character representation uses conversion state, of type <i>mbstate_t</i>. Conversion of a string uses a finite-state machine; when it is interrupted after the complete conversion of a number of characters, it may need to save a state for processing the remaining characters. Such a conversion state is needed for the sake of encodings such as ISO-2022 and UTF-7. </p>
<p> The initial state is the state at the beginning of conversion of a string. There are two kinds of state: the one used by multibyte to wide character conversion functions, such as <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3), and the one used by wide character to multibyte conversion functions, such as <code><a href="/docs/linux/man/3-wcsrtombs/">wcsrtombs</a></code>(3), but they both fit in a <i>mbstate_t</i>, and they both have the same representation for an initial state. </p>
<p> For 8-bit encodings, all states are equivalent to the initial state. For multibyte encodings like UTF-8, EUC-*, BIG5 or SJIS, the wide character to multibyte conversion functions never produce non-initial states, but the multibyte to wide-character conversion functions like <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3) do produce non-initial states when interrupted in the middle of a character. </p>
<p> One possible way to create an <i>mbstate_t</i> in initial state is to set it to zero: </p>
<p> mbstate_t state; memset(&amp;state, 0, sizeof(state)); </p>
<p> On Linux, the following works as well, but might generate compiler warnings: </p>
<p> mbstate_t state = { 0 }; </p>
<p> The function <code>mbsinit</code>() tests whether <i>*ps</i> corresponds to an initial state.</p>
<h2>RETURN VALUE</h2>
<p> <code>mbsinit</code>() returns nonzero if <i>*ps</i> is an initial state, or if <i>ps</i> is NULL. Otherwise, it returns 0.</p>
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
<td> <code>mbsinit</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>mbsinit</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mbrlen/">mbrlen</a></code>(3), <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3), <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3), <code><a href="/docs/linux/man/3-wcrtomb/">wcrtomb</a></code>(3), <code><a href="/docs/linux/man/3-wcsrtombs/">wcsrtombs</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
