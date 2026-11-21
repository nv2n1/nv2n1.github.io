---
title: "msgunfmt(1)"
name: "msgunfmt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgunfmt/"
description: "msgunfmt – uncompile message catalog from binary format"
---

<h2 class="name">NAME</h2>
<p> msgunfmt &#8211; uncompile message catalog from binary format </p>
<h2>SYNOPSIS</h2>
<p> <code>msgunfmt</code> [<i>OPTION</i>] [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Convert binary message catalog to Uniforum style .po file. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Operation mode:</h3>
<dl>
<dt><code>-j</code>, <code>&#8211;java</code></dt>
<dd> Java mode: input is a Java ResourceBundle class</dd>
<dt><code>&#8211;csharp</code></dt>
<dd> C# mode: input is a .NET .dll file</dd>
<dt><code>&#8211;csharp-resources</code></dt>
<dd> C# resources mode: input is a .NET .resources file</dd>
<dt><code>&#8211;tcl</code></dt>
<dd> Tcl mode: input is a tcl/msgcat .msg file</dd></dl>
<h3>Input file location:</h3>
<dl>
<dt>FILE &#8230;</dt>
<dd> input .mo files</dd></dl>
<p> If no input file is given or if it is -, standard input is read.</p>
<h3>Input file location in Java mode:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;resource</code>=<i>RESOURCE</i></dt>
<dd> resource name</dd>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></dt>
<dd> locale name, either language or language_COUNTRY</dd></dl>
<p> The class name is determined by appending the locale name to the resource name, separated with an underscore. The class is located using the CLASSPATH.</p>
<h3>Input file location in C# mode:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;resource</code>=<i>RESOURCE</i></dt>
<dd> resource name</dd>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></dt>
<dd> locale name, either language or language_COUNTRY</dd>
<dt><code>-d</code> DIRECTORY</dt>
<dd> base directory for locale dependent .dll files</dd></dl>
<p> The <code>-l</code> and <code>-d</code> options are mandatory. The .dll file is located in a subdirectory of the specified directory whose name depends on the locale.</p>
<h3>Input file location in Tcl mode:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></dt>
<dd> locale name, either language or language_COUNTRY</dd>
<dt><code>-d</code> DIRECTORY</dt>
<dd> base directory of .msg message catalogs</dd></dl>
<p> The <code>-l</code> and <code>-d</code> options are mandatory. The .msg file is located in the specified directory.</p>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> write output to specified file</dd></dl>
<p> The results are written to standard output if no output file is specified or if it is -.</p>
<h3>Output details:</h3>
<dl>
<dt><code>&#8211;color</code></dt>
<dd> use colors and other text attributes always</dd>
<dt><code>&#8211;color</code>=<i>WHEN</i></dt>
<dd> use colors and other text attributes if WHEN. WHEN may be &#8216;always&#8217;, &#8216;never&#8217;, &#8216;auto&#8217;, or &#8216;html&#8217;.</dd>
<dt><code>&#8211;style</code>=<i>STYLEFILE</i></dt>
<dd> specify CSS style rule file for <code>&#8211;color</code></dd>
<dt><code>-e</code>, <code>&#8211;no-escape</code></dt>
<dd> do not use C escapes in output (default)</dd>
<dt><code>-E</code>, <code>&#8211;escape</code></dt>
<dd> use C escapes in output, no extended chars</dd>
<dt><code>&#8211;force-po</code></dt>
<dd> write PO file even if empty</dd>
<dt><code>-i</code>, <code>&#8211;indent</code></dt>
<dd> write indented output style</dd>
<dt><code>&#8211;strict</code></dt>
<dd> write strict uniforum style</dd>
<dt><code>-p</code>, <code>&#8211;properties-output</code></dt>
<dd> write out a Java .properties file</dd>
<dt><code>&#8211;stringtable-output</code></dt>
<dd> write out a NeXTstep/GNUstep .strings file</dd>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>NUMBER</i></dt>
<dd> set output page width</dd>
<dt><code>&#8211;no-wrap</code></dt>
<dd> do not break long message lines, longer than the output page width, into several lines</dd>
<dt><code>-s</code>, <code>&#8211;sort-output</code></dt>
<dd> generate sorted output</dd></dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> increase verbosity level</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Ulrich Drepper.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnu-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-1998, 2000-2016 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>msgunfmt</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msgunfmt</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info msgunfmt</code></dd></dl>
<p> should give you access to the complete manual. </p>
