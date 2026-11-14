---
title: "lbzcat(1)"
name: "lbzcat"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lbzcat/"
description: "lbzip2 – parallel bzip2 utility"
---

<h2 class="name">NAME</h2>
<p> lbzip2 &#8211; parallel bzip2 utility</p>
<h2>SYNOPSIS</h2>
<p> <code>lbzip2</code>|<code>bzip2</code> [<code>-n</code> <i>WTHRS</i>] [<code>-k</code>|<code>-c</code>|<code>-t</code>] [<code>-d</code>] [<code>-1</code> .. <code>-9</code>] [<code>-f</code>] [<code>-s</code>] [<code>-u</code>] [<code>-v</code>] [<code>-S</code>] [ <i>FILE &#8230; </i>] </p>
<p> <code>lbunzip2</code>|<code>bunzip2</code> [<code>-n</code> <i>WTHRS</i>] [<code>-k</code>|<code>-c</code>|<code>-t</code>] [<code>-z</code>] [<code>-f</code>] [<code>-s</code>] [<code>-u</code>] [<code>-v</code>] [<code>-S</code>] [ <i>FILE &#8230; </i>] </p>
<p> <code>lbzcat</code>|<code>bzcat</code> [<code>-n</code> <i>WTHRS</i>] [<code>-z</code>] [<code>-f</code>] [<code>-s</code>] [<code>-u</code>] [<code>-v</code>] [<code>-S</code>] [ <i>FILE &#8230; </i>] </p>
<p> <code>lbzip2</code>|<code>bzip2</code>|<code>lbunzip2</code>|<code>bunzip2</code>|<code>lbzcat</code>|<code>bzcat</code> <code>-h</code> </p>
<h2>DESCRIPTION</h2>
<p> Compress or decompress <i>FILE</i> operands or standard input to regular files or standard output using the Burrows-Wheeler block-sorting text compression algorithm. The <code>lbzip2</code> utility employs multiple threads and an input-bound splitter even when decompressing <code>.bz2</code> files created by standard bzip2. </p>
<p> Compression is generally considerably better than that achieved by more conventional LZ77/LZ78-based compressors, and competitive with all but the best of the PPM family of statistical compressors. </p>
<p> Compression is always performed, even if the compressed file is slightly larger than the original. The worst case expansion is for files of zero length, which expand to fourteen bytes. Random data (including the output of most file compressors) is coded with asymptotic expansion of around 0.5%. </p>
<p> The command-line options are deliberately very similar to those of <code>bzip2</code> and <code>gzip</code>, but they are not identical. </p>
<h2>INVOCATION</h2>
<p> The default mode of operation is compression. If the utility is invoked as <code>lbunzip2</code> or <code>bunzip2</code>, the mode is switched to decompression. Calling the utility as <code>lbzcat</code> or <code>bzcat</code> selects decompression, with the decompressed byte-stream written to standard output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n </code><i>WTHRS</i></p>
<dd> Set the number of (de)compressor threads to <i>WTHRS</i>. If this option is not specified, <code>lbzip2</code> tries to query the system for the number of online processors (if both the compilation environment and the execution environment support that), or exits with an error (if it&#8217;s unable to determine the number of processors online). </p>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Don&#8217;t remove <i>FILE</i> operands after successful (de)compression. Open regular input files with more than one link. </p>
<dt><code>-c</code>, <code>&#8211;stdout</code></p>
<dd> Write output to standard output, even when <i>FILE</i> operands are present. Implies <code>-k</code> and excludes <code>-t</code>. </p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd> Test decompression; discard output instead of writing it to files or standard output. Implies <code>-k</code> and excludes <code>-c</code>. Roughly equivalent to passing <code>-c</code> and redirecting standard output to the bit bucket. </p>
<dt><code>-d</code>, <code>&#8211;decompress</code></p>
<dd> Force decompression over the mode of operation selected by the invocation name. </p>
<dt><code>-z</code>, <code>&#8211;compress</code></p>
<dd> Force compression over the mode of operation selected by the invocation name. </p>
<dt><code>-1</code> .. <code>-9</code></p>
<dd> Set the compression block size to 100K .. 900K, in 100K increments. Ignored during decompression. See also the BLOCK SIZE section below. </p>
<dt><code>&#8211;fast</code></p>
<dd> Alias for <code>-1</code>. </p>
<dt><code>&#8211;best</code></p>
<dd> Alias for <code>-9</code>. This is the default. </p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Open non-regular input files. Open input files with more than one link, breaking links when <code>-k</code> isn&#8217;t specified in addition. Try to remove each output file before opening it. By default <code>lbzip2</code> will not overwrite existing files; if you want this to happen, you should specify <code>-f</code>. If <code>-c</code> and <code>-d</code> are also given don&#8217;t reject files not in bzip2 format, just copy them without change; without <code>-f lbzip2</code> would stop after reaching a file that is not in bzip2 format. </p>
<dt><code>-s</code>, <code>&#8211;small</code></p>
<dd> Reduce memory usage at cost of performance. </p>
<dt><code>-u</code>, <code>&#8211;sequential</code></p>
<dd> Perform splitting input blocks sequentially. This may improve compression ratio and decrease CPU usage, but will degrade scalability. </p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be more verbose. Print more detailed information about (de)compression progress to standard error: before processing each file, print a message stating the names of input and output files; during (de)compression, print a rough percentage of completeness and estimated time of arrival (only if standard error is connected to a terminal); after processing each file print a message showing compression ratio, space savings, total compression time (wall time) and average (de)compression speed (bytes of plain data processed per second). </p>
<dt><code>-S</code></p>
<dd> Print condition variable statistics to standard error for each completed (de)compression operation. Useful in profiling. </p>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;repetitive-fast</code>, &#8211;repetitive-best<code>, </code>&#8211;exponential</p>
<dd> Accepted for compatibility with <code>bzip2</code>, otherwise ignored. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help on command-line usage on standard output and exit successfully. </p>
<dt><code>-L</code>, <code>&#8211;license</code>, <code>-V</code>, <code>&#8211;version</code></p>
<dd> Print license and version information on standard output and exit successfully. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>LBZIP2</i>, <i>BZIP2</i>, <i>BZIP</i></p>
<dd> Before parsing the command line, lbzip2 inserts the contents of these variables, in the order specified, between the invocation name and the rest of the command line. Tokens are separated by spaces and tabs, which cannot be escaped. </p>
</dl>
<h2>OPERANDS</h2>
<dl>
<dt><i>FILE</i></p>
<dd> Specify files to compress or decompress. </p>
<p> <i>FILE</i>s with <code>.bz2</code>, <code>.tbz</code>, <code>.tbz2</code> and <code>.tz2</code> name suffixes will be skipped when compressing. When decompressing, <code>.bz2</code> suffixes will be removed in output filenames; <code>.tbz</code>, <code>.tbz2</code> and <code>.tz2</code> suffixes will be replaced by <code>.tar</code>; other filenames will be suffixed with <code>.out</code>. If an <code>INT</code> or <code>TERM</code> signal is delivered to <code>lbzip2</code>, then it removes the regular output file currently open before exiting. </p>
<p> If no FILE is given, lbzip2 works as a filter, processing standard input to standard output. In this case, <code>lbzip2</code> will decline to write compressed output to a terminal (or read compressed input from a terminal), as this would be entirely incomprehensible and therefore pointless. </p>
</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> if <code>lbzip2</code> finishes successfully. This presumes that whenever it tries, <code>lbzip2</code> never fails to write to standard error. </p>
<dt><code>1</code></p>
<dd> if <code>lbzip2</code> encounters a fatal error. </p>
<dt><code>4</code></p>
<dd> if <code>lbzip2</code> issues warnings without encountering a fatal error. This presumes that whenever it tries, <code>lbzip2</code> never fails to write to standard error. </p>
<dt><code>SIGPIPE</code>, <code>SIGXFSZ</code></p>
<dd> if <code>lbzip2</code> intends to exit with status <code>1</code> due to any fatal error, but any such signal with inherited <code>SIG_DFL</code> action was generated for <code>lbzip2</code> previously, then <code>lbzip2</code> terminates by way of one of said signals, after cleaning up any interrupted output file. </p>
<dt><code>SIGABRT</code></p>
<dd> if a runtime assertion fails (i.e. <code>lbzip2</code> detects a bug in itself). Hopefully whoever compiled your binary wasn&#8217;t bold enough to <code>#define NDEBUG</code>. </p>
<dt><code>SIGINT</code>, <code>SIGTERM</code></p>
<dd> <code>lbzip2</code> catches these signals so that it can remove an interrupted output file. In such cases, <code>lbzip2</code> exits by re-raising (one of) the received signal(s). </p>
</dl>
<h2>BLOCK SIZE</h2>
<p> <code>lbzip2</code> compresses large files in blocks. It can operate at various block sizes, ranging from 100k to 900k in 100k steps, and it allocates only as much memory as it needs to. The block size affects both the compression ratio achieved, and the amount of memory needed both for compression and decompression. Compression and decompression speed is virtually unaffected by block size, provided that the file being processed is large enough to be split among all worker threads. </p>
<p> The flags <code>-1</code> through <code>-9</code> specify the block size to be 100,000 bytes through 900,000 bytes (the default) respectively. At decompression-time, the block size used for compression is read from the compressed file &#8212; the flags <code>-1</code> to <code>-9</code> are irrelevant to and so ignored during decompression. </p>
<p> Larger block sizes give rapidly diminishing marginal returns; most of the compression comes from the first two or three hundred k of block size, a fact worth bearing in mind when using <code>lbzip2</code> on small machines. It is also important to appreciate that the decompression memory requirement is set at compression-time by the choice of block size. In general you should try and use the largest block size memory constraints allow. </p>
<p> Another significant point applies to small files. By design, only one of <code>lbzip2</code>&#8216;s worker threads can work on a single block. This means that if the number of blocks in the compressed file is less than the number of processors online, then some of worker threads will remain idle for the entire time. Compressing small files with smaller block sizes can therefore significantly increase both compression and decompression speed. The speed difference is more noticeable as the number of CPU cores grows. </p>
<h2>ERROR HANDLING</h2>
<p> Dealing with error conditions is the least satisfactory aspect of <code>lbzip2</code>. The policy is to try and leave the filesystem in a consistent state, then quit, even if it means not processing some of the files mentioned in the command line. </p>
<p> `A consistent state&#8217; means that a file exists either in its compressed or uncompressed form, but not both. This boils down to the rule `delete the output file if an error condition occurs, leaving the input intact&#8217;. Input files are only deleted when we can be pretty sure the output file has been written and closed successfully. </p>
<h2>RESOURCE ALLOCATION</h2>
<p> <code>lbzip2</code> needs various kinds of system resources to operate. Those include memory, threads, mutexes and condition variables. The policy is to simply give up if a resource allocation failure occurs. </p>
<p> Resource consumption grows linearly with number of worker threads. If <code>lbzip2</code> fails because of lack of some resources, decreasing number of worker threads may help. It would be possible for <code>lbzip2</code> to try to reduce number of worker threads (and hence the resource consumption), or to move on to subsequent files in the hope that some might need less resources, but the complications for doing this seem more trouble than they are worth. </p>
<h2>DAMAGED FILES</h2>
<p> <code>lbzip2</code> attempts to compress data by performing several non-trivial transformations on it. Every compression of a file implies an assumption that the compressed file can be decompressed to reproduce the original. Great efforts in design, coding and testing have been made to ensure that this program works correctly. However, the complexity of the algorithms, and, in particular, the presence of various special cases in the code which occur with very low but non-zero probability make it very difficult to rule out the possibility of bugs remaining in the program. That is not to say this program is inherently unreliable. Indeed, I very much hope the opposite is true &#8212; <code>lbzip2</code> has been carefully constructed and extensively tested. </p>
<p> As a self-check for your protection, <code>lbzip2</code> uses 32-bit CRCs to make sure that the decompressed version of a file is identical to the original. This guards against corruption of the compressed data, and against undiscovered bugs in <code>lbzip2</code> (hopefully unlikely). The chances of data corruption going undetected is microscopic, about one chance in four billion for each file processed. Be aware, though, that the check occurs upon decompression, so it can only tell you that that something is wrong. </p>
<p> CRCs can only detect corrupted files, they can&#8217;t help you recover the original, uncompressed data. However, because of the block nature of the compression algorithm, it may be possible to recover some parts of the damaged file, even if some blocks are destroyed. </p>
<h2>BUGS</h2>
<p> Separate input files don&#8217;t share worker threads; at most one input file is worked on at any moment. </p>
<h2>AUTHORS</h2>
<p> <code>lbzip2</code> was originally written by Laszlo Ersek &lt;lacos [at] caesar.elte.hu&gt;, <a rel="nofollow" href="http://lacos.hu/.">http://lacos.hu/.</a> Versions 2.0 and later were written by Mikolaj Izdebski. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011, 2012, 2013 Mikolaj Izdebski<br />
 Copyright (C) 2008, 2009, 2010 Laszlo Ersek<br />
 Copyright (C) 1996 Julian Seward </p>
<p> This manual page is part of lbzip2, version 2.5. lbzip2 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> lbzip2 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with lbzip2. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<h2>THANKS</h2>
<p> Adam Maulis at ELTE IIG; Julian Seward; Paul Sladen; Michael Thomas from Caltech HEP; Bryan Stillwell; Zsolt Bartos-Elekes; Imre Csatlos; Gabor Kovesdan; Paul Wise; Paolo Bonzini; Department of Electrical and Information Engineering at the University of Oulu; Yuta Mori. </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code>lbzip2</code> home page</p>
<dd> <a rel="nofollow" href="http://lbzip2.org/">http://lbzip2.org/</a> </p>
<dt><code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1)</p>
<dd> <a rel="nofollow" href="http://www.bzip.org/">http://www.bzip.org/</a> </p>
<dt><code><a href="/docs/linux/man/1-pbzip2/">pbzip2</a></code>(1)</p>
<dd> <a rel="nofollow" href="http://compression.ca/pbzip2/">http://compression.ca/pbzip2/</a> </p>
<dt><code><a href="/docs/linux/man/1-bzip2smp/">bzip2smp</a></code>(1)</p>
<dd> <a rel="nofollow" href="http://bzip2smp.sourceforge.net/">http://bzip2smp.sourceforge.net/</a> </p>
<dt><code><a href="/docs/linux/man/1-smpbzip2/">smpbzip2</a></code>(1)</p>
<dd> <a rel="nofollow" href="http://home.student.utwente.nl/n.werensteijn/smpbzip2/">http://home.student.utwente.nl/n.werensteijn/smpbzip2/</a> </p>
<dt><code><a href="/docs/linux/man/1-dbzip2/">dbzip2</a></code>(1)</p>
<dd> <a rel="nofollow" href="http://www.mediawiki.org/wiki/Dbzip2">http://www.mediawiki.org/wiki/Dbzip2</a> </p>
<dt><code><a href="/docs/linux/man/1-p7zip/">p7zip</a></code>(1)</p>
<dd> <a rel="nofollow" href="http://p7zip.sourceforge.net/">http://p7zip.sourceforge.net/</a> </p>
</dl>
<h2>Index</h2>
