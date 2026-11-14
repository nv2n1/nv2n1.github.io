---
title: "pcre_assign_jit_stack(3)"
name: "pcre_assign_jit_stack"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre_assign_jit_stack/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
void pcre_assign_jit_stack(pcre_extra *extra,
                           pcre_jit_callback callback, void *data);

void pcre16_assign_jit_stack(pcre16_extra *extra,
                             pcre16_jit_callback callback, void *data);

void pcre32_assign_jit_stack(pcre32_extra *extra,
                             pcre32_jit_callback callback, void *data);</code></pre>
<h2>Description</h2>
<p>This function provides control over the memory used as a stack at run-time by a call to <code>pcre[16|32]_exec()</code> with a pattern that has been successfully compiled with JIT optimization. The arguments are:<br />
&nbsp;<wbr>&nbsp;extra&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the data pointer returned by&nbsp;<code>pcre[16|32]_study()</code><br />
&nbsp;<wbr>&nbsp;callback&nbsp;<wbr>&nbsp;a callback function<br />
&nbsp;<wbr>&nbsp;data&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a JIT stack or a value to be passed to the callback<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function If <i>callback</i> is NULL and <i>data</i> is NULL, an internal 32K block on the machine stack is used. If <i>callback</i> is NULL and <i>data</i> is not NULL, <i>data</i> must be a valid JIT stack, the result of calling <code>pcre[16|32]_jit_stack_alloc()</code>. If <i>callback</i> not NULL, it is called with <i>data</i> as an argument at the start of matching, in order to set up a JIT stack. If the result is NULL, the internal 32K stack is used; otherwise the return value must be a valid JIT stack, the result of calling <code>pcre[16|32]_jit_stack_alloc()</code>. You may safely assign the same JIT stack to multiple patterns, as long as they are all matched in the same thread. In a multithread application, each thread must use its own JIT stack. For more details, see the <code>pcrejit</code> page. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
