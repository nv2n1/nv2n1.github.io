---
title: "i686-w64-mingw32-strings(1)"
name: "i686-w64-mingw32-strings"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i686-w64-mingw32-strings/"
description: "strings – print the strings of printable characters in files."
---

<h2 class="name">NAME</h2>
<p> strings &#8211; print the strings of printable characters in files. </p>
<h2>SYNOPSIS</h2>
<p> strings [<code>-afovV</code>] [<code>&#8211;</code><i>min-len</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-n</code>&nbsp;<wbr><i>min-len</i>]&nbsp;<wbr>[<code>&#8211;bytes=</code><i>min-len</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-t</code>&nbsp;<wbr><i>radix</i>]&nbsp;<wbr>[<code>&#8211;radix=</code><i>radix</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-e</code>&nbsp;<wbr><i>encoding</i>]&nbsp;<wbr>[<code>&#8211;encoding=</code><i>encoding</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;</code>]&nbsp;<wbr>[<code>&#8211;all</code>]&nbsp;<wbr>[<code>&#8211;print-file-name</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-T</code>&nbsp;<wbr><i>bfdname</i>]&nbsp;<wbr>[<code>&#8211;target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-w</code>]&nbsp;<wbr>[<code>&#8211;include-all-whitespace</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;help</code>]&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr><i>file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> For each <i>file</i> given, <font SIZE="-1">GNU </font><code>strings</code> prints the printable character sequences that are at least 4 characters long (or the number given with the options below) and are followed by an unprintable character. </p>
<p> Depending upon how the strings program was configured it will default to either displaying all the printable sequences that it can find in each file, or only those sequences that are in loadable, initialized data sections. If the file type in unrecognizable, or if strings is reading from stdin then it will always display all of the printable sequences that it can find. </p>
<p> For backwards compatibility any file that occurs after a command line option of just <code>&#8211;</code> will also be scanned in full, regardless of the presence of any <code>-d</code> option. </p>
<p> <code>strings</code> is mainly useful for determining the contents of non-text files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;all</code></p>
<dd>
<dt><code>&#8211;</code></p>
<dd> Scan the whole file, regardless of what sections it contains or whether those sections are loaded or initialized. Normally this is the default behaviour, but strings can be configured so that the <code>-d</code> is the default instead. </p>
<p> The <code>&#8211;</code> option is position dependent and forces strings to perform full scans of any file that is mentioned after the <code>&#8211;</code> on the command line, even if the <code>-d</code> option has been specified.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;data</code></p>
<dd> Only print strings from initialized, loaded data sections in the file. This may reduce the amount of garbage in the output, but it also exposes the strings program to any security flaws that may be present in the <font SIZE="-1">BFD</font> library used to scan and load sections. Strings can be configured so that this option is the default behaviour. In such cases the <code>-a</code> option can be used to avoid using the <font SIZE="-1">BFD</font> library and instead just print all of the strings found in the file.</p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;print-file-name</code></p>
<dd> Print the name of the file before each string.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the program usage on the standard output and exit.</p>
<dt><code>&#8211;</code><i>min-len</i></p>
<dd>
<dt><code>-n</code> <i>min-len</i></p>
<dd>
<dt><code>&#8211;bytes=</code><i>min-len</i></p>
<dd> Print sequences of characters that are at least <i>min-len</i> characters long, instead of the default 4.</p>
<dt><code>-o</code></p>
<dd> Like <code>-t o</code>. Some other versions of <code>strings</code> have <code>-o</code> act like <code>-t d</code> instead. Since we can not be compatible with both ways, we simply chose one.</p>
<dt><code>-t</code> <i>radix</i></p>
<dd>
<dt><code>&#8211;radix=</code><i>radix</i></p>
<dd> Print the offset within the file before each string. The single character argument specifies the radix of the offset&#8212;<code>o</code> for octal, <code>x</code> for hexadecimal, or <code>d</code> for decimal.</p>
<dt><code>-e</code> <i>encoding</i></p>
<dd>
<dt><code>&#8211;encoding=</code><i>encoding</i></p>
<dd> Select the character encoding of the strings that are to be found. Possible values for <i>encoding</i> are: <code>s</code> = single-7-bit-byte characters (<font SIZE="-1">ASCII, ISO 8859,</font> etc., default), <code>S</code> = single-8-bit-byte characters, <code>b</code> = 16-bit bigendian, <code>l</code> = 16-bit littleendian, <code>B</code> = 32-bit bigendian, <code>L</code> = 32-bit littleendian. Useful for finding wide character strings. (<code>l</code> and <code>b</code> apply to, for example, Unicode <font SIZE="-1">UTF-16/UCS-2</font> encodings).</p>
<dt><code>-T</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;target=</code><i>bfdname</i></p>
<dd> Specify an object code format other than your system&#8217;s default format.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Print the program version number on the standard output and exit.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;include-all-whitespace</code></p>
<dd> By default tab and space characters are included in the strings that are displayed, but other whitespace characters, such a newlines and carriage returns, are not. The <code>-w</code> option changes this so that all whitespace characters are considered to be part of a string.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1), <i><a href="/docs/linux/man/1-nm/">nm</a></i>(1), <i><a href="/docs/linux/man/1-objdump/">objdump</a></i>(1), <i><a href="/docs/linux/man/1-ranlib/">ranlib</a></i>(1), <i><a href="/docs/linux/man/1-readelf/">readelf</a></i>(1) and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2014 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
