---
title: "wipefs(8)"
name: "wipefs"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wipefs/"
description: "wipefs – wipe a signature from a device"
---

<p>wipefs &#8211; wipe a signature from a device</p>
<h2>Synopsis</h2>
<p><code>wipefs</code> [options] <i>device</i>&#8230; </p>
<p> <code>wipefs</code> [<code>&#8211;backup</code>] <code>-o</code> <i>offset device</i>&#8230; </p>
<p> <code>wipefs</code> [<code>&#8211;backup</code>] <code>-a</code> <i>device</i>&#8230;</p>
<h2>Description</h2>
<p><code>wipefs</code> can erase filesystem, raid or partition-table signatures (magic strings) from the specified <i>device</i> to make the signatures invisible for libblkid. <code>wipefs</code> does not erase the filesystem itself nor any other data from the device. </p>
<p> When used without any options, <code>wipefs</code> lists all visible filesystems and the offsets of their basic signatures. The default output is subject to change. So whenever possible, you should avoid using default outputs in your scripts. Always explicitly define expected columns by using <code>&#8211;output</code> <i>columns-list</i> in environments where a stable output is required. </p>
<p> <code>wipefs</code> calls the BLKRRPART ioctl when it has erased a partition-table signature to inform the kernel about the change. The ioctl is called as the last step and when all specified signatures from all specified devices are already erased. This feature can be used to wipe content on partitions devices as well as partition table on a disk device, for example by <code>wipefs -a /dev/sdc1 /dev/sdc2 /dev/sdc</code>. </p>
<p> Note that some filesystems and some partition tables store more magic strings on the device (e.g., FAT, ZFS, GPT). The <code>wipefs</code> command (since v2.31) lists all the offset where a magic strings have been detected. </p>
<p> When option <code>-a</code> is used, all magic strings that are visible for <code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3) are erased. In this case the <code>wipefs</code> scans the device again after each modification (erase) until no magic string is found. </p>
<p> Note that by default <code>wipefs</code> does not erase nested partition tables on non-whole disk devices. For this the option <code>&#8211;force</code> is required.</p>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dd>Erase all available signatures. The set of erased signatures can be restricted with the <code>-t</code> option.</dl>
<p> <code>-b</code>, <code>&#8211;backup</code></p>
<dl>
<dd>Create a signature backup to the file <i>$HOME/wipefs-&lt;devname&gt;-&lt;offset&gt;.bak</i>. For more details see the <code>EXAMPLE</code> section.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>Force erasure, even if the filesystem is mounted. This is required in order to erase a partition-table signature on a block device.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dd>Use JSON output format.</dl>
<p> <code>&#8211;lock</code>[=<i>mode</i>]</p>
<dl>
<dd>Use exclusive BSD lock for device or file it operates. The optional argument <i>mode</i> can be <code>yes</code>, <code>no</code> (or 1 and 0) or <code>nonblock</code>. If the <i>mode</i> argument is omitted, it defaults to <code>&quot;yes&quot;</code>. This option overwrites environment variable <code>$LOCK_BLOCK_DEVICE</code>. The default is not to use any lock at all, but it&#8217;s recommended to avoid collisions with udevd or other tools.</dl>
<p> <code>-i</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print a header line.</dl>
<p> <code>-O</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Specify which output columns to print. Use <code>&#8211;help</code> to get a list of all supported columns.</dl>
<p> <code>-n</code>, <code>&#8211;no-act</code></p>
<dl>
<dd>Causes everything to be done except for the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) call.</dl>
<p> <code>-o</code>, <code>&#8211;offset</code> <i>offset</i></p>
<dl>
<dd>Specify the location (in bytes) of the signature which should be erased from the device. The <i>offset</i> number may include a &quot;0x&quot; prefix; then the number will be interpreted as a hex value. It is possible to specify multiple <code>-o</code> options. </p>
<p> The <i>offset</i> argument may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;), or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB.</dl>
<p> <code>-p</code>, <code>&#8211;parsable</code></p>
<dl>
<dd>Print out in parsable instead of printable format. Encode all potentially unsafe characters of a string to the corresponding hex value prefixed by &#8216;
