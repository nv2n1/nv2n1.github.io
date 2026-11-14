---
title: "pomerge(1)"
name: "pomerge"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pomerge/"
description: "pomerge – Merges XLIFF and Gettext PO localization files."
---

<h2>NAME</h2>
<p> pomerge &#8211; Merges XLIFF and Gettext PO localization files.</p>
<h2>SYNOPSIS</h2>
<p> <code>pomerge </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp] [&#8211;mergeblanks] [&#8211;mergefuzzy] [&#8211;mergecomments]</p>
<h2>DESCRIPTION</h2>
<p> Snippet file produced by e.g. :doc:`pogrep &lt;/commands/pogrep&gt;` and updated by a translator can be merged back into the original files. </p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pomerge.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pomerge.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in xlf, po, pot, pot formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in po, pot, pot, xlf formats</p>
<dt>-t/&#8211;template</p>
<dd> read from TEMPLATE in pot, po, pot, xlf formats</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>&#8211;mergeblanks</p>
<dd> whether to overwrite existing translations with blank translations (yes/no). Default is yes.</p>
<dt>&#8211;mergefuzzy</p>
<dd> whether to consider fuzzy translations from input (yes/no). Default is yes.</p>
<dt>&#8211;mergecomments</p>
<dd> whether to merge comments as well as translations (yes/no). Default is yes. </p>
</dl>
<h2>Index</h2>
