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
<h2>SYNOPSIS</h2>
<p> <code>poterminology </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-u|&#8211;update <i>UPDATEFILE</i>] [-S|&#8211;stopword-list <i>STOPFILE</i>] [-F|&#8211;fold-titlecase] [-C|&#8211;preserve-case] [-I|&#8211;ignore-case] [&#8211;accelerator <i>ACCELERATORS</i>] [-t|&#8211;term-words <i>LENGTH</i>] [&#8211;nonstop-needed <i>MIN</i>] [&#8211;inputs-needed <i>MIN</i>] [&#8211;fullmsg-needed <i>MIN</i>] [&#8211;substr-needed <i>MIN</i>] [&#8211;locs-needed <i>MIN</i>] [&#8211;sort <i>ORDER</i>] [&#8211;source-language <i>LANG</i>] [-v|&#8211;invert]</p>
<h2>DESCRIPTION</h2>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/poterminology.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/poterminology.html</a> for examples and usage instructions.</p>
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
<dd> read from INPUT in pot, po formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in po, pot formats</p>
<dt>-u/&#8211;update</p>
<dd> update terminology in UPDATEFILE</p>
<dt>-S/&#8211;stopword-list</p>
<dd> read stopword (term exclusion) list from STOPFILE (default /builddir/build/BUILD/translate-toolkit-1.11.0/translate/misc/../../share/stoplist-en)</p>
<dt>-F/&#8211;fold-titlecase</p>
<dd> fold &quot;Title Case&quot; to lowercase (default)</p>
<dt>-C/&#8211;preserve-case</p>
<dd> preserve all uppercase/lowercase</p>
<dt>-I/&#8211;ignore-case</p>
<dd> make all terms lowercase</p>
<dt>&#8211;accelerator</p>
<dd> ignore the given accelerator characters when matching</p>
<dt>-t/&#8211;term-words</p>
<dd> generate terms of up to LENGTH words (default 3)</p>
<dt>&#8211;nonstop-needed</p>
<dd> omit terms with less than MIN nonstop words (default 1)</p>
<dt>&#8211;inputs-needed</p>
<dd> omit terms appearing in less than MIN input files (default 2, or 1 if only one input file)</p>
<dt>&#8211;fullmsg-needed</p>
<dd> omit full message terms appearing in less than MIN different messages (default 1)</p>
<dt>&#8211;substr-needed</p>
<dd> omit substring-only terms appearing in less than MIN different messages (default 2)</p>
<dt>&#8211;locs-needed</p>
<dd> omit terms appearing in less than MIN different original source files (default 2)</p>
<dt>&#8211;sort</p>
<dd> output sort order(s): frequency, dictionary, length (may repeat option, default is all in above order)</p>
<dt>&#8211;source-language</p>
<dd> the source language code (default &#8216;en&#8217;)</p>
<dt>-v/&#8211;invert</p>
<dd> invert the source and target languages for terminology </p>
</dl>
<h2>Index</h2>
