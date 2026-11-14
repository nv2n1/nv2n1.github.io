---
title: "parted(8)"
name: "parted"
section: "8"
letter: "p"
url: "/docs/linux/man/8-parted/"
description: "parted – a partition manipulation program"
---

<p>parted &#8211; a partition manipulation program</p>
<h2>Synopsis</h2>
<p><code>parted</code> [options] [device [command [options&#8230;]&#8230;]]</p>
<h2>Description</h2>
<p><code>parted</code> is a program to manipulate disk partitions. It supports multiple partition table formats, including MS-DOS and GPT. It is useful for creating space for new operating systems, reorganising disk usage, and copying data to new hard disks. </p>
<p> This manual page documents <code>parted</code> briefly. Complete documentation is distributed with the package in GNU Info format.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>displays a help message</p>
<dt><code>-l, &#8211;list</code></p>
<dd>lists partition layout on all block devices</p>
<dt><code>-m, &#8211;machine</code></p>
<dd>displays machine parseable output</p>
<dt><code>-s, &#8211;script</code></p>
<dd>never prompts for user intervention</p>
<dt><code>-v, &#8211;version</code></p>
<dd>displays the version</p>
<dt><code>-a </code><i>alignment-type</i>, &#8211;align <i>alignment-type</i></p>
<dd>Set alignment for newly created partitions, valid alignment types are:</p>
<dl>
<dd>
<dl>
<dt>none</p>
<dd>Use the minimum alignment allowed by the disk type.</p>
<dt>cylinder</p>
<dd>Align partitions to cylinders.</p>
<dt>minimal</p>
<dd>Use minimum alignment as given by the disk topology information. This and the opt value will use layout information provided by the disk to align the logical partition table addresses to actual physical blocks on the disks. The min value is the minimum alignment needed to align the partition properly to physical blocks, which avoids performance degradation.</p>
<dt>optimal</p>
<dd>Use optimum alignment as given by the disk topology information. This aligns to a multiple of the physical block size in a way that guarantees optimal performance.</dl>
</dl>
</dl>
<h2>Commands</h2>
<dl>
<dt><code>[device]</code></p>
<dd>The block device to be used. When none is given, <code>parted</code> will use the first block device it finds.</p>
<dt><code>[command [options]]</code></p>
<dd>Specifies the command to be executed. If no command is given, <code>parted</code> will present a command prompt. Possible commands are:</p>
<dl>
<dd>
<dl>
<dt><code>help </code><i>[command]</i></p>
<dd>Print general help, or help on <i>command</i> if specified.</p>
<dt><code>align-check </code><i>type</i> <i>partition</i></p>
<dd>Check if <i>partition</i> satisfies the alignment constraint of <i>type</i>. <i>type</i> must be &quot;minimal&quot; or &quot;optimal&quot;.</p>
<dt><code>mklabel </code><i>label-type</i></p>
<dd>Create a new disklabel (partition table) of <i>label-type</i>. <i>label-type</i> should be one of &quot;aix&quot;, &quot;amiga&quot;, &quot;bsd&quot;, &quot;dvh&quot;, &quot;gpt&quot;, &quot;loop&quot;, &quot;mac&quot;, &quot;msdos&quot;, &quot;pc98&quot;, or &quot;sun&quot;.</p>
<dt><code>mkpart [</code><i>part-type</i> <i>name</i> <i>fs-type</i>] <i>start</i> <i>end</i></p>
<dd>Create a new partition. <i>part-type</i> may be specified only with msdos and dvh partition tables, it should be one of &quot;primary&quot;, &quot;logical&quot;, or &quot;extended&quot;. <i>name</i> is required for GPT partition tables and <i>fs-type</i> is optional. <i>fs-type</i> can be one of &quot;btrfs&quot;, &quot;ext2&quot;, &quot;ext3&quot;, &quot;ext4&quot;, &quot;fat16&quot;, &quot;fat32&quot;, &quot;hfs&quot;, &quot;hfs+&quot;, &quot;linux-swap&quot;, &quot;ntfs&quot;, &quot;reiserfs&quot;, &quot;udf&quot;, or &quot;xfs&quot;.</p>
<dt><code>name </code><i>partition</i> <i>name</i></p>
<dd>Set the name of <i>partition</i> to <i>name</i>. This option works only on Mac, PC98, and GPT disklabels. The name can be placed in double quotes, if necessary. And depending on the shell may need to also be wrapped in single quotes so that the shell doesn&#8217;t strip off the double quotes.</p>
<dt><code>print</code></p>
<dd>Display the partition table.</p>
<dt><code>quit</code></p>
<dd>Exit from <code>parted</code>.</p>
<dt><code>rescue </code><i>start</i> <i>end</i></p>
<dd>Rescue a lost partition that was located somewhere between <i>start</i> and <i>end</i>. If a partition is found, <code>parted</code> will ask if you want to create an entry for it in the partition table.</p>
<dt><code>resizepart </code><i>partition</i> <i>end</i></p>
<dd>Change the <i>end</i> position of <i>partition</i>. Note that this does not modify any filesystem present in the partition.</p>
<dt><code>rm </code><i>partition</i></p>
<dd>Delete <i>partition</i>.</p>
<dt><code>select </code><i>device</i></p>
<dd>Choose <i>device</i> as the current device to edit. <i>device</i> should usually be a Linux hard disk device, but it can be a partition, software raid device, or an LVM logical volume if necessary.</p>
<dt><code>set </code><i>partition</i> <i>flag</i> <i>state</i></p>
<dd>Change the state of the <i>flag</i> on <i>partition</i> to <i>state</i>. Supported flags are: &quot;boot&quot;, &quot;root&quot;, &quot;swap&quot;, &quot;hidden&quot;, &quot;raid&quot;, &quot;lvm&quot;, &quot;lba&quot;, &quot;legacy_boot&quot;, &quot;irst&quot;, &quot;msftres&quot;, &quot;esp&quot;, &quot;chromeos_kernel&quot;, &quot;bls_boot&quot; and &quot;palo&quot;. <i>state</i> should be either &quot;on&quot; or &quot;off&quot;.</p>
<dt><code>unit </code><i>unit</i></p>
<dd>Set <i>unit</i> as the unit to use when displaying locations and sizes, and for interpreting those given by the user when not suffixed with an explicit unit. <i>unit</i> can be one of &quot;s&quot; (sectors), &quot;B&quot; (bytes), &quot;kB&quot;, &quot;MB&quot;, &quot;MiB&quot;, &quot;GB&quot;, &quot;GiB&quot;, &quot;TB&quot;, &quot;TiB&quot;, &quot;%&quot; (percentage of device size), &quot;cyl&quot; (cylinders), &quot;chs&quot; (cylinders, heads, sectors), or &quot;compact&quot; (megabytes for input, and a human-friendly form for output).</p>
<dt><code>toggle </code><i>partition</i> <i>flag</i></p>
<dd>Toggle the state of <i>flag</i> on <i>partition</i>.</p>
<dt><code>version</code></p>
<dd>Display version information and a copyright message.</dl>
</dl>
</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-parted [at] gnu.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), The <i>parted</i> program is fully documented in the <code><a href="/docs/linux/man/1-info/">info</a>(1)</code> format <i>GNU partitioning software</i> manual which is distributed with the parted-doc Debian package.</p>
<h2>Author</h2>
<p>This manual page was written by Timshel Knoll &lt;timshel [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
