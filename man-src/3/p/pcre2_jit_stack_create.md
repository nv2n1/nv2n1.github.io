---
title: "pcre2_jit_stack_create(3)"
name: "pcre2_jit_stack_create"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_jit_stack_create/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_jit_stack *pcre2_jit_stack_create(PCRE2_SIZE </code><i>startsize</i>,
<code> PCRE2_SIZE </code><i>maxsize</i>, pcre2_general_context *<i>gcontext</i>);</pre>
<h2>Description</h2>
<p>This function is used to create a stack for use by the code compiled by the JIT compiler. The first two arguments are a starting size for the stack, and a maximum size to which it is allowed to grow. The final argument is a general context, for memory allocation functions, or NULL for standard memory allocation. The result can be passed to the JIT run-time code by calling <code>pcre2_jit_stack_assign()</code> to associate the stack with a compiled pattern, which can then be processed by <code>pcre2_match()</code> or <code>pcre2_jit_match()</code>. A maximum stack size of 512KiB to 1MiB should be more than enough for any pattern. For more details, see the <code>pcre2jit</code> page. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
