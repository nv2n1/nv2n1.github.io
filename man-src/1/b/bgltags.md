---
title: "bgltags(1)"
name: "bgltags"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bgltags/"
description: "bgltags – generate tag file for Emacs"
---

<h2 class="name">NAME</h2>
<p> bgltags &#8211; generate tag file for Emacs</p>
<h2>SYNOPSIS</h2>
<p> <code>bgltags</code> [ options ] [ <i>objfile</i> [ <i>gmon.out</i> ] ] </p>
<h2>DESCRIPTION</h2>
<p> The <code>bgltags</code> program is used to create a tag table file, in a format understood by <code><a href="/docs/linux/man/1-emacs/">emacs</a>(1)</code>. This programs understand the syntax of the Bigloo files. It reads the files specified on the command line, and write a tag table (defaults: <i>TAGS</i>) in the current working directory. Files specified with relative file names will be recorded in the tag table with file names relative to the directory where the tag table re- sides. Files specified with absolute file names will be recorded with absolute file names. The program does not recognize the language used in an input file based on its file name and contents. The <i>&#8211;language</i> switch can be used to force parsing of the file names following the switch according to the given language, overriding guesses based on file-name extensions. Source files that are not Scheme are actually processed by the <code>etags</code> program. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>-a, &#8211;append</code></p>
<dd>
<dd> Append to existing tag file. </p>
<dt><code>-o tagfile, &#8211;output=tagfile</code></p>
<dd> Explicit name of file for tag table; overrides default `TAGS&#8217;. </p>
<dt><code>-v</code></p>
<dd> Print the current version of the program. </p>
<dt><code>-module</code></p>
<dd> Generate an entry in the table for each modules. Normally modules identifier are not indexed in the tags table. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bigloo/">bigloo</a>(1), <a href="/docs/linux/man/1-bglafile/">bglafile</a>(1), <a href="/docs/linux/man/1-bgldepend/">bgldepend</a>(1), <a href="/docs/linux/man/1-etags/">etags</a>(1), <a href="/docs/linux/man/1-emacs/">emacs</a>(1), <a href="/docs/linux/man/1-bglmco/">bglmco</a>(1), <a href="/docs/linux/man/1-xemacs/">xemacs</a>(1) </p>
<h2>AUTHOR</h2>
<p> Manuel SERRANO, Manuel.Serrano [at] inria.fr </p>
<h2>Index</h2>
