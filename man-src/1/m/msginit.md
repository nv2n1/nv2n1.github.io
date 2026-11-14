---
title: "msginit(1)"
name: "msginit"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msginit/"
description: "msginit – initialize a message catalog"
---

<h2 class="name">NAME</h2>
<p> msginit &#8211; initialize a message catalog </p>
<h2>SYNOPSIS</h2>
<p> <code>msginit</code> [<i>OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> Creates a new PO file, initializing the meta information with values from the user&#8217;s environment. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;input</code>=<i>INPUTFILE</i></p>
<dd> input POT file</dl>
<p> If no input file is given, the current directory is searched for the POT file. If it is -, standard input is read.</p>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> write output to specified PO file</dl>
<p> If no output file is given, it depends on the <code>&#8211;locale</code> option or the user&#8217;s locale setting. If it is -, the results are written to standard output.</p>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></p>
<dd> input file is in Java .properties syntax</p>
<dt><code>&#8211;stringtable-input</code></p>
<dd> input file is in NeXTstep/GNUstep .strings syntax</dl>
<h3>Output details:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LL_CC</i></p>
<dd> set target locale</p>
<dt><code>&#8211;no-translator</code></p>
<dd> assume the PO file is automatically generated</p>
<dt><code>&#8211;color</code></p>
<dd> use colors and other text attributes always</p>
<dt><code>&#8211;color</code>=<i>WHEN</i></p>
<dd> use colors and other text attributes if WHEN. WHEN may be &#8216;always&#8217;, &#8216;never&#8217;, &#8216;auto&#8217;, or &#8216;html&#8217;.</p>
<dt><code>&#8211;style</code>=<i>STYLEFILE</i></p>
<dd> specify CSS style rule file for <code>&#8211;color</code></p>
<dt><code>-p</code>, <code>&#8211;properties-output</code></p>
<dd> write out a Java .properties file</p>
<dt><code>&#8211;stringtable-output</code></p>
<dd> write out a NeXTstep/GNUstep .strings file</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>NUMBER</i></p>
<dd> set output page width</p>
<dt><code>&#8211;no-wrap</code></p>
<dd> do not break long message lines, longer than the output page width, into several lines</dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Bruno Haible.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnu-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2016 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>msginit</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msginit</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info msginit</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
