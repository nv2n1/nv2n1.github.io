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
</dl>
<p> Grab PDF grid and param files from the LHAPDF repository and install them into the local LHAPDF data directory.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>&#8211;repo</code>=<i>URL</i></dt>
<dd> Base URL of online sets repository (<a rel="nofollow" href="http://www.hepforge.org/archive/lhapdf/pdfsets/current)">http://www.hepforge.org/archive/lhapdf/pdfsets/current)</a></dd>
<dt><code>&#8211;dest</code>=<i>DEST</i></dt>
<dd> PDF sets directory to install to (/usr/share/lhapdf/PDFsets)</dd>
<dt><code>&#8211;all</code></dt>
<dd> Get ALL sets (this will be hundreds of megabytes&#8230; be careful!)</dd>
<dt><code>&#8211;list</code></dt>
<dd> Just list available files</dd>
<dt><code>&#8211;force</code></dt>
<dd> Overwrite existing files</dd>
<dt><code>&#8211;dryrun</code></dt>
<dd> Don&#8217;t actually do any downloading</dd>
<dt><code>-Q</code>, <code>&#8211;quiet</code></dt>
<dd> Suppress normal messages</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd> Add extra debug messages</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Show all available sets:</dt>
<dd> lhapdf-getdata <code>&#8211;list</code></dd>
<dt>Get all NNPDF PDFs with pattern matching:</dt>
<dd> lhapdf-getdata NNPDF</dd>
<dt>Get CTEQ6L1, CTEQ66, MRST-S LO* and LO** PDFs with pattern matching:</dt>
<dd> lhapdf-getdata CTEQ6ll CTEQ66 lomod MCal</dd>
<dt>Get MSTW2008 68% confidence PDF by full name:</dt>
<dd> lhapdf-getdata MSTW2008lo68cl.LHgrid</dd>
<dt>See how much downloading would be involved in getting all PDF sets:</dt>
<dd> lhapdf-getdata <code>&#8211;all</code> <code>&#8211;dryrun</code></dd>
<dt>I&#8217;m hardcore, give me the whole collection:</dt>
<dd> lhapdf-getdata <code>&#8211;all</code></dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Lifeng Sun &lt;lifongsun [at] gmail.com&gt; for the Debian system (but may be used by others). </p>
