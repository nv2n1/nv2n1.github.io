---

title: "po4a-gettextize(1)"
name: "po4a-gettextize"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po4a-gettextize/"
---

po4a-gettextize - convert an original file (and its translation) to a po file 

<h2>SYNOPSIS</h2>

 po4a-gettextize -f &lt;fmt&gt; -m &lt;master.doc&gt; [-l &lt;XX.doc&gt;] -p &lt;XX.po&gt; 

 (XX.po is the output, all others are inputs)

<h2>DESCRIPTION</h2>

 The po4a (po for anything) project goal is to ease translations (and more interestingly, the maintenance of translations) using gettext tools on areas where they were not expected like documentation. 

 The <tt>&quot;po4a-gettextize&quot;</tt> script is in charge of converting documentation files to po files. If you start a new translation, <tt>&quot;po4a-gettextize&quot;</tt> will extract the translatable strings from the documentation file and write a pot file from it. 

 If you already have a translated file, <tt>&quot;po4a-gettextize&quot;</tt> will try to extract the translations it contains and put them in place in the written po file. Be warned that very few intelligence is used in this process: the Nth string of the translated file is supposed to be the translation of the Nth string in the original. If it's not the case, you're dead. That's why it is very important that both files share exactly the same structure. 

 However, <tt>&quot;po4a-gettextize&quot;</tt> will diagnose your death by detecting any desynchronisation between files, and reporting where they occur. In that case, you should edit manually the files to solve the reported disparity. Even if no error were reported, you should check carefully that the generated po file is correct (ie, that each msgstr is the translation of the associated msgid, and not the one before or after). 

 Even if the script manages to do its job without any apparent problem, it still marks all extracted translations as fuzzy, to make sure that the translator will have a look at them, and detect any remaining problem. 

 If the master document has non-ascii characters, the new generated po file will be in utf-8, in order to allow non-standard characters in a culture independent way. Else (if the master document is completely in ascii), the generated po will use the encoding of the translated input document.

<h2>OPTIONS</h2>

<dl>
<dt>-f, --format
</dt><dd> Format of the documentation you want to handle. Use the --help-format option to see the list of available formats.
</dd><dt>-m, --master
</dt><dd> File containing the master document to translate. You can use this option multiple times if you want to gettextize multiple documents.
</dd><dt>-M, --master-charset
</dt><dd> Charset of the file containing the document to translate.
</dd><dt>-l, --localized
</dt><dd> File containing the localized (translated) document. If you provided multiple master files, you may wish to provide multiple localized file by using this option more than once.
</dd><dt>-L, --localized-charset
</dt><dd> Charset of the file containing the localized document.
</dd><dt>-p, --po
</dt><dd> File where the message catalog should be written. If not given, the message catalog will be written to the standard output.
</dd><dt>-o, --option
</dt><dd> Extra option(s) to pass to the format plugin. Specify each option in the 'name=value' format. See the documentation of each plugin for more information about the valid options and their meanings.
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

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/7-po4a/">po4a</a></i>(7), <i><a HREF="/docs/linux/man/1-po4a-updatepo/">po4a-updatepo</a></i>(1), <i><a HREF="/docs/linux/man/1-po4a-translate/">po4a-translate</a></i>(1), <i><a HREF="/docs/linux/man/1-po4a-normalize/">po4a-normalize</a></i>(1).

<h2>AUTHORS</h2>

 <pre>
 Denis Barbier &lt;barbier [at] linuxfr.org&gt;
 Martin Quinson (mquinson#debian.org)
</pre>

<h2>COPYRIGHT AND LICENSE</h2>

 Copyright 2002, 2003, 2004 by SPI, inc. 

 This program is free software; you may redistribute it and/or modify it under the terms of GPL (see the COPYING file).
