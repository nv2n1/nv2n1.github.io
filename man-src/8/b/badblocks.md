---
title: "badblocks(8)"
name: "badblocks"
section: "8"
letter: "b"
url: "/docs/linux/man/8-badblocks/"
description: "badblocks – search a device for bad blocks"
---

<p>badblocks &#8211; search a device for bad blocks</p>
<h2>Synopsis</h2>
<p><code>badblocks</code> [ <code>-svwnfBX</code> ] [ <code>-b</code> <i>block_size</i> ] [ <code>-c</code> <i>blocks_at_once</i> ] [ <code>-d</code> <i>read_delay_factor</i> ] [ <code>-e</code> <i>max_bad_blocks</i> ] [ <code>-i</code> <i>input_file</i> ] [ <code>-o</code> <i>output_file</i> ] [ <code>-p</code> <i>num_passes</i> ] [ <code>-t</code> <i>test_pattern</i> ] <i>device</i> [ <i>last_block</i> ] [ <i>first_block</i> ]</p>
<h2>Description</h2>
<p><code>badblocks</code> is used to search for bad blocks on a device (usually a disk partition). <i>device</i> is the special file corresponding to the device (e.g <i>/dev/hdc1</i>). <i>last_block</i> is the last block to be checked; if it is not specified, the last block on the device is used as a default. <i>first_block</i> is an optional parameter specifying the starting block number for the test, which allows the testing to start in the middle of the disk. If it is not specified the first block on the disk is used as a default. </p>
<p> <code>Important note:</code> If the output of <code>badblocks</code> is going to be fed to the <code>e2fsck</code> or <code>mke2fs</code> programs, it is important that the block size is properly specified, since the block numbers which are generated are very dependent on the block size in use by the file system. For this reason, it is strongly recommended that users <code>not</code> run <code>badblocks</code> directly, but rather use the <code>-c</code> option of the <code>e2fsck</code> and <code>mke2fs</code> programs.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code><i> block_size</i></p>
<dd>Specify the size of blocks in bytes. The default is 1024.</p>
<dt><code>-c</code><i> number of blocks</i></p>
<dd>is the number of blocks which are tested at a time. The default is 64.</p>
<dt><code>-d</code><i> read delay factor</i></p>
<dd>This parameter, if passed and non-zero, will cause bad blocks to sleep between reads if there were no errors encountered in the read operation; the delay will be calculated as a percentage of the time it took for the read operation to be performed. In other words, a value of 100 will cause each read to be delayed by the amount the previous read took, and a value of 200 by twice the amount.</p>
<dt><code>-e</code><i> max bad block count</i></p>
<dd>Specify a maximum number of bad blocks before aborting the test. The default is 0, meaning the test will continue until the end of the test range is reached.</p>
<dt><code>-f</code></p>
<dd>Normally, badblocks will refuse to do a read/write or a non-destructive test on a device which is mounted, since either can cause the system to potentially crash and/or damage the file system even if it is mounted read-only. This can be overridden using the <code>-f</code> flag, but should almost never be used &#8212; if you think you&#8217;re smarter than the <code>badblocks</code> program, you almost certainly aren&#8217;t. The only time when this option might be safe to use is if the /etc/mtab file is incorrect, and the device really isn&#8217;t mounted.</p>
<dt><code>-i</code><i> input_file</i></p>
<dd>Read a list of already existing known bad blocks. <code>Badblocks</code> will skip testing these blocks since they are known to be bad. If <i>input_file</i> is specified as &quot;-&quot;, the list will be read from the standard input. Blocks listed in this list will be omitted from the list of <i>new</i> bad blocks produced on the standard output or in the output file. The <code>-b</code> option of <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8) can be used to retrieve the list of blocks currently marked bad on an existing file system, in a format suitable for use with this option.</p>
<dt><code>-n</code></p>
<dd>Use non-destructive read-write mode. By default only a non-destructive read-only test is done. This option must not be combined with the <code>-w</code> option, as they are mutually exclusive.</p>
<dt><code>-o</code><i> output_file</i></p>
<dd>Write the list of bad blocks to the specified file. Without this option, <code>badblocks</code> displays the list on its standard output. The format of this file is suitable for use by the <code>-l</code> option in <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) or <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8).</p>
<dt><code>-p</code><i> num_passes</i></p>
<dd>Repeat scanning the disk until there are no new blocks discovered in num_passes consecutive scans of the disk. Default is 0, meaning <code>badblocks</code> will exit after the first pass.</p>
<dt><code>-s</code></p>
<dd>Show the progress of the scan by writing out rough percentage completion of the current badblocks pass over the disk. Note that badblocks may do multiple test passes over the disk, in particular if the <code>-p</code> or <code>-w</code> option is requested by the user.</p>
<dt><code>-t</code><i> test_pattern</i></p>
<dd>Specify a test pattern to be read (and written) to disk blocks. The <i>test_pattern</i> may either be a numeric value between 0 and ULONG_MAX-1 inclusive, or the word &quot;random&quot;, which specifies that the block should be filled with a random bit pattern. For read/write (<code>-w</code>) and non-destructive (<code>-n</code>) modes, one or more test patterns may be specified by specifying the <code>-t</code> option for each test pattern desired. For read-only mode only a single pattern may be specified and it may not be &quot;random&quot;. Read-only testing with a pattern assumes that the specified pattern has previously been written to the disk &#8211; if not, large numbers of blocks will fail verification. If multiple patterns are specified then all blocks will be tested with one pattern before proceeding to the next pattern.</p>
<dt><code>-v</code></p>
<dd>Verbose mode. Will write the number of read errors, write errors and data- corruptions to stderr.</p>
<dt><code>-w</code></p>
<dd>Use write-mode test. With this option, <code>badblocks</code> scans for bad blocks by writing some patterns (0xaa, 0x55, 0xff, 0x00) on every block of the device, reading every block and comparing the contents. This option may not be combined with the <code>-n</code> option, as they are mutually exclusive.</p>
<dt><code>-B</code></p>
<dd>Use buffered I/O and do not use Direct I/O, even if it is available.</p>
<dt><code>-X</code></p>
<dd>Internal flag only to be used by <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) and <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8). It bypasses the exclusive mode in-use device safety check.</dl>
<h2>Warning</h2>
<p>Never use the <code>-w</code> option on a device containing an existing file system. This option erases data! If you want to do write-mode testing on an existing file system, use the <code>-n</code> option instead. It is slower, but it will preserve your data. </p>
<p> The <code>-e</code> option will cause badblocks to output a possibly incomplete list of bad blocks. Therefore it is recommended to use it only when one wants to know if there are any bad blocks at all on the device, and not when the list of bad blocks is wanted.</p>
<h2>Author</h2>
<p><code>badblocks</code> was written by Remy Card &lt;Remy.Card [at] linux.org&gt;. Current maintainer is Theodore Ts&#8217;o &lt;tytso [at] alum.mit.edu&gt;. Non-destructive read/write test implemented by David Beattie &lt;dbeattie [at] softhome.net&gt;.</p>
<h2>Availability</h2>
<p><code>badblocks</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) </p>
