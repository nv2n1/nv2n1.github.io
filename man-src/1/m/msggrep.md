---

title: "msggrep(1)"
name: "msggrep"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msggrep/"
description: "msggrep – pattern matching on message catalog"
---

<p> msggrep &#8211; pattern matching on message catalog </p>
<h2>SYNOPSIS</h2>
<p> <code>msggrep</code> [<i>OPTION</i>] [<i>INPUTFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Extracts all messages of a translation catalog that match a given pattern or belong to some given source files. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt>INPUTFILE</dt>
<dd> input PO file</dd>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></dt>
<dd> add DIRECTORY to list for input files search</dd></dl>
<p> If no input file is given or if it is -, standard input is read.</p>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> write output to specified file</dd></dl>
<p> The results are written to standard output if no output file is specified or if it is -.</p>
<h3>Message selection:</h3>
<dl>
<dt>
</dt><dd> [-N SOURCEFILE]&#8230; [-M DOMAINNAME]&#8230; [-J MSGCTXT-PATTERN] [-K MSGID-PATTERN] [-T MSGSTR-PATTERN] [-C COMMENT-PATTERN] [-X EXTRACTED-COMMENT-PATTERN]</dd></dl>
<p> A message is selected if it comes from one of the specified source files, or if it comes from one of the specified domains, or if <code>-J</code> is given and its context (msgctxt) matches MSGCTXT-PATTERN, or if <code>-K</code> is given and its key (msgid or msgid_plural) matches MSGID-PATTERN, or if <code>-T</code> is given and its translation (msgstr) matches MSGSTR-PATTERN, or if <code>-C</code> is given and the translator&#8217;s comment matches COMMENT-PATTERN, or if <code>-X</code> is given and the extracted comment matches EXTRACTED-COMMENT-PATTERN. </p>
<p> When more than one selection criterion is specified, the set of selected messages is the union of the selected messages of each criterion. </p>
<p> MSGCTXT-PATTERN or MSGID-PATTERN or MSGSTR-PATTERN or COMMENT-PATTERN or EXTRACTED-COMMENT-PATTERN syntax:</p>
<dl>
<dt>
</dt><dd> [-E | <code>-F]</code> [-e PATTERN | <code>-f</code> FILE]&#8230;</dd></dl>
<p> PATTERNs are basic regular expressions by default, or extended regular expressions if <code>-E</code> is given, or fixed strings if <code>-F</code> is given.</p>
<dl>
<dt><code>-N</code>, <code>&#8211;location</code>=<i>SOURCEFILE</i></dt>
<dd> select messages extracted from SOURCEFILE</dd>
<dt><code>-M</code>, <code>&#8211;domain</code>=<i>DOMAINNAME</i></dt>
<dd> select messages belonging to domain DOMAINNAME</dd>
<dt><code>-J</code>, <code>&#8211;msgctxt</code></dt>
<dd> start of patterns for the msgctxt</dd>
<dt><code>-K</code>, <code>&#8211;msgid</code></dt>
<dd> start of patterns for the msgid</dd>
<dt><code>-T</code>, <code>&#8211;msgstr</code></dt>
<dd> start of patterns for the msgstr</dd>
<dt><code>-C</code>, <code>&#8211;comment</code></dt>
<dd> start of patterns for the translator&#8217;s comment</dd>
<dt><code>-X</code>, <code>&#8211;extracted-comment</code></dt>
<dd> start of patterns for the extracted comment</dd>
<dt><code>-E</code>, <code>&#8211;extended-regexp</code></dt>
<dd> PATTERN is an extended regular expression</dd>
<dt><code>-F</code>, <code>&#8211;fixed-strings</code></dt>
<dd> PATTERN is a set of newline-separated strings</dd>
<dt><code>-e</code>, <code>&#8211;regexp</code>=<i>PATTERN</i></dt>
<dd> use PATTERN as a regular expression</dd>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>FILE</i></dt>
<dd> obtain PATTERN from FILE</dd>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></dt>
<dd> ignore case distinctions</dd>
<dt><code>-v</code>, <code>&#8211;invert-match</code></dt>
<dd> output only the messages that do not match any selection criterion</dd></dl>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></dt>
<dd> input file is in Java .properties syntax</dd>
<dt><code>&#8211;stringtable-input</code></dt>
<dd> input file is in NeXTstep/GNUstep .strings syntax</dd></dl>
<h3>Output details:</h3>
<dl>
<dt><code>&#8211;color</code></dt>
<dd> use colors and other text attributes always</dd>
<dt><code>&#8211;color</code>=<i>WHEN</i></dt>
<dd> use colors and other text attributes if WHEN. WHEN may be &#8216;always&#8217;, &#8216;never&#8217;, &#8216;auto&#8217;, or &#8216;html&#8217;.</dd>
<dt><code>&#8211;style</code>=<i>STYLEFILE</i></dt>
<dd> specify CSS style rule file for <code>&#8211;color</code></dd>
<dt><code>&#8211;no-escape</code></dt>
<dd> do not use C escapes in output (default)</dd>
<dt><code>&#8211;escape</code></dt>
<dd> use C escapes in output, no extended chars</dd>
<dt><code>&#8211;force-po</code></dt>
<dd> write PO file even if empty</dd>
<dt><code>&#8211;indent</code></dt>
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
<dt><code>&#8211;sort-output</code></dt>
<dd> generate sorted output</dd>
<dt><code>&#8211;sort-by-file</code></dt>
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
<p> The full documentation for <code>msggrep</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msggrep</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info msggrep</code></dd></dl>
<p> should give you access to the complete manual. </p>
