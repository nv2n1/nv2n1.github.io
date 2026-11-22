---

title: "msgmerge(1)"
name: "msgmerge"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgmerge/"
description: "msgmerge – merge message catalog and template"
---

<p> msgmerge &#8211; merge message catalog and template </p>
<h2>SYNOPSIS</h2>
<p> <code>msgmerge</code> [<i>OPTION</i>] <i>def.po ref.pot</i></p>
<h2>DESCRIPTION</h2>
<p> Merges two Uniforum style .po files together. The def.po file is an existing PO file with translations which will be taken over to the newly created file as long as they still match; comments will be preserved, but extracted comments and file positions will be discarded. The ref.pot file is the last created PO file with up-to-date source references but old translations, or a PO Template file (generally created by xgettext); any translations or comments in the file will be discarded, however dot comments and file positions will be preserved. Where an exact match cannot be found, fuzzy matching is used to produce better results. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt>def.po</dt>
<dd> translations referring to old sources</dd>
<dt>ref.pot</dt>
<dd> references to new sources</dd>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></dt>
<dd> add DIRECTORY to list for input files search</dd>
<dt><code>-C</code>, <code>&#8211;compendium</code>=<i>FILE</i></dt>
<dd> additional library of message translations, may be specified more than once</dd></dl>
<h3>Operation mode:</h3>
<dl>
<dt><code>-U</code>, <code>&#8211;update</code></dt>
<dd> update def.po, do nothing if def.po already up to date</dd></dl>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> write output to specified file</dd></dl>
<p> The results are written to standard output if no output file is specified or if it is -. </p>
<p> Output file location in update mode: The result is written back to def.po.</p>
<dl>
<dt><code>&#8211;backup</code>=<i>CONTROL</i></dt>
<dd> make a backup of def.po</dd>
<dt><code>&#8211;suffix</code>=<i>SUFFIX</i></dt>
<dd> override the usual backup suffix</dd></dl>
<p> The version control method may be selected via the <code>&#8211;backup</code> option or through the VERSION_CONTROL environment variable. Here are the values:</p>
<dl>
<dt>none, off</dt>
<dd> never make backups (even if <code>&#8211;backup</code> is given)</dd>
<dt>numbered, t</dt>
<dd> make numbered backups</dd>
<dt>existing, nil</dt>
<dd> numbered if numbered backups exist, simple otherwise</dd>
<dt>simple, never</dt>
<dd> always make simple backups</dd></dl>
<p> The backup suffix is &#8216;~&#8217;, unless set with <code>&#8211;suffix</code> or the SIMPLE_BACKUP_SUFFIX environment variable.</p>
<h3>Operation modifiers:</h3>
<dl>
<dt><code>-m</code>, <code>&#8211;multi-domain</code></dt>
<dd> apply ref.pot to each of the domains in def.po</dd>
<dt><code>-N</code>, <code>&#8211;no-fuzzy-matching</code></dt>
<dd> do not use fuzzy matching</dd>
<dt><code>&#8211;previous</code></dt>
<dd> keep previous msgids of translated messages</dd></dl>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></dt>
<dd> input files are in Java .properties syntax</dd>
<dt><code>&#8211;stringtable-input</code></dt>
<dd> input files are in NeXTstep/GNUstep .strings syntax</dd></dl>
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
<dd> output version information and exit</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> increase verbosity level</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></dt>
<dd> suppress progress indicators</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Peter Miller.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnu-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-1998, 2000-2016 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>msgmerge</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msgmerge</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info msgmerge</code></dd></dl>
<p> should give you access to the complete manual. </p>
