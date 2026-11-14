---
title: "csv2tbx(1)"
name: "csv2tbx"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csv2tbx/"
description: "csv2tbx – Convert Comma-Separated Value (.csv) files to a TermBase eXchange (.tbx) glossary file"
---

<h2>NAME</h2>
<p> csv2tbx &#8211; Convert Comma-Separated Value (.csv) files to a TermBase eXchange (.tbx) glossary file</p>
<h2>SYNOPSIS</h2>
<p> <code>csv2tbx </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [&#8211;charset <i>CHARSET</i>] [&#8211;columnorder]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/csv2tbx.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/csv2tbx.html</a> for examples and usage instructions</p>
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
<dd> read from INPUT in csv format</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in tbx format</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>&#8211;charset</p>
<dd> set charset to decode from csv files</p>
<dt>&#8211;columnorder</p>
<dd> specify the order and position of columns (comment,source,target) </p>
</dl>
<h2>Index</h2>
