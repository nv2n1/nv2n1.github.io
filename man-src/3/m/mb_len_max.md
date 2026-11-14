---
title: "mb_len_max(3)"
name: "mb_len_max"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mb_len_max/"
description: "MB_LEN_MAX – maximum multibyte length of a character across all locales"
---

<p>MB_LEN_MAX &#8211; maximum multibyte length of a character across all locales </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;limits.h&gt;</code></pre>
<h2>Description</h2>
<p>The <code>MB_LEN_MAX</code> macro is the maximum number of bytes needed to represent a single wide character, in any of the supported locales.</p>
<h2>Return Value</h2>
<p>A constant integer greater than zero.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>Notes</h2>
<p>The entities <code>MB_LEN_MAX</code> and <i>sizeof(wchar_t)</i> are totally unrelated. In glibc, <code>MB_LEN_MAX</code> is typically 16 (6 in glibc versions earlier than 2.2), while <i>sizeof(wchar_t)</i> is 4.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mb_cur_max/">MB_CUR_MAX</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
