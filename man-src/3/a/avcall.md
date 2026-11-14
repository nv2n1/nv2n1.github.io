---
title: "avcall(3)"
name: "avcall"
section: "3"
letter: "a"
url: "/docs/linux/man/3-avcall/"
description: "avcall – build a C argument list incrementally and call a C function on it."
---

<h2>NAME</h2>
<p> avcall &#8211; build a C argument list incrementally and call a C function on it.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/avcall.h">avcall.h</a>&gt;</code> </p>
<p> <code>av_alist </code><i>alist</i><code>;</code> </p>
<p> <code>av_start_</code><i>type</i><code>(</code><i>alist</i><code>, </code><i>&amp;func</i> [[<code>, </code><i>return_type</i>]<code>, </code><i>&amp;return_value</i>]<code>);</code> </p>
<p> <code>av_</code><i>type</i><code>(</code><i>alist</i><code>, </code>[<i>arg_type</i><code>,</code>] <i>value</i><code>);</code> </p>
<p> <code>av_call(</code><i>alist</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This set of macros builds an argument list for a C function and calls the function on it. It significantly reduces the amount of `glue&#8217; code required for parsers, debuggers, imbedded interpreters, C extensions to application programs and other situations where collections of functions need to be called on lists of externally-supplied arguments. </p>
<p> Function calling conventions differ considerably on different machines and <i>avcall</i> attempts to provide some degree of isolation from such architecture dependencies. </p>
<p> The interface is like <code><a href="/docs/linux/man/3-stdarg/">stdarg</a></code>(3) in reverse. All of the macros return 0 for success, &lt; 0 for failure (e.g., argument list overflow or type-not-supported).</p>
<dl>
<dt>
<dd>
<dl>
<dt>(1)</p>
<dd> <code>#include &lt;<a href="file:/usr/include/avcall.h">avcall.h</a>&gt;</code> </p>
<pre>
and declare the argument list structure
<code>av_alist </code><i>alist</i><code>;</code>
</pre>
<dt>(2)</p>
<dd> Set any special flags. This is architecture and compiler dependent. Compiler options that affect passing conventions may need to be flagged by <code>#define</code>s before the <code>#include &lt;<a href="file:/usr/include/avcall.h">avcall.h</a>&gt;</code> statement. However, the <i>configure</i> script should have determined which <code>#define</code>s are needed and put them at the top of <code>avcall.h</code>.</p>
<dt>(3)</p>
<dd> Initialize the alist with the function address and return value pointer (if any). There is a separate macro for each simple return type ([u]char, [u]short, [u]int, [u]long, [u]longlong, float, double, where `u&#8217; indicates `unsigned&#8217;). The macros for functions returning structures or pointers require an explicit type argument.</dl>
<p> E.g., </p>
<p> <code>av_start_int (</code><i>alist</i><code>, </code><i>&amp;func</i><code>, </code><i>&amp;int_return</i><code>);</code> </p>
<p> <code>av_start_double (</code><i>alist</i><code>, </code><i>&amp;func</i><code>, </code><i>&amp;double_return</i><code>);</code> </p>
<p> <code>av_start_void (</code><i>alist</i><code>, </code><i>&amp;func</i><code>);</code> </p>
<pre>
<code>av_start_struct (</code><i>alist</i><code>, </code><i>&amp;func</i><code>, </code><i>struct_type</i><code>, </code><i>splittable</i><code>, </code>
<i>&amp;struct_return</i><code>);</code>
</pre>
<pre>
<code>av_start_ptr (</code><i>alist</i><code>, </code><i>&amp;func</i><code>, </code><i>pointer_type</i><code>, </code>
<i>&amp;pointer_return</i><code>);</code>
</pre>
<p> The <i>splittable</i> flag specifies whether the <i>struct_type</i> can be returned in registers such that every struct field fits entirely in a single register. This needs to be specified for structs of size 2*sizeof(long). For structs of size &lt;= sizeof(long), <i>splittable</i> is ignored and assumed to be 1. For structs of size &gt; 2*sizeof(long), <i>splittable</i> is ignored and assumed to be 0. There are some handy macros for this: </p>
<pre>
<code>av_word_splittable_1 (</code><i>type1</i><code>)</code>
<code>av_word_splittable_2 (</code><i>type1</i><code>, </code><i>type2</i><code>)</code>
<code>av_word_splittable_3 (</code><i>type1</i><code>, </code><i>type2</i><code>, </code><i>type3</i><code>)</code>
<code>av_word_splittable_4 (</code><i>type1</i><code>, </code><i>type2</i><code>, </code><i>type3</i><code>, </code><i>type4</i><code>)</code>
</pre>
<p> For a struct with three slots </p>
<pre><code>
struct {
    type1 id1;
    type2 id2;
    type3 id3;
}
</code></pre>
<p> you can specify <i>splittable</i> as <code>av_word_splittable_3 (</code><i>type1</i><code>, </code><i>type2</i><code>, </code><i>type3</i><code>)</code> .</p>
<dl>
<dt>(4)</p>
<dd> Push the arguments on to the list in order. Again there is a macro for each simple built-in type, and the macros for structure and pointer arguments require an extra type argument:</dl>
<p> <code>av_int (</code><i>alist</i><code>, </code><i>int_value</i><code>);</code> </p>
<p> <code>av_double (</code><i>alist</i><code>, </code><i>double_value</i><code>);</code> </p>
<p> <code>av_struct (</code><i>alist</i><code>, </code><i>struct_or_union_type</i><code>, </code><i>struct_value</i><code>);</code> </p>
<p> <code>av_ptr (</code><i>alist</i><code>, </code><i>pointer_type</i><code>, </code><i>pointer_value</i><code>);</code></p>
<dl>
<dt>(5)</p>
<dd> Call the function, set the return value, and tidy up:</dl>
<p> <code>av_call (</code><i>alist</i><code>);</code></dl>
<h2>NOTES</h2>
<p> (1) Functions whose first declaration is in Kernighan &amp; Ritchie style (i.e., without a typed argument list) MUST use default K&amp;R C expression promotions (char and short to int, float to double) whether they are compiled by a K&amp;R or an ANSI compiler, because the true argument types may not be known at the call point. Such functions typically back-convert their arguments to the declared types on function entry. (In fact, the only way to pass a true char, short or float in K&amp;R C is by an explicit cast: <code>func((char)c,(float)f)</code> ). Similarly, some K&amp;R compilers (such as Sun cc on the sparc) actually return a float as a double. </p>
<p> Hence, for arguments of functions declared in K&amp;R style you should use <code>av_int()</code> and <code>av_double()</code> rather than <code>av_char(),</code> <code>av_short()</code> or <code>av_float().</code> If you use a K&amp;R compiler, the avcall header files may be able to detect this and define <code>av_float(),</code> etc, appropriately, but with an ANSI compiler there is no way <i>avcall</i> can know how a function was declared, so you have to correct the argument types yourself. </p>
<p> (2) The explicit type arguments of the <code>av_struct() </code> and <code>av_ptr() </code> macros are typically used to calculate size, alignment, and passing conventions. This may not be sufficient for some machines with unusual structure and pointer handling: in this case additional <code>av_start_</code><i>type</i><code>()</code> and <code>av_</code><i>type</i><code>()</code> macros may be defined. </p>
<p> (3) The macros <code>av_start_longlong()</code>, <code>av_start_ulonglong()</code>, <code>av_longlong()</code> and <code>av_ulonglong()</code> work only if the C compiler has a working <code>long long</code> 64-bit integer type. </p>
<p> (4) The struct types used in <code>av_start_struct()</code> and <code>av_struct()</code> must only contain (signed or unsigned) int, long, long long or pointer fields. Struct types containing (signed or unsigned) char, short, float, double or other structs are not supported. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-stdarg/">stdarg</a></code>(3), <code><a href="/docs/linux/man/3-varargs/">varargs</a></code>(3). </p>
<h2>BUGS</h2>
<p> The current implementations have been tested on a selection of common cases but there are probably still many bugs. </p>
<p> There are typically built-in limits on the size of the argument-list, which may also include the size of any structure arguments. </p>
<p> The decision whether a struct is to be returned in registers or in memory considers only the struct&#8217;s size and alignment. This is inaccurate: for example, gcc on m68k-next returns <code>struct { char a,b,c; }</code> in registers and <code>struct { char a[3]; }</code> in memory, although both types have the same size and the same alignment. </p>
<h2>NON-BUGS</h2>
<p> All information is passed in CPU registers and the stack. The <code>avcall</code> package is therefore multithread-safe. </p>
<h2>PORTING AVCALL</h2>
<p> Ports, bug-fixes, and suggestions are most welcome. The macros required for argument pushing are pretty grungy, but it does seem to be possible to port avcall to a range of machines. Ports to non-standard or non-32-bit machines are especially welcome so we can sort the interface out before it&#8217;s too late. </p>
<p> Knowledge about argument passing conventions can be found in the gcc source, file gcc-2.6.3/config/<i>cpu</i>/<i>cpu</i>.h, section &quot;Stack layout; function entry, exit and calling.&quot; </p>
<p> Some of the grunge is usually handled by a C or assembly level glue routine that actually pushes the arguments, calls the function and unpacks any return value. This is called __builtin_avcall(). A precompiled assembler version for people without gcc is also made available. The routine should ideally have flags for the passing conventions of other compilers. </p>
<p> Many of the current routines waste a lot of stack space and generally do hairy things to stack frames &#8211; a bit more assembly code would probably help things along quite a bit here. </p>
<h2>AUTHOR</h2>
<p> Bill Triggs &lt;Bill.Triggs [at] inrialpes.fr&gt;. </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Some initial ideas were stolen from the C interface to the Zelk extensions to Oliver Laumann&#8217;s Elk scheme interpreter by J.P.Lewis, NEC C&amp;C Research, &lt;zilla [at] ccrl.nj.nec.com&gt; (for Sun4 &amp; SGI), and Roy Featherstone&#8217;s &lt;roy [at] robots.oxford.ac.uk&gt; personal C interface library for Sun[34] &amp; SGI. I also looked at the machine-dependent parts of the GCC and GDB distributions, and put the gcc asm() extensions to good use. Thanks guys! </p>
<p> This work was partly supported by EC-ESPRIT Basic Research Action SECOND. </p>
<h2>Index</h2>
