---
title: "msgcat(1)"
name: "msgcat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgcat/"
description: "msgcat – combines several message catalogs"
---

<h2 class="name">NAME</h2>
<p> msgcat &#8211; combines several message catalogs </p>
<h2>SYNOPSIS</h2>
<p> <code>msgcat</code> [<i>OPTION</i>] [<i>INPUTFILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Concatenates and merges the specified PO files. Find messages which are common to two or more of the specified PO files. By using the <code>&#8211;more-than</code> option, greater commonality may be requested before messages are printed. Conversely, the <code>&#8211;less-than</code> option may be used to specify less commonality before messages are printed (i.e. <code>&#8211;less-than</code>=<i>2</i> will only print the unique messages). Translations, comments, extracted comments, and file positions will be cumulated, except that if <code>&#8211;use-first</code> is specified, they will be taken from the first PO file to define them. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt>INPUTFILE &#8230;</p>
<dd> input files</p>
<dt><code>-f</code>, <code>&#8211;files-from</code>=<i>FILE</i></p>
<dd> get list of input files from FILE</p>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></p>
<dd> add DIRECTORY to list for input files search</dl>
<p> If input file is -, standard input is read.</p>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> write output to specified file</dl>
<p> The results are written to standard output if no output file is specified or if it is -.</p>
<h3>Message selection:</h3>
<dl>
<dt>-&lt;, <code>&#8211;less-than</code>=<i>NUMBER</i></p>
<dd> print messages with less than this many definitions, defaults to infinite if not set</p>
<dt>-&gt;, <code>&#8211;more-than</code>=<i>NUMBER</i></p>
<dd> print messages with more than this many definitions, defaults to 0 if not set</p>
<dt><code>-u</code>, <code>&#8211;unique</code></p>
<dd> shorthand for <code>&#8211;less-than</code>=<i>2</i>, requests that only unique messages be printed</dl>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></p>
<dd> input files are in Java .properties syntax</p>
<dt><code>&#8211;stringtable-input</code></p>
<dd> input files are in NeXTstep/GNUstep .strings syntax</dl>
<h3>Output details:</h3>
<dl>
<dt><code>-t</code>, <code>&#8211;to-code</code>=<i>NAME</i></p>
<dd> encoding for output</p>
<dt><code>&#8211;use-first</code></p>
<dd> use first available translation for each message, don&#8217;t merge several translations</p>
<dt><code>&#8211;lang</code>=<i>CATALOGNAME</i></p>
<dd> set &#8216;Language&#8217; field in the header entry</p>
<dt><code>&#8211;color</code></p>
<dd> use colors and other text attributes always</p>
<dt><code>&#8211;color</code>=<i>WHEN</i></p>
<dd> use colors and other text attributes if WHEN. WHEN may be &#8216;always&#8217;, &#8216;never&#8217;, &#8216;auto&#8217;, or &#8216;html&#8217;.</p>
<dt><code>&#8211;style</code>=<i>STYLEFILE</i></p>
<dd> specify CSS style rule file for <code>&#8211;color</code></p>
<dt><code>-e</code>, <code>&#8211;no-escape</code></p>
<dd> do not use C escapes in output (default)</p>
<dt><code>-E</code>, <code>&#8211;escape</code></p>
<dd> use C escapes in output, no extended chars</p>
<dt><code>&#8211;force-po</code></p>
<dd> write PO file even if empty</p>
<dt><code>-i</code>, <code>&#8211;indent</code></p>
<dd> write the .po file using indented style</p>
<dt><code>&#8211;no-location</code></p>
<dd> do not write &#8216;#: filename:line&#8217; lines</p>
<dt><code>-n</code>, <code>&#8211;add-location</code></p>
<dd> generate &#8216;#: filename:line&#8217; lines (default)</p>
<dt><code>&#8211;strict</code></p>
<dd> write out strict Uniforum conforming .po file</p>
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
<p> The full documentation for <code>msgcat</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msgcat</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info msgcat</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
