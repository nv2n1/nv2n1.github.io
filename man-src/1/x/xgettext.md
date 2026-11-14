---
title: "xgettext(1)"
name: "xgettext"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xgettext/"
description: "xgettext – extract gettext strings from source"
---

<h2 class="name">NAME</h2>
<p> xgettext &#8211; extract gettext strings from source </p>
<h2>SYNOPSIS</h2>
<p> <code>xgettext</code> [<i>OPTION</i>] [<i>INPUTFILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Extract translatable strings from given input files. </p>
<p> Mandatory arguments to long options are mandatory for short options too. Similarly for optional arguments.</p>
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
<dt><code>-d</code>, <code>&#8211;default-domain</code>=<i>NAME</i></p>
<dd> use NAME.po for output (instead of messages.po)</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> write output to specified file</p>
<dt><code>-p</code>, <code>&#8211;output-dir</code>=<i>DIR</i></p>
<dd> output files will be placed in directory DIR</dl>
<p> If output file is -, output is written to standard output.</p>
<h3>Choice of input file language:</h3>
<dl>
<dt><code>-L</code>, <code>&#8211;language</code>=<i>NAME</i></p>
<dd> recognise the specified language (C, C++, ObjectiveC, PO, Shell, Python, Lisp, EmacsLisp, librep, Scheme, Smalltalk, Java, JavaProperties, C#, awk, YCP, Tcl, Perl, PHP, GCC-source, NXStringTable, RST, Glade, Lua, JavaScript, Vala, Desktop)</p>
<dt><code>-C</code>, <code>&#8211;c</code>++</p>
<dd> shorthand for <code>&#8211;language</code>=<i>C</i>++</dl>
<p> By default the language is guessed depending on the input file name extension.</p>
<h3>Input file interpretation:</h3>
<dl>
<dt><code>&#8211;from-code</code>=<i>NAME</i></p>
<dd> encoding of input files (except for Python, Tcl, Glade)</dl>
<p> By default the input files are assumed to be in ASCII.</p>
<h3>Operation mode:</h3>
<dl>
<dt><code>-j</code>, <code>&#8211;join-existing</code></p>
<dd> join messages with existing file</p>
<dt><code>-x</code>, <code>&#8211;exclude-file</code>=<i>FILE</i>.po</p>
<dd> entries from FILE.po are not extracted</p>
<dt><code>-cTAG</code>, <code>&#8211;add-comments</code>=<i>TAG</i></p>
<dd> place comment blocks starting with TAG and preceding keyword lines in output file</p>
<dt><code>-c</code>, <code>&#8211;add-comments</code></p>
<dd> place all comment blocks preceding keyword lines in output file</p>
<dt><code>&#8211;check</code>=<i>NAME</i></p>
<dd> perform syntax check on messages (ellipsis-unicode, space-ellipsis,</p>
<dt>
<dd> quote-unicode, bullet-unicode)</p>
<dt><code>&#8211;sentence-end</code>=<i>TYPE</i></p>
<dd> type describing the end of sentence (single-space, which is the default,</p>
<dt>
<dd> or double-space)</dl>
<h3>Language specific options:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;extract-all</code></p>
<dd> extract all strings (only languages C, C++, ObjectiveC, Shell, Python, Lisp, EmacsLisp, librep, Scheme, Java, C#, awk, Tcl, Perl, PHP, GCC-source, Glade, Lua, JavaScript, Vala)</p>
<dt><code>-kWORD</code>, <code>&#8211;keyword</code>=<i>WORD</i></p>
<dd> look for WORD as an additional keyword</p>
<dt><code>-k</code>, <code>&#8211;keyword</code></p>
<dd> do not to use default keywords (only languages C, C++, ObjectiveC, Shell, Python, Lisp, EmacsLisp, librep, Scheme, Java, C#, awk, Tcl, Perl, PHP, GCC-source, Glade, Lua, JavaScript, Vala, Desktop)</p>
<dt><code>&#8211;flag</code>=<i>WORD</i>:ARG:FLAG</p>
<dd> additional flag for strings inside the argument number ARG of keyword WORD</p>
<dt>
<dd> (only languages C, C++, ObjectiveC, Shell, Python, Lisp, EmacsLisp, librep, Scheme, Java, C#, awk, YCP, Tcl, Perl, PHP, GCC-source, Lua, JavaScript, Vala)</p>
<dt><code>-T</code>, <code>&#8211;trigraphs</code></p>
<dd> understand ANSI C trigraphs for input (only languages C, C++, ObjectiveC)</p>
<dt><code>&#8211;its</code>=<i>FILE</i></p>
<dd> apply ITS rules from FILE (only XML based languages)</p>
<dt><code>&#8211;qt</code></p>
<dd> recognize Qt format strings (only language C++)</p>
<dt><code>&#8211;kde</code></p>
<dd> recognize KDE 4 format strings (only language C++)</p>
<dt><code>&#8211;boost</code></p>
<dd> recognize Boost format strings (only language C++)</p>
<dt><code>&#8211;debug</code></p>
<dd> more detailed formatstring recognition result</dl>
<h3>Output details:</h3>
<dl>
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
<dt><code>&#8211;properties-output</code></p>
<dd> write out a Java .properties file</p>
<dt><code>&#8211;stringtable-output</code></p>
<dd> write out a NeXTstep/GNUstep .strings file</p>
<dt><code>&#8211;itstool</code></p>
<dd> write out itstool comments</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>NUMBER</i></p>
<dd> set output page width</p>
<dt><code>&#8211;no-wrap</code></p>
<dd> do not break long message lines, longer than the output page width, into several lines</p>
<dt><code>-s</code>, <code>&#8211;sort-output</code></p>
<dd> generate sorted output</p>
<dt><code>-F</code>, <code>&#8211;sort-by-file</code></p>
<dd> sort output by file location</p>
<dt><code>&#8211;omit-header</code></p>
<dd> don&#8217;t write header with &#8216;msgid &quot;&quot;&#8217; entry</p>
<dt><code>&#8211;copyright-holder</code>=<i>STRING</i></p>
<dd> set copyright holder in output</p>
<dt><code>&#8211;foreign-user</code></p>
<dd> omit FSF copyright in output for foreign user</p>
<dt><code>&#8211;package-name</code>=<i>PACKAGE</i></p>
<dd> set package name in output</p>
<dt><code>&#8211;package-version</code>=<i>VERSION</i></p>
<dd> set package version in output</p>
<dt><code>&#8211;msgid-bugs-address</code>=<i>EMAIL</i>@ADDRESS</p>
<dd> set report address for msgid bugs</p>
<dt><code>-m[STRING]</code>, <code>&#8211;msgstr-prefix</code>[=<i>STRING</i>]</p>
<dd> use STRING or &quot;&quot; as prefix for msgstr values</p>
<dt><code>-M[STRING]</code>, <code>&#8211;msgstr-suffix</code>[=<i>STRING</i>]</p>
<dd> use STRING or &quot;&quot; as suffix for msgstr values</dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Ulrich Drepper.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnu-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-1998, 2000-2016 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>xgettext</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>xgettext</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info xgettext</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
