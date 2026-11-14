---
title: "pcre2_convert_context_copy(3)"
name: "pcre2_convert_context_copy"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_convert_context_copy/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_convert_context *pcre2_convert_context_copy(</code>
<code> pcre2_convert_context *</code><i>cvcontext</i>);</pre>
<h2>Description</h2>
<p>This function is part of an experimental set of pattern conversion functions. It makes a new copy of a convert context, using the memory allocation function that was used for the original context. The result is NULL if the memory cannot be obtained. The pattern conversion functions are described in the <code>pcre2convert</code> documentation. </p>
