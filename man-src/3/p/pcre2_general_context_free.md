---
title: "pcre2_general_context_free(3)"
name: "pcre2_general_context_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_general_context_free/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_general_context_free(pcre2_general_context *gcontext);</code></pre>
<h2>Description</h2>
<p>This function frees the memory occupied by a general context, using the memory freeing function within the context, if set. If the argument is NULL, the function returns immediately without doing anything. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
