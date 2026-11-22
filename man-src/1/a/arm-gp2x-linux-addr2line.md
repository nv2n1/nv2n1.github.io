---

title: "arm-gp2x-linux-addr2line(1)"
name: "arm-gp2x-linux-addr2line"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm-gp2x-linux-addr2line/"
description: "addr2line – convert addresses into file names and line numbers."
---

<p> addr2line &#8211; convert addresses into file names and line numbers.</p>
<h2>SYNOPSIS</h2>
<p> addr2line [<code>-b</code> <i>bfdname</i>|<code>&#8211;target=</code><i>bfdname</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-C</code>|<code>&#8211;demangle</code>[=<i>style</i>]]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-e</code>&nbsp;<wbr><i>filename</i>|<code>&#8211;exe=</code><i>filename</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-f</code>|<code>&#8211;functions</code>]&nbsp;<wbr>[<code>-s</code>|<code>&#8211;basename</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-H</code>|<code>&#8211;help</code>]&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[addr addr &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>addr2line</code> translates program addresses into file names and line numbers. Given an address and an executable, it uses the debugging information in the executable to figure out which file name and line number are associated with a given address. </p>
<p> The executable to use is specified with the <code>-e</code> option. The default is the file <i>a.out</i>. </p>
<p> <code>addr2line</code> has two modes of operation. </p>
<p> In the first, hexadecimal addresses are specified on the command line, and <code>addr2line</code> displays the file name and line number for each address. </p>
<p> In the second, <code>addr2line</code> reads hexadecimal addresses from standard input, and prints the file name and line number for each address on standard output. In this mode, <code>addr2line</code> may be used in a pipe to convert dynamically chosen addresses. </p>
<p> The format of the output is <code>FILENAME:LINENO</code>. The file name and line number for each address is printed on a separate line. If the <code>-f</code> option is used, then each <code>FILENAME:LINENO</code> line is preceded by a <code>FUNCTIONNAME</code> line which is the name of the function containing the address. </p>
<p> If the file name or function name can not be determined, <code>addr2line</code> will print two question marks in their place. If the line number can not be determined, <code>addr2line</code> will print 0.</p>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent.</p>
<dl>
<dt><code>-b</code> <i>bfdname</i></dt>
<dd>
</dd><dt><code>&#8211;target=</code><i>bfdname</i></dt>
<dd> Specify that the object-code format for the object files is <i>bfdname</i>.</dd>
<dt><code>-C</code></dt>
<dd>
</dd><dt><code>&#8211;demangle[=</code><i>style</i><code>]</code></dt>
<dd> Decode (<i>demangle</i>) low-level symbol names into user-level names. Besides removing any initial underscore prepended by the system, this makes C++ function names readable. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler.</dd>
<dt><code>-e</code> <i>filename</i></dt>
<dd>
</dd><dt><code>&#8211;exe=</code><i>filename</i></dt>
<dd> Specify the name of the executable for which addresses should be translated. The default file is <i>a.out</i>.</dd>
<dt><code>-f</code></dt>
<dd>
</dd><dt><code>&#8211;functions</code></dt>
<dd> Display function names as well as file and line number information.</dd>
<dt><code>-s</code></dt>
<dd>
</dd><dt><code>&#8211;basenames</code></dt>
<dd> Display only the base of each file name.</dd></dl>
<h2>SEE ALSO</h2>
<p> Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;GNU Free Documentation License&#8221;. </p>
