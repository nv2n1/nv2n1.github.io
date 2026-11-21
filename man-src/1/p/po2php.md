---

title: "po2php(1)"
name: "po2php"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po2php/"
description: "po2php – Convert Gettext PO localization files to PHP localization files."
---

<h2>NAME</h2>
<p> po2php &#8211; Convert Gettext PO localization files to PHP localization files.</p>
<p> <code>po2php </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp] [&#8211;threshold <i>PERCENT</i>] [&#8211;fuzzy] [&#8211;nofuzzy]</p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/php2po.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/php2po.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in po, pot formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in html, php formats</dd>
<dt>-t/&#8211;template</dt>
<dd> read from TEMPLATE in html, php formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>&#8211;threshold</dt>
<dd> only convert files where the translation completion is above PERCENT</dd>
<dt>&#8211;fuzzy</dt>
<dd> use translations marked fuzzy</dd>
<dt>&#8211;nofuzzy</dt>
<dd> don&#8217;t use translations marked fuzzy (default) </dd>
</dl>
