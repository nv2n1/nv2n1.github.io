---
title: "nm(1)"
name: "nm"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nm/"
description: "nm – list symbols from object files"
---

<h2 class="name">NAME</h2>
<p> nm &#8211; list symbols from object files </p>
<h2>SYNOPSIS</h2>
<p> nm [<code>-A</code>|<code>-o</code>|<code>&#8211;print-file-name</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-a</code>|<code>&#8211;debug-syms</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-B</code>|<code>&#8211;format=bsd</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-C</code>|<code>&#8211;demangle</code>[=<i>style</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-D</code>|<code>&#8211;dynamic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-f</code><i>format</i>|<code>&#8211;format=</code><i>format</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-g</code>|<code>&#8211;extern-only</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-h</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;ifunc-chars=</code><i></i><font SIZE="-1"><i>CHARS</i></font><i></i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-j</code>|<code>&#8211;format=just-symbols</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-l</code>|<code>&#8211;line-numbers</code>]&nbsp;[<code>&#8211;inlines</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-n</code>|<code>-v</code>|<code>&#8211;numeric-sort</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-P</code>|<code>&#8211;portability</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-p</code>|<code>&#8211;no-sort</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-r</code>|<code>&#8211;reverse-sort</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-S</code>|<code>&#8211;print-size</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-s</code>|<code>&#8211;print-armap</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-t</code>&nbsp;<i>radix</i>|<code>&#8211;radix=</code><i>radix</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-u</code>|<code>&#8211;undefined-only</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-U</code>&nbsp;<i>method</i>]&nbsp;[<code>&#8211;unicode=</code><i>method</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-V</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-X 32_64</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;defined-only</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;no-demangle</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;no-recurse-limit</code>|<code>&#8211;recurse-limit</code>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;plugin</code>&nbsp;<i>name</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;size-sort</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;special-syms</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;synthetic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;with-symbol-versions</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;without-symbol-versions</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<i>objfile</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">GNU</font> <code>nm</code> lists the symbols from object files <i>objfile</i>&#8230;. If no object files are listed as arguments, <code>nm</code> assumes the file <i>a.out</i>. </p>
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
<dd> The symbol is in the <font SIZE="-1">BSS</font> data section. This section typically contains zero-initialized or uninitialized data, although the exact behavior is system dependent.</p>
<dt>&quot;C&quot;</p>
<dd>
<dt>&quot;c&quot;</p>
<dd> The symbol is common. Common symbols are uninitialized data. When linking, multiple common symbols may appear with the same name. If the symbol is defined anywhere, the common symbols are treated as undefined references. The lower case <i>c</i> character is used when the symbol is in a special section for small commons.</p>
<dt>&quot;D&quot;</p>
<dd>
<dt>&quot;d&quot;</p>
<dd> The symbol is in the initialized data section.</p>
<dt>&quot;G&quot;</p>
<dd>
<dt>&quot;g&quot;</p>
<dd> The symbol is in an initialized data section for small objects. Some object file formats permit more efficient access to small data objects, such as a global int variable as opposed to a large global array.</p>
<dt>&quot;i&quot;</p>
<dd> For <font SIZE="-1">PE</font> format files this indicates that the symbol is in a section specific to the implementation of DLLs. </p>
<p> For <font SIZE="-1">ELF</font> format files this indicates that the symbol is an indirect function. This is a <font SIZE="-1">GNU</font> extension to the standard set of <font SIZE="-1">ELF</font> symbol types. It indicates a symbol which if referenced by a relocation does not evaluate to its address, but instead must be invoked at runtime. The runtime execution will then return the value to be used in the relocation. </p>
<p> Note &#8211; the actual symbols display for <font SIZE="-1">GNU</font> indirect symbols is controlled by the <code>&#8211;ifunc-chars</code> command line option. If this option has been provided then the first character in the string will be used for global indirect function symbols. If the string contains a second character then that will be used for local indirect function symbols.</p>
<dt>&quot;I&quot;</p>
<dd> The symbol is an indirect reference to another symbol.</p>
<dt>&quot;N&quot;</p>
<dd> The symbol is a debugging symbol.</p>
<dt>&quot;n&quot;</p>
<dd> The symbol is in the read-only data section.</p>
<dt>&quot;p&quot;</p>
<dd> The symbol is in a stack unwind section.</p>
<dt>&quot;R&quot;</p>
<dd>
<dt>&quot;r&quot;</p>
<dd> The symbol is in a read only data section.</p>
<dt>&quot;S&quot;</p>
<dd>
<dt>&quot;s&quot;</p>
<dd> The symbol is in an uninitialized or zero-initialized data section for small objects.</p>
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
<dd> The symbol name. If a symbol has version information associated with it, then the version information is displayed as well. If the versioned symbol is undefined or hidden from linker, the version string is displayed as a suffix to the symbol name, preceded by an @ character. For example <code>foo [at] VER_1</code>. If the version is the default version to be used when resolving unversioned references to the symbol, then it is displayed as a suffix preceded by two @ characters. For example <code>foo@@VER_2</code>.</dl>
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
<dd> The same as <code>&#8211;format=bsd</code> (for compatibility with the <font SIZE="-1">MIPS</font> <code>nm</code>).</p>
<dt><code>-C</code></p>
<dd>
<dt><code>&#8211;demangle[=</code><i>style</i><code>]</code></p>
<dd> Decode (<i>demangle</i>) low-level symbol names into user-level names. Besides removing any initial underscore prepended by the system, this makes C<font SIZE="-2">++</font> function names readable. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler.</p>
<dt><code>&#8211;no-demangle</code></p>
<dd> Do not demangle low-level symbol names. This is the default.</p>
<dt><code>&#8211;recurse-limit</code></p>
<dd>
<dt><code>&#8211;no-recurse-limit</code></p>
<dd>
<dt><code>&#8211;recursion-limit</code></p>
<dd>
<dt><code>&#8211;no-recursion-limit</code></p>
<dd> Enables or disables a limit on the amount of recursion performed whilst demangling strings. Since the name mangling formats allow for an infinite level of recursion it is possible to create strings whose decoding will exhaust the amount of stack space available on the host machine, triggering a memory fault. The limit tries to prevent this from happening by restricting recursion to 2048 levels of nesting. </p>
<p> The default is for this limit to be enabled, but disabling it may be necessary in order to demangle truly complicated names. Note however that if the recursion limit is disabled then stack exhaustion is possible and any bug reports about such an event will be rejected.</p>
<dt><code>-D</code></p>
<dd>
<dt><code>&#8211;dynamic</code></p>
<dd> Display the dynamic symbols rather than the normal symbols. This is only meaningful for dynamic objects, such as certain types of shared libraries.</p>
<dt><code>-f</code> <i>format</i></p>
<dd>
<dt><code>&#8211;format=</code><i>format</i></p>
<dd> Use the output format <i>format</i>, which can be <tt>&quot;bsd&quot;</tt>, <tt>&quot;sysv&quot;</tt>, <tt>&quot;posix&quot;</tt> or <tt>&quot;just-symbols&quot;</tt>. The default is <tt>&quot;bsd&quot;</tt>. Only the first character of <i>format</i> is significant; it can be either upper or lower case.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;extern-only</code></p>
<dd> Display only external symbols.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of the options to <code>nm</code> and exit.</p>
<dt><code>&#8211;ifunc-chars=</code><i></i><font SIZE="-1"><i>CHARS</i></font><i></i></p>
<dd> When display <font SIZE="-1">GNU</font> indirect function symbols <code>nm</code> will default to using the <tt>&quot;i&quot;</tt> character for both local indirect functions and global indirect functions. The <code>&#8211;ifunc-chars</code> option allows the user to specify a string containing one or two characters. The first character will be used for global indirect function symbols and the second character, if present, will be used for local indirect function symbols.</p>
<dt><code>j</code></p>
<dd> The same as <code>&#8211;format=just-symbols</code>.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;line-numbers</code></p>
<dd> For each symbol, use debugging information to try to find a filename and line number. For a defined symbol, look for the line number of the address of the symbol. For an undefined symbol, look for the line number of a relocation entry which refers to the symbol. If line number information can be found, print it after the other symbol information.</p>
<dt><code>&#8211;inlines</code></p>
<dd> When option <code>-l</code> is active, if the address belongs to a function that was inlined, then this option causes the source information for all enclosing scopes back to the first non-inlined function to be printed as well. For example, if <tt>&quot;main&quot;</tt> inlines <tt>&quot;callee1&quot;</tt> which inlines <tt>&quot;callee2&quot;</tt>, and address is from <tt>&quot;callee2&quot;</tt>, the source information for <tt>&quot;callee1&quot;</tt> and <tt>&quot;main&quot;</tt> will also be printed.</p>
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
<dt><code>-U</code> <i>[d|i|l|e|x|h]</i></p>
<dd>
<dt><code>&#8211;unicode=</code><i>[default|invalid|locale|escape|hex|highlight]</i></p>
<dd> Controls the display of <font SIZE="-1">UTF-8</font> encoded multibyte characters in strings. The default (<code>&#8211;unicode=default</code>) is to give them no special treatment. The <code>&#8211;unicode=locale</code> option displays the sequence in the current locale, which may or may not support them. The options <code>&#8211;unicode=hex</code> and <code>&#8211;unicode=invalid</code> display them as hex byte sequences enclosed by either angle brackets or curly braces. </p>
<p> The <code>&#8211;unicode=escape</code> option displays them as escape sequences (<i>
