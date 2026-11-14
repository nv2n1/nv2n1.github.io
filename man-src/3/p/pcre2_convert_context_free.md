---
title: "pcre2_convert_context_free(3)"
name: "pcre2_convert_context_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_convert_context_free/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_convert_context_free(pcre2_convert_context *cvcontext);</code></pre>
<h2>Description</h2>
<p>This function is part of an experimental set of pattern conversion functions. It frees the memory occupied by a convert context, using the memory freeing function from the general context with which it was created, or <code>free()</code> if that was not set. If the argument is NULL, the function returns immediately without doing anything. The pattern conversion functions are described in the <code>pcre2convert</code> documentation. </p>
