---
title: "pcre2_set_parens_nest_limit(3)"
name: "pcre2_set_parens_nest_limit"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_parens_nest_limit/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_set_parens_nest_limit(pcre2_compile_context *ccontext,
                                uint32_t value);</code></pre>
<h2>Description</h2>
<p>This function sets, in a compile context, the maximum depth of nested parentheses in a pattern. The result is always zero. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
