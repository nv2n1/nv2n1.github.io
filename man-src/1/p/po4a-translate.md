---

title: "po4a-translate(1)"
name: "po4a-translate"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po4a-translate/"
---

po4a-translate - convert a po file back to documentation format 

<h2>SYNOPSIS</h2>

 po4a-translate -f &lt;fmt&gt; -m &lt;master.doc&gt; -p &lt;XX.po&gt; -l &lt;XX.doc&gt; 

 (XX.doc is the output, all others are inputs)

<h2>DESCRIPTION</h2>

 The po4a (po for anything) project goal is to ease translations (and more interestingly, the maintenance of translations) using gettext tools on areas where they were not expected like documentation. 

 The <tt>&quot;po4a-translate&quot;</tt> script is in charge of converting the translation (which was done in a po file) under the documentation format back. The provided <tt>&quot;po&quot;</tt> file should be the translation of the <tt>&quot;pot&quot;</tt> file which were produced by <i><a HREF="/docs/linux/man/1-po4a-gettextize/">po4a-gettextize</a></i>(1).

<h2>OPTIONS</h2>

<dl>
<dt>-f, --format
</dt><dd> Format of the documentation you want to handle. Use the --help-format option to see the list of available formats.
</dd><dt>-a, --addendum
</dt><dd> Add a file to the resulting file (to put translator's name or a section ``About this translation'', for example). The first line of the file to insert should be a PO4A header indicating where it should be added (see section <i></i><i>HOWTO</i><i> add extra text to translations</i> in <i><a HREF="/docs/linux/man/7-po4a/">po4a</a></i>(7)).
</dd><dt>-A, --addendum-charset
</dt><dd> Charset of the addenda. Note that all the addenda should be in the same charset.
</dd><dt>-m, --master
</dt><dd> File containing the master document to translate.
</dd><dt>-M, --master-charset
</dt><dd> Charset of the file containing the document to translate.
</dd><dt>-l, --localized
</dt><dd> File where the localized (translated) document should be written.
</dd><dt>-L, --localized-charset
</dt><dd> Charset of the file containing the localized document.
</dd><dt>-p, --po
</dt><dd> File from which the message catalog should be read.
</dd><dt>-o, --option
</dt><dd> Extra option(s) to pass to the format plugin. Specify each option in the 'name=value' format. See the documentation of each plugin for more information about the valid options and their meanings.
</dd><dt>-k, --keep
</dt><dd> Minimal threshold for translation percentage to keep (ie, write) the resulting file (default: 80). Ie, by default, files have to be translated at at least 80% to get written.
</dd><dt>-w, --width
</dt><dd> Column at which we should wrap the resulting file.
</dd><dt>-h, --help
</dt><dd> Show a short help message.
</dd><dt>--help-format
</dt><dd> List the documentation format understood by po4a.
</dd><dt>-V, --version
</dt><dd> Display the version of the script and exit.
</dd><dt>-v, --verbose
</dt><dd> Increase the verbosity of the program.
</dd><dt>-d, --debug
</dt><dd> Output some debugging information.</dd></dl>

<h2>Adding content (beside translations) to generated files</h2>

 To add some extra content to the generated document beside what you translated (like the name of the translator, or a ``about this translation'' section), you should use the <tt>&quot;--addendum&quot;</tt> option. 

 The first line of the addendum must be a header indicating where to put it in the document (it can be before or after a given part of the document). The rest of the file will be added verbatim to the resulting file without further processing. 

 Note that if po4a-translate fails to add one of the given files, it discards the whole translation (because the missing file could be the one indicating the author, what would prevent the users to contact him to report bugs in the translation). 

 The header has a pretty rigid syntax. For more information on how to use this feature and how it works, please refer to the <i><a HREF="/docs/linux/man/7-po4a/">po4a</a></i>(7) man page.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/7-po4a/">po4a</a></i>(7), <i><a HREF="/docs/linux/man/1-po4a-gettextize/">po4a-gettextize</a></i>(1), <i><a HREF="/docs/linux/man/1-po4a-updatepo/">po4a-updatepo</a></i>(1), <i><a HREF="/docs/linux/man/1-po4a-normalize/">po4a-normalize</a></i>(1).

<h2>AUTHORS</h2>

 <pre>
 Denis Barbier &lt;barbier [at] linuxfr.org&gt;
 Martin Quinson (mquinson#debian.org)
</pre>

<h2>COPYRIGHT AND LICENSE</h2>

 Copyright 2002, 2003, 2004 by SPI, inc. 

 This program is free software; you may redistribute it and/or modify it under the terms of GPL (see the COPYING file).
