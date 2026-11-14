---
title: "pcre2_code_copy_with_tables(3)"
name: "pcre2_code_copy_with_tables"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_code_copy_with_tables/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_code *pcre2_code_copy_with_tables(const pcre2_code *</code><i>code</i>);</pre>
<h2>Description</h2>
<p>This function makes a copy of the memory used for a compiled pattern, excluding any memory used by the JIT compiler. Without a subsequent call to <code>pcre2_jit_compile()</code>, the copy can be used only for non-JIT matching. Unlike <code>pcre2_code_copy()</code>, a separate copy of the character tables is also made, with the new code pointing to it. This memory will be automatically freed when <code>pcre2_code_free()</code> is called. The yield of the function is NULL if <i>code</i> is NULL or if sufficient memory cannot be obtained. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
