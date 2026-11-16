---
title: "lvscan(8)"
name: "lvscan"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvscan/"
description: "lvscan – List all logical volumes in all volume groups"
---

<p>lvscan &#8211; List all logical volumes in all volume groups</p>
<h2>Synopsis</h2>
<p><code>lvscan</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;]</p>
<h2>Description</h2>
<p>lvscan scans all VGs or all supported LVM block devices in the system for LVs. The output consists of one line for each LV indicating whether or not it is active, a snapshot or origin, the size of the device and its allocation policy. Use <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) or <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) to obtain more comprehensive information about LVs.</p>
<h2>Usage</h2>
<p><code>lvscan</code> </p>
<dl>
<dd>[ <code>-a</code>|<code>&#8211;all</code> ]<br />
 [ <code>-b</code>|<code>&#8211;blockdevice</code> ]<br />
 [ <code>&#8211;ignorelockingfailure</code> ]<br />
 [ <code>&#8211;readonly</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
 [ COMMON_OPTIONS ]</dd></dl>
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
 [ <code>&#8211;version</code> ]</dd></dl>
<h2>Options</h2>
<dl>
<dt> <code>-a</code>|<code>&#8211;all</code></dt>
<dd>
</dd><dd>Show information about internal LVs. These are components of normal LVs, such as mirrors, which are not independently accessible, e.g. not mountable.</dd>
<dt> <code>-b</code>|<code>&#8211;blockdevice</code></dt>
<dd>
</dd><dd>No longer used.</dd>
<dt> <code>&#8211;commandprofile</code> <i>String</i></dt>
<dd>
</dd><dd>The command profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</dd>
<dt> <code>&#8211;config</code> <i>String</i></dt>
<dd>
</dd><dd>Config settings for the command. These override lvm.conf settings. The String arg uses the same format as lvm.conf, or may use section/field syntax. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about config.</dd>
<dt> <code>-d</code>|<code>&#8211;debug</code> &#8230;</dt>
<dd>
</dd><dd>Set debug level. Repeat from 1 to 6 times to increase the detail of messages sent to the log file and/or syslog (if configured).</dd>
<dt> <code>&#8211;driverloaded</code> <code>y</code>|<code>n</code></dt>
<dd>
</dd><dd>If set to no, the command will not attempt to use device-mapper. For testing and debugging.</dd>
<dt> <code>-h</code>|<code>&#8211;help</code></dt>
<dd>
</dd><dd>Display help text.</dd>
<dt> <code>&#8211;ignorelockingfailure</code></dt>
<dd>
</dd><dd>Allows a command to continue with read-only metadata operations after locking failures.</dd>
<dt> <code>&#8211;lockopt</code> <i>String</i></dt>
<dd>
</dd><dd>Used to pass options for special cases to lvmlockd. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</dd>
<dt> <code>&#8211;longhelp</code></dt>
<dd>
</dd><dd>Display long help text.</dd>
<dt> <code>&#8211;nolocking</code></dt>
<dd>
</dd><dd>Disable locking.</dd>
<dt> <code>&#8211;profile</code> <i>String</i></dt>
<dd>
</dd><dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</dd>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</dt>
<dd>
</dd><dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</dd>
<dt> <code>&#8211;readonly</code></dt>
<dd>
</dd><dd>Run the command in a special read-only mode which will read on-disk metadata without needing to take any locks. This can be used to peek inside metadata used by a virtual machine image while the virtual machine is running. No attempt will be made to communicate with the device-mapper kernel driver, so this option is unable to report whether or not LVs are actually in use.</dd>
<dt> <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code></dt>
<dd>
</dd><dd>Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf. <code>basic</code> is the original format with columns and rows. If there is more than one report per command, each report is prefixed with the report name for identification. <code>json</code> produces report output in JSON format. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information.</dd>
<dt> <code>-t</code>|<code>&#8211;test</code></dt>
<dd>
</dd><dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</dd>
<dt> <code>-v</code>|<code>&#8211;verbose</code> &#8230;</dt>
<dd>
</dd><dd>Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.</dd>
<dt> <code>&#8211;version</code></dt>
<dd>
</dd><dd>Display version information.</dd>
<dt> <code>-y</code>|<code>&#8211;yes</code></dt>
<dd>
</dd><dd>Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution. (For automatic no, see -qq.)</dd></dl>
<h2>Variables</h2>
<dl>
<dt> <i>String</i></dt>
<dd>
</dd><dd>See the option description for information about the string content.</dd>
<dt> <i>Size</i>[UNIT]</dt>
<dd>
</dd><dd>Size is an input number that accepts an optional unit. Input units are always treated as base two values, regardless of capitalization, e.g. &#8216;k&#8217; and &#8216;K&#8217; both refer to 1024. The default input unit is specified by letter, followed by |UNIT. UNIT represents other possible input units: <code>bBsSkKmMgGtTpPeE</code>. b|B is bytes, s|S is sectors of 512 bytes, k|K is kilobytes, m|M is megabytes, g|G is gigabytes, t|T is terabytes, p|P is petabytes, e|E is exabytes. (This should not be confused with the output control &#8211;units, where capital letters mean multiple of 1000.)</dd></dl>
<h2>Environment Variables</h2>
<p>See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about environment variables used by lvm. For example, LVM_VG_NAME can generally be substituted for a required VG parameter.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code>lvmdbusd</code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
