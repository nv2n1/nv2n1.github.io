---
title: "pcre2_jit_free_unused_memory(3)"
name: "pcre2_jit_free_unused_memory"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_jit_free_unused_memory/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_jit_free_unused_memory(pcre2_general_context *gcontext);</code></pre>
<h2>Description</h2>
<p>This function frees unused JIT executable memory. The argument is a general context, for custom memory management, or NULL for standard memory management. JIT memory allocation retains some memory in order to improve future JIT compilation speed. In low memory conditions, <code>pcre2_jit_free_unused_memory() can be used to cause this memory to be freed. There is a complete description of the PCRE2 native API in the pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
