---
title: "avr-nm(1)"
name: "avr-nm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avr-nm/"
description: "nm – list symbols from object files"
---

<h2 class="name">NAME</h2>
<p> nm &#8211; list symbols from object files </p>
<h2>SYNOPSIS</h2>
<p> nm [<code>-A</code>|<code>-o</code>|<code>&#8211;print-file-name</code>] [<code>-a</code>|<code>&#8211;debug-syms</code>]<br />
[<code>-B</code>|<code>&#8211;format=bsd</code>]&nbsp;<wbr>[<code>-C</code>|<code>&#8211;demangle</code>[=<i>style</i>]]<br />
[<code>-D</code>|<code>&#8211;dynamic</code>]&nbsp;<wbr>[<code>-f</code><i>format</i>|<code>&#8211;format=</code><i>format</i>]<br />
[<code>-g</code>|<code>&#8211;extern-only</code>]&nbsp;<wbr>[<code>-h</code>|<code>&#8211;help</code>]<br />
[<code>-l</code>|<code>&#8211;line-numbers</code>]&nbsp;<wbr>[<code>-n</code>|<code>-v</code>|<code>&#8211;numeric-sort</code>]<br />
[<code>-P</code>|<code>&#8211;portability</code>]&nbsp;<wbr>[<code>-p</code>|<code>&#8211;no-sort</code>]<br />
[<code>-r</code>|<code>&#8211;reverse-sort</code>]&nbsp;<wbr>[<code>-S</code>|<code>&#8211;print-size</code>]<br />
[<code>-s</code>|<code>&#8211;print-armap</code>]&nbsp;<wbr>[<code>-t</code>&nbsp;<wbr><i>radix</i>|<code>&#8211;radix=</code><i>radix</i>]<br />
[<code>-u</code>|<code>&#8211;undefined-only</code>]&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br />
[<code>-X 32_64</code>]&nbsp;<wbr>[<code>&#8211;defined-only</code>]&nbsp;<wbr>[<code>&#8211;no-demangle</code>]<br />
[<code>&#8211;plugin</code>&nbsp;<wbr><i>name</i>]&nbsp;<wbr>[<code>&#8211;size-sort</code>]&nbsp;<wbr>[<code>&#8211;special-syms</code>]<br />
[<code>&#8211;synthetic</code>]&nbsp;<wbr>[<code>&#8211;target=</code><i>bfdname</i>]<br />
[<i>objfile</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">GNU </font><code>nm</code> lists the symbols from object files <i>objfile</i>&#8230;. If no object files are listed as arguments, <code>nm</code> assumes the file <i>a.out</i>. </p>
<p> For each symbol, <code>nm</code> shows:</p>
<dl>
<dt>&bull;</p>
<dd> The symbol value, in the radix selected by options (see below), or hexadecimal by default.</p>
<dt>&bull;</p>
<dd> The symbol type. At least the following types are used; others are, as well, depending on the object file format. If lowercase, the symbol is usually local; if uppercase, the symbol is global (external). There are however a few lowercase symbols that are shown for special global symbols (<tt>&quot;u&quot;</tt>, <tt>&quot;v&quot;</tt> and <tt>&quot;w&quot;</tt>).</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;A&quot;</p>
<dd> The symbol&#8217;s value is absolute, and will not be changed by further linking.</p>
<dt>&quot;B&quot;</p>
<dd>
<dt>&quot;b&quot;</p>
<dd> The symbol is in the uninitialized data section (known as <font SIZE="-1">BSS</font>).</p>
<dt>&quot;C&quot;</p>
<dd> The symbol is common. Common symbols are uninitialized data. When linking, multiple common symbols may appear with the same name. If the symbol is defined anywhere, the common symbols are treated as undefined references.</p>
<dt>&quot;D&quot;</p>
<dd>
<dt>&quot;d&quot;</p>
<dd> The symbol is in the initialized data section.</p>
<dt>&quot;G&quot;</p>
<dd>
<dt>&quot;g&quot;</p>
<dd> The symbol is in an initialized data section for small objects. Some object file formats permit more efficient access to small data objects, such as a global int variable as opposed to a large global array.</p>
<dt>&quot;i&quot;</p>
<dd> For <font SIZE="-1">PE</font> format files this indicates that the symbol is in a section specific to the implementation of DLLs. For <font SIZE="-1">ELF</font> format files this indicates that the symbol is an indirect function. This is a <font SIZE="-1">GNU</font> extension to the standard set of <font SIZE="-1">ELF</font> symbol types. It indicates a symbol which if referenced by a relocation does not evaluate to its address, but instead must be invoked at runtime. The runtime execution will then return the value to be used in the relocation.</p>
<dt>&quot;I&quot;</p>
<dd> The symbol is an indirect reference to another symbol.</p>
<dt>&quot;N&quot;</p>
<dd> The symbol is a debugging symbol.</p>
<dt>&quot;p&quot;</p>
<dd> The symbols is in a stack unwind section.</p>
<dt>&quot;R&quot;</p>
<dd>
<dt>&quot;r&quot;</p>
<dd> The symbol is in a read only data section.</p>
<dt>&quot;S&quot;</p>
<dd>
<dt>&quot;s&quot;</p>
<dd> The symbol is in an uninitialized data section for small objects.</p>
<dt>&quot;T&quot;</p>
<dd>
<dt>&quot;t&quot;</p>
<dd> The symbol is in the text (code) section.</p>
<dt>&quot;U&quot;</p>
<dd> The symbol is undefined.</p>
<dt>&quot;u&quot;</p>
<dd> The symbol is a unique global symbol. This is a <font SIZE="-1">GNU</font> extension to the standard set of <font SIZE="-1">ELF</font> symbol bindings. For such a symbol the dynamic linker will make sure that in the entire process there is just one symbol with this name and type in use.</p>
<dt>&quot;V&quot;</p>
<dd>
<dt>&quot;v&quot;</p>
<dd> The symbol is a weak object. When a weak defined symbol is linked with a normal defined symbol, the normal defined symbol is used with no error. When a weak undefined symbol is linked and the symbol is not defined, the value of the weak symbol becomes zero with no error. On some systems, uppercase indicates that a default value has been specified.</p>
<dt>&quot;W&quot;</p>
<dd>
<dt>&quot;w&quot;</p>
<dd> The symbol is a weak symbol that has not been specifically tagged as a weak object symbol. When a weak defined symbol is linked with a normal defined symbol, the normal defined symbol is used with no error. When a weak undefined symbol is linked and the symbol is not defined, the value of the symbol is determined in a system-specific manner without error. On some systems, uppercase indicates that a default value has been specified.</p>
<dt>&quot;-&quot;</p>
<dd> The symbol is a stabs symbol in an a.out object file. In this case, the next values printed are the stabs other field, the stabs desc field, and the stab type. Stabs symbols are used to hold debugging information.</p>
<dt>&quot;?&quot;</p>
<dd> The symbol type is unknown, or object file format specific.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> The symbol name.</dl>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent.</p>
<dl>
<dt><code>-A</code></p>
<dd>
<dt><code>-o</code></p>
<dd>
<dt><code>&#8211;print-file-name</code></p>
<dd> Precede each symbol by the name of the input file (or archive member) in which it was found, rather than identifying the input file once only, before all of its symbols.</p>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;debug-syms</code></p>
<dd> Display all symbols, even debugger-only symbols; normally these are not listed.</p>
<dt><code>-B</code></p>
<dd> The same as <code>&#8211;format=bsd</code> (for compatibility with the <font SIZE="-1">MIPS </font><code>nm</code>).</p>
<dt><code>-C</code></p>
<dd>
<dt><code>&#8211;demangle[=</code><i>style</i><code>]</code></p>
<dd> Decode (<i>demangle</i>) low-level symbol names into user-level names. Besides removing any initial underscore prepended by the system, this makes C<font SIZE="-2">++</font> function names readable. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler.</p>
<dt><code>&#8211;no-demangle</code></p>
<dd> Do not demangle low-level symbol names. This is the default.</p>
<dt><code>-D</code></p>
<dd>
<dt><code>&#8211;dynamic</code></p>
<dd> Display the dynamic symbols rather than the normal symbols. This is only meaningful for dynamic objects, such as certain types of shared libraries.</p>
<dt><code>-f</code> <i>format</i></p>
<dd>
<dt><code>&#8211;format=</code><i>format</i></p>
<dd> Use the output format <i>format</i>, which can be <tt>&quot;bsd&quot;</tt>, <tt>&quot;sysv&quot;</tt>, or <tt>&quot;posix&quot;</tt>. The default is <tt>&quot;bsd&quot;</tt>. Only the first character of <i>format</i> is significant; it can be either upper or lower case.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;extern-only</code></p>
<dd> Display only external symbols.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of the options to <code>nm</code> and exit.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;line-numbers</code></p>
<dd> For each symbol, use debugging information to try to find a filename and line number. For a defined symbol, look for the line number of the address of the symbol. For an undefined symbol, look for the line number of a relocation entry which refers to the symbol. If line number information can be found, print it after the other symbol information.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;numeric-sort</code></p>
<dd> Sort symbols numerically by their addresses, rather than alphabetically by their names.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;no-sort</code></p>
<dd> Do not bother to sort the symbols in any order; print them in the order encountered.</p>
<dt><code>-P</code></p>
<dd>
<dt><code>&#8211;portability</code></p>
<dd> Use the <font SIZE="-1">POSIX.2</font> standard output format instead of the default format. Equivalent to <code>-f posix</code>.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;reverse-sort</code></p>
<dd> Reverse the order of the sort (whether numeric or alphabetic); let the last come first.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;print-size</code></p>
<dd> Print both value and size of defined symbols for the <tt>&quot;bsd&quot;</tt> output style. This option has no effect for object formats that do not record symbol sizes, unless <code>&#8211;size-sort</code> is also used in which case a calculated size is displayed.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;print-armap</code></p>
<dd> When listing symbols from archive members, include the index: a mapping (stored in the archive by <code>ar</code> or <code>ranlib</code>) of which modules contain definitions for which names.</p>
<dt><code>-t</code> <i>radix</i></p>
<dd>
<dt><code>&#8211;radix=</code><i>radix</i></p>
<dd> Use <i>radix</i> as the radix for printing the symbol values. It must be <code>d</code> for decimal, <code>o</code> for octal, or <code>x</code> for hexadecimal.</p>
<dt><code>-u</code></p>
<dd>
<dt><code>&#8211;undefined-only</code></p>
<dd> Display only undefined symbols (those external to each object file).</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Show the version number of <code>nm</code> and exit.</p>
<dt><code>-X</code></p>
<dd> This option is ignored for compatibility with the <font SIZE="-1">AIX</font> version of <code>nm</code>. It takes one parameter which must be the string <code>32_64</code>. The default mode of <font SIZE="-1">AIX </font><code>nm</code> corresponds to <code>-X 32</code>, which is not supported by <font SIZE="-1">GNU </font><code>nm</code>.</p>
<dt><code>&#8211;defined-only</code></p>
<dd> Display only defined symbols for each object file.</p>
<dt><code>&#8211;plugin</code> <i>name</i></p>
<dd> Load the plugin called <i>name</i> to add support for extra target types. This option is only available if the toolchain has been built with plugin support enabled.</p>
<dt><code>&#8211;size-sort</code></p>
<dd> Sort symbols by size. The size is computed as the difference between the value of the symbol and the value of the symbol with the next higher value. If the <tt>&quot;bsd&quot;</tt> output format is used the size of the symbol is printed, rather than the value, and <code>-S</code> must be used in order both size and value to be printed.</p>
<dt><code>&#8211;special-syms</code></p>
<dd> Display symbols which have a target-specific special meaning. These symbols are usually used by the target for some special processing and are not normally helpful when included in the normal symbol lists. For example for <font SIZE="-1">ARM</font> targets this option would skip the mapping symbols used to mark transitions between <font SIZE="-1">ARM</font> code, <font SIZE="-1">THUMB</font> code and data.</p>
<dt><code>&#8211;synthetic</code></p>
<dd> Include synthetic symbols in the output. These are special symbols created by the linker for various purposes. They are not shown by default since they are not part of the binary&#8217;s original source code.</p>
<dt><code>&#8211;target=</code><i>bfdname</i></p>
<dd> Specify an object code format other than your system&#8217;s default format.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1), <i><a href="/docs/linux/man/1-objdump/">objdump</a></i>(1), <i><a href="/docs/linux/man/1-ranlib/">ranlib</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2013 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
