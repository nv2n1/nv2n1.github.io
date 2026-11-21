---
title: "msgcmp(1)"
name: "msgcmp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgcmp/"
description: "msgcmp – compare message catalog and template"
---

<h2 class="name">NAME</h2>
<p> msgcmp &#8211; compare message catalog and template </p>
<h2>SYNOPSIS</h2>
<p> <code>msgcmp</code> [<i>OPTION</i>] <i>def.po ref.pot</i></p>
<h2>DESCRIPTION</h2>
<p> Compare two Uniforum style .po files to check that both contain the same set of msgid strings. The def.po file is an existing PO file with the translations. The ref.pot file is the last created PO file, or a PO Template file (generally created by xgettext). This is useful for checking that you have translated each and every message in your program. Where an exact match cannot be found, fuzzy matching is used to produce better diagnostics. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt>def.po</dt>
<dd> translations</dd>
<dt>ref.pot</dt>
<dd> references to the sources</dd>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></dt>
<dd> add DIRECTORY to list for input files search</dd></dl>
<h3>Operation modifiers:</h3>
<dl>
<dt><code>-m</code>, <code>&#8211;multi-domain</code></dt>
<dd> apply ref.pot to each of the domains in def.po</dd>
<dt><code>-N</code>, <code>&#8211;no-fuzzy-matching</code></dt>
<dd> do not use fuzzy matching</dd>
<dt><code>&#8211;use-fuzzy</code></dt>
<dd> consider fuzzy entries</dd>
<dt><code>&#8211;use-untranslated</code></dt>
<dd> consider untranslated entries</dd></dl>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></dt>
<dd> input files are in Java .properties syntax</dd>
<dt><code>&#8211;stringtable-input</code></dt>
<dd> input files are in NeXTstep/GNUstep .strings syntax</dd></dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Peter Miller.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnu-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-1998, 2000-2016 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>msgcmp</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msgcmp</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info msgcmp</code></dd></dl>
<p> should give you access to the complete manual. </p>
