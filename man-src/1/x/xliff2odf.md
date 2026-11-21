---

title: "xliff2odf(1)"
name: "xliff2odf"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xliff2odf/"
description: "xliff2odf – Convert XLIFF translation files to OpenDocument (ODF) files."
---

<h2>NAME</h2>
<p> xliff2odf &#8211; Convert XLIFF translation files to OpenDocument (ODF) files.</p>
<p> <code>xliff2odf </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp]</p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/odf2xliff.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/odf2xliff.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in xlf format</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in oth, odc, ots, oti, otg, odm, odp, ott, otc, ods, odf, odi, odg, otf, otp, odt formats</dd>
<dt>-t/&#8211;template</dt>
<dd> read from TEMPLATE in oth, odc, ots, oti, otg, odm, odp, ott, otc, ods, odf, odi, odg, otf, otp, odt formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp </dd>
</dl>
