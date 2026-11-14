---
title: "i686-pc-mingw32-addr2line(1)"
name: "i686-pc-mingw32-addr2line"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i686-pc-mingw32-addr2line/"
description: "addr2line – convert addresses into file names and line numbers."
---

<h2 class="name">NAME</h2>
<p> addr2line &#8211; convert addresses into file names and line numbers. </p>
<h2>SYNOPSIS</h2>
<p> addr2line [<code>-b</code> <i>bfdname</i>|<code>&#8211;target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-C</code>|<code>&#8211;demangle</code>[=<i>style</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-e</code>&nbsp;<wbr><i>filename</i>|<code>&#8211;exe=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-f</code>|<code>&#8211;functions</code>]&nbsp;<wbr>[<code>-s</code>|<code>&#8211;basename</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-i</code>|<code>&#8211;inlines</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-j</code>|<code>&#8211;section=</code><i>name</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-H</code>|<code>&#8211;help</code>]&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[addr addr &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>addr2line</code> translates addresses into file names and line numbers. Given an address in an executable or an offset in a section of a relocatable object, it uses the debugging information to figure out which file name and line number are associated with it. </p>
<p> The executable or relocatable object to use is specified with the <code>-e</code> option. The default is the file <i>a.out</i>. The section in the relocatable object to use is specified with the <code>-j</code> option. </p>
<p> <code>addr2line</code> has two modes of operation. </p>
<p> In the first, hexadecimal addresses are specified on the command line, and <code>addr2line</code> displays the file name and line number for each address. </p>
<p> In the second, <code>addr2line</code> reads hexadecimal addresses from standard input, and prints the file name and line number for each address on standard output. In this mode, <code>addr2line</code> may be used in a pipe to convert dynamically chosen addresses. </p>
<p> The format of the output is <font SIZE="-1"><code>FILENAME:LINENO</code></font>. The file name and line number for each address is printed on a separate line. If the <code>-f</code> option is used, then each <font SIZE="-1"><code>FILENAME:LINENO</code></font> line is preceded by a <font SIZE="-1"><code>FUNCTIONNAME</code></font> line which is the name of the function containing the address. </p>
<p> If the file name or function name can not be determined, <code>addr2line</code> will print two question marks in their place. If the line number can not be determined, <code>addr2line</code> will print 0.</p>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent.</p>
<dl>
<dt><code>-b</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;target=</code><i>bfdname</i></p>
<dd> Specify that the object-code format for the object files is <i>bfdname</i>.</p>
<dt><code>-C</code></p>
<dd>
<dt><code>&#8211;demangle[=</code><i>style</i><code>]</code></p>
<dd> Decode (<i>demangle</i>) low-level symbol names into user-level names. Besides removing any initial underscore prepended by the system, this makes C<font SIZE="-2">++</font> function names readable. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler.</p>
<dt><code>-e</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;exe=</code><i>filename</i></p>
<dd> Specify the name of the executable for which addresses should be translated. The default file is <i>a.out</i>.</p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;functions</code></p>
<dd> Display function names as well as file and line number information.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;basenames</code></p>
<dd> Display only the base of each file name.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;inlines</code></p>
<dd> If the address belongs to a function that was inlined, the source information for all enclosing scopes back to the first non-inlined function will also be printed. For example, if <tt>&quot;main&quot;</tt> inlines <tt>&quot;callee1&quot;</tt> which inlines <tt>&quot;callee2&quot;</tt>, and address is from <tt>&quot;callee2&quot;</tt>, the source information for <tt>&quot;callee1&quot;</tt> and <tt>&quot;main&quot;</tt> will also be printed.</p>
<dt><code>-j</code></p>
<dd>
<dt><code>&#8211;section</code></p>
<dd> Read offsets relative to the specified section instead of absolute addresses.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
