---
title: "mb_cur_max(3)"
name: "mb_cur_max"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mb_cur_max/"
description: "MB_CUR_MAX – maximum length of a multibyte character in the current locale"
---

<p>MB_CUR_MAX &#8211; maximum length of a multibyte character in the current locale </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;</code></pre>
<h2>Description</h2>
<p>The <code>MB_CUR_MAX</code> macro defines an integer expression giving the maximum number of bytes needed to represent a single wide character in the current locale. This value is locale dependent and therefore not a compile-time constant.</p>
<h2>Return Value</h2>
<p>An integer in the range [1, <code>MB_LEN_MAX</code>]. The value 1 denotes traditional 8-bit encoded characters.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mb_len_max/">MB_LEN_MAX</a></code>(3), <code><a href="/docs/linux/man/3-mblen/">mblen</a></code>(3), <code><a href="/docs/linux/man/3-mbstowcs/">mbstowcs</a></code>(3), <code><a href="/docs/linux/man/3-mbtowc/">mbtowc</a></code>(3), <code><a href="/docs/linux/man/3-wcstombs/">wcstombs</a></code>(3), <code><a href="/docs/linux/man/3-wctomb/">wctomb</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
