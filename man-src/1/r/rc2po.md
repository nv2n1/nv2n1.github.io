---
title: "rc2po(1)"
name: "rc2po"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rc2po/"
description: "rc2po – Convert Windows RC files to Gettext PO localization files."
---

<h2>NAME</h2>
<p> rc2po &#8211; Convert Windows RC files to Gettext PO localization files.</p>
<h2>SYNOPSIS</h2>
<p> <code>rc2po </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp] [-P|&#8211;pot] [&#8211;charset <i>CHARSET</i>] [-l|&#8211;lang <i>LANG</i>] [&#8211;sublang <i>SUBLANG</i>] [&#8211;duplicates <i>DUPLICATESTYLE</i>]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/rc2po.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/rc2po.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in nls, rc formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in po, pot formats</p>
<dt>-t/&#8211;template</p>
<dd> read from TEMPLATE in nls, rc formats</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>-P/&#8211;pot</p>
<dd> output PO Templates (.pot) rather than PO files (.po)</p>
<dt>&#8211;charset</p>
<dd> charset to use to decode the RC files (default: cp1252)</p>
<dt>-l/&#8211;lang</p>
<dd> LANG entry (default: LANG_ENGLISH)</p>
<dt>&#8211;sublang</p>
<dd> SUBLANG entry (default: SUBLANG_DEFAULT)</p>
<dt>&#8211;duplicates</p>
<dd> what to do with duplicate strings (identical source text): merge, msgctxt (default: &#8216;msgctxt&#8217;) </p>
</dl>
<h2>Index</h2>
