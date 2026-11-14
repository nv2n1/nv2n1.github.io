---
title: "vgrename(8)"
name: "vgrename"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vgrename/"
description: "vgrename – Rename a volume group"
---

<p>vgrename &#8211; Rename a volume group</p>
<h2>Synopsis</h2>
<p><code>vgrename</code> <i>position_args</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;]</p>
<h2>Description</h2>
<p>vgrename renames a VG. </p>
<p> All VGs visible to a system need to have different names, otherwise many LVM commands will refuse to run or give warning messages. VGs with the same name can occur when disks are moved between machines, or filters are changed. If a newly connected disk has a VG with the same name as the VG containing the root filesystem, the machine may not boot correctly. When two VGs have the same name, the VG UUID can be used in place of the source VG name.</p>
<h2>Usage</h2>
<p>Rename a VG. </p>
<p> <code>vgrename</code> <i>VG</i> <i>VG</i><i>_new</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> Rename a VG by specifying the VG UUID. </p>
<p> <code>vgrename</code> <i>String</i> <i>VG</i><i>_new</i> </p>
<dl>
<dd>[ COMMON_OPTIONS ]</dl>
<p> Common options for command:</p>
<dl>
<dd>[ <code>-A</code>|<code>&#8211;autobackup</code> <code>y</code>|<code>n</code> ]<br />
 [ <code>-f</code>|<code>&#8211;force</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]</dl>
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
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code></p>
<dd>
<dd>Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf. <code>basic</code> is the original format with columns and rows. If there is more than one report per command, each report is prefixed with the report name for identification. <code>json</code> produces report output in JSON format. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information.</p>
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
<dt> <i>String</i></p>
<dd>
<dd>See the option description for information about the string content.</p>
<dt> <i>Size</i>[UNIT]</p>
<dd>
<dd>Size is an input number that accepts an optional unit. Input units are always treated as base two values, regardless of capitalization, e.g. &#8216;k&#8217; and &#8216;K&#8217; both refer to 1024. The default input unit is specified by letter, followed by |UNIT. UNIT represents other possible input units: <code>bBsSkKmMgGtTpPeE</code>. b|B is bytes, s|S is sectors of 512 bytes, k|K is kilobytes, m|M is megabytes, g|G is gigabytes, t|T is terabytes, p|P is petabytes, e|E is exabytes. (This should not be confused with the output control &#8211;units, where capital letters mean multiple of 1000.)</dl>
<h2>Environment Variables</h2>
<p>See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about environment variables used by lvm. For example, LVM_VG_NAME can generally be substituted for a required VG parameter.</p>
<h2>Examples</h2>
<p>Rename VG &quot;vg02&quot; to &quot;myvg&quot;:<br />
 <code>vgrename vg02 myvg</code> </p>
<p> Rename the VG with the specified UUID to &quot;myvg&quot;.<br />
 <code>vgrename Zvlifi-Ep3t-e0Ng-U42h-o0ye-KHu1-nl7Ns4 myvg</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
