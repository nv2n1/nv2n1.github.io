---

title: "pogrep(1)"
name: "pogrep"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pogrep/"
description: "pogrep – Grep XLIFF, Gettext PO and TMX localization files."
---

<h2>NAME</h2>
<p> pogrep &#8211; Grep XLIFF, Gettext PO and TMX localization files.</p>
<p> <code>pogrep </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [&#8211;search <i>SEARCHPARTS</i>] [-I|&#8211;ignore-case] [-e|&#8211;regexp] [-v|&#8211;invert-match] [&#8211;accelerator <i>ACCELERATOR</i>] [-k|&#8211;keep-translations]</p>
<p> Matches are output to snippet files of the same type which can then be reviewed and later merged using :doc:`pomerge &lt;/commands/pomerge&gt;`. </p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pogrep.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pogrep.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in xliff, mo, xlf, tmx, gmo, pot, xlff, po formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in po, xliff, mo, xlf, tmx, gmo, pot, xlff formats</dd>
<dt>&#8211;search</dt>
<dd> searches the given parts (source, target, notes and locations)</dd>
<dt>-I/&#8211;ignore-case</dt>
<dd> ignore case distinctions</dd>
<dt>-e/&#8211;regexp</dt>
<dd> use regular expression matching</dd>
<dt>-v/&#8211;invert-match</dt>
<dd> select non-matching lines</dd>
<dt>&#8211;accelerator</dt>
<dd> ignores the given accelerator when matching</dd>
<dt>-k/&#8211;keep-translations</dt>
<dd> always extract units with translations </dd>
</dl>
