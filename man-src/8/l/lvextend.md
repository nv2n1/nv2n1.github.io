---
title: "lvextend(8)"
name: "lvextend"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvextend/"
description: "lvextend – Add space to a logical volume"
---

<p>lvextend &#8211; Add space to a logical volume</p>
<h2>Synopsis</h2>
<p><code>lvextend</code> <i>option_args</i> <i>position_args</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>position_args</i>&nbsp;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;alloc</code>&nbsp;<code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code> </p>
<p>&nbsp;<code>-A</code>|<code>&#8211;autobackup</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;commandprofile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;config</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-d</code>|<code>&#8211;debug</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;driverloaded</code>&nbsp;<code>y</code>|<code>n</code> </p>
<p>&nbsp;<code>-l</code>|<code>&#8211;extents</code>&nbsp;[<code>+</code>]<i>Number</i>[PERCENT] </p>
<p>&nbsp;<code>-f</code>|<code>&#8211;force</code> </p>
<p>&nbsp;<code>-h</code>|<code>&#8211;help</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;lockopt</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;longhelp</code> </p>
<p>&nbsp;<code>-m</code>|<code>&#8211;mirrors</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<code>-n</code>|<code>&#8211;nofsck</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;nolocking</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;nosync</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;noudevsync</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;poolmetadatasize</code>&nbsp;[<code>+</code>]<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;profile</code>&nbsp;<i>String</i> </p>
<p>&nbsp;<code>-q</code>|<code>&#8211;quiet</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;reportformat</code>&nbsp;<code>basic</code>|<code>json</code> </p>
<p>&nbsp;<code>-r</code>|<code>&#8211;resizefs</code> </p>
<p>&nbsp;<code>-L</code>|<code>&#8211;size</code>&nbsp;[<code>+</code>]<i>Size</i>[m|UNIT] </p>
<p>&nbsp;<code>-i</code>|<code>&#8211;stripes</code>&nbsp;<i>Number</i> </p>
<p>&nbsp;<code>-I</code>|<code>&#8211;stripesize</code>&nbsp;<i>Size</i>[k|UNIT] </p>
<p>&nbsp;<code>-t</code>|<code>&#8211;test</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;type</code>&nbsp;<code>linear</code>|<code>striped</code>|<code>snapshot</code>|<code>mirror</code>|<code>raid</code>|<code>thin</code>|<code>cache</code>|<code>vdo</code>|<code>thin-pool</code>|<code>cache-pool</code>|<code>vdo-pool</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;usepolicies</code> </p>
<p>&nbsp;<code>-v</code>|<code>&#8211;verbose</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;version</code> </p>
<p>&nbsp;<code>-y</code>|<code>&#8211;yes</code></p>
<h2>Description</h2>
<p>lvextend extends the size of an LV. This requires allocating logical extents from the VG&#8217;s free physical extents. If the extension adds a new LV segment, the new segment will use the existing segment type of the LV. </p>
<p> Extending a copy-on-write snapshot LV adds space for COW blocks. </p>
<p> Use <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) to change the number of data images in a RAID or mirrored LV. </p>
<p> In the usage section below, <code>&#8211;size</code> <i>Size</i> can be replaced with <code>&#8211;extents</code> <i>Number</i>. See both descriptions the options section.</p>
<h2>Usage</h2>
<p>Extend an LV by a specified size. </p>
<p> <code>lvextend</code> <code>-L</code>|<code>&#8211;size</code> [<code>+</code>]<i>Size</i>[m|UNIT] <i>LV</i> </p>
<dl>
<dd>[ <code>-l</code>|<code>&#8211;extents</code> [<code>+</code>]<i>Number</i>[PERCENT] ]<br />
 [ <code>-r</code>|<code>&#8211;resizefs</code> ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ <code>&#8211;poolmetadatasize</code> [<code>+</code>]<i>Size</i>[m|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Extend an LV by specified PV extents. </p>
<p> <code>lvextend</code> <i>LV</i> <i>PV</i> &#8230; </p>
<dl>
<dd>[ <code>-r</code>|<code>&#8211;resizefs</code> ]<br />
 [ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<p> &#8211; </p>
<p> Extend a pool metadata SubLV by a specified size. </p>
<p> <code>lvextend</code> <code>&#8211;poolmetadatasize</code> [<code>+</code>]<i>Size</i>[m|UNIT] <i>LV</i><i>_thinpool</i> </p>
<dl>
<dd>[ <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i> ]<br />
 [ <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT] ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Extend an LV according to a predefined policy. </p>
<p> <code>lvextend</code> <code>&#8211;usepolicies</code> <i>LV</i><i>_snapshot_thinpool</i> </p>
<dl>
<dd>[ <code>-r</code>|<code>&#8211;resizefs</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>PV</i> &#8230; ]</dl>
<p> &#8211; </p>
<p> Common options for command:</p>
<dl>
<dd>[ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>-m</code>|<code>&#8211;mirrors</code> <i>Number</i> ]<br />
 [ <code>-n</code>|<code>&#8211;nofsck</code> ]<br />
 [ <code>&#8211;alloc</code> <code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code> ]<br />
 [ <code>&#8211;nosync</code> ]<br />
 [ <code>&#8211;noudevsync</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
 [ <code>&#8211;type</code> <code>linear</code>|<code>striped</code>|<code>snapshot</code>|<code>mirror</code>|<code>raid</code>|<code>thin</code>|<code>cache</code>|<code>vdo</code>|<code>thin-pool</code>|<code>cache-pool</code>|<code>vdo-pool</code> ]</dl>
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
<dt> <code>&#8211;alloc</code> <code>contiguous</code>|<code>cling</code>|<code>cling_by_tags</code>|<code>normal</code>|<code>anywhere</code>|<code>inherit</code></p>
<dd>
<dd>Determines the allocation policy when a command needs to allocate Physical Extents (PEs) from the VG. Each VG and LV has an allocation policy which can be changed with vgchange/lvchange, or overriden on the command line. <code>normal</code> applies common sense rules such as not placing parallel stripes on the same PV. <code>inherit</code> applies the VG policy to an LV. <code>contiguous</code> requires new PEs be placed adjacent to existing PEs. <code>cling</code> places new PEs on the same PV as existing PEs in the same stripe of the LV. If there are sufficient PEs for an allocation, but normal does not use them, <code>anywhere</code> will use them even if it reduces performance, e.g. by placing two stripes on the same PV. Optional positional PV args on the command line can also be used to limit which PVs the command will use for allocation. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for more information about allocation.</p>
<dt> <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>Specifies if metadata should be backed up automatically after a change. Enabling this is strongly advised! See <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) for more information.</p>
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
<dt> <code>-l</code>|<code>&#8211;extents</code> [<code>+</code>]<i>Number</i>[PERCENT]</p>
<dd>
<dd>Specifies the new size of the LV in logical extents. The &#8211;size and &#8211;extents options are alternate methods of specifying size. The total number of physical extents used will be greater when redundant data is needed for RAID levels. An alternate syntax allows the size to be determined indirectly as a percentage of the size of a related VG, LV, or set of PVs. The suffix <code>%VG</code> denotes the total size of the VG, the suffix <code>%FREE</code> the remaining free space in the VG, and the suffix <code>%PVS</code> the free space in the specified PVs. For a snapshot, the size can be expressed as a percentage of the total size of the origin LV with the suffix <code>%ORIGIN</code> (<code>100%ORIGIN</code> provides space for the whole origin). When expressed as a percentage, the size defines an upper limit for the number of logical extents in the new LV. The precise number of logical extents in the new LV is not determined until the command has completed. When the plus <code>+</code> or minus <code>&#8211;</code> prefix is used, the value is not an absolute size, but is relative and added or subtracted from the current size.</p>
<dt> <code>-f</code>|<code>&#8211;force</code> &#8230;</p>
<dd>
<dd>Override various checks, confirmations and protections. Use with extreme caution.</p>
<dt> <code>-h</code>|<code>&#8211;help</code></p>
<dd>
<dd>Display help text.</p>
<dt> <code>&#8211;lockopt</code> <i>String</i></p>
<dd>
<dd>Used to pass options for special cases to lvmlockd. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</p>
<dt> <code>&#8211;longhelp</code></p>
<dd>
<dd>Display long help text.</p>
<dt> <code>-m</code>|<code>&#8211;mirrors</code> <i>Number</i></p>
<dd>
<dd>Not used.</p>
<dt> <code>-n</code>|<code>&#8211;nofsck</code></p>
<dd>
<dd>Do not perform fsck before resizing filesystem when filesystem requires it. You may need to use &#8211;force to proceed with this option.</p>
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;nosync</code></p>
<dd>
<dd>Causes the creation of mirror, raid1, raid4, raid5 and raid10 to skip the initial synchronization. In case of mirror, raid1 and raid10, any data written afterwards will be mirrored, but the original contents will not be copied. In case of raid4 and raid5, no parity blocks will be written, though any data written afterwards will cause parity blocks to be stored. This is useful for skipping a potentially long and resource intensive initial sync of an empty mirror/raid1/raid4/raid5 and raid10 LV. This option is not valid for raid6, because raid6 relies on proper parity (P and Q Syndromes) being created during initial synchronization in order to reconstruct proper user date in case of device failures. raid0 and raid0_meta do not provide any data copies or parity support and thus do not support initial synchronization.</p>
<dt> <code>&#8211;noudevsync</code></p>
<dd>
<dd>Disables udev synchronisation. The process will not wait for notification from udev. It will continue irrespective of any possible udev processing in the background. Only use this if udev is not running or has rules that ignore the devices LVM creates.</p>
<dt> <code>&#8211;poolmetadatasize</code> [<code>+</code>]<i>Size</i>[m|UNIT]</p>
<dd>
<dd>Specifies the new size of the pool metadata LV. The plus prefix <code>+</code> can be used, in which case the value is added to the current size.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code></p>
<dd>
<dd>Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf. <code>basic</code> is the original format with columns and rows. If there is more than one report per command, each report is prefixed with the report name for identification. <code>json</code> produces report output in JSON format. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information.</p>
<dt> <code>-r</code>|<code>&#8211;resizefs</code></p>
<dd>
<dd>Resize underlying filesystem together with the LV using <a href="/docs/linux/man/8-fsadm/">fsadm</a>(8).</p>
<dt> <code>-L</code>|<code>&#8211;size</code> [<code>+</code>]<i>Size</i>[m|UNIT]</p>
<dd>
<dd>Specifies the new size of the LV. The &#8211;size and &#8211;extents options are alternate methods of specifying size. The total number of physical extents used will be greater when redundant data is needed for RAID levels. When the plus <code>+</code> or minus <code>&#8211;</code> prefix is used, the value is not an absolute size, but is relative and added or subtracted from the current size.</p>
<dt> <code>-i</code>|<code>&#8211;stripes</code> <i>Number</i></p>
<dd>
<dd>Specifies the number of stripes in a striped LV. This is the number of PVs (devices) that a striped LV is spread across. Data that appears sequential in the LV is spread across multiple devices in units of the stripe size (see &#8211;stripesize). This does not change existing allocated space, but only applies to space being allocated by the command. When creating a RAID 4/5/6 LV, this number does not include the extra devices that are required for parity. The largest number depends on the RAID type (raid0: 64, raid10: 32, raid4/5: 63, raid6: 62), and when unspecified, the default depends on the RAID type (raid0: 2, raid10: 2, raid4/5: 3, raid6: 5.) To stripe a new raid LV across all PVs by default, see lvm.conf allocation/raid_stripe_all_devices.</p>
<dt> <code>-I</code>|<code>&#8211;stripesize</code> <i>Size</i>[k|UNIT]</p>
<dd>
<dd>The amount of data that is written to one device before moving to the next in a striped LV.</p>
<dt> <code>-t</code>|<code>&#8211;test</code></p>
<dd>
<dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</p>
<dt> <code>&#8211;type</code> <code>linear</code>|<code>striped</code>|<code>snapshot</code>|<code>mirror</code>|<code>raid</code>|<code>thin</code>|<code>cache</code>|<code>vdo</code>|<code>thin-pool</code>|<code>cache-pool</code>|<code>vdo-pool</code></p>
<dd>
<dd>The LV type, also known as &quot;segment type&quot; or &quot;segtype&quot;. See usage descriptions for the specific ways to use these types. For more information about redundancy and performance (<code>raid</code>&lt;N&gt;, <code>mirror</code>, <code>striped</code>, <code>linear</code>) see <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7). For thin provisioning (<code>thin</code>, <code>thin-pool</code>) see <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7). For performance caching (<code>cache</code>, <code>cache-pool</code>) see <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7). For copy-on-write snapshots (<code>snapshot</code>) see usage definitions. For VDO (<code>vdo</code>) see <code><a href="/docs/linux/man/7-lvmvdo/">lvmvdo</a></code>(7). Several commands omit an explicit type option because the type is inferred from other options or shortcuts (e.g. &#8211;stripes, &#8211;mirrors, &#8211;snapshot, &#8211;virtualsize, &#8211;thin, &#8211;cache, &#8211;vdo). Use inferred types with care because it can lead to unexpected results.</p>
<dt> <code>&#8211;usepolicies</code></p>
<dd>
<dd>Perform an operation according to the policy configured in lvm.conf or a profile.</p>
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
<dt> <i>LV</i></p>
<dd>
<dd>Logical Volume name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names. An LV positional arg generally includes the VG name and LV name, e.g. VG/LV. LV followed by _&lt;type&gt; indicates that an LV of the given type is required. (raid represents raid&lt;N&gt; type)</p>
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
<p>Extend the size of an LV by 54MiB, using a specific PV.<br />
 <code>lvextend -L +54 vg01/lvol10 /dev/sdk3</code> </p>
<p> Extend the size of an LV by the amount of free space on PV /dev/sdk3. This is equivalent to specifying &quot;-l +100%PVS&quot; on the command line.<br />
 <code>lvextend vg01/lvol01 /dev/sdk3</code> </p>
<p> Extend an LV by 16MiB using specific physical extents.<br />
 <code>lvextend -L+16m vg01/lvol01 /dev/sda:8-9 /dev/sdb:8-9</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
