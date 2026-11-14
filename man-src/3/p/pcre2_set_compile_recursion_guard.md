---
title: "pcre2_set_compile_recursion_guard(3)"
name: "pcre2_set_compile_recursion_guard"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_compile_recursion_guard/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_set_compile_recursion_guard(pcre2_compile_context *ccontext,
                                      int (*guard_function)(uint32_t, void *), void *user_data);</code></pre>
<h2>Description</h2>
<p>This function defines, within a compile context, a function that is called whenever <code>pcre2_compile()</code> starts to compile a parenthesized part of a pattern. The first argument to the function gives the current depth of parenthesis nesting, and the second is user data that is supplied when the function is set up. The callout function should return zero if all is well, or non-zero to force an error. This feature is provided so that applications can check the available system stack space, in order to avoid running out. The result of <code>pcre2_set_compile_recursion_guard()</code> is always zero. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
