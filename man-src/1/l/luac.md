---
title: "luac(1)"
name: "luac"
section: "1"
letter: "l"
url: "/docs/linux/man/1-luac/"
description: "luac – Lua compiler"
---

<h2>NAME</h2>
<p> luac &#8211; Lua compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>luac</code> [ <i>options</i> ] [ <i>filenames</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>luac</code> is the Lua compiler. It translates programs written in the Lua programming language into binary files that can be later loaded and executed. </p>
<p> The main advantages of precompiling chunks are: faster loading, protecting source code from accidental user changes, and off-line syntax checking. </p>
<p> Pre-compiling does not imply faster execution because in Lua chunks are always compiled into bytecodes before being executed. <code>luac</code> simply allows those bytecodes to be saved in a file for later execution. </p>
<p> Pre-compiled chunks are not necessarily smaller than the corresponding source. The main goal in pre-compiling is faster loading. </p>
<p> The binary files created by <code>luac</code> are portable only among architectures with the same word size and byte order. </p>
<p> <code>luac</code> produces a single output file containing the bytecodes for all source files given. By default, the output file is named <code>luac.out</code>, but you can change this with the <code>-o</code> option. </p>
<p> In the command line, you can mix text files containing Lua source and binary files containing precompiled chunks. This is useful to combine several precompiled chunks, even from different (but compatible) platforms, into a single precompiled chunk. </p>
<p> You can use <code>&#8216;-&#8216;</code> to indicate the standard input as a source file and <code>&#8216;&#8211;&#8216;</code> to signal the end of options (that is, all remaining arguments will be treated as files even if they start with <code>&#8216;-&#8216;</code>). </p>
<p> The internal format of the binary files produced by <code>luac</code> is likely to change when a new version of Lua is released. So, save the source files of all Lua programs that you precompile. </p>
<h2>OPTIONS</h2>
<p> Options must be separate.</p>
<dl>
<dt><code>-l</code></p>
<dd> produce a listing of the compiled bytecode for Lua&#8217;s virtual machine. Listing bytecodes is useful to learn about Lua&#8217;s virtual machine. If no files are given, then <code>luac</code> loads <code>luac.out</code> and lists its contents.</p>
<dt><code>-o</code><i> file</i></p>
<dd> output to <i>file</i>, instead of the default <code>luac.out</code>. (You can use <code>&#8216;-&#8216;</code> for standard output, but not on platforms that open standard output in text mode.) The output file may be a source file because all files are loaded before the output file is written. Be careful not to overwrite precious files.</p>
<dt><code>-p</code></p>
<dd> load files but do not generate any output file. Used mainly for syntax checking and for testing precompiled chunks: corrupted files will probably generate errors when loaded. Lua always performs a thorough integrity test on precompiled chunks. Bytecode that passes this test is completely safe, in the sense that it will not break the interpreter. However, there is no guarantee that such code does anything sensible. (None can be given, because the halting problem is unsolvable.) If no files are given, then <code>luac</code> loads <code>luac.out</code> and tests its contents. No messages are displayed if the file passes the integrity test.</p>
<dt><code>-s</code></p>
<dd> strip debug information before writing the output file. This saves some space in very large chunks, but if errors occur when running a stripped chunk, then the error messages may not contain the full information they usually do. For instance, line numbers and names of local variables are lost.</p>
<dt><code>-v</code></p>
<dd> show version information.</dl>
<h2>FILES</h2>
<dl>
<dt><code>luac.out</code></p>
<dd> default output file</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lua/">lua</a></code>(1)<br />
 <a rel="nofollow" href="http://www.lua.org/">http://www.lua.org/</a></p>
<h2>DIAGNOSTICS</h2>
<p> Error messages should be self explanatory.</p>
<h2>AUTHORS</h2>
<p> L. H. de Figueiredo, R. Ierusalimschy and W. Celes </p>
<h2>Index</h2>
