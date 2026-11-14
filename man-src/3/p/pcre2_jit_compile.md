---
title: "pcre2_jit_compile(3)"
name: "pcre2_jit_compile"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_jit_compile/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_jit_compile(pcre2_code *code, uint32_t options);</code></pre>
<h2>Description</h2>
<p>This function requests JIT compilation, which, if the just-in-time compiler is available, further processes a compiled pattern into machine code that executes much faster than the <code>pcre2_match()</code> interpretive matching function. Full details are given in the <code>pcre2jit</code> documentation. The first argument is a pointer that was returned by a successful call to <code>pcre2_compile()</code>, and the second must contain one or more of the following bits:<br />
&nbsp;<wbr>&nbsp;PCRE2_JIT_COMPLETE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compile code for full matching<br />
&nbsp;<wbr>&nbsp;PCRE2_JIT_PARTIAL_SOFT&nbsp;<wbr>&nbsp;compile code for soft partial matching<br />
&nbsp;<wbr>&nbsp;PCRE2_JIT_PARTIAL_HARD&nbsp;<wbr>&nbsp;compile code for hard partial matching There is also an obsolete option called PCRE2_JIT_INVALID_UTF, which has been superseded by the <code>pcre2_compile()</code> option PCRE2_MATCH_INVALID_UTF. The old option is deprecated and may be removed in the future. The yield of the function is 0 for success, or a negative error code otherwise. In particular, PCRE2_ERROR_JIT_BADOPTION is returned if JIT is not supported or if an unknown bit is set in <i>options</i>. The function can also return PCRE2_ERROR_NOMEMORY if JIT is unable to allocate executable memory for the compiler, even if it was because of a system security restriction. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
