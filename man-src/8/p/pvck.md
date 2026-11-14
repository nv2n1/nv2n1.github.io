---
title: "pvck(8)"
name: "pvck"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pvck/"
description: "pvck – Check metadata on physical volumes"
---

<p>pvck &#8211; Check metadata on physical volumes</p>
<h2>Synopsis</h2>
<p><code>pvck</code> <i>option_args</i> <i>position_args</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;commandprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;config</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-d</code>|<code>&#8211;debug</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;driverloaded</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;dump</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-f</code>|<code>&#8211;file</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-h</code>|<code>&#8211;help</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;labelsector</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;lockopt</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;longhelp</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;nolocking</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;profile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;[pv]metadatacopies</code>&nbsp;<code>0</code>|<code>1</code>|<code>2</code> </p>
<p>&nbsp;<code>-q</code>|<code>&#8211;quiet</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;repair</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;repairtype</code>&nbsp;<code>pv_header</code>|<code>metadata</code>|<code>label_header</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;settings</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-t</code>|<code>&#8211;test</code> </p>
<p>&nbsp;<code>-v</code>|<code>&#8211;verbose</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;version</code> </p>
<p>&nbsp;<code>-y</code>|<code>&#8211;yes</code></p>
<h2>Description</h2>
<p>pvck checks and repairs LVM metadata on PVs.</p>
<h3>Dump</h3>
<p><code>headers</code><br />
 Print header values and warn if any values are incorrect. Checks the label_header, pv_header, mda_header(s), and metadata text. <code>metadata</code><br />
 Print or save the current metadata text, using headers to locate the metadata. If headers are damaged, the metadata may not be found. Use &#8211;settings &quot;mda_num=2&quot; to look in mda2 (the second mda at the end of the device (if used). The metadata text is printed to stdout. With &#8211;file, the metadata text is saved to a file. <code>metadata_all</code><br />
 List or save all versions of metadata found in the metadata area, using headers to locate the metadata. If headers are damaged, the metadata may not be found. Use &#8211;settings &quot;mda_num=2&quot; as above. All metadata versions are listed (add -v to include descriptions and dates in the listing.) With -file, all versions are written to a file. <code>metadata_search</code><br />
 Search for all versions of metadata in the common locations. This does not use headers, so it can find metadata even when headers are damaged. Use &#8211;settings &quot;mda_num=2&quot; as above. All metadata versions are listed (add -v to include descriptions and dates in the listing.) With &#8211;file, all versions are written to a file. To save one copy of metadata, use &#8211;settings &quot;metadata_offset=&lt;offset&gt;&quot;, where the offset is taken from the dump listing. <code>metadata_area</code><br />
 Save the entire text metadata area to a file without processing.</p>
<h3>Repair</h3>
<p><code>&#8211;repair</code><br />
 Repair headers and metadata on a PV. This uses a metadata input file that was extracted by &#8211;dump, or a backup file (from /etc/lvm/backup). When possible, use metadata saved by &#8211;dump from another PV in the same VG (or from a second metadata area on the PV). There are cases where the PV UUID needs to be specified for the PV being repaired. It is specified using &#8211;settings &quot;pv_uuid=&lt;UUID&gt;&quot;. In particular, if the device name for the PV being repaired does not match the previous device name of the PV, then LVM may not be able to determine the correct PV UUID. When headers are damaged on more than one PV in a VG, it is important for the user to determine the correct PV UUID and specify it in &#8211;settings. Otherwise, the wrong PV UUID could be used if device names have been swapped since the metadata was last written. If a PV had no metadata areas and the pv_header is damaged, then the repair will not know to create no metadata areas during repair. It will by default repair metadata in mda1. To repair with no metadata areas, use &#8211;settings &quot;mda_offset=0 mda_size=0&quot;. There are cases where repair should be run on all PVs in the VG (using the same metadata file): if all PVs in the VG are damaged, if using an old metadata version, or if a backup file is used instead of raw metadata. Using &#8211;repair is equivalent to running &#8211;repairtype pv_header followed by &#8211;repairtype metadata. <code>&#8211;repairtype pv_header</code><br />
 Repairs the header sector, containing the pv_header and label_header. <code>&#8211;repairtype metadata</code><br />
 Repairs the mda_header and metadata text. It requires the headers to be correct (having been undamaged or already repaired). <code>&#8211;repairtype label_header</code><br />
 Repairs label_header fields, leaving the pv_header (in the same sector) unchanged. (repairtype pv_header should usually be used instead.) </p>
<h2>Usage</h2>
<p>Check for metadata on a device </p>
<p> <code>pvck</code> <i>PV</i> &#8230; </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Check and print LVM headers and metadata on a device </p>
<p> <code>pvck</code> <code>&#8211;dump</code> <i>String</i> <i>PV</i> </p>
<dl>
<dd>[ <code>-f</code>|<code>&#8211;file</code> <i>String</i> ]<br />
 [ <code>&#8211;settings</code> <i>String</i> ]<br />
 [ <code>&#8211;[pv]metadatacopies</code> <code>0</code>|<code>1</code>|<code>2</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Repair LVM headers or metadata on a device </p>
<p> <code>pvck</code> <code>&#8211;repairtype</code> <code>pv_header</code>|<code>metadata</code>|<code>label_header</code> <i>PV</i> </p>
<dl>
<dd>[ <code>-f</code>|<code>&#8211;file</code> <i>String</i> ]<br />
 [ <code>&#8211;settings</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Repair LVM headers and metadata on a device </p>
<p> <code>pvck</code> <code>&#8211;repair</code> <code>-f</code>|<code>&#8211;file</code> <i>String</i> <i>PV</i> </p>
<dl>
<dd>[ <code>&#8211;settings</code> <i>String</i> ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Common options for command:</p>
<dl>
<dd>[ <code>&#8211;labelsector</code> <i>Number</i> ]</dl>
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
<dt> <code>&#8211;commandprofile</code> <i>String</i></p>
<dd>
<dd>The command profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;config</code> <i>String</i></p>
<dd>
<dd>Config settings for the command. These override lvm.conf settings. The String arg uses the same format as lvm.conf, or may use section/field syntax. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about config.</p>
<dt> <code>-d</code>|<code>&#8211;debug</code> &#8230;</p>
<dd>
<dd>Set debug level. Repeat from 1 to 6 times to increase the detail of messages sent to the log file and/or syslog (if configured).</p>
<dt> <code>&#8211;driverloaded</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>If set to no, the command will not attempt to use device-mapper. For testing and debugging.</p>
<dt> <code>&#8211;dump</code> <i>String</i></p>
<dd>
<dd>Dump headers and metadata from a PV for debugging and repair. Option values include: <code>headers</code> to print and check LVM headers, <code>metadata</code> to print or save the current text metadata, <code>metadata_all</code> to list or save all versions of metadata, <code>metadata_search</code> to list or save all versions of metadata, searching standard locations in case of damaged headers, <code>metadata_area</code> to save an entire text metadata area to a file.</p>
<dt> <code>-f</code>|<code>&#8211;file</code> <i>String</i></p>
<dd>
<dd>Metadata file to read or write.</p>
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
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>&#8211;[pv]metadatacopies</code> <code>0</code>|<code>1</code>|<code>2</code></p>
<dd>
<dd>The number of metadata areas to set aside on a PV for storing VG metadata. When 2, one copy of the VG metadata is stored at the front of the PV and a second copy is stored at the end. When 1, one copy of the VG metadata is stored at the front of the PV. When 0, no copies of the VG metadata are stored on the given PV. This may be useful in VGs containing many PVs (this places limitations on the ability to use vgsplit later.)</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>&#8211;repair</code></p>
<dd>
<dd>Repair headers and metadata on a PV.</p>
<dt> <code>&#8211;repairtype</code> <code>pv_header</code>|<code>metadata</code>|<code>label_header</code></p>
<dd>
<dd>Repair headers and metadata on a PV. See command description.</p>
<dt> <code>&#8211;settings</code> <i>String</i></p>
<dd>
<dd>Specifies command specific settings in &quot;Key = Value&quot; form. Repeat this option to specify multiple values.</p>
<dt> <code>-t</code>|<code>&#8211;test</code></p>
<dd>
<dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</p>
<dt> <code>-v</code>|<code>&#8211;verbose</code> &#8230;</p>
<dd>
<dd>Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.</p>
<dt> <code>&#8211;version</code></p>
<dd>
<dd>Display version information.</p>
<dt> <code>-y</code>|<code>&#8211;yes</code></p>
<dd>
<dd>Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution. (For automatic no, see -qq.)</dl>
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
<p>If the partition table is corrupted or lost on /dev/sda, and you suspect there was an LVM partition at approximately 100 MiB, then this area of the disk can be scanned using the <code>&#8211;labelsector</code> parameter with a value of 204800 (100 * 1024 * 1024 / 512 = 204800).<br />
 <code>pvck &#8211;labelsector 204800 /dev/sda</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
