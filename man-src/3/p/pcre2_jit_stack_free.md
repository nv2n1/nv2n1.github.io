---
title: "pcre2_jit_stack_free(3)"
name: "pcre2_jit_stack_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_jit_stack_free/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_jit_stack_free(pcre2_jit_stack *jit_stack);</code></pre>
<h2>Description</h2>
<p>This function is used to free a JIT stack that was created by <code>pcre2_jit_stack_create()</code> when it is no longer needed. If the argument is NULL, the function returns immediately without doing anything. For more details, see the <code>pcre2jit</code> page. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
