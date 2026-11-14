---
title: "pvcreate(8)"
name: "pvcreate"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pvcreate/"
description: "pvcreate – Initialize physical volume(s) for use by LVM"
---

<p>pvcreate &#8211; Initialize physical volume(s) for use by LVM</p>
<h2>Synopsis</h2>
<p><code>pvcreate</code> <i>position_args</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;]</p>
<h2>Description</h2>
<p>pvcreate initializes a Physical Volume (PV) on a device so the device is recognized as belonging to LVM. This allows the PV to be used in a Volume Group (VG). An LVM disk label is written to the device, and LVM metadata areas are initialized. A PV can be placed on a whole device or partition. </p>
<p> Use <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) to create a new VG on the PV, or <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) to add the PV to an existing VG. Use <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) to remove the LVM disk label from the device. </p>
<p> The force option will create a PV without confirmation. Repeating the force option (<code>-ff</code>) will forcibly create a PV, overriding checks that normally prevent it, e.g. if the PV is already in a VG. </p>
<p> <code>Metadata location, size, and alignment</code> </p>
<p> The LVM disk label begins 512 bytes from the start of the device, and is 512 bytes in size. </p>
<p> The LVM metadata area begins at an offset (from the start of the device) equal to the page size of the machine creating the PV (often 4 KiB.) The metadata area contains a 512 byte header and a multi-KiB circular buffer that holds text copies of the VG metadata. </p>
<p> With default settings, the first physical extent (PE), which contains LV data, is 1 MiB from the start of the device. This location is controlled by <code>default_data_alignment</code> in lvm.conf, which is set to 1 (MiB) by default. The pe_start will be a multiple of this many MiB. This location can be checked with:<br />
 <code>pvs -o pe_start</code> <i>PV</i> </p>
<p> The size of the LVM metadata area is the space between the the start of the metadata area and the first PE. When metadata begins at 4 KiB and the first PE is at 1024 KiB, the metadata area size is 1020 KiB. This can be checked with:<br />
 <code>pvs -o mda_size</code> <i>PV</i> </p>
<p> The mda_size cannot be increased after pvcreate, so if larger metadata is needed, it must be set during pvcreate. Two copies of the VG metadata must always fit within the metadata area, so the maximum VG metadata size is around half the mda_size. This can be checked with:<br />
 <code>vgs -o mda_free</code> <i>VG</i> </p>
<p> A larger metadata area can be set with &#8211;metadatasize. The resulting mda_size may be larger than specified due to default_data_alignment placing pe_start on a MiB boundary, and the fact that the metadata area extends to the first PE. With metadata starting at 4 KiB and default_data_alignment 1 (MiB), setting &#8211;metadatasize 2048k results in pe_start of 3 MiB and mda_size of 3068 KiB. Alternatively, &#8211;metadatasize 2044k results in pe_start at 2 MiB and mda_size of 2044 KiB. </p>
<p> The alignment of pe_start described above may be automatically overriden based on md device properties or device i/o properties reported in sysfs. These automatic adjustments can be enabled/disabled using lvm.conf settings md_chunk_alignment and data_alignment_offset_detection. </p>
<p> To use a different pe_start alignment, use the &#8211;dataalignment option. The &#8211;metadatasize option would also typically be used in this case because the metadata area size also determines the location of pe_start. When using these two options together, pe_start is calculated as: metadata area start (page size), plus the specified &#8211;metadatasize, rounded up to the next multiple of &#8211;dataalignment. With metadata starting at 4 KiB, &#8211;metadatasize 2048k, and &#8211;dataalignment 128k, pe_start is 2176 KiB and mda_size is 2172 KiB. The pe_start of 2176 KiB is the nearest even multiple of 128 KiB that provides at least 2048 KiB of metadata space. Always check the resulting alignment and metadata size when using these options. </p>
<p> To shift an aligned pe_start value, use the &#8211;dataaligmentoffset option. The pe_start alignment is calculated as described above, and then the value specified with &#8211;dataaligmentoffset is added to produce the final pe_start value.</p>
<h2>Usage</h2>
<p><code>pvcreate</code> <i>PV</i> &#8230; </p>
<dl>
<dd>[ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>-M</code>|<code>&#8211;metadatatype</code> <code>lvm2</code> ]<br />
 [ <code>-u</code>|<code>&#8211;uuid</code> <i>String</i> ]<br />
 [ <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;dataalignment</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;dataalignmentoffset</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;bootloaderareasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;labelsector</code> <i>Number</i> ]<br />
 [ <code>&#8211;[pv]metadatacopies</code> <code>0</code>|<code>1</code>|<code>2</code> ]<br />
 [ <code>&#8211;metadatasize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;metadataignore</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;norestorefile</code> ]<br />
 [ <code>&#8211;setphysicalvolumesize</code> <i>Size</i>[m|UNIT] ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
 [ <code>&#8211;restorefile</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> Common options for lvm:</p>
<dl>
<dd>[ <code>-d</code>|<code>&#8211;debug</code> ]<br />
 [ <code>-h</code>|<code>&#8211;help</code> ]<br />
 [ <code>-q</code>|<code>&#8211;quiet</code> ]<br />
 [ <code>-t</code>|<code>&#8211;test</code> ]<br />
 [ <code>-v</code>|<code>&#8211;verbose</code> ]<br />
 [ <code>-y</code>|<code>&#8211;yes</code> ]<br />
 [ <code>&#8211;commandprofile</code> <i>String</i> ]<br />
 [ <code>&#8211;config</code> <i>String</i> ]<br />
 [ <code>&#8211;driverloaded</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>&#8211;lockopt</code> <i>String</i> ]<br />
 [ <code>&#8211;longhelp</code> ]<br />
 [ <code>&#8211;nolocking</code> ]<br />
 [ <code>&#8211;profile</code> <i>String</i> ]<br />
 [ <code>&#8211;version</code> ]</dl>
<h2>Options</h2>
<dl>
<dt> <code>&#8211;bootloaderareasize</code> <i>Size</i>[m|UNIT]</p>
<dd>
<dd>Reserve space for the bootloader between the LVM metadata area and the first PE. The bootloader area is reserved for bootloaders to embed their own data or metadata; LVM will not use it. The bootloader area begins where the first PE would otherwise be located. The first PE is moved out by the size of the bootloader area, and then moved out further if necessary to match the data alignment. The start of the bootloader area is always aligned, see also &#8211;dataalignment and &#8211;dataalignmentoffset. The bootloader area may be larger than requested due to the alignment, but it&#8217;s never less than the requested size. To see the bootloader area start and size of an existing PV use pvs -o +pv_ba_start,pv_ba_size.</p>
<dt> <code>&#8211;commandprofile</code> <i>String</i></p>
<dd>
<dd>The command profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;config</code> <i>String</i></p>
<dd>
<dd>Config settings for the command. These override lvm.conf settings. The String arg uses the same format as lvm.conf, or may use section/field syntax. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about config.</p>
<dt> <code>&#8211;dataalignment</code> <i>Size</i>[k|UNIT]</p>
<dd>
<dd>Align the start of a PV data area with a multiple of this number. To see the location of the first Physical Extent (PE) of an existing PV, use pvs -o +pe_start. In addition, it may be shifted by an alignment offset, see &#8211;dataalignmentoffset. Also specify an appropriate PE size when creating a VG.</p>
<dt> <code>&#8211;dataalignmentoffset</code> <i>Size</i>[k|UNIT]</p>
<dd>
<dd>Shift the start of the PV data area by this additional offset.</p>
<dt> <code>-d</code>|<code>&#8211;debug</code> &#8230;</p>
<dd>
<dd>Set debug level. Repeat from 1 to 6 times to increase the detail of messages sent to the log file and/or syslog (if configured).</p>
<dt> <code>&#8211;driverloaded</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>If set to no, the command will not attempt to use device-mapper. For testing and debugging.</p>
<dt> <code>-f</code>|<code>&#8211;force</code> &#8230;</p>
<dd>
<dd>Override various checks, confirmations and protections. Use with extreme caution.</p>
<dt> <code>-h</code>|<code>&#8211;help</code></p>
<dd>
<dd>Display help text.</p>
<dt> <code>&#8211;labelsector</code> <i>Number</i></p>
<dd>
<dd>By default the PV is labelled with an LVM2 identifier in its second sector (sector 1). This lets you use a different sector near the start of the disk (between 0 and 3 inclusive &#8211; see LABEL_SCAN_SECTORS in the source). Use with care.</p>
<dt> <code>&#8211;lockopt</code> <i>String</i></p>
<dd>
<dd>Used to pass options for special cases to lvmlockd. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</p>
<dt> <code>&#8211;longhelp</code></p>
<dd>
<dd>Display long help text.</p>
<dt> <code>&#8211;metadataignore</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Specifies the metadataignore property of a PV. If yes, metadata areas on the PV are ignored, and lvm will not store metadata in the metadata areas of the PV. If no, lvm will store metadata on the PV.</p>
<dt> <code>&#8211;metadatasize</code> <i>Size</i>[m|UNIT]</p>
<dd>
<dd>The approximate amount of space used for each VG metadata area. The size may be rounded.</p>
<dt> <code>-M</code>|<code>&#8211;metadatatype</code> <code>lvm2</code></p>
<dd>
<dd>Specifies the type of on-disk metadata to use. <code>lvm2</code> (or just <code>2</code>) is the current, standard format. <code>lvm1</code> (or just <code>1</code>) is no longer used.</p>
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;norestorefile</code></p>
<dd>
<dd>In conjunction with &#8211;uuid, this allows a uuid to be specified without also requiring that a backup of the metadata be provided.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>&#8211;[pv]metadatacopies</code> <code>0</code>|<code>1</code>|<code>2</code></p>
<dd>
<dd>The number of metadata areas to set aside on a PV for storing VG metadata. When 2, one copy of the VG metadata is stored at the front of the PV and a second copy is stored at the end. When 1, one copy of the VG metadata is stored at the front of the PV. When 0, no copies of the VG metadata are stored on the given PV. This may be useful in VGs containing many PVs (this places limitations on the ability to use vgsplit later.)</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code></p>
<dd>
<dd>Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf. <code>basic</code> is the original format with columns and rows. If there is more than one report per command, each report is prefixed with the report name for identification. <code>json</code> produces report output in JSON format. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information.</p>
<dt> <code>&#8211;restorefile</code> <i>String</i></p>
<dd>
<dd>In conjunction with &#8211;uuid, this reads the file (produced by vgcfgbackup), extracts the location and size of the data on the PV, and ensures that the metadata produced by the program is consistent with the contents of the file, i.e. the physical extents will be in the same place and not be overwritten by new metadata. This provides a mechanism to upgrade the metadata format or to add/remove metadata areas. Use with care.</p>
<dt> <code>&#8211;setphysicalvolumesize</code> <i>Size</i>[m|UNIT]</p>
<dd>
<dd>Overrides the automatically detected size of the PV. Use with care, or prior to reducing the physical size of the device.</p>
<dt> <code>-t</code>|<code>&#8211;test</code></p>
<dd>
<dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</p>
<dt> <code>-u</code>|<code>&#8211;uuid</code> <i>String</i></p>
<dd>
<dd>Specify a UUID for the device. Without this option, a random UUID is generated. This option is needed before restoring a backup of LVM metadata onto a replacement device; see <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8). As such, use of &#8211;restorefile is compulsory unless the &#8211;norestorefile is used. All PVs must have unique UUIDs, and LVM will prevent certain operations if multiple devices are seen with the same UUID. See <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) for more information.</p>
<dt> <code>-v</code>|<code>&#8211;verbose</code> &#8230;</p>
<dd>
<dd>Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.</p>
<dt> <code>&#8211;version</code></p>
<dd>
<dd>Display version information.</p>
<dt> <code>-y</code>|<code>&#8211;yes</code></p>
<dd>
<dd>Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution. (For automatic no, see -qq.)</p>
<dt> <code>-Z</code>|<code>&#8211;zero</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Controls if the first 4 sectors (2048 bytes) of the device are wiped. The default is to wipe these sectors unless either or both of &#8211;restorefile or &#8211;uuid are specified.</dl>
<h2>Variables</h2>
<dl>
<dt> <i>PV</i></p>
<dd>
<dd>Physical Volume name, a device path under /dev. For commands managing physical extents, a PV positional arg generally accepts a suffix indicating a range (or multiple ranges) of physical extents (PEs). When the first PE is omitted, it defaults to the start of the device, and when the last PE is omitted it defaults to end. Start and end range (inclusive): <i>PV</i>[<code>:</code><i>PE</i><code>&#8211;</code><i>PE</i>]&#8230; Start and length range (counting from 0): <i>PV</i>[<code>:</code><i>PE</i><code>+</code><i>PE</i>]&#8230;</p>
<dt> <i>String</i></p>
<dd>
<dd>See the option description for information about the string content.</p>
<dt> <i>Size</i>[UNIT]</p>
<dd>
<dd>Size is an input number that accepts an optional unit. Input units are always treated as base two values, regardless of capitalization, e.g. &#8216;k&#8217; and &#8216;K&#8217; both refer to 1024. The default input unit is specified by letter, followed by |UNIT. UNIT represents other possible input units: <code>bBsSkKmMgGtTpPeE</code>. b|B is bytes, s|S is sectors of 512 bytes, k|K is kilobytes, m|M is megabytes, g|G is gigabytes, t|T is terabytes, p|P is petabytes, e|E is exabytes. (This should not be confused with the output control &#8211;units, where capital letters mean multiple of 1000.)</dl>
<h2>Environment Variables</h2>
<p>See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about environment variables used by lvm. For example, LVM_VG_NAME can generally be substituted for a required VG parameter.</p>
<h2>Examples</h2>
<p>Initialize a partition and a full device.<br />
 <code>pvcreate /dev/sdc4 /dev/sde</code> </p>
<p> If a device is a 4KiB sector drive that compensates for windows partitioning (sector 7 is the lowest aligned logical block, the 4KiB sectors start at LBA -1, and consequently sector 63 is aligned on a 4KiB boundary) manually account for this when initializing for use by LVM.<br />
 <code>pvcreate &#8211;dataalignmentoffset 7s /dev/sdb</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
