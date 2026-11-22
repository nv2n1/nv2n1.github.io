---

title: "x86_64-linux-gnu-nm(1)"
name: "x86_64-linux-gnu-nm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-linux-gnu-nm/"
---

<p> nm &#8211; list symbols from object files </p>
<h2>SYNOPSIS</h2>
<p> nm [<code>-A</code>|<code>-o</code>|<code>--print-file-name</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-a</code>|<code>--debug-syms</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-B</code>|<code>--format=bsd</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-C</code>|<code>--demangle</code>[=<i>style</i>]] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-D</code>|<code>--dynamic</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-f</code><i>format</i>|<code>--format=</code><i>format</i>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-g</code>|<code>--extern-only</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-h</code>|<code>--help</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--ifunc-chars=</code><i></i><i>CHARS</i><i></i>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-j</code>|<code>--format=just-symbols</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-l</code>|<code>--line-numbers</code>]&nbsp;[<code>--inlines</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-n</code>|<code>-v</code>|<code>--numeric-sort</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-P</code>|<code>--portability</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-p</code>|<code>--no-sort</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-r</code>|<code>--reverse-sort</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-S</code>|<code>--print-size</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-s</code>|<code>--print-armap</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-t</code>&nbsp;<i>radix</i>|<code>--radix=</code><i>radix</i>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-u</code>|<code>--undefined-only</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-U</code>&nbsp;<i>method</i>]&nbsp;[<code>--unicode=</code><i>method</i>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-V</code>|<code>--version</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-X 32_64</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--defined-only</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--no-demangle</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--no-recurse-limit</code>|<code>--recurse-limit</code>]] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--plugin</code>&nbsp;<i>name</i>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--size-sort</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--special-syms</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--synthetic</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--target=</code><i>bfdname</i>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--with-symbol-versions</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>--without-symbol-versions</code>] <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<i>objfile</i>...]  </p>
<h2>DESCRIPTION</h2>
<p> GNU <code>nm</code> lists the symbols from object files <i>objfile</i>.... If no object files are listed as arguments, <code>nm</code> assumes the file <i>a.out</i>. </p>
<p> For each symbol, <code>nm</code> shows: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The symbol value, in the radix selected by options (see below), or hexadecimal by default. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The symbol type. At least the following types are used; others are, as well, depending on the object file format. If lowercase, the symbol is usually local; if uppercase, the symbol is global (external). There are however a few lowercase symbols that are shown for special global symbols (<code>&quot;u&quot;</code>, <code>&quot;v&quot;</code> and <code>&quot;w&quot;</code>). </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&quot;A&quot;</dt>
<dd> <p> The symbol&#8217;s value is absolute, and will not be changed by further linking. </p>
 </dd>
<dt>&quot;B&quot;</dt>
<dd>  </dd>
<dt>&quot;b&quot;</dt>
<dd> <p> The symbol is in the BSS data section. This section typically contains zero-initialized or uninitialized data, although the exact behavior is system dependent. </p>
 </dd>
<dt>&quot;C&quot;</dt>
<dd>  </dd>
<dt>&quot;c&quot;</dt>
<dd> <p> The symbol is common. Common symbols are uninitialized data. When linking, multiple common symbols may appear with the same name. If the symbol is defined anywhere, the common symbols are treated as undefined references. The lower case <i>c</i> character is used when the symbol is in a special section for small commons. </p>
 </dd>
<dt>&quot;D&quot;</dt>
<dd>  </dd>
<dt>&quot;d&quot;</dt>
<dd> <p> The symbol is in the initialized data section. </p>
 </dd>
<dt>&quot;G&quot;</dt>
<dd>  </dd>
<dt>&quot;g&quot;</dt>
<dd> <p> The symbol is in an initialized data section for small objects. Some object file formats permit more efficient access to small data objects, such as a global int variable as opposed to a large global array. </p>
 </dd>
<dt>&quot;i&quot;</dt>
<dd> <p> For PE format files this indicates that the symbol is in a section specific to the implementation of DLLs. </p>
<p> For ELF format files this indicates that the symbol is an indirect function. This is a GNU extension to the standard set of ELF symbol types. It indicates a symbol which if referenced by a relocation does not evaluate to its address, but instead must be invoked at runtime. The runtime execution will then return the value to be used in the relocation. </p>
<p> Note &#8211; the actual symbols display for GNU indirect symbols is controlled by the <code>--ifunc-chars</code> command line option. If this option has been provided then the first character in the string will be used for global indirect function symbols. If the string contains a second character then that will be used for local indirect function symbols. </p>
 </dd>
<dt>&quot;I&quot;</dt>
<dd> <p> The symbol is an indirect reference to another symbol. </p>
 </dd>
<dt>&quot;N&quot;</dt>
<dd> <p> The symbol is a debugging symbol. </p>
 </dd>
<dt>&quot;n&quot;</dt>
<dd> <p> The symbol is in the read-only data section. </p>
 </dd>
<dt>&quot;p&quot;</dt>
<dd> <p> The symbol is in a stack unwind section. </p>
 </dd>
<dt>&quot;R&quot;</dt>
<dd>  </dd>
<dt>&quot;r&quot;</dt>
<dd> <p> The symbol is in a read only data section. </p>
 </dd>
<dt>&quot;S&quot;</dt>
<dd>  </dd>
<dt>&quot;s&quot;</dt>
<dd> <p> The symbol is in an uninitialized or zero-initialized data section for small objects. </p>
 </dd>
<dt>&quot;T&quot;</dt>
<dd>  </dd>
<dt>&quot;t&quot;</dt>
<dd> <p> The symbol is in the text (code) section. </p>
 </dd>
<dt>&quot;U&quot;</dt>
<dd> <p> The symbol is undefined. </p>
 </dd>
<dt>&quot;u&quot;</dt>
<dd> <p> The symbol is a unique global symbol. This is a GNU extension to the standard set of ELF symbol bindings. For such a symbol the dynamic linker will make sure that in the entire process there is just one symbol with this name and type in use. </p>
 </dd>
<dt>&quot;V&quot;</dt>
<dd>  </dd>
<dt>&quot;v&quot;</dt>
<dd> <p> The symbol is a weak object. When a weak defined symbol is linked with a normal defined symbol, the normal defined symbol is used with no error. When a weak undefined symbol is linked and the symbol is not defined, the value of the weak symbol becomes zero with no error. On some systems, uppercase indicates that a default value has been specified. </p>
 </dd>
<dt>&quot;W&quot;</dt>
<dd>  </dd>
<dt>&quot;w&quot;</dt>
<dd> <p> The symbol is a weak symbol that has not been specifically tagged as a weak object symbol. When a weak defined symbol is linked with a normal defined symbol, the normal defined symbol is used with no error. When a weak undefined symbol is linked and the symbol is not defined, the value of the symbol is determined in a system-specific manner without error. On some systems, uppercase indicates that a default value has been specified. </p>
 </dd>
<dt>&quot;-&quot;</dt>
<dd> <p> The symbol is a stabs symbol in an a.out object file. In this case, the next values printed are the stabs other field, the stabs desc field, and the stab type. Stabs symbols are used to hold debugging information. </p>
 </dd>
<dt>&quot;?&quot;</dt>
<dd> <p> The symbol type is unknown, or object file format specific. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> The symbol name. If a symbol has version information associated with it, then the version information is displayed as well. If the versioned symbol is undefined or hidden from linker, the version string is displayed as a suffix to the symbol name, preceded by an @ character. For example <code>foo [at] VER_1</code>. If the version is the default version to be used when resolving unversioned references to the symbol, then it is displayed as a suffix preceded by two @ characters. For example <code>foo@@VER_2</code>. </p>
 </dd></dl>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent. </p>
<dl>
<dt><code>-A</code></dt>
<dd>  </dd>
<dt><code>-o</code></dt>
<dd>  </dd>
<dt><code>--print-file-name</code></dt>
<dd> <p> Precede each symbol by the name of the input file (or archive member) in which it was found, rather than identifying the input file once only, before all of its symbols. </p>
 </dd>
<dt><code>-a</code></dt>
<dd>  </dd>
<dt><code>--debug-syms</code></dt>
<dd> <p> Display all symbols, even debugger-only symbols; normally these are not listed. </p>
 </dd>
<dt><code>-B</code></dt>
<dd> <p> The same as <code>--format=bsd</code> (for compatibility with the MIPS <code>nm</code>). </p>
 </dd>
<dt><code>-C</code></dt>
<dd>  </dd>
<dt><code>--demangle[=</code><i>style</i><code>]</code></dt>
<dd> <p> Decode (<i>demangle</i>) low-level symbol names into user-level names. Besides removing any initial underscore prepended by the system, this makes C++ function names readable. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler. </p>
 </dd>
<dt><code>--no-demangle</code></dt>
<dd> <p> Do not demangle low-level symbol names. This is the default. </p>
 </dd>
<dt><code>--recurse-limit</code></dt>
<dd>  </dd>
<dt><code>--no-recurse-limit</code></dt>
<dd>  </dd>
<dt><code>--recursion-limit</code></dt>
<dd>  </dd>
<dt><code>--no-recursion-limit</code></dt>
<dd> <p> Enables or disables a limit on the amount of recursion performed whilst demangling strings. Since the name mangling formats allow for an infinite level of recursion it is possible to create strings whose decoding will exhaust the amount of stack space available on the host machine, triggering a memory fault. The limit tries to prevent this from happening by restricting recursion to 2048 levels of nesting. </p>
<p> The default is for this limit to be enabled, but disabling it may be necessary in order to demangle truly complicated names. Note however that if the recursion limit is disabled then stack exhaustion is possible and any bug reports about such an event will be rejected. </p>
 </dd>
<dt><code>-D</code></dt>
<dd>  </dd>
<dt><code>--dynamic</code></dt>
<dd> <p> Display the dynamic symbols rather than the normal symbols. This is only meaningful for dynamic objects, such as certain types of shared libraries. </p>
 </dd>
<dt><code>-f</code><i>format</i></dt>
<dd>  </dd>
<dt><code>--format=</code><i>format</i></dt>
<dd> <p> Use the output format <i>format</i>, which can be <code>&quot;bsd&quot;</code>, <code>&quot;sysv&quot;</code>, <code>&quot;posix&quot;</code> or <code>&quot;just-symbols&quot;</code>. The default is <code>&quot;bsd&quot;</code>. Only the first character of <i>format</i> is significant; it can be either upper or lower case. </p>
 </dd>
<dt><code>-g</code></dt>
<dd>  </dd>
<dt><code>--extern-only</code></dt>
<dd> <p> Display only external symbols. </p>
 </dd>
<dt><code>-h</code></dt>
<dd>  </dd>
<dt><code>--help</code></dt>
<dd> <p> Show a summary of the options to <code>nm</code> and exit. </p>
 </dd>
<dt><code>--ifunc-chars=</code><i></i><i>CHARS</i><i></i></dt>
<dd> <p> When display GNU indirect function symbols <code>nm</code> will default to using the <code>&quot;i&quot;</code> character for both local indirect functions and global indirect functions. The <code>--ifunc-chars</code> option allows the user to specify a string containing one or two characters. The first character will be used for global indirect function symbols and the second character, if present, will be used for local indirect function symbols. </p>
 </dd>
<dt><code>j</code></dt>
<dd> <p> The same as <code>--format=just-symbols</code>. </p>
 </dd>
<dt><code>-l</code></dt>
<dd>  </dd>
<dt><code>--line-numbers</code></dt>
<dd> <p> For each symbol, use debugging information to try to find a filename and line number. For a defined symbol, look for the line number of the address of the symbol. For an undefined symbol, look for the line number of a relocation entry which refers to the symbol. If line number information can be found, print it after the other symbol information. </p>
 </dd>
<dt><code>--inlines</code></dt>
<dd> <p> When option <code>-l</code> is active, if the address belongs to a function that was inlined, then this option causes the source information for all enclosing scopes back to the first non-inlined function to be printed as well. For example, if <code>&quot;main&quot;</code> inlines <code>&quot;callee1&quot;</code> which inlines <code>&quot;callee2&quot;</code>, and address is from <code>&quot;callee2&quot;</code>, the source information for <code>&quot;callee1&quot;</code> and <code>&quot;main&quot;</code> will also be printed. </p>
 </dd>
<dt><code>-n</code></dt>
<dd>  </dd>
<dt><code>-v</code></dt>
<dd>  </dd>
<dt><code>--numeric-sort</code></dt>
<dd> <p> Sort symbols numerically by their addresses, rather than alphabetically by their names. </p>
 </dd>
<dt><code>-p</code></dt>
<dd>  </dd>
<dt><code>--no-sort</code></dt>
<dd> <p> Do not bother to sort the symbols in any order; print them in the order encountered. </p>
 </dd>
<dt><code>-P</code></dt>
<dd>  </dd>
<dt><code>--portability</code></dt>
<dd> <p> Use the POSIX.2 standard output format instead of the default format. Equivalent to <code>-f posix</code>. </p>
 </dd>
<dt><code>-r</code></dt>
<dd>  </dd>
<dt><code>--reverse-sort</code></dt>
<dd> <p> Reverse the order of the sort (whether numeric or alphabetic); let the last come first. </p>
 </dd>
<dt><code>-S</code></dt>
<dd>  </dd>
<dt><code>--print-size</code></dt>
<dd> <p> Print both value and size of defined symbols for the <code>&quot;bsd&quot;</code> output style. This option has no effect for object formats that do not record symbol sizes, unless <code>--size-sort</code> is also used in which case a calculated size is displayed. </p>
 </dd>
<dt><code>-s</code></dt>
<dd>  </dd>
<dt><code>--print-armap</code></dt>
<dd> <p> When listing symbols from archive members, include the index: a mapping (stored in the archive by <code>ar</code> or <code>ranlib</code>) of which modules contain definitions for which names. </p>
 </dd>
<dt><code>-t</code><i>radix</i></dt>
<dd>  </dd>
<dt><code>--radix=</code><i>radix</i></dt>
<dd> <p> Use <i>radix</i> as the radix for printing the symbol values. It must be <code>d</code> for decimal, <code>o</code> for octal, or <code>x</code> for hexadecimal. </p>
 </dd>
<dt><code>-u</code></dt>
<dd>  </dd>
<dt><code>--undefined-only</code></dt>
<dd> <p> Display only undefined symbols (those external to each object file). </p>
 </dd>
<dt><code>-U</code><i>[d|i|l|e|x|h]</i></dt>
<dd>  </dd>
<dt><code>--unicode=</code><i>[default|invalid|locale|escape|hex|highlight]</i></dt>
<dd> <p> Controls the display of UTF-8 encoded multibyte characters in strings. The default (<code>--unicode=default</code>) is to give them no special treatment. The <code>--unicode=locale</code> option displays the sequence in the current locale, which may or may not support them. The options <code>--unicode=hex</code> and <code>--unicode=invalid</code> display them as hex byte sequences enclosed by either angle brackets or curly braces. </p>
<p> The <code>--unicode=escape</code> option displays them as escape sequences (<i>\uxxxx</i>) and the <code>--unicode=highlight</code> option displays them as escape sequences highlighted in red (if supported by the output device). The colouring is intended to draw attention to the presence of unicode sequences where they might not be expected. </p>
 </dd>
<dt><code>-V</code></dt>
<dd>  </dd>
<dt><code>--version</code></dt>
<dd> <p> Show the version number of <code>nm</code> and exit. </p>
 </dd>
<dt><code>-X</code></dt>
<dd> <p> This option is ignored for compatibility with the AIX version of <code>nm</code>. It takes one parameter which must be the string <code>32_64</code>. The default mode of AIX <code>nm</code> corresponds to <code>-X 32</code>, which is not supported by GNU <code>nm</code>. </p>
 </dd>
<dt><code>--defined-only</code></dt>
<dd> <p> Display only defined symbols for each object file. </p>
 </dd>
<dt><code>--plugin</code><i>name</i></dt>
<dd> <p> Load the plugin called <i>name</i> to add support for extra target types. This option is only available if the toolchain has been built with plugin support enabled. </p>
<p> If <code>--plugin</code> is not provided, but plugin support has been enabled then <code>nm</code> iterates over the files in <i>${libdir}/bfd-plugins</i> in alphabetic order and the first plugin that claims the object in question is used. </p>
<p> Please note that this plugin search directory is <i>not</i> the one used by <code>ld</code>&#8216;s <code>-plugin</code> option. In order to make <code>nm</code> use the linker plugin it must be copied into the <i>${libdir}/bfd-plugins</i> directory. For GCC based compilations the linker plugin is called <i>liblto_plugin.so.0.0.0</i>. For Clang based compilations it is called <i>LLVMgold.so</i>. The GCC plugin is always backwards compatible with earlier versions, so it is sufficient to just copy the newest one. </p>
 </dd>
<dt><code>--size-sort</code></dt>
<dd> <p> Sort symbols by size. For ELF objects symbol sizes are read from the ELF, for other object types the symbol sizes are computed as the difference between the value of the symbol and the value of the symbol with the next higher value. If the <code>&quot;bsd&quot;</code> output format is used the size of the symbol is printed, rather than the value, and <code>-S</code> must be used in order both size and value to be printed. </p>
 </dd>
<dt><code>--special-syms</code></dt>
<dd> <p> Display symbols which have a target-specific special meaning. These symbols are usually used by the target for some special processing and are not normally helpful when included in the normal symbol lists. For example for ARM targets this option would skip the mapping symbols used to mark transitions between ARM code, THUMB code and data. </p>
 </dd>
<dt><code>--synthetic</code></dt>
<dd> <p> Include synthetic symbols in the output. These are special symbols created by the linker for various purposes. They are not shown by default since they are not part of the binary&#8217;s original source code. </p>
 </dd>
<dt><code>--with-symbol-versions</code></dt>
<dd>  </dd>
<dt><code>--without-symbol-versions</code></dt>
<dd> <p> Enables or disables the display of symbol version information. The version string is displayed as a suffix to the symbol name, preceded by an @ character. For example <code>foo [at] VER_1</code>. If the version is the default version to be used when resolving unversioned references to the symbol then it is displayed as a suffix preceded by two @ characters. For example <code>foo@@VER_2</code>. By default, symbol version information is displayed. </p>
 </dd>
<dt><code>--target=</code><i>bfdname</i></dt>
<dd> <p> Specify an object code format other than your system&#8217;s default format. </p>
 </dd>
<dt><code>@</code><i>file</i></dt>
<dd> <p> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ar/">ar</a></code>(1), <code><a href="/docs/linux/man/1-objdump/">objdump</a></code>(1), <code><a href="/docs/linux/man/1-ranlib/">ranlib</a></code>(1), and the Info entries for <i>binutils</i>.  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2022 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled ``GNU Free Documentation License&#8217;&#8216;. </p>
