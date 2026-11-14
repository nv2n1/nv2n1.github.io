---
title: "callback(3)"
name: "callback"
section: "3"
letter: "c"
url: "/docs/linux/man/3-callback/"
description: "callback – closures with variable arguments as first-class C functions"
---

<h2>NAME</h2>
<p> callback &#8211; closures with variable arguments as first-class C functions</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/callback.h">callback.h</a>&gt;</code> </p>
<pre><code>
void function(data, alist) void *data;
va_alist alist;
{
    va_start_type(alist[, return_type]);
    arg = va_arg_type(alist[, arg_type]);
    va_return_type(alist[[, return_type ], return_value]);
}
</code></pre>
<p> <i>callback</i><code> = alloc_callback(</code><i>&amp;function</i><code>, </code><i>data</i><code>);</code> </p>
<p> <code>free_callback(</code><i>callback</i><code>);</code> </p>
<pre>
<code>is_callback(</code><i>callback</i><code>)</code>
<code>callback_address(</code><i>callback</i><code>)</code>
<code>callback_data(</code><i>callback</i><code>)</code>
</pre>
<h2>DESCRIPTION</h2>
<p> These functions implement <i>closures</i> with variable arguments as first-class C functions. </p>
<p> Closures as <i>first-class C functions</i> means that they fit into a function pointer and can be called exactly like any other C function. Moreover, they can be called with variable arguments and can return variable return values. </p>
<p> <i>callback</i><code> = alloc_callback(</code><i>&amp;function</i><code>, </code><i>data</i><code>)</code> allocates a callback. When <i>callback</i> gets called, it arranges to call <i>function</i>, passing <i>data</i> as first argument and, as second argument, the entire sequence of arguments passed to <i>callback</i>. </p>
<p> Function calling conventions differ considerably on different machines, therefore the arguments are accessed and the result value is stored through the same macros as used by the <i>vacall</i> package, see below. </p>
<p> The callbacks are functions with indefinite extent: <i>callback</i> is only deallocated when <code>free_callback(</code><i>callback</i><code>)</code> is called. </p>
<p> <code>is_callback(</code><i>callback</i><code>)</code> checks whether the C function <i>callback</i> was produced by a call to <i>alloc_callback</i>. If this returns true, the arguments given to <i>alloc_callback</i> can be retrieved:</p>
<dl>
<dt>
<dd>
<p> <code>callback_address(</code><i>callback</i><code>)</code> returns <i>&amp;function</i>, </p>
<p> <code>callback_data(</code><i>callback</i><code>)</code> returns <i>data</i>.</dl>
<h2>VACALL MACROS</h2>
<p> Within <i>function</i>, the following macros can be used to walk through the argument list and specify a return value:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>va_start_</code><i>type</i><code>(</code><i>alist</i><code>[, </code><i>return_type</i><code>]);</code></p>
<dd> starts the walk through the argument list and specifies the return type.</p>
<dt><i>arg</i><code> = va_arg_</code><i>type</i><code>(</code><i>alist</i><code>[, </code><i>arg_type</i><code>]);</code></p>
<dd> fetches the next argument from the argument list.</p>
<dt><code>va_return_</code><i>type</i><code>(</code><i>alist</i><code>[[, </code><i>return_type</i><code>], </code><i>return_value</i><code>]);</code></p>
<dd> ends the walk through the argument list and specifies the return value.</dl>
</dl>
<p> The <i>type</i> in <code>va_start_</code><i>type</i> and <code>va_return_</code><i>type</i> shall be one of <code>void</code>, <code>int</code>, <code>uint</code>, <code>long</code>, <code>ulong</code>, <code>longlong</code>, <code>ulonglong</code>, <code>double</code>, <code>struct</code>, <code>ptr</code> or (for ANSI C calling conventions only) <code>char</code>, <code>schar</code>, <code>uchar</code>, <code>short</code>, <code>ushort</code>, <code>float</code>, depending on the class of <i>return_type</i>. </p>
<p> The <i>type</i> specifiers in <code>va_start_</code><i>type</i> and <code>va_return_</code><i>type</i> must be the same. The <i>return_type</i> specifiers passed to <code>va_start_</code><i>type</i> and <code>va_return_</code><i>type</i> must be the same. </p>
<p> The <i>type</i> in <code>va_arg_</code><i>type</i> shall be one of <code>int</code>, <code>uint</code>, <code>long</code>, <code>ulong</code>, <code>longlong</code>, <code>ulonglong</code>, <code>double</code>, <code>struct</code>, <code>ptr</code> or (for ANSI C calling conventions only) <code>char</code>, <code>schar</code>, <code>uchar</code>, <code>short</code>, <code>ushort</code>, <code>float</code>, depending on the class of <i>arg_type</i>. </p>
<p> In <code>va_start_struct(</code><i>alist</i><code>, </code><i>return_type</i><code>, </code><i>splittable</i><code>);</code> the <i>splittable</i> flag specifies whether the struct <i>return_type</i> can be returned in registers such that every struct field fits entirely in a single register. This needs to be specified for structs of size 2*sizeof(long). For structs of size &lt;= sizeof(long), <i>splittable</i> is ignored and assumed to be 1. For structs of size &gt; 2*sizeof(long), <i>splittable</i> is ignored and assumed to be 0. There are some handy macros for this: </p>
<pre>
<code>va_word_splittable_1 (</code><i>type1</i><code>)</code>
<code>va_word_splittable_2 (</code><i>type1</i><code>, </code><i>type2</i><code>)</code>
<code>va_word_splittable_3 (</code><i>type1</i><code>, </code><i>type2</i><code>, </code><i>type3</i><code>)</code>
<code>va_word_splittable_4 (</code><i>type1</i><code>, </code><i>type2</i><code>, </code><i>type3</i><code>, </code><i>type4</i><code>)</code>
</pre>
<p> For a struct with three slots </p>
<pre><code>
struct {
    type1 id1;
    type2 id2;
    type3 id3;
}
</code></pre>
<p> you can specify <i>splittable</i> as <code>va_word_splittable_3 (</code><i>type1</i><code>, </code><i>type2</i><code>, </code><i>type3</i><code>)</code> . </p>
<h2>NOTES</h2>
<p> Functions which want to emulate Kernighan &amp; Ritchie style functions (i.e., in ANSI C, functions without a typed argument list) cannot use the <i>type</i> values <code>char</code>, <code>schar</code>, <code>uchar</code>, <code>short</code>, <code>ushort</code>, <code>float</code>. As prescribed by the default K&amp;R C expression promotions, they have to use <code>int</code> instead of <code>char</code>, <code>schar</code>, <code>uchar</code>, <code>short</code>, <code>ushort</code> and <code>double</code> instead of <code>float</code>. </p>
<p> The macros <code>va_start_longlong()</code>, <code>va_start_ulonglong()</code>, <code>va_return_longlong()</code>, <code>va_return_ulonglong()</code>, <code>va_arg_longlong()</code> and <code>va_arg_ulonglong()</code> work only if the C compiler has a working <code>long long</code> 64-bit integer type. </p>
<p> The struct types used in <code>va_start_struct()</code> and <code>va_struct()</code> must only contain (signed or unsigned) int, long, long long or pointer fields. Struct types containing (signed or unsigned) char, short, float, double or other structs are not supported. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-vacall/">vacall</a></code>(3), <code><a href="/docs/linux/man/3-trampoline/">trampoline</a></code>(3). </p>
<h2>BUGS</h2>
<p> The current implementations have been tested on a selection of common cases but there are probably still many bugs. </p>
<p> There are typically built-in limits on the size of the argument-list, which may also include the size of any structure arguments. </p>
<p> The decision whether a struct is to be returned in registers or in memory considers only the struct&#8217;s size and alignment. This is inaccurate: for example, gcc on m68k-next returns <code>struct { char a,b,c; }</code> in registers and <code>struct { char a[3]; }</code> in memory, although both types have the same size and the same alignment. </p>
<p> <code>&lt;<a href="file:/usr/include/callback.h">callback.h</a>&gt;</code> cannot be included when <code>&lt;<a href="file:/usr/include/varargs.h">varargs.h</a>&gt;</code> or <code>&lt;<a href="file:/usr/include/stdarg.h">stdarg.h</a>&gt;</code> is included. (Name clash for <code>va_alist</code>.) </p>
<p> The argument list can only be walked once. </p>
<h2>NON-BUGS</h2>
<p> All information is passed in CPU registers and the stack. The <code>callback</code> package is therefore multithread-safe. </p>
<h2>PORTING</h2>
<p> Porting <code>callback</code> consists in first porting the <code>vacall</code> and <code>trampoline</code> packages, then choosing a CPU register for passing the closure from <code>trampoline</code> to <code>vacall</code>. This register is normally the register designated by STATIC_CHAIN_REGNUM in the gcc source, file gcc-2.7.2/config/<i>cpu</i>/<i>cpu</i>.h. </p>
<h2>AUTHOR</h2>
<p> Bruno Haible &lt;bruno [at] clisp.org&gt; </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Many ideas were cribbed from the gcc source. </p>
<h2>Index</h2>
