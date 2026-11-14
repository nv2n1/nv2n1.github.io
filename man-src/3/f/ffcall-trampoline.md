---
title: "ffcall-trampoline(3)"
name: "ffcall-trampoline"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ffcall-trampoline/"
description: "trampoline – closures as first-class C functions"
---

<h2>NAME</h2>
<p> trampoline &#8211; closures as first-class C functions</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;trampoline.h&gt;</code> </p>
<p> <code>function = alloc_trampoline(address, variable, data);</code> </p>
<p> <code>free_trampoline(function);</code> </p>
<pre>
<code>is_trampoline(function)</code>
<code>trampoline_address(function)</code>
<code>trampoline_variable(function)</code>
<code>trampoline_data(function)</code>
</pre>
<h2>DESCRIPTION</h2>
<p> These functions implement <i>closures</i> as first-class C functions. A closure consists of a regular C function and a piece of data which gets passed to the C function when the closure is called. </p>
<p> Closures as <i>first-class C functions</i> means that they fit into a function pointer and can be called exactly like any other C function. <i>function</i><code> = alloc_trampoline(</code><i>address</i><code>, </code><i>variable</i><code>, </code><i>data</i><code>)</code> allocates a closure. When <i>function</i> gets called, it stores <i>data</i> in the variable <i>variable</i> and calls the C function at <i>address</i>. The function at <i>address</i> is responsible for fetching <i>data</i> out of <i>variable</i> immediately, before execution of any other function call. </p>
<p> This is much like <code>gcc</code>&#8216;s local functions, except that the GNU C local functions have dynamic extent (i.e. are deallocated when the creating function returns), while <i>trampoline</i> provides functions with indefinite extent: <i>function</i> is only deallocated when <code>free_trampoline(</code><i>function</i><code>)</code> is called. </p>
<p> <code>is_trampoline(</code><i>function</i><code>)</code> checks whether the C function <i>function</i> was produced by a call to <i>alloc_trampoline</i>. If this returns true, the arguments given to <i>alloc_trampoline</i> can be retrieved:</p>
<dl>
<dt>
<dd>
<p> <code>trampoline_address(</code><i>function</i><code>)</code> returns <i>address</i>, </p>
<p> <code>trampoline_variable(</code><i>function</i><code>)</code> returns <i>variable</i>, </p>
<p> <code>trampoline_data(</code><i>function</i><code>)</code> returns <i>data</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/3-varargs/">varargs</a></code>(3), <code><a href="/docs/linux/man/3-callback/">callback</a></code>(3) </p>
<h2>BUGS</h2>
<p> Passing the data through a global variable is not reentrant. Don&#8217;t call trampoline functions from within signal handlers. This is fixed in the <code><a href="/docs/linux/man/3-callback/">callback</a></code>(3) package. </p>
<h2>PORTING</h2>
<p> The way <code>gcc</code> builds local functions is described in the gcc source, file gcc-2.6.3/config/<i>cpu</i>/<i>cpu</i>.h. </p>
<h2>AUTHOR</h2>
<p> Bruno Haible &lt;bruno [at] clisp.org&gt; </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Many ideas were cribbed from the gcc source. </p>
<h2>Index</h2>
