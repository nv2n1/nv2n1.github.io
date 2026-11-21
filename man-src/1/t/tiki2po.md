---

title: "tiki2po(1)"
name: "tiki2po"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiki2po/"
description: "tiki2po – Convert TikiWiki’s language.php files to GetText PO files."
---

<h2>NAME</h2>
<p> tiki2po &#8211; Convert TikiWiki&#8217;s language.php files to GetText PO files.</p>
<p> <code>tiki2po </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [&#8211;include-unused]</p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/tiki2po.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/tiki2po.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in php format</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in po, pot formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>&#8211;include-unused</dt>
<dd> Include strings in the unused section </dd>
</dl>
