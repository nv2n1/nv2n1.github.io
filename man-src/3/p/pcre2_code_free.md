---
title: "pcre2_code_free(3)"
name: "pcre2_code_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_code_free/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_code_free(pcre2_code *code);</code></pre>
<h2>Description</h2>
<p>If <i>code</i> is NULL, this function does nothing. Otherwise, <i>code</i> must point to a compiled pattern. This function frees its memory, including any memory used by the JIT compiler. If the compiled pattern was created by a call to <code>pcre2_code_copy_with_tables()</code>, the memory for the character tables is also freed. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
