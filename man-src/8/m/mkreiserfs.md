---
title: "mkreiserfs(8)"
name: "mkreiserfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkreiserfs/"
description: "mkreiserfs – The create tool for the Linux ReiserFS filesystem."
---

<p>mkreiserfs &#8211; The create tool for the Linux ReiserFS filesystem.</p>
<h2>Synopsis</h2>
<p><code>mkreiserfs</code> [ <code>-dfV</code> ] [ <code>-b</code> | <code>&#8211;block-size </code><i>N</i> ] [ <code>-h</code> | <code>&#8211;hash </code><i>HASH</i> ] [ <code>-u</code> | <code>&#8211;uuid </code><i>UUID</i> ] [ <code>-l</code> | <code>&#8211;label </code><i>LABEL</i> ] [ <code>&#8211;format </code><i>FORMAT</i> ] [ <code>-q</code> | <code>&#8211;quiet</code> ] [ <code>-j</code> | <code>&#8211;journal-device </code><i>FILE</i> ] [ <code>-s</code> | <code>&#8211;journal-size </code><i>N</i> ] [ <code>-o</code> | <code>&#8211;journal-offset </code><i>N</i> ] [ <code>-t</code> | <code>&#8211;transaction-max-size</code> <i>N</i> ] [ <code>-B</code> | <code>&#8211;badblocks</code> <i>file</i> ] <i> device</i> [ <i>filesystem-size</i> ]</p>
<h2>Description</h2>
<p><code>mkreiserfs</code> creates a Linux ReiserFS filesystem on a device (usually a disk partition).</p>
<dl>
<dt><i>device</i></p>
<dd>is the special file corresponding to a device or to a partition (e.g /dev/hdXX for an IDE disk partition or /dev/sdXX for a SCSI disk partition).</p>
<dt><i>filesystem-size</i></p>
<dd>is the size in blocks of the filesystem. If omitted, <code>mkreiserfs</code> will automatically set it.</dl>
<h2>Options</h2>
<dl>
<dt><code>-b</code> | <code>&#8211;block-size </code><i>N</i></p>
<dd><i>N</i> is block size in bytes. It may only be set to a power of 2 within the 512-8192 interval.</p>
<dt><code>-h</code> | <code>&#8211;hash </code><i>HASH</i></p>
<dd><i>HASH</i> specifies which hash function will sort the names in the directories. Choose from r5, rupasov, or tea. r5 is the default one.</p>
<dt><code>&#8211;format </code><i>FORMAT</i></p>
<dd><i>FORMAT</i> specifies the format for the new filsystem. Choose format 3.5 or 3.6. If none is specified <code>mkreiserfs</code> will create format 3.6 if running kernel is 2.4 or higher, and format 3.5 if kernel 2.2 is running, and will refuse creation under all other kernels.</p>
<dt><code>-u</code> | <code>&#8211;uuid </code><i>UUID</i></p>
<dd>Sets the Universally Unique IDentifier of the filesystem to <i>UUID</i> (see also <code><a href="/docs/linux/man/8-uuidgen/">uuidgen</a>(8)</code>). The format of the <i>UUID</i> is a series of hex digits separated by hypthens, e.g.: &quot;c1b9d5a2-f162-11cf-9ece-0020afc76f16&quot;. If the option is skipped, <code>mkreiserfs</code> will by default generate a new <i>UUID</i>.</p>
<dt><code>-l</code> | <code>&#8211;label </code><i>LABEL</i></p>
<dd>Sets the volume label of the filesystem. <i>LABEL</i> can at most be 16 characters long; if it is longer than 16 characters, <code>mkreiserfs</code> will truncate it.</p>
<dt><code>-q</code> | <code>&#8211;quiet </code></p>
<dd>Sets <code>mkreiserfs</code> to work quietly without producing messages, progress or questions. It is useful, but only for use by end users, if you run <code>mkreiserfs</code> in a script.</p>
<dt><code>-j</code> | <code>&#8211;journal-device </code><i>FILE</i></p>
<dd><i>FILE</i> is the name of the block device on which is to be places the filesystem journal.</p>
<dt><code>-o</code> | <code>&#8211;journal-offset </code><i>N</i></p>
<dd><i>N</i> is the offset where the journal starts when it is to be on a separate device. Default is 0. <i>N</i> has no effect when the journal is to be on the host device.</p>
<dt><code>-s</code> | <code>&#8211;journal-size </code><i>N</p>
<dd>N</i> is the size of the journal in blocks. When the journal is to be on a separate device, its size defaults to the number of blocks that the device has. When journal is to be on the host device, its size defaults to 8193 and the maximal possible size is 32749 (for blocksize 4k). The minimum size is 513 blocks (whether the journal is on the host or on a separate device).</p>
<dt><code>-t</code> | <code>&#8211;transaction-max-size </code><i>N</p>
<dd>N</i> is the maximum transaction size parameter for the journal. The default, and max possible, value is 1024 blocks. It should be less than half the size of the journal. If specified incorrectly, it will automatically be adjusted.</p>
<dt><code>-B</code> | <code>&#8211;badblocks </code><i>file</p>
<dd>File</i> is the file name of the file that contains the list of blocks to be marked as bad on the filesystem. This list can be created by <code>/sbin/badblocks -b block-size device</code>.</p>
<dt><code>-f</code></p>
<dd>Forces <code>mkreiserfs</code> to continue even when the device is the whole disk, looks mounted, or is not a block device. If <code>-f</code> is specified more than once, it allows the user to avoid asking for confirmation.</p>
<dt><code>-d</code></p>
<dd>Sets <code>mkreiserfs</code> to print debugging information during <code>mkreiserfs</code>.</p>
<dt><code>-V</code></p>
<dd>Prints the version and then exits. </p>
</dl>
<h2>Author</h2>
<p>This version of <code>mkreiserfs</code> has been written by Edward Shishkin &lt;edward [at] namesys.com&gt;.</p>
<h2>Bugs</h2>
<p>Please report bugs to the ReiserFS developers &lt;reiserfs-devel [at] vger.kernel.org&gt;, providing as much information as possible&#8211;your hardware, kernel, patches, settings, all printed messages; check the syslog file for any related information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-reiserfsck/">reiserfsck</a></code>(8), <code><a href="/docs/linux/man/8-debugreiserfs/">debugreiserfs</a></code>(8), <code><a href="/docs/linux/man/8-reiserfstune/">reiserfstune</a></code>(8) </p>
