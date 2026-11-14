---
title: "pcre2_convert_context_create(3)"
name: "pcre2_convert_context_create"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_convert_context_create/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_convert_context *pcre2_convert_context_create(</code>
<code> pcre2_general_context *</code><i>gcontext</i>);</pre>
<h2>Description</h2>
<p>This function is part of an experimental set of pattern conversion functions. It creates and initializes a new convert context. If its argument is NULL, <code>malloc()</code> is used to get the necessary memory; otherwise the memory allocation function within the general context is used. The result is NULL if the memory could not be obtained. The pattern conversion functions are described in the <code>pcre2convert</code> documentation. </p>
