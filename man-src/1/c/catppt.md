---
title: "catppt(1)"
name: "catppt"
section: "1"
letter: "c"
url: "/docs/linux/man/1-catppt/"
description: "catppt – reads MS-PowerPoint file and puts its content on standard output"
---

<h2>NAME</h2>
<p> catppt &#8211; reads MS-PowerPoint file and puts its content on standard output</p>
<h2>SYNOPSIS</h2>
<p> <code>catppt </code>[<code>-lV</code>] [<code>-b</code> <i> string </i>] [<code>-s</code> <i> charset </i>] [<code>-d</code> <i> charset </i>] <i>files</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>catppt</code> reads MS-PowerPoint presentations and dumps its content to stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code></p>
<dd> list known charsets and exit successfully</p>
<dt><code>-b</code><i>string</i></p>
<dd> slides break string. This string (by default &#8211; formfeed) would be output at the end of each slide page. </p>
<dt><code>-d</code><i>charset`</i></p>
<dd> &#8211; specifies destination charset name. Charset file has format described in CHARACTER SETS section of <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1) manual page. By default, current locale charset would be used if langinfo support was enabled at the compile time. </p>
<dt><code>-s</code><i>charset</i></p>
<dd> &#8211; specifies source charset. Typically, PowerPoint files use UNICODE strings with known charsets, but for some reason you may wish to override it. </p>
<dt><code>-V</code></p>
<dd> outputs version number </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1), <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1), <code><a href="/docs/linux/man/1-xls2csv/">xls2csv</a></code>(1), <code><a href="/docs/linux/man/1-strings/">strings</a></code>(1), <code><a href="/docs/linux/man/4-utf/">utf</a></code>(4), <code><a href="/docs/linux/man/4-unicode/">unicode</a></code>(4) </p>
<h2>AUTHOR</h2>
<p> Alex Ott &lt;alexott [at] gmail.com&gt; </p>
<h2>Index</h2>
