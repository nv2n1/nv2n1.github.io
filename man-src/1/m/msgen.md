---
title: "msgen(1)"
name: "msgen"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgen/"
description: "msgen – create English message catalog"
---

<h2 class="name">NAME</h2>
<p> msgen &#8211; create English message catalog </p>
<h2>SYNOPSIS</h2>
<p> <code>msgen</code> [<i>OPTION</i>] <i>INPUTFILE</i></p>
<h2>DESCRIPTION</h2>
<p> Creates an English translation catalog. The input file is the last created English PO file, or a PO Template file (generally created by xgettext). Untranslated entries are assigned a translation that is identical to the msgid. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt>INPUTFILE</dt>
<dd> input PO or POT file</dd>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></dt>
<dd> add DIRECTORY to list for input files search</dd></dl>
<p> If input file is -, standard input is read.</p>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> write output to specified file</dd></dl>
<p> The results are written to standard output if no output file is specified or if it is -.</p>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></dt>
<dd> input file is in Java .properties syntax</dd>
<dt><code>&#8211;stringtable-input</code></dt>
<dd> input file is in NeXTstep/GNUstep .strings syntax</dd></dl>
<h3>Output details:</h3>
<dl>
<dt><code>&#8211;lang</code>=<i>CATALOGNAME</i></dt>
<dd> set &#8216;Language&#8217; field in the header entry</dd>
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
<dd> indented output style</dd>
<dt><code>&#8211;no-location</code></dt>
<dd> suppress &#8216;#: filename:line&#8217; lines</dd>
<dt><code>-n</code>, <code>&#8211;add-location</code></dt>
<dd> preserve &#8216;#: filename:line&#8217; lines (default)</dd>
<dt><code>&#8211;strict</code></dt>
<dd> strict Uniforum output style</dd>
<dt><code>-p</code>, <code>&#8211;properties-output</code></dt>
<dd> write out a Java .properties file</dd>
<dt><code>&#8211;stringtable-output</code></dt>
<dd> write out a NeXTstep/GNUstep .strings file</dd>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>NUMBER</i></dt>
<dd> set output page width</dd>
<dt><code>&#8211;no-wrap</code></dt>
<dd> do not break long message lines, longer than the output page width, into several lines</dd>
<dt><code>-s</code>, <code>&#8211;sort-output</code></dt>
<dd> generate sorted output</dd>
<dt><code>-F</code>, <code>&#8211;sort-by-file</code></dt>
<dd> sort output by file location</dd></dl>
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
<p> The full documentation for <code>msgen</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msgen</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info msgen</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
