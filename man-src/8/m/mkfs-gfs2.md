---
title: "mkfs-gfs2(8)"
name: "mkfs-gfs2"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-gfs2/"
description: "mkfs.gfs2 – create a gfs2 filesystem"
---

<p>mkfs.gfs2 &#8211; create a gfs2 filesystem</p>
<h2>Synopsis</h2>
<p><code>mkfs.gfs2</code> [<i>options</i>] <i>device</i> <i>[block-count]</i> </p>
<h2>Description</h2>
<p>mkfs.gfs2 is used to create a gfs2 file system. </p>
<h2>Options</h2>
<p>The default values of the following options have been chosen for best results. In most cases, there should be no need to choose different values. The exceptions to this are the number of journals (<code>-j</code>) and the lock table (<code>-t</code>), as these options will be specific to your cluster.</p>
<dl>
<dt><code>-b</code> <i>bytes</i></p>
<dd>Set the filesystem block size to <i>bytes</i> which must be a power of two. The minimum block size is 512 and the block size cannot exceed the machine&#8217;s memory page size, which on most architectures is 4096 bytes. The default block size is 4096 bytes.</p>
<dt><code>-c</code> <i>megabytes</i></p>
<dd>Initial size of each journal&#8217;s quota change file. The default is 1MB.</p>
<dt><code>-D</code></p>
<dd>Enable debugging output.</p>
<dt><code>-h</code></p>
<dd>Print out a help message describing the available options, then exit.</p>
<dt><code>-J</code> <i>megabytes</i></p>
<dd>The size of each journal. The default journal size is 128 megabytes and the minimum size is 8 megabytes.</p>
<dt><code>-j</code> <i>journals</i></p>
<dd>The number of journals for mkfs.gfs2 to create. At least one journal is required for each machine that will mount the filesystem concurrently. If this option is not specified, only one journal will be created. This number may be used as an indicator of the number of nodes in the cluster in order to optimize the layout of the filesystem. As such, it is best to set this option with the maximum number of mounters in mind than to add more journals later.</p>
<dt><code>-K</code></p>
<dd>Do not attempt to discard the block device contents. Issuing discards to the device allows some solid state devices and sparse or thin-provisioned storage devices to optimise free space. Other devices may emulate this behaviour by zeroing the device contents, which can be a slow process.</p>
<dt><code>-O</code></p>
<dd>Override. This option prevents mkfs.gfs2 from asking for confirmation before writing the filesystem.</p>
<dt><code>-o</code></p>
<dd>Specify extended options. Multiple options can be separated by commas. Valid extended options are:</p>
<dl>
<dd>
<dl>
<dt><code>help</code></p>
<dd>Display an extended options help summary, then exit.</p>
<dt><code>sunit=</code><i>bytes</i></p>
<dd>This is used to specify the stripe unit for a RAID device or striped logical volume. This option ensures that resource groups will be stripe unit aligned and overrides the stripe unit value obtained by probing the device. This value must be a multiple of the file system block size and must be specified with the <i>swidth</i> option.</p>
<dt><code>swidth=</code><i>bytes</i></p>
<dd>This is used to specify the stripe width for a RAID device or striped logical volume. This option ensures that resource groups will be stripe aligned and overrides the stripe width value obtained by probing the device. This value must be a multiple of the <i>sunit</i> option and must also be specified with it.</p>
<dt><code>align=</code><i>[0|1]</i></p>
<dd>Disable or enable the alignment of resource groups. The default behaviour is to align resource groups to the stripe width and stripe unit values obtained from probing the device or specified with the <i>swidth</i> and <i>sunit</i> extended options.</dl>
</dl>
<dt><code>-p</code> <i>protocol</i></p>
<dd>Specify the locking protocol to use when no locking protocol is specified at mount time. Valid locking protocols are:</p>
<dl>
<dd>
<dl>
<dt><code>lock_dlm</code></p>
<dd>This is the default. It enables DLM-based locking for use in shared storage configurations.</p>
<dt><code>lock_nolock</code></p>
<dd>This enables single-node locking</dl>
</dl>
<dt><code>-q</code></p>
<dd>Quiet mode. Do not print anything.</p>
<dt><code>-r</code> <i>megabytes</i></p>
<dd>mkfs.gfs2 will try to make resource groups approximately this large. The minimum resource group size is 32 MB and the maximum is 2048 MB. A large resource group size may increase performance on very large file systems. If not specified, mkfs.gfs2 will choose the resource group size based on the size and alignment characteristics of the target device.</p>
<dt><code>-t</code> <i>clustername:lockspace</i></p>
<dd>The &quot;lock table&quot; pair used to uniquely identify this filesystem in a cluster. The cluster name segment (maximum 32 characters) must match the name given to your cluster in its configuration; only members of this cluster are permitted to use this file system. The lockspace segment (maximum 30 characters) is a unique file system name used to distinguish this gfs2 file system. Valid <i>clustername</i>s and <i>lockspace</i>s may only contain alphanumeric characters, hyphens (-) and underscores (_).</p>
<dt><code>-V</code></p>
<dd>Print program version information, then exit.</p>
<dt><i>block-count</i></p>
<dd>Use <i>block-count</i> as the size of the filesystem instead of using the whole device. <i>block-count</i> is specified as a number of filesystem blocks.</dl>
<h2>Example</h2>
<pre><dl><dt><dd># mkfs.gfs2 -t mycluster:mygfs2 -p lock_dlm -j 2 /dev/vg0/lv_gfs2
This will create a gfs2 filesystem on the block device /dev/vg0/lv_gfs2. It
will belong to a cluster named &quot;mycluster&quot; and use the &quot;mygfs2&quot; lock space. It
will use DLM for locking and create journals for a two-node cluster.
# mkfs.gfs2 -t mycluster:mygfs2 -p lock_nolock -j 3 /dev/vg0/lv_gfs2
This will create a filesystem on the block device /dev/vg0/lv_gfs2. It
will belong to a cluster named &quot;mycluster&quot; and use the &quot;mygfs2&quot; lockspace, but
it will have no cluster locking by default as lock_nolock is used. It will
have journals for a three-node cluster.
</dl></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-gfs2/">gfs2</a></code>(5), <code><a href="/docs/linux/man/8-gfs2_jadd/">gfs2_jadd</a></code>(8), <code><a href="/docs/linux/man/8-gfs2_grow/">gfs2_grow</a></code>(8) </p>
