---
title: "delwords(1)"
name: "delwords"
section: "1"
letter: "d"
url: "/docs/linux/man/1-delwords/"
description: "delwords – Deleting words from specified dictionary collectively"
---

<h2>NAME</h2>
<p> delwords &#8211; Deleting words from specified dictionary collectively</p>
<h2>SYNOPSIS</h2>
<p> <code>delwords [{-cs|-cannaserver} </code><i>cannaserver</i>] dicname</p>
<h2>DESCRIPTION</h2>
<p> <i>delwords</i> deletes words from specified dictionary according to the word information from the standard input. The standard input must be in a format of &#8220;Text Dictionary format&#8221; of Canna. </p>
<p> <i>dicname</i> must be a &#8220;Text Dictionary format&#8221; which can be rewritten.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-cs <i>cannaserver</i> (or -cannaserver <i>cannaserver</i>)</p>
<dd> Specifies the hostname on which the specified dictionary is expected to exist.</dl>
<h2>EXAMPLE</h2>
<pre>
  % delwords mydic &lt; remwords
</pre>
<p> Deletes words defined in <i>remwords</i> from <i>mydic</i>. </p>
<pre>
  % catdic mydic | delwords mydic
</pre>
<p> Clears the contents of <i>mydic</i>. </p>
<h2>Index</h2>
