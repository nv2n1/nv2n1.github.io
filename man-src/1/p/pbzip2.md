---
title: "pbzip2(1)"
name: "pbzip2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbzip2/"
description: "pbzip2 – parallel bzip2 file compressor, v1.1.10"
---

<h2>NAME</h2>
<p> pbzip2 &#8211; parallel bzip2 file compressor, v1.1.10</p>
<h2>SYNOPSIS</h2>
<p> <code>pbzip2</code> [<code> -123456789 </code>] [<code> -b#cdfhklm#p#qrS#tvVz </code>] [ <i>filenames &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>pbzip2</i> is a parallel implementation of the bzip2 block-sorting file compressor that uses pthreads and achieves near-linear speedup on SMP machines. The output of this version is fully compatible with bzip2 v1.0.2 or newer (ie: anything compressed with <i>pbzip2</i> can be decompressed with bzip2). </p>
<p> <i>pbzip2</i> should work on any system that has a pthreads compatible C++ compiler (such as gcc). It has been tested on: Linux, Windows (cygwin), Solaris, Tru64/OSF1, HP-UX, and Irix. </p>
<p> The default settings for <i>pbzip2</i> will work well in most cases. The only switch you will likely need to use is -d to decompress files and -p to set the # of processors for <i>pbzip2</i> to use if autodetect is not supported on your system, or you want to use a specific # of CPUs.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b#</code></p>
<dd> Where # is block size in 100k steps (default 9 = 900k)</p>
<dt><code>-c, &#8211;stdout</code></p>
<dd> Output to standard out (stdout)</p>
<dt><code>-d,&#8211;decompress</code></p>
<dd> Decompress file</p>
<dt><code>-f,&#8211;force</code></p>
<dd> Force, overwrite existing output file</p>
<dt><code>-h,&#8211;help</code></p>
<dd> Print this help message</p>
<dt><code>-k,&#8211;keep</code></p>
<dd> Keep input file, do not delete</p>
<dt><code>-l,&#8211;loadavg</code></p>
<dd> Load average determines max number processors to use</p>
<dt><code>-m#</code></p>
<dd> Where # is max memory usage in 1MB steps (default 100 = 100MB)</p>
<dt><code>-p#</code></p>
<dd> Where # is the number of processors (default: autodetect)</p>
<dt><code>-q,&#8211;quiet</code></p>
<dd> Quiet mode (default)</p>
<dt><code>-r,&#8211;read</code></p>
<dd> Read entire input file into RAM and split between processors</p>
<dt><code>-S#</code></p>
<dd> Child thread stack size in 1KB steps (default stack size if unspecified)</p>
<dt><code>-t,&#8211;test</code></p>
<dd> Test compressed file integrity</p>
<dt><code>-v,&#8211;verbose</code></p>
<dd> Verbose mode</p>
<dt><code>-V</code></p>
<dd> Display version info for <i>pbzip2</i> then exit</p>
<dt><code>-z,&#8211;compress</code></p>
<dd> Compress file (default)</p>
<dt><code>-1,&#8211;fast &#8230; -9,&#8211;best</code></p>
<dd> Set BWT block size to 100k .. 900k (default 900k).</p>
<dt><code>&#8211;ignore-trailing-garbage=#</code></p>
<dd> Ignore trailing garbage flag (1 &#8211; ignored; 0 &#8211; forbidden)</dl>
<p> If no file names are given, pbzip2 compresses or decompresses from standard input to standard output.</p>
<h2>FILE SIZES</h2>
<p> You should be able to compress files larger than 4GB with <i>pbzip2.</i> </p>
<p> Files that are compressed with <i>pbzip2</i> are broken up into pieces and each individual piece is compressed. This is how <i>pbzip2</i> runs faster on multiple CPUs since the pieces can be compressed simultaneously. The final .bz2 file may be slightly larger than if it was compressed with the regular bzip2 program due to this file splitting (usually less than 0.2% larger). Files that are compressed with <i>pbzip2</i> will also gain considerable speedup when decompressed using <i>pbzip2.</i> </p>
<p> Files that were compressed using bzip2 will not see speedup since bzip2 packages the data into a single chunk that cannot be split between processors.</p>
<h2>EXAMPLES</h2>
<p> Example 1: pbzip2 myfile.tar </p>
<p> This example will compress the file &quot;myfile.tar&quot; into the compressed file &quot;myfile.tar.bz2&quot;. It will use the autodetected # of processors (or 2 processors if autodetect not supported) with the default file block size of 900k and default BWT block size of 900k. </p>
<p> Example 2: pbzip2 -b15k myfile.tar </p>
<p> This example will compress the file &quot;myfile.tar&quot; into the compressed file &quot;myfile.tar.bz2&quot;. It will use the autodetected # of processors (or 2 processors if autodetect not supported) with a file block size of 1500k and a BWT block size of 900k. The file &quot;myfile.tar&quot; will not be deleted after compression is finished. </p>
<p> Example 3: pbzip2 -p4 -r -5 myfile.tar second*.txt </p>
<p> This example will compress the file &quot;myfile.tar&quot; into the compressed file &quot;myfile.tar.bz2&quot;. It will use 4 processors with a BWT block size of 500k. The file block size will be the size of &quot;myfile.tar&quot; divided by 4 (# of processors) so that the data will be split evenly among each processor. This requires you have enough RAM for pbzip2 to read the entire file into memory for compression. Pbzip2 will then use the same options to compress all other files that match the wildcard &quot;second*.txt&quot; in that directory. </p>
<p> Example 4: tar cf myfile.tar.bz2 &#8211;use-compress-prog=pbzip2 dir_to_compress/<br />
 Example 4: tar -c directory_to_compress/ | pbzip2 -c &gt; myfile.tar.bz2 </p>
<p> These examples will compress the data being given to pbzip2 via pipe from TAR into the compressed file &quot;myfile.tar.bz2&quot;. It will use the autodetected # of processors (or 2 processors if autodetect not supported) with the default file block size of 900k and default BWT block size of 900k. TAR is collecting all of the files from the &quot;directory_to_compress/&quot; directory and passing the data to pbzip2 as it works. </p>
<p> Example 5: pbzip2 -d -m500 myfile.tar.bz2 </p>
<p> This example will decompress the file &quot;myfile.tar.bz2&quot; into the decompressed file &quot;myfile.tar&quot;. It will use the autodetected # of processors (or 2 processors if autodetect not supported). It will use a maximum of 500MB of memory for decompression. The switches -b, -r, and -1..-9 are not valid for decompression. </p>
<p> Example 6: pbzip2 -dc myfile.tar.bz2 | tar x </p>
<p> This example will decompress and untar the file &quot;myfile.tar.bz2&quot; piping the output of the decompressing pbzip2 to tar. </p>
<p> Example 7: pbzip2 -c &lt; myfile.txt &gt; myfile.txt.bz2 </p>
<p> This example will read myfile.txt from standard input compressing it to standard output which is redirected to to myfile.txt.bz2.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1) <a href="/docs/linux/man/1-gzip/">gzip</a>(1) <a href="/docs/linux/man/1-lzip/">lzip</a>(1) <a href="/docs/linux/man/1-rzip/">rzip</a>(1) <a href="/docs/linux/man/1-zip/">zip</a>(1)</p>
<h2>AUTHOR</h2>
<p> Jeff Gilchrist </p>
<p> <a rel="nofollow" href="http://compression.ca">http://compression.ca</a> </p>
<h2>Index</h2>
