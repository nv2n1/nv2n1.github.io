---
title: "po2tmx(1)"
name: "po2tmx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po2tmx/"
description: "po2tmx – Convert Gettext PO localization files to a TMX (Translation Memory eXchange) file."
---

<h2>NAME</h2>
<p> po2tmx &#8211; Convert Gettext PO localization files to a TMX (Translation Memory eXchange) file.</p>
<h2>SYNOPSIS</h2>
<p> <code>po2tmx </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [-l|&#8211;language <i>LANG</i>] [&#8211;source-language <i>LANG</i>] [&#8211;comments]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/po2tmx.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/po2tmx.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in po, pot formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in tmx format</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>-l/&#8211;language</p>
<dd> set target language code (e.g. af-ZA) [required]</p>
<dt>&#8211;source-language</p>
<dd> set source language code (default: en)</p>
<dt>&#8211;comments</p>
<dd> set default comment import: none, source, type or others (default: none) </p>
</dl>
<h2>Index</h2>
