---
title: "bglpp(1)"
name: "bglpp"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bglpp/"
description: "bglpp – a Scheme Pretty Printer"
---

<h2 class="name">NAME</h2>
<p> bglpp &#8211; a Scheme Pretty Printer</p>
<h2>SYNOPSIS</h2>
<p> <code>bglpp</code> [ options ] <i>sourcefile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>bglpp</code> reads <i>sourcefile</i> one at a time and pretty print them. Normally <code>bglpp</code> output its result on the standard output device. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>-o &lt;file&gt;</code></p>
<dd>
<dd> Output files to <i>file</i>. </p>
<dt><code>-comment</code></p>
<dd> Don&#8217;t output any Scheme comments. </p>
<dt><code>-upper</code></p>
<dd> Translate identifiers to upper case. </p>
<dt><code>-lower</code></p>
<dd> Translate identifiers to lower case. </p>
<dt><code>-w&lt;width&gt;</code></p>
<dd> Set output device column <i>width</i>. </p>
</dl>
<h2>EXAMPLE</h2>
<p> To pretty print the file &#8220;foo.scm&#8221; translating identifier to lower case, for an output device with 50 columns: </p>
<p> &#8220;bglpp foo.scm -w50 -lower&#8221;. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bigloo/">bigloo</a>(1), <a href="/docs/linux/man/1-indent/">indent</a>(1), <a href="/docs/linux/man/1-cb/">cb</a>(1) </p>
<h2>AUTHOR</h2>
<p> Manuel SERRANO, Manuel.Serrano [at] inria.fr </p>
<h2>Index</h2>
