---
title: "malsym(1)"
name: "malsym"
section: "1"
letter: "m"
url: "/docs/linux/man/1-malsym/"
description: "malsym – compile a Malaga symbol file"
---

<h2 class="name">NAME</h2>
<p> malsym &#8211; compile a Malaga symbol file</p>
<h2>SYNOPSIS</h2>
<p> <code>malsym</code> <i>symbol-file</i> </p>
<p> <code>malsym</code> <i>extended-symbol-file</i> <code>-use</code> <i>symbol-file</i> </p>
<h2>DESCRIPTION</h2>
<p> Malaga is a development environment for natural-language grammars based on the Left-Associative Grammar formalism. Malaga grammars can be used for automatic morphological and/or syntactic analysis. </p>
<p> The program <code>malsym</code> compiles a Malaga symbol file. Give it the symbol file (suffix <code>.sym</code> or <code>.esym</code>) that is to be translated as argument. If an <i>extended-symbol-file</i> (suffix <code>.esym</code>) is to be compiled, you must add the option <code>-use</code>. </p>
<p> See <code>info Malaga</code> for details. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>[<code>elp</code>]</p>
<dd> Print a help text about <code>malsym</code>&#8216;s command line arguments and exit.</p>
<dt><code>-u</code>[<code>se</code>] <i>symbol-file</i></p>
<dd> Use the already compiled <i>symbol-file</i> as the base symbol file when compiling an <i>extended symbol file</i>.</p>
<dt><code>-v</code>[<code>ersion</code>]</p>
<dd> Print <code>malsym</code>&#8216;s version number and exit. </p>
</dl>
<h2>AUTHORS</h2>
<p> Malaga has been developed by Bjoern Beutel. Numerous other people distributed to it. This manpage was originally written for the Debian distribution by Antti-Juhani Kaijanaho. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-malaga/">malaga</a></code>(1), <code><a href="/docs/linux/man/1-mallex/">mallex</a></code>(1), <code><a href="/docs/linux/man/1-malmake/">malmake</a></code>(1), <code><a href="/docs/linux/man/1-malrul/">malrul</a></code>(1), <code><a href="/docs/linux/man/1-malshow/">malshow</a></code>(1) </p>
<p> &#8220;Malaga 7, User&#8217;s and Programmer&#8217;s Manual&#8221;. Available in Debian systems via <code>info Malaga</code>, and, if the malaga-doc package is installed, in various formats (DVI, Postscript, PDF, HTML) under <i>/usr/share/doc/malaga-doc/</i>. </p>
<h2>Index</h2>
