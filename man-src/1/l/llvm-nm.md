---
title: "llvm-nm(1)"
name: "llvm-nm"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-nm/"
description: "llvm-nm – list LLVM bitcode file’s symbol table"
---

<h2 class="name">NAME</h2>
<p> llvm-nm &#8211; list LLVM bitcode file&#8217;s symbol table </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-nm</code> [<i>options</i>] [<i>filenames&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-nm</code> utility lists the names of symbols from the <font SIZE="-1">LLVM</font> bitcode files, or <code>ar</code> archives containing <font SIZE="-1">LLVM</font> bitcode files, named on the command line. Each symbol is listed along with some simple information about its provenance. If no file name is specified, or <i>&#8211;</i> is used as a file name, <code>llvm-nm</code> will process a bitcode file on its standard input stream. </p>
<p> <code>llvm-nm</code>&#8216;s default output format is the traditional <font SIZE="-1">BSD</font> <code>nm</code> output format. Each such output record consists of an (optional) 8-digit hexadecimal address, followed by a type code character, followed by a name, for each symbol. One record is printed per line; fields are separated by spaces. When the address is omitted, it is replaced by 8 spaces. </p>
<p> Type code characters currently supported, and their meanings, are as follows:</p>
<dl>
<dt>U</p>
<dd> Named object is referenced but undefined in this bitcode file</p>
<dt>C</p>
<dd> Common (multiple definitions link together into one def)</p>
<dt>W</p>
<dd> Weak reference (multiple definitions link together into zero or one definitions)</p>
<dt>t</p>
<dd> Local function (text) object</p>
<dt>T</p>
<dd> Global function (text) object</p>
<dt>d</p>
<dd> Local data object</p>
<dt>D</p>
<dd> Global data object</p>
<dt>?</p>
<dd> Something unrecognizable</dl>
<p> Because <font SIZE="-1">LLVM</font> bitcode files typically contain objects that are not considered to have addresses until they are linked into an executable image or dynamically compiled &#8220;just-in-time&#8221;, <code>llvm-nm</code> does not print an address for any symbol, even symbols which are defined in the bitcode file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-P</code></p>
<dd> Use <font SIZE="-1">POSIX</font>.2 output format. Alias for <code>&#8211;format=posix</code>.</p>
<dt><code>-B</code> (default)</p>
<dd> Use <font SIZE="-1">BSD</font> output format. Alias for <code>&#8211;format=bsd</code>.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command-line options and their meanings.</p>
<dt><code>&#8211;defined-only</code></p>
<dd> Print only symbols defined in this bitcode file (as opposed to symbols which may be referenced by objects in this file, but not defined in this file.)</p>
<dt><code>&#8211;extern-only</code>, <code>-g</code></p>
<dd> Print only symbols whose definitions are external; that is, accessible from other bitcode files.</p>
<dt><code>&#8211;undefined-only</code>, <code>-u</code></p>
<dd> Print only symbols referenced but not defined in this bitcode file.</p>
<dt><code>&#8211;format=</code><i>fmt</i>, <code>-f</code></p>
<dd> Select an output format; <i>fmt</i> may be <i>sysv</i>, <i>posix</i>, or <i>bsd</i>. The default is <i>bsd</i>.</dl>
<h2>BUGS</h2>
<p> <code>llvm-nm</code> cannot demangle C<font SIZE="-2">++</font> mangled names, like <font SIZE="-1">GNU</font> <code>nm</code> can.</p>
<h2>EXIT STATUS</h2>
<p> <code>llvm-nm</code> exits with an exit code of zero.</p>
<h2>SEE ALSO</h2>
<p> llvm-dis, <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1), <i><a href="/docs/linux/man/1-nm/">nm</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
