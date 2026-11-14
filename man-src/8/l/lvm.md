---
title: "lvm(8)"
name: "lvm"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvm/"
description: "lvm — LVM2 tools"
---

<p>lvm &#8212; LVM2 tools</p>
<h2>Synopsis</h2>
<p><code>lvm</code> [<i>command</i>|<i>file</i>]</p>
<h2>Description</h2>
<p>The Logical Volume Manager (LVM) provides tools to create virtual block devices from physical devices. Virtual devices may be easier to manage than physical devices, and can have capabilities beyond what the physical devices provide themselves. A Volume Group (VG) is a collection of one or more physical devices, each called a Physical Volume (PV). A Logical Volume (LV) is a virtual block device that can be used by the system or applications. Each block of data in an LV is stored on one or more PV in the VG, according to algorithms implemented by Device Mapper (DM) in the kernel. </p>
<p> The lvm command, and other commands listed below, are the command-line tools for LVM. A separate manual page describes each command in detail. </p>
<p> If <code>lvm</code> is invoked with no arguments it presents a readline prompt (assuming it was compiled with readline support). LVM commands may be entered interactively at this prompt with readline facilities including history and command name and option completion. Refer to <code><a href="/docs/linux/man/3-readline/">readline</a></code>(3) for details. </p>
<p> If <code>lvm</code> is invoked with argv[0] set to the name of a specific LVM command (for example by using a hard or soft link) it acts as that command. </p>
<p> On invocation, <code>lvm</code> requires that only the standard file descriptors stdin, stdout and stderr are available. If others are found, they get closed and messages are issued warning about the leak. This warning can be suppressed by setting the environment variable <code>LVM_SUPPRESS_FD_WARNINGS</code>. </p>
<p> Where commands take VG or LV names as arguments, the full path name is optional. An LV called &quot;lvol0&quot; in a VG called &quot;vg0&quot; can be specified as &quot;vg0/lvol0&quot;. Where a list of VGs is required but is left empty, a list of all VGs will be substituted. Where a list of LVs is required but a VG is given, a list of all the LVs in that VG will be substituted. So <code>lvdisplay vg0</code> will display all the LVs in &quot;vg0&quot;. Tags can also be used &#8211; see <code>&#8211;addtag</code> below. </p>
<p> One advantage of using the built-in shell is that configuration information gets cached internally between commands. </p>
<p> A file containing a simple script with one command per line can also be given on the command line. The script can also be executed directly if the first line is #! followed by the absolute path of <code>lvm</code>. </p>
<p> Additional hyphens within option names are ignored. For example, <code>&#8211;readonly</code> and <code>&#8211;read-only</code> are both accepted.</p>
<h2>Built-In Commands</h2>
<p>The following commands are built into lvm without links normally being created in the filesystem for them. </p>
<dl>
<dt><code>config</code></p>
<dd>The same as <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) below.</p>
<dt><code>devtypes</code></p>
<dd>Display the recognised built-in block device types.</p>
<dt><code>dumpconfig</code></p>
<dd>The same as <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) below.</p>
<dt><code>formats</code></p>
<dd>Display recognised metadata formats.</p>
<dt><code>fullreport</code></p>
<dd>Report information about PVs, PV segments, VGs, LVs and LV segments, all at once.</p>
<dt><code>help</code></p>
<dd>Display the help text.</p>
<dt><code>lastlog</code></p>
<dd>Display log report of last command run in LVM shell if command log reporting is enabled.</p>
<dt><code>lvpoll</code></p>
<dd>Complete lvmpolld operations (Internal command).</p>
<dt><code>segtypes</code></p>
<dd>Display recognised Logical Volume segment types.</p>
<dt><code>systemid</code></p>
<dd>Display any system ID currently set on this host.</p>
<dt><code>tags</code></p>
<dd>Display any tags defined on this host.</p>
<dt><code>version</code></p>
<dd>Display version information.</dl>
<h2>Commands</h2>
<p>The following commands implement the core LVM functionality. </p>
<dl>
<dt><code>pvchange</code></p>
<dd>Change attributes of a Physical Volume.</p>
<dt><code>pvck</code></p>
<dd>Check Physical Volume metadata.</p>
<dt><code>pvcreate</code></p>
<dd>Initialize a disk or partition for use by LVM.</p>
<dt><code>pvdisplay</code></p>
<dd>Display attributes of a Physical Volume.</p>
<dt><code>pvmove</code></p>
<dd>Move Physical Extents.</p>
<dt><code>pvremove</code></p>
<dd>Remove a Physical Volume.</p>
<dt><code>pvresize</code></p>
<dd>Resize a disk or partition in use by LVM2.</p>
<dt><code>pvs</code></p>
<dd>Report information about Physical Volumes.</p>
<dt><code>pvscan</code></p>
<dd>Scan all disks for Physical Volumes.</p>
<dt><code>vgcfgbackup</code></p>
<dd>Backup Volume Group descriptor area.</p>
<dt><code>vgcfgrestore</code></p>
<dd>Restore Volume Group descriptor area.</p>
<dt><code>vgchange</code></p>
<dd>Change attributes of a Volume Group.</p>
<dt><code>vgck</code></p>
<dd>Check Volume Group metadata.</p>
<dt><code>vgconvert</code></p>
<dd>Convert Volume Group metadata format.</p>
<dt><code>vgcreate</code></p>
<dd>Create a Volume Group.</p>
<dt><code>vgdisplay</code></p>
<dd>Display attributes of Volume Groups.</p>
<dt><code>vgexport</code></p>
<dd>Make volume Groups unknown to the system.</p>
<dt><code>vgextend</code></p>
<dd>Add Physical Volumes to a Volume Group.</p>
<dt><code>vgimport</code></p>
<dd>Make exported Volume Groups known to the system.</p>
<dt><code>vgimportclone</code></p>
<dd>Import and rename duplicated Volume Group (e.g. a hardware snapshot).</p>
<dt><code>vgmerge</code></p>
<dd>Merge two Volume Groups.</p>
<dt><code>vgmknodes</code></p>
<dd>Recreate Volume Group directory and Logical Volume special files</p>
<dt><code>vgreduce</code></p>
<dd>Reduce a Volume Group by removing one or more Physical Volumes.</p>
<dt><code>vgremove</code></p>
<dd>Remove a Volume Group.</p>
<dt><code>vgrename</code></p>
<dd>Rename a Volume Group.</p>
<dt><code>vgs</code></p>
<dd>Report information about Volume Groups.</p>
<dt><code>vgscan</code></p>
<dd>Scan all disks for Volume Groups.</p>
<dt><code>vgsplit</code></p>
<dd>Split a Volume Group into two, moving any logical volumes from one Volume Group to another by moving entire Physical Volumes.</p>
<dt><code>lvchange</code></p>
<dd>Change attributes of a Logical Volume.</p>
<dt><code>lvconvert</code></p>
<dd>Convert a Logical Volume from linear to mirror or snapshot.</p>
<dt><code>lvcreate</code></p>
<dd>Create a Logical Volume in an existing Volume Group.</p>
<dt><code>lvdisplay</code></p>
<dd>Display attributes of a Logical Volume.</p>
<dt><code>lvextend</code></p>
<dd>Extend the size of a Logical Volume.</p>
<dt><code>lvmconfig</code></p>
<dd>Display the configuration information after loading <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) and any other configuration files.</p>
<dt><code>lvmdiskscan</code></p>
<dd>Scan for all devices visible to LVM2.</p>
<dt><code>lvmdump</code></p>
<dd>Create lvm2 information dumps for diagnostic purposes.</p>
<dt><code>lvreduce</code></p>
<dd>Reduce the size of a Logical Volume.</p>
<dt><code>lvremove</code></p>
<dd>Remove a Logical Volume.</p>
<dt><code>lvrename</code></p>
<dd>Rename a Logical Volume.</p>
<dt><code>lvresize</code></p>
<dd>Resize a Logical Volume.</p>
<dt><code>lvs</code></p>
<dd>Report information about Logical Volumes.</p>
<dt><code>lvscan</code></p>
<dd>Scan (all disks) for Logical Volumes.</dl>
<p> The following LVM1 commands are not implemented in LVM2: <code>lvmchange</code>, <code>lvmsadc</code>, <code>lvmsar</code>, <code>pvdata</code>. For performance metrics, use <code><a href="/docs/linux/man/8-dmstats/">dmstats</a></code>(8) or to manipulate the kernel device-mapper driver used by LVM2 directly, use <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8).</p>
<h2>Valid Names</h2>
<p>The valid characters for VG and LV names are: <code>a</code>&#8211;<code>z</code> <code>A</code>&#8211;<code>Z</code> <code>0</code>&#8211;<code>9</code> <code>+ _ . &#8211;</code> </p>
<p> VG names cannot begin with a hyphen. The name of a new LV also cannot begin with a hyphen. However, if the configuration setting <code>metadata/record_lvs_history</code> is enabled then an LV name with a hyphen as a prefix indicates that, although the LV was removed, it is still being tracked because it forms part of the history of at least one LV that is still present. This helps to record the ancestry of thin snapshots even after some links in the chain have been removed. A reference to the historical LV &#8216;lvol1&#8217; in VG &#8216;vg00&#8217; would be &#8216;vg00/\-lvol1&#8217; or just &#8216;-lvol1&#8217; if the VG is already set. (The latter form must be preceded by &#8216;&#8211;&#8216; to terminate command line option processing before reaching this argument.) </p>
<p> There are also various reserved names that are used internally by lvm that can not be used as LV or VG names. A VG cannot be called anything that exists in <i>/dev/</i> at the time of creation, nor can it be called &#8216;.&#8217; or &#8216;..&#8217;. An LV cannot be called &#8216;.&#8217;, &#8216;..&#8217;, &#8216;snapshot&#8217; or &#8216;pvmove&#8217;. The LV name may also not contain any of the following strings: &#8216;_cdata&#8217;, &#8216;_cmeta&#8217;, &#8216;_corig&#8217;, &#8216;_mlog&#8217;, &#8216;_mimage&#8217;, &#8216;_pmspare&#8217;, &#8216;_rimage&#8217;, &#8216;_rmeta&#8217;, &#8216;_tdata&#8217;, &#8216;_tmeta&#8217;, &#8216;_vorigin&#8217; or &#8216;_vdata&#8217;. A directory bearing the name of each Volume Group is created under <i>/dev</i> when any of its Logical Volumes are activated. Each active Logical Volume is accessible from this directory as a symbolic link leading to a device node. Links or nodes in <i>/dev/mapper</i> are intended only for internal use and the precise format and escaping might change between releases and distributions. Other software and scripts should use the <i>/dev/VolumeGroupName/LogicalVolumeName</i> format to reduce the chance of needing amendment when the software is updated. Should you need to process the node names in /dev/mapper, you may use <code>dmsetup splitname</code> to separate out the original VG, LV and internal layer names.</p>
<h2>Unique Names</h2>
<p>VG names should be unique. vgcreate will produce an error if the specified VG name matches an existing VG name. However, there are cases where different VGs with the same name can appear to LVM, e.g. after moving disks or changing filters. </p>
<p> When VGs with the same name exist, commands operating on all VGs will include all of the VGs with the same name. If the ambiguous VG name is specified on the command line, the command will produce an error. The error states that multiple VGs exist with the specified name. To process one of the VGs specifically, the &#8211;select option should be used with the UUID of the intended VG: &#8216;&#8211;select vg_uuid=&lt;uuid&gt;&#8217;. </p>
<p> An exception is if all but one of the VGs with the shared name is foreign (see <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7).) In this case, the one VG that is not foreign is assumed to be the intended VG and is processed. </p>
<p> LV names are unique within a VG. The name of an historical LV cannot be reused until the historical LV has itself been removed or renamed.</p>
<h2>Allocation</h2>
<p>When an operation needs to allocate Physical Extents for one or more Logical Volumes, the tools proceed as follows: </p>
<p> First of all, they generate the complete set of unallocated Physical Extents in the Volume Group. If any ranges of Physical Extents are supplied at the end of the command line, only unallocated Physical Extents within those ranges on the specified Physical Volumes are considered. </p>
<p> Then they try each allocation policy in turn, starting with the strictest policy (<code>contiguous</code>) and ending with the allocation policy specified using <code>&#8211;alloc</code> or set as the default for the particular Logical Volume or Volume Group concerned. For each policy, working from the lowest-numbered Logical Extent of the empty Logical Volume space that needs to be filled, they allocate as much space as possible according to the restrictions imposed by the policy. If more space is needed, they move on to the next policy. </p>
<p> The restrictions are as follows: </p>
<p> <code>Contiguous</code> requires that the physical location of any Logical Extent that is not the first Logical Extent of a Logical Volume is adjacent to the physical location of the Logical Extent immediately preceding it. </p>
<p> <code>Cling</code> requires that the Physical Volume used for any Logical Extent to be added to an existing Logical Volume is already in use by at least one Logical Extent earlier in that Logical Volume. If the configuration parameter <code>allocation/cling_tag_list</code> is defined, then two Physical Volumes are considered to match if any of the listed tags is present on both Physical Volumes. This allows groups of Physical Volumes with similar properties (such as their physical location) to be tagged and treated as equivalent for allocation purposes. </p>
<p> When a Logical Volume is striped or mirrored, the above restrictions are applied independently to each stripe or mirror image (leg) that needs space. </p>
<p> <code>Normal</code> will not choose a Physical Extent that shares the same Physical Volume as a Logical Extent already allocated to a parallel Logical Volume (i.e. a different stripe or mirror image/leg) at the same offset within that parallel Logical Volume. </p>
<p> When allocating a mirror log at the same time as Logical Volumes to hold the mirror data, Normal will first try to select different Physical Volumes for the log and the data. If that&#8217;s not possible and the <code>allocation/mirror_logs_require_separate_pvs</code> configuration parameter is set to 0, it will then allow the log to share Physical Volume(s) with part of the data. </p>
<p> When allocating thin pool metadata, similar considerations to those of a mirror log in the last paragraph apply based on the value of the <code>allocation/thin_pool_metadata_require_separate_pvs</code> configuration parameter. </p>
<p> If you rely upon any layout behaviour beyond that documented here, be aware that it might change in future versions of the code. </p>
<p> For example, if you supply on the command line two empty Physical Volumes that have an identical number of free Physical Extents available for allocation, the current code considers using each of them in the order they are listed, but there is no guarantee that future releases will maintain that property. If it is important to obtain a specific layout for a particular Logical Volume, then you should build it up through a sequence of <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) and <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) steps such that the restrictions described above applied to each step leave the tools no discretion over the layout. </p>
<p> To view the way the allocation process currently works in any specific case, read the debug logging output, for example by adding <code>-vvvv</code> to a command.</p>
<h2>Logical Volume Types</h2>
<p>Some logical volume types are simple to create and can be done with a single <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) command. The linear and striped logical volume types are an example of this. Other logical volume types may require more than one command to create. The cache (<code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7)) and thin provisioning (<code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7)) types are examples of this.</p>
<h2>Diagnostics</h2>
<p>All tools return a status code of zero on success or non-zero on failure. The non-zero codes distinguish only between the broad categories of unrecognised commands, problems processing the command line arguments and any other failures. As LVM remains under active development, the code used in a specific case occasionally changes between releases. Message text may also change.</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>HOME</code></p>
<dd>Directory containing <i>.lvm_history</i> if the internal readline shell is invoked.</p>
<dt><code>LVM_OUT_FD</code></p>
<dd>File descriptor to use for common output from LVM commands.</p>
<dt><code>LVM_ERR_FD</code></p>
<dd>File descriptor to use for error output from LVM commands.</p>
<dt><code>LVM_REPORT_FD</code></p>
<dd>File descriptor to use for report output from LVM commands.</p>
<dt><code>LVM_COMMAND_PROFILE</code></p>
<dd>Name of default command profile to use for LVM commands. This profile is overriden by direct use of <code>&#8211;commandprofile</code> command line option.</p>
<dt><code>LVM_RUN_BY_DMEVENTD</code></p>
<dd>This variable is normally set by dmeventd plugin to inform lvm2 command it is running from dmeventd plugin so lvm2 takes some extra action to avoid comunication and deadlocks with dmeventd.</p>
<dt><code>LVM_SYSTEM_DIR</code></p>
<dd>Directory containing <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) and other LVM system files. Defaults to &quot;<i>/etc/lvm</i>&quot;.</p>
<dt><code>LVM_SUPPRESS_FD_WARNINGS</code></p>
<dd>Suppress warnings about unexpected file descriptors passed into LVM.</p>
<dt><code>LVM_SUPPRESS_SYSLOG</code></p>
<dd>Suppress contacting syslog.</p>
<dt><code>LVM_VG_NAME</code></p>
<dd>The Volume Group name that is assumed for any reference to a Logical Volume that doesn&#8217;t specify a path. Not set by default.</p>
<dt><code>LVM_LVMPOLLD_PIDFILE</code></p>
<dd>Path to the file that stores the lvmpolld process ID.</p>
<dt><code>LVM_LVMPOLLD_SOCKET</code></p>
<dd>Path to the socket used to communicate with lvmpolld..</p>
<dt><code>LVM_LOG_FILE_EPOCH</code></p>
<dd>A string of up to 32 letters appended to the log filename and followed by the process ID and a startup timestamp using this format string &quot;_%s_%d_%llu&quot;. When set, each process logs to a separate file.</p>
<dt><code>LVM_LOG_FILE_MAX_LINES</code></p>
<dd>If more than this number of lines are sent to the log file, the command gets aborted. Automated tests use this to terminate looping commands.</p>
<dt><code>LVM_EXPECTED_EXIT_STATUS</code></p>
<dd>The status anticipated when the process exits. Use &quot;&gt;N&quot; to match any status greater than N. If the actual exit status matches and a log file got produced, it is deleted. <code>LVM_LOG_FILE_EPOCH</code> and <code>LVM_EXPECTED_EXIT_STATUS</code> together allow automated test scripts to discard uninteresting log data.</p>
<dt><code>LVM_SUPPRESS_LOCKING_FAILURE_MESSAGES</code></p>
<dd>Used to suppress warning messages when the configured locking is known to be unavailable.</p>
<dt><code>DM_ABORT_ON_INTERNAL_ERRORS</code></p>
<dd>Abort processing if the code detects a non-fatal internal error.</p>
<dt><code>DM_DISABLE_UDEV</code></p>
<dd>Avoid interaction with udev. LVM will manage the relevant nodes in /dev directly.</p>
<dt><code>DM_DEBUG_WITH_LINE_NUMBERS</code></p>
<dd>Prepends source file name and code line number with libdm debugging.</dl>
<h2>Files</h2>
<p><i>/etc/lvm/lvm.conf</i><br />
 <i>$HOME/.lvm_history</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8), <code><a href="/docs/linux/man/8-dmstats/">dmstats</a></code>(8), <code><a href="/docs/linux/man/3-readline/">readline</a></code>(3) </p>
