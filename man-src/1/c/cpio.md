---
title: "cpio(1)"
name: "cpio"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpio/"
description: "cpio – copy files to and from archives"
---

<h2 class="name">NAME</h2>
<p> cpio &#8211; copy files to and from archives </p>
<h2>SYNOPSIS</h2>
<p> <code>cpio</code> {<code>-o</code>|<code>&#8211;create</code>} [<code>-0acvABLV</code>] [<code>-C</code> <i>BYTES</i>] [<code>-H</code> <i>FORMAT</i>] [<code>-M</code> <i>MESSAGE</i>] [<code>-O</code> [[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE</i>] [<code>-F</code> [[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE</i>] [<code>&#8211;file=</code>[[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE</i>] [<code>&#8211;format=</code><i>FORMAT</i>] [<code>&#8211;message=</code><i>MESSAGE</i>] [<code>&#8211;null</code>] [<code>&#8211;reset-access-time</code>] [<code>&#8211;verbose</code>] [<code>&#8211;dot</code>] [<code>&#8211;append</code>] [<code>&#8211;block-size=</code><i>blocks</i>] [<code>&#8211;dereference</code>] [<code>&#8211;io-size=</code><i>BYTES</i>] [<code>&#8211;quiet</code>] [<code>&#8211;force-local</code>] [<code>&#8211;rsh-command=</code><i>COMMAND</i>] <code>&lt;</code> <i>name-list</i> [<code>&gt;</code> <i>archive</i>] </p>
<p> <code>cpio</code> {<code>-i</code>|<code>&#8211;extract</code>} [<code>-bcdfmnrtsuvBSV</code>] [<code>-C</code> <i>BYTES</i>] [<code>-E</code> <i>FILE</i>] [<code>-H</code> <i>FORMAT</i>] [<code>-M</code> <i>MESSAGE</i>] [<code>-R</code> [<i>USER</i>][<code>:.</code>][<i>GROUP</i>]] [<code>-I</code> [[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE</i>] [<code>-F</code> [[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE</i>] [<code>&#8211;file=</code>[[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE</i>] [<code>&#8211;make-directories</code>] [<code>&#8211;nonmatching</code>] [<code>&#8211;preserve-modification-time</code>] [<code>&#8211;numeric-uid-gid</code>] [<code>&#8211;rename</code>] [<code>&#8211;list</code>] [<code>&#8211;swap-bytes</code>] [<code>&#8211;swap</code>] [<code>&#8211;dot</code>] [<code>&#8211;unconditional</code>] [<code>&#8211;verbose</code>] [<code>&#8211;block-size=</code><i>BLOCKS</i>] [<code>&#8211;swap-halfwords</code>] [<code>&#8211;io-size=</code><i>BYTES</i>] [<code>&#8211;pattern-file=</code><i>FILE</i>] [<code>&#8211;format=</code><i>FORMAT</i>] [<code>&#8211;owner=</code>[<i>USER][</i><code>:.</code>][<i>GROUP</i>]] [<code>&#8211;no-preserve-owner</code>] [<code>&#8211;message=</code><i>MESSAGE</i>] [<code>&#8211;force-local</code>] [<code>&#8211;no-absolute-filenames</code>] [<code>&#8211;sparse</code>] [<code>&#8211;only-verify-crc</code>] [<code>&#8211;to-stdout</code>] [<code>&#8211;quiet</code>] [<code>&#8211;rsh-command=</code><i>COMMAND</i>] [<i>pattern</i>&#8230;] [<code>&lt;</code> <i>archive</i>] </p>
<p> <code>cpio</code> {<code>-p</code>|<code>&#8211;pass-through</code>} [<code>-0adlmuvLV</code>] [<code>-R</code> [<i>USER</i>][<code>:.</code>][<i>GROUP</i>]] [<code>&#8211;null</code>] [<code>&#8211;reset-access-time</code>] [<code>&#8211;make-directories</code>] [<code>&#8211;link</code>] [<code>&#8211;quiet</code>] [<code>&#8211;preserve-modification-time] [&#8211;unconditional</code>] [<code>&#8211;verbose</code>] [<code>&#8211;dot</code>] [<code>&#8211;dereference</code>] [<code>&#8211;owner=</code>[<i>USER</i>][<code>:.</code>][<i>GROUP</i>]] [<code>&#8211;no-preserve-owner</code>] [<code>&#8211;sparse</code>] <i>destination-directory</i> <code>&lt;</code> <i>name-list</i> </p>
<p> <code>cpio</code> {<code>-?</code>|<code>&#8211;help</code>|<code>&#8211;usage</code>|<code>&#8211;version</code>}</p>
<h2>REPORTING BUGS</h2>
<p> Report cpio bugs to bug-cpio [at] gnu.org </p>
<p> GNU cpio home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/cpio/">http://www.gnu.org/software/cpio/</a>&gt; </p>
<p> General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt; </p>
<p> Report cpio translation bugs to &lt;<a rel="nofollow" href="http://translationproject.org/team/">http://translationproject.org/team/</a>&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-cpio/">cpio</a>(5)</p>
<h2>DESCRIPTION</h2>
<p> GNU <code>cpio</code> copies files between archives and directories. It supports the following archive formats: old binary cpio, old portable cpio, SVR4 cpio with and without checksum, HP cpio, and various tar formats. </p>
<p> The operation mode is requested by one of the following options:</p>
<dl>
<dt><code>-o</code>, <code>&#8211;create</code></p>
<dd> Copy-out. Read a list of file names from the standard input and create on the standard output (unless overridden by the <code>&#8211;file</code> option) an archive containing these files.</p>
<dt><code>-i</code>, <code>&#8211;extract</code></p>
<dd> Copy-in. Read the archive from standard input (or from the file supplied with the <code>&#8211;file</code> option) and extract files from it, or (if the <code>-t</code> option is given) list its contents to the standard output. If one or more <i>pattern</i>s are supplied, read or list only files matching these patterns. The <code>-t</code> option alone implies <code>-i</code>.</p>
<dt><code>-p</code>, <code>&#8211;pass-through</code></p>
<dd> Pass-through. Read a list of file names from the standard input and copy them to the specified directory.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Give a short help summary and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print program version and exit.</dl>
<h2>REPORTING BUGS</h2>
<p> Report cpio bugs to bug-cpio [at] gnu.org </p>
<p> GNU cpio home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/cpio/">http://www.gnu.org/software/cpio/</a>&gt; </p>
<p> General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt; </p>
<p> Report cpio translation bugs to &lt;<a rel="nofollow" href="http://translationproject.org/team/">http://translationproject.org/team/</a>&gt;</p>
<h2>OPTIONS</h2>
<h3>Operation modifiers valid in any mode</h3>
<dl>
<dt><code>&#8211;block-size=</code><i>BLOCK-SIZE</i></p>
<dd> Set the I/O block size to <i>BLOCK-SIZE</i> * 512 bytes.</p>
<dt><code>-B</code></p>
<dd> Set the I/O block size to 5120 bytes.</p>
<dt><code>-c</code></p>
<dd> Use the old portable (ASCII) archive format. This is the same as <code>-H odc</code>.</p>
<dt><code>-C</code>, <code>&#8211;io-size=</code><i>NUMBER</i></p>
<dd> Set the I/O block size to the given <i>NUMBER</i> of bytes.</p>
<dt><code>-D</code>, <code>&#8211;directory=</code><i>DIR</i></p>
<dd> Change to directory <i>DIR</i>.</p>
<dt><code>&#8211;force-local</code></p>
<dd> Archive file is local, even if its name contains colons.</p>
<dt><code>-H</code>, <code>&#8211;format=</code><i>FORMAT</i></p>
<dd> Use given archive <code>FORMAT</code>. Valid formats are (the number in parentheses gives maximum size for individual archive member):</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>bin</code></p>
<dd> The obsolete binary format. (2147483647 bytes)</p>
<dt><code>odc</code></p>
<dd> The old (POSIX.1) portable format. (8589934591 bytes)</p>
<dt><code>newc</code></p>
<dd> The new (SVR4) portable format, which supports file systems having more than 65536 i-nodes. (4294967295 bytes)</p>
<dt><code>crc</code></p>
<dd> The new (SVR4) portable format with a checksum added.</p>
<dt><code>tar</code></p>
<dd> The old tar format. (8589934591 bytes)</p>
<dt><code>ustar</code></p>
<dd> The POSIX.1 tar format. Also recognizes GNU tar archives, which are similar but not identical. (8589934591 bytes)</p>
<dt><code>hpbin</code></p>
<dd> The obsolete binary format used by HPUX&#8217;s cpio (which stores device files differently).</p>
<dt><code>hpodc</code></p>
<dd> The portable format used by HPUX&#8217;s cpio (which stores device files differently).</dl>
</dl>
<dt><code>-R</code>, <code>&#8211;owner=</code>[<i>USER</i>][<code>:.</code>][<i>GROUP</i>]</p>
<dd> In copy-in and copy-pass mode, set the ownership of all files created to the specified <i>USER</i> and/or <i>GROUP</i>. In copy-out mode, store the supplied owner information in the archive. </p>
<p> <i>USER</i> and <i>GROUP</i> are first looked up in the system user and group databases. If not found, <code>cpio</code> checks if they consist of decimal digits only and, if so, treats them as numeric UID and GID, correspondingly. </p>
<p> To avoid the lookup and ensure that arguments are treated as numeric values, prefix them with a plus sign, e.g.: <code>-R +0:+0</code>.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Do not print the number of blocks copied at the end of the run.</p>
<dt><code>&#8211;rsh-command=</code><i>COMMAND</i></p>
<dd> Use remote <i>COMMAND</i> instead of <code>rsh</code>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbosely list the files processed.</p>
<dt><code>-V</code>, <code>&#8211;dot</code></p>
<dd> Print a &quot;<code>.</code>&quot; for each file processed.</p>
<dt><code>-W</code>, <code>&#8211;warning=</code><i>FLAG</i></p>
<dd> Controlsи warning display. The <i>FLAG</i> is one of <code>none</code>, to disable all warnings, <code>all</code> to enable them, <code>truncate</code>, to enable warnings about field truncation, and <code>no-truncate</code>, to disable them. </p>
<p> Multiple <code>-W</code> options accumulate.</dl>
<h3>Operation modifiers valid in copy-in and copy-out modes</h3>
<dl>
<dt><code>-F</code>, <code>&#8211;file=</code>[[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE-FILE</i></p>
<dd> Use this <i>ARCHIVE-FILE</i> instead of standard input (in copy-in mode) or standard output (in copy-out mode). Optional <i>USER</i> and <i>HOST</i> specify the user and host names in case of a remote archive.</p>
<dt><code>-M</code>, <code>&#8211;message=</code><i>STRING</i></p>
<dd> Print <i>STRING</i> when the end of a volume of the backup media is reached.</dl>
<h3>Operation modifiers valid only in copy-in mode</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;swap</code></p>
<dd> Swap both halfwords of words and bytes of halfwords in the data. Equivalent to <code>-sS</code>.</p>
<dt><code>-f</code>, <code>&#8211;nonmatching</code></p>
<dd> Only copy files that do not match any of the given patterns.</p>
<dt><code>-n</code>, <code>&#8211;numeric-uid-gid</code></p>
<dd> In the verbose table of contents listing, show numeric UID and GID.</p>
<dt><code>-r</code>, <code>&#8211;rename</code></p>
<dd> Interactively rename files.</p>
<dt><code>-s</code>, <code>&#8211;swap-bytes</code></p>
<dd> Swap the bytes of each halfword in the files.</p>
<dt><code>-S</code>, <code>&#8211;swap-halfwords</code></p>
<dd> Swap the halfwords of each word (4 bytes) in the files.</p>
<dt><code>&#8211;to-stdout</code></p>
<dd> Extract files to standard output.</p>
<dt><code>-E</code>, <code>&#8211;pattern-file=</code><i>FILE</i></p>
<dd> Read additional patterns specifying filenames to extract or list from <i>FILE</i>.</p>
<dt><code>&#8211;only-verify-crc</code></p>
<dd> When reading a CRC format archive, only verify the CRC&#8217;s of each file in the archive, without actually extracting the files.</dl>
<h3>Operation modifiers valid only in copy-out mode</h3>
<dl>
<dt><code>-A</code>, <code>&#8211;append</code></p>
<dd> Append to an existing archive.</p>
<dt><code>&#8211;device-independent</code>, <code>&#8211;reproducible</code></p>
<dd> Create reproducible archives. This is equivalent to <code>&#8211;ignore-devno &#8211;renumber-inodes</code>.</p>
<dt><code>&#8211;ignore-devno</code></p>
<dd> Store 0 in the device number field of each archive member, instead of the actual device number.</p>
<dt><code>-O</code> [[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE-NAME</i></p>
<dd> Use <i>ARCHIVE-NAME</i> instead of standard output. Optional <i>USER</i> and <i>HOST</i> specify the user and host names in case of a remote archive. </p>
<p> The output archive name can be specified wither using this option, or using <code>-F</code> (<code>&#8211;file</code>), but not both.</p>
<dt><code>&#8211;renumber-inodes</code></p>
<dd> Renumber inodes when storing them in the archive.</dl>
<h3>Operation modifiers valid only in copy-pass mode</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;link</code></p>
<dd> Link files instead of copying them, when possible.</dl>
<h3>Operation modifiers valid in copy-in and copy-out modes</h3>
<dl>
<dt><code>&#8211;absolute-filenames</code></p>
<dd> Do not strip file system prefix components from the file names. This is the default.</p>
<dt><code>&#8211;no-absolute-filenames</code></p>
<dd> Create all files relative to the current directory.</dl>
<h3>Operation modifiers valid in copy-out and copy-pass modes</h3>
<dl>
<dt><code>-0</code>, <code>&#8211;null</code></p>
<dd> Filenames in the list are delimited by null characters instead of newlines.</p>
<dt><code>-a</code>, <code>&#8211;reset-access-time</code></p>
<dd> Reset the access times of files after reading them.</p>
<dt><code>-I</code> [[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE-NAME</i></p>
<dd> Use <i>ARCHIVE-NAME</i> instead of standard input. Optional <i>USER</i> and <i>HOST</i> specify the user and host names in case of a remote archive. </p>
<p> The input archive name can be specified wither using this option, or using <code>-F</code> (<code>&#8211;file</code>), but not both.</p>
<dt><code>-L</code>, <code>&#8211;dereference</code></p>
<dd> Dereference symbolic links (copy the files that they point to instead of copying the links).</dl>
<h3>Operation modifiers valid in copy-in and copy-pass modes</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;make-directories</code></p>
<dd> Create leading directories where needed.</p>
<dt><code>-m</code>, <code>&#8211;preserve-modification-time</code></p>
<dd> Retain previous file modification times when creating files.</p>
<dt><code>&#8211;no-preserve-owner</code></p>
<dd> Do not change the ownership of the files.</p>
<dt><code>&#8211;sparse</code></p>
<dd> Write files with large blocks of zeros as sparse files.</p>
<dt><code>-u</code>, <code>&#8211;unconditional</code></p>
<dd> Replace all files unconditionally.</dl>
<h2>RETURN VALUE</h2>
<p> GNU <code>cpio</code> exits with code <code>0</code> if it was able to successfully complete the requested operation. On errors, it exits with code <code>2</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/8-rmt/">rmt</a></code>(8), <code><a href="/docs/linux/man/1-mt/">mt</a></code>(1).</p>
<h2>BUG REPORTS</h2>
<p> Report bugs to &lt;bug-cpio [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2014 Free Software Foundation, Inc.<br />
 License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
