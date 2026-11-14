---
title: "uncrustify(1)"
name: "uncrustify"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uncrustify/"
description: "uncrustify – C, C++, C#, D, Java and Pawn source code beautifier"
---

<h2>NAME</h2>
<p> uncrustify &#8211; C, C++, C#, D, Java and Pawn source code beautifier </p>
<h2>SYNOPSIS</h2>
<p> <code>uncrustify </code>[<i>OPTIONS</i>] [<i>FILES</i>] </p>
<h2>DESCRIPTION</h2>
<p> If no input files are specified, the input is read from stdin.<br />
 If reading from stdin, you should specify the language using -l. </p>
<p> If -F is used or files are specified on the command line, the output filename is <i>PFX</i> + &quot;/&quot; + filename + <i>SFX</i>.<br />
 Unless, of course, the options <code>&#8211;replace</code> or <code>&#8211;no-backup</code> are used. </p>
<p> When reading from stdin or doing a single file via the &#8216;-f&#8217; option, the output is dumped to stdout, unless redirected with -o FILE. </p>
<p> Errors are always dumped to stderr </p>
<h2>OPTIONS</h2>
<h3>Basic Options:</h3>
<dl>
<dt><code>-c</code><i> CFG</p>
<dd> Use the config file CFG</i>.<br />
 If not specified, uncrustify will use <code>$UNCRUSTIFY_CONFIG</code> or <code>$HOME/.uncrustify.cfg</code>.</p>
<dt><code>-f</code><i> FILE</p>
<dd> Process the single file FILE</i>, sending output to stdout or the file specified with <code>-o</code>.</p>
<dt><code>-o</code><i> FILE</p>
<dd> Redirect output to FILE</i>.<br />
 Use with <code>-f</code>, <code>&#8211;update-config</code>, <code>&#8211;update-config-with-doc</code>, <code>&#8211;universalindent</code>.</p>
<dt><code>&#8211;check</code></p>
<dd> Do not output the new text, instead verify that nothing changes when the file(s) are processed. The status of every file is printed to stderr. The exit code is EXIT_SUCCESS if there were no changes, EXIT_FAILURE otherwise.</p>
<dt><code>-F</code><i> FILE</p>
<dd> Read files to process from FILE</i>, one filename per line. If <i>FILE</i> is &#8216;-&#8216; then read filenames from standard input instead of a file.<br />
 You can create this file using something like &#8216;<code>find . -name &quot;*.c&quot; &gt; list.txt</code>&#8216;.<br />
 This cannot be combined with <code>-f</code>.</p>
<dt><code>&#8211;prefix</code><i> PFX</p>
<dd> Prepend PFX</i> to the output filename path.<br />
 This cannot be combined with <code>-f</code>, <code>&#8211;replace</code>, or <code>&#8211;no-backup</code>.</p>
<dt><code>&#8211;suffix</code><i> SFX</p>
<dd> Append SFX</i> to the output filename.<br />
 The default is &#8216;.uncrustify&#8217; if neither <i>SFX</i> or <i>PFX</i> are specified.<br />
 This cannot be combined with <code>-f</code>, <code>&#8211;replace</code>, or <code>&#8211;no-backup</code>.</p>
<dt><code>&#8211;frag</code><i></p>
<dd> Assume the input is a code fragment and the first line is properly indented.</p>
<dt></i><code>&#8211;replace</code></p>
<dd> Replace source files (creates a backup).<br />
 This cannot be combined with <code>-f</code>, <code>&#8211;prefix</code>, or <code>&#8211;suffix</code>.</p>
<dt><code>&#8211;no-backup</code></p>
<dd> Replace files, no backup. Useful if files are under source control<br />
 This cannot be combined with <code>-f</code>, <code>&#8211;prefix</code>, or <code>&#8211;suffix</code>.</p>
<dt><code>&#8211;mtime</code></p>
<dd> Preserve mtime on replaced files.</p>
<dt><code>-l</code></p>
<dd> Language override: C, CPP, D, CS, JAVA, PAWN, VALA, OC, OC+</p>
<dt><code>-t</code></p>
<dd> Load a file with types (usually not needed)</p>
<dt><code>-q</code></p>
<dd> Quiet mode &#8211; no output on stderr (<code>-L</code> will override)</dl>
<h3>Config/Help Options:</h3>
<dl>
<dt><code>-h</code> -? <code>&#8211;help</code> <code>&#8211;usage</code></p>
<dd> Print this message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version and exit</p>
<dt><code>&#8211;show-config</code></p>
<dd> Print out option documentation and exit</p>
<dt><code>&#8211;update-config</code></p>
<dd> Output a new config file.</p>
<dt><code>&#8211;update-config-with-doc</code></p>
<dd> Output a new config file with embedded usage comments.</p>
<dt><code>&#8211;universalindent</code></p>
<dd> Output a config file for Universal Indent GUI.</p>
<dt><code>&#8211;detect</code></p>
<dd> Detects the config from a source file. Use with &#8216;-f FILE&#8217;. Detection is currently fairly limited. </p>
</dl>
<h3>Debug Options:</h3>
<dl>
<dt><code>-p</code><i> FILE</p>
<dd> Dump debug info to a file</p>
<dt></i><code>-L</code><i> SEV</p>
<dd> Set the log severity (see log_levels.h)</p>
<dt></i><code>-s</code></p>
<dd> Show the log severity in the logs</p>
<dt><code>&#8211;decode</code><i> FLAG</p>
<dd> Print FLAG</i> as text and exit </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Read a D file from stdin, output to stdout.</p>
<dd> cat foo.d | uncrustify -q -c my.cfg -l d</p>
<dt>Process a file, output to stdout.</p>
<dd> uncrustify -c my.cfg -d foo.d</p>
<dt>Process a source tree, output to a different tree.</p>
<dd> find src -name &quot;*.[ch]&quot; &gt; files.txt<br />
 uncrustify -c my.cfg -F files.txt &#8211;prefix out</p>
<dt>Process a source tree in-place.</p>
<dd> uncrustify -c my.cfg &#8211;no-backup $(find src -name &quot;*.[ch]&quot;) </p>
</dl>
<h2>NOTES</h2>
<p> Use comments containing &#8216; *INDENT-OFF*&#8217; and &#8216; *INDENT-ON*&#8217; to disable processing of parts of the source file. </p>
<h2>AUTHOR</h2>
<p> Written by Ben Gardner </p>
<h2>REPORTING BUGS</h2>
<p> Use the issue tracker at &lt;<a rel="nofollow" href="http://sourceforge.net/projects/uncrustify">http://sourceforge.net/projects/uncrustify</a>&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006-2014 Ben Gardner<br />
 Copyright (C) 2015, 2016 Guy Maurel </p>
<h2>LICENSE</h2>
<p> GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt; </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
