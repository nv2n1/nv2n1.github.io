---
title: "rrdrestore(1)"
name: "rrdrestore"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdrestore/"
description: "rrdrestore – Restore the contents of an RRD from its XML dump format"
---

<h2 class="name">NAME</h2>
<p> rrdrestore &#8211; Restore the contents of an RRD from its XML dump format </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>restore</code> <i>filename.xml</i> <i>filename.rrd</i> [<code>&#8211;range-check</code>|<code>-r</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>restore</code> function reads the <font SIZE="-1">XML</font> representation of an <font SIZE="-1">RRD</font> and converts it to the native <font SIZE="-1"><code>RRD</code></font> format.</p>
<dl>
<dt><i>filename.xml</i></p>
<dd> The name of the <font SIZE="-1"><code>XML</code></font> file you want to restore.</p>
<dt><i>filename.rrd</i></p>
<dd> The name of the <font SIZE="-1"><code>RRD</code></font> to restore.</p>
<dt><code>&#8211;range-check</code>|<code>-r</code></p>
<dd> Make sure the values in the RRAs do not exceed the limits defined for the various data sources.</p>
<dt><code>&#8211;force-overwrite</code>|<code>-f</code></p>
<dd> Allows <code>RRDtool</code> to overwrite the destination <font SIZE="-1"><code>RRD</code></font>.</dl>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
