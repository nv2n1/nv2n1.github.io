---
title: "mergelib(1)"
name: "mergelib"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mergelib/"
description: "mergelib – merge one library into another"
---

<h2>NAME</h2>
<p> mergelib &#8211; merge one library into another</p>
<h2>SYNOPSIS</h2>
<p> <code>mergelib</code> <i>to-library</i> <i>from-library</i> [<i>object-filename-prefix</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <i>mergelib</i> program merges objects from one library into another. The names of object files in <i>from-library</i> will be prefixed by <i>object-filename-prefix</i> (&#34;_&#34; by default) to avoid name clashes. The merged library will be left in <i>to-library</i>.</p>
<h2>AUTHOR</h2>
<p> Jim Fulton wrote the <i>mergelib</i> program for the X Consortium. </p>
<p> Colin Watson wrote this manual page, originally for the Debian Project. </p>
<h2>Index</h2>
