---
title: "malrul(1)"
name: "malrul"
section: "1"
letter: "m"
url: "/docs/linux/man/1-malrul/"
description: "malrul – compile a Malaga rule file"
---

<h2 class="name">NAME</h2>
<p> malrul &#8211; compile a Malaga rule file</p>
<h2>SYNOPSIS</h2>
<p> <code>malrul</code> <i>symbol-file</i> <i>rule-file</i> </p>
<h2>DESCRIPTION</h2>
<p> Malaga is a development environment for natural-language grammars based on the Left-Associative Grammar formalism. Malaga grammars can be used for automatic morphological and/or syntactic analysis. </p>
<p> The program <code>malrul</code> compiles a Malaga rule file. Give it the rule file that is to be translated (suffix <code>.mor</code>, <code>.syn</code> or <code>.all</code>) and the associated symbol file (suffix <code>.sym</code> or <code>.esym</code>) as command-line arguments. The order of the arguments is arbitrary. </p>
<p> See <code>info Malaga</code> for details. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>[<code>elp</code>]</p>
<dd> Print a help text about <code>malrul</code>&#8216;s command line arguments and exit.</p>
<dt><code>-v</code>[<code>ersion</code>]</p>
<dd> Print <code>malrul</code>&#8216;s version number and exit. </p>
</dl>
<h2>AUTHORS</h2>
<p> Malaga has been developed by Bjoern Beutel. Numerous other people distributed to it. This manpage was originally written for the Debian distribution by Antti-Juhani Kaijanaho. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-malaga/">malaga</a></code>(1), <code><a href="/docs/linux/man/1-mallex/">mallex</a></code>(1), <code><a href="/docs/linux/man/1-malmake/">malmake</a></code>(1), <code><a href="/docs/linux/man/1-malshow/">malshow</a></code>(1), <code><a href="/docs/linux/man/1-malsym/">malsym</a></code>(1) </p>
<p> &#8220;Malaga 7, User&#8217;s and Programmer&#8217;s Manual&#8221;. Available in Debian systems via <code>info Malaga</code>, and, if the malaga-doc package is installed, in various formats (DVI, Postscript, PDF, HTML) under <i>/usr/share/doc/malaga-doc/</i>. </p>
<h2>Index</h2>
