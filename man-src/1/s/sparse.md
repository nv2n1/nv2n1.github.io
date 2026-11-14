---
title: "sparse(1)"
name: "sparse"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sparse/"
description: "sparse – Semantic Parser for C"
---

<h2>NAME</h2>
<p> sparse &#8211; Semantic Parser for C</p>
<h2>SYNOPSIS</h2>
<p> <code>sparse</code> [<i>WARNING OPTIONS</i>]&#8230; <i>file.c</i></p>
<h2>DESCRIPTION</h2>
<p> Sparse parses C source and looks for errors, producing warnings on standard error. </p>
<p> Sparse accepts options controlling the set of warnings to generate. To turn on warnings Sparse does not issue by default, use the corresponding warning option <code>-Wsomething</code>. Sparse issues some warnings by default; to turn off those warnings, pass the negation of the associated warning option, <code>-Wno-something</code>.</p>
<h2>WARNING OPTIONS</h2>
<dl>
<dt><code>-Wsparse-all</code></p>
<dd> Turn on all sparse warnings, except for those explicitly disabled via <code>-Wno-something</code>.</p>
<dt><code>-Waddress-space</code></p>
<dd> Warn about code which mixes pointers to different address spaces. </p>
<p> Sparse allows an extended attribute <code>__attribute__((address_space(</code><i>num</i><code>)))</code> on pointers, which designates a pointer target in address space <i>num</i> (a constant integer). With <code>-Waddress-space</code>, Sparse treats pointers with identical target types but different address spaces as distinct types. To override this warning, such as for functions which convert pointers between address spaces, use a type that includes <code>__attribute__((force))</code>. </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-address-space</code>.</p>
<dt><code>-Wbitwise</code></p>
<dd> Warn about unsupported operations or type mismatches with restricted integer types. </p>
<p> Sparse supports an extended attribute, <code>__attribute__((bitwise))</code>, which creates a new restricted integer type from a base integer type, distinct from the base integer type and from any other restricted integer type not declared in the same declaration or <code>typedef</code>. For example, this allows programs to create <code>typedef</code>s for integer types with specific endianness. With <code>-Wbitwise</code>, Sparse will warn on any use of a restricted type in arithmetic operations other than bitwise operations, and on any conversion of one restricted type into another, except via a cast that includes <code>__attribute__((force))</code>. </p>
<p> __bitwise ends up being a &quot;stronger integer separation&quot;. That one doesn&#8217;t allow you to mix with non-bitwise integers, so now it&#8217;s much harder to lose the type by mistake. </p>
<p> __bitwise is for *unique types* that cannot be mixed with other types, and that you&#8217;d never want to just use as a random integer (the integer 0 is special, though, and gets silently accepted iirc &#8211; it&#8217;s kind of like &quot;NULL&quot; for pointers). So &quot;gfp_t&quot; or the &quot;safe endianness&quot; types would be __bitwise: you can only operate on them by doing specific operations that know about *that* particular type. </p>
<p> Generally, you want bitwise if you are looking for type safety. Sparse does not issue these warnings by default.</p>
<dt><code>-Wcast-to-as</code></p>
<dd> Warn about casts which add an address space to a pointer type. </p>
<p> A cast that includes <code>__attribute__((force))</code> will suppress this warning. </p>
<p> Sparse does not issue these warnings by default.</p>
<dt><code>-Wcast-truncate</code></p>
<dd> Warn about casts that truncate constant values. </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-cast-truncate</code>.</p>
<dt><code>-Wcontext</code></p>
<dd> Warn about potential errors in synchronization or other delimited contexts. </p>
<p> Sparse supports several means of designating functions or statements that delimit contexts, such as synchronization. Functions with the extended attribute <code>__attribute__((context(</code><i>expression</i><code>,</code><i>in_context</i><code>,</code><i>out_context</i><code>))</code> require the context <i>expression</i> (for instance, a lock) to have the value <i>in_context</i> (a constant nonnegative integer) when called, and return with the value <i>out_context</i> (a constant nonnegative integer). For APIs defined via macros, use the statement form <code>__context__(</code><i>expression</i><code>,</code><i>in_value</i><code>,</code><i>out_value</i><code>)</code> in the body of the macro. </p>
<p> With <code>-Wcontext</code> Sparse will warn when it sees a function change the context without indicating this with a <code>context</code> attribute, either by decreasing a context below zero (such as by releasing a lock without acquiring it), or returning with a changed context (such as by acquiring a lock without releasing it). Sparse will also warn about blocks of code which may potentially execute with different contexts. </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-context</code>.</p>
<dt><code>-Wdecl</code></p>
<dd> Warn about any non-<code>static</code> variable or function definition that has no previous declaration. </p>
<p> Private symbols (functions and variables) internal to a given source file should use <code>static</code>, to allow additional compiler optimizations, allow detection of unused symbols, and prevent other code from relying on these internal symbols. Public symbols used by other source files will need declarations visible to those other source files, such as in a header file. All declarations should fall into one of these two categories. Thus, with <code>-Wdecl</code>, Sparse warns about any symbol definition with neither <code>static</code> nor a declaration. To fix this warning, declare private symbols <code>static</code>, and ensure that the files defining public symbols have the symbol declarations available first (such as by including the appropriate header file). </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-decl</code>.</p>
<dt><code>-Wdeclaration-after-statement</code></p>
<dd> Warn about declarations that are not at the start of a block. </p>
<p> These declarations are permitted in C99 but not in C89. </p>
<p> Sparse issues these warnings by default only when the C dialect is C89 (i.e. -ansi or -std=c89). To turn them off, use <code>-Wno-declaration-after-statement</code>.</p>
<dt><code>-Wdefault-bitfield-sign</code></p>
<dd> Warn about any bitfield with no explicit signedness. </p>
<p> Bitfields have no standard-specified default signedness. (C99 6.7.2) A bitfield without an explicit <code>signed</code> or <code>unsigned</code> creates a portability problem for software that relies on the available range of values. To fix this, specify the bitfield type as <code>signed</code> or <code>unsigned</code> explicitly. </p>
<p> Sparse does not issue these warnings by default.</p>
<dt><code>-Wdesignated-init</code></p>
<dd> Warn about positional initialization of structs marked as requiring designated initializers. </p>
<p> Sparse allows an attribute <code>__attribute__((designated_init))</code> which marks a struct as requiring designated initializers. Sparse will warn about positional initialization of a struct variable or struct literal of a type that has this attribute. </p>
<p> Requiring designated initializers for a particular struct type will insulate code using that struct type from changes to the layout of the type, avoiding the need to change initializers for that type unless they initialize a removed or incompatibly changed field. </p>
<p> Common examples of this type of struct include collections of function pointers for the implementations of a class of related operations, for which the default NULL for an unmentioned field in a designated initializer will correctly indicate the absence of that operation. </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-designated-init</code>.</p>
<dt><code>-Wdo-while</code></p>
<dd> Warn about do-while loops that do not delimit the loop body with braces. </p>
<p> Sparse does not issue these warnings by default.</p>
<dt><code>-Wenum-mismatch</code></p>
<dd> Warn about the use of an expression of an incorrect <code>enum</code> type when initializing another <code>enum</code> type, assigning to another <code>enum</code> type, or passing an argument to a function which expects another <code>enum</code> type. </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-enum-mismatch</code>.</p>
<dt><code>-Winit-cstring</code></p>
<dd> Warn about initialization of a char array with a too long constant C string. </p>
<p> If the size of the char array and the length of the string is the same, there is no space for the last nul char of the string in the array: </p>
<pre><code>
char s[3] = "abc";
</code></pre>
<p> If the array is used as a byte array, not as C string, this warning is just noise. However, if the array is passed to functions dealing with C string like printf(%s) and strcmp, it may cause a trouble. </p>
<p> Sparse does not issue these warnings by default.</p>
<dt><code>-Wnon-pointer-null</code></p>
<dd> Warn about the use of 0 as a NULL pointer. </p>
<p> 0 has integer type. NULL has pointer type. </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-non-pointer-null</code>.</p>
<dt><code>-Wold-initializer</code></p>
<dd> Warn about the use of the pre-C99 GCC syntax for designated initializers. </p>
<p> C99 provides a standard syntax for designated fields in <code>struct</code> or <code>union</code> initializers: </p>
<p>struct structname var = {.field = value};</p>
<p> GCC also has an old, non-standard syntax for designated initializers which predates C99: </p>
<pre><code>
struct structname var = {field : value};
</code></pre>
<p> Sparse will warn about the use of GCC&#8217;s non-standard syntax for designated initializers. To fix this warning, convert designated initializers to use the standard C99 syntax. </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-old-initializer</code>.</p>
<dt><code>-Wone-bit-signed-bitfield</code></p>
<dd> Warn about any one-bit <code>signed</code> bitfields. </p>
<p> A one-bit <code>signed</code> bitfield can only have the values 0 and -1, or with some compilers only 0; this results in unexpected behavior for programs which expected the ability to store 0 and 1. </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-one-bit-signed-bitfield</code>.</p>
<dt><code>-Wparen-string</code></p>
<dd> Warn about the use of a parenthesized string to initialize an array. </p>
<p> Standard C syntax does not permit a parenthesized string as an array initializer. GCC allows this syntax as an extension. With <code>-Wparen-string</code>, Sparse will warn about this syntax. </p>
<p> Sparse does not issue these warnings by default.</p>
<dt><code>-Wptr-subtraction-blows</code></p>
<dd> Warn when subtracting two pointers to a type with a non-power-of-two size. </p>
<p> Subtracting two pointers to a given type gives a difference in terms of the number of items of that type. To generate this value, compilers will usually need to divide the difference by the size of the type, an potentially expensive operation for sizes other than powers of two. </p>
<p> Code written using pointer subtraction can often use another approach instead, such as array indexing with an explicit array index variable, which may allow compilers to generate more efficient code. </p>
<p> Sparse does not issue these warnings by default.</p>
<dt><code>-Wreturn-void</code></p>
<dd> Warn if a function with return type void returns a void expression. </p>
<p> C99 permits this, and in some cases this allows for more generic code in macros that use typeof or take a type as a macro argument. However, some programs consider this poor style, and those programs can use <code>-Wreturn-void</code> to get warnings about it. </p>
<p> Sparse does not issue these warnings by default.</p>
<dt><code>-Wshadow</code></p>
<dd> Warn when declaring a symbol which shadows a declaration with the same name in an outer scope. </p>
<p> Such declarations can lead to error-prone code. </p>
<p> Sparse does not issue these warnings by default.</p>
<dt><code>-Wtransparent-union</code></p>
<dd> Warn about any declaration using the GCC extension <code>__attribute__((transparent_union))</code>. </p>
<p> Sparse issues these warnings by default. To turn them off, use <code>-Wno-transparent-union</code>.</p>
<dt><code>-Wtypesign</code></p>
<dd> Warn when converting a pointer to an integer type into a pointer to an integer type with different signedness. </p>
<p> Sparse does not issue these warnings by default.</p>
<dt><code>-Wundef</code></p>
<dd> Warn about preprocessor conditionals that use the value of an undefined preprocessor symbol. </p>
<p> Standard C (C99 6.10.1) permits using the value of an undefined preprocessor symbol in preprocessor conditionals, and specifies it has have a value of 0. However, this behavior can lead to subtle errors. </p>
<p> Sparse does not issue these warnings by default.</dl>
<h2>MISC OPTIONS</h2>
<dl>
<dt><code>-gcc-base-dir </code><i>dir</i></p>
<dd> Look for compiler-provided system headers in <i>dir</i>/include/ and <i>dir</i>/include-fixed/.</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-ftabstop=WIDTH</code></p>
<dd> Set the distance between tab stops. This helps sparse report correct column numbers in warnings or errors. If the value is less than 1 or greater than 100, the option is ignored. The default is 8.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cgcc/">cgcc</a></code>(1)</p>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="http://www.kernel.org/pub/software/devel/sparse/">http://www.kernel.org/pub/software/devel/sparse/</a></p>
<h2>MAILING LIST</h2>
<p> linux-sparse [at] vger.kernel.org</p>
<h2>MAINTAINER</h2>
<p> Josh Triplett &lt;josh [at] kernel.org&gt; </p>
<h2>Index</h2>
