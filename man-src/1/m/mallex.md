---
title: "mallex(1)"
name: "mallex"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mallex/"
description: "mallex – generate a Malaga run-time lexicon"
---

<h2 class="name">NAME</h2>
<p> mallex &#8211; generate a Malaga run-time lexicon</p>
<h2>SYNOPSIS</h2>
<p> <code>mallex</code> [<code>-binary</code>|<code>-readable</code>|<code>-prelex</code>] <i>project-file</i> </p>
<p> <code>mallex</code> [<code>-binary</code>|<code>-readable</code>|<code>-prelex</code>] <i>symbol-file</i> <i>rule-file</i> [<i>lexicon-file</i>] [<i>prelex-file</i>] </p>
<h2>DESCRIPTION</h2>
<p> Malaga is a development environment for natural-language grammars based on the Left-Associative Grammar formalism. Malaga grammars can be used for automatic morphological and/or syntactic analysis. </p>
<p> The program <code>mallex</code> generates a Malaga run-time lexicon by letting allomorph rules process a base-form lexicon. It can be started in <i>interactive mode</i> to help find bugs in the base-form lexicon or in the allomorph rules. </p>
<p> <code>mallex</code> uses the following grammar components:</p>
<dl>
<dt><i>symbol-file</i></p>
<dd> The <i>symbol-file</i> has the suffix <code>.sym</code> and contains the symbols that are used in the lexicon and/or the allomorph rules.</p>
<dt><i>rule-file</i></p>
<dd> The <i>rule-file</i> has the suffix <code>.all</code> and contains the allomorph rules used to create the runtime-lexicon.</p>
<dt><i>lexicon-file</i></p>
<dd> The <i>lexicon-file</i> has the suffix <code>.lex</code> and contains the base-form lexicon entries that are used as input for the allomorph rules.</p>
<dt><i>prelex-file</i> (optional)</p>
<dd> The <i>prelex-file</i> has the suffix <code>.prelex</code> and contains precompiled allomorph entries, which have been created by a former run of <code>mallex</code> with the option <code>-prelex</code>.</dl>
<p> You can give the names of the grammar components as command line arguments, in any order. Alternatively, you can describe these components in a <i>project-file</i> and use the name of the project file as <code>mallex</code>&#8216; single command-line argument. A project file has the suffix <code>.pro</code>. </p>
<p> If no command line options are given, <code>mallex</code> runs in interactive mode, and you can enter commands. The <i>lexicon-file</i> and <i>prelex-file</i> are not used in interactive mode. If you are not sure about the name of a command, use the command <code>help</code> to get an overview of all <code>mallex</code> commands. </p>
<p> If you want to quit <code>mallex</code>, enter the command <code>quit</code>. </p>
<p> See <code>info Malaga</code> for details. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>[<code>inary</code>]</p>
<dd> Create the run time lexicon file from the base form lexicon file and the optional prelex file, and save it as a binary run-time lexicon, which can be used by <code>malaga</code>.</p>
<dt><code>-h</code>[<code>elp</code>]</p>
<dd> Print a help text about <code>mallex</code>&#8216; command line arguments and exit.</p>
<dt><code>-p</code>[<code>relex</code>]</p>
<dd> Create the run time lexicon, and save it as a binary <i>prelex-file</i>, which can be read in later by another <code>mallex</code> run. output stream.</p>
<dt><code>-r</code>[<code>eadable</code>]</p>
<dd> Create the run time lexicon but don&#8217;t save it, but print its entries in human-readable form on the standard output stream.</p>
<dt><code>-v</code>[<code>ersion</code>]</p>
<dd> Print <code>mallex</code>&#8216; version number and exit. </p>
</dl>
<h2>AUTHORS</h2>
<p> Malaga has been developed by Bjoern Beutel. Numerous other people distributed to it. This manpage was originally written for the Debian distribution by Antti-Juhani Kaijanaho. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-malaga/">malaga</a></code>(1), <code><a href="/docs/linux/man/1-malmake/">malmake</a></code>(1), <code><a href="/docs/linux/man/1-malrul/">malrul</a></code>(1), <code><a href="/docs/linux/man/1-malshow/">malshow</a></code>(1), <code><a href="/docs/linux/man/1-malsym/">malsym</a></code>(1) </p>
<p> &#8220;Malaga 7, User&#8217;s and Programmer&#8217;s Manual&#8221;. Available in Debian systems via <code>info Malaga</code>, and, if the malaga-doc package is installed, in various formats (DVI, Postscript, PDF, HTML) under <i>/usr/share/doc/malaga-doc/</i>. </p>
<h2>Index</h2>
