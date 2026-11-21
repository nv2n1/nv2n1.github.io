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
<dt><code>-o</code>, <code>&#8211;create</code></dt>
<dd> Copy-out. Read a list of file names from the standard input and create on the standard output (unless overridden by the <code>&#8211;file</code> option) an archive containing these files.</dd>
<dt><code>-i</code>, <code>&#8211;extract</code></dt>
<dd> Copy-in. Read the archive from standard input (or from the file supplied with the <code>&#8211;file</code> option) and extract files from it, or (if the <code>-t</code> option is given) list its contents to the standard output. If one or more <i>pattern</i>s are supplied, read or list only files matching these patterns. The <code>-t</code> option alone implies <code>-i</code>.</dd>
<dt><code>-p</code>, <code>&#8211;pass-through</code></dt>
<dd> Pass-through. Read a list of file names from the standard input and copy them to the specified directory.</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Give a short help summary and exit.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Print a short usage message and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print program version and exit.</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report cpio bugs to bug-cpio [at] gnu.org </p>
<p> GNU cpio home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/cpio/">http://www.gnu.org/software/cpio/</a>&gt; </p>
<p> General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt; </p>
<p> Report cpio translation bugs to &lt;<a rel="nofollow" href="http://translationproject.org/team/">http://translationproject.org/team/</a>&gt;</p>
<h2>OPTIONS</h2>
<h3>Operation modifiers valid in any mode</h3>
<dl>
<dt><code>&#8211;block-size=</code><i>BLOCK-SIZE</i></dt>
<dd> Set the I/O block size to <i>BLOCK-SIZE</i> * 512 bytes.</dd>
<dt><code>-B</code></dt>
<dd> Set the I/O block size to 5120 bytes.</dd>
<dt><code>-c</code></dt>
<dd> Use the old portable (ASCII) archive format. This is the same as <code>-H odc</code>.</dd>
<dt><code>-C</code>, <code>&#8211;io-size=</code><i>NUMBER</i></dt>
<dd> Set the I/O block size to the given <i>NUMBER</i> of bytes.</dd>
<dt><code>-D</code>, <code>&#8211;directory=</code><i>DIR</i></dt>
<dd> Change to directory <i>DIR</i>.</dd>
<dt><code>&#8211;force-local</code></dt>
<dd> Archive file is local, even if its name contains colons.</dd>
<dt><code>-H</code>, <code>&#8211;format=</code><i>FORMAT</i></dt>
<dd> Use given archive <code>FORMAT</code>. Valid formats are (the number in parentheses gives maximum size for individual archive member):</dd>
<dl>
<dl>
<dt><code>bin</code></dt>
<dd> The obsolete binary format. (2147483647 bytes)</dd>
<dt><code>odc</code></dt>
<dd> The old (POSIX.1) portable format. (8589934591 bytes)</dd>
<dt><code>newc</code></dt>
<dd> The new (SVR4) portable format, which supports file systems having more than 65536 i-nodes. (4294967295 bytes)</dd>
<dt><code>crc</code></dt>
<dd> The new (SVR4) portable format with a checksum added.</dd>
<dt><code>tar</code></dt>
<dd> The old tar format. (8589934591 bytes)</dd>
<dt><code>ustar</code></dt>
<dd> The POSIX.1 tar format. Also recognizes GNU tar archives, which are similar but not identical. (8589934591 bytes)</dd>
<dt><code>hpbin</code></dt>
<dd> The obsolete binary format used by HPUX&#8217;s cpio (which stores device files differently).</dd>
<dt><code>hpodc</code></dt>
<dd> The portable format used by HPUX&#8217;s cpio (which stores device files differently).</dd></dl>
</dl>
<dt><code>-R</code>, <code>&#8211;owner=</code>[<i>USER</i>][<code>:.</code>][<i>GROUP</i>]</dt>
<dd> In copy-in and copy-pass mode, set the ownership of all files created to the specified <i>USER</i> and/or <i>GROUP</i>. In copy-out mode, store the supplied owner information in the archive. </dd>
<p> <i>USER</i> and <i>GROUP</i> are first looked up in the system user and group databases. If not found, <code>cpio</code> checks if they consist of decimal digits only and, if so, treats them as numeric UID and GID, correspondingly. </p>
<p> To avoid the lookup and ensure that arguments are treated as numeric values, prefix them with a plus sign, e.g.: <code>-R +0:+0</code>.</p>
<dt><code>&#8211;quiet</code></dt>
<dd> Do not print the number of blocks copied at the end of the run.</dd>
<dt><code>&#8211;rsh-command=</code><i>COMMAND</i></dt>
<dd> Use remote <i>COMMAND</i> instead of <code>rsh</code>.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Verbosely list the files processed.</dd>
<dt><code>-V</code>, <code>&#8211;dot</code></dt>
<dd> Print a &quot;<code>.</code>&quot; for each file processed.</dd>
<dt><code>-W</code>, <code>&#8211;warning=</code><i>FLAG</i></dt>
<dd> Controlsи warning display. The <i>FLAG</i> is one of <code>none</code>, to disable all warnings, <code>all</code> to enable them, <code>truncate</code>, to enable warnings about field truncation, and <code>no-truncate</code>, to disable them. </dd>
<p> Multiple <code>-W</code> options accumulate.</dl>
<h3>Operation modifiers valid in copy-in and copy-out modes</h3>
<dl>
<dt><code>-F</code>, <code>&#8211;file=</code>[[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE-FILE</i></dt>
<dd> Use this <i>ARCHIVE-FILE</i> instead of standard input (in copy-in mode) or standard output (in copy-out mode). Optional <i>USER</i> and <i>HOST</i> specify the user and host names in case of a remote archive.</dd>
<dt><code>-M</code>, <code>&#8211;message=</code><i>STRING</i></dt>
<dd> Print <i>STRING</i> when the end of a volume of the backup media is reached.</dd></dl>
<h3>Operation modifiers valid only in copy-in mode</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;swap</code></dt>
<dd> Swap both halfwords of words and bytes of halfwords in the data. Equivalent to <code>-sS</code>.</dd>
<dt><code>-f</code>, <code>&#8211;nonmatching</code></dt>
<dd> Only copy files that do not match any of the given patterns.</dd>
<dt><code>-n</code>, <code>&#8211;numeric-uid-gid</code></dt>
<dd> In the verbose table of contents listing, show numeric UID and GID.</dd>
<dt><code>-r</code>, <code>&#8211;rename</code></dt>
<dd> Interactively rename files.</dd>
<dt><code>-s</code>, <code>&#8211;swap-bytes</code></dt>
<dd> Swap the bytes of each halfword in the files.</dd>
<dt><code>-S</code>, <code>&#8211;swap-halfwords</code></dt>
<dd> Swap the halfwords of each word (4 bytes) in the files.</dd>
<dt><code>&#8211;to-stdout</code></dt>
<dd> Extract files to standard output.</dd>
<dt><code>-E</code>, <code>&#8211;pattern-file=</code><i>FILE</i></dt>
<dd> Read additional patterns specifying filenames to extract or list from <i>FILE</i>.</dd>
<dt><code>&#8211;only-verify-crc</code></dt>
<dd> When reading a CRC format archive, only verify the CRC&#8217;s of each file in the archive, without actually extracting the files.</dd></dl>
<h3>Operation modifiers valid only in copy-out mode</h3>
<dl>
<dt><code>-A</code>, <code>&#8211;append</code></dt>
<dd> Append to an existing archive.</dd>
<dt><code>&#8211;device-independent</code>, <code>&#8211;reproducible</code></dt>
<dd> Create reproducible archives. This is equivalent to <code>&#8211;ignore-devno &#8211;renumber-inodes</code>.</dd>
<dt><code>&#8211;ignore-devno</code></dt>
<dd> Store 0 in the device number field of each archive member, instead of the actual device number.</dd>
<dt><code>-O</code> [[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE-NAME</i></dt>
<dd> Use <i>ARCHIVE-NAME</i> instead of standard output. Optional <i>USER</i> and <i>HOST</i> specify the user and host names in case of a remote archive. </dd>
<p> The output archive name can be specified wither using this option, or using <code>-F</code> (<code>&#8211;file</code>), but not both.</p>
<dt><code>&#8211;renumber-inodes</code></dt>
<dd> Renumber inodes when storing them in the archive.</dd></dl>
<h3>Operation modifiers valid only in copy-pass mode</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;link</code></dt>
<dd> Link files instead of copying them, when possible.</dd></dl>
<h3>Operation modifiers valid in copy-in and copy-out modes</h3>
<dl>
<dt><code>&#8211;absolute-filenames</code></dt>
<dd> Do not strip file system prefix components from the file names. This is the default.</dd>
<dt><code>&#8211;no-absolute-filenames</code></dt>
<dd> Create all files relative to the current directory.</dd></dl>
<h3>Operation modifiers valid in copy-out and copy-pass modes</h3>
<dl>
<dt><code>-0</code>, <code>&#8211;null</code></dt>
<dd> Filenames in the list are delimited by null characters instead of newlines.</dd>
<dt><code>-a</code>, <code>&#8211;reset-access-time</code></dt>
<dd> Reset the access times of files after reading them.</dd>
<dt><code>-I</code> [[<i>USER</i><code>@</code>]<i>HOST</i><code>:</code>]<i>ARCHIVE-NAME</i></dt>
<dd> Use <i>ARCHIVE-NAME</i> instead of standard input. Optional <i>USER</i> and <i>HOST</i> specify the user and host names in case of a remote archive. </dd>
<p> The input archive name can be specified wither using this option, or using <code>-F</code> (<code>&#8211;file</code>), but not both.</p>
<dt><code>-L</code>, <code>&#8211;dereference</code></dt>
<dd> Dereference symbolic links (copy the files that they point to instead of copying the links).</dd></dl>
<h3>Operation modifiers valid in copy-in and copy-pass modes</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;make-directories</code></dt>
<dd> Create leading directories where needed.</dd>
<dt><code>-m</code>, <code>&#8211;preserve-modification-time</code></dt>
<dd> Retain previous file modification times when creating files.</dd>
<dt><code>&#8211;no-preserve-owner</code></dt>
<dd> Do not change the ownership of the files.</dd>
<dt><code>&#8211;sparse</code></dt>
<dd> Write files with large blocks of zeros as sparse files.</dd>
<dt><code>-u</code>, <code>&#8211;unconditional</code></dt>
<dd> Replace all files unconditionally.</dd></dl>
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
