---
title: "git-stripspace(1)"
name: "git-stripspace"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-stripspace/"
description: "git-stripspace – Remove unnecessary whitespace"
---

<h2 class="name">NAME</h2>
<p> git-stripspace &#8211; Remove unnecessary whitespace </p>
<h2>SYNOPSIS</h2>
<pre><code>
git stripspace[-s | --strip - comments] git stripspace[-c | --comment - lines]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Read text, such as commit messages, notes, tags and branch descriptions, from the standard input and clean it in the manner used by Git. </p>
<p> With no arguments, this will: </p>
<dl>
<dt>
<dd> &bull; remove trailing whitespace from all lines</dl>
<dl>
<dt>
<dd> &bull; collapse multiple consecutive empty lines into one empty line</dl>
<dl>
<dt>
<dd> &bull; remove empty lines from the beginning and end of the input</dl>
<dl>
<dt>
<dd> &bull; add a missing <i>
</i> to the last line if necessary.</dl>
<p> In the case where the input consists entirely of whitespace characters, no output will be produced. </p>
<p> <code>NOTE</code>: This is intended for cleaning metadata, prefer the <code>&#8211;whitespace=fix</code> mode of <code><a href="/docs/linux/man/1-git-apply/">git-apply</a></code>(1) for correcting whitespace of patches or files in the repository.</p>
<h2>OPTIONS</h2>
<p> -s, &#8211;strip-comments</p>
<dl>
<dt>
<dd> Skip and remove all lines starting with comment character (default <i>#</i>).</dl>
<p> -c, &#8211;comment-lines</p>
<dl>
<dt>
<dd> Prepend comment character and blank to each line. Lines will automatically be terminated with a newline. On empty lines, only the comment character will be prepended.</dl>
<h2>EXAMPLES</h2>
<p> Given the following noisy input with <i>$</i> indicating the end of a line: </p>
<dl>
<dt>
<dd>
<pre>
|A brief introduction   $
|   $
|$
|A new paragraph$
|# with a commented-out line    $
|explaining lots of stuff.$
|$
|# An old paragraph, also commented-out. $
|      $
|The end.$
|  $
</pre>
</dl>
<p> Use <i>git stripspace</i> with no arguments to obtain: </p>
<dl>
<dt>
<dd>
<pre>
|A brief introduction$
|$
|A new paragraph$
|# with a commented-out line$
|explaining lots of stuff.$
|$
|# An old paragraph, also commented-out.$
|$
|The end.$
</pre>
</dl>
<p> Use <i>git stripspace &#8211;strip-comments</i> to obtain: </p>
<dl>
<dt>
<dd>
<pre>
|A brief introduction$
|$
|A new paragraph$
|explaining lots of stuff.$
|$
|The end.$
</pre>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
