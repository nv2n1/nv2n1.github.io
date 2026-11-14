---
title: "lvremove(8)"
name: "lvremove"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvremove/"
description: "lvremove – Remove logical volume(s) from the system"
---

<p>lvremove &#8211; Remove logical volume(s) from the system</p>
<h2>Synopsis</h2>
<p><code>lvremove</code> <i>position_args</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;]</p>
<h2>Description</h2>
<p>lvremove removes one or more LVs. For standard LVs, this returns the logical extents that were used by the LV to the VG for use by other LVs. </p>
<p> Confirmation will be requested before deactivating any active LV prior to removal. LVs cannot be deactivated or removed while they are open (e.g. if they contain a mounted filesystem). Removing an origin LV will also remove all dependent snapshots. </p>
<p> When a single force option is used, LVs are removed without confirmation, and the command will try to deactivate unused LVs. </p>
<p> To remove damaged LVs, two force options may be required (<code>-ff</code>). </p>
<p> <code>Historical LVs</code> </p>
<p> If the configuration setting <code>metadata/record_lvs_history</code> is enabled and the LV being removed forms part of the history of at least one LV that is still present, then a simplified representation of the LV will be retained. This includes the time of removal (<code>lv_time_removed</code> reporting field), creation time (<code>lv_time</code>), name (<code>lv_name</code>), LV uuid (<code>lv_uuid</code>) and VG name (<code>vg_name</code>). This allows later reporting to see the ancestry chain of thin snapshot volumes, even after some intermediate LVs have been removed. The names of such historical LVs acquire a hyphen as a prefix (e.g. &#8216;-lvol1&#8217;) and cannot be reactivated. Use lvremove a second time, with the hyphen, to remove the record of the former LV completely.</p>
<h2>Usage</h2>
<p><code>lvremove</code> <i>VG</i>|<i>LV</i>|<i>Tag</i>|<i>Select</i> &#8230; </p>
<dl>
<dd>[ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ <code>&#8211;nohistory</code> ]<br />
 [ <code>&#8211;noudevsync</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
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
<dt> <code>&#8211;nohistory</code></p>
<dd>
<dd>Do not record history of LVs being removed. This has no effect unless the configuration setting metadata/record_lvs_history is enabled.</p>
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;noudevsync</code></p>
<dd>
<dd>Disables udev synchronisation. The process will not wait for notification from udev. It will continue irrespective of any possible udev processing in the background. Only use this if udev is not running or has rules that ignore the devices LVM creates.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code></p>
<dd>
<dd>Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf. <code>basic</code> is the original format with columns and rows. If there is more than one report per command, each report is prefixed with the report name for identification. <code>json</code> produces report output in JSON format. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information.</p>
<dt> <code>-S</code>|<code>&#8211;select</code> <i>String</i></p>
<dd>
<dd>Select objects for processing and reporting based on specified criteria. The criteria syntax is described by <code>&#8211;select help</code> and <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7). For reporting commands, one row is displayed for each object matching the criteria. See <code>&#8211;options help</code> for selectable object fields. Rows can be displayed with an additional &quot;selected&quot; field (-o selected) showing 1 if the row matches the selection and 0 otherwise. For non-reporting commands which process LVM entities, the selection is used to choose items to process.</p>
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
<dt> <i>VG</i></p>
<dd>
<dd>Volume Group name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names.</p>
<dt> <i>LV</i></p>
<dd>
<dd>Logical Volume name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for valid names. An LV positional arg generally includes the VG name and LV name, e.g. VG/LV.</p>
<dt> <i>Tag</i></p>
<dd>
<dd>Tag name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about tag names and using tags in place of a VG, LV or PV.</p>
<dt> <i>Select</i></p>
<dd>
<dd>Select indicates that a required positional parameter can be omitted if the <code>&#8211;select</code> option is used. No arg appears in this position.</p>
<dt> <i>String</i></p>
<dd>
<dd>See the option description for information about the string content.</p>
<dt> <i>Size</i>[UNIT]</p>
<dd>
<dd>Size is an input number that accepts an optional unit. Input units are always treated as base two values, regardless of capitalization, e.g. &#8216;k&#8217; and &#8216;K&#8217; both refer to 1024. The default input unit is specified by letter, followed by |UNIT. UNIT represents other possible input units: <code>bBsSkKmMgGtTpPeE</code>. b|B is bytes, s|S is sectors of 512 bytes, k|K is kilobytes, m|M is megabytes, g|G is gigabytes, t|T is terabytes, p|P is petabytes, e|E is exabytes. (This should not be confused with the output control &#8211;units, where capital letters mean multiple of 1000.)</dl>
<h2>Environment Variables</h2>
<p>See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about environment variables used by lvm. For example, LVM_VG_NAME can generally be substituted for a required VG parameter.</p>
<h2>Examples</h2>
<p>Remove an active LV without asking for confirmation.<br />
 <code>lvremove -f vg00/lvol1</code> </p>
<p> Remove all LVs the specified VG.<br />
 <code>lvremove vg00</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
