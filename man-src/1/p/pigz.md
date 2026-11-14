---
title: "pigz(1)"
name: "pigz"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pigz/"
description: "pigz, unpigz – compress or expand files"
---

<h2 class="name">NAME</h2>
<p> pigz, unpigz &#8211; compress or expand files </p>
<h2>SYNOPSIS</h2>
<p> <code>pigz</code> [<code> -cdfhikKlLmMnNqrRtz0..9,11 </code>] [ <code>-b</code> <i>blocksize</i> ] [ <code>-p</code> <i>threads</i> ] [ <code>-S</code> <i>suffix</i> ] [ <i>name &#8230;</i> ]<br />
 <code>unpigz</code> [<code> -cfhikKlLmMnNqrRtz </code>] [ <code>-b</code> <i>blocksize</i> ] [ <code>-p</code> <i>threads</i> ] [ <code>-S</code> <i>suffix</i> ] [ <i>name &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Pigz</i> compresses using threads to make use of multiple processors and cores. The input is broken up into 128 KB chunks with each compressed in parallel. The individual check value for each chunk is also calculated in parallel. The compressed data is written in order to the output, and a combined check value is calculated from the individual check values. </p>
<p> The compressed data format generated is in the gzip, zlib, or single-entry zip format using the deflate compression method. The compression produces partial raw deflate streams which are concatenated by a single write thread and wrapped with the appropriate header and trailer, where the trailer contains the combined check value. </p>
<p> Each partial raw deflate stream is terminated by an empty stored block (using the Z_SYNC_FLUSH option of zlib), in order to end that partial bit stream at a byte boundary. That allows the partial streams to be concatenated simply as sequences of bytes. This adds a very small four to five byte overhead to the output for each input chunk. </p>
<p> The default input block size is 128K, but can be changed with the <code>-b</code> option. The number of compress threads is set by default to the number of online processors, which can be changed using the <code>-p</code> option. Specifying <code>-p 1</code> avoids the use of threads entirely. </p>
<p> The input blocks, while compressed independently, have the last 32K of the previous block loaded as a preset dictionary to preserve the compression effectiveness of deflating in a single thread. This can be turned off using the <code>-i</code> or <code>&#8211;independent</code> option, so that the blocks can be decompressed independently for partial error recovery or for random access. This also inserts an extra empty block to flag independent blocks by prefacing each with the nine-byte sequence (in hex): 00 00 FF FF 00 00 00 FF FF. </p>
<p> Decompression can&#8217;t be parallelized, at least not without specially prepared deflate streams for that purpose. As a result, <i>pigz</i> uses a single thread (the main thread) for decompression, but will create three other threads for reading, writing, and check calculation, which can speed up decompression under some circumstances. Parallel decompression can be turned off by specifying one process ( <code>-dp 1</code> or <code>-tp 1</code> ). </p>
<p> All options on the command line are processed before any names are processed. If no names are provided on the command line, or if &quot;-&quot; is given as a name (but not after &quot;&#8211;&quot;), then the input is taken from stdin. </p>
<p> Compressed files can be restored to their original form using <i>pigz -d</i> or <i>unpigz.</i> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-# &#8211;fast &#8211;best</code></p>
<dd> Regulate the speed of compression using the specified digit <i>#</i>, where <code>-1</code> or <code>&#8211;fast</code> indicates the fastest compression method (less compression) and <code>-9</code> or <code>&#8211;best</code> indicates the slowest compression method (best compression). <code>-0</code> is no compression. <code>-11</code> gives a few percent better compression at a severe cost in execution time, using the zopfli algorithm by Jyrki Alakuijala. The default is <code>-6.</code></p>
<dt><code>-A &#8211;alias xxx</code></p>
<dd> Use xxx as the name for any &#8211;zip entry from stdin (the default name is &quot;-&quot;).</p>
<dt><code>-b &#8211;blocksize mmm</code></p>
<dd> Set compression block size to mmmK (default 128KiB).</p>
<dt><code>-c &#8211;stdout &#8211;to-stdout</code></p>
<dd> Write all processed output to stdout (won&#8217;t delete).</p>
<dt><code>-C &#8211;comment ccc</code></p>
<dd> Include the provided comment in the gzip header or zip central file header.</p>
<dt><code>-d &#8211;decompress &#8211;uncompress</code></p>
<dd> Decompress the compressed input.</p>
<dt><code>-f &#8211;force</code></p>
<dd> Force overwrite, compress .gz, links, and to terminal.</p>
<dt><code>-h &#8211;help</code></p>
<dd> Display a help screen and quit.</p>
<dt><code>-H &#8211;huffman</code></p>
<dd> Compress using the Huffman-only strategy.</p>
<dt><code>-i &#8211;independent</code></p>
<dd> Compress blocks independently for damage recovery.</p>
<dt><code>-k &#8211;keep</code></p>
<dd> Do not delete original file after processing.</p>
<dt><code>-K &#8211;zip</code></p>
<dd> Compress to PKWare zip (.zip) single entry format.</p>
<dt><code>-l &#8211;list</code></p>
<dd> List the contents of the compressed input.</p>
<dt><code>-L &#8211;license</code></p>
<dd> Display the <i>pigz</i> license and quit.</p>
<dt><code>-m &#8211;no-time</code></p>
<dd> Do not store or restore the modification time. -Nm will store or restore the name, but not the modification time. Note that the order of the options is important.</p>
<dt><code>-M &#8211;time</code></p>
<dd> Store or restore the modification time. -nM will store or restore the modification time, but not the name. Note that the order of the options is important.</p>
<dt><code>-n &#8211;no-name</code></p>
<dd> Do not store or restore the file name or the modification time. This is the default when decompressing. When the file name is not restored from the header, the name of the compressed file with the suffix stripped is the name of the decompressed file. When the modification time is not restored from the header, the modification time of the compressed file is used (not the current time).</p>
<dt><code>-N &#8211;name</code></p>
<dd> Store or restore both the file name and the modification time. This is the default when compressing.</p>
<dt><code>-p &#8211;processes n</code></p>
<dd> Allow up to n processes (default is the number of online processors)</p>
<dt><code>-q &#8211;quiet &#8211;silent</code></p>
<dd> Print no messages, even on error.</p>
<dt><code>-r &#8211;recursive</code></p>
<dd> Process the contents of all subdirectories.</p>
<dt><code>-R &#8211;rsyncable</code></p>
<dd> Input-determined block locations for rsync.</p>
<dt><code>-S &#8211;suffix .sss</code></p>
<dd> Use suffix .sss instead of .gz (for compression).</p>
<dt><code>-t &#8211;test</code></p>
<dd> Test the integrity of the compressed input.</p>
<dt><code>-U &#8211;rle</code></p>
<dd> Compress using the run length encoding strategy.</p>
<dt><code>-v &#8211;verbose</code></p>
<dd> Provide more verbose output.</p>
<dt><code>-V &#8211;version</code></p>
<dd> Show the version of pigz. -vV also shows the zlib version.</p>
<dt><code>-z &#8211;zlib</code></p>
<dd> Compress to zlib (.zz) instead of gzip format.</p>
<dt><code>&#8212;</code></p>
<dd> All arguments after &quot;&#8211;&quot; are treated as file names (for names that start with &quot;-&quot;)</p>
<dt>These options are unique to the -11 compression level:</p>
<dd>
<dt><code>-F &#8211;first</code></p>
<dd> Do iterations first, before block split (default is last).</p>
<dt><code>-I, &#8211;iterations n</code></p>
<dd> Number of iterations for optimization (default 15).</p>
<dt><code>-J, &#8211;maxsplits n</code></p>
<dd> Maximum number of split blocks (default 15).</p>
<dt><code>-O &#8211;oneblock</code></p>
<dd> Do not split into smaller blocks (default is block splitting).</dl>
<h2>COPYRIGHT NOTICE</h2>
<p> This software is provided &#8216;as-is&#8217;, without any express or implied warranty. In no event will the author be held liable for any damages arising from the use of this software. </p>
<p> Copyright (C) 2007-2021 Mark Adler &lt;madler [at] alumni.caltech.edu&gt; </p>
<h2>Index</h2>
