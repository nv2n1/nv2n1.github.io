---
title: "mid3iconv(1)"
name: "mid3iconv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mid3iconv/"
description: "mid3iconv – convert ID3 tag encodings"
---

<h2>NAME</h2>
<p> mid3iconv &#8211; convert ID3 tag encodings</p>
<h2>SYNOPSIS</h2>
<p> <code>mid3iconv</code> [<i>options</i>] <i>filename</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>mid3iconv</code> converts ID3 tags from legacy encodings to Unicode and stores them using the ID3v2 format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;debug</code>,<code> -d</code></p>
<dd> Print updated tags</p>
<dt><code>&#8211;dry-run</code>,<code> -p</code></p>
<dd> Do not actually modify files</p>
<dt><code>&#8211;encoding</code>,<code> -e</code></p>
<dd> Convert from this encoding. By default, your locale&#8217;s default encoding is used.</p>
<dt><code>&#8211;force-v1</code></p>
<dd> Use an ID3v1 tag even if an ID3v2 tag is present</p>
<dt><code>&#8211;quiet</code>,<code> -q</code></p>
<dd> Only output errors</p>
<dt><code>&#8211;remove-v1</code></p>
<dd> Remove any ID3v1 tag after processing the files</dl>
<h2>AUTHOR</h2>
<p> Emfox Zhou. </p>
<p> Based on id3iconv (<i><a rel="nofollow" href="http://www.cs.berkeley.edu/~zf/id3iconv/">http://www.cs.berkeley.edu/~zf/id3iconv/</a></i>) by Feng Zhou. </p>
<h2>Index</h2>
