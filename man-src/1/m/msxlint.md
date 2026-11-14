---
title: "msxlint(1)"
name: "msxlint"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msxlint/"
description: "msxlint – detects incorrectly formatted notes lines in a MusiXTeX source file."
---

<h2 class="name">NAME</h2>
<p> msxlint &#8211; detects incorrectly formatted notes lines in a MusiXTeX source file.</p>
<h2>SYNOPSIS</h2>
<p> <code>msxlint</code> [<code>-v | &#8211;version | -h | &#8211;help</code>] </p>
<p> <code>msxlint</code> [<code>-d&nbsp;</code>|<code>&nbsp;&#8211;debug</code>]&#8230; [<i>infile</i>[<i></i><code>.tex</code>]&#8230;] </p>
<p> If no <i>infiles</i> are specifed, standard input is used. </p>
<h2>USAGE</h2>
<p> The format that notes commands are expected to match is determined by \instrumentnumber and \setstaffs commands, or uses of the \TransformNotes macro defined in musixtnt.tex (see musixdoc.pdf), or re-definitions of the notes macro. Output consists of messages about format errors, with listings of the ill-formatted lines. </p>
<h2>LIMITATIONS</h2>
<p> User-defined macros are not processed or expanded. Notes commands (
otes, \Notes, etc.) can have line breaks, but other commands must fit on one line.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fixmsxpart/">fixmsxpart</a></code>(1) </p>
<p> musixdoc.pdf </p>
<h2>AUTHOR</h2>
<p> This program and manual page were written by Bob Tennent &lt;rdt [at] cs.queensu.ca&gt;. </p>
<h2>Index</h2>
