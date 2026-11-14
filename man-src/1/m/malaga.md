---
title: "malaga(1)"
name: "malaga"
section: "1"
letter: "m"
url: "/docs/linux/man/1-malaga/"
description: "malaga – natural-language word and sentence analysis"
---

<h2 class="name">NAME</h2>
<p> malaga &#8211; natural-language word and sentence analysis</p>
<h2>SYNOPSIS</h2>
<p> <code>malaga</code> [<code>-morphology</code>|<code>-syntax</code>] [<code>-quoted</code>] [<code>-input</code> <i>input</i>] <i>project-file</i> </p>
<h2>DESCRIPTION</h2>
<p> Malaga is a development environment for natural-language grammars based on the Left-Associative Grammar formalism. Malaga grammars can be used for automatic morphological and/or syntactic analysis. </p>
<p> The program <code>malaga</code> is Malaga&#8217;s user interface for analysing word forms and sentences, displaying the results and finding bugs in a grammar. </p>
<p> <code>malaga</code> requires the name of a language-dependent <i>project-file</i> as a command-line argument. </p>
<p> If no command line options are given, <code>malaga</code> starts in interactive mode, and you can enter commands. If you are not sure about the name of a command, use the command <code>help</code> to get an overview of all <code>malaga</code> commands. </p>
<p> If you want to quit <code>malaga</code>, enter the command <code>quit</code>. </p>
<p> See <code>info Malaga</code> for details. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>[<code>elp</code>]</p>
<dd> Print a help text about <code>malaga</code>&#8216;s command line arguments and exit.</p>
<dt><code>-i</code>[<code>nput</code>] <i>input</i></p>
<dd> Analyse a single word or sentence given as command line argument (only valid in morphology or syntax mode).</p>
<dt><code>-m</code>[<code>orphology</code>]</p>
<dd> Start <code>malaga</code> in morphology mode. In this mode word forms are read in from the standard input stream and analysed (one word form per line). The analysis result are written to the standard output stream.</p>
<dt><code>-q</code>[<code>uoted</code>]</p>
<dd> The input lines to be analysed are quoted (only valid in morphology or syntax mode).</p>
<dt><code>-s</code>[<code>yntax</code>]</p>
<dd> Start <code>malaga</code> in syntax mode. In this mode sentences are read in from the standard input stream and analysed (one sentence per line). The analysis result is written to the standard output stream.</p>
<dt><code>-v</code>[<code>ersion</code>]</p>
<dd> Print <code>malaga</code>&#8216;s version number and exit. </p>
</dl>
<h2>AUTHORS</h2>
<p> Malaga was written by Bjoern Beutel. Numerous other people distributed to Malaga. This manpage was originally written for the Debian distribution by Antti-Juhani Kaijanaho. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mallex/">mallex</a></code>(1), <code><a href="/docs/linux/man/1-malmake/">malmake</a></code>(1), <code><a href="/docs/linux/man/1-malrul/">malrul</a></code>(1), <code><a href="/docs/linux/man/1-malshow/">malshow</a></code>(1), <code><a href="/docs/linux/man/1-malsym/">malsym</a></code>(1) </p>
<p> &#8220;Malaga 7, User&#8217;s and Programmer&#8217;s Manual&#8221;. Available in Debian systems via <code>info Malaga</code>, and, if the malaga-doc package is installed, in various formats (DVI, Postscript, PDF, HTML) under <i>/usr/share/doc/malaga-doc/</i>. </p>
<h2>Index</h2>
