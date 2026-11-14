---
title: "cross-nlmconv(1)"
name: "cross-nlmconv"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cross-nlmconv/"
description: "nlmconv – converts object code into an NLM."
---

<h2 class="name">NAME</h2>
<p> nlmconv &#8211; converts object code into an NLM. </p>
<h2>SYNOPSIS</h2>
<p> nlmconv [<code>-I</code> <i>bfdname</i>|<code>&#8211;input-target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-O</code>&nbsp;<wbr><i>bfdname</i>|<code>&#8211;output-target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-T</code>&nbsp;<wbr><i>headerfile</i>|<code>&#8211;header-file=</code><i>headerfile</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-d</code>|<code>&#8211;debug</code>]&nbsp;<wbr>[<code>-l</code>&nbsp;<wbr><i>linker</i>|<code>&#8211;linker=</code><i>linker</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-h</code>|<code>&#8211;help</code>]&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr><i>infile</i>&nbsp;<wbr><i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>nlmconv</code> converts the relocatable <code>i386</code> object file <i>infile</i> into the NetWare Loadable Module <i>outfile</i>, optionally reading <i>headerfile</i> for <font SIZE="-1">NLM</font> header information. For instructions on writing the <font SIZE="-1">NLM</font> command file language used in header files, see the <code>linkers</code> section, <font SIZE="-1"><code>NLMLINK</code></font> in particular, of the <i></i><font SIZE="-1"><i>NLM</i></font><i> Development and Tools Overview</i>, which is part of the <font SIZE="-1">NLM</font> Software Developer&#8217;s Kit (&#8220;<font SIZE="-1">NLM SDK&#8221;</font>), available from Novell, Inc. <code>nlmconv</code> uses the <font SIZE="-1">GNU</font> Binary File Descriptor library to read <i>infile</i>; </p>
<p> <code>nlmconv</code> can perform a link step. In other words, you can list more than one object file for input if you list them in the definitions file (rather than simply specifying one input file on the command line). In this case, <code>nlmconv</code> calls the linker for you.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-I</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;input-target=</code><i>bfdname</i></p>
<dd> Object format of the input file. <code>nlmconv</code> can usually determine the format of a given file (so no default is necessary).</p>
<dt><code>-O</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;output-target=</code><i>bfdname</i></p>
<dd> Object format of the output file. <code>nlmconv</code> infers the output format based on the input format, e.g. for a <code>i386</code> input file the output format is <code>nlm32-i386</code>.</p>
<dt><code>-T</code> <i>headerfile</i></p>
<dd>
<dt><code>&#8211;header-file=</code><i>headerfile</i></p>
<dd> Reads <i>headerfile</i> for <font SIZE="-1">NLM</font> header information. For instructions on writing the <font SIZE="-1">NLM</font> command file language used in header files, see see the <code>linkers</code> section, of the <i></i><font SIZE="-1"><i>NLM</i></font><i> Development and Tools Overview</i>, which is part of the <font SIZE="-1">NLM</font> Software Developer&#8217;s Kit, available from Novell, Inc.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;debug</code></p>
<dd> Displays (on standard error) the linker command line used by <code>nlmconv</code>.</p>
<dt><code>-l</code> <i>linker</i></p>
<dd>
<dt><code>&#8211;linker=</code><i>linker</i></p>
<dd> Use <i>linker</i> for any linking. <i>linker</i> can be an absolute or a relative pathname.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Prints a usage summary.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Prints the version number for <code>nlmconv</code>.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2015 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
