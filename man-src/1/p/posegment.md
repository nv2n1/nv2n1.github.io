---
title: "posegment(1)"
name: "posegment"
section: "1"
letter: "p"
url: "/docs/linux/man/1-posegment/"
description: "posegment – Segment Gettext PO, XLIFF and TMX localization files at the sentence level."
---

<h2>NAME</h2>
<p> posegment &#8211; Segment Gettext PO, XLIFF and TMX localization files at the sentence level.</p>
<h2>SYNOPSIS</h2>
<p> <code>posegment </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [-P|&#8211;pot] [-l|&#8211;language <i>LANG</i>] [&#8211;source-language <i>LANG</i>] [&#8211;keepspaces] [&#8211;only-aligned]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/posegment.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/posegment.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in tmx, xlf, po, pot formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in tmx, xlf, po, pot formats</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>-P/&#8211;pot</p>
<dd> output PO Templates (.pot) rather than PO files (.po)</p>
<dt>-l/&#8211;language</p>
<dd> the target language code</p>
<dt>&#8211;source-language</p>
<dd> the source language code (default &#8216;en&#8217;)</p>
<dt>&#8211;keepspaces</p>
<dd> Disable automatic stripping of whitespace</p>
<dt>&#8211;only-aligned</p>
<dd> Removes units where sentence number does not correspond </p>
</dl>
<h2>Index</h2>
