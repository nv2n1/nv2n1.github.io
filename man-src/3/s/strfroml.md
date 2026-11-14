---
title: "strfroml(3)"
name: "strfroml"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strfroml/"
description: "strfromd, strfromf, strfroml – convert a floating-point value into a string"
---

<p>strfromd, strfromf, strfroml &#8211; convert a floating-point value into a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

int strfromd(char *restrict str, size_t n,
             const char *restrict format, double fp);
int strfromf(char *restrict str, size_t n,
             const char *restrict format, float fp);
int strfroml(char *restrict str, size_t n,
             const char *restrict format, long double fp);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strfromd</code>(), <code>strfromf</code>(), <code>strfroml</code>():</p>
<dl>
<dd>__STDC_WANT_IEC_60559_BFP_EXT__</dl>
<h2>Description</h2>
<p>These functions convert a floating-point value, <i>fp</i>, into a string of characters, <i>str</i>, with a configurable <i>format</i> string. At most <i>n</i> characters are stored into <i>str</i>. The terminating null byte (&#8216;
