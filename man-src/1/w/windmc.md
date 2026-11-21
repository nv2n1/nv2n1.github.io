---

title: "windmc(1)"
name: "windmc"
section: "1"
letter: "w"
url: "/docs/linux/man/1-windmc/"
description: "windmc – generates Windows message resources."
---

<p> windmc &#8211; generates Windows message resources. </p>
<h2>SYNOPSIS</h2>
<p> windmc [options] input-file</p>
<h2>DESCRIPTION</h2>
<p> <code>windmc</code> reads message definitions from an input file (.mc) and translate them into a set of output files. The output files may be of four kinds:</p>
<dl>
<dt>&quot;h&quot;</dt>
<dd> A C header file containing the message definitions.</dd>
<dt>&quot;rc&quot;</dt>
<dd> A resource file compilable by the <code>windres</code> tool.</dd>
<dt>&quot;bin&quot;</dt>
<dd> One or more binary files containing the resource data for a specific message language.</dd>
<dt>&quot;dbg&quot;</dt>
<dd> A C include file that maps message id&#8217;s to their symbolic name.</dd></dl>
<p> The exact description of these different formats is available in documentation from Microsoft. </p>
<p> When <code>windmc</code> converts from the <tt>&quot;mc&quot;</tt> format to the <tt>&quot;bin&quot;</tt> format, <tt>&quot;rc&quot;</tt>, <tt>&quot;h&quot;</tt>, and optional <tt>&quot;dbg&quot;</tt> it is acting like the Windows Message Compiler.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd>
</dd><dt><code>&#8211;ascii_in</code></dt>
<dd> Specifies that the input file specified is <font SIZE="-1">ASCII.</font> This is the default behaviour.</dd>
<dt><code>-A</code></dt>
<dd>
</dd><dt><code>&#8211;ascii_out</code></dt>
<dd> Specifies that messages in the output <tt>&quot;bin&quot;</tt> files should be in <font SIZE="-1">ASCII</font> format.</dd>
<dt><code>-b</code></dt>
<dd>
</dd><dt><code>&#8211;binprefix</code></dt>
<dd> Specifies that <tt>&quot;bin&quot;</tt> filenames should have to be prefixed by the basename of the source file.</dd>
<dt><code>-c</code></dt>
<dd>
</dd><dt><code>&#8211;customflag</code></dt>
<dd> Sets the customer bit in all message id&#8217;s.</dd>
<dt><code>-C</code> <i>codepage</i></dt>
<dd>
</dd><dt><code>&#8211;codepage_in</code> <i>codepage</i></dt>
<dd> Sets the default codepage to be used to convert input file to <font SIZE="-1">UTF16.</font> The default is ocdepage 1252.</dd>
<dt><code>-d</code></dt>
<dd>
</dd><dt><code>&#8211;decimal_values</code></dt>
<dd> Outputs the constants in the header file in decimal. Default is using hexadecimal output.</dd>
<dt><code>-e</code> <i>ext</i></dt>
<dd>
</dd><dt><code>&#8211;extension</code> <i>ext</i></dt>
<dd> The extension for the header file. The default is .h extension.</dd>
<dt><code>-F</code> <i>target</i></dt>
<dd>
</dd><dt><code>&#8211;target</code> <i>target</i></dt>
<dd> Specify the <font SIZE="-1">BFD</font> format to use for a bin file as output. This is a <font SIZE="-1">BFD</font> target name; you can use the <code>&#8211;help</code> option to see a list of supported targets. Normally <code>windmc</code> will use the default format, which is the first one listed by the <code>&#8211;help</code> option.</dd>
<dt><code>-h</code> <i>path</i></dt>
<dd>
</dd><dt><code>&#8211;headerdir</code> <i>path</i></dt>
<dd> The target directory of the generated header file. The default is the current directory.</dd>
<dt><code>-H</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd> Displays a list of command line options and then exits.</dd>
<dt><code>-m</code> <i>characters</i></dt>
<dd>
</dd><dt><code>&#8211;maxlength</code> <i>characters</i></dt>
<dd> Instructs <code>windmc</code> to generate a warning if the length of any message exceeds the number specified.</dd>
<dt><code>-n</code></dt>
<dd>
</dd><dt><code>&#8211;nullterminate</code></dt>
<dd> Terminate message text in <tt>&quot;bin&quot;</tt> files by zero. By default they are terminated by <font SIZE="-1">CR/LF.</font></dd>
<dt><code>-o</code></dt>
<dd>
</dd><dt><code>&#8211;hresult_use</code></dt>
<dd> Not yet implemented. Instructs <tt>&quot;windmc&quot;</tt> to generate an <font SIZE="-1">OLE2</font> header file, using <font SIZE="-1">HRESULT</font> definitions. Status codes are used if the flag is not specified.</dd>
<dt><code>-O</code> <i>codepage</i></dt>
<dd>
</dd><dt><code>&#8211;codepage_out</code> <i>codepage</i></dt>
<dd> Sets the default codepage to be used to output text files. The default is ocdepage 1252.</dd>
<dt><code>-r</code> <i>path</i></dt>
<dd>
</dd><dt><code>&#8211;rcdir</code> <i>path</i></dt>
<dd> The target directory for the generated <tt>&quot;rc&quot;</tt> script and the generated <tt>&quot;bin&quot;</tt> files that the resource compiler script includes. The default is the current directory.</dd>
<dt><code>-u</code></dt>
<dd>
</dd><dt><code>&#8211;unicode_in</code></dt>
<dd> Specifies that the input file is <font SIZE="-1">UTF16.</font></dd>
<dt><code>-U</code></dt>
<dd>
</dd><dt><code>&#8211;unicode_out</code></dt>
<dd> Specifies that messages in the output <tt>&quot;bin&quot;</tt> file should be in <font SIZE="-1">UTF16</font> format. This is the default behaviour.</dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;verbose</code></dt>
<dd> Enable verbose mode.</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Prints the version number for <code>windmc</code>.</dd>
<dt><code>-x</code> <i>path</i></dt>
<dd>
</dd><dt><code>&#8211;xdgb</code> <i>path</i></dt>
<dd> The path of the <tt>&quot;dbg&quot;</tt> C include file that maps message id&#8217;s to the symbolic name. No such file is generated without specifying the switch.</dd>
<dt><code>@</code><i>file</i></dt>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </dd>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2014 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
