---
title: "porestructure(1)"
name: "porestructure"
section: "1"
letter: "p"
url: "/docs/linux/man/1-porestructure/"
description: "porestructure – Restructure Gettxt PO files produced by :doc:`poconflicts </commands/poconflicts>` into the original directory tree for merging using :doc:`pomerge </commands/pomerge>`."
---

<h2>NAME</h2>
<p> porestructure &#8211; Restructure Gettxt PO files produced by :doc:`poconflicts &lt;/commands/poconflicts&gt;` into the original directory tree for merging using :doc:`pomerge &lt;/commands/pomerge&gt;`.</p>
<h2>SYNOPSIS</h2>
<p> <code>porestructure </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i></p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pomerge.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pomerge.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in po format</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in po format </dd>
</dl>
