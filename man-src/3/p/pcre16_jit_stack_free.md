---
title: "pcre16_jit_stack_free(3)"
name: "pcre16_jit_stack_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre16_jit_stack_free/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
void pcre_jit_stack_free(pcre_jit_stack *stack);
void pcre16_jit_stack_free(pcre16_jit_stack *stack);
void pcre32_jit_stack_free(pcre32_jit_stack *stack);</code></pre>
<h2>Description</h2>
<p>This function is used to free a JIT stack that was created by <code>pcre[16|32]_jit_stack_alloc()</code> when it is no longer needed. For more details, see the <code>pcrejit</code> page. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
