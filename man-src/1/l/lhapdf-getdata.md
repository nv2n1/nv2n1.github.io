---
title: "lhapdf-getdata(1)"
name: "lhapdf-getdata"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lhapdf-getdata/"
description: "lhapdf-getdata – Get PDF sets from the LHAPDF repository"
---

<h2>NAME</h2>
<p> lhapdf-getdata &#8211; Get PDF sets from the LHAPDF repository</p>
<h2>SYNOPSIS</h2>
<p> <code>lhapdf-getdata</code> [<i>&#8211;main</i>] [<i>&#8211;all</i>] [<i>&#8211;repo=URL</i>] [<i>&#8211;dest=DEST</i>] [<i>&#8211;dryrun</i>] &lt;name|number&gt; [&lt;name|number&gt; &#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd></dl>
<p> Grab PDF grid and param files from the LHAPDF repository and install them into the local LHAPDF data directory.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>&#8211;repo</code>=<i>URL</i></p>
<dd> Base URL of online sets repository (<a rel="nofollow" href="http://www.hepforge.org/archive/lhapdf/pdfsets/current)">http://www.hepforge.org/archive/lhapdf/pdfsets/current)</a></p>
<dt><code>&#8211;dest</code>=<i>DEST</i></p>
<dd> PDF sets directory to install to (/usr/share/lhapdf/PDFsets)</p>
<dt><code>&#8211;all</code></p>
<dd> Get ALL sets (this will be hundreds of megabytes&#8230; be careful!)</p>
<dt><code>&#8211;list</code></p>
<dd> Just list available files</p>
<dt><code>&#8211;force</code></p>
<dd> Overwrite existing files</p>
<dt><code>&#8211;dryrun</code></p>
<dd> Don&#8217;t actually do any downloading</p>
<dt><code>-Q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress normal messages</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Add extra debug messages</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Show all available sets:</p>
<dd> lhapdf-getdata <code>&#8211;list</code></p>
<dt>Get all NNPDF PDFs with pattern matching:</p>
<dd> lhapdf-getdata NNPDF</p>
<dt>Get CTEQ6L1, CTEQ66, MRST-S LO* and LO** PDFs with pattern matching:</p>
<dd> lhapdf-getdata CTEQ6ll CTEQ66 lomod MCal</p>
<dt>Get MSTW2008 68% confidence PDF by full name:</p>
<dd> lhapdf-getdata MSTW2008lo68cl.LHgrid</p>
<dt>See how much downloading would be involved in getting all PDF sets:</p>
<dd> lhapdf-getdata <code>&#8211;all</code> <code>&#8211;dryrun</code></p>
<dt>I&#8217;m hardcore, give me the whole collection:</p>
<dd> lhapdf-getdata <code>&#8211;all</code></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Lifeng Sun &lt;lifongsun [at] gmail.com&gt; for the Debian system (but may be used by others). </p>
<h2>Index</h2>
