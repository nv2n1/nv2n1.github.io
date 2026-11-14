---
title: "voikkogc(1)"
name: "voikkogc"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voikkogc/"
description: "voikkogc – test program for Voikko grammar checker"
---

<h2>NAME</h2>
<p> voikkogc &#8211; test program for Voikko grammar checker</p>
<h2>SYNOPSIS</h2>
<p> <code>voikkogc</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>voikkogc</code> is a test program for grammar checking functionality in libvoikko, library of Finnish language tools. It reads sentences or paragraphs from stdin (one per line) and print the results to stdout. The results are structures containing information about grammar errors found in the input paragraph.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;tokenize</code></p>
<dd> Instead of looking for grammar errors, split input into tokens. The tokens are prefixed by type: &quot;W&quot; is a word, &quot;P&quot; is punctuation, &quot;S&quot; is whitespace, &quot;U&quot; is unknown and &quot;E&quot; is a prefix for error messages.</p>
<dt><code>&#8211;split-sentences</code></p>
<dd> Instead of looking for grammar errors, split input into sentences. The sentences are prefixed by type: &quot;B&quot; means that end of sentence is a probably correct, &quot;P&quot; means that end of sentence is a possibly correct (but probably this and the next identified sentence should be joined) and &quot;E&quot; means that sentence ends at the end of input.</p>
<dt><code>-n</code></p>
<dd> Prefix all grammar checker messages with line number of input data.</p>
<dt><code>accept_titles=</code><i>n</i></p>
<dd>
<dt><code>accept_unfinished_paragraphs=</code><i>n</i></p>
<dd>
<dt><code>accept_bulleted_lists=</code><i>n</i></p>
<dd>
 Set the value of the specified boolean option.</p>
<dt><code>explanation_language=</code><i>langcode</i></p>
<dd> Print human readable error explanation in the specified language.</dl>
<h2>BUGS</h2>
<p> Human readable error explanations are printed in UTF-8 regardless of current locale settings.</p>
<h2>SEE ALSO</h2>
<p> <code>voikkospell</code> for common options of different Voikko test tools.</p>
<h2>AUTHOR</h2>
<p> voikkogc and this manual page were written by Harri Pitk&auml;nen (hatapitk [at] iki.fi). </p>
<h2>Index</h2>
