---
title: "wcwidth(3)"
name: "wcwidth"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcwidth/"
description: "wcwidth – determine columns needed for a wide character"
---

<p>wcwidth &#8211; determine columns needed for a wide character</p>
<h2>Synopsis</h2>
<pre><code>#define _XOPEN_SOURCE /* See feature_test_macros(7) */
#include &lt;wchar.h&gt;

int wcwidth(wchar_t c);</code></pre>
<h2>Description</h2>
<p>The <code>wcwidth</code>() function returns the number of columns needed to represent the wide character <i>c</i>. If <i>c</i> is a printable wide character, the value is at least 0. If <i>c</i> is null wide character (L&#8217;
