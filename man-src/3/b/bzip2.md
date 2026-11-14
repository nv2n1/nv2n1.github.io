---
title: "bzip2(3)"
name: "bzip2"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bzip2/"
description: "bzip2, bunzip2 – a block-sorting file compressor, v1.0.6 bzcat – decompresses files to stdout bzip2recover – recovers data from damaged bzip2 files"
---

<h2>NAME</h2>
<p> bzip2, bunzip2 &#8211; a block-sorting file compressor, v1.0.6<br />
 bzcat &#8211; decompresses files to stdout<br />
 bzip2recover &#8211; recovers data from damaged bzip2 files </p>
<h2>SYNOPSIS</h2>
<p> <code>bzip2</code> [<code> -cdfkqstvzVL123456789 </code>] [ <i>filenames &#8230;</i> ]<br />
 <code>bunzip2</code> [<code> -fkvsVL </code>] [ <i>filenames &#8230;</i> ]<br />
 <code>bzcat</code> [<code> -s </code>] [ <i>filenames &#8230;</i> ]<br />
 <code>bzip2recover</code> <i>filename</i> </p>
<h2>DESCRIPTION</h2>
<p> <i>bzip2</i> compresses files using the Burrows-Wheeler block sorting text compression algorithm, and Huffman coding. Compression is generally considerably better than that achieved by more conventional LZ77/LZ78-based compressors, and approaches the performance of the PPM family of statistical compressors. </p>
<p> The command-line options are deliberately very similar to those of <i>GNU gzip, </i> but they are not identical. </p>
<p> <i>bzip2</i> expects a list of file names to accompany the command-line flags. Each file is replaced by a compressed version of itself, with the name &quot;original_name.bz2&quot;. Each compressed file has the same modification date, permissions, and, when possible, ownership as the corresponding original, so that these properties can be correctly restored at decompression time. File name handling is naive in the sense that there is no mechanism for preserving original file names, permissions, ownerships or dates in filesystems which lack these concepts, or have serious file name length restrictions, such as MS-DOS. </p>
<p> <i>bzip2</i> and <i>bunzip2</i> will by default not overwrite existing files. If you want this to happen, specify the -f flag. </p>
<p> If no file names are specified, <i>bzip2</i> compresses from standard input to standard output. In this case, <i>bzip2</i> will decline to write compressed output to a terminal, as this would be entirely incomprehensible and therefore pointless. </p>
<p> <i>bunzip2</i> (or <i>bzip2 -d) </i> decompresses all specified files. Files which were not created by <i>bzip2</i> will be detected and ignored, and a warning issued. <i>bzip2</i> attempts to guess the filename for the decompressed file from that of the compressed file as follows: </p>
<p>&nbsp;<wbr>filename.bz2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>becomes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filename<br />
&nbsp;<wbr>filename.bz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>becomes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filename<br />
&nbsp;<wbr>filename.tbz2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>becomes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filename.tar<br />
&nbsp;<wbr>filename.tbz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>becomes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filename.tar<br />
&nbsp;<wbr>anyothername&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>becomes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>anyothername.out </p>
<p> If the file does not end in one of the recognised endings, <i>.bz2, </i> <i>.bz, </i> <i>.tbz2</i> or <i>.tbz, </i> <i>bzip2 </i> complains that it cannot guess the name of the original file, and uses the original name with <i>.out</i> appended. </p>
<p> As with compression, supplying no filenames causes decompression from standard input to standard output. </p>
<p> <i>bunzip2 </i> will correctly decompress a file which is the concatenation of two or more compressed files. The result is the concatenation of the corresponding uncompressed files. Integrity testing (-t) of concatenated compressed files is also supported. </p>
<p> You can also compress or decompress files to the standard output by giving the -c flag. Multiple files may be compressed and decompressed like this. The resulting outputs are fed sequentially to stdout. Compression of multiple files in this manner generates a stream containing multiple compressed file representations. Such a stream can be decompressed correctly only by <i>bzip2 </i> version 0.9.0 or later. Earlier versions of <i>bzip2</i> will stop after decompressing the first file in the stream. </p>
<p> <i>bzcat</i> (or <i>bzip2 -dc) </i> decompresses all specified files to the standard output. </p>
<p> <i>bzip2</i> will read arguments from the environment variables <i>BZIP2</i> and <i>BZIP,</i> in that order, and will process them before any arguments read from the command line. This gives a convenient way to supply default arguments. </p>
<p> Compression is always performed, even if the compressed file is slightly larger than the original. Files of less than about one hundred bytes tend to get larger, since the compression mechanism has a constant overhead in the region of 50 bytes. Random data (including the output of most file compressors) is coded at about 8.05 bits per byte, giving an expansion of around 0.5%. </p>
<p> As a self-check for your protection, <i>bzip2</i> uses 32-bit CRCs to make sure that the decompressed version of a file is identical to the original. This guards against corruption of the compressed data, and against undetected bugs in <i>bzip2</i> (hopefully very unlikely). The chances of data corruption going undetected is microscopic, about one chance in four billion for each file processed. Be aware, though, that the check occurs upon decompression, so it can only tell you that something is wrong. It can&#8217;t help you recover the original uncompressed data. You can use <i>bzip2recover</i> to try to recover data from damaged files. </p>
<p> Return values: 0 for a normal exit, 1 for environmental problems (file not found, invalid flags, I/O errors, &amp;c), 2 to indicate a corrupt compressed file, 3 for an internal consistency error (eg, bug) which caused <i>bzip2</i> to panic. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c &#8211;stdout</code></p>
<dd> Compress or decompress to standard output.</p>
<dt><code>-d &#8211;decompress</code></p>
<dd> Force decompression. <i>bzip2, </i> <i>bunzip2 </i> and <i>bzcat </i> are really the same program, and the decision about what actions to take is done on the basis of which name is used. This flag overrides that mechanism, and forces <i>bzip2</i> to decompress.</p>
<dt><code>-z &#8211;compress</code></p>
<dd> The complement to -d: forces compression, regardless of the invocation name.</p>
<dt><code>-t &#8211;test</code></p>
<dd> Check integrity of the specified file(s), but don&#8217;t decompress them. This really performs a trial decompression and throws away the result.</p>
<dt><code>-f &#8211;force</code></p>
<dd> Force overwrite of output files. Normally, <i>bzip2 </i> will not overwrite existing output files. Also forces <i>bzip2 </i> to break hard links to files, which it otherwise wouldn&#8217;t do. </p>
<p> bzip2 normally declines to decompress files which don&#8217;t have the correct magic header bytes. If forced (-f), however, it will pass such files through unmodified. This is how GNU gzip behaves.</p>
<dt><code>-k &#8211;keep</code></p>
<dd> Keep (don&#8217;t delete) input files during compression or decompression.</p>
<dt><code>-s &#8211;small</code></p>
<dd> Reduce memory usage, for compression, decompression and testing. Files are decompressed and tested using a modified algorithm which only requires 2.5 bytes per block byte. This means any file can be decompressed in 2300k of memory, albeit at about half the normal speed. </p>
<p> During compression, -s selects a block size of 200k, which limits memory use to around the same figure, at the expense of your compression ratio. In short, if your machine is low on memory (8 megabytes or less), use -s for everything. See MEMORY MANAGEMENT below.</p>
<dt><code>-q &#8211;quiet</code></p>
<dd> Suppress non-essential warning messages. Messages pertaining to I/O errors and other critical events will not be suppressed.</p>
<dt><code>-v &#8211;verbose</code></p>
<dd> Verbose mode &#8212; show the compression ratio for each file processed. Further -v&#8217;s increase the verbosity level, spewing out lots of information which is primarily of interest for diagnostic purposes.</p>
<dt><code>-L &#8211;license -V &#8211;version</code></p>
<dd> Display the software version, license terms and conditions.</p>
<dt><code>-1 (or &#8211;fast) to -9 (or &#8211;best)</code></p>
<dd> Set the block size to 100 k, 200 k .. 900 k when compressing. Has no effect when decompressing. See MEMORY MANAGEMENT below. The &#8211;fast and &#8211;best aliases are primarily for GNU gzip compatibility. In particular, &#8211;fast doesn&#8217;t make things significantly faster. And &#8211;best merely selects the default behaviour.</p>
<dt><code>&#8212;</code></p>
<dd> Treats all subsequent arguments as file names, even if they start with a dash. This is so you can handle files with names beginning with a dash, for example: bzip2 &#8212; -myfilename.</p>
<dt><code>&#8211;repetitive-fast &#8211;repetitive-best</code></p>
<dd> These flags are redundant in versions 0.9.5 and above. They provided some coarse control over the behaviour of the sorting algorithm in earlier versions, which was sometimes useful. 0.9.5 and above have an improved algorithm which renders these flags irrelevant. </p>
</dl>
<h2>MEMORY MANAGEMENT</h2>
<p> <i>bzip2 </i> compresses large files in blocks. The block size affects both the compression ratio achieved, and the amount of memory needed for compression and decompression. The flags -1 through -9 specify the block size to be 100,000 bytes through 900,000 bytes (the default) respectively. At decompression time, the block size used for compression is read from the header of the compressed file, and <i>bunzip2</i> then allocates itself just enough memory to decompress the file. Since block sizes are stored in compressed files, it follows that the flags -1 to -9 are irrelevant to and so ignored during decompression. </p>
<p> Compression and decompression requirements, in bytes, can be estimated as: </p>
<p>&nbsp;<wbr>Compression:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>400k&nbsp;<wbr>+&nbsp;<wbr>(&nbsp;<wbr>8 x block size&nbsp;<wbr>) </p>
<p>&nbsp;<wbr>Decompression: 100k&nbsp;<wbr>+&nbsp;<wbr>(&nbsp;<wbr>4 x block size&nbsp;<wbr>), or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>100k&nbsp;<wbr>+&nbsp;<wbr>(&nbsp;<wbr>2.5 x block size&nbsp;<wbr>) </p>
<p> Larger block sizes give rapidly diminishing marginal returns. Most of the compression comes from the first two or three hundred k of block size, a fact worth bearing in mind when using <i>bzip2</i> on small machines. It is also important to appreciate that the decompression memory requirement is set at compression time by the choice of block size. </p>
<p> For files compressed with the default 900k block size, <i>bunzip2</i> will require about 3700 kbytes to decompress. To support decompression of any file on a 4 megabyte machine, <i>bunzip2</i> has an option to decompress using approximately half this amount of memory, about 2300 kbytes. Decompression speed is also halved, so you should use this option only where necessary. The relevant flag is -s. </p>
<p> In general, try and use the largest block size memory constraints allow, since that maximises the compression achieved. Compression and decompression speed are virtually unaffected by block size. </p>
<p> Another significant point applies to files which fit in a single block &#8212; that means most files you&#8217;d encounter using a large block size. The amount of real memory touched is proportional to the size of the file, since the file is smaller than a block. For example, compressing a file 20,000 bytes long with the flag -9 will cause the compressor to allocate around 7600k of memory, but only touch 400k + 20000 * 8 = 560 kbytes of it. Similarly, the decompressor will allocate 3700k but only touch 100k + 20000 * 4 = 180 kbytes. </p>
<p> Here is a table which summarises the maximum memory usage for different block sizes. Also recorded is the total compressed size for 14 files of the Calgary Text Compression Corpus totalling 3,141,622 bytes. This column gives some feel for how compression varies with block size. These figures tend to understate the advantage of larger block sizes for larger files, since the Corpus is dominated by smaller files. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Compress&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Decompress&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Decompress&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Corpus<br />
&nbsp;<wbr>Flag&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-s usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Size </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1200k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>500k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>350k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>914704<br />
&nbsp;<wbr>&nbsp;<wbr>-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2000k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>900k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>600k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>877703<br />
&nbsp;<wbr>&nbsp;<wbr>-3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2800k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1300k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>850k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>860338<br />
&nbsp;<wbr>&nbsp;<wbr>-4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3600k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1700k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1100k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>846899<br />
&nbsp;<wbr>&nbsp;<wbr>-5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4400k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2100k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1350k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>845160<br />
&nbsp;<wbr>&nbsp;<wbr>-6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5200k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2500k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1600k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>838626<br />
&nbsp;<wbr>&nbsp;<wbr>-7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6100k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2900k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1850k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>834096<br />
&nbsp;<wbr>&nbsp;<wbr>-8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6800k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3300k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2100k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>828642<br />
&nbsp;<wbr>&nbsp;<wbr>-9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>7600k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3700k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2350k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>828642 </p>
<h2>RECOVERING DATA FROM DAMAGED FILES</h2>
<p> <i>bzip2</i> compresses files in blocks, usually 900kbytes long. Each block is handled independently. If a media or transmission error causes a multi-block .bz2 file to become damaged, it may be possible to recover data from the undamaged blocks in the file. </p>
<p> The compressed representation of each block is delimited by a 48-bit pattern, which makes it possible to find the block boundaries with reasonable certainty. Each block also carries its own 32-bit CRC, so damaged blocks can be distinguished from undamaged ones. </p>
<p> <i>bzip2recover</i> is a simple program whose purpose is to search for blocks in .bz2 files, and write each block out into its own .bz2 file. You can then use <i>bzip2 </i> -t to test the integrity of the resulting files, and decompress those which are undamaged. </p>
<p> <i>bzip2recover</i> takes a single argument, the name of the damaged file, and writes a number of files &quot;rec00001file.bz2&quot;, &quot;rec00002file.bz2&quot;, etc, containing the extracted blocks. The output filenames are designed so that the use of wildcards in subsequent processing &#8212; for example, &quot;bzip2 -dc rec*file.bz2 &gt; recovered_data&quot; &#8212; processes the files in the correct order. </p>
<p> <i>bzip2recover</i> should be of most use dealing with large .bz2 files, as these will contain many blocks. It is clearly futile to use it on damaged single-block files, since a damaged block cannot be recovered. If you wish to minimise any potential data loss through media or transmission errors, you might consider compressing with a smaller block size. </p>
<h2>PERFORMANCE NOTES</h2>
<p> The sorting phase of compression gathers together similar strings in the file. Because of this, files containing very long runs of repeated symbols, like &quot;aabaabaabaab &#8230;&quot; (repeated several hundred times) may compress more slowly than normal. Versions 0.9.5 and above fare much better than previous versions in this respect. The ratio between worst-case and average-case compression time is in the region of 10:1. For previous versions, this figure was more like 100:1. You can use the -vvvv option to monitor progress in great detail, if you want. </p>
<p> Decompression speed is unaffected by these phenomena. </p>
<p> <i>bzip2</i> usually allocates several megabytes of memory to operate in, and then charges all over it in a fairly random fashion. This means that performance, both for compressing and decompressing, is largely determined by the speed at which your machine can service cache misses. Because of this, small changes to the code to reduce the miss rate have been observed to give disproportionately large performance improvements. I imagine <i>bzip2</i> will perform best on machines with very large caches. </p>
<h2>CAVEATS</h2>
<p> I/O error messages are not as helpful as they could be. <i>bzip2</i> tries hard to detect I/O errors and exit cleanly, but the details of what the problem is sometimes seem rather misleading. </p>
<p> This manual page pertains to version 1.0.6 of <i>bzip2. </i> Compressed data created by this version is entirely forwards and backwards compatible with the previous public releases, versions 0.1pl2, 0.9.0, 0.9.5, 1.0.0, 1.0.1, 1.0.2 and above, but with the following exception: 0.9.0 and above can correctly decompress multiple concatenated compressed files. 0.1pl2 cannot do this; it will stop after decompressing just the first file in the stream. </p>
<p> <i>bzip2recover</i> versions prior to 1.0.2 used 32-bit integers to represent bit positions in compressed files, so they could not handle compressed files more than 512 megabytes long. Versions 1.0.2 and above use 64-bit ints on some platforms which support them (GNU supported targets, and Windows). To establish whether or not bzip2recover was built with such a limitation, run it without arguments. In any event you can build yourself an unlimited version if you can recompile it with MaybeUInt64 set to be an unsigned 64-bit integer. </p>
<h2>AUTHOR</h2>
<p> Julian Seward, jsewardbzip.org. </p>
<p> <a rel="nofollow" href="http://www.bzip.org">http://www.bzip.org</a> </p>
<p> The ideas embodied in <i>bzip2</i> are due to (at least) the following people: Michael Burrows and David Wheeler (for the block sorting transformation), David Wheeler (again, for the Huffman coder), Peter Fenwick (for the structured coding model in the original <i>bzip,</i> and many refinements), and Alistair Moffat, Radford Neal and Ian Witten (for the arithmetic coder in the original <i>bzip). </i> I am much indebted for their help, support and advice. See the manual in the source distribution for pointers to sources of documentation. Christian von Roques encouraged me to look for faster sorting algorithms, so as to speed up compression. Bela Lubkin encouraged me to improve the worst-case compression performance. Donna Robinson XMLised the documentation. The bz* scripts are derived from those of GNU gzip. Many people sent patches, helped with portability problems, lent machines, gave advice and were generally helpful. </p>
<h2>Index</h2>
