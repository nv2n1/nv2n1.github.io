---

title: "rrdfirst(1)"
name: "rrdfirst"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdfirst/"
description: "rrdfirst – Return the date of the first data sample in an RRA within an RRD"
---

<p> rrdfirst &#8211; Return the date of the first data sample in an RRA within an RRD </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>first</code> <i>filename</i> [<i>&#8211;rraindex number</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>first</code> function returns the UNIX timestamp of the first data sample entered into the specified RRA of the RRD file.</p>
<dl>
<dt><i>filename</i></dt>
<dd> The name of the <code>RRD</code> that contains the data.</dd>
<dt><i>&#8211;rraindex number</i></dt>
<dd> The index number of the <code>RRA</code> that is to be examined. If not specified, the index defaults to zero. <code>RRA</code> index numbers can be determined through <code>rrdtool info</code>.</dd></dl>
<h2>AUTHOR</h2>
<p> Burton Strauss &lt;Burton [at] ntopSupport.com&gt; </p>
