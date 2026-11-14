---
title: "compress(1)"
name: "compress"
section: "1"
letter: "c"
url: "/docs/linux/man/1-compress/"
description: "compress, uncompress, zcat – compress and expand data"
---

<h2>NAME</h2>
<p> compress, uncompress, zcat &#8211; compress and expand data</p>
<h2>SYNOPSIS</h2>
<p> <code>compress</code> [ <code>-f</code> ] [ <code>-v</code> ] [ <code>-c</code> ] [ <code>-V</code> ] [ <code>-r</code> ] [ <code>-b</code> <i>bits</i> ] [ <i>name &#8230;</i> ]<br />
 <code>uncompress</code> [ <code>-f</code> ] [ <code>-v</code> ] [ <code>-c</code> ] [ <code>-V</code> ] [ <i>name &#8230;</i> ]<br />
 <code>zcat</code> [ <code>-V</code> ] [ <i>name &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Compress</i> reduces the size of the named files using adaptive Lempel-Ziv coding. Whenever possible, each file is replaced by one with the extension <code>.Z,</code> while keeping the same ownership modes, access and modification times. If no files are specified, the standard input is compressed to the standard output. <i>Compress</i> will only attempt to compress regular files. In particular, it will ignore symbolic links. If a file has multiple hard links, <i>compress</i> will refuse to compress it unless the <code>-f</code> flag is given. </p>
<p> If <code>-f</code> is not given and <i>compress</i> is run in the foreground, the user is prompted as to whether an existing file should be overwritten. </p>
<p> Compressed files can be restored to their original form using <i>uncompress</i> or <i>zcat.</i> </p>
<p> <i>uncompress</i> takes a list of files on its command line and replaces each file whose name ends with <code>.Z</code> and which begins with the correct magic number with an uncompressed file without the <code>.Z.</code> The uncompressed file will have the mode, ownership and timestamps of the compressed file. </p>
<p> The <code>-c</code> option makes <i>compress/uncompress</i> write to the standard output; no files are changed. </p>
<p> <i>zcat</i> is identical to <i>uncompress</i> <code>-c.</code> <i>zcat</i> uncompresses either a list of files on the command line or its standard input and writes the uncompressed data on standard output. <i>zcat</i> will uncompress files that have the correct magic number whether they have a <code>.Z</code> suffix or not. </p>
<p> If the <code>-r</code> flag is specified, <i>compress</i> will operate recursively. If any of the file names specified on the command line are directories, <i>compress</i> will descend into the directory and compress all the files it finds there. </p>
<p> The <code>-V</code> flag tells each of these programs to print its version and patchlevel, along with any preprocessor flags specified during compilation, on stderr before doing any compression or uncompression. </p>
<p> <i>Compress</i> uses the modified Lempel-Ziv algorithm popularized in &quot;A Technique for High Performance Data Compression&quot;, Terry A. Welch, <i>IEEE Computer,</i> vol. 17, no. 6 (June 1984), pp. 8-19. Common substrings in the file are first replaced by 9-bit codes 257 and up. When code 512 is reached, the algorithm switches to 10-bit codes and continues to use more bits until the limit specified by the <code>-b</code> flag is reached (default 16). <i>Bits</i> must be between 9 and 16. The default can be changed in the source to allow <i>compress</i> to be run on a smaller machine. </p>
<p> After the <i>bits</i> limit is attained, <i>compress</i> periodically checks the compression ratio. If it is increasing, <i>compress</i> continues to use the existing code dictionary. However, if the compression ratio decreases, <i>compress</i> discards the table of substrings and rebuilds it from scratch. This allows the algorithm to adapt to the next &quot;block&quot; of the file. </p>
<p> Note that the <code>-b</code> flag is omitted for <i>uncompress,</i> since the <i>bits</i> parameter specified during compression is encoded within the output, along with a magic number to ensure that neither decompression of random data nor recompression of compressed data is attempted. </p>
<p> The amount of compression obtained depends on the size of the input, the number of <i>bits</i> per code, and the distribution of common substrings. Typically, text such as source code or English is reduced by 50-60%. Compression is generally much better than that achieved by Huffman coding (as used in <i>pack</i>), or adaptive Huffman coding (<i>compact</i>), and takes less time to compute. </p>
<p> Under the <code>-v</code> option, a message is printed yielding the percentage of reduction for each file compressed.</p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is normally 0; if the last file is larger after (attempted) compression, the status is 2; if an error occurs, exit status is 1. </p>
<p> Usage: compress [-dfvcVr] [-b maxbits] [file &#8230;] Invalid options were specified on the command line. Missing maxbits Maxbits must follow <code>-b</code>. <i>file</i>: not in compressed format The file specified to <i>uncompress</i> has not been compressed. <i>file</i>: compressed with <i>xx</i> bits, can only handle <i>yy</i> bits <i>File</i> was compressed by a program that could deal with more <i>bits</i> than the compress code on this machine. Recompress the file with smaller <i>bits</i>. <i>file</i>: already has .Z suffix &#8212; no change The file is assumed to be already compressed. Rename the file and try again. <i>file</i>: filename too long to tack on .Z The file cannot be compressed because its name is longer than 12 characters. Rename and try again. This message does not occur on BSD systems. <i>file</i> already exists; do you wish to overwrite (y or n)? Respond &quot;y&quot; if you want the output file to be replaced; &quot;n&quot; if not. uncompress: corrupt input A SIGSEGV violation was detected which usually means that the input file has been corrupted. Compression: <i>xx.xx%</i> Percentage of the input saved by compression. (Relevant only for <code>-v</code>.) &#8212; not a regular file or directory: ignored When the input file is not a regular file or directory, (e.g. a symbolic link, socket, FIFO, device file), it is left unaltered. &#8212; has <i>xx </i> other links: unchanged The input file has links; it is left unchanged. See <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1) for more information. Use the <code>-f</code> flag to force compression of multiply-linked files. &#8212; file unchanged No savings is achieved by compression. The input remains virgin.</p>
<h2>BUGS</h2>
<p> Although compressed files are compatible between machines with large memory, <code>-b</code>12 should be used for file transfer to architectures with a small process data space (64KB or less, as exhibited by the DEC PDP series, the Intel 80286, etc.) </p>
<p> Invoking compress with a <code>-r</code> flag will occasionally cause it to produce spurious error warnings of the form </p>
<p> &quot;&lt;filename&gt;.Z already has .Z suffix &#8211; ignored&quot; </p>
<p> These warnings can be ignored. See the comments in compress42.c:compdir() in the source distribution for an explanation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pack/">pack</a></code>(1), <code><a href="/docs/linux/man/1-compact/">compact</a></code>(1) </p>
<h2>Index</h2>
