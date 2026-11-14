---
title: "pcre2_converted_pattern_free(3)"
name: "pcre2_converted_pattern_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_converted_pattern_free/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_converted_pattern_free(PCRE2_UCHAR *converted_pattern);</code></pre>
<h2>Description</h2>
<p>This function is part of an experimental set of pattern conversion functions. It frees the memory occupied by a converted pattern that was obtained by calling <code>pcre2_pattern_convert()</code> with arguments that caused it to place the converted pattern into newly obtained heap memory. If the argument is NULL, the function returns immediately without doing anything. The pattern conversion functions are described in the <code>pcre2convert</code> documentation. </p>
