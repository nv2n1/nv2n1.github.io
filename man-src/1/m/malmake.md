---
title: "malmake(1)"
name: "malmake"
section: "1"
letter: "m"
url: "/docs/linux/man/1-malmake/"
description: "malmake – compile a Malaga project"
---

<h2 class="name">NAME</h2>
<p> malmake &#8211; compile a Malaga project</p>
<h2>SYNOPSIS</h2>
<p> <code>malmake</code> [<code>-new</code>] <i>project-file</i> </p>
<h2>DESCRIPTION</h2>
<p> Malaga is a development environment for natural-language grammars based on the Left-Associative Grammar formalism. Malaga grammars can be used for automatic morphological and/or syntactic analysis. </p>
<p> The program <code>malmake</code> reads a project file, checks if all grammar files needed do exist, and translates all grammar files that have not yet been translated or whose source files have changed since they have been translated. It calls the programs <code><a href="/docs/linux/man/1-malsym/">malsym</a></code>(1), <code><a href="/docs/linux/man/1-mallex/">mallex</a></code>(1) and <code><a href="/docs/linux/man/1-malrul/">malrul</a></code>(1) if needed. It is in essence a <code><a href="/docs/linux/man/1-make/">make</a></code>(1) for the Malaga programming language. </p>
<p> See <code>info Malaga</code> for details. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>[<code>elp</code>]</p>
<dd> Print a help text about <code>malmake</code>&#8216;s command line arguments and exit.</p>
<dt><code>-n</code>[<code>ew</code>]</p>
<dd> (Re)compile all files, even if their sources have not changed meanwhile.</p>
<dt><code>-v</code>[<code>ersion</code>]</p>
<dd> Print <code>malmake</code>&#8216;s version number and exit. </p>
</dl>
<h2>AUTHORS</h2>
<p> Malaga has been developed by Bjoern Beutel. Numerous other people distributed to it. This manpage was originally written for the Debian distribution by Antti-Juhani Kaijanaho. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-malaga/">malaga</a></code>(1), <code><a href="/docs/linux/man/1-mallex/">mallex</a></code>(1), <code><a href="/docs/linux/man/1-malrul/">malrul</a></code>(1), <code><a href="/docs/linux/man/1-malshow/">malshow</a></code>(1), <code><a href="/docs/linux/man/1-malsym/">malsym</a></code>(1) </p>
<p> &#8220;Malaga 7, User&#8217;s and Programmer&#8217;s Manual&#8221;. Available in Debian systems via <code>info Malaga</code>, and, if the malaga-doc package is installed, in various formats (DVI, Postscript, PDF, HTML) under <i>/usr/share/doc/malaga-doc/</i>. </p>
<h2>Index</h2>
