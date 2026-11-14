---
title: "wcsrtombs(3)"
name: "wcsrtombs"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsrtombs/"
description: "wcsrtombs – convert a wide-character string to a multibyte string"
---

<p>wcsrtombs &#8211; convert a wide-character string to a multibyte string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

size_t wcsrtombs(char *dest, const wchar_t **src,
                 size_t len, mbstate_t *ps);</code></pre>
<h2>Description</h2>
<p>If <i>dest</i> is not NULL, the <code>wcsrtombs</code>() function converts the wide-character string <i>*src</i> to a multibyte string starting at <i>dest</i>. At most <i>len</i> bytes are written to <i>dest</i>. The shift state <i>*ps</i> is updated. The conversion is effectively performed by repeatedly calling <i>wcrtomb(dest, *src, ps)</i>, as long as this call succeeds, and then incrementing <i>dest</i> by the number of bytes written and <i>*src</i> by one. The conversion can stop for three reasons:</p>
<dl>
<dt>1.</p>
<dd>A wide character has been encountered that can not be represented as a multibyte sequence (according to the current locale). In this case, <i>*src</i> is left pointing to the invalid wide character, <i>(size_t)&nbsp;-1</i> is returned, and <i>errno</i> is set to <code>EILSEQ</code>.</p>
<dt>2.</p>
<dd>The length limit forces a stop. In this case, <i>*src</i> is left pointing to the next wide character to be converted, and the number of bytes written to <i>dest</i> is returned.</p>
<dt>3.</p>
<dd>The wide-character string has been completely converted, including the terminating null wide character (L&#8217;
