---
title: "msggrep(1)"
name: "msggrep"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msggrep/"
description: "msggrep – pattern matching on message catalog"
---

<h2 class="name">NAME</h2>
<p> msggrep &#8211; pattern matching on message catalog </p>
<h2>SYNOPSIS</h2>
<p> <code>msggrep</code> [<i>OPTION</i>] [<i>INPUTFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Extracts all messages of a translation catalog that match a given pattern or belong to some given source files. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt>INPUTFILE</p>
<dd> input PO file</p>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></p>
<dd> add DIRECTORY to list for input files search</dl>
<p> If no input file is given or if it is -, standard input is read.</p>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> write output to specified file</dl>
<p> The results are written to standard output if no output file is specified or if it is -.</p>
<h3>Message selection:</h3>
<dl>
<dt>
<dd> [-N SOURCEFILE]&#8230; [-M DOMAINNAME]&#8230; [-J MSGCTXT-PATTERN] [-K MSGID-PATTERN] [-T MSGSTR-PATTERN] [-C COMMENT-PATTERN] [-X EXTRACTED-COMMENT-PATTERN]</dl>
<p> A message is selected if it comes from one of the specified source files, or if it comes from one of the specified domains, or if <code>-J</code> is given and its context (msgctxt) matches MSGCTXT-PATTERN, or if <code>-K</code> is given and its key (msgid or msgid_plural) matches MSGID-PATTERN, or if <code>-T</code> is given and its translation (msgstr) matches MSGSTR-PATTERN, or if <code>-C</code> is given and the translator&#8217;s comment matches COMMENT-PATTERN, or if <code>-X</code> is given and the extracted comment matches EXTRACTED-COMMENT-PATTERN. </p>
<p> When more than one selection criterion is specified, the set of selected messages is the union of the selected messages of each criterion. </p>
<p> MSGCTXT-PATTERN or MSGID-PATTERN or MSGSTR-PATTERN or COMMENT-PATTERN or EXTRACTED-COMMENT-PATTERN syntax:</p>
<dl>
<dt>
<dd> [-E | <code>-F]</code> [-e PATTERN | <code>-f</code> FILE]&#8230;</dl>
<p> PATTERNs are basic regular expressions by default, or extended regular expressions if <code>-E</code> is given, or fixed strings if <code>-F</code> is given.</p>
<dl>
<dt><code>-N</code>, <code>&#8211;location</code>=<i>SOURCEFILE</i></p>
<dd> select messages extracted from SOURCEFILE</p>
<dt><code>-M</code>, <code>&#8211;domain</code>=<i>DOMAINNAME</i></p>
<dd> select messages belonging to domain DOMAINNAME</p>
<dt><code>-J</code>, <code>&#8211;msgctxt</code></p>
<dd> start of patterns for the msgctxt</p>
<dt><code>-K</code>, <code>&#8211;msgid</code></p>
<dd> start of patterns for the msgid</p>
<dt><code>-T</code>, <code>&#8211;msgstr</code></p>
<dd> start of patterns for the msgstr</p>
<dt><code>-C</code>, <code>&#8211;comment</code></p>
<dd> start of patterns for the translator&#8217;s comment</p>
<dt><code>-X</code>, <code>&#8211;extracted-comment</code></p>
<dd> start of patterns for the extracted comment</p>
<dt><code>-E</code>, <code>&#8211;extended-regexp</code></p>
<dd> PATTERN is an extended regular expression</p>
<dt><code>-F</code>, <code>&#8211;fixed-strings</code></p>
<dd> PATTERN is a set of newline-separated strings</p>
<dt><code>-e</code>, <code>&#8211;regexp</code>=<i>PATTERN</i></p>
<dd> use PATTERN as a regular expression</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>FILE</i></p>
<dd> obtain PATTERN from FILE</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> ignore case distinctions</p>
<dt><code>-v</code>, <code>&#8211;invert-match</code></p>
<dd> output only the messages that do not match any selection criterion</dl>
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
<dt><code>&#8211;escape</code></p>
<dd> use C escapes in output, no extended chars</p>
<dt><code>&#8211;force-po</code></p>
<dd> write PO file even if empty</p>
<dt><code>&#8211;indent</code></p>
<dd> indented output style</p>
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
<dt><code>&#8211;sort-output</code></p>
<dd> generate sorted output</p>
<dt><code>&#8211;sort-by-file</code></p>
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
<p> The full documentation for <code>msggrep</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msggrep</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info msggrep</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
