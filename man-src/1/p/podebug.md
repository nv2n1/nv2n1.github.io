---

title: "podebug(1)"
name: "podebug"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podebug/"
description: "podebug – Insert debug messages into XLIFF and Gettext PO localization files."
---

<p> podebug &#8211; Insert debug messages into XLIFF and Gettext PO localization files.</p>
<h2>SYNOPSIS</h2>
<p> <code>podebug </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [-f|&#8211;format] [&#8211;rewrite <i>STYLE</i>] [&#8211;ignore <i>APPLICATION</i>]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/podebug.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/podebug.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in tmx, xlf, pot, po, pot formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in tmx, xlf, po, pot formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>-f/&#8211;format</dt>
<dd> specify format string</dd>
<dt>&#8211;rewrite</dt>
<dd> the translation rewrite style: blank, bracket, chef, en, flipped, unicode, xxx</dd>
<dt>&#8211;ignore</dt>
<dd> apply tagging ignore rules for the given application: gtk, kde, mozilla, openoffice </dd>
</dl>
