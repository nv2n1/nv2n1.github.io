---
title: "po2oo(1)"
name: "po2oo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po2oo/"
description: "po2oo – Convert Gettext PO localization files to an OpenOffice.org (SDF) localization file."
---

<h2>NAME</h2>
<p> po2oo &#8211; Convert Gettext PO localization files to an OpenOffice.org (SDF) localization file.</p>
<h2>SYNOPSIS</h2>
<p> <code>po2oo </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp] [-l|&#8211;language <i>LANG</i>] [&#8211;source-language <i>LANG</i>] [-T|&#8211;keeptimestamp] [&#8211;nonrecursiveoutput] [&#8211;nonrecursivetemplate] [&#8211;skipsource] [&#8211;filteraction <i>ACTION</i>] [&#8211;threshold <i>PERCENT</i>] [&#8211;fuzzy] [&#8211;nofuzzy] [&#8211;multifile <i>MULTIFILESTYLE</i>]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/oo2po.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/oo2po.html</a> for examples and usage instructions.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> show program&#8217;s version number and exit</p>
<dt>-h/&#8211;help</p>
<dd> show this help message and exit</p>
<dt>&#8211;manpage</p>
<dd> output a manpage based on the help</p>
<dt>&#8211;progress</p>
<dd> show progress as: dots, none, bar, names, verbose</p>
<dt>&#8211;errorlevel</p>
<dd> show errorlevel as: none, message, exception, traceback</p>
<dt>-i/&#8211;input</p>
<dd> read from INPUT in xlf, po, pot formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in oo, sdf formats</p>
<dt>-t/&#8211;template</p>
<dd> read from TEMPLATE in oo, sdf formats</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>-l/&#8211;language</p>
<dd> set target language code (e.g. af-ZA) [required]</p>
<dt>&#8211;source-language</p>
<dd> set source language code (default en-US)</p>
<dt>-T/&#8211;keeptimestamp</p>
<dd> don&#8217;t change the timestamps of the strings</p>
<dt>&#8211;nonrecursiveoutput</p>
<dd> don&#8217;t treat the output oo as a recursive store</p>
<dt>&#8211;nonrecursivetemplate</p>
<dd> don&#8217;t treat the template oo as a recursive store</p>
<dt>&#8211;skipsource</p>
<dd> don&#8217;t output the source language, but fallback to it where needed</p>
<dt>&#8211;filteraction</p>
<dd> action on pofilter failure: none (default), warn, exclude-serious, exclude-all</p>
<dt>&#8211;threshold</p>
<dd> only convert files where the translation completion is above PERCENT</p>
<dt>&#8211;fuzzy</p>
<dd> use translations marked fuzzy</p>
<dt>&#8211;nofuzzy</p>
<dd> don&#8217;t use translations marked fuzzy (default)</p>
<dt>&#8211;multifile</p>
<dd> how to split po/pot files (single, toplevel or onefile) </p>
</dl>
<h2>Index</h2>
