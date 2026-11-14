---
title: "pcre2_jit_stack_assign(3)"
name: "pcre2_jit_stack_assign"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_jit_stack_assign/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_jit_stack_assign(pcre2_match_context *mcontext,
                            pcre2_jit_callback callback_function, void *callback_data);</code></pre>
<h2>Description</h2>
<p>This function provides control over the memory used by JIT as a run-time stack when <code>pcre2_match()</code> or <code>pcre2_jit_match()</code> is called with a pattern that has been successfully processed by the JIT compiler. The information that determines which stack is used is put into a match context that is subsequently passed to a matching function. The arguments of this function are:<br />
&nbsp;<wbr>&nbsp;mcontext&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a pointer to a match context<br />
&nbsp;<wbr>&nbsp;callback&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a callback function<br />
&nbsp;<wbr>&nbsp;callback_data&nbsp;<wbr>&nbsp;a JIT stack or a value to be passed to the callback If <i>mcontext</i> is NULL, the function returns immediately, without doing anything. If <i>callback</i> is NULL and <i>callback_data</i> is NULL, an internal 32KiB block on the machine stack is used. If <i>callback</i> is NULL and <i>callback_data</i> is not NULL, <i>callback_data</i> must be a valid JIT stack, the result of calling <code>pcre2_jit_stack_create()</code>. If <i>callback</i> not NULL, it is called with <i>callback_data</i> as an argument at the start of matching, in order to set up a JIT stack. If the result is NULL, the internal 32KiB stack is used; otherwise the return value must be a valid JIT stack, the result of calling <code>pcre2_jit_stack_create()</code>. You may safely use the same JIT stack for multiple patterns, as long as they are all matched in the same thread. In a multithread application, each thread must use its own JIT stack. For more details, see the <code>pcre2jit</code> page. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
