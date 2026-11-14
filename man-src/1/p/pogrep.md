---
title: "pogrep(1)"
name: "pogrep"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pogrep/"
description: "pogrep – Grep XLIFF, Gettext PO and TMX localization files."
---

<h2>NAME</h2>
<p> pogrep &#8211; Grep XLIFF, Gettext PO and TMX localization files.</p>
<h2>SYNOPSIS</h2>
<p> <code>pogrep </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [&#8211;search <i>SEARCHPARTS</i>] [-I|&#8211;ignore-case] [-e|&#8211;regexp] [-v|&#8211;invert-match] [&#8211;accelerator <i>ACCELERATOR</i>] [-k|&#8211;keep-translations]</p>
<h2>DESCRIPTION</h2>
<p> Matches are output to snippet files of the same type which can then be reviewed and later merged using :doc:`pomerge &lt;/commands/pomerge&gt;`. </p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pogrep.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pogrep.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in xliff, mo, xlf, tmx, gmo, pot, xlff, po formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in po, xliff, mo, xlf, tmx, gmo, pot, xlff formats</p>
<dt>&#8211;search</p>
<dd> searches the given parts (source, target, notes and locations)</p>
<dt>-I/&#8211;ignore-case</p>
<dd> ignore case distinctions</p>
<dt>-e/&#8211;regexp</p>
<dd> use regular expression matching</p>
<dt>-v/&#8211;invert-match</p>
<dd> select non-matching lines</p>
<dt>&#8211;accelerator</p>
<dd> ignores the given accelerator when matching</p>
<dt>-k/&#8211;keep-translations</p>
<dd> always extract units with translations </p>
</dl>
<h2>Index</h2>
