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
<dd> read from INPUT in nls, rc formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in po, pot formats</dd>
<dt>-t/&#8211;template</dt>
<dd> read from TEMPLATE in nls, rc formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>-P/&#8211;pot</dt>
<dd> output PO Templates (.pot) rather than PO files (.po)</dd>
<dt>&#8211;charset</dt>
<dd> charset to use to decode the RC files (default: cp1252)</dd>
<dt>-l/&#8211;lang</dt>
<dd> LANG entry (default: LANG_ENGLISH)</dd>
<dt>&#8211;sublang</dt>
<dd> SUBLANG entry (default: SUBLANG_DEFAULT)</dd>
<dt>&#8211;duplicates</dt>
<dd> what to do with duplicate strings (identical source text): merge, msgctxt (default: &#8216;msgctxt&#8217;) </dd>
</dl>
