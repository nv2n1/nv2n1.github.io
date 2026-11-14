---
title: "pcre2_set_recursion_memory_management(3)"
name: "pcre2_set_recursion_memory_management"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_recursion_memory_management/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_set_recursion_memory_management(
    pcre2_match_context *mcontext,
    void *(*private_malloc)(PCRE2_SIZE, void *),
    void (*private_free)(void *, void *), void *memory_data);</code></pre>
<h2>Description</h2>
<p>From release 10.30 onwards, this function is obsolete and does nothing. The result is always zero. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
