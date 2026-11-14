---
title: "pcre2_jit_match(3)"
name: "pcre2_jit_match"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_jit_match/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_jit_match(const pcre2_code *code, PCRE2_SPTR subject,
                    PCRE2_SIZE length, PCRE2_SIZE startoffset,
                    uint32_t options, pcre2_match_data *match_data,
                    pcre2_match_context *mcontext);</code></pre>
<h2>Description</h2>
<p>This function matches a compiled regular expression that has been successfully processed by the JIT compiler against a given subject string, using a matching algorithm that is similar to Perl&#8217;s. It is a &quot;fast path&quot; interface to JIT, and it bypasses some of the sanity checks that <code>pcre2_match()</code> applies. Its arguments are exactly the same as for <code>pcre2_match()</code>. The supported options are PCRE2_NOTBOL, PCRE2_NOTEOL, PCRE2_NOTEMPTY, PCRE2_NOTEMPTY_ATSTART, PCRE2_PARTIAL_HARD, and PCRE2_PARTIAL_SOFT. Unsupported options are ignored. The subject string is not checked for UTF validity. The return values are the same as for <code>pcre2_match()</code> plus PCRE2_ERROR_JIT_BADOPTION if a matching mode (partial or complete) is requested that was not compiled. For details of partial matching, see the <code>pcre2partial</code> page. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the JIT API in the <code>pcre2jit</code> page. </p>
