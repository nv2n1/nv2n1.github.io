---
title: "oo2po(1)"
name: "oo2po"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oo2po/"
description: "oo2po – Convert an OpenOffice.org (SDF) localization file to Gettext PO localization files."
---

<h2>NAME</h2>
<p> oo2po &#8211; Convert an OpenOffice.org (SDF) localization file to Gettext PO localization files.</p>
<h2>SYNOPSIS</h2>
<p> <code>oo2po </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [-P|&#8211;pot] [-l|&#8211;language <i>LANG</i>] [&#8211;source-language <i>LANG</i>] [&#8211;nonrecursiveinput] [&#8211;duplicates <i>DUPLICATESTYLE</i>] [&#8211;multifile <i>MULTIFILESTYLE</i>]</p>
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
<dd> read from INPUT in oo, sdf formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in po, pot formats</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>-P/&#8211;pot</p>
<dd> output PO Templates (.pot) rather than PO files (.po)</p>
<dt>-l/&#8211;language</p>
<dd> set target language to extract from oo file (e.g. af-ZA)</p>
<dt>&#8211;source-language</p>
<dd> set source language code (default en-US)</p>
<dt>&#8211;nonrecursiveinput</p>
<dd> don&#8217;t treat the input oo as a recursive store</p>
<dt>&#8211;duplicates</p>
<dd> what to do with duplicate strings (identical source text): merge, msgctxt (default: &#8216;msgctxt&#8217;)</p>
<dt>&#8211;multifile</p>
<dd> how to split po/pot files (single, toplevel or onefile) </p>
</dl>
<h2>Index</h2>
