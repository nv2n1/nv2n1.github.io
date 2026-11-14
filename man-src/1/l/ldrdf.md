---
title: "ldrdf(1)"
name: "ldrdf"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldrdf/"
description: "ldrdf – link RDOFF objects and libraries produced by rdflib(1)"
---

<h2>NAME</h2>
<p> ldrdf &#8211; link RDOFF objects and libraries produced by <a href="/docs/linux/man/1-rdflib/">rdflib</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>ldrdf</code> [-o <i>output-file</i>] <i>object-file</i>&#8230; [-l<i>library</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>ldrdf</code> is a version of unix <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) (or DOS LINK) for use with RDOFF files. It is capable of linking RDOFF objects, and libraries produced with the <code><a href="/docs/linux/man/1-rdflib/">rdflib</a></code>(1) utility. </p>
<p> Libraries must be specified with their path as no search is performed. Modules in libraries are not linked to the program unless they are referred to.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-o <i>output-file</i></p>
<dd> Specify an output file. The default output filename is &#8216;<i>aout.rdx</i>&#8216;.</p>
<dt>-v</p>
<dd> Increase verbosity level. Currently 4 verbosity levels are available: default (which only prints error information), normal (which prints information about the produced object, -v), medium (which prints information about what the program is doing, -v -v) and high (which prints all available information, -v -v -v).</p>
<dt>-p</p>
<dd> Change alignment value to which multiple segments combigned into a single segment should be aligned (must be either 1, 2, 4, 8, 16, 32 or 256; default is 16).</dl>
<h2>AUTHORS</h2>
<p> Julian Hall &lt;jules [at] earthcorp.com&gt;. </p>
<p> This manual page was written by Matej Vela &lt;vela [at] debian.org&gt;. </p>
<h2>Index</h2>
