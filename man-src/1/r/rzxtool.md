---
title: "rzxtool(1)"
name: "rzxtool"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rzxtool/"
description: "rzxtool – Modify Sinclair ZX Spectrum input recording files"
---

<h2 class="name">NAME</h2>
<p> rzxtool &#8211; Modify Sinclair ZX Spectrum input recording files </p>
<h2>SYNOPSIS</h2>
<p> <code>rzxtool</code> [-d<i>block number</i>] [-e<i>block number</i>,<i>filename</i>] [-i<i>block number</i>,<i>filename</i>] [-u] <i>rzxfile</i> [<i>outfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> rzxtool allows some simple modifications to be made to Sinclair ZX Spectrum input recording files: blocks can be removed, snapshot data can be extracted or snapshots can be inserted into the file. The file can also be uncompressed.</p>
<h2>OPTIONS</h2>
<p> -d<i>block number</i></p>
<dl>
<dt>
<dd> The block number specified will be deleted from the file. Block numbers start at zero and ignore any &quot;creator information&quot; blocks in the file. The modified file will be written to <i>outfile</i>.</dl>
<p> -e<i>block number</i>,<i>filename</i></p>
<dl>
<dt>
<dd> The snapshot in the specified block number will be written to the specified filename. All snapshot formats supported by <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3) are available.</dl>
<p> -i<i>block number</i>,<i>filename</i></p>
<dl>
<dt>
<dd> The snapshot specified in <i>filename</i> will be added to the file at the position specified by <i>block number</i>.</dl>
<p> -u</p>
<dl>
<dt>
<dd> When outputting an RZX file, this option causes the input recording data to be output uncompressed; if this option is not given, the data will be compressed using <i><a href="/docs/linux/man/3-zlib/">zlib</a></i>(3).</dl>
<p> <i>rzxfile</i></p>
<dl>
<dt>
<dd> specifies an input recording file whose contents are to be modified.</dl>
<p> <i>outfile</i></p>
<dl>
<dt>
<dd> specifies where the modified input file should be written.</dl>
<h2>BUGS</h2>
<p> None known</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fuse/">fuse</a></i>(1), <i><a href="/docs/linux/man/1-fuse-utils/">fuse-utils</a></i>(1), <i><a href="/docs/linux/man/1-rzxcheck/">rzxcheck</a></i>(1), <i><a href="/docs/linux/man/1-rzxdump/">rzxdump</a></i>(1), <i><a href="/docs/linux/man/3-zlib/">zlib</a></i>(3) </p>
<p> The comp.sys.sinclair Spectrum FAQ, at<br />
 <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/index.html">http://www.worldofspectrum.org/faq/index.html</a></i>.</p>
<h2>AUTHOR</h2>
<p> Philip Kendall (philip-fuse [at] shadowmagic.org.uk). </p>
<h2>Index</h2>
