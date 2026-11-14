---
title: "ncgm2cgm(1)"
name: "ncgm2cgm"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncgm2cgm/"
description: "cgm2ncgm ncgm2cgm – filter NCAR CGM to/from vanilla CGM"
---

<h2>NAME</h2>
<p> cgm2ncgm ncgm2cgm &#8211; filter <code>NCAR CGM</code> to/from vanilla <code>CGM</code></p>
<h2>SYNOPSIS</h2>
<p> <code>ncgm2cgm</code> [&nbsp;<wbr><code>-s&nbsp;<wbr></code><i>output block size</i>&nbsp;<wbr>] [&nbsp;<wbr><code>-V&nbsp;<wbr>] </p>
<p> cgm2ncgm</code> [&nbsp;<wbr><code>-s&nbsp;<wbr></code><i>input block size</i>&nbsp;<wbr>] [&nbsp;<wbr><code>-V&nbsp;<wbr>] </p>
<p> </code></p>
<h2>DESCRIPTION</h2>
<p> <code>ncgm2cgm</code> and <code>cgm2ncgm</code> are filters for converting back and forth between <code>NCAR Computer Graphics Metafile</code> (CGM) and vanilla CGM. <code>ncgm2cgm</code> strips the wrapper from NCAR CGM records while cgm2ncgm restores it. I/O is done from standard in/out respectively. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code><i>&nbsp;<wbr>size</i></p>
<dd> Set block size in bytes for reads/writes of vanilla CGM. The default blocking factor is 1024.</p>
<dt><code>-V</code></p>
<dd> Print the version number and then exit.</dl>
<h2>SEE ALSO</h2>
<pre>
<i>ISO/DIS 8632 CGM Functional Specification</i> (Nov. 1985)
</pre>
<h2>BUGS</h2>
<p> Some <i>vanilla</i> metafile interpretors take advantage of shortcuts provided by their CGM generators. In effect, they are not <i>true</i> CGM interpretors. Although it will still be possible to convert these metafiles to NCAR format that may be interpreted by NCAR Graphics translators. It may not be the case that the aforementioned interpreters will be able to translate <i>true</i> vanilla metafiles, such as produced by <code>ncgm2cgm.</code></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
