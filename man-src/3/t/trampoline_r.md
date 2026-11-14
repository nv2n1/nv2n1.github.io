---
title: "trampoline_r(3)"
name: "trampoline_r"
section: "3"
letter: "t"
url: "/docs/linux/man/3-trampoline_r/"
description: "trampoline – closures as first-class C functions"
---

<p>trampoline &#8211; closures as first-class C functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;trampoline_r.h&gt;
function = alloc_trampoline_r(address, data0, data1);</code></pre>
<p> <code>free_trampoline_r(function);</code> </p>
<pre><code>is_trampoline_r(function)</code>
<code>trampoline_r_address(function)</code>
<code>trampoline_r_data0(function)</code>
<code>trampoline_r_data1(function)</code></pre>
<h2>Description</h2>
<p>These functions implement <i>closures</i> as first-class C functions. A closure consists of a regular C function and a piece of data which gets passed to the C function when the closure is called. Closures as <i>first-class C functions</i> means that they fit into a function pointer and can be called exactly like any other C function. <i>function</i><code> = alloc_trampoline_r(</code><i>address</i><code>, </code><i>data0</i><code>, </code><i>data1</i><code>)</code> allocates a closure. When <i>function</i> gets called, it stores in a special &quot;lexical chain register&quot; a pointer to a storage area containing <i>data0</i> in its first word and <i>data1</i> in its second word and calls the C function at <i>address</i>. The function at <i>address</i> is responsible for fetching <i>data0</i> and <i>data1</i> off the pointer. Note that the &quot;lexical chain register&quot; is a call-used register, i.e. is clobbered by function calls. This is much like <code>gcc</code>&#8216;s local functions, except that the GNU C local functions have dynamic extent (i.e. are deallocated when the creating function returns), while <i>trampoline</i> provides functions with indefinite extent: <i>function</i> is only deallocated when <code>free_trampoline_r(</code><i>function</i><code>)</code> is called. <code>is_trampoline_r(</code><i>function</i><code>)</code> checks whether the C function <i>function</i> was produced by a call to <i>alloc_trampoline_r</i>. If this returns true, the arguments given to <i>alloc_trampoline_r</i> can be retrieved:</p>
<dl>
<dd><code>trampoline_r_address(</code><i>function</i><code>)</code> returns <i>address</i>, <code>trampoline_r_data0(</code><i>function</i><code>)</code> returns <i>data0</i>, <code>trampoline_r_data1(</code><i>function</i><code>)</code> returns <i>data1</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-trampoline/">trampoline</a></code>(3), <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/3-varargs/">varargs</a></code>(3) </p>
<h2>Porting</h2>
<p>The way <code>gcc</code> builds local functions is described in the gcc source, file gcc-2.6.3/config/<i>cpu</i>/<i>cpu</i>.h.</p>
<h2>Author</h2>
<p>Bruno Haible &lt;bruno [at] clisp.org&gt;</p>
<h2>Acknowledgements</h2>
<p>Many ideas were cribbed from the gcc source.</p>
