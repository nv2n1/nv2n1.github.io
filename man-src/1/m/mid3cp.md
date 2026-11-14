---
title: "mid3cp(1)"
name: "mid3cp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mid3cp/"
description: "mid3cp – copy ID3 tags"
---

<h2>NAME</h2>
<p> mid3cp &#8211; copy ID3 tags</p>
<h2>SYNOPSIS</h2>
<p> <code>mid3cp</code> [<i>options</i>] <i>source</i> <i>dest</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mid3cp</code> copies the ID3 tags from a source file to a destination file. </p>
<p> It is designed to provide similar functionality to id3lib&#8217;s id3cp tool, and can optionally write ID3v1 tags. It can also exclude specific tags from being copied.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;verbose</code>,<code> -v</code></p>
<dd> Be verbose: state all operations performed, and list tags in source file.</p>
<dt><code>&#8211;write-v1</code></p>
<dd> Write ID3v1 tags to the destination file, derived from the ID3v2 tags.</p>
<dt><code>&#8211;exclude-tag</code>,<code> -x</code></p>
<dd> Exclude a specific tag from being copied. Can be specified multiple times.</dl>
<h2>AUTHOR</h2>
<p> Marcus Sundman. </p>
<p> Based on id3cp (part of id3lib) by Dirk Mahoney and Scott Thomas Haug. </p>
<h2>Index</h2>
