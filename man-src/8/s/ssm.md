---
title: "ssm(8)"
name: "ssm"
section: "8"
letter: "s"
url: "/docs/linux/man/8-ssm/"
description: "ssm – System Storage Manager: a single tool to manage your storage"
---

<p>ssm &#8211; System Storage Manager: a single tool to manage your storage</p>
<h2>Synopsis</h2>
<p><code>ssm</code> [<code>-h</code>] [<code>&#8211;version</code>] [<code>-v</code>] [<code>-f</code>] [<code>-b</code> BACKEND] [<code>-n</code>] {check,resize,create,list,add,remove,snapshot,mount} &#8230; </p>
<p> <code>ssm</code> <code>create</code> [<code>-h</code>] [<code>-s</code> SIZE] [<code>-n</code> NAME] [<code>&#8211;fstype</code> FSTYPE] [<code>-r</code> LEVEL] [<code>-I</code> STRIPESIZE] [<code>-i</code> STRIPES] [<code>-p</code> POOL] [<code>-e</code> [{luks,plain}]] [<code>-o</code> MNT_OPTIONS] [<code>-v</code> VIRTUAL_SIZE] [<code>device</code> [<code>device</code> &#8230;]] [mount] </p>
<p> <code>ssm</code> <code>list</code> [<code>-h</code>] [{volumes,vol,dev,devices,pool,pools,fs,filesystems,snap,snapshots}] </p>
<p> <code>ssm</code> <code>remove</code> [<code>-h</code>] [<code>-a</code>] [<code>items</code> [<code>items</code> &#8230;]] </p>
<p> <code>ssm</code> <code>resize</code> [<code>-h</code>] [<code>-s</code> SIZE] <code>volume</code> [<code>device</code> [<code>device</code> &#8230;]] </p>
<p> <code>ssm</code> <code>check</code> [<code>-h</code>] <code>device</code> [<code>device</code> &#8230;] </p>
<p> <code>ssm</code> <code>snapshot</code> [<code>-h</code>] [<code>-s</code> SIZE] [<code>-d</code> DEST | <code>-n</code> NAME] volume </p>
<p> <code>ssm</code> <code>add</code> [<code>-h</code>] [<code>-p</code> POOL] <code>device</code> [<code>device</code> &#8230;] </p>
<p> <code>ssm</code> <code>mount</code> [<code>-h</code>] [<code>-o</code> OPTIONS] <code>volume</code> directory</p>
<h2>Description</h2>
<p>System Storage Manager provides an easy to use command line interface to manage your storage using various technologies like lvm, btrfs, encrypted volumes and more. </p>
<p> In more sophisticated enterprise storage environments, management with Device Mapper (dm), Logical Volume Manager (LVM), or Multiple Devices (md) is becoming increasingly more difficult. With file systems added to the mix, the number of tools needed to configure and manage storage has grown so large that it is simply not user friendly. With so many options for a system administrator to consider, the opportunity for errors and problems is large. </p>
<p> The btrfs administration tools have shown us that storage management can be simplified, and we are working to bring that ease of use to Linux filesystems in general.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd>show program&#8217;s version number and exit</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd>Show aditional information while executing.</p>
<dt><code>-f</code>,<code> &#8211;force</code></p>
<dd>Force execution in the case where ssm has some doubts or questions.</p>
<dt><code>-b</code><i>&nbsp;<wbr>BACKEND</i>,<code>&nbsp;<wbr>&#8211;backend</code><i>&nbsp;<wbr>BACKEND</i></p>
<dd>Choose backend to use. Currently you can choose from (lvm,btrfs,crypt).</p>
<dt><code>-n</code>,<code> &#8211;dry-run</code></p>
<dd>Dry run. Do not do anything, just parse the command line options and gather system information if necessary. Note that with this option ssm will not perform all the check as some of them are done by the backends themselves. This option is mainly used for debugging purposes, but still requires root privileges.</dl>
<h2>System Storage Manager Commands</h2>
<h3>Introduction</h3>
<p>System Storage Manager has several commands that you can specify on the command line as a first argument to ssm. They all have a specific use and their own arguments, but global ssm arguments are propagated to all commands.</p>
<h3>Create command</h3>
<p><code>ssm</code> <code>create</code> [<code>-h</code>] [<code>-s</code> SIZE] [<code>-n</code> NAME] [<code>&#8211;fstype</code> FSTYPE] [<code>-r</code> LEVEL] [<code>-I</code> STRIPESIZE] [<code>-i</code> STRIPES] [<code>-p</code> POOL] [<code>-e</code> [{luks,plain}]] [<code>-o</code> MNT_OPTIONS] [<code>-v</code> VIRTUAL_SIZE] [<code>device</code> [<code>device</code> &#8230;]] [mount] </p>
<p> This command creates a new volume with defined parameters. If a <code>device</code> is provided it will be used to create the volume, hence it will be added into the <code>pool</code> prior to volume creation (See <i>Add command section</i>). More than one device can be used to create a volume. </p>
<p> If the <code>device</code> is already being used in a different pool, then <code>ssm</code> will ask you whether you want to remove it from the original pool. If you decline, or the removal fails, then the <code>volume</code> creation fails if the <i>SIZE</i> was not provided. On the other hand, if the <i>SIZE</i> is provided and some devices can not be added to the <code>pool</code>, the volume creation might still succeed if there is enough space in the <code>pool</code>. </p>
<p> In addition to specifying size of the volume directly, percentage can be specified as well. Specify <code>&#8211;size 70%</code> to indicate the volume size to be 70% of total pool size. Additionally, percentage of the used, or free pool space can be specified as well using keywords FREE, or USED respectively. </p>
<p> The <i>POOL</i> name can be specified as well. If the pool exists, a new volume will be created from that pool (optionally adding <code>device</code> into the pool). However if the <i>POOL</i> does not exist, then <code>ssm</code> will attempt to create a new pool with the provided <code>device</code>, and then create a new volume from this pool. If the <code>&#8211;backend</code> argument is omitted, the default <code>ssm</code> backend will be used. The default backend is <i>lvm</i>. </p>
<p> <code>ssm</code> also supports creating a RAID configuration, however some back-ends might not support all RAID levels, or may not even support RAID at all. In this case, volume creation will fail. </p>
<p> If a <code>mount</code> point is provided, <code>ssm</code> will attempt to mount the volume after it is created. However it will fail if mountable file system is not present on the volume. </p>
<p> If the backend allows it (currently only supported with <code>lvm</code> backend), <code>ssm</code> can be used to create <code>thinly provisioned volumes</code> by specifying <code>&#8211;virtual-size</code> option. This will automatically create a <code>thin pool</code> of a given size provided with <code>&#8211;size</code> option and <code>thin volume</code> of a given size provided with <code>&#8211;virtual-size</code> option and name provided with <code>&#8211;name</code> option. Virtual size can be much bigger than available space in the <code>pool</code>.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>-s</code><i>&nbsp;<wbr>SIZE</i>,<code>&nbsp;<wbr>&#8211;size</code><i>&nbsp;<wbr>SIZE</i></p>
<dd>Gives the size to allocate for the new logical volume. A size suffix K|k, M|m, G|g, T|t, P|p, E|e can be used to define &#8216;power of two&#8217; units. If no unit is provided, it defaults to kilobytes. This is optional and if not given, maximum possible size will be used. Additionally the new size can be specified as a percentage of the total pool size (50%), as a percentage of free pool space (50%FREE), or as a percentage of used pool space (50%USED).</p>
<dt><code>-n</code><i>&nbsp;<wbr>NAME</i>,<code>&nbsp;<wbr>&#8211;name</code><i>&nbsp;<wbr>NAME</i></p>
<dd>The name for the new logical volume. This is optional and if omitted, name will be generated by the corresponding backend.</p>
<dt><code>&#8211;fstype</code><i>&nbsp;<wbr>FSTYPE</i></p>
<dd>Gives the file system type to create on the new logical volume. Supported file systems are (ext3, ext4, xfs, btrfs). This is optional and if not given file system will not be created.</p>
<dt><code>-r</code><i>&nbsp;<wbr>LEVEL</i>,<code>&nbsp;<wbr>&#8211;raid</code><i>&nbsp;<wbr>LEVEL</i></p>
<dd>Specify a RAID level you want to use when creating a new volume. Note that some backends might not implement all supported RAID levels. This is optional and if no specified, linear volume will be created. You can choose from the following list of supported levels (0,1,10).</p>
<dt><code>-I</code><i>&nbsp;<wbr>STRIPESIZE</i>,<code>&nbsp;<wbr>&#8211;stripesize</code><i>&nbsp;<wbr>STRIPESIZE</i></p>
<dd>Gives the number of kilobytes for the granularity of stripes. This is optional and if not given, backend default will be used. Note that you have to specify RAID level as well.</p>
<dt><code>-i</code><i>&nbsp;<wbr>STRIPES</i>,<code>&nbsp;<wbr>&#8211;stripes</code><i>&nbsp;<wbr>STRIPES</i></p>
<dd>Gives the number of stripes. This is equal to the number of physical volumes to scatter the logical volume. This is optional and if stripesize is set and multiple devices are provided stripes is determined automatically from the number of devices. Note that you have to specify RAID level as well.</p>
<dt><code>-p</code><i>&nbsp;<wbr>POOL</i>,<code>&nbsp;<wbr>&#8211;pool</code><i>&nbsp;<wbr>POOL</i></p>
<dd>Pool to use to create the new volume.</p>
<dt><code>-e [{luks,plain}], &#8211;encrypt [{luks,plain}]</code></p>
<dd>Create encrpted volume. Extension to use can be specified.</p>
<dt><code>-o</code><i>&nbsp;<wbr>MNT_OPTIONS</i>,<code>&nbsp;<wbr>&#8211;mnt-options</code><i>&nbsp;<wbr>MNT_OPTIONS</i></p>
<dd>Mount options are specified with a -o flag followed by a comma separated string of options. This option is equivalent to the -o <a href="/docs/linux/man/8-mount/">mount</a>(8) option.</p>
<dt><code>-v</code><i>&nbsp;<wbr>VIRTUAL_SIZE</i>,<code>&nbsp;<wbr>&#8211;virtual-size</code><i>&nbsp;<wbr>VIRTUAL_SIZE</i></p>
<dd>Gives the virtual size for the new thinly provisioned volume. A size suffix K|k, M|m, G|g, T|t, P|p, E|e can be used to define &#8216;power of two&#8217; units. If no unit is provided, it defaults to kilobytes.</dl>
<h3>List command</h3>
<p><code>ssm</code> <code>list</code> [<code>-h</code>] [{volumes,vol,dev,devices,pool,pools,fs,filesystems,snap,snapshots}] </p>
<p> Lists information about all detected devices, pools, volumes and snapshots found on the system. The <code>list</code> command can be used either alone to list all of the information, or you can request specific sections only. </p>
<p> The following sections can be specified:</p>
<dl>
<dt><code>{volumes | vol}</code></p>
<dd>List information about all <code>volumes</code> found in the system.</p>
<dt><code>{devices | dev}</code></p>
<dd>List information about all <code>devices</code> found on the system. Some devices are intentionally hidden, like for example cdrom or DM/MD devices since those are actually listed as volumes.</p>
<dt><code>{pools | pool}</code></p>
<dd>List information about all <code>pools</code> found in the system.</p>
<dt><code>{filesystems | fs}</code></p>
<dd>List information about all volumes containing <code>filesystems</code> found in the system.</p>
<dt><code>{snapshots | snap}</code></p>
<dd>List information about all <code>snapshots</code> found in the system. Note that some back-ends do not support snapshotting and some cannot distinguish snapshot from regular volumes. In this case, <code>ssm</code> will try to recognize the volume name in order to identify a <code>snapshot</code>, but if the <code>ssm</code> regular expression does not match the snapshot pattern, the problematic snapshot will not be recognized.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>show this help message and exit</dl>
<h3>Remove command</h3>
<p><code>ssm</code> <code>remove</code> [<code>-h</code>] [<code>-a</code>] [<code>items</code> [<code>items</code> &#8230;]] </p>
<p> This command removes an <code>item</code> from the system. Multiple items can be specified. If the <code>item</code> cannot be removed for some reason, it will be skipped. </p>
<p> An <code>item</code> can be any of the following:</p>
<dl>
<dt><code>device</code></p>
<dd>Remove a <code>device</code> from the pool. Note that this cannot be done in some cases where the device is being used by the pool. You can use the <code>-f</code> argument to <i>force</i> removal. If the device does not belong to any pool, it will be skipped.</p>
<dt><code>pool</code></p>
<dd>Remove a <code>pool</code> from the system. This will also remove all volumes created from that pool.</p>
<dt><code>volume</code></p>
<dd>Remove a <code>volume</code> from the system. Note that this will fail if the <code>volume</code> is mounted and cannot be <i>forced</i> with <code>-f</code>.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>-a</code>,<code> &#8211;all</code></p>
<dd>Remove all pools in the system.</dl>
<h3>Resize command</h3>
<p><code>ssm</code> <code>resize</code> [<code>-h</code>] [<code>-s</code> SIZE] <code>volume</code> [<code>device</code> [<code>device</code> &#8230;]] </p>
<p> Change size of the <code>volume</code> and file system. If there is no file system, only the <code>volume</code> itself will be resized. You can specify a <code>device</code> to add into the <code>volume</code> pool prior the resize. Note that the <code>device</code> will only be added into the pool if the <code>volume</code> size is going to grow. </p>
<p> If the <code>device</code> is already used in a different pool, then <code>ssm</code> will ask you whether or not you want to remove it from the original pool. </p>
<p> In some cases, the file system has to be mounted in order to resize. This will be handled by <code>ssm</code> automatically by mounting the <code>volume</code> temporarily. </p>
<p> In addition to specifying new size of the volume directly, percentage can be specified as well. Specify <code>&#8211;size 70%</code> to resize the volume to 70% of it&#8217;s original size. Additionally, percentage of the used, or free pool space can be specified as well using keywords FREE, or USED respectively. </p>
<p> Note that resizing btrfs subvolume is not supported, only the whole file system can be resized.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>-s</code><i>&nbsp;<wbr>SIZE</i>,<code>&nbsp;<wbr>&#8211;size</code><i>&nbsp;<wbr>SIZE</i></p>
<dd>New size of the volume. With the + or &#8211; sign the value is added to or subtracted from the actual size of the volume and without it, the value will be set as the new volume size. A size suffix of [k|K] for kilobytes, [m|M] for megabytes, [g|G] for gigabytes, [t|T] for terabytes or [p|P] for petabytes is optional. If no unit is provided the default is kilobytes. Additionally the new size can be specified as a percentage of the original volume size ([+][-]50%), as a percentage of free pool space ([+][-]50%FREE), or as a percentage of used pool space ([+][-]50%USED).</dl>
<h3>Check command</h3>
<p><code>ssm</code> <code>check</code> [<code>-h</code>] <code>device</code> [<code>device</code> &#8230;] </p>
<p> Check the file system consistency on the <code>volume</code>. You can specify multiple volumes to check. If there is no file system on the <code>volume</code>, this <code>volume</code> will be skipped. </p>
<p> In some cases the file system has to be mounted in order to check the file system. This will be handled by <code>ssm</code> automatically by mounting the <code>volume</code> temporarily.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>show this help message and exit</dl>
<h3>Snapshot command</h3>
<p><code>ssm</code> <code>snapshot</code> [<code>-h</code>] [<code>-s</code> SIZE] [<code>-d</code> DEST | <code>-n</code> NAME] volume </p>
<p> Take a snapshot of an existing <code>volume</code>. This operation will fail if the back-end to which the <code>volume</code> belongs to does not support snapshotting. Note that you cannot specify both <i>NAME</i> and <i>DEST</i> since those options are mutually exclusive. </p>
<p> In addition to specifying new size of the volume directly, percentage can be specified as well. Specify <code>&#8211;size 70%</code> to indicate the new snapshot size to be 70% of the origin volume size. Additionally, percentage of the used, or free pool space can be specified as well using keywords FREE, or USED respectively. </p>
<p> In some cases the file system has to be mounted in order to take a snapshot of the <code>volume</code>. This will be handled by <code>ssm</code> automatically by mounting the <code>volume</code> temporarily.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>-s</code><i>&nbsp;<wbr>SIZE</i>,<code>&nbsp;<wbr>&#8211;size</code><i>&nbsp;<wbr>SIZE</i></p>
<dd>Gives the size to allocate for the new snapshot volume. A size suffix K|k, M|m, G|g, T|t, P|p, E|e can be used to define &#8216;power of two&#8217; units. If no unit is provided, it defaults to kilobytes. This is optional and if not given, the size will be determined automatically. Additionally the new size can be specified as a percentage of the original volume size (50%), as a percentage of free pool space (50%FREE), or as a percentage of used pool space (50%USED).</p>
<dt><code>-d</code><i>&nbsp;<wbr>DEST</i>,<code>&nbsp;<wbr>&#8211;dest</code><i>&nbsp;<wbr>DEST</i></p>
<dd>Destination of the snapshot specified with absolute path to be used for the new snapshot. This is optional and if not specified default backend policy will be performed.</p>
<dt><code>-n</code><i>&nbsp;<wbr>NAME</i>,<code>&nbsp;<wbr>&#8211;name</code><i>&nbsp;<wbr>NAME</i></p>
<dd>Name of the new snapshot. This is optional and if not specified default backend policy will be performed.</dl>
<h3>Add command</h3>
<p><code>ssm</code> <code>add</code> [<code>-h</code>] [<code>-p</code> POOL] <code>device</code> [<code>device</code> &#8230;] </p>
<p> This command adds a <code>device</code> into the pool. By default, the <code>device</code> will not be added if it&#8217;s already a part of a different pool, but the user will be asked whether or not to remove the device from its pool. When multiple devices are provided, all of them are added into the pool. If one of the devices cannot be added into the pool for any reason, the add command will fail. If no pool is specified, the default pool will be chosen. In the case of a non existing pool, it will be created using the provided devices.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>-p</code><i>&nbsp;<wbr>POOL</i>,<code>&nbsp;<wbr>&#8211;pool</code><i>&nbsp;<wbr>POOL</i></p>
<dd>Pool to add device into. If not specified the default pool is used.</dl>
<h3>Mount command</h3>
<p><code>ssm</code> <code>mount</code> [<code>-h</code>] [<code>-o</code> OPTIONS] <code>volume</code> directory </p>
<p> This command will mount the <code>volume</code> at the specified <code>directory</code>. The <code>volume</code> can be specified in the same way as with <code><a href="/docs/linux/man/8-mount/">mount</a>(8)</code>, however in addition, one can also specify a <code>volume</code> in the format as it appears in the <code>ssm list</code> table. </p>
<p> For example, instead of finding out what the device and subvolume id of the btrfs subvolume &quot;btrfs_pool:vol001&quot; is in order to mount it, one can simply call <code>ssm mount btrfs_pool:vol001 /mnt/test</code>. </p>
<p> One can also specify <i>OPTIONS</i> in the same way as with <code><a href="/docs/linux/man/8-mount/">mount</a>(8)</code>.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>-o</code><i>&nbsp;<wbr>OPTIONS</i>,<code>&nbsp;<wbr>&#8211;options</code><i>&nbsp;<wbr>OPTIONS</i></p>
<dd>Options are specified with a -o flag followed by a comma separated string of options. This option is equivalent to the same <a href="/docs/linux/man/8-mount/">mount</a>(8) option.</dl>
<h2>Back-Ends</h2>
<h3>Introduction</h3>
<p>Ssm aims to create a unified user interface for various technologies like Device Mapper (dm), Btrfs file system, Multiple Devices (md) and possibly more. In order to do so we have a core abstraction layer in <code>ssmlib/main.py</code>. This abstraction layer should ideally know nothing about the underlying technology, but rather comply with <code>device</code>, <code>pool</code> and <code>volume</code> abstractions. </p>
<p> Various backends can be registered in <code>ssmlib/main.py</code> in order to handle specific storage technology, implementing methods like <i>create</i>, <i>snapshot</i>, or <i>remove</i> volumes and pools. The core will then call these methods to manage the storage without needing to know what lies underneath it. There are already several backends registered in ssm.</p>
<h3>Btrfs backend</h3>
<p>Btrfs is the file system with many advanced features including volume management. This is the reason why btrfs is handled differently than other <i>conventional</i> file systems in <code>ssm</code>. It is used as a volume management back-end. </p>
<p> Pools, volumes and snapshots can be created with btrfs backend and here is what it means from the btrfs point of view:</p>
<dl>
<dt><code>pool</code></p>
<dd>A pool is actually a btrfs file system itself, because it can be extended by adding more devices, or shrunk by removing devices from it. Subvolumes and snapshots can also be created. When the new btrfs pool should be created, <code>ssm</code> simply creates a btrfs file system, which means that every new btrfs pool has one volume of the same name as the pool itself which can not be removed without removing the entire pool. The default btrfs pool name is <code>btrfs_pool</code>. </p>
<p> When creating a new btrfs pool, the name of the pool is used as the file system label. If there is an already existing btrfs file system in the system without a label, a btrfs pool name will be generated for internal use in the following format &quot;btrfs_{device base name}&quot;. </p>
<p> A btrfs pool is created when the <code>create</code> or <code>add</code> command is used with specified devices and non existing pool name.</p>
<dt><code>volume</code></p>
<dd>A volume in the btrfs back-end is actually just btrfs subvolume with the exception of the first volume created on btrfs pool creation, which is the file system itself. Subvolumes can only be created on the btrfs file system when it is mounted, but the user does not have to worry about that since <code>ssm</code> will automatically mount the file system temporarily in order to create a new subvolume. </p>
<p> The volume name is used as subvolume path in the btrfs file system and every object in this path must exist in order to create a volume. The volume name for internal tracking and that is visible to the user is generated in the format &quot;{pool_name}:{volume name}&quot;, but volumes can be also referenced by its mount point. </p>
<p> The btrfs volumes are only shown in the <i>list</i> output, when the file system is mounted, with the exception of the main btrfs volume &#8211; the file system itself. </p>
<p> Also note that btrfs volumes and subvolumes cannot be resized. This is mainly limitation of the btrfs tools which currently do not work reliably. </p>
<p> A new btrfs volume can be created with the <code>create</code> command.</p>
<dt><code>snapshot</code></p>
<dd>The btrfs file system supports subvolume snapshotting, so you can take a snapshot of any btrfs volume in the system with <code>ssm</code>. However btrfs does not distinguish between subvolumes and snapshots, because a snapshot is actually just a subvolume with some blocks shared with a different subvolume. This means, that <code>ssm</code> is not able to directly recognize a btrfs snapshot. Instead, <code>ssm</code> will try to recognize a special name format of the btrfs volume that denotes it is a snapshot. However, if the <i>NAME</i> is specified when creating snapshot which does not match the special pattern, snapshot will not be recognized by the <code>ssm</code> and it will be listed as regular btrfs volume. </p>
<p> A new btrfs snapshot can be created with the <code>snapshot</code> command.</p>
<dt><code>device</code></p>
<dd>Btrfs does not require a special device to be created on.</dl>
<h3>Lvm backend</h3>
<p>Pools, volumes and snapshots can be created with lvm, which pretty much match the lvm abstraction.</p>
<dl>
<dt><code>pool</code></p>
<dd>An lvm pool is just a <i>volume group</i> in lvm language. It means that it is grouping devices and new logical volumes can be created out of the lvm pool. The default lvm pool name is <code>lvm_pool</code>. </p>
<p> An lvm pool is created when the <code>create</code> or <code>add</code> commands are used with specified devices and a non existing pool name. </p>
<p> Alternatively a <code>thin pool</code> can be created as a result of using <code>&#8211;virtual-size</code> option to create <code>thin volume</code>.</p>
<dt><code>volume</code></p>
<dd>An lvm volume is just a <i>logical volume</i> in lvm language. An lvm volume can be created with the <code>create</code> command.</p>
<dt><code>snapshot</code></p>
<dd>Lvm volumes can be snapshotted as well. When a snapshot is created from the lvm volume, a new <i>snapshot</i> volume is created, which can be handled as any other lvm volume. Unlike <i>btrfs</i> lvm is able to distinguish snapshot from regular volume, so there is no need for a snapshot name to match special pattern.</p>
<dt><code>device</code></p>
<dd>Lvm requires a <i>physical device</i> to be created on the device, but with <code>ssm</code> this is transparent for the user.</dl>
<h3>Crypt backend</h3>
<p>The crypt backend in <code>ssm</code> uses cryptsetup and dm-crypt target to manage encrypted volumes. The crypt backend can be used as a regular backend for creating encrypted volumes on top of regular block devices, or even other volumes (lvm or md volumes for example). Or it can be used to create encrypted lvm volumes right away in a single step. </p>
<p> Only volumes can be created with crypt backend. This backend does not support pooling and does not require special devices.</p>
<dl>
<dt><code>pool</code></p>
<dd>The crypt backend does not support pooling, and it is not possible to create crypt pool or add a device into a pool.</p>
<dt><code>volume</code></p>
<dd>A volume in the crypt backend is the volume created by dm-crypt which represents the data on the original encrypted device in unencrypted form. The crypt backend does not support pooling, so only one device can be used to create crypt volume. It also does not support raid or any device concatenation. </p>
<p> Currently two modes, or extensions are supported: luks and plain. Luks is used by default. For more information about the extensions, please see <code>cryptsetup</code> manual page.</p>
<dt><code>snapshot</code></p>
<dd>The crypt backend does not support snapshotting, however if the encrypted volume is created on top of an lvm volume, the lvm volume itself can be snapshotted. The snapshot can be then opened by using <code>cryptsetup</code>. It is possible that this might change in the future so that <code>ssm</code> will be able to activate the volume directly without the extra step.</p>
<dt><code>device</code></p>
<dd>The crypt backend does not require a special device to be created on.</dl>
<h3>MD backend</h3>
<p>MD backend in <code>ssm</code> is currently limited to only gather the information about MD volumes in the system. You can not create or manage MD volumes or pools, but this functionality will be extended in the future.</p>
<h2>Examples</h2>
<p><code>List</code> system storage information: </p>
<pre># ssm list</pre>
<p><code>List</code> all pools in the system: </p>
<pre># ssm list pools</pre>
<p><code>Create</code> a new 100GB <code>volume</code> with the default lvm backend using <i>/dev/sda</i> and <i>/dev/sdb</i> with xfs file system: </p>
<pre># ssm create --size 100G --fs xfs /dev/sda /dev/sdb</pre>
<p><code>Create</code> a new <code>volume</code> with a btrfs backend using <i>/dev/sda</i> and <i>/dev/sdb</i> and let the volume to be RAID 1: </p>
<pre># ssm -b btrfs create --raid 1 /dev/sda /dev/sdb</pre>
<p>Using the lvm backend <code>create</code> a RAID 0 <code>volume</code> with devices <i>/dev/sda</i> and <i>/dev/sdb</i> with 128kB stripe size, ext4 file system and mount it on <i>/home</i>: </p>
<pre># ssm create --raid 0 --stripesize 128k /dev/sda /dev/sdb /home</pre>
<p><code>Create</code> a new <code>thinly provisioned volume</code> with a lvm backend using devices <i>/dev/sda</i> and <i>/dev/sdb</i> using <i>&#8211;virtual-size</i> option: </p>
<pre># ssm create --virtual-size 1T /dev/sda /dev/sdb</pre>
<p><code>Create</code> a new <code>thinly provisioned volume</code> with a defined <code>thin pool</code> size and devices <i>/dev/sda</i> and <i>/dev/sdb</i>: </p>
<pre># ssm create --size 50G --virtual-size 1T /dev/sda /dev/sdb</pre>
<p><code>Extend</code> btrfs <code>volume</code> <i>btrfs_pool</i> by 500GB and use <i>/dev/sdc</i> and <i>/dev/sde</i> to cover the resize: </p>
<pre># ssm resize -s +500G btrfs_pool /dev/sdc /dev/sde</pre>
<p><code>Shrink volume</code> <i>/dev/lvm_pool/lvol001</i> by 1TB: </p>
<pre># ssm resize -s-1t /dev/lvm_pool/lvol001</pre>
<p><code>Remove</code> <i>/dev/sda</i> <code>device</code> from the pool, remove the <i>btrfs_pool</i> <code>pool</code> and also remove the <code>volume</code> <i>/dev/lvm_pool/lvol001</i>: </p>
<pre># ssm remove /dev/sda btrfs_pool /dev/lvm_pool/lvol001</pre>
<p><code>Take a snapshot</code> of the btrfs volume <i>btrfs_pool:my_volume</i>: </p>
<pre># ssm snapshot btrfs_pool:my_volume</pre>
<p><code>Add devices</code> <i>/dev/sda</i> and <i>/dev/sdb</i> into the <i>btrfs_pool</i> pool: </p>
<pre># ssm add -p btrfs_pool /dev/sda /dev/sdb</pre>
<p><code>Mount btrfs subvolume</code> <i>btrfs_pool:vol001</i> on <i>/mnt/test</i>: </p>
<pre># ssm mount btrfs_pool:vol001 /mnt/test</pre>
<h2>Environment Variables</h2>
<dl>
<dt><code>SSM_DEFAULT_BACKEND</code></p>
<dd>Specify which backend will be used by default. This can be overridden by specifying the <code>-b</code> or <code>&#8211;backend</code> argument. Currently only <i>lvm</i> and <i>btrfs</i> are supported.</p>
<dt><code>SSM_LVM_DEFAULT_POOL</code></p>
<dd>Name of the default lvm pool to be used if the <code>-p</code> or <code>&#8211;pool</code> argument is omitted.</p>
<dt><code>SSM_BTRFS_DEFAULT_POOL</code></p>
<dd>Name of the default btrfs pool to be used if the <code>-p</code> or <code>&#8211;pool</code> argument is omitted.</p>
<dt><code>SSM_PREFIX_FILTER</code></p>
<dd>When this is set, <code>ssm</code> will filter out all devices, volumes and pools whose name does not start with this prefix. It is used mainly in the <code>ssm</code> test suite to make sure that we do not scramble the local system configuration.</dl>
<h2>Licence</h2>
<p>(C)2011 Red Hat, Inc., Lukas Czerner &lt;<i>lczerner [at] redhat.com</i>&gt; </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program. If not, see &lt;<i><a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a></i>&gt;.</p>
<h2>Requirements</h2>
<p>Python 2.6 or higher is required to run this tool. System Storage Manager can only be run as root since most of the commands require root privileges. </p>
<p> There are other requirements listed below, but note that you do not necessarily need all dependencies for all backends. However if some of the tools required by a backend are missing, that backend will not work.</p>
<h3>Python modules</h3>
<dl>
<dt>&bull;</p>
<dd>os</p>
<dt>&bull;</p>
<dd>re</p>
<dt>&bull;</p>
<dd>sys</p>
<dt>&bull;</p>
<dd>stat</p>
<dt>&bull;</p>
<dd>argparse</p>
<dt>&bull;</p>
<dd>datetime</p>
<dt>&bull;</p>
<dd>threading</p>
<dt>&bull;</p>
<dd>subprocess</dl>
<h3>System tools</h3>
<dl>
<dt>&bull;</p>
<dd>tune2fs</p>
<dt>&bull;</p>
<dd>fsck.SUPPORTED_FS</p>
<dt>&bull;</p>
<dd>resize2fs</p>
<dt>&bull;</p>
<dd>xfs_db</p>
<dt>&bull;</p>
<dd>xfs_check</p>
<dt>&bull;</p>
<dd>xfs_growfs</p>
<dt>&bull;</p>
<dd>mkfs.SUPPORTED_FS</p>
<dt>&bull;</p>
<dd>which</p>
<dt>&bull;</p>
<dd>mount</p>
<dt>&bull;</p>
<dd>blkid</p>
<dt>&bull;</p>
<dd>wipefs</dl>
<h3>Lvm backend</h3>
<dl>
<dt>&bull;</p>
<dd>lvm2 binaries</dl>
<h3>Btrfs backend</h3>
<dl>
<dt>&bull;</p>
<dd>btrfs progs</dl>
<h3>Crypt backend</h3>
<dl>
<dt>&bull;</p>
<dd>dmsetup</p>
<dt>&bull;</p>
<dd>cryptsetup</dl>
<h2>Availability</h2>
<p><code>System storage manager</code> is available from <i><a rel="nofollow" href="http://storagemanager.sourceforge.net">http://storagemanager.sourceforge.net</a></i>. You can subscribe to <i>storagemanager-devel [at] lists.sourceforge.net</i> to follow the current development.</p>
<h2>Author</h2>
<p>LukÃ¡Å¡ Czerner &lt;lczerner [at] redhat.com&gt;</p>
<h2>Copyright</h2>
<p>2015, Red Hat, Inc., LukÃ¡Å¡ Czerner &lt;lczerner [at] redhat.com&gt;</p>
