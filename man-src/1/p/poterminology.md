---

title: "poterminology(1)"
name: "poterminology"
section: "1"
letter: "p"
url: "/docs/linux/man/1-poterminology/"
description: "poterminology – Create a terminology file by reading a set of .po or .pot files to produce a pootle-terminology.pot."
---

<h2>NAME</h2>
<p> poterminology &#8211; Create a terminology file by reading a set of .po or .pot files to produce a pootle-terminology.pot.</p>
<p> <code>poterminology </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-u|&#8211;update <i>UPDATEFILE</i>] [-S|&#8211;stopword-list <i>STOPFILE</i>] [-F|&#8211;fold-titlecase] [-C|&#8211;preserve-case] [-I|&#8211;ignore-case] [&#8211;accelerator <i>ACCELERATORS</i>] [-t|&#8211;term-words <i>LENGTH</i>] [&#8211;nonstop-needed <i>MIN</i>] [&#8211;inputs-needed <i>MIN</i>] [&#8211;fullmsg-needed <i>MIN</i>] [&#8211;substr-needed <i>MIN</i>] [&#8211;locs-needed <i>MIN</i>] [&#8211;sort <i>ORDER</i>] [&#8211;source-language <i>LANG</i>] [-v|&#8211;invert]</p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/poterminology.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/poterminology.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in pot, po formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in po, pot formats</dd>
<dt>-u/&#8211;update</dt>
<dd> update terminology in UPDATEFILE</dd>
<dt>-S/&#8211;stopword-list</dt>
<dd> read stopword (term exclusion) list from STOPFILE (default /builddir/build/BUILD/translate-toolkit-1.11.0/translate/misc/../../share/stoplist-en)</dd>
<dt>-F/&#8211;fold-titlecase</dt>
<dd> fold &quot;Title Case&quot; to lowercase (default)</dd>
<dt>-C/&#8211;preserve-case</dt>
<dd> preserve all uppercase/lowercase</dd>
<dt>-I/&#8211;ignore-case</dt>
<dd> make all terms lowercase</dd>
<dt>&#8211;accelerator</dt>
<dd> ignore the given accelerator characters when matching</dd>
<dt>-t/&#8211;term-words</dt>
<dd> generate terms of up to LENGTH words (default 3)</dd>
<dt>&#8211;nonstop-needed</dt>
<dd> omit terms with less than MIN nonstop words (default 1)</dd>
<dt>&#8211;inputs-needed</dt>
<dd> omit terms appearing in less than MIN input files (default 2, or 1 if only one input file)</dd>
<dt>&#8211;fullmsg-needed</dt>
<dd> omit full message terms appearing in less than MIN different messages (default 1)</dd>
<dt>&#8211;substr-needed</dt>
<dd> omit substring-only terms appearing in less than MIN different messages (default 2)</dd>
<dt>&#8211;locs-needed</dt>
<dd> omit terms appearing in less than MIN different original source files (default 2)</dd>
<dt>&#8211;sort</dt>
<dd> output sort order(s): frequency, dictionary, length (may repeat option, default is all in above order)</dd>
<dt>&#8211;source-language</dt>
<dd> the source language code (default &#8216;en&#8217;)</dd>
<dt>-v/&#8211;invert</dt>
<dd> invert the source and target languages for terminology </dd>
</dl>
