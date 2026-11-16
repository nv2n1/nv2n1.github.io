---
title: "odf2xliff(1)"
name: "odf2xliff"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odf2xliff/"
description: "odf2xliff – Convert OpenDocument (ODF) files to XLIFF localization files."
---

<h2>NAME</h2>
<p> odf2xliff &#8211; Convert OpenDocument (ODF) files to XLIFF localization files.</p>
<h2>SYNOPSIS</h2>
<p> <code>odf2xliff </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-S|&#8211;timestamp] [&#8211;engine]</p>
<h2>DESCRIPTION</h2>
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
<dd> read from INPUT in oth, oti, ots, odp, ods, odt, otf, otg, odi, odm, sxw, otp, otc, odc, ott, odf, odg formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in xlf format</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>&#8211;engine</dt>
<dd> Choose whether itools (&#8211;engine=itools) or the translate toolkit (&#8211;engine=toolkit)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>should be used as the engine to convert an ODF file to an XLIFF file. </dd>
</dl>
<h2>Index</h2>
