---
title: "mkswap(8)"
name: "mkswap"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkswap/"
description: "mkswap – set up a Linux swap area"
---

<p>mkswap &#8211; set up a Linux swap area</p>
<h2>Synopsis</h2>
<p><code>mkswap</code> [options] <i>device</i> [<i>size</i>]</p>
<h2>Description</h2>
<p><code>mkswap</code> sets up a Linux swap area on a device or in a file. </p>
<p> The <i>device</i> argument will usually be a disk partition (something like <i>/dev/sdb7</i>) but can also be a file. The Linux kernel does not look at partition IDs, but many installation scripts will assume that partitions of hex type 82 (LINUX_SWAP) are meant to be swap partitions. (<code>Warning: Solaris also uses this type. Be careful not to kill your Solaris partitions.</code>) </p>
<p> The <i>size</i> parameter is superfluous but retained for backwards compatibility. (It specifies the desired size of the swap area in 1024-byte blocks. <code>mkswap</code> will use the entire partition or file if it is omitted. Specifying it is unwise &#8211; a typo may destroy your disk.) </p>
<p> After creating the swap area, you need the <code>swapon</code> command to start using it. Usually swap areas are listed in <i>/etc/fstab</i> so that they can be taken into use at boot time by a <code>swapon -a</code> command in some boot script.</p>
<h2>Warning</h2>
<p>The swap header does not touch the first block. A boot loader or disk label can be there, but it is not a recommended setup. The recommended setup is to use a separate partition for a Linux swap area. </p>
<p> <code>mkswap</code>, like many others mkfs-like utils, <code>erases the first partition block to make any previous filesystem invisible.</code> </p>
<p> However, <code>mkswap</code> refuses to erase the first block on a device with a disk label (SUN, BSD, &#8230;).</p>
<h2>Options</h2>
<p><code>-c</code>, <code>&#8211;check</code></p>
<dl>
<dd>Check the device (if it is a block device) for bad blocks before creating the swap area. If any bad blocks are found, the count is printed.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>Go ahead even if the command is stupid. This allows the creation of a swap area larger than the file or partition it resides on. </p>
<p> Also, without this option, <code>mkswap</code> will refuse to erase the first block on a device with a partition table.</dl>
<p> <code>-L</code>, <code>&#8211;label</code> <i>label</i></p>
<dl>
<dd>Specify a <i>label</i> for the device, to allow <code>swapon</code> by label.</dl>
<p> <code>&#8211;lock</code>[=<i>mode</i>]</p>
<dl>
<dd>Use exclusive BSD lock for device or file it operates. The optional argument <i>mode</i> can be <code>yes</code>, <code>no</code> (or 1 and 0) or <code>nonblock</code>. If the <i>mode</i> argument is omitted, it defaults to <code>&quot;yes&quot;</code>. This option overwrites environment variable <code>$LOCK_BLOCK_DEVICE</code>. The default is not to use any lock at all, but it&#8217;s recommended to avoid collisions with udevd or other tools.</dl>
<p> <code>-p</code>, <code>&#8211;pagesize</code> <i>size</i></p>
<dl>
<dd>Specify the page <i>size</i> (in bytes) to use. This option is usually unnecessary; <code>mkswap</code> reads the size from the kernel.</dl>
<p> <code>-U</code>, <code>&#8211;uuid</code> <i>UUID</i></p>
<dl>
<dd>Specify the <i>UUID</i> to use. The default is to generate a UUID.</dl>
<p> <code>-v</code>, <code>&#8211;swapversion 1</code></p>
<dl>
<dd>Specify the swap-space version. (This option is currently pointless, as the old <code>-v 0</code> option has become obsolete and now only <code>-v 1</code> is supported. The kernel has not supported v0 swap-space format since 2.5.22 (June 2002). The new version v1 is supported since 2.1.117 (August 1998).)</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dd>Verbose execution. With this option <code>mkswap</code> will output more details about detected problems during swap area set up.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<h2>Environment</h2>
<p>LIBBLKID_DEBUG=all</p>
<dl>
<dd>enables libblkid debug output.</dl>
<p> LOCK_BLOCK_DEVICE=&lt;mode&gt;</p>
<dl>
<dd>use exclusive BSD lock. The mode is &quot;1&quot; or &quot;0&quot;. See <code>&#8211;lock</code> for more details.</dl>
<h2>Notes</h2>
<p>The maximum useful size of a swap area depends on the architecture and the kernel version. </p>
<p> The maximum number of the pages that is possible to address by swap area header is 4294967295 (32-bit unsigned int). The remaining space on the swap device is ignored. </p>
<p> Presently, Linux allows 32 swap areas. The areas in use can be seen in the file <i>/proc/swaps</i>. </p>
<p> <code>mkswap</code> refuses areas smaller than 10 pages. </p>
<p> If you don&#8217;t know the page size that your machine uses, you may be able to look it up with <code>cat /proc/cpuinfo</code> (or you may not &#8211; the contents of this file depend on architecture and kernel version). </p>
<p> To set up a swap file, it is necessary to create that file before initializing it with <code>mkswap</code>, e.g. using a command like </p>
<dl>
<dd>
<pre># dd if=/dev/zero of=swapfile bs=1MiB count=$((8*1024))</pre>
</dl>
<p> to create 8GiB swapfile. </p>
<p> Please read notes from <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8) about <code>the swap file use restrictions</code> (holes, preallocation and copy-on-write issues).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>mkswap</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
