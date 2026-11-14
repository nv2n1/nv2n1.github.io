---
title: "msgfilter(1)"
name: "msgfilter"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgfilter/"
description: "msgfilter – edit translations of message catalog"
---

<h2 class="name">NAME</h2>
<p> msgfilter &#8211; edit translations of message catalog </p>
<h2>SYNOPSIS</h2>
<p> <code>msgfilter</code> [<i>OPTION</i>] <i>FILTER </i>[<i>FILTER-OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> Applies a filter to all translations of a translation catalog. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;input</code>=<i>INPUTFILE</i></p>
<dd> input PO file</p>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></p>
<dd> add DIRECTORY to list for input files search</dl>
<p> If no input file is given or if it is -, standard input is read.</p>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> write output to specified file</dl>
<p> The results are written to standard output if no output file is specified or if it is -. </p>
<p> The FILTER can be any program that reads a translation from standard input and writes a modified translation to standard output.</p>
<h3>Filter input and output:</h3>
<dl>
<dt><code>&#8211;newline</code></p>
<dd> add a newline at the end of input and remove a newline from the end of output</dl>
<h3>Useful FILTER-OPTIONs when the FILTER is &#8216;sed&#8217;:</h3>
<dl>
<dt><code>-e</code>, <code>&#8211;expression</code>=<i>SCRIPT</i></p>
<dd> add SCRIPT to the commands to be executed</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>SCRIPTFILE</i></p>
<dd> add the contents of SCRIPTFILE to the commands to be executed</p>
<dt><code>-n</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> suppress automatic printing of pattern space</dl>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></p>
<dd> input file is in Java .properties syntax</p>
<dt><code>&#8211;stringtable-input</code></p>
<dd> input file is in NeXTstep/GNUstep .strings syntax</dl>
<h3>Output details:</h3>
<dl>
<dt><code>&#8211;color</code></p>
<dd> use colors and other text attributes always</p>
<dt><code>&#8211;color</code>=<i>WHEN</i></p>
<dd> use colors and other text attributes if WHEN. WHEN may be &#8216;always&#8217;, &#8216;never&#8217;, &#8216;auto&#8217;, or &#8216;html&#8217;.</p>
<dt><code>&#8211;style</code>=<i>STYLEFILE</i></p>
<dd> specify CSS style rule file for <code>&#8211;color</code></p>
<dt><code>&#8211;no-escape</code></p>
<dd> do not use C escapes in output (default)</p>
<dt><code>-E</code>, <code>&#8211;escape</code></p>
<dd> use C escapes in output, no extended chars</p>
<dt><code>&#8211;force-po</code></p>
<dd> write PO file even if empty</p>
<dt><code>&#8211;indent</code></p>
<dd> indented output style</p>
<dt><code>&#8211;keep-header</code></p>
<dd> keep header entry unmodified, don&#8217;t filter it</p>
<dt><code>&#8211;no-location</code></p>
<dd> suppress &#8216;#: filename:line&#8217; lines</p>
<dt><code>-n</code>, <code>&#8211;add-location</code></p>
<dd> preserve &#8216;#: filename:line&#8217; lines (default)</p>
<dt><code>&#8211;strict</code></p>
<dd> strict Uniforum output style</p>
<dt><code>-p</code>, <code>&#8211;properties-output</code></p>
<dd> write out a Java .properties file</p>
<dt><code>&#8211;stringtable-output</code></p>
<dd> write out a NeXTstep/GNUstep .strings file</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>NUMBER</i></p>
<dd> set output page width</p>
<dt><code>&#8211;no-wrap</code></p>
<dd> do not break long message lines, longer than the output page width, into several lines</p>
<dt><code>-s</code>, <code>&#8211;sort-output</code></p>
<dd> generate sorted output</p>
<dt><code>-F</code>, <code>&#8211;sort-by-file</code></p>
<dd> sort output by file location</dl>
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
<p> The full documentation for <code>msgfilter</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msgfilter</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info msgfilter</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
