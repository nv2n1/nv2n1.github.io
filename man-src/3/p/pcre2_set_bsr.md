---
title: "pcre2_set_bsr(3)"
name: "pcre2_set_bsr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_bsr/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_set_bsr(pcre2_compile_context *ccontext,
                  uint32_t value);</code></pre>
<h2>Description</h2>
<p>This function sets the convention for processing \R within a compile context. The second argument must be one of PCRE2_BSR_ANYCRLF or PCRE2_BSR_UNICODE. The result is zero for success or PCRE2_ERROR_BADDATA if the second argument is invalid. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
