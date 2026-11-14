---
title: "lzma(1)"
name: "lzma"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lzma/"
description: "xz, unxz, xzcat, lzma, unlzma, lzcat – Compress or decompress .xz and .lzma files"
---

<h2 class="name">NAME</h2>
<p> xz, unxz, xzcat, lzma, unlzma, lzcat &#8211; Compress or decompress .xz and .lzma files </p>
<h2>SYNOPSIS</h2>
<p> <code>xz</code> [<i>option&#8230;</i>] [<i>file&#8230;</i>]</p>
<h2>COMMAND ALIASES</h2>
<p> <code>unxz</code> is equivalent to <code>xz &#8211;decompress</code>.<br />
 <code>xzcat</code> is equivalent to <code>xz &#8211;decompress &#8211;stdout</code>.<br />
 <code>lzma</code> is equivalent to <code>xz &#8211;format=lzma</code>.<br />
 <code>unlzma</code> is equivalent to <code>xz &#8211;format=lzma &#8211;decompress</code>.<br />
 <code>lzcat</code> is equivalent to <code>xz &#8211;format=lzma &#8211;decompress &#8211;stdout</code>. </p>
<p> When writing scripts that need to decompress files, it is recommended to always use the name <code>xz</code> with appropriate arguments (<code>xz -d</code> or <code>xz -dc</code>) instead of the names <code>unxz</code> and <code>xzcat</code>.</p>
<h2>DESCRIPTION</h2>
<p> <code>xz</code> is a general-purpose data compression tool with command line syntax similar to <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) and <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1). The native file format is the <code>.xz</code> format, but the legacy <code>.lzma</code> format used by LZMA Utils and raw compressed streams with no container format headers are also supported. </p>
<p> <code>xz</code> compresses or decompresses each <i>file</i> according to the selected operation mode. If no <i>files</i> are given or <i>file</i> is <code>&#8211;</code>, <code>xz</code> reads from standard input and writes the processed data to standard output. <code>xz</code> will refuse (display an error and skip the <i>file</i>) to write compressed data to standard output if it is a terminal. Similarly, <code>xz</code> will refuse to read compressed data from standard input if it is a terminal. </p>
<p> Unless <code>&#8211;stdout</code> is specified, <i>files</i> other than <code>&#8211;</code> are written to a new file whose name is derived from the source <i>file</i> name:</p>
<dl>
<dt>&bull;</p>
<dd> When compressing, the suffix of the target file format (<code>.xz</code> or <code>.lzma</code>) is appended to the source filename to get the target filename.</p>
<dt>&bull;</p>
<dd> When decompressing, the <code>.xz</code> or <code>.lzma</code> suffix is removed from the filename to get the target filename. <code>xz</code> also recognizes the suffixes <code>.txz</code> and <code>.tlz</code>, and replaces them with the <code>.tar</code> suffix.</dl>
<p> If the target file already exists, an error is displayed and the <i>file</i> is skipped. </p>
<p> Unless writing to standard output, <code>xz</code> will display a warning and skip the <i>file</i> if any of the following applies:</p>
<dl>
<dt>&bull;</p>
<dd> <i>File</i> is not a regular file. Symbolic links are not followed, and thus they are not considered to be regular files.</p>
<dt>&bull;</p>
<dd> <i>File</i> has more than one hard link.</p>
<dt>&bull;</p>
<dd> <i>File</i> has setuid, setgid, or sticky bit set.</p>
<dt>&bull;</p>
<dd> The operation mode is set to compress and the <i>file</i> already has a suffix of the target file format (<code>.xz</code> or <code>.txz</code> when compressing to the <code>.xz</code> format, and <code>.lzma</code> or <code>.tlz</code> when compressing to the <code>.lzma</code> format).</p>
<dt>&bull;</p>
<dd> The operation mode is set to decompress and the <i>file</i> doesn&#8217;t have a suffix of any of the supported file formats (<code>.xz</code>, <code>.txz</code>, <code>.lzma</code>, or <code>.tlz</code>).</dl>
<p> After successfully compressing or decompressing the <i>file</i>, <code>xz</code> copies the owner, group, permissions, access time, and modification time from the source <i>file</i> to the target file. If copying the group fails, the permissions are modified so that the target file doesn&#8217;t become accessible to users who didn&#8217;t have permission to access the source <i>file</i>. <code>xz</code> doesn&#8217;t support copying other metadata like access control lists or extended attributes yet. </p>
<p> Once the target file has been successfully closed, the source <i>file</i> is removed unless <code>&#8211;keep</code> was specified. The source <i>file</i> is never removed if the output is written to standard output. </p>
<p> Sending <code>SIGINFO</code> or <code>SIGUSR1</code> to the <code>xz</code> process makes it print progress information to standard error. This has only limited use since when standard error is a terminal, using <code>&#8211;verbose</code> will display an automatically updating progress indicator.</p>
<h3>Memory usage</h3>
<p> The memory usage of <code>xz</code> varies from a few hundred kilobytes to several gigabytes depending on the compression settings. The settings used when compressing a file determine the memory requirements of the decompressor. Typically the decompressor needs 5&nbsp;% to 20&nbsp;% of the amount of memory that the compressor needed when creating the file. For example, decompressing a file created with <code>xz -9</code> currently requires 65 MiB of memory. Still, it is possible to have <code>.xz</code> files that require several gigabytes of memory to decompress. </p>
<p> Especially users of older systems may find the possibility of very large memory usage annoying. To prevent uncomfortable surprises, <code>xz</code> has a built-in memory usage limiter, which is disabled by default. While some operating systems provide ways to limit the memory usage of processes, relying on it wasn&#8217;t deemed to be flexible enough (for example, using <code><a href="/docs/linux/man/1-ulimit/">ulimit</a></code>(1) to limit virtual memory tends to cripple <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)). </p>
<p> The memory usage limiter can be enabled with the command line option <code>&#8211;memlimit=</code><i>limit</i>. Often it is more convenient to enable the limiter by default by setting the environment variable <code>XZ_DEFAULTS</code>, for example, <code>XZ_DEFAULTS=&#8211;memlimit=150MiB</code>. It is possible to set the limits separately for compression and decompression by using <code>&#8211;memlimit-compress=</code><i>limit</i> and <code>&#8211;memlimit-decompress=</code><i>limit</i>. Using these two options outside <code>XZ_DEFAULTS</code> is rarely useful because a single run of <code>xz</code> cannot do both compression and decompression and <code>&#8211;memlimit=</code><i>limit</i> (or <code>-M</code> <i>limit</i>) is shorter to type on the command line. </p>
<p> If the specified memory usage limit is exceeded when decompressing, <code>xz</code> will display an error and decompressing the file will fail. If the limit is exceeded when compressing, <code>xz</code> will try to scale the settings down so that the limit is no longer exceeded (except when using <code>&#8211;format=raw</code> or <code>&#8211;no-adjust</code>). This way the operation won&#8217;t fail unless the limit is very small. The scaling of the settings is done in steps that don&#8217;t match the compression level presets, for example, if the limit is only slightly less than the amount required for <code>xz -9</code>, the settings will be scaled down only a little, not all the way down to <code>xz -8</code>.</p>
<h3>Concatenation and padding with .xz files</h3>
<p> It is possible to concatenate <code>.xz</code> files as is. <code>xz</code> will decompress such files as if they were a single <code>.xz</code> file. </p>
<p> It is possible to insert padding between the concatenated parts or after the last part. The padding must consist of null bytes and the size of the padding must be a multiple of four bytes. This can be useful, for example, if the <code>.xz</code> file is stored on a medium that measures file sizes in 512-byte blocks. </p>
<p> Concatenation and padding are not allowed with <code>.lzma</code> files or raw streams.</p>
<h2>OPTIONS</h2>
<h3>Integer suffixes and special values</h3>
<p> In most places where an integer argument is expected, an optional suffix is supported to easily indicate large integers. There must be no space between the integer and the suffix.</p>
<dl>
<dt><code>KiB</code></p>
<dd> Multiply the integer by 1,024 (2^10). <code>Ki</code>, <code>k</code>, <code>kB</code>, <code>K</code>, and <code>KB</code> are accepted as synonyms for <code>KiB</code>.</p>
<dt><code>MiB</code></p>
<dd> Multiply the integer by 1,048,576 (2^20). <code>Mi</code>, <code>m</code>, <code>M</code>, and <code>MB</code> are accepted as synonyms for <code>MiB</code>.</p>
<dt><code>GiB</code></p>
<dd> Multiply the integer by 1,073,741,824 (2^30). <code>Gi</code>, <code>g</code>, <code>G</code>, and <code>GB</code> are accepted as synonyms for <code>GiB</code>.</dl>
<p> The special value <code>max</code> can be used to indicate the maximum integer value supported by the option.</p>
<h3>Operation mode</h3>
<p> If multiple operation mode options are given, the last one takes effect.</p>
<dl>
<dt><code>-z</code>, <code>&#8211;compress</code></p>
<dd> Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the command name (for example, <code>unxz</code> implies <code>&#8211;decompress</code>).</p>
<dt><code>-d</code>, <code>&#8211;decompress</code>, <code>&#8211;uncompress</code></p>
<dd> Decompress.</p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd> Test the integrity of compressed <i>files</i>. This option is equivalent to <code>&#8211;decompress &#8211;stdout</code> except that the decompressed data is discarded instead of being written to standard output. No files are created or removed.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> Print information about compressed <i>files</i>. No uncompressed output is produced, and no files are created or removed. In list mode, the program cannot read the compressed data from standard input or from other unseekable sources.</p>
<dt>
<dd> The default listing shows basic information about <i>files</i>, one file per line. To get more detailed information, use also the <code>&#8211;verbose</code> option. For even more information, use <code>&#8211;verbose</code> twice, but note that this may be slow, because getting all the extra information requires many seeks. The width of verbose output exceeds 80 characters, so piping the output to, for example, <code>less -S</code> may be convenient if the terminal isn&#8217;t wide enough.</p>
<dt>
<dd> The exact output may vary between <code>xz</code> versions and different locales. For machine-readable output, <code>&#8211;robot &#8211;list</code> should be used.</dl>
<h3>Operation modifiers</h3>
<dl>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Don&#8217;t delete the input files.</p>
<dt>
<dd> Since <code>xz</code> 5.4.0, this option also makes <code>xz</code> compress or decompress even if the input is a symbolic link to a regular file, has more than one hard link, or has the setuid, setgid, or sticky bit set. The setuid, setgid, and sticky bits are not copied to the target file. In earlier versions this was only done with <code>&#8211;force</code>.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> This option has several effects:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> If the target file already exists, delete it before compressing or decompressing.</p>
<dt>&bull;</p>
<dd> Compress or decompress even if the input is a symbolic link to a regular file, has more than one hard link, or has the setuid, setgid, or sticky bit set. The setuid, setgid, and sticky bits are not copied to the target file.</p>
<dt>&bull;</p>
<dd> When used with <code>&#8211;decompress</code> <code>&#8211;stdout</code> and <code>xz</code> cannot recognize the type of the source file, copy the source file as is to standard output. This allows <code>xzcat</code> <code>&#8211;force</code> to be used like <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) for files that have not been compressed with <code>xz</code>. Note that in future, <code>xz</code> might support new compressed file formats, which may make <code>xz</code> decompress more types of files instead of copying them as is to standard output. <code>&#8211;format=</code><i>format</i> can be used to restrict <code>xz</code> to decompress only a single file format.</dl>
</dl>
<dt><code>-c</code>, <code>&#8211;stdout</code>, <code>&#8211;to-stdout</code></p>
<dd> Write the compressed or decompressed data to standard output instead of a file. This implies <code>&#8211;keep</code>.</p>
<dt><code>&#8211;single-stream</code></p>
<dd> Decompress only the first <code>.xz</code> stream, and silently ignore possible remaining input data following the stream. Normally such trailing garbage makes <code>xz</code> display an error.</p>
<dt>
<dd> <code>xz</code> never decompresses more than one stream from <code>.lzma</code> files or raw streams, but this option still makes <code>xz</code> ignore the possible trailing data after the <code>.lzma</code> file or raw stream.</p>
<dt>
<dd> This option has no effect if the operation mode is not <code>&#8211;decompress</code> or <code>&#8211;test</code>.</p>
<dt><code>&#8211;no-sparse</code></p>
<dd> Disable creation of sparse files. By default, if decompressing into a regular file, <code>xz</code> tries to make the file sparse if the decompressed data contains long sequences of binary zeros. It also works when writing to standard output as long as standard output is connected to a regular file and certain additional conditions are met to make it safe. Creating sparse files may save disk space and speed up the decompression by reducing the amount of disk I/O.</p>
<dt><code>-S</code> <i>.suf</i>, <code>&#8211;suffix=</code><i>.suf</p>
<dd> When compressing, use .suf</i> as the suffix for the target file instead of <code>.xz</code> or <code>.lzma</code>. If not writing to standard output and the source file already has the suffix <i>.suf</i>, a warning is displayed and the file is skipped.</p>
<dt>
<dd> When decompressing, recognize files with the suffix <i>.suf</i> in addition to files with the <code>.xz</code>, <code>.txz</code>, <code>.lzma</code>, or <code>.tlz</code> suffix. If the source file has the suffix <i>.suf</i>, the suffix is removed to get the target filename.</p>
<dt>
<dd> When compressing or decompressing raw streams (<code>&#8211;format=raw</code>), the suffix must always be specified unless writing to standard output, because there is no default suffix for raw streams.</p>
<dt><code>&#8211;files</code>[<code>=</code><i>file</i>]</p>
<dd> Read the filenames to process from <i>file</i>; if <i>file</i> is omitted, filenames are read from standard input. Filenames must be terminated with the newline character. A dash (<code>&#8211;</code>) is taken as a regular filename; it doesn&#8217;t mean standard input. If filenames are given also as command line arguments, they are processed before the filenames read from <i>file</i>.</p>
<dt><code>&#8211;files0</code>[<code>=</code><i>file</i>]</p>
<dd> This is identical to <code>&#8211;files</code>[<code>=</code><i>file</i>] except that each filename must be terminated with the null character.</dl>
<h3>Basic file format and compression options</h3>
<dl>
<dt><code>-F</code> <i>format</i>, <code>&#8211;format=</code><i>format</p>
<dd> Specify the file format</i> to compress or decompress:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> This is the default. When compressing, <code>auto</code> is equivalent to <code>xz</code>. When decompressing, the format of the input file is automatically detected. Note that raw streams (created with <code>&#8211;format=raw</code>) cannot be auto-detected.</p>
<dt><code>xz</code></p>
<dd> Compress to the <code>.xz</code> file format, or accept only <code>.xz</code> files when decompressing.</p>
<dt><code>lzma</code>, <code>alone</code></p>
<dd> Compress to the legacy <code>.lzma</code> file format, or accept only <code>.lzma</code> files when decompressing. The alternative name <code>alone</code> is provided for backwards compatibility with LZMA Utils.</p>
<dt><code>raw</code></p>
<dd> Compress or uncompress a raw stream (no headers). This is meant for advanced users only. To decode raw streams, you need use <code>&#8211;format=raw</code> and explicitly specify the filter chain, which normally would have been stored in the container headers.</dl>
</dl>
<dt><code>-C</code> <i>check</i>, <code>&#8211;check=</code><i>check</p>
<dd> Specify the type of the integrity check. The check is calculated from the uncompressed data and stored in the </i><code>.xz</code> file. This option has an effect only when compressing into the <code>.xz</code> format; the <code>.lzma</code> format doesn&#8217;t support integrity checks. The integrity check (if any) is verified when the <code>.xz</code> file is decompressed.</p>
<dt>
<dd> Supported <i>check</i> types:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> Don&#8217;t calculate an integrity check at all. This is usually a bad idea. This can be useful when integrity of the data is verified by other means anyway.</p>
<dt><code>crc32</code></p>
<dd> Calculate CRC32 using the polynomial from IEEE-802.3 (Ethernet).</p>
<dt><code>crc64</code></p>
<dd> Calculate CRC64 using the polynomial from ECMA-182. This is the default, since it is slightly better than CRC32 at detecting damaged files and the speed difference is negligible.</p>
<dt><code>sha256</code></p>
<dd> Calculate SHA-256. This is somewhat slower than CRC32 and CRC64.</dl>
</dl>
<dt>
<dd> Integrity of the <code>.xz</code> headers is always verified with CRC32. It is not possible to change or disable it.</p>
<dt><code>&#8211;ignore-check</code></p>
<dd> Don&#8217;t verify the integrity check of the compressed data when decompressing. The CRC32 values in the <code>.xz</code> headers will still be verified normally.</p>
<dt>
<dd> <code>Do not use this option unless you know what you are doing.</code> Possible reasons to use this option:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Trying to recover data from a corrupt .xz file.</p>
<dt>&bull;</p>
<dd> Speeding up decompression. This matters mostly with SHA-256 or with files that have compressed extremely well. It&#8217;s recommended to not use this option for this purpose unless the file integrity is verified externally in some other way.</dl>
</dl>
<dt><code>-0</code> &#8230; <code>-9</code></p>
<dd> Select a compression preset level. The default is <code>-6</code>. If multiple preset levels are specified, the last one takes effect. If a custom filter chain was already specified, setting a compression preset level clears the custom filter chain.</p>
<dt>
<dd> The differences between the presets are more significant than with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) and <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1). The selected compression settings determine the memory requirements of the decompressor, thus using a too high preset level might make it painful to decompress the file on an old system with little RAM. Specifically, <code>it&#8217;s not a good idea to blindly use -9 for everything</code> like it often is with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) and <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1).</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-0</code> &#8230; <code>-3</code></p>
<dd> These are somewhat fast presets. <code>-0</code> is sometimes faster than <code>gzip -9</code> while compressing much better. The higher ones often have speed comparable to <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) with comparable or better compression ratio, although the results depend a lot on the type of data being compressed.</p>
<dt><code>-4</code> &#8230; <code>-6</code></p>
<dd> Good to very good compression while keeping decompressor memory usage reasonable even for old systems. <code>-6</code> is the default, which is usually a good choice for distributing files that need to be decompressible even on systems with only 16 MiB RAM. (<code>-5e</code> or <code>-6e</code> may be worth considering too. See <code>&#8211;extreme</code>.)</p>
<dt><code>-7 &#8230; -9</code></p>
<dd> These are like <code>-6</code> but with higher compressor and decompressor memory requirements. These are useful only when compressing files bigger than 8 MiB, 16 MiB, and 32 MiB, respectively.</dl>
</dl>
<dt>
<dd> On the same hardware, the decompression speed is approximately a constant number of bytes of compressed data per second. In other words, the better the compression, the faster the decompression will usually be. This also means that the amount of uncompressed output produced per second can vary a lot.</p>
<dt>
<dd> The following table summarises the features of the presets:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center>Preset</td>
<td ALIGN=center>DictSize</td>
<td ALIGN=center>CompCPU</td>
<td ALIGN=center>CompMem</td>
<td ALIGN=center>DecMem
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>256 KiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>3 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>1 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>1 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>9 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>2 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>2 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>17 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>3 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>4 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>32 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>5 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>4 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>48 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>5 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>94 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>9 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>94 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>9 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>16 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>186 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>17 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>32 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>370 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>33 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>64 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>674 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>65 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
</table>
</dl>
</dl>
<dt>
<dd> Column descriptions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> DictSize is the LZMA2 dictionary size. It is waste of memory to use a dictionary bigger than the size of the uncompressed file. This is why it is good to avoid using the presets <code>-7</code> &#8230; <code>-9</code> when there&#8217;s no real need for them. At <code>-6</code> and lower, the amount of memory wasted is usually low enough to not matter.</p>
<dt>&bull;</p>
<dd> CompCPU is a simplified representation of the LZMA2 settings that affect compression speed. The dictionary size affects speed too, so while CompCPU is the same for levels <code>-6</code> &#8230; <code>-9</code>, higher levels still tend to be a little slower. To get even slower and thus possibly better compression, see <code>&#8211;extreme</code>.</p>
<dt>&bull;</p>
<dd> CompMem contains the compressor memory requirements in the single-threaded mode. It may vary slightly between <code>xz</code> versions. Memory requirements of some of the future multithreaded modes may be dramatically higher than that of the single-threaded mode.</p>
<dt>&bull;</p>
<dd> DecMem contains the decompressor memory requirements. That is, the compression settings determine the memory requirements of the decompressor. The exact decompressor memory usage is slightly more than the LZMA2 dictionary size, but the values in the table have been rounded up to the next full MiB.</dl>
</dl>
<dt><code>-e</code>, <code>&#8211;extreme</code></p>
<dd> Use a slower variant of the selected compression preset level (<code>-0</code> &#8230; <code>-9</code>) to hopefully get a little bit better compression ratio, but with bad luck this can also make it worse. Decompressor memory usage is not affected, but compressor memory usage increases a little at preset levels <code>-0</code> &#8230; <code>-3</code>.</p>
<dt>
<dd> Since there are two presets with dictionary sizes 4 MiB and 8 MiB, the presets <code>-3e</code> and <code>-5e</code> use slightly faster settings (lower CompCPU) than <code>-4e</code> and <code>-6e</code>, respectively. That way no two presets are identical.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center>Preset</td>
<td ALIGN=center>DictSize</td>
<td ALIGN=center>CompCPU</td>
<td ALIGN=center>CompMem</td>
<td ALIGN=center>DecMem
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-0e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>256 KiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>4 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>1 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-1e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>1 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>13 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>2 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-2e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>2 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>25 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>3 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-3e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>4 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>48 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>5 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-4e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>4 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>48 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>5 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-5e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>94 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>9 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-6e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>94 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>9 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-7e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>16 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>186 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>17 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-8e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>32 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>370 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>33 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-9e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>64 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>674 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>65 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
</table>
</dl>
</dl>
<dt>
<dd> For example, there are a total of four presets that use 8 MiB dictionary, whose order from the fastest to the slowest is <code>-5</code>, <code>-6</code>, <code>-5e</code>, and <code>-6e</code>.</p>
<dt><code>&#8211;fast</code></p>
<dd>
<dt><code>&#8211;best</code></p>
<dd> These are somewhat misleading aliases for <code>-0</code> and <code>-9</code>, respectively. These are provided only for backwards compatibility with LZMA Utils. Avoid using these options.</p>
<dt><code>&#8211;block-size=</code><i>size</i></p>
<dd> When compressing to the <code>.xz</code> format, split the input data into blocks of <i>size</i> bytes. The blocks are compressed independently from each other, which helps with multi-threading and makes limited random-access decompression possible. This option is typically used to override the default block size in multi-threaded mode, but this option can be used in single-threaded mode too.</p>
<dt>
<dd> In multi-threaded mode about three times <i>size</i> bytes will be allocated in each thread for buffering input and output. The default <i>size</i> is three times the LZMA2 dictionary size or 1 MiB, whichever is more. Typically a good value is 2-4 times the size of the LZMA2 dictionary or at least 1 MiB. Using <i>size</i> less than the LZMA2 dictionary size is waste of RAM because then the LZMA2 dictionary buffer will never get fully used. The sizes of the blocks are stored in the block headers, which a future version of <code>xz</code> will use for multi-threaded decompression.</p>
<dt>
<dd> In single-threaded mode no block splitting is done by default. Setting this option doesn&#8217;t affect memory usage. No size information is stored in block headers, thus files created in single-threaded mode won&#8217;t be identical to files created in multi-threaded mode. The lack of size information also means that a future version of <code>xz</code> won&#8217;t be able decompress the files in multi-threaded mode.</p>
<dt><code>&#8211;block-list=</code><i>sizes</i></p>
<dd> When compressing to the <code>.xz</code> format, start a new block after the given intervals of uncompressed data.</p>
<dt>
<dd> The uncompressed <i>sizes</i> of the blocks are specified as a comma-separated list. Omitting a size (two or more consecutive commas) is a shorthand to use the size of the previous block.</p>
<dt>
<dd> If the input file is bigger than the sum of <i>sizes</i>, the last value in <i>sizes</i> is repeated until the end of the file. A special value of <code>0</code> may be used as the last value to indicate that the rest of the file should be encoded as a single block.</p>
<dt>
<dd> If one specifies <i>sizes</i> that exceed the encoder&#8217;s block size (either the default value in threaded mode or the value specified with <code>&#8211;block-size=</code><i>size</i>), the encoder will create additional blocks while keeping the boundaries specified in <i>sizes</i>. For example, if one specifies <code>&#8211;block-size=10MiB</code> <code>&#8211;block-list=5MiB,10MiB,8MiB,12MiB,24MiB</code> and the input file is 80 MiB, one will get 11 blocks: 5, 10, 8, 10, 2, 10, 10, 4, 10, 10, and 1 MiB.</p>
<dt>
<dd> In multi-threaded mode the sizes of the blocks are stored in the block headers. This isn&#8217;t done in single-threaded mode, so the encoded output won&#8217;t be identical to that of the multi-threaded mode.</p>
<dt><code>&#8211;flush-timeout=</code><i>timeout</i></p>
<dd> When compressing, if more than <i>timeout</i> milliseconds (a positive integer) has passed since the previous flush and reading more input would block, all the pending input data is flushed from the encoder and made available in the output stream. This can be useful if <code>xz</code> is used to compress data that is streamed over a network. Small <i>timeout</i> values make the data available at the receiving end with a small delay, but large <i>timeout</i> values give better compression ratio.</p>
<dt>
<dd> This feature is disabled by default. If this option is specified more than once, the last one takes effect. The special <i>timeout</i> value of <code>0</code> can be used to explicitly disable this feature.</p>
<dt>
<dd> This feature is not available on non-POSIX systems.</p>
<dt>
<dd> <code>This feature is still experimental.</code> Currently <code>xz</code> is unsuitable for decompressing the stream in real time due to how <code>xz</code> does buffering.</p>
<dt><code>&#8211;memlimit-compress=</code><i>limit</i></p>
<dd> Set a memory usage limit for compression. If this option is specified multiple times, the last one takes effect.</p>
<dt>
<dd> If the compression settings exceed the <i>limit</i>, <code>xz</code> will adjust the settings downwards so that the limit is no longer exceeded and display a notice that automatic adjustment was done. Such adjustments are not made when compressing with <code>&#8211;format=raw</code> or if <code>&#8211;no-adjust</code> has been specified. In those cases, an error is displayed and <code>xz</code> will exit with exit status 1.</p>
<dt>
<dd> The <i>limit</i> can be specified in multiple ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The <i>limit</i> can be an absolute value in bytes. Using an integer suffix like <code>MiB</code> can be useful. Example: <code>&#8211;memlimit-compress=80MiB</code></p>
<dt>&bull;</p>
<dd> The <i>limit</i> can be specified as a percentage of total physical memory (RAM). This can be useful especially when setting the <code>XZ_DEFAULTS</code> environment variable in a shell initialization script that is shared between different computers. That way the limit is automatically bigger on systems with more memory. Example: <code>&#8211;memlimit-compress=70%</code></p>
<dt>&bull;</p>
<dd> The <i>limit</i> can be reset back to its default value by setting it to <code>0</code>. This is currently equivalent to setting the <i>limit</i> to <code>max</code> (no memory usage limit). Once multithreading support has been implemented, there may be a difference between <code>0</code> and <code>max</code> for the multithreaded case, so it is recommended to use <code>0</code> instead of <code>max</code> until the details have been decided.</dl>
</dl>
<dt>
<dd> For 32-bit <code>xz</code> there is a special case: if the <i>limit</i> would be over <code>4020 MiB</code>, the <i>limit</i> is set to <code>4020 MiB</code>. (The values <code>0</code> and <code>max</code> aren&#8217;t affected by this. A similar feature doesn&#8217;t exist for decompression.) This can be helpful when a 32-bit executable has access to 4 GiB address space while hopefully doing no harm in other situations.</p>
<dt>
<dd> See also the section <code>Memory usage</code>.</p>
<dt><code>&#8211;memlimit-decompress=</code><i>limit</i></p>
<dd> Set a memory usage limit for decompression. This also affects the <code>&#8211;list</code> mode. If the operation is not possible without exceeding the <i>limit</i>, <code>xz</code> will display an error and decompressing the file will fail. See <code>&#8211;memlimit-compress=</code><i>limit</i> for possible ways to specify the <i>limit</i>.</p>
<dt><code>-M</code> <i>limit</i>, <code>&#8211;memlimit=</code><i>limit</i>, <code>&#8211;memory=</code><i>limit</p>
<dd> This is equivalent to specifying </i><code>&#8211;memlimit-compress=</code><i>limit</i> <code>&#8211;memlimit-decompress=</code><i>limit</i>.</p>
<dt><code>&#8211;no-adjust</code></p>
<dd> Display an error and exit if the compression settings exceed the memory usage limit. The default is to adjust the settings downwards so that the memory usage limit is not exceeded. Automatic adjusting is always disabled when creating raw streams (<code>&#8211;format=raw</code>).</p>
<dt><code>-T</code> <i>threads</i>, <code>&#8211;threads=</code><i>threads</p>
<dd> Specify the number of worker threads to use. Setting threads</i> to a special value <code>0</code> makes <code>xz</code> use as many threads as there are CPU cores on the system. The actual number of threads can be less than <i>threads</i> if the input file is not big enough for threading with the given settings or if using more threads would exceed the memory usage limit.</p>
<dt>
<dd> Currently the only threading method is to split the input into blocks and compress them independently from each other. The default block size depends on the compression level and can be overridden with the <code>&#8211;block-size=</code><i>size</i> option.</p>
<dt>
<dd> Threaded decompression hasn&#8217;t been implemented yet. It will only work on files that contain multiple blocks with size information in block headers. All files compressed in multi-threaded mode meet this condition, but files compressed in single-threaded mode don&#8217;t even if <code>&#8211;block-size=</code><i>size</i> is used.</dl>
<h3>Custom compressor filter chains</h3>
<p> A custom filter chain allows specifying the compression settings in detail instead of relying on the settings associated to the presets. When a custom filter chain is specified, preset options (<code>-0</code> &#8230; <code>-9</code> and <code>&#8211;extreme</code>) earlier on the command line are forgotten. If a preset option is specified after one or more custom filter chain options, the new preset takes effect and the custom filter chain options specified earlier are forgotten. </p>
<p> A filter chain is comparable to piping on the command line. When compressing, the uncompressed input goes to the first filter, whose output goes to the next filter (if any). The output of the last filter gets written to the compressed file. The maximum number of filters in the chain is four, but typically a filter chain has only one or two filters. </p>
<p> Many filters have limitations on where they can be in the filter chain: some filters can work only as the last filter in the chain, some only as a non-last filter, and some work in any position in the chain. Depending on the filter, this limitation is either inherent to the filter design or exists to prevent security issues. </p>
<p> A custom filter chain is specified by using one or more filter options in the order they are wanted in the filter chain. That is, the order of filter options is significant! When decoding raw streams (<code>&#8211;format=raw</code>), the filter chain is specified in the same order as it was specified when compressing. </p>
<p> Filters take filter-specific <i>options</i> as a comma-separated list. Extra commas in <i>options</i> are ignored. Every option has a default value, so you need to specify only those you want to change. </p>
<p> To see the whole filter chain and <i>options</i>, use <code>xz -vv</code> (that is, use <code>&#8211;verbose</code> twice). This works also for viewing the filter chain options used by presets.</p>
<dl>
<dt><code>&#8211;lzma1</code>[<code>=</code><i>options</i>]</p>
<dd>
<dt><code>&#8211;lzma2</code>[<code>=</code><i>options</i>]</p>
<dd> Add LZMA1 or LZMA2 filter to the filter chain. These filters can be used only as the last filter in the chain.</p>
<dt>
<dd> LZMA1 is a legacy filter, which is supported almost solely due to the legacy <code>.lzma</code> file format, which supports only LZMA1. LZMA2 is an updated version of LZMA1 to fix some practical issues of LZMA1. The <code>.xz</code> format uses LZMA2 and doesn&#8217;t support LZMA1 at all. Compression speed and ratios of LZMA1 and LZMA2 are practically the same.</p>
<dt>
<dd> LZMA1 and LZMA2 share the same set of <i>options</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>preset=</code><i>preset</i></p>
<dd> Reset all LZMA1 or LZMA2 <i>options</i> to <i>preset</i>. <i>Preset</i> consist of an integer, which may be followed by single-letter preset modifiers. The integer can be from <code>0</code> to <code>9</code>, matching the command line options <code>-0</code> &#8230; <code>-9</code>. The only supported modifier is currently <code>e</code>, which matches <code>&#8211;extreme</code>. If no <code>preset</code> is specified, the default values of LZMA1 or LZMA2 <i>options</i> are taken from the preset <code>6</code>.</p>
<dt><code>dict=</code><i>size</i></p>
<dd> Dictionary (history buffer) <i>size</i> indicates how many bytes of the recently processed uncompressed data is kept in memory. The algorithm tries to find repeating byte sequences (matches) in the uncompressed data, and replace them with references to the data currently in the dictionary. The bigger the dictionary, the higher is the chance to find a match. Thus, increasing dictionary <i>size</i> usually improves compression ratio, but a dictionary bigger than the uncompressed file is waste of memory.</p>
<dt>
<dd> Typical dictionary <i>size</i> is from 64 KiB to 64 MiB. The minimum is 4 KiB. The maximum for compression is currently 1.5 GiB (1536 MiB). The decompressor already supports dictionaries up to one byte less than 4 GiB, which is the maximum for the LZMA1 and LZMA2 stream formats.</p>
<dt>
<dd> Dictionary <i>size</i> and match finder (<i>mf</i>) together determine the memory usage of the LZMA1 or LZMA2 encoder. The same (or bigger) dictionary <i>size</i> is required for decompressing that was used when compressing, thus the memory usage of the decoder is determined by the dictionary size used when compressing. The <code>.xz</code> headers store the dictionary <i>size</i> either as 2^<i>n</i> or 2^<i>n</i> + 2^(<i>n</i>-1), so these <i>sizes</i> are somewhat preferred for compression. Other <i>sizes</i> will get rounded up when stored in the <code>.xz</code> headers.</p>
<dt><code>lc=</code><i>lc</i></p>
<dd> Specify the number of literal context bits. The minimum is 0 and the maximum is 4; the default is 3. In addition, the sum of <i>lc</i> and <i>lp</i> must not exceed 4.</p>
<dt>
<dd> All bytes that cannot be encoded as matches are encoded as literals. That is, literals are simply 8-bit bytes that are encoded one at a time.</p>
<dt>
<dd> The literal coding makes an assumption that the highest <i>lc</i> bits of the previous uncompressed byte correlate with the next byte. For example, in typical English text, an upper-case letter is often followed by a lower-case letter, and a lower-case letter is usually followed by another lower-case letter. In the US-ASCII character set, the highest three bits are 010 for upper-case letters and 011 for lower-case letters. When <i>lc</i> is at least 3, the literal coding can take advantage of this property in the uncompressed data.</p>
<dt>
<dd> The default value (3) is usually good. If you want maximum compression, test <code>lc=4</code>. Sometimes it helps a little, and sometimes it makes compression worse. If it makes it worse, test <code>lc=2</code> too.</p>
<dt><code>lp=</code><i>lp</i></p>
<dd> Specify the number of literal position bits. The minimum is 0 and the maximum is 4; the default is 0.</p>
<dt>
<dd> <i>Lp</i> affects what kind of alignment in the uncompressed data is assumed when encoding literals. See <i>pb</i> below for more information about alignment.</p>
<dt><code>pb=</code><i>pb</i></p>
<dd> Specify the number of position bits. The minimum is 0 and the maximum is 4; the default is 2.</p>
<dt>
<dd> <i>Pb</i> affects what kind of alignment in the uncompressed data is assumed in general. The default means four-byte alignment (2^<i>pb</i>=2^2=4), which is often a good choice when there&#8217;s no better guess.</p>
<dt>
<dd> When the aligment is known, setting <i>pb</i> accordingly may reduce the file size a little. For example, with text files having one-byte alignment (US-ASCII, ISO-8859-*, UTF-8), setting <code>pb=0</code> can improve compression slightly. For UTF-16 text, <code>pb=1</code> is a good choice. If the alignment is an odd number like 3 bytes, <code>pb=0</code> might be the best choice.</p>
<dt>
<dd> Even though the assumed alignment can be adjusted with <i>pb</i> and <i>lp</i>, LZMA1 and LZMA2 still slightly favor 16-byte alignment. It might be worth taking into account when designing file formats that are likely to be often compressed with LZMA1 or LZMA2.</p>
<dt><code>mf=</code><i>mf</i></p>
<dd> Match finder has a major effect on encoder speed, memory usage, and compression ratio. Usually Hash Chain match finders are faster than Binary Tree match finders. The default depends on the <i>preset</i>: 0 uses <code>hc3</code>, 1-3 use <code>hc4</code>, and the rest use <code>bt4</code>.</p>
<dt>
<dd> The following match finders are supported. The memory usage formulas below are rough approximations, which are closest to the reality when <i>dict</i> is a power of two.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>hc3</code></p>
<dd> Hash Chain with 2- and 3-byte hashing<br />
 Minimum value for <i>nice</i>: 3<br />
 Memory usage:<br />
 <i>dict</i> * 7.5 (if <i>dict</i> &lt;= 16 MiB);<br />
 <i>dict</i> * 5.5 + 64 MiB (if <i>dict</i> &gt; 16 MiB)</p>
<dt><code>hc4</code></p>
<dd> Hash Chain with 2-, 3-, and 4-byte hashing<br />
 Minimum value for <i>nice</i>: 4<br />
 Memory usage:<br />
 <i>dict</i> * 7.5 (if <i>dict</i> &lt;= 32 MiB);<br />
 <i>dict</i> * 6.5 (if <i>dict</i> &gt; 32 MiB)</p>
<dt><code>bt2</code></p>
<dd> Binary Tree with 2-byte hashing<br />
 Minimum value for <i>nice</i>: 2<br />
 Memory usage: <i>dict</i> * 9.5</p>
<dt><code>bt3</code></p>
<dd> Binary Tree with 2- and 3-byte hashing<br />
 Minimum value for <i>nice</i>: 3<br />
 Memory usage:<br />
 <i>dict</i> * 11.5 (if <i>dict</i> &lt;= 16 MiB);<br />
 <i>dict</i> * 9.5 + 64 MiB (if <i>dict</i> &gt; 16 MiB)</p>
<dt><code>bt4</code></p>
<dd> Binary Tree with 2-, 3-, and 4-byte hashing<br />
 Minimum value for <i>nice</i>: 4<br />
 Memory usage:<br />
 <i>dict</i> * 11.5 (if <i>dict</i> &lt;= 32 MiB);<br />
 <i>dict</i> * 10.5 (if <i>dict</i> &gt; 32 MiB)</dl>
</dl>
<dt><code>mode=</code><i>mode</i></p>
<dd> Compression <i>mode</i> specifies the method to analyze the data produced by the match finder. Supported <i>modes</i> are <code>fast</code> and <code>normal</code>. The default is <code>fast</code> for <i>presets</i> 0-3 and <code>normal</code> for <i>presets</i> 4-9.</p>
<dt>
<dd> Usually <code>fast</code> is used with Hash Chain match finders and <code>normal</code> with Binary Tree match finders. This is also what the <i>presets</i> do.</p>
<dt><code>nice=</code><i>nice</i></p>
<dd> Specify what is considered to be a nice length for a match. Once a match of at least <i>nice</i> bytes is found, the algorithm stops looking for possibly better matches.</p>
<dt>
<dd> <i>Nice</i> can be 2-273 bytes. Higher values tend to give better compression ratio at the expense of speed. The default depends on the <i>preset</i>.</p>
<dt><code>depth=</code><i>depth</i></p>
<dd> Specify the maximum search depth in the match finder. The default is the special value of 0, which makes the compressor determine a reasonable <i>depth</i> from <i>mf</i> and <i>nice</i>.</p>
<dt>
<dd> Reasonable <i>depth</i> for Hash Chains is 4-100 and 16-1000 for Binary Trees. Using very high values for <i>depth</i> can make the encoder extremely slow with some files. Avoid setting the <i>depth</i> over 1000 unless you are prepared to interrupt the compression in case it is taking far too long.</dl>
</dl>
<dt>
<dd> When decoding raw streams (<code>&#8211;format=raw</code>), LZMA2 needs only the dictionary <i>size</i>. LZMA1 needs also <i>lc</i>, <i>lp</i>, and <i>pb</i>.</p>
<dt><code>&#8211;x86</code>[<code>=</code><i>options</i>]</p>
<dd>
<dt><code>&#8211;powerpc</code>[<code>=</code><i>options</i>]</p>
<dd>
<dt><code>&#8211;ia64</code>[<code>=</code><i>options</i>]</p>
<dd>
<dt><code>&#8211;arm</code>[<code>=</code><i>options</i>]</p>
<dd>
<dt><code>&#8211;armthumb</code>[<code>=</code><i>options</i>]</p>
<dd>
<dt><code>&#8211;sparc</code>[<code>=</code><i>options</i>]</p>
<dd> Add a branch/call/jump (BCJ) filter to the filter chain. These filters can be used only as a non-last filter in the filter chain.</p>
<dt>
<dd> A BCJ filter converts relative addresses in the machine code to their absolute counterparts. This doesn&#8217;t change the size of the data, but it increases redundancy, which can help LZMA2 to produce 0-15&nbsp;% smaller <code>.xz</code> file. The BCJ filters are always reversible, so using a BCJ filter for wrong type of data doesn&#8217;t cause any data loss, although it may make the compression ratio slightly worse.</p>
<dt>
<dd> It is fine to apply a BCJ filter on a whole executable; there&#8217;s no need to apply it only on the executable section. Applying a BCJ filter on an archive that contains both executable and non-executable files may or may not give good results, so it generally isn&#8217;t good to blindly apply a BCJ filter when compressing binary packages for distribution.</p>
<dt>
<dd> These BCJ filters are very fast and use insignificant amount of memory. If a BCJ filter improves compression ratio of a file, it can improve decompression speed at the same time. This is because, on the same hardware, the decompression speed of LZMA2 is roughly a fixed number of bytes of compressed data per second.</p>
<dt>
<dd> These BCJ filters have known problems related to the compression ratio:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Some types of files containing executable code (for example, object files, static libraries, and Linux kernel modules) have the addresses in the instructions filled with filler values. These BCJ filters will still do the address conversion, which will make the compression worse with these files.</p>
<dt>&bull;</p>
<dd> Applying a BCJ filter on an archive containing multiple similar executables can make the compression ratio worse than not using a BCJ filter. This is because the BCJ filter doesn&#8217;t detect the boundaries of the executable files, and doesn&#8217;t reset the address conversion counter for each executable.</dl>
</dl>
<dt>
<dd> Both of the above problems will be fixed in the future in a new filter. The old BCJ filters will still be useful in embedded systems, because the decoder of the new filter will be bigger and use more memory.</p>
<dt>
<dd> Different instruction sets have different alignment:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>Filter</td>
<td ALIGN=right>Alignment&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td>x86</td>
<td ALIGN=right>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>32-bit or 64-bit x86
</td>
</tr>
<tr VALIGN=top>
<td>PowerPC</td>
<td ALIGN=right>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>Big endian only
</td>
</tr>
<tr VALIGN=top>
<td>ARM</td>
<td ALIGN=right>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>Little endian only
</td>
</tr>
<tr VALIGN=top>
<td>ARM-Thumb</td>
<td ALIGN=right>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>Little endian only
</td>
</tr>
<tr VALIGN=top>
<td>IA-64</td>
<td ALIGN=right>16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>Big or little endian
</td>
</tr>
<tr VALIGN=top>
<td>SPARC</td>
<td ALIGN=right>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>Big or little endian
</td>
</tr>
</table>
</dl>
</dl>
<dt>
<dd> Since the BCJ-filtered data is usually compressed with LZMA2, the compression ratio may be improved slightly if the LZMA2 options are set to match the alignment of the selected BCJ filter. For example, with the IA-64 filter, it&#8217;s good to set <code>pb=4</code> with LZMA2 (2^4=16). The x86 filter is an exception; it&#8217;s usually good to stick to LZMA2&#8217;s default four-byte alignment when compressing x86 executables.</p>
<dt>
<dd> All BCJ filters support the same <i>options</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>start=</code><i>offset</i></p>
<dd> Specify the start <i>offset</i> that is used when converting between relative and absolute addresses. The <i>offset</i> must be a multiple of the alignment of the filter (see the table above). The default is zero. In practice, the default is good; specifying a custom <i>offset</i> is almost never useful.</dl>
</dl>
<dt><code>&#8211;delta</code>[<code>=</code><i>options</i>]</p>
<dd> Add the Delta filter to the filter chain. The Delta filter can be only used as a non-last filter in the filter chain.</p>
<dt>
<dd> Currently only simple byte-wise delta calculation is supported. It can be useful when compressing, for example, uncompressed bitmap images or uncompressed PCM audio. However, special purpose algorithms may give significantly better results than Delta + LZMA2. This is true especially with audio, which compresses faster and better, for example, with <code><a href="/docs/linux/man/1-flac/">flac</a></code>(1).</p>
<dt>
<dd> Supported <i>options</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>dist=</code><i>distance</i></p>
<dd> Specify the <i>distance</i> of the delta calculation in bytes. <i>distance</i> must be 1-256. The default is 1.</p>
<dt>
<dd> For example, with <code>dist=2</code> and eight-byte input A1 B1 A2 B3 A3 B5 A4 B7, the output will be A1 B1 01 02 01 02 01 02.</dl>
</dl>
</dl>
<h3>Other options</h3>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress warnings and notices. Specify this twice to suppress errors too. This option has no effect on the exit status. That is, even if a warning was suppressed, the exit status to indicate a warning is still used.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose. If standard error is connected to a terminal, <code>xz</code> will display a progress indicator. Specifying <code>&#8211;verbose</code> twice will give even more verbose output.</p>
<dt>
<dd> The progress indicator shows the following information:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Completion percentage is shown if the size of the input file is known. That is, the percentage cannot be shown in pipes.</p>
<dt>&bull;</p>
<dd> Amount of compressed data produced (compressing) or consumed (decompressing).</p>
<dt>&bull;</p>
<dd> Amount of uncompressed data consumed (compressing) or produced (decompressing).</p>
<dt>&bull;</p>
<dd> Compression ratio, which is calculated by dividing the amount of compressed data processed so far by the amount of uncompressed data processed so far.</p>
<dt>&bull;</p>
<dd> Compression or decompression speed. This is measured as the amount of uncompressed data consumed (compression) or produced (decompression) per second. It is shown after a few seconds have passed since <code>xz</code> started processing the file.</p>
<dt>&bull;</p>
<dd> Elapsed time in the format M:SS or H:MM:SS.</p>
<dt>&bull;</p>
<dd> Estimated remaining time is shown only when the size of the input file is known and a couple of seconds have already passed since <code>xz</code> started processing the file. The time is shown in a less precise format which never has any colons, for example, 2 min 30 s.</dl>
</dl>
<dt>
<dd> When standard error is not a terminal, <code>&#8211;verbose</code> will make <code>xz</code> print the filename, compressed size, uncompressed size, compression ratio, and possibly also the speed and elapsed time on a single line to standard error after compressing or decompressing the file. The speed and elapsed time are included only when the operation took at least a few seconds. If the operation didn&#8217;t finish, for example, due to user interruption, also the completion percentage is printed if the size of the input file is known.</p>
<dt><code>-Q</code>, <code>&#8211;no-warn</code></p>
<dd> Don&#8217;t set the exit status to 2 even if a condition worth a warning was detected. This option doesn&#8217;t affect the verbosity level, thus both <code>&#8211;quiet</code> and <code>&#8211;no-warn</code> have to be used to not display warnings and to not alter the exit status.</p>
<dt><code>&#8211;robot</code></p>
<dd> Print messages in a machine-parsable format. This is intended to ease writing frontends that want to use <code>xz</code> instead of liblzma, which may be the case with various scripts. The output with this option enabled is meant to be stable across <code>xz</code> releases. See the section <code>ROBOT MODE</code> for details.</p>
<dt><code>&#8211;info-memory</code></p>
<dd> Display, in human-readable format, how much physical memory (RAM) <code>xz</code> thinks the system has and the memory usage limits for compression and decompression, and exit successfully.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a help message describing the most commonly used options, and exit successfully.</p>
<dt><code>-H</code>, <code>&#8211;long-help</code></p>
<dd> Display a help message describing all features of <code>xz</code>, and exit successfully</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display the version number of <code>xz</code> and liblzma in human readable format. To get machine-parsable output, specify <code>&#8211;robot</code> before <code>&#8211;version</code>.</dl>
<h2>ROBOT MODE</h2>
<p> The robot mode is activated with the <code>&#8211;robot</code> option. It makes the output of <code>xz</code> easier to parse by other programs. Currently <code>&#8211;robot</code> is supported only together with <code>&#8211;version</code>, <code>&#8211;info-memory</code>, and <code>&#8211;list</code>. It will be supported for compression and decompression in the future.</p>
<h3>Version</h3>
<p> <code>xz &#8211;robot &#8211;version</code> will print the version number of <code>xz</code> and liblzma in the following format: </p>
<p> <code>XZ_VERSION=</code><i>XYYYZZZS</i><br />
 <code>LIBLZMA_VERSION=</code><i>XYYYZZZS</i></p>
<dl>
<dt><i>X</i></p>
<dd> Major version.</p>
<dt><i>YYY</i></p>
<dd> Minor version. Even numbers are stable. Odd numbers are alpha or beta versions.</p>
<dt><i>ZZZ</i></p>
<dd> Patch level for stable releases or just a counter for development releases.</p>
<dt><i>S</i></p>
<dd> Stability. 0 is alpha, 1 is beta, and 2 is stable. <i>S</i> should be always 2 when <i>YYY</i> is even.</dl>
<p> <i>XYYYZZZS</i> are the same on both lines if <code>xz</code> and liblzma are from the same XZ Utils release. </p>
<p> Examples: 4.999.9beta is <code>49990091</code> and 5.0.0 is <code>50000002</code>.</p>
<h3>Memory limit information</h3>
<p> <code>xz &#8211;robot &#8211;info-memory</code> prints a single line with three tab-separated columns:</p>
<dl>
<dt>1.</p>
<dd> Total amount of physical memory (RAM) in bytes</p>
<dt>2.</p>
<dd> Memory usage limit for compression in bytes. A special value of zero indicates the default setting, which for single-threaded mode is the same as no limit.</p>
<dt>3.</p>
<dd> Memory usage limit for decompression in bytes. A special value of zero indicates the default setting, which for single-threaded mode is the same as no limit.</dl>
<p> In the future, the output of <code>xz &#8211;robot &#8211;info-memory</code> may have more columns, but never more than a single line.</p>
<h3>List mode</h3>
<p> <code>xz &#8211;robot &#8211;list</code> uses tab-separated output. The first column of every line has a string that indicates the type of the information found on that line:</p>
<dl>
<dt><code>name</code></p>
<dd> This is always the first line when starting to list a file. The second column on the line is the filename.</p>
<dt><code>file</code></p>
<dd> This line contains overall information about the <code>.xz</code> file. This line is always printed after the <code>name</code> line.</p>
<dt><code>stream</code></p>
<dd> This line type is used only when <code>&#8211;verbose</code> was specified. There are as many <code>stream</code> lines as there are streams in the <code>.xz</code> file.</p>
<dt><code>block</code></p>
<dd> This line type is used only when <code>&#8211;verbose</code> was specified. There are as many <code>block</code> lines as there are blocks in the <code>.xz</code> file. The <code>block</code> lines are shown after all the <code>stream</code> lines; different line types are not interleaved.</p>
<dt><code>summary</code></p>
<dd> This line type is used only when <code>&#8211;verbose</code> was specified twice. This line is printed after all <code>block</code> lines. Like the <code>file</code> line, the <code>summary</code> line contains overall information about the <code>.xz</code> file.</p>
<dt><code>totals</code></p>
<dd> This line is always the very last line of the list output. It shows the total counts and sizes.</dl>
<p> The columns of the <code>file</code> lines:</p>
<dl>
<dt>
<dd>
<dl>
<dt>2.</p>
<dd> Number of streams in the file</p>
<dt>3.</p>
<dd> Total number of blocks in the stream(s)</p>
<dt>4.</p>
<dd> Compressed size of the file</p>
<dt>5.</p>
<dd> Uncompressed size of the file</p>
<dt>6.</p>
<dd> Compression ratio, for example, <code>0.123</code>. If ratio is over 9.999, three dashes (<code>&#8212;</code>) are displayed instead of the ratio.</p>
<dt>7.</p>
<dd> Comma-separated list of integrity check names. The following strings are used for the known check types: <code>None</code>, <code>CRC32</code>, <code>CRC64</code>, and <code>SHA-256</code>. For unknown check types, <code>Unknown-</code><i>N</i> is used, where <i>N</i> is the Check ID as a decimal number (one or two digits).</p>
<dt>8.</p>
<dd> Total size of stream padding in the file</dl>
</dl>
<p> The columns of the <code>stream</code> lines:</p>
<dl>
<dt>
<dd>
<dl>
<dt>2.</p>
<dd> Stream number (the first stream is 1)</p>
<dt>3.</p>
<dd> Number of blocks in the stream</p>
<dt>4.</p>
<dd> Compressed start offset</p>
<dt>5.</p>
<dd> Uncompressed start offset</p>
<dt>6.</p>
<dd> Compressed size (does not include stream padding)</p>
<dt>7.</p>
<dd> Uncompressed size</p>
<dt>8.</p>
<dd> Compression ratio</p>
<dt>9.</p>
<dd> Name of the integrity check</p>
<dt>10.</p>
<dd> Size of stream padding</dl>
</dl>
<p> The columns of the <code>block</code> lines:</p>
<dl>
<dt>
<dd>
<dl>
<dt>2.</p>
<dd> Number of the stream containing this block</p>
<dt>3.</p>
<dd> Block number relative to the beginning of the stream (the first block is 1)</p>
<dt>4.</p>
<dd> Block number relative to the beginning of the file</p>
<dt>5.</p>
<dd> Compressed start offset relative to the beginning of the file</p>
<dt>6.</p>
<dd> Uncompressed start offset relative to the beginning of the file</p>
<dt>7.</p>
<dd> Total compressed size of the block (includes headers)</p>
<dt>8.</p>
<dd> Uncompressed size</p>
<dt>9.</p>
<dd> Compression ratio</p>
<dt>10.</p>
<dd> Name of the integrity check</dl>
</dl>
<p> If <code>&#8211;verbose</code> was specified twice, additional columns are included on the <code>block</code> lines. These are not displayed with a single <code>&#8211;verbose</code>, because getting this information requires many seeks and can thus be slow:</p>
<dl>
<dt>
<dd>
<dl>
<dt>11.</p>
<dd> Value of the integrity check in hexadecimal</p>
<dt>12.</p>
<dd> Block header size</p>
<dt>13.</p>
<dd> Block flags: <code>c</code> indicates that compressed size is present, and <code>u</code> indicates that uncompressed size is present. If the flag is not set, a dash (<code>&#8211;</code>) is shown instead to keep the string length fixed. New flags may be added to the end of the string in the future.</p>
<dt>14.</p>
<dd> Size of the actual compressed data in the block (this excludes the block header, block padding, and check fields)</p>
<dt>15.</p>
<dd> Amount of memory (in bytes) required to decompress this block with this <code>xz</code> version</p>
<dt>16.</p>
<dd> Filter chain. Note that most of the options used at compression time cannot be known, because only the options that are needed for decompression are stored in the <code>.xz</code> headers.</dl>
</dl>
<p> The columns of the <code>summary</code> lines:</p>
<dl>
<dt>
<dd>
<dl>
<dt>2.</p>
<dd> Amount of memory (in bytes) required to decompress this file with this <code>xz</code> version</p>
<dt>3.</p>
<dd> <code>yes</code> or <code>no</code> indicating if all block headers have both compressed size and uncompressed size stored in them</dl>
<p> <i>Since</i> <code>xz</code> <i>5.1.2alpha:</i></p>
<dl>
<dt>4.</p>
<dd> Minimum <code>xz</code> version required to decompress the file</dl>
</dl>
<p> The columns of the <code>totals</code> line:</p>
<dl>
<dt>
<dd>
<dl>
<dt>2.</p>
<dd> Number of streams</p>
<dt>3.</p>
<dd> Number of blocks</p>
<dt>4.</p>
<dd> Compressed size</p>
<dt>5.</p>
<dd> Uncompressed size</p>
<dt>6.</p>
<dd> Average compression ratio</p>
<dt>7.</p>
<dd> Comma-separated list of integrity check names that were present in the files</p>
<dt>8.</p>
<dd> Stream padding size</p>
<dt>9.</p>
<dd> Number of files. This is here to keep the order of the earlier columns the same as on <code>file</code> lines.</dl>
</dl>
<p> If <code>&#8211;verbose</code> was specified twice, additional columns are included on the <code>totals</code> line:</p>
<dl>
<dt>
<dd>
<dl>
<dt>10.</p>
<dd> Maximum amount of memory (in bytes) required to decompress the files with this <code>xz</code> version</p>
<dt>11.</p>
<dd> <code>yes</code> or <code>no</code> indicating if all block headers have both compressed size and uncompressed size stored in them</dl>
<p> <i>Since</i> <code>xz</code> <i>5.1.2alpha:</i></p>
<dl>
<dt>12.</p>
<dd> Minimum <code>xz</code> version required to decompress the file</dl>
</dl>
<p> Future versions may add new line types and new columns can be added to the existing line types, but the existing columns won&#8217;t be changed.</p>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> All is good.</p>
<dt><code>1</code></p>
<dd> An error occurred.</p>
<dt><code>2</code></p>
<dd> Something worth a warning occurred, but no actual errors occurred.</dl>
<p> Notices (not warnings or errors) printed on standard error don&#8217;t affect the exit status.</p>
<h2>ENVIRONMENT</h2>
<p> <code>xz</code> parses space-separated lists of options from the environment variables <code>XZ_DEFAULTS</code> and <code>XZ_OPT</code>, in this order, before parsing the options from the command line. Note that only options are parsed from the environment variables; all non-options are silently ignored. Parsing is done with <code><a href="/docs/linux/man/3-getopt_long/">getopt_long</a></code>(3) which is used also for the command line arguments.</p>
<dl>
<dt><code>XZ_DEFAULTS</code></p>
<dd> User-specific or system-wide default options. Typically this is set in a shell initialization script to enable <code>xz</code>&#8216;s memory usage limiter by default. Excluding shell initialization scripts and similar special cases, scripts must never set or unset <code>XZ_DEFAULTS</code>.</p>
<dt><code>XZ_OPT</code></p>
<dd> This is for passing options to <code>xz</code> when it is not possible to set the options directly on the <code>xz</code> command line. This is the case when <code>xz</code> is run by a script or tool, for example, GNU <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
XZ_OPT=-2v tar caf foo.tar.xz foo
</pre>
</dl>
</dl>
<dt>
<dd> Scripts may use <code>XZ_OPT</code>, for example, to set script-specific default compression options. It is still recommended to allow users to override <code>XZ_OPT</code> if that is reasonable. For example, in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) scripts one may use something like this:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
XZ_OPT=${XZ_OPT-&quot;-7e&quot;}
export XZ_OPT
</pre>
</dl>
</dl>
</dl>
<h2>LZMA UTILS COMPATIBILITY</h2>
<p> The command line syntax of <code>xz</code> is practically a superset of <code>lzma</code>, <code>unlzma</code>, and <code>lzcat</code> as found from LZMA Utils 4.32.x. In most cases, it is possible to replace LZMA Utils with XZ Utils without breaking existing scripts. There are some incompatibilities though, which may sometimes cause problems.</p>
<h3>Compression preset levels</h3>
<p> The numbering of the compression level presets is not identical in <code>xz</code> and LZMA Utils. The most important difference is how dictionary sizes are mapped to different presets. Dictionary size is roughly equal to the decompressor memory usage.</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center>Level</td>
<td ALIGN=center>xz</td>
<td ALIGN=center>LZMA Utils
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-0</td>
<td ALIGN=right>256 KiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>N/A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-1</td>
<td ALIGN=right>1 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>64 KiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-2</td>
<td ALIGN=right>2 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>1 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-3</td>
<td ALIGN=right>4 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>512 KiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-4</td>
<td ALIGN=right>4 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>1 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-5</td>
<td ALIGN=right>8 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>2 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-6</td>
<td ALIGN=right>8 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>4 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-7</td>
<td ALIGN=right>16 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-8</td>
<td ALIGN=right>32 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>16 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-9</td>
<td ALIGN=right>64 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>32 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
</table>
</dl>
<p> The dictionary size differences affect the compressor memory usage too, but there are some other differences between LZMA Utils and XZ Utils, which make the difference even bigger:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center>Level</td>
<td ALIGN=center>xz</td>
<td ALIGN=center>LZMA Utils 4.32.x
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-0</td>
<td ALIGN=right>3 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>N/A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-1</td>
<td ALIGN=right>9 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>2 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-2</td>
<td ALIGN=right>17 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>12 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-3</td>
<td ALIGN=right>32 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>12 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-4</td>
<td ALIGN=right>48 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>16 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-5</td>
<td ALIGN=right>94 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>26 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-6</td>
<td ALIGN=right>94 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>45 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-7</td>
<td ALIGN=right>186 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>83 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-8</td>
<td ALIGN=right>370 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>159 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-9</td>
<td ALIGN=right>674 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>311 MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
</table>
</dl>
<p> The default preset level in LZMA Utils is <code>-7</code> while in XZ Utils it is <code>-6</code>, so both use an 8 MiB dictionary by default.</p>
<h3>Streamed vs. non-streamed .lzma files</h3>
<p> The uncompressed size of the file can be stored in the <code>.lzma</code> header. LZMA Utils does that when compressing regular files. The alternative is to mark that uncompressed size is unknown and use end-of-payload marker to indicate where the decompressor should stop. LZMA Utils uses this method when uncompressed size isn&#8217;t known, which is the case, for example, in pipes. </p>
<p> <code>xz</code> supports decompressing <code>.lzma</code> files with or without end-of-payload marker, but all <code>.lzma</code> files created by <code>xz</code> will use end-of-payload marker and have uncompressed size marked as unknown in the <code>.lzma</code> header. This may be a problem in some uncommon situations. For example, a <code>.lzma</code> decompressor in an embedded device might work only with files that have known uncompressed size. If you hit this problem, you need to use LZMA Utils or LZMA SDK to create <code>.lzma</code> files with known uncompressed size.</p>
<h3>Unsupported .lzma files</h3>
<p> The <code>.lzma</code> format allows <i>lc</i> values up to 8, and <i>lp</i> values up to 4. LZMA Utils can decompress files with any <i>lc</i> and <i>lp</i>, but always creates files with <code>lc=3</code> and <code>lp=0</code>. Creating files with other <i>lc</i> and <i>lp</i> is possible with <code>xz</code> and with LZMA SDK. </p>
<p> The implementation of the LZMA1 filter in liblzma requires that the sum of <i>lc</i> and <i>lp</i> must not exceed 4. Thus, <code>.lzma</code> files, which exceed this limitation, cannot be decompressed with <code>xz</code>. </p>
<p> LZMA Utils creates only <code>.lzma</code> files which have a dictionary size of 2^<i>n</i> (a power of 2) but accepts files with any dictionary size. liblzma accepts only <code>.lzma</code> files which have a dictionary size of 2^<i>n</i> or 2^<i>n</i> + 2^(<i>n</i>-1). This is to decrease false positives when detecting <code>.lzma</code> files. </p>
<p> These limitations shouldn&#8217;t be a problem in practice, since practically all <code>.lzma</code> files have been compressed with settings that liblzma will accept.</p>
<h3>Trailing garbage</h3>
<p> When decompressing, LZMA Utils silently ignore everything after the first <code>.lzma</code> stream. In most situations, this is a bug. This also means that LZMA Utils don&#8217;t support decompressing concatenated <code>.lzma</code> files. </p>
<p> If there is data left after the first <code>.lzma</code> stream, <code>xz</code> considers the file to be corrupt unless <code>&#8211;single-stream</code> was used. This may break obscure scripts which have assumed that trailing garbage is ignored.</p>
<h2>NOTES</h2>
<h3>Compressed output may vary</h3>
<p> The exact compressed output produced from the same uncompressed input file may vary between XZ Utils versions even if compression options are identical. This is because the encoder can be improved (faster or better compression) without affecting the file format. The output can vary even between different builds of the same XZ Utils version, if different build options are used. </p>
<p> The above means that once <code>&#8211;rsyncable</code> has been implemented, the resulting files won&#8217;t necessarily be rsyncable unless both old and new files have been compressed with the same xz version. This problem can be fixed if a part of the encoder implementation is frozen to keep rsyncable output stable across xz versions.</p>
<h3>Embedded .xz decompressors</h3>
<p> Embedded <code>.xz</code> decompressor implementations like XZ Embedded don&#8217;t necessarily support files created with integrity <i>check</i> types other than <code>none</code> and <code>crc32</code>. Since the default is <code>&#8211;check=crc64</code>, you must use <code>&#8211;check=none</code> or <code>&#8211;check=crc32</code> when creating files for embedded systems. </p>
<p> Outside embedded systems, all <code>.xz</code> format decompressors support all the <i>check</i> types, or at least are able to decompress the file without verifying the integrity check if the particular <i>check</i> is not supported. </p>
<p> XZ Embedded supports BCJ filters, but only with the default start offset.</p>
<h2>EXAMPLES</h2>
<h3>Basics</h3>
<p> Compress the file <i>foo</i> into <i>foo.xz</i> using the default compression level (<code>-6</code>), and remove <i>foo</i> if compression is successful:</p>
<dl>
<dt>
<dd>
<pre>
xz foo
</pre>
</dl>
<p> Decompress <i>bar.xz</i> into <i>bar</i> and don&#8217;t remove <i>bar.xz</i> even if decompression is successful:</p>
<dl>
<dt>
<dd>
<pre>
xz -dk bar.xz
</pre>
</dl>
<p> Create <i>baz.tar.xz</i> with the preset <code>-4e</code> (<code>-4 &#8211;extreme</code>), which is slower than the default <code>-6</code>, but needs less memory for compression and decompression (48 MiB and 5 MiB, respectively):</p>
<dl>
<dt>
<dd>
<pre>
tar cf - baz | xz -4e &gt; baz.tar.xz
</pre>
</dl>
<p> A mix of compressed and uncompressed files can be decompressed to standard output with a single command:</p>
<dl>
<dt>
<dd>
<pre>
xz -dcf a.txt b.txt.xz c.txt d.txt.lzma &gt; abcd.txt
</pre>
</dl>
<h3>Parallel compression of many files</h3>
<p> On GNU and *BSD, <code><a href="/docs/linux/man/1-find/">find</a></code>(1) and <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1) can be used to parallelize compression of many files:</p>
<dl>
<dt>
<dd>
<pre>
find . -type f \! -name '*.xz' -print0 \
    | xargs -0r -P4 -n16 xz -T1
</pre>
</dl>
<p> The <code>-P</code> option to <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1) sets the number of parallel <code>xz</code> processes. The best value for the <code>-n</code> option depends on how many files there are to be compressed. If there are only a couple of files, the value should probably be 1; with tens of thousands of files, 100 or even more may be appropriate to reduce the number of <code>xz</code> processes that <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1) will eventually create. </p>
<p> The option <code>-T1</code> for <code>xz</code> is there to force it to single-threaded mode, because <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1) is used to control the amount of parallelization.</p>
<h3>Robot mode</h3>
<p> Calculate how many bytes have been saved in total after compressing multiple files:</p>
<dl>
<dt>
<dd>
<pre><code>
xz-- robot-- list *.xz | awk '/^totals/{print $5-$4}'
</code></pre>
</dl>
<p> A script may want to know that it is using new enough <code>xz</code>. The following <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) script checks that the version number of the <code>xz</code> tool is at least 5.0.0. This method is compatible with old beta versions, which didn&#8217;t support the <code>&#8211;robot</code> option:</p>
<dl>
<dt>
<dd>
<p>if<br />
    !eval &#8220;$(xz &#8211;robot &#8211;version 2&gt; /dev/null)&#8221; ||<br />
        [&#8220;$XZ_VERSION&#8221; &#8211; lt 50000002];<br />
then<br />
    echo &#8220;Your xz is too old.&#8221; fi<br />
        unset XZ_VERSION LIBLZMA_VERSION
</dl>
<p> Set a memory usage limit for decompression using <code>XZ_OPT</code>, but if a limit has already been set, don&#8217;t increase it:</p>
<dl>
<dt>
<dd>
<pre><code>
NEWLIM = $((123 &lt;&lt; 20)) &amp; nbsp;
&amp;nbsp;
# 123 MiB OLDLIM = $(xz -- robot -- info - memory | cut - f3) if[$OLDLIM - eq 0 - o $OLDLIM - gt $NEWLIM];
then
    XZ_OPT = "$XZ_OPT --memlimit-decompress=$NEWLIM" export XZ_OPT
        fi
</code></pre>
</dl>
<h3>Custom compressor filter chains</h3>
<p> The simplest use for custom filter chains is customizing a LZMA2 preset. This can be useful, because the presets cover only a subset of the potentially useful combinations of compression settings. </p>
<p> The CompCPU columns of the tables from the descriptions of the options <code>-0</code> &#8230; <code>-9</code> and <code>&#8211;extreme</code> are useful when customizing LZMA2 presets. Here are the relevant parts collected from those two tables:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center>Preset</td>
<td ALIGN=center>CompCPU
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-5e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>-6e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
</table>
</dl>
<p> If you know that a file requires somewhat big dictionary (for example, 32 MiB) to compress well, but you want to compress it quicker than <code>xz -8</code> would do, a preset with a low CompCPU value (for example, 1) can be modified to use a bigger dictionary:</p>
<dl>
<dt>
<dd>
<pre>
xz --lzma2=preset=1,dict=32MiB foo.tar
</pre>
</dl>
<p> With certain files, the above command may be faster than <code>xz -6</code> while compressing significantly better. However, it must be emphasized that only some files benefit from a big dictionary while keeping the CompCPU value low. The most obvious situation, where a big dictionary can help a lot, is an archive containing very similar files of at least a few megabytes each. The dictionary size has to be significantly bigger than any individual file to allow LZMA2 to take full advantage of the similarities between consecutive files. </p>
<p> If very high compressor and decompressor memory usage is fine, and the file being compressed is at least several hundred megabytes, it may be useful to use an even bigger dictionary than the 64 MiB that <code>xz -9</code> would use:</p>
<dl>
<dt>
<dd>
<pre>
xz -vv --lzma2=dict=192MiB big_foo.tar
</pre>
</dl>
<p> Using <code>-vv</code> (<code>&#8211;verbose &#8211;verbose</code>) like in the above example can be useful to see the memory requirements of the compressor and decompressor. Remember that using a dictionary bigger than the size of the uncompressed file is waste of memory, so the above command isn&#8217;t useful for small files. </p>
<p> Sometimes the compression time doesn&#8217;t matter, but the decompressor memory usage has to be kept low, for example, to make it possible to decompress the file on an embedded system. The following command uses <code>-6e</code> (<code>-6 &#8211;extreme</code>) as a base and sets the dictionary to only 64 KiB. The resulting file can be decompressed with XZ Embedded (that&#8217;s why there is <code>&#8211;check=crc32</code>) using about 100 KiB of memory.</p>
<dl>
<dt>
<dd>
<pre>
xz --check=crc32 --lzma2=preset=6e,dict=64KiB foo
</pre>
</dl>
<p> If you want to squeeze out as many bytes as possible, adjusting the number of literal context bits (<i>lc</i>) and number of position bits (<i>pb</i>) can sometimes help. Adjusting the number of literal position bits (<i>lp</i>) might help too, but usually <i>lc</i> and <i>pb</i> are more important. For example, a source code archive contains mostly US-ASCII text, so something like the following might give slightly (like 0.1&nbsp;%) smaller file than <code>xz -6e</code> (try also without <code>lc=4</code>):</p>
<dl>
<dt>
<dd>
<pre>
xz --lzma2=preset=6e,pb=0,lc=4 source_code.tar
</pre>
</dl>
<p> Using another filter together with LZMA2 can improve compression with certain file types. For example, to compress a x86-32 or x86-64 shared library using the x86 BCJ filter:</p>
<dl>
<dt>
<dd>
<pre>
xz --x86 --lzma2 libfoo.so
</pre>
</dl>
<p> Note that the order of the filter options is significant. If <code>&#8211;x86</code> is specified after <code>&#8211;lzma2</code>, <code>xz</code> will give an error, because there cannot be any filter after LZMA2, and also because the x86 BCJ filter cannot be used as the last filter in the chain. </p>
<p> The Delta filter together with LZMA2 can give good results with bitmap images. It should usually beat PNG, which has a few more advanced filters than simple delta but uses Deflate for the actual compression. </p>
<p> The image has to be saved in uncompressed format, for example, as uncompressed TIFF. The distance parameter of the Delta filter is set to match the number of bytes per pixel in the image. For example, 24-bit RGB bitmap needs <code>dist=3</code>, and it is also good to pass <code>pb=0</code> to LZMA2 to accommodate the three-byte alignment:</p>
<dl>
<dt>
<dd>
<pre>
xz --delta=dist=3 --lzma2=pb=0 foo.tiff
</pre>
</dl>
<p> If multiple images have been put into a single archive (for example, <code>.tar</code>), the Delta filter will work on that too as long as all images have the same number of bytes per pixel.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xzdec/">xzdec</a></code>(1), <code><a href="/docs/linux/man/1-xzdiff/">xzdiff</a></code>(1), <code><a href="/docs/linux/man/1-xzgrep/">xzgrep</a></code>(1), <code><a href="/docs/linux/man/1-xzless/">xzless</a></code>(1), <code><a href="/docs/linux/man/1-xzmore/">xzmore</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-7z/">7z</a></code>(1) </p>
<p> XZ Utils: &lt;<a rel="nofollow" href="https://tukaani.org/xz/">https://tukaani.org/xz/</a>&gt;<br />
 XZ Embedded: &lt;<a rel="nofollow" href="https://tukaani.org/xz/embedded.html">https://tukaani.org/xz/embedded.html</a>&gt;<br />
 LZMA SDK: &lt;<a rel="nofollow" href="http://7-zip.org/sdk.html">http://7-zip.org/sdk.html</a>&gt; </p>
<h2>Index</h2>
