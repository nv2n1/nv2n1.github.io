---
title: "mdadm(8)"
name: "mdadm"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mdadm/"
description: "mdadm – manage MD devices aka Linux Software RAID"
---

<p>mdadm &#8211; manage MD devices <i>aka</i> Linux Software RAID</p>
<h2>Synopsis</h2>
<p><code>mdadm</code><i> [mode] &lt;raiddevice&gt; [options] &lt;component-devices&gt;</i> </p>
<h2>Description</h2>
<p>RAID devices are virtual devices created from two or more real block devices. This allows multiple devices (typically disk drives or partitions thereof) to be combined into a single device to hold (for example) a single filesystem. Some RAID levels include redundancy and so can survive some degree of device failure. Linux Software RAID devices are implemented through the md (Multiple Devices) device driver. Currently, Linux supports <code>LINEAR</code> md devices, <code>RAID0</code> (striping), <code>RAID1</code> (mirroring), <code>RAID4</code>, <code>RAID5</code>, <code>RAID6</code>, <code>RAID10</code>, <code>MULTIPATH</code>, <code>FAULTY</code>, and <code>CONTAINER</code>. <code>MULTIPATH</code> is not a Software RAID mechanism, but does involve multiple devices: each device is a path to one common physical storage device. New installations should not use md/multipath as it is not well supported and has no ongoing development. Use the Device Mapper based multipath-tools instead. <code>FAULTY</code> is also not true RAID, and it only involves one device. It provides a layer over a true device that can be used to inject faults. <code>CONTAINER</code> is different again. A <code>CONTAINER</code> is a collection of devices that are managed as a set. This is similar to the set of devices connected to a hardware RAID controller. The set of devices may contain a number of different RAID arrays each utilising some (or all) of the blocks from a number of the devices in the set. For example, two devices in a 5-device set might form a RAID1 using the whole devices. The remaining three might have a RAID5 over the first half of each device, and a RAID0 over the second half. With a <code>CONTAINER</code>, there is one set of metadata that describes all of the arrays in the container. So when <i>mdadm</i> creates a <code>CONTAINER</code> device, the device just represents the metadata. Other normal arrays (RAID1 etc) can be created inside the container. </p>
<h2>Modes</h2>
<p>mdadm has several major modes of operation:</p>
<dl>
<dt><code>Assemble</code></p>
<dd>Assemble the components of a previously created array into an active array. Components can be explicitly given or can be searched for. <i>mdadm</i> checks that the components do form a bona fide array, and can, on request, fiddle superblock information so as to assemble a faulty array. </p>
<dt><code>Build</code></p>
<dd>Build an array that doesn&#8217;t have per-device metadata (superblocks). For these sorts of arrays, <i>mdadm</i> cannot differentiate between initial creation and subsequent assembly of an array. It also cannot perform any checks that appropriate components have been requested. Because of this, the <code>Build</code> mode should only be used together with a complete understanding of what you are doing. </p>
<dt><code>Create</code></p>
<dd>Create a new array with per-device metadata (superblocks). Appropriate metadata is written to each device, and then the array comprising those devices is activated. A &#8216;resync&#8217; process is started to make sure that the array is consistent (e.g. both sides of a mirror contain the same data) but the content of the device is left otherwise untouched. The array can be used as soon as it has been created. There is no need to wait for the initial resync to finish. </p>
<dt><code>Follow or Monitor</code></p>
<dd>Monitor one or more md devices and act on any state changes. This is only meaningful for RAID1, 4, 5, 6, 10 or multipath arrays, as only these have interesting state. RAID0 or Linear never have missing, spare, or failed drives, so there is nothing to monitor. </p>
<dt><code>Grow</code></p>
<dd>Grow (or shrink) an array, or otherwise reshape it in some way. Currently supported growth options including changing the active size of component devices and changing the number of active devices in Linear and RAID levels 0/1/4/5/6, changing the RAID level between 0, 1, 5, and 6, and between 0 and 10, changing the chunk size and layout for RAID 0,4,5,6,10 as well as adding or removing a write-intent bitmap and changing the array&#8217;s consistency policy. </p>
<dt><code>Incremental Assembly</code></p>
<dd>Add a single device to an appropriate array. If the addition of the device makes the array runnable, the array will be started. This provides a convenient interface to a <i>hot-plug</i> system. As each device is detected, <i>mdadm</i> has a chance to include it in some array as appropriate. Optionally, when the <i>&#8211;fail</i> flag is passed in we will remove the device from any active array instead of adding it. </p>
<p> If a <code>CONTAINER</code> is passed to <i>mdadm</i> in this mode, then any arrays within that container will be assembled and started. </p>
<dt><code>Manage</code></p>
<dd>This is for doing things to specific components of an array such as adding new spares and removing faulty devices. </p>
<dt><code>Misc</code></p>
<dd>This is an &#8216;everything else&#8217; mode that supports operations on active arrays, operations on component devices such as erasing old superblocks, and information gathering operations. </p>
<dt><code>Auto-detect</code></p>
<dd>This mode does not act on a specific device or array, but rather it requests the Linux Kernel to activate any auto-detected arrays.</dl>
<h2>Options</h2>
<h2>Options for selecting a mode are:</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;assemble</code></p>
<dd>Assemble a pre-existing array. </p>
<dt><code>-B</code>, <code>&#8211;build</code></p>
<dd>Build a legacy array without superblocks. </p>
<dt><code>-C</code>, <code>&#8211;create</code></p>
<dd>Create a new array. </p>
<dt><code>-F</code>, <code>&#8211;follow</code>, <code>&#8211;monitor</code></p>
<dd>Select <code>Monitor</code> mode. </p>
<dt><code>-G</code>, <code>&#8211;grow</code></p>
<dd>Change the size or shape of an active array. </p>
<dt><code>-I</code>, <code>&#8211;incremental</code></p>
<dd>Add/remove a single device to/from an appropriate array, and possibly start the array. </p>
<dt><code>&#8211;auto-detect</code></p>
<dd>Request that the kernel starts any auto-detected arrays. This can only work if <i>md</i> is compiled into the kernel &#8212; not if it is a module. Arrays can be auto-detected by the kernel if all the components are in primary MS-DOS partitions with partition type <code>FD</code>, and all use v0.90 metadata. In-kernel autodetect is not recommended for new installations. Using <i>mdadm</i> to detect and assemble arrays &#8212; possibly in an <i>initrd</i> &#8212; is substantially more flexible and should be preferred. </p>
</dl>
<p> If a device is given before any options, or if the first option is one of <code>&#8211;add</code>, <code>&#8211;re-add</code>, <code>&#8211;add-spare</code>, <code>&#8211;fail</code>, <code>&#8211;remove</code>, or <code>&#8211;replace</code>, then the MANAGE mode is assumed. Anything other than these will cause the <code>Misc</code> mode to be assumed.</p>
<h2>Options that are not mode-specific are:</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display general help message or, after one of the above options, a mode-specific help message. </p>
<dt><code>&#8211;help-options</code></p>
<dd>Display more detailed help about command line parsing and some commonly used options. </p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information for mdadm. </p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Be more verbose about what is happening. This can be used twice to be extra-verbose. The extra verbosity currently only affects <code>&#8211;detail &#8211;scan</code> and <code>&#8211;examine &#8211;scan</code>. </p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Avoid printing purely informative messages. With this, <i>mdadm</i> will be silent unless there is something really important to report. </p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Be more forceful about certain operations. See the various modes for the exact meaning of this option in different contexts. </p>
<dt><code>-c</code>, <code>&#8211;config=</code></p>
<dd>Specify the config file or directory. Default is to use <code>/etc/mdadm/mdadm.conf</code> and <code>/etc/mdadm/mdadm.conf.d</code>, or if those are missing then <code>/etc/mdadm.conf</code> and <code>/etc/mdadm.conf.d</code>. If the config file given is <code>partitions</code> then nothing will be read, but <i>mdadm</i> will act as though the config file contained exactly<br />
 <code> DEVICE partitions containers</code><br />
 and will read <code>/proc/partitions</code> to find a list of devices to scan, and <code>/proc/mdstat</code> to find a list of containers to examine. If the word <code>none</code> is given for the config file, then <i>mdadm</i> will act as though the config file were empty. </p>
<p> If the name given is of a directory, then <i>mdadm</i> will collect all the files contained in the directory with a name ending in <code>.conf</code>, sort them lexically, and process all of those files as config files. </p>
<dt><code>-s</code>, <code>&#8211;scan</code></p>
<dd>Scan config file or <code>/proc/mdstat</code> for missing information. In general, this option gives <i>mdadm</i> permission to get any missing information (like component devices, array devices, array identities, and alert destination) from the configuration file (see previous option); one exception is MISC mode when using <code>&#8211;detail</code> or <code>&#8211;stop,</code> in which case <code>&#8211;scan</code> says to get a list of array devices from <code>/proc/mdstat</code>. </p>
<dt><code>-e</code>, <code>&#8211;metadata=</code></p>
<dd>Declare the style of RAID metadata (superblock) to be used. The default is 1.2 for <code>&#8211;create</code>, and to guess for other operations. The default can be overridden by setting the <code>metadata</code> value for the <code>CREATE</code> keyword in <code>mdadm.conf</code>. </p>
<p> Options are:</p>
<dl>
<dd>
<dl>
<dt>0, 0.90, default</p>
<dd>
<dt>0, 0.90</p>
<dd>Use the original 0.90 format superblock. This format limits arrays to 28 component devices and limits component devices of levels 1 and greater to 2 terabytes. It is also possible for there to be confusion about whether the superblock applies to a whole device or just the last partition, if that partition starts on a 64K boundary.</p>
<dt>1, 1.0, 1.1, 1.2</p>
<dd>
<dt>1, 1.0, 1.1, 1.2 default</p>
<dd>Use the new version-1 format superblock. This has fewer restrictions. It can easily be moved between hosts with different endian-ness, and a recovery operation can be checkpointed and restarted. The different sub-versions store the superblock at different locations on the device, either at the end (for 1.0), at the start (for 1.1) or 4K from the start (for 1.2). &quot;1&quot; is equivalent to &quot;1.2&quot; (the commonly preferred 1.x format).<br />
&nbsp;&quot;default&quot;&nbsp;is equivalent to&nbsp;&quot;1.2&quot;.</p>
<dt>ddf</p>
<dd>Use the &quot;Industry Standard&quot; DDF (Disk Data Format) format defined by SNIA. When creating a DDF array a <code>CONTAINER</code> will be created, and normal arrays can be created in that container.</p>
<dt>imsm</p>
<dd>Use the Intel(R) Matrix Storage Manager metadata format. This creates a <code>CONTAINER</code> which is managed in a similar manner to DDF, and is supported by an option-rom on some platforms:</p>
<dd><code><a rel="nofollow" href="http://www.intel.com/design/chipsets/matrixstorage_sb.htm">http://www.intel.com/design/chipsets/matrixstorage_sb.htm</a></code></dl>
</dl>
<dt><code>&#8211;homehost=</code></p>
<dd>This will override any <code>HOMEHOST</code> setting in the config file and provides the identity of the host which should be considered the home for any arrays. </p>
<p> When creating an array, the <code>homehost</code> will be recorded in the metadata. For version-1 superblocks, it will be prefixed to the array name. For version-0.90 superblocks, part of the SHA1 hash of the hostname will be stored in the later half of the UUID. </p>
<p> When reporting information about an array, any array which is tagged for the given homehost will be reported as such. </p>
<p> When using Auto-Assemble, only arrays tagged for the given homehost will be allowed to use &#8216;local&#8217; names (i.e. not ending in &#8216;_&#8217; followed by a digit string). See below under <code>Auto Assembly</code>. </p>
<p> The special name &quot;<code>any</code>&quot; can be used as a wild card. If an array is created with <code>&#8211;homehost=any</code> then the name &quot;<code>any</code>&quot; will be stored in the array and it can be assembled in the same way on any host. If an array is assembled with this option, then the homehost recorded on the array will be ignored. </p>
<dt><code>&#8211;prefer=</code></p>
<dd>When <i>mdadm</i> needs to print the name for a device it normally finds the name in <code>/dev</code> which refers to the device and is shortest. When a path component is given with <code>&#8211;prefer</code> <i>mdadm</i> will prefer a longer name if it contains that component. For example <code>&#8211;prefer=by-uuid</code> will prefer a name in a subdirectory of <code>/dev</code> called <code>by-uuid</code>. </p>
<p> This functionality is currently only provided by <code>&#8211;detail</code> and <code>&#8211;monitor</code>. </p>
<dt><code>&#8211;home-cluster=</code></p>
<dd>specifies the cluster name for the md device. The md device can be assembled only on the cluster which matches the name specified. If this option is not provided, mdadm tries to detect the cluster name automatically. </p>
</dl>
<h2>For create, build, or grow:</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;raid-devices=</code></p>
<dd>Specify the number of active devices in the array. This, plus the number of spare devices (see below) must equal the number of <i>component-devices</i> (including &quot;<code>missing</code>&quot; devices) that are listed on the command line for <code>&#8211;create</code>. Setting a value of 1 is probably a mistake and so requires that <code>&#8211;force</code> be specified first. A value of 1 will then be allowed for linear, multipath, RAID0 and RAID1. It is never allowed for RAID4, RAID5 or RAID6.<br />
 This number can only be changed using <code>&#8211;grow</code> for RAID1, RAID4, RAID5 and RAID6 arrays, and only on kernels which provide the necessary support. </p>
<dt><code>-x</code>, <code>&#8211;spare-devices=</code></p>
<dd>Specify the number of spare (eXtra) devices in the initial array. Spares can also be added and removed later. The number of component devices listed on the command line must equal the number of RAID devices plus the number of spare devices. </p>
<dt><code>-z</code>, <code>&#8211;size=</code></p>
<dd>Amount (in Kilobytes) of space to use from each drive in RAID levels 1/4/5/6. This must be a multiple of the chunk size, and must leave about 128Kb of space at the end of the drive for the RAID superblock. If this is not specified (as it normally is not) the smallest drive (or partition) sets the size, though if there is a variance among the drives of greater than 1%, a warning is issued. </p>
<p> A suffix of &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; can be given to indicate Kilobytes, Megabytes or Gigabytes respectively. </p>
<p> Sometimes a replacement drive can be a little smaller than the original drives though this should be minimised by IDEMA standards. Such a replacement drive will be rejected by <i>md</i>. To guard against this it can be useful to set the initial size slightly smaller than the smaller device with the aim that it will still be larger than any replacement. </p>
<p> This value can be set with <code>&#8211;grow</code> for RAID level 1/4/5/6 though <code>CONTAINER</code> based arrays such as those with IMSM metadata may not be able to support this. If the array was created with a size smaller than the currently active drives, the extra space can be accessed using <code>&#8211;grow</code>. The size can be given as <code>max</code> which means to choose the largest size that fits on all current drives. </p>
<p> Before reducing the size of the array (with <code>&#8211;grow &#8211;size=</code>) you should make sure that space isn&#8217;t needed. If the device holds a filesystem, you would need to resize the filesystem to use less space. </p>
<p> After reducing the array size you should check that the data stored in the device is still available. If the device holds a filesystem, then an &#8216;fsck&#8217; of the filesystem is a minimum requirement. If there are problems the array can be made bigger again with no loss with another <code>&#8211;grow &#8211;size=</code> command. </p>
<p> This value cannot be used when creating a <code>CONTAINER</code> such as with DDF and IMSM metadata, though it perfectly valid when creating an array inside a container. </p>
<dt><code>-Z</code>, <code>&#8211;array-size=</code></p>
<dd>This is only meaningful with <code>&#8211;grow</code> and its effect is not persistent: when the array is stopped and restarted the default array size will be restored. </p>
<p> Setting the array-size causes the array to appear smaller to programs that access the data. This is particularly needed before reshaping an array so that it will be smaller. As the reshape is not reversible, but setting the size with <code>&#8211;array-size</code> is, it is required that the array size is reduced as appropriate before the number of devices in the array is reduced. </p>
<p> Before reducing the size of the array you should make sure that space isn&#8217;t needed. If the device holds a filesystem, you would need to resize the filesystem to use less space. </p>
<p> After reducing the array size you should check that the data stored in the device is still available. If the device holds a filesystem, then an &#8216;fsck&#8217; of the filesystem is a minimum requirement. If there are problems the array can be made bigger again with no loss with another <code>&#8211;grow &#8211;array-size=</code> command. </p>
<p> A suffix of &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; can be given to indicate Kilobytes, Megabytes or Gigabytes respectively. A value of <code>max</code> restores the apparent size of the array to be whatever the real amount of available space is. </p>
<p> Clustered arrays do not support this parameter yet. </p>
<dt><code>-c</code>, <code>&#8211;chunk=</code></p>
<dd>Specify chunk size of kilobytes. The default when creating an array is 512KB. To ensure compatibility with earlier versions, the default when building an array with no persistent metadata is 64KB. This is only meaningful for RAID0, RAID4, RAID5, RAID6, and RAID10. </p>
<p> RAID4, RAID5, RAID6, and RAID10 require the chunk size to be a power of 2. In any case it must be a multiple of 4KB. </p>
<p> A suffix of &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; can be given to indicate Kilobytes, Megabytes or Gigabytes respectively. </p>
<dt><code>&#8211;rounding=</code></p>
<dd>Specify rounding factor for a Linear array. The size of each component will be rounded down to a multiple of this size. This is a synonym for <code>&#8211;chunk</code> but highlights the different meaning for Linear as compared to other RAID levels. The default is 64K if a kernel earlier than 2.6.16 is in use, and is 0K (i.e. no rounding) in later kernels. </p>
<dt><code>-l</code>, <code>&#8211;level=</code></p>
<dd>Set RAID level. When used with <code>&#8211;create</code>, options are: linear, raid0, 0, stripe, raid1, 1, mirror, raid4, 4, raid5, 5, raid6, 6, raid10, 10, multipath, mp, faulty, container. Obviously some of these are synonymous. </p>
<p> When a <code>CONTAINER</code> metadata type is requested, only the <code>container</code> level is permitted, and it does not need to be explicitly given. </p>
<p> When used with <code>&#8211;build</code>, only linear, stripe, raid0, 0, raid1, multipath, mp, and faulty are valid. </p>
<p> Can be used with <code>&#8211;grow</code> to change the RAID level in some cases. See LEVEL CHANGES below. </p>
<dt><code>-p</code>, <code>&#8211;layout=</code></p>
<dd>This option configures the fine details of data layout for RAID5, RAID6, and RAID10 arrays, and controls the failure modes for <i>faulty</i>. </p>
<p> The layout of the RAID5 parity block can be one of <code>left-asymmetric</code>, <code>left-symmetric</code>, <code>right-asymmetric</code>, <code>right-symmetric</code>, <code>la</code>, <code>ra</code>, <code>ls</code>, <code>rs</code>. The default is <code>left-symmetric</code>. </p>
<p> It is also possible to cause RAID5 to use a RAID4-like layout by choosing <code>parity-first</code>, or <code>parity-last</code>. </p>
<p> Finally for RAID5 there are DDF-compatible layouts, <code>ddf-zero-restart</code>, <code>ddf-N-restart</code>, and <code>ddf-N-continue</code>. </p>
<p> These same layouts are available for RAID6. There are also 4 layouts that will provide an intermediate stage for converting between RAID5 and RAID6. These provide a layout which is identical to the corresponding RAID5 layout on the first N-1 devices, and has the &#8216;Q&#8217; syndrome (the second &#8216;parity&#8217; block used by RAID6) on the last device. These layouts are: <code>left-symmetric-6</code>, <code>right-symmetric-6</code>, <code>left-asymmetric-6</code>, <code>right-asymmetric-6</code>, and <code>parity-first-6</code>. </p>
<p> When setting the failure mode for level <i>faulty,</i> the options are: <code>write-transient</code>, <code>wt</code>, <code>read-transient</code>, <code>rt</code>, <code>write-persistent</code>, <code>wp</code>, <code>read-persistent</code>, <code>rp</code>, <code>write-all</code>, <code>read-fixable</code>, <code>rf</code>, <code>clear</code>, <code>flush</code>, <code>none</code>. </p>
<p> Each failure mode can be followed by a number, which is used as a period between fault generation. Without a number, the fault is generated once on the first relevant request. With a number, the fault will be generated after that many requests, and will continue to be generated every time the period elapses. </p>
<p> Multiple failure modes can be current simultaneously by using the <code>&#8211;grow</code> option to set subsequent failure modes. </p>
<p> &quot;clear&quot; or &quot;none&quot; will remove any pending or periodic failure modes, and &quot;flush&quot; will clear any persistent faults. </p>
<p> Finally, the layout options for RAID10 are one of &#8216;n&#8217;, &#8216;o&#8217; or &#8216;f&#8217; followed by a small number. The default is &#8216;n2&#8217;. The supported options are: </p>
<p> <i>&#8216;n&#8217;</i> signals &#8216;near&#8217; copies. Multiple copies of one data block are at similar offsets in different devices. </p>
<p> <i>&#8216;o&#8217;</i> signals &#8216;offset&#8217; copies. Rather than the chunks being duplicated within a stripe, whole stripes are duplicated but are rotated by one device so duplicate blocks are on different devices. Thus subsequent copies of a block are in the next drive, and are one chunk further down. </p>
<p> <i>&#8216;f&#8217;</i> signals &#8216;far&#8217; copies (multiple copies have very different offsets). See <a href="/docs/linux/man/4-md/">md</a>(4) for more detail about &#8216;near&#8217;, &#8216;offset&#8217;, and &#8216;far&#8217;. </p>
<p> The number is the number of copies of each datablock. 2 is normal, 3 can be useful. This number can be at most equal to the number of devices in the array. It does not need to divide evenly into that number (e.g. it is perfectly legal to have an &#8216;n2&#8217; layout for an array with an odd number of devices). </p>
<p> When an array is converted between RAID5 and RAID6 an intermediate RAID6 layout is used in which the second parity block (Q) is always on the last device. To convert a RAID5 to RAID6 and leave it in this new layout (which does not require re-striping) use <code>&#8211;layout=preserve</code>. This will try to avoid any restriping. </p>
<p> The converse of this is <code>&#8211;layout=normalise</code> which will change a non-standard RAID6 layout into a more standard arrangement. </p>
<dt><code>&#8211;parity=</code></p>
<dd>same as <code>&#8211;layout</code> (thus explaining the p of <code>-p</code>). </p>
<dt><code>-b</code>, <code>&#8211;bitmap=</code></p>
<dd>Specify a file to store a write-intent bitmap in. The file should not exist unless <code>&#8211;force</code> is also given. The same file should be provided when assembling the array. If the word <code>internal</code> is given, then the bitmap is stored with the metadata on the array, and so is replicated on all devices. If the word <code>none</code> is given with <code>&#8211;grow</code> mode, then any bitmap that is present is removed. If the word <code>clustered</code> is given, the array is created for a clustered environment. One bitmap is created for each node as defined by the <code>&#8211;nodes</code> parameter and are stored internally. </p>
<p> To help catch typing errors, the filename must contain at least one slash (&#8216;/&#8217;) if it is a real file (not &#8216;internal&#8217; or &#8216;none&#8217;). </p>
<p> Note: external bitmaps are only known to work on ext2 and ext3. Storing bitmap files on other filesystems may result in serious problems. </p>
<p> When creating an array on devices which are 100G or larger, <i>mdadm</i> automatically adds an internal bitmap as it will usually be beneficial. This can be suppressed with <code>&#8211;bitmap=none</code> or by selecting a different consistency policy with <code>&#8211;consistency-policy</code>. </p>
<dt><code>&#8211;bitmap-chunk=</code></p>
<dd>Set the chunksize of the bitmap. Each bit corresponds to that many Kilobytes of storage. When using a file based bitmap, the default is to use the smallest size that is at-least 4 and requires no more than 2^21 chunks. When using an <code>internal</code> bitmap, the chunksize defaults to 64Meg, or larger if necessary to fit the bitmap into the available space. </p>
<p> A suffix of &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; can be given to indicate Kilobytes, Megabytes or Gigabytes respectively. </p>
<dt><code>-W</code>, <code>&#8211;write-mostly</code></p>
<dd>subsequent devices listed in a <code>&#8211;build</code>, <code>&#8211;create</code>, or <code>&#8211;add</code> command will be flagged as &#8216;write-mostly&#8217;. This is valid for RAID1 only and means that the &#8216;md&#8217; driver will avoid reading from these devices if at all possible. This can be useful if mirroring over a slow link. </p>
<dt><code>&#8211;write-behind=</code></p>
<dd>Specify that write-behind mode should be enabled (valid for RAID1 only). If an argument is specified, it will set the maximum number of outstanding writes allowed. The default value is 256. A write-intent bitmap is required in order to use write-behind mode, and write-behind is only attempted on drives marked as <i>write-mostly</i>. </p>
<dt><code>&#8211;failfast</code></p>
<dd>subsequent devices listed in a <code>&#8211;create</code> or <code>&#8211;add</code> command will be flagged as &#8216;failfast&#8217;. This is valid for RAID1 and RAID10 only. IO requests to these devices will be encouraged to fail quickly rather than cause long delays due to error handling. Also no attempt is made to repair a read error on these devices. </p>
<p> If an array becomes degraded so that the &#8216;failfast&#8217; device is the only usable device, the &#8216;failfast&#8217; flag will then be ignored and extended delays will be preferred to complete failure. </p>
<p> The &#8216;failfast&#8217; flag is appropriate for storage arrays which have a low probability of true failure, but which may sometimes cause unacceptable delays due to internal maintenance functions. </p>
<dt><code>&#8211;assume-clean</code></p>
<dd>Tell <i>mdadm</i> that the array pre-existed and is known to be clean. It can be useful when trying to recover from a major failure as you can be sure that no data will be affected unless you actually write to the array. It can also be used when creating a RAID1 or RAID10 if you want to avoid the initial resync, however this practice &#8212; while normally safe &#8212; is not recommended. Use this only if you really know what you are doing.</p>
<dd>When the devices that will be part of a new array were filled with zeros before creation the operator knows the array is actually clean. If that is the case, such as after running badblocks, this argument can be used to tell mdadm the facts the operator knows.</p>
<dd>When an array is resized to a larger size with <code>&#8211;grow &#8211;size=</code> the new space is normally resynced in that same way that the whole array is resynced at creation. From Linux version 3.0, <code>&#8211;assume-clean</code> can be used with that command to avoid the automatic resync. </p>
<dt><code>&#8211;backup-file=</code></p>
<dd>This is needed when <code>&#8211;grow</code> is used to increase the number of raid-devices in a RAID5 or RAID6 if there are no spare devices available, or to shrink, change RAID level or layout. See the GROW MODE section below on RAID-DEVICES CHANGES. The file must be stored on a separate device, not on the RAID array being reshaped. </p>
<dt><code>&#8211;data-offset=</code></p>
<dd>Arrays with 1.x metadata can leave a gap between the start of the device and the start of array data. This gap can be used for various metadata. The start of data is known as the <i>data-offset</i>. Normally an appropriate data offset is computed automatically. However it can be useful to set it explicitly such as when re-creating an array which was originally created using a different version of <i>mdadm</i> which computed a different offset. </p>
<p> Setting the offset explicitly over-rides the default. The value given is in Kilobytes unless a suffix of &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; is used to explicitly indicate Kilobytes, Megabytes or Gigabytes respectively. </p>
<p> Since Linux 3.4, <code>&#8211;data-offset</code> can also be used with <code>&#8211;grow</code> for some RAID levels (initially on RAID10). This allows the data-offset to be changed as part of the reshape process. When the data offset is changed, no backup file is required as the difference in offsets is used to provide the same functionality. </p>
<p> When the new offset is earlier than the old offset, the number of devices in the array cannot shrink. When it is after the old offset, the number of devices in the array cannot increase. </p>
<p> When creating an array, <code>&#8211;data-offset</code> can be specified as <code>variable</code>. In the case each member device is expected to have a offset appended to the name, separated by a colon. This makes it possible to recreate exactly an array which has varying data offsets (as can happen when different versions of <i>mdadm</i> are used to add different devices). </p>
<dt><code>&#8211;continue</code></p>
<dd>This option is complementary to the <code>&#8211;freeze-reshape</code> option for assembly. It is needed when <code>&#8211;grow</code> operation is interrupted and it is not restarted automatically due to <code>&#8211;freeze-reshape</code> usage during array assembly. This option is used together with <code>-G</code> , ( <code>&#8211;grow</code> ) command and device for a pending reshape to be continued. All parameters required for reshape continuation will be read from array metadata. If initial <code>&#8211;grow</code> command had required <code>&#8211;backup-file=</code> option to be set, continuation option will require to have exactly the same backup file given as well.</p>
<dd>Any other parameter passed together with <code>&#8211;continue</code> option will be ignored. </p>
<dt><code>-N</code>, <code>&#8211;name=</code></p>
<dd>Set a <code>name</code> for the array. This is currently only effective when creating an array with a version-1 superblock, or an array in a DDF container. The name is a simple textual string that can be used to identify array components when assembling. If name is needed but not specified, it is taken from the basename of the device that is being created. e.g. when creating <i>/dev/md/home</i> the <code>name</code> will default to <i>home</i>. </p>
<dt><code>-R</code>, <code>&#8211;run</code></p>
<dd>Insist that <i>mdadm</i> run the array, even if some of the components appear to be active in another array or filesystem. Normally <i>mdadm</i> will ask for confirmation before including such components in an array. This option causes that question to be suppressed. </p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Insist that <i>mdadm</i> accept the geometry and layout specified without question. Normally <i>mdadm</i> will not allow creation of an array with only one device, and will try to create a RAID5 array with one missing drive (as this makes the initial resync work faster). With <code>&#8211;force</code>, <i>mdadm</i> will not try to be so clever. </p>
<dt><code>-o</code>, <code>&#8211;readonly</code></p>
<dd>Start the array <code>read only</code> rather than read-write as normal. No writes will be allowed to the array, and no resync, recovery, or reshape will be started. It works with Create, Assemble, Manage and Misc mode. </p>
<dt><code>-a</code>, <code>&#8211;auto{=yes,md,mdp,part,p}{NN}</code></p>
<dd>Instruct mdadm how to create the device file if needed, possibly allocating an unused minor number. &quot;md&quot; causes a non-partitionable array to be used (though since Linux 2.6.28, these array devices are in fact partitionable). &quot;mdp&quot;, &quot;part&quot; or &quot;p&quot; causes a partitionable array (2.6 and later) to be used. &quot;yes&quot; requires the named md device to have a &#8216;standard&#8217; format, and the type and minor number will be determined from this. With mdadm 3.0, device creation is normally left up to <i>udev</i> so this option is unlikely to be needed. See DEVICE NAMES below. </p>
<p> The argument can also come immediately after &quot;-a&quot;. e.g. &quot;-ap&quot;. </p>
<p> If <code>&#8211;auto</code> is not given on the command line or in the config file, then the default will be <code>&#8211;auto=yes</code>. </p>
<p> If <code>&#8211;scan</code> is also given, then any <i>auto=</i> entries in the config file will override the <code>&#8211;auto</code> instruction given on the command line. </p>
<p> For partitionable arrays, <i>mdadm</i> will create the device file for the whole array and for the first 4 partitions. A different number of partitions can be specified at the end of this option (e.g. <code>&#8211;auto=p7</code>). If the device name ends with a digit, the partition names add a &#8216;p&#8217;, and a number, e.g. <i>/dev/md/home1p3</i>. If there is no trailing digit, then the partition names just have a number added, e.g. <i>/dev/md/scratch3</i>. </p>
<p> If the md device name is in a &#8216;standard&#8217; format as described in DEVICE NAMES, then it will be created, if necessary, with the appropriate device number based on that name. If the device name is not in one of these formats, then a unused device number will be allocated. The device number will be considered unused if there is no active array for that number, and there is no entry in /dev for that number and with a non-standard name. Names that are not in &#8216;standard&#8217; format are only allowed in &quot;/dev/md/&quot;. </p>
<p> This is meaningful with <code>&#8211;create</code> or <code>&#8211;build</code>. </p>
<dt><code>-a</code>, <code>&#8211;add</code></p>
<dd>This option can be used in Grow mode in two cases. </p>
<p> If the target array is a Linear array, then <code>&#8211;add</code> can be used to add one or more devices to the array. They are simply catenated on to the end of the array. Once added, the devices cannot be removed. </p>
<p> If the <code>&#8211;raid-disks</code> option is being used to increase the number of devices in an array, then <code>&#8211;add</code> can be used to add some extra devices to be included in the array. In most cases this is not needed as the extra devices can be added as spares first, and then the number of raid-disks can be changed. However for RAID0, it is not possible to add spares. So to increase the number of devices in a RAID0, it is necessary to set the new number of devices, and to add the new devices, in the same command. </p>
<dt><code>&#8211;nodes</code></p>
<dd>Only works when the array is for clustered environment. It specifies the maximum number of nodes in the cluster that will use this device simultaneously. If not specified, this defaults to 4. </p>
<dt><code>&#8211;write-journal</code></p>
<dd>Specify journal device for the RAID-4/5/6 array. The journal device should be a SSD with reasonable lifetime. </p>
<dt><code>&#8211;symlinks</code></p>
<dd>Auto creation of symlinks in /dev to /dev/md, option &#8211;symlinks must be &#8216;no&#8217; or &#8216;yes&#8217; and work with &#8211;create and &#8211;build. </p>
<dt><code>-k</code>, <code>&#8211;consistency-policy=</code></p>
<dd>Specify how the array maintains consistency in case of unexpected shutdown. Only relevant for RAID levels with redundancy. Currently supported options are:</p>
<dl>
<dd>
<dl>
<dt><code>resync</code></p>
<dd>Full resync is performed and all redundancy is regenerated when the array is started after unclean shutdown. </p>
<dt><code>bitmap</code></p>
<dd>Resync assisted by a write-intent bitmap. Implicitly selected when using <code>&#8211;bitmap</code>. </p>
<dt><code>journal</code></p>
<dd>For RAID levels 4/5/6, journal device is used to log transactions and replay after unclean shutdown. Implicitly selected when using <code>&#8211;write-journal</code>. </p>
<dt><code>ppl</code></p>
<dd>For RAID5 only, Partial Parity Log is used to close the write hole and eliminate resync. PPL is stored in the metadata region of RAID member drives, no additional journal drive is needed. </p>
</dl>
<p> Can be used with &#8211;grow to change the consistency policy of an active array in some cases. See CONSISTENCY POLICY CHANGES below.</dl>
</dl>
<h2>For assemble:</h2>
<dl>
<dt><code>-u</code>, <code>&#8211;uuid=</code></p>
<dd>uuid of array to assemble. Devices which don&#8217;t have this uuid are excluded </p>
<dt><code>-m</code>, <code>&#8211;super-minor=</code></p>
<dd>Minor number of device that array was created for. Devices which don&#8217;t have this minor number are excluded. If you create an array as /dev/md1, then all superblocks will contain the minor number 1, even if the array is later assembled as /dev/md2. </p>
<p> Giving the literal word &quot;dev&quot; for <code>&#8211;super-minor</code> will cause <i>mdadm</i> to use the minor number of the md device that is being assembled. e.g. when assembling <code>/dev/md0</code>, <code>&#8211;super-minor=dev</code> will look for super blocks with a minor number of 0. </p>
<p> <code>&#8211;super-minor</code> is only relevant for v0.90 metadata, and should not normally be used. Using <code>&#8211;uuid</code> is much safer. </p>
<dt><code>-N</code>, <code>&#8211;name=</code></p>
<dd>Specify the name of the array to assemble. This must be the name that was specified when creating the array. It must either match the name stored in the superblock exactly, or it must match with the current <i>homehost</i> prefixed to the start of the given name. </p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Assemble the array even if the metadata on some devices appears to be out-of-date. If <i>mdadm</i> cannot find enough working devices to start the array, but can find some devices that are recorded as having failed, then it will mark those devices as working so that the array can be started. An array which requires <code>&#8211;force</code> to be started may contain data corruption. Use it carefully. </p>
<dt><code>-R</code>, <code>&#8211;run</code></p>
<dd>Attempt to start the array even if fewer drives were given than were present last time the array was active. Normally if not all the expected drives are found and <code>&#8211;scan</code> is not used, then the array will be assembled but not started. With <code>&#8211;run</code> an attempt will be made to start it anyway. </p>
<dt><code>&#8211;no-degraded</code></p>
<dd>This is the reverse of <code>&#8211;run</code> in that it inhibits the startup of array unless all expected drives are present. This is only needed with <code>&#8211;scan,</code> and can be used if the physical connections to devices are not as reliable as you would like. </p>
<dt><code>-a</code>, <code>&#8211;auto{=no,yes,md,mdp,part}</code></p>
<dd>See this option under Create and Build options. </p>
<dt><code>-b</code>, <code>&#8211;bitmap=</code></p>
<dd>Specify the bitmap file that was given when the array was created. If an array has an <code>internal</code> bitmap, there is no need to specify this when assembling the array. </p>
<dt><code>&#8211;backup-file=</code></p>
<dd>If <code>&#8211;backup-file</code> was used while reshaping an array (e.g. changing number of devices or chunk size) and the system crashed during the critical section, then the same <code>&#8211;backup-file</code> must be presented to <code>&#8211;assemble</code> to allow possibly corrupted data to be restored, and the reshape to be completed. </p>
<dt><code>&#8211;invalid-backup</code></p>
<dd>If the file needed for the above option is not available for any reason an empty file can be given together with this option to indicate that the backup file is invalid. In this case the data that was being rearranged at the time of the crash could be irrecoverably lost, but the rest of the array may still be recoverable. This option should only be used as a last resort if there is no way to recover the backup file. </p>
<dt><code>-U</code>, <code>&#8211;update=</code></p>
<dd>Update the superblock on each device while assembling the array. The argument given to this flag can be one of <code>sparc2.2</code>, <code>summaries</code>, <code>uuid</code>, <code>name</code>, <code>nodes</code>, <code>homehost</code>, <code>home-cluster</code>, <code>resync</code>, <code>byteorder</code>, <code>devicesize</code>, <code>no-bitmap</code>, <code>bbl</code>, <code>no-bbl</code>, <code>ppl</code>, <code>no-ppl</code>, <code>metadata</code>, or <code>super-minor</code>. </p>
<p> The <code>sparc2.2</code> option will adjust the superblock of an array what was created on a Sparc machine running a patched 2.2 Linux kernel. This kernel got the alignment of part of the superblock wrong. You can use the <code>&#8211;examine &#8211;sparc2.2</code> option to <i>mdadm</i> to see what effect this would have. </p>
<p> The <code>super-minor</code> option will update the <code>preferred minor</code> field on each superblock to match the minor number of the array being assembled. This can be useful if <code>&#8211;examine</code> reports a different &quot;Preferred Minor&quot; to <code>&#8211;detail</code>. In some cases this update will be performed automatically by the kernel driver. In particular the update happens automatically at the first write to an array with redundancy (RAID level 1 or greater) on a 2.6 (or later) kernel. </p>
<p> The <code>uuid</code> option will change the uuid of the array. If a UUID is given with the <code>&#8211;uuid</code> option that UUID will be used as a new UUID and will <code>NOT</code> be used to help identify the devices in the array. If no <code>&#8211;uuid</code> is given, a random UUID is chosen. </p>
<p> The <code>name</code> option will change the <i>name</i> of the array as stored in the superblock. This is only supported for version-1 superblocks. </p>
<p> The <code>nodes</code> option will change the <i>nodes</i> of the array as stored in the bitmap superblock. This option only works for a clustered environment. </p>
<p> The <code>homehost</code> option will change the <i>homehost</i> as recorded in the superblock. For version-0 superblocks, this is the same as updating the UUID. For version-1 superblocks, this involves updating the name. </p>
<p> The <code>home-cluster</code> option will change the cluster name as recorded in the superblock and bitmap. This option only works for clustered environment. </p>
<p> The <code>resync</code> option will cause the array to be marked <i>dirty</i> meaning that any redundancy in the array (e.g. parity for RAID5, copies for RAID1) may be incorrect. This will cause the RAID system to perform a &quot;resync&quot; pass to make sure that all redundant information is correct. </p>
<p> The <code>byteorder</code> option allows arrays to be moved between machines with different byte-order, such as from a big-endian machine like a Sparc or some MIPS machines, to a little-endian x86_64 machine. When assembling such an array for the first time after a move, giving <code>&#8211;update=byteorder</code> will cause <i>mdadm</i> to expect superblocks to have their byteorder reversed, and will correct that order before assembling the array. This is only valid with original (Version 0.90) superblocks. </p>
<p> The <code>summaries</code> option will correct the summaries in the superblock. That is the counts of total, working, active, failed, and spare devices. </p>
<p> The <code>devicesize</code> option will rarely be of use. It applies to version 1.1 and 1.2 metadata only (where the metadata is at the start of the device) and is only useful when the component device has changed size (typically become larger). The version 1 metadata records the amount of the device that can be used to store data, so if a device in a version 1.1 or 1.2 array becomes larger, the metadata will still be visible, but the extra space will not. In this case it might be useful to assemble the array with <code>&#8211;update=devicesize</code>. This will cause <i>mdadm</i> to determine the maximum usable amount of space on each device and update the relevant field in the metadata. </p>
<p> The <code>metadata</code> option only works on v0.90 metadata arrays and will convert them to v1.0 metadata. The array must not be dirty (i.e. it must not need a sync) and it must not have a write-intent bitmap. </p>
<p> The old metadata will remain on the devices, but will appear older than the new metadata and so will usually be ignored. The old metadata (or indeed the new metadata) can be removed by giving the appropriate <code>&#8211;metadata=</code> option to <code>&#8211;zero-superblock</code>. </p>
<p> The <code>no-bitmap</code> option can be used when an array has an internal bitmap which is corrupt in some way so that assembling the array normally fails. It will cause any internal bitmap to be ignored. </p>
<p> The <code>bbl</code> option will reserve space in each device for a bad block list. This will be 4K in size and positioned near the end of any free space between the superblock and the data. </p>
<p> The <code>no-bbl</code> option will cause any reservation of space for a bad block list to be removed. If the bad block list contains entries, this will fail, as removing the list could cause data corruption. </p>
<p> The <code>ppl</code> option will enable PPL for a RAID5 array and reserve space for PPL on each device. There must be enough free space between the data and superblock and a write-intent bitmap or journal must not be used. </p>
<p> The <code>no-ppl</code> option will disable PPL in the superblock. </p>
<dt><code>&#8211;freeze-reshape</code></p>
<dd>Option is intended to be used in start-up scripts during initrd boot phase. When array under reshape is assembled during initrd phase, this option stops reshape after reshape critical section is being restored. This happens before file system pivot operation and avoids loss of file system context. Losing file system context would cause reshape to be broken. </p>
<p> Reshape can be continued later using the <code>&#8211;continue</code> option for the grow command. </p>
<dt><code>&#8211;symlinks</code></p>
<dd>See this option under Create and Build options. </p>
</dl>
<h2>For Manage mode:</h2>
<dl>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd>Unless a more serious error occurred, <i>mdadm</i> will exit with a status of 2 if no changes were made to the array and 0 if at least one change was made. This can be useful when an indirect specifier such as <code>missing</code>, <code>detached</code> or <code>faulty</code> is used in requesting an operation on the array. <code>&#8211;test</code> will report failure if these specifiers didn&#8217;t find any match. </p>
<dt><code>-a</code>, <code>&#8211;add</code></p>
<dd>hot-add listed devices. If a device appears to have recently been part of the array (possibly it failed or was removed) the device is re-added as described in the next point. If that fails or the device was never part of the array, the device is added as a hot-spare. If the array is degraded, it will immediately start to rebuild data onto that spare. </p>
<p> Note that this and the following options are only meaningful on array with redundancy. They don&#8217;t apply to RAID0 or Linear. </p>
<dt><code>&#8211;re-add</code></p>
<dd>re-add a device that was previously removed from an array. If the metadata on the device reports that it is a member of the array, and the slot that it used is still vacant, then the device will be added back to the array in the same position. This will normally cause the data for that device to be recovered. However based on the event count on the device, the recovery may only require sections that are flagged a write-intent bitmap to be recovered or may not require any recovery at all. </p>
<p> When used on an array that has no metadata (i.e. it was built with <code>&#8211;build)</code> it will be assumed that bitmap-based recovery is enough to make the device fully consistent with the array. </p>
<p> When used with v1.x metadata, <code>&#8211;re-add</code> can be accompanied by <code>&#8211;update=devicesize</code>, <code>&#8211;update=bbl</code>, or <code>&#8211;update=no-bbl</code>. See the description of these option when used in Assemble mode for an explanation of their use. </p>
<p> If the device name given is <code>missing</code> then <i>mdadm</i> will try to find any device that looks like it should be part of the array but isn&#8217;t and will try to re-add all such devices. </p>
<p> If the device name given is <code>faulty</code> then <i>mdadm</i> will find all devices in the array that are marked <code>faulty</code>, remove them and attempt to immediately re-add them. This can be useful if you are certain that the reason for failure has been resolved. </p>
<dt><code>&#8211;add-spare</code></p>
<dd>Add a device as a spare. This is similar to <code>&#8211;add</code> except that it does not attempt <code>&#8211;re-add</code> first. The device will be added as a spare even if it looks like it could be an recent member of the array. </p>
<dt><code>-r</code>, <code>&#8211;remove</code></p>
<dd>remove listed devices. They must not be active. i.e. they should be failed or spare devices. </p>
<p> As well as the name of a device file (e.g. <code>/dev/sda1</code>) the words <code>failed</code>, <code>detached</code> and names like <code>set-A</code> can be given to <code>&#8211;remove</code>. The first causes all failed device to be removed. The second causes any device which is no longer connected to the system (i.e an &#8216;open&#8217; returns <code>ENXIO</code>) to be removed. The third will remove a set as describe below under <code>&#8211;fail</code>. </p>
<dt><code>-f</code>, <code>&#8211;fail</code></p>
<dd>Mark listed devices as faulty. As well as the name of a device file, the word <code>detached</code> or a set name like <code>set-A</code> can be given. The former will cause any device that has been detached from the system to be marked as failed. It can then be removed. </p>
<p> For RAID10 arrays where the number of copies evenly divides the number of devices, the devices can be conceptually divided into sets where each set contains a single complete copy of the data on the array. Sometimes a RAID10 array will be configured so that these sets are on separate controllers. In this case all the devices in one set can be failed by giving a name like <code>set-A</code> or <code>set-B</code> to <code>&#8211;fail</code>. The appropriate set names are reported by <code>&#8211;detail</code>. </p>
<dt><code>&#8211;set-faulty</code></p>
<dd>same as <code>&#8211;fail</code>. </p>
<dt><code>&#8211;replace</code></p>
<dd>Mark listed devices as requiring replacement. As soon as a spare is available, it will be rebuilt and will replace the marked device. This is similar to marking a device as faulty, but the device remains in service during the recovery process to increase resilience against multiple failures. When the replacement process finishes, the replaced device will be marked as faulty. </p>
<dt><code>&#8211;with</code></p>
<dd>This can follow a list of <code>&#8211;replace</code> devices. The devices listed after <code>&#8211;with</code> will be preferentially used to replace the devices listed after <code>&#8211;replace</code>. These device must already be spare devices in the array. </p>
<dt><code>&#8211;write-mostly</code></p>
<dd>Subsequent devices that are added or re-added will have the &#8216;write-mostly&#8217; flag set. This is only valid for RAID1 and means that the &#8216;md&#8217; driver will avoid reading from these devices if possible.</p>
<dt><code>&#8211;readwrite</code></p>
<dd>Subsequent devices that are added or re-added will have the &#8216;write-mostly&#8217; flag cleared.</p>
<dt><code>&#8211;cluster-confirm</code></p>
<dd>Confirm the existence of the device. This is issued in response to an &#8211;add request by a node in a cluster. When a node adds a device it sends a message to all nodes in the cluster to look for a device with a UUID. This translates to a udev notification with the UUID of the device to be added and the slot number. The receiving node must acknowledge this message with &#8211;cluster-confirm. Valid arguments are &lt;slot&gt;:&lt;devicename&gt; in case the device is found or &lt;slot&gt;:missing in case the device is not found. </p>
<dt><code>&#8211;add-journal</code></p>
<dd>Add journal to an existing array, or recreate journal for RAID-4/5/6 array that lost a journal device. To avoid interrupting on-going write opertions, <code>&#8211;add-journal</code> only works for array in Read-Only state. </p>
<dt><code>&#8211;failfast</code></p>
<dd>Subsequent devices that are added or re-added will have the &#8216;failfast&#8217; flag set. This is only valid for RAID1 and RAID10 and means that the &#8216;md&#8217; driver will avoid long timeouts on error handling where possible.</p>
<dt><code>&#8211;nofailfast</code></p>
<dd>Subsequent devices that are re-added will be re-added without the &#8216;failfast&#8217; flag set. </p>
</dl>
<p> Each of these options requires that the first device listed is the array to be acted upon, and the remainder are component devices to be added, removed, marked as faulty, etc. Several different operations can be specified for different devices, e.g. mdadm /dev/md0 &#8211;add /dev/sda1 &#8211;fail /dev/sdb1 &#8211;remove /dev/sdb1 Each operation applies to all devices listed until the next operation. </p>
<p> If an array is using a write-intent bitmap, then devices which have been removed can be re-added in a way that avoids a full reconstruction but instead just updates the blocks that have changed since the device was removed. For arrays with persistent metadata (superblocks) this is done automatically. For arrays created with <code>&#8211;build</code> mdadm needs to be told that this device we removed recently with <code>&#8211;re-add</code>. </p>
<p> Devices can only be removed from an array if they are not in active use, i.e. that must be spares or failed devices. To remove an active device, it must first be marked as <code>faulty.</code></p>
<h2>For Misc mode:</h2>
<dl>
<dt><code>-Q</code>, <code>&#8211;query</code></p>
<dd>Examine a device to see (1) if it is an md device and (2) if it is a component of an md array. Information about what is discovered is presented. </p>
<dt><code>-D</code>, <code>&#8211;detail</code></p>
<dd>Print details of one or more md devices. </p>
<dt><code>&#8211;detail-platform</code></p>
<dd>Print details of the platform&#8217;s RAID capabilities (firmware / hardware topology) for a given metadata format. If used without argument, mdadm will scan all controllers looking for their capabilities. Otherwise, mdadm will only look at the controller specified by the argument in form of an absolute filepath or a link, e.g. <i>/sys/devices/pci0000:00/0000:00:1f.2</i>. </p>
<dt><code>-Y</code>, <code>&#8211;export</code></p>
<dd>When used with <code>&#8211;detail</code>, <code>&#8211;detail-platform</code>, <code>&#8211;examine</code>, or <code>&#8211;incremental</code> output will be formatted as <code>key=value</code> pairs for easy import into the environment. </p>
<p> With <code>&#8211;incremental</code> The value <code>MD_STARTED</code> indicates whether an array was started (<code>yes</code>) or not, which may include a reason (<code>unsafe</code>, <code>nothing</code>, <code>no</code>). Also the value <code>MD_FOREIGN</code> indicates if the array is expected on this host (<code>no</code>), or seems to be from elsewhere (<code>yes</code>). </p>
<dt><code>-E</code>, <code>&#8211;examine</code></p>
<dd>Print contents of the metadata stored on the named device(s). Note the contrast between <code>&#8211;examine</code> and <code>&#8211;detail</code>. <code>&#8211;examine</code> applies to devices which are components of an array, while <code>&#8211;detail</code> applies to a whole array which is currently active.</p>
<dt><code>&#8211;sparc2.2</code></p>
<dd>If an array was created on a SPARC machine with a 2.2 Linux kernel patched with RAID support, the superblock will have been created incorrectly, or at least incompatibly with 2.4 and later kernels. Using the <code>&#8211;sparc2.2</code> flag with <code>&#8211;examine</code> will fix the superblock before displaying it. If this appears to do the right thing, then the array can be successfully assembled using <code>&#8211;assemble &#8211;update=sparc2.2</code>. </p>
<dt><code>-X</code>, <code>&#8211;examine-bitmap</code></p>
<dd>Report information about a bitmap file. The argument is either an external bitmap file or an array component in case of an internal bitmap. Note that running this on an array device (e.g. <code>/dev/md0</code>) does not report the bitmap for that array. </p>
<dt><code>&#8211;examine-badblocks</code></p>
<dd>List the bad-blocks recorded for the device, if a bad-blocks list has been configured. Currently only <code>1.x</code> metadata supports bad-blocks lists. </p>
<dt><code>&#8211;dump=</code><i>directory</i></p>
<dd>
<dt><code>&#8211;restore=</code><i>directory</i></p>
<dd>Save metadata from lists devices, or restore metadata to listed devices. </p>
<dt><code>-R</code>, <code>&#8211;run</code></p>
<dd>start a partially assembled array. If <code>&#8211;assemble</code> did not find enough devices to fully start the array, it might leaving it partially assembled. If you wish, you can then use <code>&#8211;run</code> to start the array in degraded mode. </p>
<dt><code>-S</code>, <code>&#8211;stop</code></p>
<dd>deactivate array, releasing all resources. </p>
<dt><code>-o</code>, <code>&#8211;readonly</code></p>
<dd>mark array as readonly. </p>
<dt><code>-w</code>, <code>&#8211;readwrite</code></p>
<dd>mark array as readwrite. </p>
<dt><code>&#8211;zero-superblock</code></p>
<dd>If the device contains a valid md superblock, the block is overwritten with zeros. With <code>&#8211;force</code> the block where the superblock would be is overwritten even if it doesn&#8217;t appear to be valid. </p>
<p> <code>Note:</code> Be careful to call &#8211;zero-superblock with clustered raid, make sure array isn&#8217;t used or assembled in other cluster node before execute it. </p>
<dt><code>&#8211;kill-subarray=</code></p>
<dd>If the device is a container and the argument to &#8211;kill-subarray specifies an inactive subarray in the container, then the subarray is deleted. Deleting all subarrays will leave an &#8217;empty-container&#8217; or spare superblock on the drives. See <code>&#8211;zero-superblock</code> for completely removing a superblock. Note that some formats depend on the subarray index for generating a UUID, this command will fail if it would change the UUID of an active subarray. </p>
<dt><code>&#8211;update-subarray=</code></p>
<dd>If the device is a container and the argument to &#8211;update-subarray specifies a subarray in the container, then attempt to update the given superblock field in the subarray. See below in <code>MISC MODE</code> for details. </p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd>When used with <code>&#8211;detail</code>, the exit status of <i>mdadm</i> is set to reflect the status of the device. See below in <code>MISC MODE</code> for details. </p>
<dt><code>-W</code>, <code>&#8211;wait</code></p>
<dd>For each md device given, wait for any resync, recovery, or reshape activity to finish before returning. <i>mdadm</i> will return with success if it actually waited for every device listed, otherwise it will return failure. </p>
<dt><code>&#8211;wait-clean</code></p>
<dd>For each md device given, or each device in /proc/mdstat if <code>&#8211;scan</code> is given, arrange for the array to be marked clean as soon as possible. <i>mdadm</i> will return with success if the array uses external metadata and we successfully waited. For native arrays this returns immediately as the kernel handles dirty-clean transitions at shutdown. No action is taken if safe-mode handling is disabled. </p>
<dt><code>&#8211;action=</code></p>
<dd>Set the &quot;sync_action&quot; for all md devices given to one of <code>idle</code>, <code>frozen</code>, <code>check</code>, <code>repair</code>. Setting to <code>idle</code> will abort any currently running action though some actions will automatically restart. Setting to <code>frozen</code> will abort any current action and ensure no other action starts automatically. </p>
<p> Details of <code>check</code> and <code>repair</code> can be found it <i><a href="/docs/linux/man/4-md/">md</a></i>(4) under <code>SCRUBBING AND MISMATCHES</code>. </p>
</dl>
<h2>For Incremental Assembly mode:</h2>
<dl>
<dt><code>&#8211;rebuild-map</code>, <code>-r</code></p>
<dd>Rebuild the map file (<code>/run/mdadm/map</code>) that <i>mdadm</i> uses to help track which arrays are currently being assembled. </p>
<dt><code>&#8211;run</code>, <code>-R</code></p>
<dd>Run any array assembled as soon as a minimal number of devices are available, rather than waiting until all expected devices are present. </p>
<dt><code>&#8211;scan</code>, <code>-s</code></p>
<dd>Only meaningful with <code>-R</code> this will scan the <code>map</code> file for arrays that are being incrementally assembled and will try to start any that are not already started. If any such array is listed in <code>mdadm.conf</code> as requiring an external bitmap, that bitmap will be attached first. </p>
<dt><code>&#8211;fail</code>, <code>-f</code></p>
<dd>This allows the hot-plug system to remove devices that have fully disappeared from the kernel. It will first fail and then remove the device from any array it belongs to. The device name given should be a kernel device name such as &quot;sda&quot;, not a name in <i>/dev</i>. </p>
<dt><code>&#8211;path=</code></p>
<dd>Only used with &#8211;fail. The &#8216;path&#8217; given will be recorded so that if a new device appears at the same location it can be automatically added to the same array. This allows the failed device to be automatically replaced by a new device without metadata if it appears at specified path. This option is normally only set by a <i>udev</i> script. </p>
</dl>
<h2>For Monitor mode:</h2>
<dl>
<dt><code>-m</code>, <code>&#8211;mail</code></p>
<dd>Give a mail address to send alerts to. </p>
<dt><code>-p</code>, <code>&#8211;program</code>, <code>&#8211;alert</code></p>
<dd>Give a program to be run whenever an event is detected. </p>
<dt><code>-y</code>, <code>&#8211;syslog</code></p>
<dd>Cause all events to be reported through &#8216;syslog&#8217;. The messages have facility of &#8216;daemon&#8217; and varying priorities. </p>
<dt><code>-d</code>, <code>&#8211;delay</code></p>
<dd>Give a delay in seconds. <i>mdadm</i> polls the md arrays and then waits this many seconds before polling again. The default is 60 seconds. Since 2.6.16, there is no need to reduce this as the kernel alerts <i>mdadm</i> immediately when there is any change. </p>
<dt><code>-r</code>, <code>&#8211;increment</code></p>
<dd>Give a percentage increment. <i>mdadm</i> will generate RebuildNN events with the given percentage increment. </p>
<dt><code>-f</code>, <code>&#8211;daemonise</code></p>
<dd>Tell <i>mdadm</i> to run as a background daemon if it decides to monitor anything. This causes it to fork and run in the child, and to disconnect from the terminal. The process id of the child is written to stdout. This is useful with <code>&#8211;scan</code> which will only continue monitoring if a mail address or alert program is found in the config file. </p>
<dt><code>-i</code>, <code>&#8211;pid-file</code></p>
<dd>When <i>mdadm</i> is running in daemon mode, write the pid of the daemon process to the specified file, instead of printing it on standard output. </p>
<dt><code>-1</code>, <code>&#8211;oneshot</code></p>
<dd>Check arrays only once. This will generate <code>NewArray</code> events and more significantly <code>DegradedArray</code> and <code>SparesMissing</code> events. Running <code> mdadm &#8211;monitor &#8211;scan -1</code> from a cron script will ensure regular notification of any degraded arrays. </p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd>Generate a <code>TestMessage</code> alert for every array found at startup. This alert gets mailed and passed to the alert program. This can be used for testing that alert message do get through successfully. </p>
<dt><code>&#8211;no-sharing</code></p>
<dd>This inhibits the functionality for moving spares between arrays. Only one monitoring process started with <code>&#8211;scan</code> but without this flag is allowed, otherwise the two could interfere with each other. </p>
</dl>
<h2>Assemble Mode</h2>
<dl>
<dd>Usage: <code>mdadm &#8211;assemble</code> <i>md-device options-and-component-devices&#8230;</i></p>
<dd>Usage: <code>mdadm &#8211;assemble &#8211;scan</code> <i>md-devices-and-options&#8230;</i></p>
<dd>Usage: <code>mdadm &#8211;assemble &#8211;scan</code> <i>options&#8230;</i> </p>
</dl>
<p> This usage assembles one or more RAID arrays from pre-existing components. For each array, mdadm needs to know the md device, the identity of the array, and a number of component-devices. These can be found in a number of ways. </p>
<p> In the first usage example (without the <code>&#8211;scan</code>) the first device given is the md device. In the second usage example, all devices listed are treated as md devices and assembly is attempted. In the third (where no devices are listed) all md devices that are listed in the configuration file are assembled. If no arrays are described by the configuration file, then any arrays that can be found on unused devices will be assembled. </p>
<p> If precisely one device is listed, but <code>&#8211;scan</code> is not given, then <i>mdadm</i> acts as though <code>&#8211;scan</code> was given and identity information is extracted from the configuration file. </p>
<p> The identity can be given with the <code>&#8211;uuid</code> option, the <code>&#8211;name</code> option, or the <code>&#8211;super-minor</code> option, will be taken from the md-device record in the config file, or will be taken from the super block of the first component-device listed on the command line. </p>
<p> Devices can be given on the <code>&#8211;assemble</code> command line or in the config file. Only devices which have an md superblock which contains the right identity will be considered for any array. </p>
<p> The config file is only used if explicitly named with <code>&#8211;config</code> or requested with (a possibly implicit) <code>&#8211;scan</code>. In the later case, <code>/etc/mdadm/mdadm.conf</code> or <code>/etc/mdadm.conf</code> is used. </p>
<p> If <code>&#8211;scan</code> is not given, then the config file will only be used to find the identity of md arrays. </p>
<p> Normally the array will be started after it is assembled. However if <code>&#8211;scan</code> is not given and not all expected drives were listed, then the array is not started (to guard against usage errors). To insist that the array be started in this case (as may work for RAID1, 4, 5, 6, or 10), give the <code>&#8211;run</code> flag. </p>
<p> If <i>udev</i> is active, <i>mdadm</i> does not create any entries in <code>/dev</code> but leaves that to <i>udev</i>. It does record information in <code>/run/mdadm/map</code> which will allow <i>udev</i> to choose the correct name. </p>
<p> If <i>mdadm</i> detects that udev is not configured, it will create the devices in <code>/dev</code> itself. </p>
<p> In Linux kernels prior to version 2.6.28 there were two distinctly different types of md devices that could be created: one that could be partitioned using standard partitioning tools and one that could not. Since 2.6.28 that distinction is no longer relevant as both type of devices can be partitioned. <i>mdadm</i> will normally create the type that originally could not be partitioned as it has a well defined major number (9). </p>
<p> Prior to 2.6.28, it is important that mdadm chooses the correct type of array device to use. This can be controlled with the <code>&#8211;auto</code> option. In particular, a value of &quot;mdp&quot; or &quot;part&quot; or &quot;p&quot; tells mdadm to use a partitionable device rather than the default. </p>
<p> In the no-udev case, the value given to <code>&#8211;auto</code> can be suffixed by a number. This tells <i>mdadm</i> to create that number of partition devices rather than the default of 4. </p>
<p> The value given to <code>&#8211;auto</code> can also be given in the configuration file as a word starting <code>auto=</code> on the ARRAY line for the relevant array.</p>
<h3>Auto Assembly</h3>
<p>When <code>&#8211;assemble</code> is used with <code>&#8211;scan</code> and no devices are listed, <i>mdadm</i> will first attempt to assemble all the arrays listed in the config file. </p>
<p> If no arrays are listed in the config (other than those marked <code>&lt;ignore&gt;</code>) it will look through the available devices for possible arrays and will try to assemble anything that it finds. Arrays which are tagged as belonging to the given homehost will be assembled and started normally. Arrays which do not obviously belong to this host are given names that are expected not to conflict with anything local, and are started &quot;read-auto&quot; so that nothing is written to any device until the array is written to. i.e. automatic resync etc is delayed. </p>
<p> If <i>mdadm</i> finds a consistent set of devices that look like they should comprise an array, and if the superblock is tagged as belonging to the given home host, it will automatically choose a device name and try to assemble the array. If the array uses version-0.90 metadata, then the <code>minor</code> number as recorded in the superblock is used to create a name in <code>/dev/md/</code> so for example <code>/dev/md/3</code>. If the array uses version-1 metadata, then the <code>name</code> from the superblock is used to similarly create a name in <code>/dev/md/</code> (the name will have any &#8216;host&#8217; prefix stripped first). </p>
<p> This behaviour can be modified by the <i>AUTO</i> line in the <i>mdadm.conf</i> configuration file. This line can indicate that specific metadata type should, or should not, be automatically assembled. If an array is found which is not listed in <i>mdadm.conf</i> and has a metadata format that is denied by the <i>AUTO</i> line, then it will not be assembled. The <i>AUTO</i> line can also request that all arrays identified as being for this homehost should be assembled regardless of their metadata type. See <i><a href="/docs/linux/man/5-mdadm-conf/">mdadm.conf</a></i>(5) for further details. </p>
<p> Note: Auto assembly cannot be used for assembling and activating some arrays which are undergoing reshape. In particular as the <code>backup-file</code> cannot be given, any reshape which requires a backup-file to continue cannot be started by auto assembly. An array which is growing to more devices and has passed the critical section can be assembled using auto-assembly.</p>
<h2>Build Mode</h2>
<dl>
<dd>Usage: <code>mdadm &#8211;build</code> <i>md-device</i> <code>&#8211;chunk=</code><i>X</i> <code>&#8211;level=</code><i>Y</i> <code>&#8211;raid-devices=</code><i>Z</i> <i>devices</i> </p>
</dl>
<p> This usage is similar to <code>&#8211;create</code>. The difference is that it creates an array without a superblock. With these arrays there is no difference between initially creating the array and subsequently assembling the array, except that hopefully there is useful data there in the second case. </p>
<p> The level may raid0, linear, raid1, raid10, multipath, or faulty, or one of their synonyms. All devices must be listed and the array will be started once complete. It will often be appropriate to use <code>&#8211;assume-clean</code> with levels raid1 or raid10.</p>
<h2>Create Mode</h2>
<dl>
<dd>Usage: <code>mdadm &#8211;create</code> <i>md-device</i> <code>&#8211;chunk=</code><i>X</i> <code>&#8211;level=</code><i>Y</i><br />
 <code>&#8211;raid-devices=</code><i>Z</i> <i>devices</i> </p>
</dl>
<p> This usage will initialise a new md array, associate some devices with it, and activate the array. </p>
<p> The named device will normally not exist when <i>mdadm &#8211;create</i> is run, but will be created by <i>udev</i> once the array becomes active. </p>
<p> As devices are added, they are checked to see if they contain RAID superblocks or filesystems. They are also checked to see if the variance in device size exceeds 1%. </p>
<p> If any discrepancy is found, the array will not automatically be run, though the presence of a <code>&#8211;run</code> can override this caution. </p>
<p> To create a &quot;degraded&quot; array in which some devices are missing, simply give the word &quot;<code>missing</code>&quot; in place of a device name. This will cause <i>mdadm</i> to leave the corresponding slot in the array empty. For a RAID4 or RAID5 array at most one slot can be &quot;<code>missing</code>&quot;; for a RAID6 array at most two slots. For a RAID1 array, only one real device needs to be given. All of the others can be &quot;<code>missing</code>&quot;. </p>
<p> When creating a RAID5 array, <i>mdadm</i> will automatically create a degraded array with an extra spare drive. This is because building the spare into a degraded array is in general faster than resyncing the parity on a non-degraded, but not clean, array. This feature can be overridden with the <code>&#8211;force</code> option. </p>
<p> When creating an array with version-1 metadata a name for the array is required. If this is not given with the <code>&#8211;name</code> option, <i>mdadm</i> will choose a name based on the last component of the name of the device being created. So if <code>/dev/md3</code> is being created, then the name <code>3</code> will be chosen. If <code>/dev/md/home</code> is being created, then the name <code>home</code> will be used. </p>
<p> When creating a partition based array, using <i>mdadm</i> with version-1.x metadata, the partition type should be set to <code>0xDA</code> (non fs-data). This type selection allows for greater precision since using any other [RAID auto-detect (0xFD) or a GNU/Linux partition (0x83)], might create problems in the event of array recovery through a live cdrom. </p>
<p> A new array will normally get a randomly assigned 128bit UUID which is very likely to be unique. If you have a specific need, you can choose a UUID for the array by giving the <code>&#8211;uuid=</code> option. Be warned that creating two arrays with the same UUID is a recipe for disaster. Also, using <code>&#8211;uuid=</code> when creating a v0.90 array will silently override any <code>&#8211;homehost=</code> setting. </p>
<p> If the array type supports a write-intent bitmap, and if the devices in the array exceed 100G is size, an internal write-intent bitmap will automatically be added unless some other option is explicitly requested with the <code>&#8211;bitmap</code> option or a different consistency policy is selected with the <code>&#8211;consistency-policy</code> option. In any case space for a bitmap will be reserved so that one can be added later with <code>&#8211;grow &#8211;bitmap=internal</code>. </p>
<p> If the metadata type supports it (currently only 1.x and IMSM metadata), space will be allocated to store a bad block list. This allows a modest number of bad blocks to be recorded, allowing the drive to remain in service while only partially functional. </p>
<p> When creating an array within a <code>CONTAINER</code> <i>mdadm</i> can be given either the list of devices to use, or simply the name of the container. The former case gives control over which devices in the container will be used for the array. The latter case allows <i>mdadm</i> to automatically choose which devices to use based on how much spare space is available. </p>
<p> The General Management options that are valid with <code>&#8211;create</code> are:</p>
<dl>
<dt><code>&#8211;run</code></p>
<dd>insist on running the array even if some devices look like they might be in use. </p>
<dt><code>&#8211;readonly</code></p>
<dd>start the array in readonly mode. </p>
</dl>
<h2>Manage Mode</h2>
<dl>
<dd>Usage: <code>mdadm</code> <i>device</i> <i>options&#8230; devices&#8230;</i></dl>
<p> This usage will allow individual devices in an array to be failed, removed or added. It is possible to perform multiple operations with on command. For example:<br />
 <code> mdadm /dev/md0 -f /dev/hda1 -r /dev/hda1 -a /dev/hda1</code><br />
 will firstly mark <code>/dev/hda1</code> as faulty in <code>/dev/md0</code> and will then remove it from the array and finally add it back in as a spare. However only one md array can be affected by a single command. </p>
<p> When a device is added to an active array, mdadm checks to see if it has metadata on it which suggests that it was recently a member of the array. If it does, it tries to &quot;re-add&quot; the device. If there have been no changes since the device was removed, or if the array has a write-intent bitmap which has recorded whatever changes there were, then the device will immediately become a full member of the array and those differences recorded in the bitmap will be resolved.</p>
<h2>Misc Mode</h2>
<dl>
<dd>Usage: <code>mdadm</code> <i>options &#8230;</i> <i>devices &#8230;</i></dl>
<p> MISC mode includes a number of distinct operations that operate on distinct devices. The operations are:</p>
<dl>
<dt><code>&#8211;query</code></p>
<dd>The device is examined to see if it is (1) an active md array, or (2) a component of an md array. The information discovered is reported. </p>
<dt><code>&#8211;detail</code></p>
<dd>The device should be an active md device. <code>mdadm</code> will display a detailed description of the array. <code>&#8211;brief</code> or <code>&#8211;scan</code> will cause the output to be less detailed and the format to be suitable for inclusion in <code>mdadm.conf</code>. The exit status of <i>mdadm</i> will normally be 0 unless <i>mdadm</i> failed to get useful information about the device(s); however, if the <code>&#8211;test</code> option is given, then the exit status will be:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>The array is functioning normally.</p>
<dt>1</p>
<dd>The array has at least one failed device.</p>
<dt>2</p>
<dd>The array has multiple failed devices such that it is unusable.</p>
<dt>4</p>
<dd>There was an error while trying to get information about the device.</dl>
</dl>
<dt><code>&#8211;detail-platform</code></p>
<dd>Print detail of the platform&#8217;s RAID capabilities (firmware / hardware topology). If the metadata is specified with <code>-e</code> or <code>&#8211;metadata=</code> then the return status will be:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>metadata successfully enumerated its platform components on this system</p>
<dt>1</p>
<dd>metadata is platform independent</p>
<dt>2</p>
<dd>metadata failed to find its platform components on this system</dl>
</dl>
<dt><code>&#8211;update-subarray=</code></p>
<dd>If the device is a container and the argument to &#8211;update-subarray specifies a subarray in the container, then attempt to update the given superblock field in the subarray. Similar to updating an array in &quot;assemble&quot; mode, the field to update is selected by <code>-U</code> or <code>&#8211;update=</code> option. The supported options are <code>name</code>, <code>ppl</code> and <code>no-ppl</code>. </p>
<p> The <code>name</code> option updates the subarray name in the metadata, it may not affect the device node name or the device node symlink until the subarray is re-assembled. If updating <code>name</code> would change the UUID of an active subarray this operation is blocked, and the command will end in an error. </p>
<p> The <code>ppl</code> and <code>no-ppl</code> options enable and disable PPL in the metadata. Currently supported only for IMSM subarrays. </p>
<dt><code>&#8211;examine</code></p>
<dd>The device should be a component of an md array. <i>mdadm</i> will read the md superblock of the device and display the contents. If <code>&#8211;brief</code> or <code>&#8211;scan</code> is given, then multiple devices that are components of the one array are grouped together and reported in a single entry suitable for inclusion in <code>mdadm.conf</code>. </p>
<p> Having <code>&#8211;scan</code> without listing any devices will cause all devices listed in the config file to be examined. </p>
<dt><code>&#8211;dump=</code><i>directory</i></p>
<dd>If the device contains RAID metadata, a file will be created in the <i>directory</i> and the metadata will be written to it. The file will be the same size as the device and have the metadata written in the file at the same locate that it exists in the device. However the file will be &quot;sparse&quot; so that only those blocks containing metadata will be allocated. The total space used will be small. </p>
<p> The file name used in the <i>directory</i> will be the base name of the device. Further if any links appear in <i>/dev/disk/by-id</i> which point to the device, then hard links to the file will be created in <i>directory</i> based on these <i>by-id</i> names. </p>
<p> Multiple devices can be listed and their metadata will all be stored in the one directory. </p>
<dt><code>&#8211;restore=</code><i>directory</i></p>
<dd>This is the reverse of <code>&#8211;dump</code>. <i>mdadm</i> will locate a file in the directory that has a name appropriate for the given device and will restore metadata from it. Names that match <i>/dev/disk/by-id</i> names are preferred, however if two of those refer to different files, <i>mdadm</i> will not choose between them but will abort the operation. </p>
<p> If a file name is given instead of a <i>directory</i> then <i>mdadm</i> will restore from that file to a single device, always provided the size of the file matches that of the device, and the file contains valid metadata.</p>
<dt><code>&#8211;stop</code></p>
<dd>The devices should be active md arrays which will be deactivated, as long as they are not currently in use. </p>
<dt><code>&#8211;run</code></p>
<dd>This will fully activate a partially assembled md array. </p>
<dt><code>&#8211;readonly</code></p>
<dd>This will mark an active array as read-only, providing that it is not currently being used. </p>
<dt><code>&#8211;readwrite</code></p>
<dd>This will change a <code>readonly</code> array back to being read/write. </p>
<dt><code>&#8211;scan</code></p>
<dd>For all operations except <code>&#8211;examine</code>, <code>&#8211;scan</code> will cause the operation to be applied to all arrays listed in <code>/proc/mdstat</code>. For <code>&#8211;examine,</code> <code>&#8211;scan</code> causes all devices listed in the config file to be examined. </p>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>Be less verbose. This is used with <code>&#8211;detail</code> and <code>&#8211;examine</code>. Using <code>&#8211;brief</code> with <code>&#8211;verbose</code> gives an intermediate level of verbosity. </p>
</dl>
<h2>Monitor Mode</h2>
<dl>
<dd>Usage: <code>mdadm &#8211;monitor</code> <i>options&#8230; devices&#8230;</i> </p>
</dl>
<p> This usage causes <i>mdadm</i> to periodically poll a number of md arrays and to report on any events noticed. <i>mdadm</i> will never exit once it decides that there are arrays to be checked, so it should normally be run in the background. </p>
<p> As well as reporting events, <i>mdadm</i> may move a spare drive from one array to another if they are in the same <code>spare-group</code> or <code>domain</code> and if the destination array has a failed drive but no spares. </p>
<p> If any devices are listed on the command line, <i>mdadm</i> will only monitor those devices. Otherwise all arrays listed in the configuration file will be monitored. Further, if <code>&#8211;scan</code> is given, then any other md devices that appear in <code>/proc/mdstat</code> will also be monitored. </p>
<p> The result of monitoring the arrays is the generation of events. These events are passed to a separate program (if specified) and may be mailed to a given E-mail address. </p>
<p> When passing events to a program, the program is run once for each event, and is given 2 or 3 command-line arguments: the first is the name of the event (see below), the second is the name of the md device which is affected, and the third is the name of a related device if relevant (such as a component device that has failed). </p>
<p> If <code>&#8211;scan</code> is given, then a program or an E-mail address must be specified on the command line or in the config file. If neither are available, then <i>mdadm</i> will not monitor anything. Without <code>&#8211;scan,</code> <i>mdadm</i> will continue monitoring as long as something was found to monitor. If no program or email is given, then each event is reported to <code>stdout</code>. </p>
<p> The different events are: </p>
<dl>
<dd>
<dl>
<dt><code>DeviceDisappeared</code></p>
<dd>An md array which previously was configured appears to no longer be configured. (syslog priority: Critical) </p>
<p> If <i>mdadm</i> was told to monitor an array which is RAID0 or Linear, then it will report <code>DeviceDisappeared</code> with the extra information <code>Wrong-Level</code>. This is because RAID0 and Linear do not support the device-failed, hot-spare and resync operations which are monitored. </p>
<dt><code>RebuildStarted</code></p>
<dd>An md array started reconstruction (e.g. recovery, resync, reshape, check, repair). (syslog priority: Warning) </p>
<dt><code>Rebuild</code><i>NN</i></p>
<dd>Where <i>NN</i> is a two-digit number (ie. 05, 48). This indicates that rebuild has passed that many percent of the total. The events are generated with fixed increment since 0. Increment size may be specified with a commandline option (default is 20). (syslog priority: Warning) </p>
<dt><code>RebuildFinished</code></p>
<dd>An md array that was rebuilding, isn&#8217;t any more, either because it finished normally or was aborted. (syslog priority: Warning) </p>
<dt><code>Fail</code></p>
<dd>An active component device of an array has been marked as faulty. (syslog priority: Critical) </p>
<dt><code>FailSpare</code></p>
<dd>A spare component device which was being rebuilt to replace a faulty device has failed. (syslog priority: Critical) </p>
<dt><code>SpareActive</code></p>
<dd>A spare component device which was being rebuilt to replace a faulty device has been successfully rebuilt and has been made active. (syslog priority: Info) </p>
<dt><code>NewArray</code></p>
<dd>A new md array has been detected in the <code>/proc/mdstat</code> file. (syslog priority: Info) </p>
<dt><code>DegradedArray</code></p>
<dd>A newly noticed array appears to be degraded. This message is not generated when <i>mdadm</i> notices a drive failure which causes degradation, but only when <i>mdadm</i> notices that an array is degraded when it first sees the array. (syslog priority: Critical) </p>
<dt><code>MoveSpare</code></p>
<dd>A spare drive has been moved from one array in a <code>spare-group</code> or <code>domain</code> to another to allow a failed drive to be replaced. (syslog priority: Info) </p>
<dt><code>SparesMissing</code></p>
<dd>If <i>mdadm</i> has been told, via the config file, that an array should have a certain number of spare devices, and <i>mdadm</i> detects that it has fewer than this number when it first sees the array, it will report a <code>SparesMissing</code> message. (syslog priority: Warning) </p>
<dt><code>TestMessage</code></p>
<dd>An array was found at startup, and the <code>&#8211;test</code> flag was given. (syslog priority: Info)</dl>
</dl>
<p> Only <code>Fail,</code> <code>FailSpare,</code> <code>DegradedArray,</code> <code>SparesMissing</code> and <code>TestMessage</code> cause Email to be sent. All events cause the program to be run. The program is run with two or three arguments: the event name, the array device and possibly a second device. </p>
<p> Each event has an associated array device (e.g. <code>/dev/md1</code>) and possibly a second device. For <code>Fail</code>, <code>FailSpare</code>, and <code>SpareActive</code> the second device is the relevant component device. For <code>MoveSpare</code> the second device is the array that the spare was moved from. </p>
<p> For <i>mdadm</i> to move spares from one array to another, the different arrays need to be labeled with the same <code>spare-group</code> or the spares must be allowed to migrate through matching POLICY domains in the configuration file. The <code>spare-group</code> name can be any string; it is only necessary that different spare groups use different names. </p>
<p> When <i>mdadm</i> detects that an array in a spare group has fewer active devices than necessary for the complete array, and has no spare devices, it will look for another array in the same spare group that has a full complement of working drive and a spare. It will then attempt to remove the spare from the second drive and add it to the first. If the removal succeeds but the adding fails, then it is added back to the original array. </p>
<p> If the spare group for a degraded array is not defined, <i>mdadm</i> will look at the rules of spare migration specified by POLICY lines in <code>mdadm.conf</code> and then follow similar steps as above if a matching spare is found.</p>
<h2>Grow Mode</h2>
<p>The GROW mode is used for changing the size or shape of an active array. For this to work, the kernel must support the necessary change. Various types of growth are being added during 2.6 development. </p>
<p> Currently the supported changes include</p>
<dl>
<dt>&bull;</p>
<dd>change the &quot;size&quot; attribute for RAID1, RAID4, RAID5 and RAID6.</p>
<dt>&bull;</p>
<dd>increase or decrease the &quot;raid-devices&quot; attribute of RAID0, RAID1, RAID4, RAID5, and RAID6.</p>
<dt>&bull;</p>
<dd>change the chunk-size and layout of RAID0, RAID4, RAID5, RAID6 and RAID10.</p>
<dt>&bull;</p>
<dd>convert between RAID1 and RAID5, between RAID5 and RAID6, between RAID0, RAID4, and RAID5, and between RAID0 and RAID10 (in the near-2 mode).</p>
<dt>&bull;</p>
<dd>add a write-intent bitmap to any array which supports these bitmaps, or remove a write-intent bitmap from such an array.</p>
<dt>&bull;</p>
<dd>change the array&#8217;s consistency policy.</dl>
<p> Using GROW on containers is currently supported only for Intel&#8217;s IMSM container format. The number of devices in a container can be increased &#8211; which affects all arrays in the container &#8211; or an array in a container can be converted between levels where those levels are supported by the container, and the conversion is on of those listed above. Resizing arrays in an IMSM container with <code>&#8211;grow &#8211;size</code> is not yet supported. </p>
<p> Notes:</p>
<dl>
<dt>&bull;</p>
<dd>Intel&#8217;s native checkpointing doesn&#8217;t use <code>&#8211;backup-file</code> option and it is transparent for assembly feature.</p>
<dt>&bull;</p>
<dd>Roaming between Windows(R) and Linux systems for IMSM metadata is not supported during grow process. </p>
</dl>
<h3>Size Changes</h3>
<p>Normally when an array is built the &quot;size&quot; is taken from the smallest of the drives. If all the small drives in an arrays are, one at a time, removed and replaced with larger drives, then you could have an array of large drives with only a small amount used. In this situation, changing the &quot;size&quot; with &quot;GROW&quot; mode will allow the extra space to start being used. If the size is increased in this way, a &quot;resync&quot; process will start to make sure the new parts of the array are synchronised. </p>
<p> Note that when an array changes size, any filesystem that may be stored in the array will not automatically grow or shrink to use or vacate the space. The filesystem will need to be explicitly told to use the extra space after growing, or to reduce its size <code>prior</code> to shrinking the array. </p>
<p> Also the size of an array cannot be changed while it has an active bitmap. If an array has a bitmap, it must be removed before the size can be changed. Once the change is complete a new bitmap can be created. </p>
<p> Note: <code>&#8211;grow &#8211;size</code> is not yet supported for external file bitmap.</p>
<h3>Raid-Devices Changes</h3>
<p>A RAID1 array can work with any number of devices from 1 upwards (though 1 is not very useful). There may be times which you want to increase or decrease the number of active devices. Note that this is different to hot-add or hot-remove which changes the number of inactive devices. </p>
<p> When reducing the number of devices in a RAID1 array, the slots which are to be removed from the array must already be vacant. That is, the devices which were in those slots must be failed and removed. </p>
<p> When the number of devices is increased, any hot spares that are present will be activated immediately. </p>
<p> Changing the number of active devices in a RAID5 or RAID6 is much more effort. Every block in the array will need to be read and written back to a new location. From 2.6.17, the Linux Kernel is able to increase the number of devices in a RAID5 safely, including restarting an interrupted &quot;reshape&quot;. From 2.6.31, the Linux Kernel is able to increase or decrease the number of devices in a RAID5 or RAID6. </p>
<p> From 2.6.35, the Linux Kernel is able to convert a RAID0 in to a RAID4 or RAID5. <i>mdadm</i> uses this functionality and the ability to add devices to a RAID4 to allow devices to be added to a RAID0. When requested to do this, <i>mdadm</i> will convert the RAID0 to a RAID4, add the necessary disks and make the reshape happen, and then convert the RAID4 back to RAID0. </p>
<p> When decreasing the number of devices, the size of the array will also decrease. If there was data in the array, it could get destroyed and this is not reversible, so you should firstly shrink the filesystem on the array to fit within the new size. To help prevent accidents, <i>mdadm</i> requires that the size of the array be decreased first with <code>mdadm &#8211;grow &#8211;array-size</code>. This is a reversible change which simply makes the end of the array inaccessible. The integrity of any data can then be checked before the non-reversible reduction in the number of devices is request. </p>
<p> When relocating the first few stripes on a RAID5 or RAID6, it is not possible to keep the data on disk completely consistent and crash-proof. To provide the required safety, mdadm disables writes to the array while this &quot;critical section&quot; is reshaped, and takes a backup of the data that is in that section. For grows, this backup may be stored in any spare devices that the array has, however it can also be stored in a separate file specified with the <code>&#8211;backup-file</code> option, and is required to be specified for shrinks, RAID level changes and layout changes. If this option is used, and the system does crash during the critical period, the same file must be passed to <code>&#8211;assemble</code> to restore the backup and reassemble the array. When shrinking rather than growing the array, the reshape is done from the end towards the beginning, so the &quot;critical section&quot; is at the end of the reshape.</p>
<h3>Level Changes</h3>
<p>Changing the RAID level of any array happens instantaneously. However in the RAID5 to RAID6 case this requires a non-standard layout of the RAID6 data, and in the RAID6 to RAID5 case that non-standard layout is required before the change can be accomplished. So while the level change is instant, the accompanying layout change can take quite a long time. A <code>&#8211;backup-file</code> is required. If the array is not simultaneously being grown or shrunk, so that the array size will remain the same &#8211; for example, reshaping a 3-drive RAID5 into a 4-drive RAID6 &#8211; the backup file will be used not just for a &quot;cricital section&quot; but throughout the reshape operation, as described below under LAYOUT CHANGES.</p>
<h3>Chunk-Size And Layout Changes</h3>
<p>Changing the chunk-size of layout without also changing the number of devices as the same time will involve re-writing all blocks in-place. To ensure against data loss in the case of a crash, a <code>&#8211;backup-file</code> must be provided for these changes. Small sections of the array will be copied to the backup file while they are being rearranged. This means that all the data is copied twice, once to the backup and once to the new layout on the array, so this type of reshape will go very slowly. </p>
<p> If the reshape is interrupted for any reason, this backup file must be made available to <code>mdadm &#8211;assemble</code> so the array can be reassembled. Consequently the file cannot be stored on the device being reshaped.</p>
<h3>Bitmap Changes</h3>
<p>A write-intent bitmap can be added to, or removed from, an active array. Either internal bitmaps, or bitmaps stored in a separate file, can be added. Note that if you add a bitmap stored in a file which is in a filesystem that is on the RAID array being affected, the system will deadlock. The bitmap must be on a separate filesystem.</p>
<h3>Consistency Policy Changes</h3>
<p>The consistency policy of an active array can be changed by using the <code>&#8211;consistency-policy</code> option in Grow mode. Currently this works only for the <code>ppl</code> and <code>resync</code> policies and allows to enable or disable the RAID5 Partial Parity Log (PPL).</p>
<h2>Incremental Mode</h2>
<dl>
<dd>Usage: <code>mdadm &#8211;incremental</code> [<code>&#8211;run</code>] [<code>&#8211;quiet</code>] <i>component-device</i> [<i>optional-aliases-for-device</i>]</p>
<dd>Usage: <code>mdadm &#8211;incremental &#8211;fail</code> <i>component-device</i></p>
<dd>Usage: <code>mdadm &#8211;incremental &#8211;rebuild-map</code></p>
<dd>Usage: <code>mdadm &#8211;incremental &#8211;run &#8211;scan</code> </p>
</dl>
<p> This mode is designed to be used in conjunction with a device discovery system. As devices are found in a system, they can be passed to <code>mdadm &#8211;incremental</code> to be conditionally added to an appropriate array. </p>
<p> Conversely, it can also be used with the <code>&#8211;fail</code> flag to do just the opposite and find whatever array a particular device is part of and remove the device from that array. </p>
<p> If the device passed is a <code>CONTAINER</code> device created by a previous call to <i>mdadm</i>, then rather than trying to add that device to an array, all the arrays described by the metadata of the container will be started. </p>
<p> <i>mdadm</i> performs a number of tests to determine if the device is part of an array, and which array it should be part of. If an appropriate array is found, or can be created, <i>mdadm</i> adds the device to the array and conditionally starts the array. </p>
<p> Note that <i>mdadm</i> will normally only add devices to an array which were previously working (active or spare) parts of that array. The support for automatic inclusion of a new drive as a spare in some array requires a configuration through POLICY in config file. </p>
<p> The tests that <i>mdadm</i> makes are as follow:</p>
<dl>
<dt>+</p>
<dd>Is the device permitted by <code>mdadm.conf</code>? That is, is it listed in a <code>DEVICES</code> line in that file. If <code>DEVICES</code> is absent then the default it to allow any device. Similarly if <code>DEVICES</code> contains the special word <code>partitions</code> then any device is allowed. Otherwise the device name given to <i>mdadm</i>, or one of the aliases given, or an alias found in the filesystem, must match one of the names or patterns in a <code>DEVICES</code> line. </p>
<p> This is the only context where the aliases are used. They are usually provided by a <i>udev</i> rules mentioning <code>$env{DEVLINKS}</code>. </p>
<dt>+</p>
<dd>Does the device have a valid md superblock? If a specific metadata version is requested with <code>&#8211;metadata</code> or <code>-e</code> then only that style of metadata is accepted, otherwise <i>mdadm</i> finds any known version of metadata. If no <i>md</i> metadata is found, the device may be still added to an array as a spare if POLICY allows. </p>
</dl>
<p> <i>mdadm</i> keeps a list of arrays that it has partially assembled in <code>/run/mdadm/map</code>. If no array exists which matches the metadata on the new device, <i>mdadm</i> must choose a device name and unit number. It does this based on any name given in <code>mdadm.conf</code> or any name information stored in the metadata. If this name suggests a unit number, that number will be used, otherwise a free unit number will be chosen. Normally <i>mdadm</i> will prefer to create a partitionable array, however if the <code>CREATE</code> line in <code>mdadm.conf</code> suggests that a non-partitionable array is preferred, that will be honoured. </p>
<p> If the array is not found in the config file and its metadata does not identify it as belonging to the &quot;homehost&quot;, then <i>mdadm</i> will choose a name for the array which is certain not to conflict with any array which does belong to this host. It does this be adding an underscore and a small number to the name preferred by the metadata. </p>
<p> Once an appropriate array is found or created and the device is added, <i>mdadm</i> must decide if the array is ready to be started. It will normally compare the number of available (non-spare) devices to the number of devices that the metadata suggests need to be active. If there are at least that many, the array will be started. This means that if any devices are missing the array will not be restarted. </p>
<p> As an alternative, <code>&#8211;run</code> may be passed to <i>mdadm</i> in which case the array will be run as soon as there are enough devices present for the data to be accessible. For a RAID1, that means one device will start the array. For a clean RAID5, the array will be started as soon as all but one drive is present. </p>
<p> Note that neither of these approaches is really ideal. If it can be known that all device discovery has completed, then<br />
 <code> mdadm -IRs</code><br />
 can be run which will try to start all arrays that are being incrementally assembled. They are started in &quot;read-auto&quot; mode in which they are read-only until the first write request. This means that no metadata updates are made and no attempt at resync or recovery happens. Further devices that are found before the first write can still be added safely.</p>
<h2>Environment</h2>
<p>This section describes environment variables that affect how mdadm operates. </p>
<dl>
<dt><code>MDADM_NO_MDMON</code></p>
<dd>Setting this value to 1 will prevent mdadm from automatically launching mdmon. This variable is intended primarily for debugging mdadm/mdmon. </p>
<dt><code>MDADM_NO_UDEV</code></p>
<dd>Normally, <i>mdadm</i> does not create any device nodes in /dev, but leaves that task to <i>udev</i>. If <i>udev</i> appears not to be configured, or if this environment variable is set to &#8216;1&#8217;, the <i>mdadm</i> will create and devices that are needed. </p>
<dt><code>MDADM_NO_SYSTEMCTL</code></p>
<dd>If <i>mdadm</i> detects that <i>systemd</i> is in use it will normally request <i>systemd</i> to start various background tasks (particularly <i>mdmon</i>) rather than forking and running them in the background. This can be suppressed by setting <code>MDADM_NO_SYSTEMCTL=1</code>. </p>
<dt><code>IMSM_NO_PLATFORM</code></p>
<dd>A key value of IMSM metadata is that it allows interoperability with boot ROMs on Intel platforms, and with other major operating systems. Consequently, <i>mdadm</i> will only allow an IMSM array to be created or modified if detects that it is running on an Intel platform which supports IMSM, and supports the particular configuration of IMSM that is being requested (some functionality requires newer OROM support). </p>
<p> These checks can be suppressed by setting IMSM_NO_PLATFORM=1 in the environment. This can be useful for testing or for disaster recovery. You should be aware that interoperability may be compromised by setting this value. </p>
<dt><code>MDADM_GROW_ALLOW_OLD</code></p>
<dd>If an array is stopped while it is performing a reshape and that reshape was making use of a backup file, then when the array is re-assembled <i>mdadm</i> will sometimes complain that the backup file is too old. If this happens and you are certain it is the right backup file, you can over-ride this check by setting <code>MDADM_GROW_ALLOW_OLD=1</code> in the environment. </p>
<dt><code>MDADM_CONF_AUTO</code></p>
<dd>Any string given in this variable is added to the start of the <code>AUTO</code> line in the config file, or treated as the whole <code>AUTO</code> line if none is given. It can be used to disable certain metadata types when <i>mdadm</i> is called from a boot script. For example<br />
 <code> export MDADM_CONF_AUTO=&#8217;-ddf -imsm&#8217;</code><br />
 will make sure that <i>mdadm</i> does not automatically assemble any DDF or IMSM arrays that are found. This can be useful on systems configured to manage such arrays with <code>dmraid</code>. </p>
</dl>
<h2>Examples</h2>
<p><code> mdadm &#8211;query /dev/name-of-device</code><br />
 This will find out if a given device is a RAID array, or is part of one, and will provide brief information about the device. <code> mdadm &#8211;assemble &#8211;scan</code><br />
 This will assemble and start all arrays listed in the standard config file. This command will typically go in a system startup file. <code> mdadm &#8211;stop &#8211;scan</code><br />
 This will shut down all arrays that can be shut down (i.e. are not currently in use). This will typically go in a system shutdown script. <code> mdadm &#8211;follow &#8211;scan &#8211;delay=120</code><br />
 If (and only if) there is an Email address or program given in the standard config file, then monitor the status of all arrays listed in that file by polling them ever 2 minutes. <code> mdadm &#8211;create /dev/md0 &#8211;level=1 &#8211;raid-devices=2 /dev/hd[ac]1</code><br />
 Create /dev/md0 as a RAID1 array consisting of /dev/hda1 and /dev/hdc1.<br />
 <code> echo &#8216;DEVICE /dev/hd*[0-9] /dev/sd*[0-9]&#8217; &gt; mdadm.conf</code><br />
 <code> mdadm &#8211;detail &#8211;scan &gt;&gt; mdadm.conf</code><br />
 This will create a prototype config file that describes currently active arrays that are known to be made from partitions of IDE or SCSI drives. This file should be reviewed before being used as it may contain unwanted detail. <code> echo &#8216;DEVICE /dev/hd[a-z] /dev/sd*[a-z]&#8217; &gt; mdadm.conf</code><br />
 <code> mdadm &#8211;examine &#8211;scan &#8211;config=mdadm.conf &gt;&gt; mdadm.conf</code><br />
 This will find arrays which could be assembled from existing IDE and SCSI whole drives (not partitions), and store the information in the format of a config file. This file is very likely to contain unwanted detail, particularly the <code>devices=</code> entries. It should be reviewed and edited before being used as an actual config file. <code> mdadm &#8211;examine &#8211;brief &#8211;scan &#8211;config=partitions</code><br />
 <code> mdadm -Ebsc partitions</code><br />
 Create a list of devices by reading <code>/proc/partitions</code>, scan these for RAID superblocks, and printout a brief listing of all that were found. <code> mdadm -Ac partitions -m 0 /dev/md0</code><br />
 Scan all partitions and devices listed in <code>/proc/partitions</code> and assemble <code>/dev/md0</code> out of all such devices with a RAID superblock with a minor number of 0. <code> mdadm &#8211;monitor &#8211;scan &#8211;daemonise &gt; /run/mdadm/mon.pid</code><br />
 If config file contains a mail address or alert program, run mdadm in the background in monitor mode monitoring all md devices. Also write pid of mdadm daemon to <code>/run/mdadm/mon.pid</code>. <code> mdadm -Iq /dev/somedevice</code><br />
 Try to incorporate newly discovered device into some array as appropriate. <code> mdadm &#8211;incremental &#8211;rebuild-map &#8211;run &#8211;scan</code><br />
 Rebuild the array map from any current arrays, and then start any that can be started. <code> mdadm /dev/md4 &#8211;fail detached &#8211;remove detached</code><br />
 Any devices which are components of /dev/md4 will be marked as faulty and then remove from the array. <code> mdadm &#8211;grow /dev/md4 &#8211;level=6 &#8211;backup-file=/root/backup-md4</code><br />
 The array <code>/dev/md4</code> which is currently a RAID5 array will be converted to RAID6. There should normally already be a spare drive attached to the array as a RAID6 needs one more drive than a matching RAID5. <code> mdadm &#8211;create /dev/md/ddf &#8211;metadata=ddf &#8211;raid-disks 6 /dev/sd[a-f]</code><br />
 Create a DDF array over 6 devices. <code> mdadm &#8211;create /dev/md/home -n3 -l5 -z 30000000 /dev/md/ddf</code><br />
 Create a RAID5 array over any 3 devices in the given DDF set. Use only 30 gigabytes of each device. <code> mdadm -A /dev/md/ddf1 /dev/sd[a-f]</code><br />
 Assemble a pre-exist ddf array. <code> mdadm -I /dev/md/ddf1</code><br />
 Assemble all arrays contained in the ddf array, assigning names as appropriate. <code> mdadm &#8211;create &#8211;help</code><br />
 Provide help about the Create mode. <code> mdadm &#8211;config &#8211;help</code><br />
 Provide help about the format of the config file. <code> mdadm &#8211;help</code><br />
 Provide general help. </p>
<h2>Files</h2>
<h3>/proc/mdstat</h3>
<p>If you&#8217;re using the <code>/proc</code> filesystem, <code>/proc/mdstat</code> lists all active md devices with information about them. <i>mdadm</i> uses this to find arrays when <code>&#8211;scan</code> is given in Misc mode, and to monitor array reconstruction on Monitor mode.</p>
<h3>/etc/mdadm/mdadm.conf (or /etc/mdadm.conf)</h3>
<p>The config file lists which devices may be scanned to see if they contain MD super block, and gives identifying information (e.g. UUID) about known MD arrays. See <code><a href="/docs/linux/man/5-mdadm-conf/">mdadm.conf</a></code>(5) for more details.</p>
<h3>/etc/mdadm/mdadm.conf.d (or /etc/mdadm.conf.d)</h3>
<p>A directory containing configuration files which are read in lexical order.</p>
<h3>/run/mdadm/map</h3>
<p>When <code>&#8211;incremental</code> mode is used, this file gets a list of arrays currently being created.</p>
<h2>Device Names</h2>
<p><i>mdadm</i> understand two sorts of names for array devices. </p>
<p> The first is the so-called &#8216;standard&#8217; format name, which matches the names used by the kernel and which appear in <i>/proc/mdstat</i>. </p>
<p> The second sort can be freely chosen, but must reside in <i>/dev/md/</i>. When giving a device name to <i>mdadm</i> to create or assemble an array, either full path name such as <i>/dev/md0</i> or <i>/dev/md/home</i> can be given, or just the suffix of the second sort of name, such as <i>home</i> can be given. </p>
<p> When <i>mdadm</i> chooses device names during auto-assembly or incremental assembly, it will sometimes add a small sequence number to the end of the name to avoid conflicted between multiple arrays that have the same name. If <i>mdadm</i> can reasonably determine that the array really is meant for this host, either by a hostname in the metadata, or by the presence of the array in <code>mdadm.conf</code>, then it will leave off the suffix if possible. Also if the homehost is specified as <code>&lt;ignore&gt;</code> <i>mdadm</i> will only use a suffix if a different array of the same name already exists or is listed in the config file. </p>
<p> The standard names for non-partitioned arrays (the only sort of md array available in 2.4 and earlier) are of the form</p>
<dl>
<dd>/dev/md<code>NN</code></dl>
<p> where NN is a number. The standard names for partitionable arrays (as available from 2.6 onwards) are of the form:</p>
<dl>
<dd>/dev/md_d<code>NN</code></dl>
<p> Partition numbers should be indicated by adding &quot;pMM&quot; to these, thus &quot;/dev/md/d1p2&quot;. </p>
<p> From kernel version 2.6.28 the &quot;non-partitioned array&quot; can actually be partitioned. So the &quot;md_d<code>NN</code>&quot; names are no longer needed, and partitions such as &quot;/dev/md<code>NN</code>p<code>XX</code>&quot; are possible. </p>
<p> From kernel version 2.6.29 standard names can be non-numeric following the form:</p>
<dl>
<dd>/dev/md_<code>XXX</code></dl>
<p> where <code>XXX</code> is any string. These names are supported by <i>mdadm</i> since version 3.3 provided they are enabled in <i>mdadm.conf</i>.</p>
<h2>Note</h2>
<p><i>mdadm</i> was previously known as <i>mdctl</i>.</p>
<h2>See Also</h2>
<p>For further information on mdadm usage, MD and the various levels of RAID, see:</p>
<dl>
<dd><code><a rel="nofollow" href="http://raid.wiki.kernel.org/">http://raid.wiki.kernel.org/</a></code></dl>
<p> (based upon Jakob &Oslash;stergaard&#8217;s Software-RAID.HOWTO) The latest version of <i>mdadm</i> should always be available from</p>
<dl>
<dd><code><a rel="nofollow" href="http://www.kernel.org/pub/linux/utils/raid/mdadm/">http://www.kernel.org/pub/linux/utils/raid/mdadm/</a></code></dl>
<p> Related man pages: <i><a href="/docs/linux/man/8-mdmon/">mdmon</a></i>(8), <i><a href="/docs/linux/man/5-mdadm-conf/">mdadm.conf</a></i>(5), <i><a href="/docs/linux/man/4-md/">md</a></i>(4). </p>
