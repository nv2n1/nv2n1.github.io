---
title: "podebug(1)"
name: "podebug"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podebug/"
description: "podebug – Insert debug messages into XLIFF and Gettext PO localization files."
---

<h2>NAME</h2>
<p> podebug &#8211; Insert debug messages into XLIFF and Gettext PO localization files.</p>
<h2>SYNOPSIS</h2>
<p> <code>podebug </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [-f|&#8211;format] [&#8211;rewrite <i>STYLE</i>] [&#8211;ignore <i>APPLICATION</i>]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/podebug.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/podebug.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in tmx, xlf, pot, po, pot formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in tmx, xlf, po, pot formats</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>-f/&#8211;format</p>
<dd> specify format string</p>
<dt>&#8211;rewrite</p>
<dd> the translation rewrite style: blank, bracket, chef, en, flipped, unicode, xxx</p>
<dt>&#8211;ignore</p>
<dd> apply tagging ignore rules for the given application: gtk, kde, mozilla, openoffice </p>
</dl>
<h2>Index</h2>
