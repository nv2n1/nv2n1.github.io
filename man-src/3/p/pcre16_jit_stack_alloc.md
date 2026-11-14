---
title: "pcre16_jit_stack_alloc(3)"
name: "pcre16_jit_stack_alloc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre16_jit_stack_alloc/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;</code></pre>
<pre><code>pcre_jit_stack *pcre_jit_stack_alloc(int </code><i>startsize</i>,
<code> int </code><i>maxsize</i>);
<code>pcre16_jit_stack *pcre16_jit_stack_alloc(int </code><i>startsize</i>,
<code> int </code><i>maxsize</i>);
<code>pcre32_jit_stack *pcre32_jit_stack_alloc(int </code><i>startsize</i>,
<code> int </code><i>maxsize</i>);</pre>
<h2>Description</h2>
<p>This function is used to create a stack for use by the code compiled by the JIT optimization of <code>pcre[16|32]_study()</code>. The arguments are a starting size for the stack, and a maximum size to which it is allowed to grow. The result can be passed to the JIT run-time code by <code>pcre[16|32]_assign_jit_stack()</code>, or that function can set up a callback for obtaining a stack. A maximum stack size of 512K to 1M should be more than enough for any pattern. For more details, see the <code>pcrejit</code> page. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
