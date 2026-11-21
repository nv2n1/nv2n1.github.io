---

title: "po2prop(1)"
name: "po2prop"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po2prop/"
description: "po2prop – Convert Gettext PO localization files to Java/Mozilla .properties files."
---

<p> po2prop &#8211; Convert Gettext PO localization files to Java/Mozilla .properties files.</p>
<h2>SYNOPSIS</h2>
<p> <code>po2prop </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp] [&#8211;personality <i>TYPE</i>] [&#8211;encoding <i>ENCODING</i>] [&#8211;removeuntranslated] [&#8211;threshold <i>PERCENT</i>] [&#8211;fuzzy] [&#8211;nofuzzy]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/prop2po.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/prop2po.html</a> for examples and usage instructions.</p>
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
<dd> write to OUTPUT in properties, lang, strings formats</dd>
<dt>-t/&#8211;template</dt>
<dd> read from TEMPLATE in properties, lang, strings formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>&#8211;personality</dt>
<dd> override the input file format: flex, java, mozilla, java-utf8, skype, gaia, strings (for .properties files, default: java)</dd>
<dt>&#8211;encoding</dt>
<dd> override the encoding set by the personality</dd>
<dt>&#8211;removeuntranslated</dt>
<dd> remove key value from output if it is untranslated</dd>
<dt>&#8211;threshold</dt>
<dd> only convert files where the translation completion is above PERCENT</dd>
<dt>&#8211;fuzzy</dt>
<dd> use translations marked fuzzy</dd>
<dt>&#8211;nofuzzy</dt>
<dd> don&#8217;t use translations marked fuzzy (default) </dd>
</dl>
