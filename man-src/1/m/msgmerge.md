---
title: "msgmerge(1)"
name: "msgmerge"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgmerge/"
description: "msgmerge – merge message catalog and template"
---

<h2 class="name">NAME</h2>
<p> msgmerge &#8211; merge message catalog and template </p>
<h2>SYNOPSIS</h2>
<p> <code>msgmerge</code> [<i>OPTION</i>] <i>def.po ref.pot</i></p>
<h2>DESCRIPTION</h2>
<p> Merges two Uniforum style .po files together. The def.po file is an existing PO file with translations which will be taken over to the newly created file as long as they still match; comments will be preserved, but extracted comments and file positions will be discarded. The ref.pot file is the last created PO file with up-to-date source references but old translations, or a PO Template file (generally created by xgettext); any translations or comments in the file will be discarded, however dot comments and file positions will be preserved. Where an exact match cannot be found, fuzzy matching is used to produce better results. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt>def.po</p>
<dd> translations referring to old sources</p>
<dt>ref.pot</p>
<dd> references to new sources</p>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></p>
<dd> add DIRECTORY to list for input files search</p>
<dt><code>-C</code>, <code>&#8211;compendium</code>=<i>FILE</i></p>
<dd> additional library of message translations, may be specified more than once</dl>
<h3>Operation mode:</h3>
<dl>
<dt><code>-U</code>, <code>&#8211;update</code></p>
<dd> update def.po, do nothing if def.po already up to date</dl>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> write output to specified file</dl>
<p> The results are written to standard output if no output file is specified or if it is -. </p>
<p> Output file location in update mode: The result is written back to def.po.</p>
<dl>
<dt><code>&#8211;backup</code>=<i>CONTROL</i></p>
<dd> make a backup of def.po</p>
<dt><code>&#8211;suffix</code>=<i>SUFFIX</i></p>
<dd> override the usual backup suffix</dl>
<p> The version control method may be selected via the <code>&#8211;backup</code> option or through the VERSION_CONTROL environment variable. Here are the values:</p>
<dl>
<dt>none, off</p>
<dd> never make backups (even if <code>&#8211;backup</code> is given)</p>
<dt>numbered, t</p>
<dd> make numbered backups</p>
<dt>existing, nil</p>
<dd> numbered if numbered backups exist, simple otherwise</p>
<dt>simple, never</p>
<dd> always make simple backups</dl>
<p> The backup suffix is &#8216;~&#8217;, unless set with <code>&#8211;suffix</code> or the SIMPLE_BACKUP_SUFFIX environment variable.</p>
<h3>Operation modifiers:</h3>
<dl>
<dt><code>-m</code>, <code>&#8211;multi-domain</code></p>
<dd> apply ref.pot to each of the domains in def.po</p>
<dt><code>-N</code>, <code>&#8211;no-fuzzy-matching</code></p>
<dd> do not use fuzzy matching</p>
<dt><code>&#8211;previous</code></p>
<dd> keep previous msgids of translated messages</dl>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></p>
<dd> input files are in Java .properties syntax</p>
<dt><code>&#8211;stringtable-input</code></p>
<dd> input files are in NeXTstep/GNUstep .strings syntax</dl>
<h3>Output details:</h3>
<dl>
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
<dt><code>-s</code>, <code>&#8211;sort-output</code></p>
<dd> generate sorted output</p>
<dt><code>-F</code>, <code>&#8211;sort-by-file</code></p>
<dd> sort output by file location</dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> increase verbosity level</p>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> suppress progress indicators</dl>
<h2>AUTHOR</h2>
<p> Written by Peter Miller.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnu-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-1998, 2000-2016 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>msgmerge</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msgmerge</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info msgmerge</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
