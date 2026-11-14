---
title: "wcsnrtombs(3)"
name: "wcsnrtombs"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsnrtombs/"
description: "wcsnrtombs – convert a wide-character string to a multibyte string"
---

<p>wcsnrtombs &#8211; convert a wide-character string to a multibyte string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

size_t wcsnrtombs(char *dest, const wchar_t **src, size_t nwc,
                  size_t len, mbstate_t *ps);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wcsnrtombs</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>wcsnrtombs</code>() function is like the <code><a href="/docs/linux/man/3-wcsrtombs/">wcsrtombs</a></code>(3) function, except that the number of wide characters to be converted, starting at <i>*src</i>, is limited to <i>nwc</i>. </p>
<p> If <i>dest</i> is not NULL, the <code>wcsnrtombs</code>() function converts at most <i>nwc</i> wide characters from the wide-character string <i>*src</i> to a multibyte string starting at <i>dest</i>. At most <i>len</i> bytes are written to <i>dest</i>. The shift state <i>*ps</i> is updated. The conversion is effectively performed by repeatedly calling <i>wcrtomb(dest, *src, ps)</i>, as long as this call succeeds, and then incrementing <i>dest</i> by the number of bytes written and <i>*src</i> by one. The conversion can stop for three reasons:</p>
<dl>
<dt>1.</p>
<dd>A wide character has been encountered that can not be represented as a multibyte sequence (according to the current locale). In this case, <i>*src</i> is left pointing to the invalid wide character, <i>(size_t)&nbsp;-1</i> is returned, and <i>errno</i> is set to <code>EILSEQ</code>.</p>
<dt>2.</p>
<dd><i>nwc</i> wide characters have been converted without encountering a null wide character (L&#8217;
