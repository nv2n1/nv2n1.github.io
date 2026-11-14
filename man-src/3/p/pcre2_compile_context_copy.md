---
title: "pcre2_compile_context_copy(3)"
name: "pcre2_compile_context_copy"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_compile_context_copy/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_compile_context *pcre2_compile_context_copy(</code>
<code> pcre2_compile_context *</code><i>ccontext</i>);</pre>
<h2>Description</h2>
<p>This function makes a new copy of a compile context, using the memory allocation function that was used for the original context. The result is NULL if the memory cannot be obtained. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
