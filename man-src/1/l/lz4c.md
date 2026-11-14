---
title: "lz4c(1)"
name: "lz4c"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lz4c/"
description: "lz4 – lz4, unlz4, lz4cat – Compress or decompress .lz4 files"
---

<h2 class="name">NAME</h2>
<p> <code>lz4</code> &#8211; lz4, unlz4, lz4cat &#8211; Compress or decompress .lz4 files </p>
<h2>SYNOPSIS</h2>
<p> <code>lz4</code> [<i>OPTIONS</i>] [-|INPUT-FILE] <i>OUTPUT-FILE</i> </p>
<p> <code>unlz4</code> is equivalent to <code>lz4 -d</code> </p>
<p> <code>lz4cat</code> is equivalent to <code>lz4 -dcfm</code> </p>
<p> When writing scripts that need to decompress files, it is recommended to always use the name <code>lz4</code> with appropriate arguments (<code>lz4 -d</code> or <code>lz4 -dc</code>) instead of the names <code>unlz4</code> and <code>lz4cat</code>.</p>
<h2>DESCRIPTION</h2>
<p> <code>lz4</code> is an extremely fast lossless compression algorithm, based on <code>byte-aligned LZ77</code> family of compression scheme. <code>lz4</code> offers compression speeds of 400 MB/s per core, linearly scalable with multi-core CPUs. It features an extremely fast decoder, with speed in multiple GB/s per core, typically reaching RAM speed limit on multi-core systems. The native file format is the <code>.lz4</code> format.</p>
<h3>Difference between lz4 and gzip</h3>
<p> <code>lz4</code> supports a command line syntax similar <i>but not identical</i> to <code><a href="/docs/linux/man/1-gzip/">gzip</a>(1)</code>. Differences are :</p>
<dl>
<dt>&bull;</p>
<dd> <code>lz4</code> compresses a single file by default (see <code>-m</code> for multiple files)</p>
<dt>&bull;</p>
<dd> <code>lz4 file1 file2</code> means : compress file1 <i>into</i> file2</p>
<dt>&bull;</p>
<dd> <code>lz4 file.lz4</code> will default to decompression (use <code>-z</code> to force compression)</p>
<dt>&bull;</p>
<dd> <code>lz4</code> preserves original files</p>
<dt>&bull;</p>
<dd> <code>lz4</code> shows real-time notification statistics during compression or decompression of a single file (use <code>-q</code> to silence them)</p>
<dt>&bull;</p>
<dd> When no destination is specified, result is sent on implicit output, which depends on <code>stdout</code> status. When <code>stdout</code> <i>is Not the console</i>, it becomes the implicit output. Otherwise, if <code>stdout</code> is the console, the implicit output is <code>filename.lz4</code>.</p>
<dt>&bull;</p>
<dd> It is considered bad practice to rely on implicit output in scripts. because the script&#8217;s environment may change. Always use explicit output in scripts. <code>-c</code> ensures that output will be <code>stdout</code>. Conversely, providing a destination name, or using <code>-m</code> ensures that the output will be either the specified name, or <code>filename.lz4</code> respectively.</p>
<dt>
<dd></dl>
<p> Default behaviors can be modified by opt-in commands, detailed below.</p>
<dl>
<dt>&bull;</p>
<dd> <code>lz4 -m</code> makes it possible to provide multiple input filenames, which will be compressed into files using suffix <code>.lz4</code>. Progress notifications become disabled by default (use <code>-v</code> to enable them). This mode has a behavior which more closely mimics <code>gzip</code> command line, with the main remaining difference being that source files are preserved by default.</p>
<dt>&bull;</p>
<dd> Similarly, <code>lz4 -m -d</code> can decompress multiple <code>*.lz4</code> files.</p>
<dt>&bull;</p>
<dd> It&#8217;s possible to opt-in to erase source files on successful compression or decompression, using <code>&#8211;rm</code> command.</p>
<dt>&bull;</p>
<dd> Consequently, <code>lz4 -m &#8211;rm</code> behaves the same as <code>gzip</code>.</p>
<dt>
<dd></dl>
<h3>Concatenation of .lz4 files</h3>
<p> It is possible to concatenate <code>.lz4</code> files as is. <code>lz4</code> will decompress such files as if they were a single <code>.lz4</code> file. For example:</p>
<dl>
<dt>
<dd>
<pre>
lz4 file1  &gt; foo.lz4
lz4 file2 &gt;&gt; foo.lz4
</pre>
<dt>
<dd></dl>
<p> Then <code>lz4cat foo.lz4</code> is equivalent to <code>cat file1 file2</code>.</p>
<h2>OPTIONS</h2>
<h3>Short commands concatenation</h3>
<p> In some cases, some options can be expressed using short command <code>-x</code> or long command <code>&#8211;long-word</code>. Short commands can be concatenated together. For example, <code>-d -c</code> is equivalent to <code>-dc</code>. Long commands cannot be concatenated. They must be clearly separated by a space.</p>
<h3>Multiple commands</h3>
<p> When multiple contradictory commands are issued on a same command line, only the latest one will be applied.</p>
<h3>Operation mode</h3>
<dl>
<dt><code>-z</code> <code>&#8211;compress</code></p>
<dd> Compress. This is the default operation mode when no operation mode option is specified, no other operation mode is implied from the command name (for example, <code>unlz4</code> implies <code>&#8211;decompress</code>), nor from the input file name (for example, a file extension <code>.lz4</code> implies <code>&#8211;decompress</code> by default). <code>-z</code> can also be used to force compression of an already compressed <code>.lz4</code> file.</p>
<dt><code>-d</code> <code>&#8211;decompress</code> <code>&#8211;uncompress</code></p>
<dd> Decompress. <code>&#8211;decompress</code> is also the default operation when the input filename has an <code>.lz4</code> extension.</p>
<dt><code>-t</code> <code>&#8211;test</code></p>
<dd> Test the integrity of compressed <code>.lz4</code> files. The decompressed data is discarded. No files are created nor removed.</p>
<dt><code>-b#</code></p>
<dd> Benchmark mode, using <code>#</code> compression level.</p>
<dt><code>&#8211;list</code></p>
<dd> List information about .lz4 files. note : current implementation is limited to single-frame .lz4 files.</dl>
<h3>Operation modifiers</h3>
<dl>
<dt><code>-#</code></p>
<dd> Compression level, with # being any value from 1 to 12. Higher values trade compression speed for compression ratio. Values above 12 are considered the same as 12. Recommended values are 1 for fast compression (default), and 9 for high compression. Speed/compression trade-off will vary depending on data to compress. Decompression speed remains fast at all settings.</p>
<dt><code>&#8211;fast[=#]</code></p>
<dd> Switch to ultra-fast compression levels. The higher the value, the faster the compression speed, at the cost of some compression ratio. If <code>=#</code> is not present, it defaults to <code>1</code>. This setting overrides compression level if one was set previously. Similarly, if a compression level is set after <code>&#8211;fast</code>, it overrides it.</p>
<dt><code>&#8211;best</code></p>
<dd> Set highest compression level. Same as -12.</p>
<dt><code>&#8211;favor-decSpeed</code></p>
<dd> Generate compressed data optimized for decompression speed. Compressed data will be larger as a consequence (typically by ~0.5%), while decompression speed will be improved by 5-20%, depending on use cases. This option only works in combination with very high compression levels (&gt;=10).</p>
<dt><code>-D dictionaryName</code></p>
<dd> Compress, decompress or benchmark using dictionary <i>dictionaryName</i>. Compression and decompression must use the same dictionary to be compatible. Using a different dictionary during decompression will either abort due to decompression error, or generate a checksum error.</p>
<dt><code>-f</code> <code>&#8211;[no-]force</code></p>
<dd> This option has several effects:</p>
<dt>
<dd> If the target file already exists, overwrite it without prompting.</p>
<dt>
<dd> When used with <code>&#8211;decompress</code> and <code>lz4</code> cannot recognize the type of the source file, copy the source file as is to standard output. This allows <code>lz4cat &#8211;force</code> to be used like <code>cat (1)</code> for files that have not been compressed with <code>lz4</code>.</p>
<dt><code>-c</code> <code>&#8211;stdout</code> <code>&#8211;to-stdout</code></p>
<dd> Force write to standard output, even if it is the console.</p>
<dt><code>-m</code> <code>&#8211;multiple</code></p>
<dd> Multiple input files. Compressed file names will be appended a <code>.lz4</code> suffix. This mode also reduces notification level. Can also be used to list multiple files. <code>lz4 -m</code> has a behavior equivalent to <code>gzip -k</code> (it preserves source files by default).</p>
<dt><code>-r</code></p>
<dd> operate recursively on directories. This mode also sets <code>-m</code> (multiple input files).</p>
<dt><code>-B#</code></p>
<dd> Block size [4-7](default : 7)<br />
 <code>-B4</code>= 64KB ; <code>-B5</code>= 256KB ; <code>-B6</code>= 1MB ; <code>-B7</code>= 4MB</p>
<dt><code>-BI</code></p>
<dd> Produce independent blocks (default)</p>
<dt><code>-BD</code></p>
<dd> Blocks depend on predecessors (improves compression ratio, more noticeable on small blocks)</p>
<dt><code>&#8211;[no-]frame-crc</code></p>
<dd> Select frame checksum (default:enabled)</p>
<dt><code>&#8211;[no-]content-size</code></p>
<dd> Header includes original size (default:not present)<br />
 Note : this option can only be activated when the original size can be determined, hence for a file. It won&#8217;t work with unknown source size, such as stdin or pipe.</p>
<dt><code>&#8211;[no-]sparse</code></p>
<dd> Sparse mode support (default:enabled on file, disabled on stdout)</p>
<dt><code>-l</code></p>
<dd> Use Legacy format (typically for Linux Kernel compression)<br />
 Note : <code>-l</code> is not compatible with <code>-m</code> (<code>&#8211;multiple</code>) nor <code>-r</code></dl>
<h3>Other options</h3>
<dl>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Verbose mode</p>
<dt><code>-q</code> <code>&#8211;quiet</code></p>
<dd> Suppress warnings and real-time statistics; specify twice to suppress errors too</p>
<dt><code>-h</code> <code>-H</code> <code>&#8211;help</code></p>
<dd> Display help/long help and exit</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd> Display Version number and exit</p>
<dt><code>-k</code> <code>&#8211;keep</code></p>
<dd> Preserve source files (default behavior)</p>
<dt><code>&#8211;rm</code></p>
<dd> Delete source files on successful compression or decompression</p>
<dt><code>&#8212;</code></p>
<dd> Treat all subsequent arguments as files</dl>
<h3>Benchmark mode</h3>
<dl>
<dt><code>-b#</code></p>
<dd> Benchmark file(s), using # compression level</p>
<dt><code>-e#</code></p>
<dd> Benchmark multiple compression levels, from b# to e# (included)</p>
<dt><code>-i#</code></p>
<dd> Minimum evaluation time in seconds [1-9] (default : 3)</dl>
<h2>BUGS</h2>
<p> Report bugs at: <a rel="nofollow" href="https://github.com/lz4/lz4/issues">https://github.com/lz4/lz4/issues</a></p>
<h2>AUTHOR</h2>
<p> Yann Collet </p>
<h2>Index</h2>
