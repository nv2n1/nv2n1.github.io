---
title: "pcre2_set_max_pattern_length(3)"
name: "pcre2_set_max_pattern_length"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_max_pattern_length/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_set_max_pattern_length(pcre2_compile_context *ccontext,
                                 PCRE2_SIZE value);</code></pre>
<h2>Description</h2>
<p>This function sets, in a compile context, the maximum text length (in code units) of the pattern that can be compiled. The result is always zero. If a longer pattern is passed to <code>pcre2_compile()</code> there is an immediate error return. The default is effectively unlimited, being the largest value a PCRE2_SIZE variable can hold. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
