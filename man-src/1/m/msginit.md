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
<dt><code>-i</code>, <code>&#8211;input</code>=<i>INPUTFILE</i></dt>
<dd> input POT file</dd></dl>
<p> If no input file is given, the current directory is searched for the POT file. If it is -, standard input is read.</p>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> write output to specified PO file</dd></dl>
<p> If no output file is given, it depends on the <code>&#8211;locale</code> option or the user&#8217;s locale setting. If it is -, the results are written to standard output.</p>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></dt>
<dd> input file is in Java .properties syntax</dd>
<dt><code>&#8211;stringtable-input</code></dt>
<dd> input file is in NeXTstep/GNUstep .strings syntax</dd></dl>
<h3>Output details:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LL_CC</i></dt>
<dd> set target locale</dd>
<dt><code>&#8211;no-translator</code></dt>
<dd> assume the PO file is automatically generated</dd>
<dt><code>&#8211;color</code></dt>
<dd> use colors and other text attributes always</dd>
<dt><code>&#8211;color</code>=<i>WHEN</i></dt>
<dd> use colors and other text attributes if WHEN. WHEN may be &#8216;always&#8217;, &#8216;never&#8217;, &#8216;auto&#8217;, or &#8216;html&#8217;.</dd>
<dt><code>&#8211;style</code>=<i>STYLEFILE</i></dt>
<dd> specify CSS style rule file for <code>&#8211;color</code></dd>
<dt><code>-p</code>, <code>&#8211;properties-output</code></dt>
<dd> write out a Java .properties file</dd>
<dt><code>&#8211;stringtable-output</code></dt>
<dd> write out a NeXTstep/GNUstep .strings file</dd>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>NUMBER</i></dt>
<dd> set output page width</dd>
<dt><code>&#8211;no-wrap</code></dt>
<dd> do not break long message lines, longer than the output page width, into several lines</dd></dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
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
</dt><dd> <code>info msginit</code></dd></dl>
<p> should give you access to the complete manual. </p>
