---

title: "xliff2oo(1)"
name: "xliff2oo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xliff2oo/"
description: "xliff2oo – Convert XLIFF localization files to an OpenOffice.org (SDF) localization file."
---

<p> xliff2oo &#8211; Convert XLIFF localization files to an OpenOffice.org (SDF) localization file.</p>
<h2>SYNOPSIS</h2>
<p> <code>xliff2oo </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp] [-l|&#8211;language <i>LANG</i>] [&#8211;source-language <i>LANG</i>] [-T|&#8211;keeptimestamp] [&#8211;nonrecursiveoutput] [&#8211;nonrecursivetemplate] [&#8211;skipsource] [&#8211;filteraction <i>ACTION</i>] [&#8211;fuzzy] [&#8211;nofuzzy] [&#8211;multifile <i>MULTIFILESTYLE</i>]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/oo2po.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/oo2po.html</a> for examples and usage instructions.</p>
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
<dd> write to OUTPUT in sdf, oo formats</dd>
<dt>-t/&#8211;template</dt>
<dd> read from TEMPLATE in sdf, oo formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>-l/&#8211;language</dt>
<dd> set target language code (e.g. af-ZA) [required]</dd>
<dt>&#8211;source-language</dt>
<dd> set source language code (default en-US)</dd>
<dt>-T/&#8211;keeptimestamp</dt>
<dd> don&#8217;t change the timestamps of the strings</dd>
<dt>&#8211;nonrecursiveoutput</dt>
<dd> don&#8217;t treat the output oo as a recursive store</dd>
<dt>&#8211;nonrecursivetemplate</dt>
<dd> don&#8217;t treat the template oo as a recursive store</dd>
<dt>&#8211;skipsource</dt>
<dd> don&#8217;t output the source language, but fallback to it where needed</dd>
<dt>&#8211;filteraction</dt>
<dd> action on pofilter failure: none (default), warn, exclude-serious, exclude-all</dd>
<dt>&#8211;fuzzy</dt>
<dd> use translations marked fuzzy</dd>
<dt>&#8211;nofuzzy</dt>
<dd> don&#8217;t use translations marked fuzzy (default)</dd>
<dt>&#8211;multifile</dt>
<dd> how to split po/pot files (single, toplevel or onefile) </dd>
</dl>
