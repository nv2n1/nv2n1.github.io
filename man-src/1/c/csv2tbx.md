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
<p> <code>csv2tbx </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [&#8211;charset <i>CHARSET</i>] [&#8211;columnorder]</p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/csv2tbx.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/csv2tbx.html</a> for examples and usage instructions</p>
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
<dd> read from INPUT in csv format</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in tbx format</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>&#8211;charset</dt>
<dd> set charset to decode from csv files</dd>
<dt>&#8211;columnorder</dt>
<dd> specify the order and position of columns (comment,source,target) </dd>
</dl>
