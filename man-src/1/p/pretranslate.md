---
title: "pretranslate(1)"
name: "pretranslate"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pretranslate/"
description: "pretranslate – Fill localization files with suggested translations based on translation memory and existing translations."
---

<h2>NAME</h2>
<p> pretranslate &#8211; Fill localization files with suggested translations based on translation memory and existing translations.</p>
<h2>SYNOPSIS</h2>
<p> <code>pretranslate </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp] [&#8211;tm] [-s|&#8211;similarity] [&#8211;nofuzzymatching]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pretranslate.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pretranslate.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in po, pot, xlf, pot formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in po, pot, xlf formats</p>
<dt>-t/&#8211;template</p>
<dd> read from TEMPLATE in po, pot, xlf formats</p>
<dt>-S/&#8211;timestamp</p>
<dd> skip conversion if the output file has newer timestamp</p>
<dt>&#8211;tm</p>
<dd> The file to use as translation memory when fuzzy matching</p>
<dt>-s/&#8211;similarity</p>
<dd> The minimum similarity for inclusion (default: 75%)</p>
<dt>&#8211;nofuzzymatching</p>
<dd> Disable fuzzy matching </p>
</dl>
<h2>Index</h2>
