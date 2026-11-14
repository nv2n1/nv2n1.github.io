---
title: "po2rc(1)"
name: "po2rc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po2rc/"
description: "po2rc – Convert Gettext PO localization files back to Windows Resource (.rc) files."
---

<h2>NAME</h2>
<p> po2rc &#8211; Convert Gettext PO localization files back to Windows Resource (.rc) files.</p>
<h2>SYNOPSIS</h2>
<p> <code>po2rc </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp] [&#8211;charset <i>CHARSET</i>] [-l|&#8211;lang <i>LANG</i>] [&#8211;sublang <i>SUBLANG</i>] [&#8211;threshold <i>PERCENT</i>] [&#8211;fuzzy] [&#8211;nofuzzy]</p>
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
<dd> read from INPUT in po, pot formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in rc format</p>
<dt>-t/&#8211;template</p>
<dd> read from TEMPLATE in rc format</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>&#8211;charset</p>
<dd> charset to use to decode the RC files (default: utf-8)</p>
<dt>-l/&#8211;lang</p>
<dd> LANG entry</p>
<dt>&#8211;sublang</p>
<dd> SUBLANG entry (default: SUBLANG_DEFAULT)</p>
<dt>&#8211;threshold</p>
<dd> only convert files where the translation completion is above PERCENT</p>
<dt>&#8211;fuzzy</p>
<dd> use translations marked fuzzy</p>
<dt>&#8211;nofuzzy</p>
<dd> don&#8217;t use translations marked fuzzy (default) </p>
</dl>
<h2>Index</h2>
