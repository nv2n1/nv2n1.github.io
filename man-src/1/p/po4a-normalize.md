---
title: "po4a-normalize(1)"
name: "po4a-normalize"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po4a-normalize/"
---

<h2 class="name">NAME</h2>
 

 po4a-normalize - normalize a documentation file by parsing it in po4a, and writing it back 

<h2>SYNOPSIS</h2>

 po4a-normalize -f &lt;fmt&gt; &lt;master.doc&gt;

<h2>DESCRIPTION</h2>

 The po4a (po for anything) project goal is to ease translations (and more interestingly, the maintenance of translations) using gettext tools on areas where they were not expected like documentation. 

 The <tt>&quot;po4a-normalize&quot;</tt> script is a debugging tool used to make sure that po4a don't change the document when it's not supposed to. Only use it if you're developing a new module, or if you doubt the sanity of the tools. 

 The generated document will be written to po4a-normalize.output while the generated po file will be written to po4a-normalize.po. No way to change that ;)

<h2>OPTIONS</h2>

<dl>
<dt>-o, --option
<dd> Extra option(s) to pass to the format plugin. Specify each option in the 'name=value' format. See the documentation of each plugin for more information about the valid options and their meanings.
<dt>-b, --blank
<dd> Create an blank translated document. The generated translated document will be generated assuming all messages are translated by a space or new line. 

 This is useful to check what parts of the document cannot be translated.
<dt>-h, --help
<dd> Show a short help message.
<dt>--help-format
<dd> List the documentation format understood by po4a.
<dt>-f, --format
<dd> Format of the documentation you want to handle. Use the --help-format option to see the list of available formats.
<dt>-M, --master-charset
<dd> Charset of the file containing the document to translate.
<dt>-V, --version
<dd> Display the version of the script and exit.</dl>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/7-po4a/">po4a</a></i>(7), <i><a HREF="/docs/linux/man/1-po4a-updatepo/">po4a-updatepo</a></i>(1), <i><a HREF="/docs/linux/man/1-po4a-translate/">po4a-translate</a></i>(1), <i><a HREF="/docs/linux/man/1-po4a-gettextize/">po4a-gettextize</a></i>(1).

<h2>AUTHORS</h2>

 <pre>
 Denis Barbier &lt;barbier [at] linuxfr.org&gt;
 Martin Quinson (mquinson#debian.org)
</pre>

<h2>COPYRIGHT AND LICENSE</h2>

 Copyright 2002, 2003, 2004 by <font SIZE="-1">SPI</font>, inc. 

 This program is free software; you may redistribute it and/or modify it under the terms of <font SIZE="-1">GPL</font> (see the <font SIZE="-1">COPYING</font> file). 

<h2>Index</h2>


