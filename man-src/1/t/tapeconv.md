---
title: "tapeconv(1)"
name: "tapeconv"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tapeconv/"
description: "tapeconv – Sinclair ZX Spectrum tape file converter"
---

<h2 class="name">NAME</h2>
<p> tapeconv &#8211; Sinclair ZX Spectrum tape file converter </p>
<h2>SYNOPSIS</h2>
<p> <code>tapeconv</code> [ -a <i>archive info TZX</i> ] [ -b ] [ -s <i>SCR loading screen</i> ] [ -i <i>JPG or GIF inlay image</i> ] <i>infile outfile</i></p>
<h2>DESCRIPTION</h2>
<p> tapeconv converts between ZX Spectrum tape images.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-a <i>archive info TZX</i></p>
<dd> causes the TZX supplied to be scanned for a Archive Info block containing author, year of relase etc. information about the file and then added to the output TZX.</p>
<dt>[ -b ]</p>
<dd> causes the output TZX to be stripped of any concatenation blocks that get created when appending TZX files.</p>
<dt>[ -s <i>SCR loading screen</i> ]</p>
<dd> causes the supplied .scr format file to be attached to the TZX as a Custom Info block marked as a loading screen.</p>
<dt>[ -i <i>JPG or GIF inlay image</i> ]</p>
<dd> causes the supplied .gif or .jpg format file to be attached to the TZX as a Custom Info block marked as a cassette inlay.</p>
<dt><i>infile</i></p>
<dd> specifies the tape file to be converted. This file can be in any of the tape formats supported by <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3).</p>
<dt><i>outfile</i></p>
<dd> specifies the output tape file. The format will be determined by the file extension and can be in any of the formats <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3) supports for output.</dl>
<h2>BUGS</h2>
<p> None known.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fuse/">fuse</a></i>(1), <i><a href="/docs/linux/man/1-fuse-utils/">fuse-utils</a></i>(1), <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3), <i><a href="/docs/linux/man/1-listbasic/">listbasic</a></i>(1), <i><a href="/docs/linux/man/1-tzxlist/">tzxlist</a></i>(1) </p>
<p> The comp.sys.sinclair Spectrum FAQ, at<br />
 <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/index.html">http://www.worldofspectrum.org/faq/index.html</a></i>.</p>
<h2>AUTHOR</h2>
<p> Philip Kendall (philip-fuse [at] shadowmagic.org.uk). </p>
<h2>Index</h2>
