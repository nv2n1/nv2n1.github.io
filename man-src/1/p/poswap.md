---

title: "poswap(1)"
name: "poswap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-poswap/"
description: "poswap – Builds a new translation file with the target of the input language as source language."
---

<p> poswap &#8211; Builds a new translation file with the target of the input language as source language.</p>
<h2>SYNOPSIS</h2>
<p> <code>poswap </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-t|&#8211;template <i>TEMPLATE</i>] [-S|&#8211;timestamp] [&#8211;reverse]</p>
<h2>DESCRIPTION</h2>
<p> Note: Ensure that the two po files correspond 100% to the same pot file before using<br/>
this. </p>
<p> To translate Kurdish (ku) through French:: </p>
<p>&nbsp;<wbr>po2swap -i fr/&nbsp;<wbr>-t ku -o fr-ku </p>
<p> To convert the fr-ku files back to en-ku:: </p>
<p>&nbsp;<wbr>po2swap &#8211;reverse -i fr/&nbsp;<wbr>-t fr-ku -o en-ku </p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/poswap.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/poswap.html</a> for examples and usage instructions.</p>
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
<dd> write to OUTPUT in po, pot formats</dd>
<dt>-t/&#8211;template</dt>
<dd> read from TEMPLATE in pot, po, pot formats</dd>
<dt>-S/&#8211;timestamp</dt>
<dd> skip conversion if the output file has newer timestamp</dd>
<dt>&#8211;reverse</dt>
<dd> reverse the process of intermediate language conversion </dd>
</dl>
