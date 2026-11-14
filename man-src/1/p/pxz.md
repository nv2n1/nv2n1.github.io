---
title: "pxz(1)"
name: "pxz"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pxz/"
description: "pxz – Parallel LZMA compressor compatible with XZ."
---

<h2>NAME</h2>
<p> pxz &#8211; Parallel LZMA compressor compatible with XZ.</p>
<h2>SYNOPSIS</h2>
<p> <code>pxz</code> [<code>options</code>]&#8230; [<i>file</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>pxz</code> is a compression utility that takes advantage of running XZ compression simultaneously on different parts of an input file on multiple cores and processors. This significantly speeds up compression time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-v</i></p>
<dd> Be verbose.</p>
<dt><i>-h, &#8211;help</i></p>
<dd> Display help.</p>
<dt><i>-f, &#8211;force</i></p>
<dd> Force operation.</p>
<dt><i>-c, &#8211;stdout</i></p>
<dd> Write results to standard output.</p>
<dt><i>-k, &#8211;keep</i></p>
<dd> Write results to standard output.</p>
<dt><i>-T, &#8211;threads</i></p>
<dd> Maximal number of threads to run simultaneously.</p>
<dt><i>-D, &#8211;context-size</i></p>
<dd> Context size per one thread specified as a multiple of dictionary size for active compression level.</p>
<dt><i>-V, &#8211;version</i></p>
<dd> Display version of PXZ.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>pxz file1 file2</p>
<dd> Compress file1 and file2 to file1.xz and file2.xz using default settings.</p>
<dt>pxz -T4 file1</p>
<dd> Compress file1 with default compression and maximum of 4 threads.</p>
<dt>pxz -k -9 file1</p>
<dd> Use maximal compression and keep the original file1, use default number of threads.</p>
<dt>pxz -f -T4 file1</p>
<dd> Compress file with default compression and with 4 threads.</p>
<dt>pxz -kvf -3 -T8 file1</p>
<dd> Use -3 compression, keep the original file, use 8 threads and show progress.</p>
<dt>tar Oc dir1 | pxz -D 12 -cv &#8211; &gt; dir1.tar.xz</p>
<dd> Move dir1 into tar, then compress it with the context of 12 sizes of dictionary per thread, show progress and write result to dir1.tar.xz.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Jindrich Novy &lt;jnovy [at] users.sourceforge.net&gt;</p>
<h2>BUGS</h2>
<p> Report bugs via <a rel="nofollow" href="http://bugzilla.redhat.com/bugzilla/">http://bugzilla.redhat.com/bugzilla/</a> </p>
<h2>Index</h2>
