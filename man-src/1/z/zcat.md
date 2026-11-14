---
title: "zcat(1)"
name: "zcat"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zcat/"
description: "gzip, gunzip, zcat – compress or expand files"
---

<h2 class="name">NAME</h2>
<p> gzip, gunzip, zcat &#8211; compress or expand files </p>
<h2>SYNOPSIS</h2>
<p> <code>gzip</code> [<code> -acdfhklLnNrtvV19 </code>] [<code>-S suffix</code>] [ <i>name &#8230;</i> ]<br />
 <code>gunzip</code> [<code> -acfhklLnNrtvV </code>] [<code>-S suffix</code>] [ <i>name &#8230;</i> ]<br />
 <code>zcat</code> [<code> -fhLV </code>] [ <i>name &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Gzip</i> reduces the size of the named files using Lempel-Ziv coding (LZ77). Whenever possible, each file is replaced by one with the extension <code>.gz</code>, while keeping the same ownership modes, access and modification times. (The default extension is <code>z</code> for MSDOS, OS/2 FAT, Windows NT FAT and Atari.) If no files are specified, or if a file name is &quot;-&quot;, the standard input is compressed to the standard output. <i>Gzip</i> will only attempt to compress regular files. In particular, it will ignore symbolic links. </p>
<p> If the compressed file name is too long for its file system, <i>gzip</i> truncates it. <i>Gzip</i> attempts to truncate only the parts of the file name longer than 3 characters. (A part is delimited by dots.) If the name consists of small parts only, the longest parts are truncated. For example, if file names are limited to 14 characters, gzip.msdos.exe is compressed to gzi.msd.exe.gz. Names are not truncated on systems which do not have a limit on file name length. </p>
<p> By default, <i>gzip</i> keeps the original file name and timestamp in the compressed file. These are used when decompressing the file with the <code>-N</code> option. This is useful when the compressed file name was truncated or when the timestamp was not preserved after a file transfer. </p>
<p> Compressed files can be restored to their original form using <i>gzip -d</i> or <i>gunzip</i> or <i>zcat</i>. If the original name saved in the compressed file is not suitable for its file system, a new name is constructed from the original one to make it legal. </p>
<p> <i>gunzip</i> takes a list of files on its command line and replaces each file whose name ends with .gz, -gz, .z, -z, or _z (ignoring case) and which begins with the correct magic number with an uncompressed file without the original extension. <i>gunzip</i> also recognizes the special extensions <code>.tgz</code> and <code>.taz</code> as shorthands for <code>.tar.gz</code> and <code>.tar.Z</code> respectively. When compressing, <i>gzip</i> uses the <code>.tgz</code> extension if necessary instead of truncating a file with a <code>.tar</code> extension. </p>
<p> <i>gunzip</i> can currently decompress files created by <i>gzip</i>, <i>zip</i>, <i>compress</i>, <i>compress -H</i> or <i>pack</i>. The detection of the input format is automatic. When using the first two formats, <i>gunzip</i> checks a 32 bit CRC. For <i>pack</i> and <i>gunzip</i> checks the uncompressed length. The standard <i>compress</i> format was not designed to allow consistency checks. However <i>gunzip</i> is sometimes able to detect a bad .Z file. If you get an error when uncompressing a .Z file, do not assume that the .Z file is correct simply because the standard <i>uncompress</i> does not complain. This generally means that the standard <i>uncompress</i> does not check its input, and happily generates garbage output. The SCO compress -H format (lzh compression method) does not include a CRC but also allows some consistency checks. </p>
<p> Files created by <i>zip</i> can be uncompressed by gzip only if they have a single member compressed with the &#8216;deflation&#8217; method. This feature is only intended to help conversion of tar.zip files to the tar.gz format. To extract a <i>zip</i> file with a single member, use a command like <i>gunzip &lt;foo.zip</i> or <i>gunzip -S .zip foo.zip</i>. To extract zip files with several members, use <i>unzip</i> instead of <i>gunzip</i>. </p>
<p> <i>zcat</i> is identical to <i>gunzip</i> <code>-c</code>. (On some systems, <i>zcat</i> may be installed as <i>gzcat</i> to preserve the original link to <i>compress</i>.) <i>zcat</i> uncompresses either a list of files on the command line or its standard input and writes the uncompressed data on standard output. <i>zcat</i> will uncompress files that have the correct magic number whether they have a <code>.gz</code> suffix or not. </p>
<p> <i>Gzip</i> uses the Lempel-Ziv algorithm used in <i>zip</i> and PKZIP. The amount of compression obtained depends on the size of the input and the distribution of common substrings. Typically, text such as source code or English is reduced by 60-70%. Compression is generally much better than that achieved by LZW (as used in <i>compress</i>), Huffman coding (as used in <i>pack</i>), or adaptive Huffman coding (<i>compact</i>). </p>
<p> Compression is always performed, even if the compressed file is slightly larger than the original. The worst case expansion is a few bytes for the gzip file header, plus 5 bytes every 32K block, or an expansion ratio of 0.015% for large files. Note that the actual number of used disk blocks almost never increases. <i>gzip</i> preserves the mode, ownership and timestamps of files when compressing or decompressing.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a &#8211;ascii</code></p>
<dd> Ascii text mode: convert end-of-lines using local conventions. This option is supported only on some non-Unix systems. For MSDOS, CR LF is converted to LF when compressing, and LF is converted to CR LF when decompressing.</p>
<dt><code>-c &#8211;stdout &#8211;to-stdout</code></p>
<dd> Write output on standard output; keep original files unchanged. If there are several input files, the output consists of a sequence of independently compressed members. To obtain better compression, concatenate all input files before compressing them.</p>
<dt><code>-d &#8211;decompress &#8211;uncompress</code></p>
<dd> Decompress.</p>
<dt><code>-f &#8211;force</code></p>
<dd> Force compression or decompression even if the file has multiple links or the corresponding file already exists, or if the compressed data is read from or written to a terminal. If the input data is not in a format recognized by <i>gzip</i>, and if the option &#8211;stdout is also given, copy the input data without change to the standard output: let <i>zcat</i> behave as <i>cat</i>. If <code>-f</code> is not given, and when not running in the background, <i>gzip</i> prompts to verify whether an existing file should be overwritten.</p>
<dt><code>-h &#8211;help</code></p>
<dd> Display a help screen and quit.</p>
<dt><code>-k &#8211;keep</code></p>
<dd> Keep (don&#8217;t delete) input files during compression or decompression.</p>
<dt><code>-l &#8211;list</code></p>
<dd> For each compressed file, list the following fields: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compressed size: size of the compressed file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uncompressed size: size of the uncompressed file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ratio: compression ratio&nbsp;(0.0%&nbsp;if unknown)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uncompressed_name: name of the uncompressed file </p>
<p> The uncompressed size is given as -1 for files not in gzip format, such as compressed .Z files. To get the uncompressed size for such a file, you can use: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;zcat file.Z | wc -c </p>
<p> In combination with the &#8211;verbose option, the following fields are also displayed: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;method: compression method<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;crc: the 32-bit CRC of the uncompressed data<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;date&nbsp;&amp;&nbsp;time: timestamp for the uncompressed file </p>
<p> The compression methods currently supported are deflate, compress, lzh (SCO compress -H) and pack. The crc is given as ffffffff for a file not in gzip format. </p>
<p> With &#8211;name, the uncompressed name, date and time are those stored within the compress file if present. </p>
<p> With &#8211;verbose, the size totals and compression ratio for all files is also displayed, unless some sizes are unknown. With &#8211;quiet, the title and totals lines are not displayed.</p>
<dt><code>-L &#8211;license</code></p>
<dd> Display the <i>gzip</i> license and quit.</p>
<dt><code>-n &#8211;no-name</code></p>
<dd> When compressing, do not save the original file name and timestamp by default. (The original name is always saved if the name had to be truncated.) When decompressing, do not restore the original file name if present (remove only the <i>gzip</i> suffix from the compressed file name) and do not restore the original timestamp if present (copy it from the compressed file). This option is the default when decompressing.</p>
<dt><code>-N &#8211;name</code></p>
<dd> When compressing, always save the original file name and timestamp; this is the default. When decompressing, restore the original file name and timestamp if present. This option is useful on systems which have a limit on file name length or when the timestamp has been lost after a file transfer.</p>
<dt><code>-q &#8211;quiet</code></p>
<dd> Suppress all warnings.</p>
<dt><code>-r &#8211;recursive</code></p>
<dd> Travel the directory structure recursively. If any of the file names specified on the command line are directories, <i>gzip</i> will descend into the directory and compress all the files it finds there (or decompress them in the case of <i>gunzip</i> ).</p>
<dt><code>-S .suf &#8211;suffix .suf</code></p>
<dd> When compressing, use suffix .suf instead of .gz. Any non-empty suffix can be given, but suffixes other than .z and .gz should be avoided to avoid confusion when files are transferred to other systems. </p>
<p> When decompressing, add .suf to the beginning of the list of suffixes to try, when deriving an output file name from an input file name.</p>
<dt><code>&#8211;synchronous</code></p>
<dd> Use synchronous output. With this option, <i>gzip</i> is less likely to lose data during a system crash, but it can be considerably slower.</p>
<dt><code>-t &#8211;test</code></p>
<dd> Test. Check the compressed file integrity.</p>
<dt><code>-v &#8211;verbose</code></p>
<dd> Verbose. Display the name and percentage reduction for each file compressed or decompressed.</p>
<dt><code>-V &#8211;version</code></p>
<dd> Version. Display the version number and compilation options then quit.</p>
<dt><code>-# &#8211;fast &#8211;best</code></p>
<dd> Regulate the speed of compression using the specified digit <i>#</i>, where <code>-1</code> or <code>&#8211;fast</code> indicates the fastest compression method (less compression) and <code>-9</code> or <code>&#8211;best</code> indicates the slowest compression method (best compression). The default compression level is <code>-6</code> (that is, biased towards high compression at expense of speed).</p>
<dt><code>&#8211;rsyncable</code></p>
<dd> When you synchronize a compressed file between two computers, this option allows rsync to transfer only files that were changed in the archive instead of the entire archive. Normally, after a change is made to any file in the archive, the compression algorithm can generate a new version of the archive that does not match the previous version of the archive. In this case, rsync transfers the entire new version of the archive to the remote computer. With this option, rsync can transfer only the changed files as well as a small amount of metadata that is required to update the archive structure in the area that was changed.</dl>
<h2>ADVANCED USAGE</h2>
<p> Multiple compressed files can be concatenated. In this case, <i>gunzip</i> will extract all members at once. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gzip -c file1&nbsp;<wbr>&nbsp;&gt;&nbsp;foo.gz<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gzip -c file2&nbsp;&gt;&gt;&nbsp;foo.gz </p>
<p> Then </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gunzip -c foo </p>
<p> is equivalent to </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cat file1 file2 </p>
<p> In case of damage to one member of a .gz file, other members can still be recovered (if the damaged member is removed). However, you can get better compression by compressing all members at once: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cat file1 file2 | gzip&nbsp;&gt;&nbsp;foo.gz </p>
<p> compresses better than </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gzip -c file1 file2&nbsp;&gt;&nbsp;foo.gz </p>
<p> If you want to recompress concatenated files to get better compression, do: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gzip -cd old.gz | gzip&nbsp;&gt;&nbsp;new.gz </p>
<p> If a compressed file consists of several members, the uncompressed size and CRC reported by the &#8211;list option applies to the last member only. If you need the uncompressed size for all members, you can use: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gzip -cd file.gz | wc -c </p>
<p> If you wish to create a single archive file with multiple members so that members can later be extracted independently, use an archiver such as tar or zip. GNU tar supports the -z option to invoke gzip transparently. gzip is designed as a complement to tar, not as a replacement.</p>
<h2>ENVIRONMENT</h2>
<p> The obsolescent environment variable <code>GZIP</code> can hold a set of default options for <i>gzip</i>. These options are interpreted first and can be overwritten by explicit command line parameters. As this can cause problems when using scripts, this feature is supported only for options that are reasonably likely to not cause too much harm, and <i>gzip</i> warns if it is used. This feature will be removed in a future release of <i>gzip</i>. </p>
<p> You can use an alias or script instead. For example, if <i>gzip</i> is in the directory <code>/usr/bin</code> you can prepend <code>$HOME/bin</code> to your <code>PATH</code> and create an executable script <code>$HOME/bin/gzip</code> containing the following: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#!&nbsp;/bin/sh<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;export PATH=/usr/bin<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exec gzip -9&nbsp;&quot;$@&quot;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-znew/">znew</a>(1), <a href="/docs/linux/man/1-zcmp/">zcmp</a>(1), <a href="/docs/linux/man/1-zmore/">zmore</a>(1), <a href="/docs/linux/man/1-zforce/">zforce</a>(1), <a href="/docs/linux/man/1-gzexe/">gzexe</a>(1), <a href="/docs/linux/man/1-zip/">zip</a>(1), <a href="/docs/linux/man/1-unzip/">unzip</a>(1), <a href="/docs/linux/man/1-compress/">compress</a>(1) </p>
<p> The <i>gzip</i> file format is specified in P. Deutsch, <font SIZE="-1">GZIP</font> file format specification version 4.3, <code>&lt;<a rel="nofollow" href="https://www.ietf.org/rfc/rfc1952.txt">https://www.ietf.org/rfc/rfc1952.txt</a>&gt;</code>, Internet RFC 1952 (May 1996). The <i>zip</i> deflation format is specified in P. Deutsch, <font SIZE="-1">DEFLATE</font> Compressed Data Format Specification version 1.3, <code>&lt;<a rel="nofollow" href="https://www.ietf.org/rfc/rfc1951.txt">https://www.ietf.org/rfc/rfc1951.txt</a>&gt;</code>, Internet RFC 1951 (May 1996).</p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is normally 0; if an error occurs, exit status is 1. If a warning occurs, exit status is 2.</p>
<dl>
<dt>Usage: gzip [-cdfhklLnNrtvV19] [-S suffix] [file &#8230;]</p>
<dd> Invalid options were specified on the command line.</p>
<dt><i>file</i>: not in gzip format</p>
<dd> The file specified to <i>gunzip</i> has not been compressed.</p>
<dt><i>file</i>: Corrupt input. Use zcat to recover some data.</p>
<dd> The compressed file has been damaged. The data up to the point of failure can be recovered using </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;zcat&nbsp;<i>file</i>&nbsp;&gt;&nbsp;recover</p>
<dt><i>file</i>: compressed with <i>xx</i> bits, can only handle <i>yy</i> bits</p>
<dd> <i>File</i> was compressed (using LZW) by a program that could deal with more <i>bits</i> than the decompress code on this machine. Recompress the file with gzip, which compresses better and uses less memory.</p>
<dt><i>file</i>: already has .gz suffix &#8212; unchanged</p>
<dd> The file is assumed to be already compressed. Rename the file and try again.</p>
<dt><i>file</i> already exists; do you wish to overwrite (y or n)?</p>
<dd> Respond &quot;y&quot; if you want the output file to be replaced; &quot;n&quot; if not.</p>
<dt>gunzip: corrupt input</p>
<dd> A SIGSEGV violation was detected which usually means that the input file has been corrupted.</p>
<dt><i>xx.x%</i> Percentage of the input saved by compression.</p>
<dd> (Relevant only for <code>-v</code> and <code>-l</code>.)</p>
<dt>&#8212; not a regular file or directory: ignored</p>
<dd> When the input file is not a regular file or directory, (e.g. a symbolic link, socket, FIFO, device file), it is left unaltered.</p>
<dt>&#8212; has <i>xx</i> other links: unchanged</p>
<dd> The input file has links; it is left unchanged. See <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1) for more information. Use the <code>-f</code> flag to force compression of multiply-linked files.</dl>
<h2>CAVEATS</h2>
<p> When writing compressed data to a tape, it is generally necessary to pad the output with zeroes up to a block boundary. When the data is read and the whole block is passed to <i>gunzip</i> for decompression, <i>gunzip</i> detects that there is extra trailing garbage after the compressed data and emits a warning by default. You can use the &#8211;quiet option to suppress the warning.</p>
<h2>BUGS</h2>
<p> The gzip format represents the input size modulo 2^32, so the &#8211;list option reports incorrect uncompressed sizes and compression ratios for uncompressed files 4 GB and larger. To work around this problem, you can use the following command to discover a large uncompressed file&#8217;s true size: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;zcat file.gz | wc -c </p>
<p> The &#8211;list option reports sizes as -1 and crc as ffffffff if the compressed file is on a non seekable media. </p>
<p> In some rare cases, the &#8211;best option gives worse compression than the default compression level (-6). On some highly redundant files, <i>compress</i> compresses better than <i>gzip</i>.</p>
<h2>COPYRIGHT NOTICE</h2>
<p> Copyright &#169; 1998-1999, 2001-2002, 2012, 2015-2018 Free Software Foundation, Inc.<br />
 Copyright &#169; 1992, 1993 Jean-loup Gailly </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Foundation. </p>
<h2>Index</h2>
