---
title: "ffcall-vacall(3)"
name: "ffcall-vacall"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ffcall-vacall/"
description: "vacall – C functions called with variable arguments"
---

<h2>NAME</h2>
<p> vacall &#8211; C functions called with variable arguments</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;vacall.h&gt;</code> </p>
<p> <code>extern void* vacall_function;</code> </p>
<pre><code>
void function(alist)
    va_alist alist;
{
    va_start_type(alist[, return_type]);
    arg = va_arg_type(alist[, arg_type]);
    va_return_type(alist[[, return_type ], return_value]);
}
</code></pre>
<p> <code>vacall_function = </code><i>&amp;function</i><code>;</code> </p>
<p> <i>val</i><code> = ((</code><i>return_type</i><code> (*) ()) vacall) (</code><i>arg1</i><code>,</code><i>arg2</i><code>,</code><i>&#8230;</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This set of macros permit a C function <i>function</i> to be called with variable arguments and to return variable return values. This is much like the <code><a href="/docs/linux/man/3-varargs/">varargs</a></code>(3) facility, but also allows the return value to be specified at run time. </p>
<p> Function calling conventions differ considerably on different machines, and <i>vacall</i> attempts to provide some degree of isolation from such architecture dependencies. </p>
<p> The function that can be called with any number and type of arguments and which will return any type of return value is <code>vacall</code>. It will do some magic and call the function stored in the variable <code>vacall_function</code>. If you want to make more than one use of <i>vacall</i>, use the <i><a href="/docs/linux/man/3-trampoline/">trampoline</a></i>(3) facility to store <i>&amp;function</i> into <code>vacall_function</code> just before calling <code>vacall</code>. </p>
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
<p> For a struct with three slots<br />
struct {<br />
    type1 id1;<br />
    type2 id2;<br />
    type3 id3;<br />
}<br />
 you can specify <i>splittable</i> as <code>va_word_splittable_3 (</code><i>type1</i><code>, </code><i>type2</i><code>, </code><i>type3</i><code>)</code> . </p>
<h2>NOTES</h2>
<p> Functions which want to emulate Kernighan &amp; Ritchie style functions (i.e., in ANSI C, functions without a typed argument list) cannot use the <i>type</i> values <code>char</code>, <code>schar</code>, <code>uchar</code>, <code>short</code>, <code>ushort</code>, <code>float</code>. As prescribed by the default K&amp;R C expression promotions, they have to use <code>int</code> instead of <code>char</code>, <code>schar</code>, <code>uchar</code>, <code>short</code>, <code>ushort</code> and <code>double</code> instead of <code>float</code>. </p>
<p> The macros <code>va_start_longlong()</code>, <code>va_start_ulonglong()</code>, <code>va_return_longlong()</code>, <code>va_return_ulonglong()</code>, <code>va_arg_longlong()</code> and <code>va_arg_ulonglong()</code> work only if the C compiler has a working <code>long long</code> 64-bit integer type. </p>
<p> The struct types used in <code>va_start_struct()</code> and <code>va_struct()</code> must only contain (signed or unsigned) int, long, long long or pointer fields. Struct types containing (signed or unsigned) char, short, float, double or other structs are not supported. </p>
<h2>EXAMPLE</h2>
<p> This example, a possible implementation of <code><a href="/docs/linux/man/3-execl/">execl</a></code>(3) on top of <code><a href="/docs/linux/man/2-execv/">execv</a></code>(2) using <code><a href="/docs/linux/man/3-varargs/">varargs</a></code>(3), </p>
<p>#include &lt;varargs.h&gt;<br />
#define MAXARGS 100<br />
/* execl is called by execl(file, arg1, arg2, &#8230;, (char *)0); */<br />
int execl(va_alist)<br />
    va_dcl<br />
{<br />
    va_list ap;<br />
    char *file;<br />
    char *args[MAXARGS];<br />
    int argno = 0;<br />
    va_start(ap);<br />
    file = va_arg(ap, char *);<br />
    while ((args[argno] = va_arg(ap, char *)) != (char *)0)<br />
        argno++;<br />
    va_end(ap);<br />
    return execv(file, args);<br />
}</p>
<p> looks like this using <code><a href="/docs/linux/man/3-vacall/">vacall</a></code>(3): </p>
<pre><code>
#include &lt;vacall.h&gt;
#define MAXARGS 100
/* execl is called by vacall(file, arg1, arg2, ..., (char *)0); */
void execl(ap)
    va_alist ap;
{
    char *file;
    char *args[MAXARGS];
    int argno = 0;
    int retval;
    va_start_int(ap);
    file = va_arg_ptr(ap, char *);
    while ((args[argno] = va_arg_ptr(ap, char *)) != (char *)0)
        argno++;
    retval = execv(file, args);
    va_return_int(ap, retval);
}
vacall_function = &amp;execl;
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-varargs/">varargs</a></code>(3), <code><a href="/docs/linux/man/3-trampoline/">trampoline</a></code>(3), <code><a href="/docs/linux/man/3-callback/">callback</a></code>(3). </p>
<h2>BUGS</h2>
<p> The current implementations have been tested on a selection of common cases but there are probably still many bugs. </p>
<p> There are typically built-in limits on the size of the argument-list, which may also include the size of any structure arguments. </p>
<p> The decision whether a struct is to be returned in registers or in memory considers only the struct&#8217;s size and alignment. This is inaccurate: for example, gcc on m68k-next returns <code>struct { char a,b,c; }</code> in registers and <code>struct { char a[3]; }</code> in memory, although both types have the same size and the same alignment. </p>
<p> <code>&lt;vacall.h&gt;</code> cannot be included when <code>&lt;varargs.h&gt;</code> or <code>&lt;stdarg.h&gt;</code> is included. (Name clash for <code>va_alist</code>.) </p>
<p> The argument list can only be walked once. </p>
<p> The use of the global variable <code>vacall_function</code> is not reentrant. This is fixed in the <code><a href="/docs/linux/man/3-callback/">callback</a></code>(3) package. </p>
<h2>PORTING</h2>
<p> Knowledge about argument passing conventions can be found in the gcc source, file gcc-2.6.3/config/<i>cpu</i>/<i>cpu</i>.h, section &quot;Stack layout; function entry, exit and calling.&quot; </p>
<p> The implementation of varargs for gcc can be found in the gcc source, files gcc-2.6.3/ginclude/va*.h. </p>
<p> gcc&#8217;s __builtin_saveregs() function is defined in the gcc source, file gcc-2.6.3/libgcc2.c. </p>
<h2>AUTHOR</h2>
<p> Bruno Haible &lt;bruno [at] clisp.org&gt; </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Many ideas and a lot of code were cribbed from the gcc source. </p>
<h2>Index</h2>
