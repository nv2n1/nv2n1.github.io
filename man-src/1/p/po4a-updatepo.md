---
title: "po4a-updatepo(1)"
name: "po4a-updatepo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po4a-updatepo/"
---

<h2 class="name">NAME</h2>
 

 po4a-updatepo - update the translation (in po format) of documentation 

<h2>SYNOPSIS</h2>

 po4a-updatepo -f &lt;fmt&gt; (-m &lt;master.doc&gt;)+ (-p &lt;<font SIZE="-1">XX</font>.po&gt;)+ 

 (<font SIZE="-1">XX</font>.po are the outputs, all others are inputs)

<h2>DESCRIPTION</h2>

 The po4a (po for anything) project goal is to ease translations (and more interestingly, the maintenance of translations) using gettext tools on areas where they were not expected like documentation. 

 The <tt>&quot;po4a-updatepo&quot;</tt> script is in charge of updating po files to make them reflect the changes made to the original documentation file. For that, it converts the documentation file to a pot file, and call <i><a HREF="/docs/linux/man/1-msgmerge/">msgmerge</a></i>(1) on this new pot and on the provided po files. 

 It is possible to give more than one po file (if you want to update several languages at once), and several documentation files (if you want to store the translations of several documents in the same po file). 

 If the master document has non-ascii characters, it will convert the po files to utf-8 (if they weren't already), in order to allow non-standard characters in a culture independent way.

<h2>COMMAND-LINE OPTIONS</h2>

<dl>
<dt>-f, --format
<dd> Format of the documentation you want to handle. Use the --help-format option to see the list of available formats.
<dt>-m, --master
<dd> File(s) containing the master document to translate.
<dt>-M, --master-charset
<dd> Charset of the files containing the document to translate. Note that all files must have the same charset.
<dt>-p, --po
<dd> Po file(s) to update. If these files do not exist, they are created by <tt>&quot;po4a-updatepo&quot;</tt>.
<dt>-o, --option
<dd> Extra option(s) to pass to the format plugin and other po4a internal module. Specify each option in the 'name=value' format. See the documentation of each plugin for more information about the valid options and their meanings.
<dt>--previous
<dd> This option adds '--previous' to the options passed to msgmerge. It requires gettext 0.16 or later.
<dt>--msgmerge-opt options
<dd> Extra options for msgmerge.
<dt>-h, --help
<dd> Show a short help message.
<dt>--help-format
<dd> List the documentation format handled by po4a.
<dt>-V, --version
<dd> Display the version of the script and exit.
<dt>-v, --verbose
<dd> Increase the verbosity of the program.
<dt>-d, --debug
<dd> Output some debugging information.</dl>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/7-po4a/">po4a</a></i>(7), <i><a HREF="/docs/linux/man/1-po4a-gettextize/">po4a-gettextize</a></i>(1), <i><a HREF="/docs/linux/man/1-po4a-translate/">po4a-translate</a></i>(1), <i><a HREF="/docs/linux/man/1-po4a-normalize/">po4a-normalize</a></i>(1).

<h2>AUTHORS</h2>

 <pre>
 Denis Barbier &lt;barbier [at] linuxfr.org&gt;
 Martin Quinson (mquinson#debian.org)
</pre>

<h2>COPYRIGHT AND LICENSE</h2>

 Copyright 2002, 2003, 2004, 2005 by <font SIZE="-1">SPI</font>, inc. 

 This program is free software; you may redistribute it and/or modify it under the terms of <font SIZE="-1">GPL</font> (see the <font SIZE="-1">COPYING</font> file). 

<h2>Index</h2>


