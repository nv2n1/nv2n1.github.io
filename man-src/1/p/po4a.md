---
title: "po4a(1)"
name: "po4a"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po4a/"
description: "po4a – update both the po files and translated documents in one shot"
---

<h2 class="name">NAME</h2>
<p> po4a &#8211; update both the po files and translated documents in one shot </p>
<h2>SYNOPSIS</h2>
<p> po4a [options] &lt;config_file&gt;</p>
<h2>DESCRIPTION</h2>
<p> The po4a (po for anything) project goal is to ease translations (and more interestingly, the maintenance of translations) using gettext tools on areas where they were not expected like documentation. </p>
<p> The <tt>&quot;po4a&quot;</tt> program is in charge of updating both the po files (to sync them to the original documents) and the translated documents (to sync them to the po files). The main point is to make the use of po4a easier without having to remember of the command line options. </p>
<p> It also allows you to mix documents having different formats into the same pot file so that you can have only one such file per project. </p>
<p> This behaviour can be mimicked by the other tools of the po4a suite (for example with makefiles), but it is rather difficult to do, and exhausting to redo the same complicated makefiles for each project using po4a. </p>
<p> The dataflow can be summarized as follow. Any changes to the master document will be reflected in the po files, and all changes to the po files (either manual or caused by previous step) will be reflected in translation documents. </p>
<pre>
 master document --&gt; po files --&gt; translations
</pre>
<p> The dataflow cannot be inversed in this tool, and changes in translations are overwritten by the content of the po files. As a matter of fact, this tool cannot be used to convert existing translations to the po4a system. For that task, please refer to <i><a href="/docs/linux/man/1-po4a-gettextize/">po4a-gettextize</a></i>(1).</p>
<h2>CONFIGURATION FILE SYNTAX</h2>
<p> The (mandatory) argument is the path to the configuration file to use. Its syntax aims at being simple and close to the configuration files used by the intl-tools projects. </p>
<p> Comments in this files are noted by the char &#8216;#&#8217;. It comments everything until the end of the line. Lines can be continued by escaping the end of line. All non blank lines must begin with a [] command, followed by its arguments. (sound difficult said that way, but it is rather easy, I hope ;)</p>
<h2>Specifying the template languages</h2>
<p> This is an optional command that can simplify the whole config file, and will make it more scalable. You have to specify a list of the languages in which you want to translate the documents. This is as simple as: </p>
<pre>
 [po4a_langs] fr de
</pre>
<p> This will enable you to expand <tt>$lang</tt> to all the specified languages in the rest of the config file.</p>
<h2>Specifying the paths to translator inputs</h2>
<p> First, you have to specify where the translator input files (ie, the files used by translators to do their job) are located. It can be done by such a line: </p>
<pre>
 [po4a_paths] doc/l10n/project.doc.pot fr:doc/l10n/fr.po de:doc/l10n/de.po
</pre>
<p> The command is thus &#8216;po4a_paths&#8217;. The first argument is the path to the pot file to use. All subsequent arguments are of the self-explanatory form: </p>
<pre>
    &lt;lang&gt;:&lt;path to the po file for this lang&gt;
</pre>
<p> If you&#8217;ve defined the template languages, you can rewrite the line above this way: </p>
<pre>
 [po4a_paths] doc/l10n/project.doc.pot $lang:doc/l10n/$lang.po
</pre>
<p> You can also use <tt>$master</tt> to refer to the document basename. In this case, po4a will use a splitted mode: one <font SIZE="-1">POT</font> and one <font SIZE="-1">PO</font> (for each language) will be created for each document specified in the po4a configuration file. See the <code>Splitted mode</code> section. </p>
<pre>
 [po4a_paths] doc/$master/$master.pot $lang:doc/$master/$lang.po
</pre>
<h2>Autodetection of the paths and languages</h2>
<p> Another command can be used to specify the name of a directory where the <font SIZE="-1">PO</font> and <font SIZE="-1">POT</font> files are located. When it is used, po4a will detect the <font SIZE="-1">POT</font> file as the only &#8220;*.pot&#8221; file from the specified directory. Po4a will also use the list of &#8220;*.po&#8221; files to define the list of languages (by stripping out the extension). These languages will be used for the substitution of the <tt>$lang</tt> variable in the rest of the configuration file. </p>
<p> This command should not be used together with the po4a_langs or po4a_paths commands. </p>
<pre>
 [po_directory] po4a/po/
</pre>
<h2>Specifying the documents to translate</h2>
<p> You now naturally have to specify which documents are translated, their format, and where to put the translations. It can be made by such lines: </p>
<pre><code>
[type:sgml] doc / my_stuff.sgml fr : doc / fr / mon_truc.sgml de : doc / de / mein_cram.sgml [type:pod] script fr : doc / fr / script .1 de : doc / de / script .1 add_fr : doc / l10n / script.fr.add
</code></pre>
<p> This should be rather self-explanatory also. Note that in the second case, doc/l10n/script.fr.add is an addendum to add to the French version of this document. Please refer to <i><a href="/docs/linux/man/7-po4a/">po4a</a></i>(7) for more information about the addenda. </p>
<p> More formally, the format is: </p>
<pre>
 [type: &lt;format&gt;] &lt;master_doc&gt; &lt;lang&gt;:&lt;localized_doc&gt;* add_&lt;lang&gt;:&lt;addendum&gt;*
</pre>
<p> If you&#8217;ve defined the template languages, you can rewrite the line above this way: </p>
<pre>
 [type: pod] script $lang:doc/$lang/script.1 \
             add_fr:doc/l10n/script.fr.add
</pre>
<p> If all the languages had addenda with similar paths, you could also write something like: </p>
<pre>
 [type: pod] script $lang:doc/$lang/script.1 \
             add_$lang:doc/l10n/script.$lang.add
</pre>
<h2>Specifying options for the modules</h2>
<p> po4a accepts options that will be passed to the module. These options are module specific and are specified with the -o switch. </p>
<p> If you need a specific option for one of the document you want to translate, you can also specify it in the configuration file. Options are introduced by the <i>opt</i> keyword. The argument of the <i>opt</i> keyword must be quoted with double quotes if it contains a space (e.g. if you specify multiple options, or an option with an argument). You can also specify options that will only apply to a specific language by using the opt_<i>lang</i> keyword. </p>
<p> Here is an example:<br />
&nbsp;<wbr>[type:man]&nbsp;<wbr>data-05/test2_man.1&nbsp;<wbr><tt>$lang:tmp</tt>/test2_man.$lang.1&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>opt:&#8220;-k 75&#8221;&nbsp;<wbr>opt_it:&#8220;-L&nbsp;<wbr><font SIZE="-1">UTF-8</font>&#8221;&nbsp;<wbr>opt_fr:-v </p>
<p> Arguments may contain spaces if you use single quotes or escaped double quotes:<br />
&nbsp;<wbr>[po4a_alias:man]&nbsp;<wbr>man opt:&#8220;-o&nbsp;<wbr>\&#8221;mdoc=NAME,SEE ALSO\&#8220;&nbsp;<wbr>-k 20&#8221; </p>
<p> If you want to specify the same options for many documents, you may want to use an alias (see the <code>Specifying aliases</code> section below). </p>
<p> You can also set options for all the documents specified in the configuration file:<br />
&nbsp;<wbr>[options]&nbsp;<wbr>opt:&#8220;&#8230;&#8221;&nbsp;<wbr>opt_fr:&#8220;&#8230;&#8221;</p>
<h2>Specifying aliases</h2>
<p> If you must specify the same options for multiple files, you may be interested in defining a module alias. This can be done this way: </p>
<p> [po4a_alias:test] man opt:&#8220;-k 21&#8221; opt_es:&#8220;-o debug=splitargs&#8221; </p>
<p> This define a module alias named <i>test</i>, based on the <i>man</i> module, with the <i>-k 21</i> apply to all the languages and with <i>-o debug=splitargs</i> applied to the Spanish translation. </p>
<p> This module alias can then be use like a regular module: </p>
<p> [type:test] data-05/test2_man.1 <tt>$lang:tmp</tt>/test2_man.$lang.1 \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>opt_it:&#8220;-L&nbsp;<wbr><font SIZE="-1">UTF-8</font>&#8221;&nbsp;<wbr>opt_fr:-v </p>
<p> Note that you can specify additional options on a per file basis.</p>
<h2>Splitted mode</h2>
<p> The splitted mode is used when <tt>$master</tt> is used in the [po4a_paths] line. </p>
<p> When the splitted mode is used, a temporary big <font SIZE="-1">POT</font> and temporary big POs are used. This permits to share the translations between all the POs. </p>
<p> If two POs have different translations for the same string, po4a will mark this string as fuzzy and will submit both translations in all the POs which contain this string. Then, when a translator updates the translation and removes the fuzzy tag in one <font SIZE="-1">PO</font>, the translation of this string will be updated in every POs automatically.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-k, &#8211;keep</p>
<dd> Minimal threshold for translation percentage to keep (ie, write) the resulting file (default: 80). Ie, by default, files have to be translated at at least 80% to get written.</p>
<dt>-h, &#8211;help</p>
<dd> Show a short help message.</p>
<dt>-M, &#8211;master-charset</p>
<dd> Charset of the files containing the documents to translate. Note that all master documents must use the same charset for now. This is a known limitation, and we are working on solving this.</p>
<dt>-L, &#8211;localized-charset</p>
<dd> Charset of the files containing the localized documents. Note that all translated documents will use the same charset for now. This is a known limitation, and we are working on solving this.</p>
<dt>-A, &#8211;addendum-charset</p>
<dd> Charset of the addenda. Note that all the addenda should be in the same charset.</p>
<dt>-V, &#8211;version</p>
<dd> Display the version of the script and exit.</p>
<dt>-v, &#8211;verbose</p>
<dd> Increase the verbosity of the program.</p>
<dt>-q, &#8211;quiet</p>
<dd> Decrease the verbosity of the program.</p>
<dt>-d, &#8211;debug</p>
<dd> Output some debugging information.</p>
<dt>-f, &#8211;force</p>
<dd> Always generate the <font SIZE="-1">POT</font> and <font SIZE="-1">PO</font> files, even if po4a considers it is not necessary. </p>
<p> The default behavior (when &#8211;force is not specified) is the following:</p>
<dt>-o, &#8211;option</p>
<dd> Extra option(s) to pass to the format plugin. Specify each option in the &#8216;name=value&#8217; format. See the documentation of each plugin for more information about the valid options and their meanings.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> If the <font SIZE="-1">POT</font> file already exists, it is regenerated if a master document or the configuration file is more recent. The <font SIZE="-1">POT</font> file is also written in a temporary document and po4a verifies that the changes are really needed. </p>
<p> Also, a translation is regenerated only if its master document, the <font SIZE="-1">PO</font> file, one of its addenda or the configuration file is more recent. To avoid trying to regenerate translations which do not pass the threshold test (see <code>&#8211;keep</code>), a file with the &#8216;.po4a-stamp&#8217; extension can be created (see <code>&#8211;stamp</code>).</dl>
</dl>
<dl>
<dt>
<dd>
<p> If a master document includes files, you should use the <code>&#8211;force</code> flag because the modification time of these included files are not taken into account. </p>
<p> The <font SIZE="-1">PO</font> files are always re-generated based on the <font SIZE="-1">POT</font> with <code>msgmerge -U</code>.</dl>
<dt>&#8211;stamp</p>
<dd> Tells po4a to create stamp files when a translation is not generated because it it does not reach the threshold. These stamp files are named according to the expected translated document, with the <i>.po4a-stamp</i> extension. </p>
<p> Note: This only activates the creation of the <i>.po4a-stamp</i> files. The stamp files are always used if they exist, and they are removed with <code>&#8211;rm-translations</code> or when the file is finally translated.</p>
<dt>&#8211;no-translations</p>
<dd> Do not generate the translated documents, only update the <font SIZE="-1">POT</font> and <font SIZE="-1">PO</font> files.</p>
<dt>&#8211;rm-translations</p>
<dd> Remove the translated files (implies &#8211;no-translations).</p>
<dt>&#8211;no-backups</p>
<dd> Do not generate the .po~ backup files.</p>
<dt>&#8211;rm-backups</p>
<dd> Remove the .po~ backup files (implies &#8211;no-backups).</p>
<dt>&#8211;variable <i>var</i>=<i>value</i></p>
<dd> Define a variable that will be expanded in the po4a configuration file. Every occurrence of <i>$(var)</i> will be replaced by <i>value</i>. This option can be used multiple times.</p>
<dt>&#8211;msgid-bugs-address email [at] address</p>
<dd> Set the report address for msgid bugs. By default, the created <font SIZE="-1">POT</font> files have no Report-Msgid-Bugs-To fields.</p>
<dt>&#8211;copyright-holder string</p>
<dd> Set the copyright holder in the <font SIZE="-1">POT</font> header. The default value is &#8220;Free Software Foundation, Inc.&#8221;</p>
<dt>&#8211;package-name string</p>
<dd> Set the package name for the <font SIZE="-1">POT</font> header. The default is &#8220;<font SIZE="-1">PACKAGE</font>&#8221;.</p>
<dt>&#8211;package-version string</p>
<dd> Set the package version for the <font SIZE="-1">POT</font> header. The default is &#8220;<font SIZE="-1">VERSION</font>&#8221;.</p>
<dt>&#8211;msgmerge-opt options</p>
<dd> Extra options for msgmerge.</p>
<dt>&#8211;previous</p>
<dd> This option adds &#8216;&#8211;previous&#8217; to the options passed to msgmerge. It requires gettext 0.16 or later.</dl>
<h2>SHORTCOMINGS</h2>
<dl>
<dt>*</p>
<dd> Duplicates some code with the po4a-* programs.</dl>
<p> Patch welcome ;)</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-po4a/">po4a</a></i>(7), <i><a href="/docs/linux/man/1-po4a-gettextize/">po4a-gettextize</a></i>(1), <i><a href="/docs/linux/man/1-po4a-updatepo/">po4a-updatepo</a></i>(1), <i><a href="/docs/linux/man/1-po4a-translate/">po4a-translate</a></i>(1), <i><a href="/docs/linux/man/1-po4a-normalize/">po4a-normalize</a></i>(1).</p>
<h2>AUTHORS</h2>
<pre>
 Denis Barbier &lt;barbier [at] linuxfr.org&gt;
 Martin Quinson (mquinson#debian.org)
</pre>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright 2002, 2003, 2004 by <font SIZE="-1">SPI</font>, inc. </p>
<p> This program is free software; you may redistribute it and/or modify it under the terms of <font SIZE="-1">GPL</font> (see the <font SIZE="-1">COPYING</font> file). </p>
<h2>Index</h2>
