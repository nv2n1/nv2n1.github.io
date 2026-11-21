---

title: "poclean(1)"
name: "poclean"
section: "1"
letter: "p"
url: "/docs/linux/man/1-poclean/"
description: "poclean – Produces a clean file from an unclean file (Trados/Wordfast) by stripping out the tw4win indicators."
---

<h2>NAME</h2>
<p> poclean &#8211; Produces a clean file from an unclean file (Trados/Wordfast) by stripping out the tw4win indicators.</p>
<p> <code>poclean </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp]</p>
<p> This does not convert an RTF file to PO/XLIFF, but produces the target file with only the target text in from a text version of the RTF.</p>
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
<dd> read from INPUT in xlf, po, pot formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in po, pot, xlf formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp </dd>
</dl>
