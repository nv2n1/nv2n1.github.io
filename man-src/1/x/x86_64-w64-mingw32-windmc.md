---
title: "x86_64-w64-mingw32-windmc(1)"
name: "x86_64-w64-mingw32-windmc"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-w64-mingw32-windmc/"
description: "windmc – generates Windows message resources."
---

<h2 class="name">NAME</h2>
<p> windmc &#8211; generates Windows message resources. </p>
<h2>SYNOPSIS</h2>
<p> windmc [options] input-file</p>
<h2>DESCRIPTION</h2>
<p> <code>windmc</code> reads message definitions from an input file (.mc) and translate them into a set of output files. The output files may be of four kinds:</p>
<dl>
<dt>&quot;h&quot;</p>
<dd> A C header file containing the message definitions.</p>
<dt>&quot;rc&quot;</p>
<dd> A resource file compilable by the <code>windres</code> tool.</p>
<dt>&quot;bin&quot;</p>
<dd> One or more binary files containing the resource data for a specific message language.</p>
<dt>&quot;dbg&quot;</p>
<dd> A C include file that maps message id&#8217;s to their symbolic name.</dl>
<p> The exact description of these different formats is available in documentation from Microsoft. </p>
<p> When <code>windmc</code> converts from the <tt>&quot;mc&quot;</tt> format to the <tt>&quot;bin&quot;</tt> format, <tt>&quot;rc&quot;</tt>, <tt>&quot;h&quot;</tt>, and optional <tt>&quot;dbg&quot;</tt> it is acting like the Windows Message Compiler.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;ascii_in</code></p>
<dd> Specifies that the input file specified is <font SIZE="-1">ASCII.</font> This is the default behaviour.</p>
<dt><code>-A</code></p>
<dd>
<dt><code>&#8211;ascii_out</code></p>
<dd> Specifies that messages in the output <tt>&quot;bin&quot;</tt> files should be in <font SIZE="-1">ASCII</font> format.</p>
<dt><code>-b</code></p>
<dd>
<dt><code>&#8211;binprefix</code></p>
<dd> Specifies that <tt>&quot;bin&quot;</tt> filenames should have to be prefixed by the basename of the source file.</p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;customflag</code></p>
<dd> Sets the customer bit in all message id&#8217;s.</p>
<dt><code>-C</code> <i>codepage</i></p>
<dd>
<dt><code>&#8211;codepage_in</code> <i>codepage</i></p>
<dd> Sets the default codepage to be used to convert input file to <font SIZE="-1">UTF16.</font> The default is ocdepage 1252.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;decimal_values</code></p>
<dd> Outputs the constants in the header file in decimal. Default is using hexadecimal output.</p>
<dt><code>-e</code> <i>ext</i></p>
<dd>
<dt><code>&#8211;extension</code> <i>ext</i></p>
<dd> The extension for the header file. The default is .h extension.</p>
<dt><code>-F</code> <i>target</i></p>
<dd>
<dt><code>&#8211;target</code> <i>target</i></p>
<dd> Specify the <font SIZE="-1">BFD</font> format to use for a bin file as output. This is a <font SIZE="-1">BFD</font> target name; you can use the <code>&#8211;help</code> option to see a list of supported targets. Normally <code>windmc</code> will use the default format, which is the first one listed by the <code>&#8211;help</code> option.</p>
<dt><code>-h</code> <i>path</i></p>
<dd>
<dt><code>&#8211;headerdir</code> <i>path</i></p>
<dd> The target directory of the generated header file. The default is the current directory.</p>
<dt><code>-H</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Displays a list of command line options and then exits.</p>
<dt><code>-m</code> <i>characters</i></p>
<dd>
<dt><code>&#8211;maxlength</code> <i>characters</i></p>
<dd> Instructs <code>windmc</code> to generate a warning if the length of any message exceeds the number specified.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;nullterminate</code></p>
<dd> Terminate message text in <tt>&quot;bin&quot;</tt> files by zero. By default they are terminated by <font SIZE="-1">CR/LF.</font></p>
<dt><code>-o</code></p>
<dd>
<dt><code>&#8211;hresult_use</code></p>
<dd> Not yet implemented. Instructs <tt>&quot;windmc&quot;</tt> to generate an <font SIZE="-1">OLE2</font> header file, using <font SIZE="-1">HRESULT</font> definitions. Status codes are used if the flag is not specified.</p>
<dt><code>-O</code> <i>codepage</i></p>
<dd>
<dt><code>&#8211;codepage_out</code> <i>codepage</i></p>
<dd> Sets the default codepage to be used to output text files. The default is ocdepage 1252.</p>
<dt><code>-r</code> <i>path</i></p>
<dd>
<dt><code>&#8211;rcdir</code> <i>path</i></p>
<dd> The target directory for the generated <tt>&quot;rc&quot;</tt> script and the generated <tt>&quot;bin&quot;</tt> files that the resource compiler script includes. The default is the current directory.</p>
<dt><code>-u</code></p>
<dd>
<dt><code>&#8211;unicode_in</code></p>
<dd> Specifies that the input file is <font SIZE="-1">UTF16.</font></p>
<dt><code>-U</code></p>
<dd>
<dt><code>&#8211;unicode_out</code></p>
<dd> Specifies that messages in the output <tt>&quot;bin&quot;</tt> file should be in <font SIZE="-1">UTF16</font> format. This is the default behaviour.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose mode.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Prints the version number for <code>windmc</code>.</p>
<dt><code>-x</code> <i>path</i></p>
<dd>
<dt><code>&#8211;xdgb</code> <i>path</i></p>
<dd> The path of the <tt>&quot;dbg&quot;</tt> C include file that maps message id&#8217;s to the symbolic name. No such file is generated without specifying the switch.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2014 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
