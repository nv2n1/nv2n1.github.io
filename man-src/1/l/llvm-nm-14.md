---
title: "llvm-nm-14(1)"
name: "llvm-nm-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-nm-14/"
description: "llvm-nm – list LLVM bitcode and object file’s symbol table"
---

<h2 class="name">NAME</h2>
<p> llvm-nm &#8211; list LLVM bitcode and object file&#8217;s symbol table </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-nm</code> [<i>options</i>] [<i>filenames…</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-nm</code> utility lists the names of symbols from LLVM bitcode files, object files, and archives. Each symbol is listed along with some simple information about its provenance. If no filename is specified, <i>a.out</i> is used as the input. If <i>&#8211;</i> is used as a filename, <code>llvm-nm</code> will read a file from its standard input stream. </p>
<p> <code>llvm-nm</code>’s default output format is the traditional BSD <code>nm</code> output format. Each such output record consists of an (optional) 8-digit hexadecimal address, followed by a type code character, followed by a name, for each symbol. One record is printed per line; fields are separated by spaces. When the address is omitted, it is replaced by 8 spaces. </p>
<p> The supported type code characters are as follows. Where both lower and upper-case characters are listed for the same meaning, a lower-case character represents a local symbol, whilst an upper-case character represents a global (external) symbol: </p>
<p> a, A Absolute symbol. </p>
<p> b, B Uninitialized data (bss) object. </p>
<p> C Common symbol. Multiple definitions link together into one definition. </p>
<p> d, D Writable data object. </p>
<p> i, I COFF: .idata symbol or symbol in a section with IMAGE_SCN_LNK_INFO set. </p>
<p> n ELF: local symbol from non-alloc section. </p>
<p> COFF: debug symbol. </p>
<p> N ELF: debug section symbol, or global symbol from non-alloc section. </p>
<p> s, S COFF: section symbol. </p>
<p> Mach-O: absolute symbol or symbol from a section other than __TEXT_EXEC __text, __TEXT __text, __DATA __data, or __DATA __bss. </p>
<p> r, R Read-only data object. </p>
<p> t, T Code (text) object. </p>
<p> u ELF: GNU unique symbol. </p>
<p> U Named object is undefined in this file. </p>
<p> v ELF: Undefined weak object. It is not a link failure if the object is not defined. </p>
<p> V ELF: Defined weak object symbol. This definition will only be used if no regular definitions exist in a link. If multiple weak definitions and no regular definitions exist, one of the weak definitions will be used. </p>
<p> w Undefined weak symbol other than an ELF object symbol. It is not a link failure if the symbol is not defined. </p>
<p> W Defined weak symbol other than an ELF object symbol. This definition will only be used if no regular definitions exist in a link. If multiple weak definitions and no regular definitions exist, one of the weak definitions will be used. </p>
<p> &#8211; Mach-O: N_STAB symbol. </p>
<p> ? Something unrecognizable. </p>
<p> Because LLVM bitcode files typically contain objects that are not considered to have addresses until they are linked into an executable image or dynamically compiled “just-in-time”, <code>llvm-nm</code> does not print an address for any symbol in an LLVM bitcode file, even symbols which are defined in the bitcode file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-B</code></p>
<dd> Use BSD output format. Alias for <code>&#8211;format=bsd</code>.</p>
<dt><code>&#8211;debug-syms, -a</code></p>
<dd> Show all symbols, even those usually suppressed.</p>
<dt><code>&#8211;defined-only</code></p>
<dd> Print only symbols defined in this file.</p>
<dt><code>&#8211;demangle, -C</code></p>
<dd> Demangle symbol names.</p>
<dt><code>&#8211;dynamic, -D</code></p>
<dd> Display dynamic symbols instead of normal symbols.</p>
<dt><code>&#8211;extern-only, -g</code></p>
<dd> Print only symbols whose definitions are external; that is, accessible from other files.</p>
<dt><code>&#8211;format=&lt;format&gt;, -f</code></p>
<dd> Select an output format; <i>format</i> may be <i>sysv</i>, <i>posix</i>, <i>darwin</i>, <i>bsd</i> or <i>just-symbols</i>. The default is <i>bsd</i>.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Print a summary of command-line options and their meanings.</p>
<dt><code>-j</code></p>
<dd> Print just the symbol names. Alias for <i>–format=just-symbols`</i>.</p>
<dt><code>-m</code></p>
<dd> Use Darwin format. Alias for <code>&#8211;format=darwin</code>.</p>
<dt><code>&#8211;no-demangle</code></p>
<dd> Don’t demangle symbol names. This is the default.</p>
<dt><code>&#8211;no-llvm-bc</code></p>
<dd> Disable the LLVM bitcode reader.</p>
<dt><code>&#8211;no-sort, -p</code></p>
<dd> Show symbols in the order encountered.</p>
<dt><code>&#8211;no-weak</code></p>
<dd> Don’t print weak symbols.</p>
<dt><code>&#8211;numeric-sort, -n, -v</code></p>
<dd> Sort symbols by address.</p>
<dt><code>&#8211;portability, -P</code></p>
<dd> Use POSIX.2 output format. Alias for <code>&#8211;format=posix</code>.</p>
<dt><code>&#8211;print-armap</code></p>
<dd> Print the archive symbol table, in addition to the symbols.</p>
<dt><code>&#8211;print-file-name, -A, -o</code></p>
<dd> Precede each symbol with the file it came from.</p>
<dt><code>&#8211;print-size, -S</code></p>
<dd> Show symbol size as well as address (not applicable for Mach-O).</p>
<dt><code>&#8211;quiet</code></p>
<dd> Suppress ‘no symbols’ diagnostic.</p>
<dt><code>&#8211;radix=&lt;RADIX&gt;, -t</code></p>
<dd> Specify the radix of the symbol address(es). Values accepted are <i>d</i> (decimal), <i>x</i> (hexadecimal) and <i>o</i> (octal).</p>
<dt><code>&#8211;reverse-sort, -r</code></p>
<dd> Sort symbols in reverse order.</p>
<dt><code>&#8211;size-sort</code></p>
<dd> Sort symbols by size.</p>
<dt><code>&#8211;special-syms</code></p>
<dd> Do not filter special symbols from the output.</p>
<dt><code>&#8211;undefined-only, -u</code></p>
<dd> Print only undefined symbols.</p>
<dt><code>&#8211;version, -V</code></p>
<dd> Display the version of the <code>llvm-nm</code> executable, then exit. Does not stack with other commands.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options from response file <i>&lt;FILE&gt;</i>.</dl>
<h2>MACH-O SPECIFIC OPTIONS</h2>
<dl>
<dt><code>&#8211;add-dyldinfo</code></p>
<dd> Add symbols from the dyldinfo, if they are not already in the symbol table. This is the default.</p>
<dt><code>&#8211;add-inlinedinfo</code></p>
<dd> Add symbols from the inlined libraries, TBD file inputs only.</p>
<dt><code>&#8211;arch=&lt;arch1[,arch2,&#8230;]&gt;</code></p>
<dd> Dump the symbols from the specified architecture(s).</p>
<dt><code>&#8211;dyldinfo-only</code></p>
<dd> Dump only symbols from the dyldinfo.</p>
<dt><code>&#8211;no-dyldinfo</code></p>
<dd> Do not add any symbols from the dyldinfo.</p>
<dt><code>-s &lt;segment&gt; &lt;section&gt;</code></p>
<dd> Dump only symbols from this segment and section name.</p>
<dt><code>-x</code></p>
<dd> Print symbol entry in hex.</dl>
<h2>BUGS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>llvm-nm</code> does not support the full set of arguments that GNU <code>nm</code> does.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-nm</code> exits with an exit code of zero.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-ar/">llvm-ar</a>(1)</code>, <code><a href="/docs/linux/man/1-llvm-objdump/">llvm-objdump</a>(1)</code>, <code><a href="/docs/linux/man/1-llvm-readelf/">llvm-readelf</a>(1)</code>, <code><a href="/docs/linux/man/1-llvm-readobj/">llvm-readobj</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
