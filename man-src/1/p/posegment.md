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
<p> <code>posegment </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [-P|&#8211;pot] [-l|&#8211;language <i>LANG</i>] [&#8211;source-language <i>LANG</i>] [&#8211;keepspaces] [&#8211;only-aligned]</p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/posegment.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/posegment.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in tmx, xlf, po, pot formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in tmx, xlf, po, pot formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>-P/&#8211;pot</dt>
<dd> output PO Templates (.pot) rather than PO files (.po)</dd>
<dt>-l/&#8211;language</dt>
<dd> the target language code</dd>
<dt>&#8211;source-language</dt>
<dd> the source language code (default &#8216;en&#8217;)</dd>
<dt>&#8211;keepspaces</dt>
<dd> Disable automatic stripping of whitespace</dd>
<dt>&#8211;only-aligned</dt>
<dd> Removes units where sentence number does not correspond </dd>
</dl>
