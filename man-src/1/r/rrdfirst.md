---
title: "rrdfirst(1)"
name: "rrdfirst"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdfirst/"
description: "rrdfirst – Return the date of the first data sample in an RRA within an RRD"
---

<h2 class="name">NAME</h2>
<p> rrdfirst &#8211; Return the date of the first data sample in an RRA within an RRD </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>first</code> <i>filename</i> [<i>&#8211;rraindex number</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>first</code> function returns the <font SIZE="-1">UNIX</font> timestamp of the first data sample entered into the specified <font SIZE="-1">RRA</font> of the <font SIZE="-1">RRD</font> file.</p>
<dl>
<dt><i>filename</i></p>
<dd> The name of the <font SIZE="-1"><code>RRD</code></font> that contains the data.</p>
<dt><i>&#8211;rraindex number</i></p>
<dd> The index number of the <font SIZE="-1"><code>RRA</code></font> that is to be examined. If not specified, the index defaults to zero. <font SIZE="-1"><code>RRA</code></font> index numbers can be determined through <code>rrdtool info</code>.</dl>
<h2>AUTHOR</h2>
<p> Burton Strauss &lt;Burton [at] ntopSupport.com&gt; </p>
<h2>Index</h2>
