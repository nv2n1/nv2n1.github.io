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
<dt>&#8211;version</dt>
<dd> show program&#8217;s version number and exit</dd>
<dt>-h/&#8211;help</dt>
<dd> show this help message and exit</dd>
<dt>&#8211;manpage</dt>
<dd> output a manpage based on the help</dd>
<dt>&#8211;progress</dt>
<dd> show progress as: dots, none, bar, names, verbose</dd>
<dt>&#8211;errorlevel</dt>
<dd> show errorlevel as: none, message, exception, traceback</dd>
<dt>-i/&#8211;input</dt>
<dd> read from INPUT in oo, sdf formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in po, pot formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>-P/&#8211;pot</dt>
<dd> output PO Templates (.pot) rather than PO files (.po)</dd>
<dt>-l/&#8211;language</dt>
<dd> set target language to extract from oo file (e.g. af-ZA)</dd>
<dt>&#8211;source-language</dt>
<dd> set source language code (default en-US)</dd>
<dt>&#8211;nonrecursiveinput</dt>
<dd> don&#8217;t treat the input oo as a recursive store</dd>
<dt>&#8211;duplicates</dt>
<dd> what to do with duplicate strings (identical source text): merge, msgctxt (default: &#8216;msgctxt&#8217;)</dd>
<dt>&#8211;multifile</dt>
<dd> how to split po/pot files (single, toplevel or onefile) </dd>
</dl>
