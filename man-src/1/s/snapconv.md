---
title: "snapconv(1)"
name: "snapconv"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snapconv/"
description: "snapconv – Sinclair ZX Spectrum snapshot converter"
---

<h2 class="name">NAME</h2>
<p> snapconv &#8211; Sinclair ZX Spectrum snapshot converter </p>
<h2>SYNOPSIS</h2>
<p> <code>snapconv</code> [ -c ] [ -n ] <i>infile outfile</i></p>
<h2>DESCRIPTION</h2>
<p> snapconv converts between ZX Spectrum snapshot files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-c</i></p>
<dd> specifies that all data in the output snapshot should be compressed, even if that compression will result in a bigger file than if some data is left uncompressed. This helps compatibility with some buggy programs that can only read entirely compressed .z80 files.</p>
<dt><i>-n</i></p>
<dd> specifies that the output snapshot should be uncompressed.</p>
<dt><i>infile</i></p>
<dd> specifies the snapshot to be converted. This file can be in any of the snapshot formats supported by <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3).</p>
<dt><i>outfile</i></p>
<dd> specifies the output snapshot. The format will be determined by the file extension and can be in any of the formats <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3) supports for output.</dl>
<h2>BUGS</h2>
<p> None known.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fuse/">fuse</a></i>(1), <i><a href="/docs/linux/man/1-fuse-utils/">fuse-utils</a></i>(1), <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3), <i><a href="/docs/linux/man/1-listbasic/">listbasic</a></i>(1), <i><a href="/docs/linux/man/1-snap2tzx/">snap2tzx</a></i>(1) </p>
<p> The comp.sys.sinclair Spectrum FAQ, at<br />
 <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/index.html">http://www.worldofspectrum.org/faq/index.html</a></i>.</p>
<h2>AUTHOR</h2>
<p> Philip Kendall (philip-fuse [at] shadowmagic.org.uk). </p>
<h2>Index</h2>
