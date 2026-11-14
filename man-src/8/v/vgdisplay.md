---
title: "vgdisplay(8)"
name: "vgdisplay"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vgdisplay/"
description: "vgdisplay – Display volume group information"
---

<p>vgdisplay &#8211; Display volume group information</p>
<h2>Synopsis</h2>
<p><code>vgdisplay</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>position_args</i>&nbsp;]</p>
<h2>Description</h2>
<p>vgdisplay shows the attributes of VGs, and the associated PVs and LVs. </p>
<p> <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) is a preferred alternative that shows the same information and more, using a more compact and configurable output format.</p>
<h2>Usage</h2>
<p><code>vgdisplay</code> </p>
<dl>
<dd>[ <code>-A</code>|<code>&#8211;activevolumegroups</code> ]<br />
 [ <code>-c</code>|<code>&#8211;colon</code> ]<br />
 [ <code>-C</code>|<code>&#8211;columns</code> ]<br />
 [ <code>-o</code>|<code>&#8211;options</code> <i>String</i> ]<br />
 [ <code>-S</code>|<code>&#8211;select</code> <i>String</i> ]<br />
 [ <code>-s</code>|<code>&#8211;short</code> ]<br />
 [ <code>-O</code>|<code>&#8211;sort</code> <i>String</i> ]<br />
 [ <code>&#8211;aligned</code> ]<br />
 [ <code>&#8211;binary</code> ]<br />
 [ <code>&#8211;configreport</code> <code>log</code>|<code>vg</code>|<code>lv</code>|<code>pv</code>|<code>pvseg</code>|<code>seg</code> ]<br />
 [ <code>&#8211;foreign</code> ]<br />
 [ <code>&#8211;ignorelockingfailure</code> ]<br />
 [ <code>&#8211;logonly</code> ]<br />
 [ <code>&#8211;noheadings</code> ]<br />
 [ <code>&#8211;nosuffix</code> ]<br />
 [ <code>&#8211;readonly</code> ]<br />
 [ <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code> ]<br />
 [ <code>&#8211;shared</code> ]<br />
 [ <code>&#8211;separator</code> <i>String</i> ]<br />
 [ <code>&#8211;unbuffered</code> ]<br />
 [ <code>&#8211;units</code> <code>r</code>|<code>R</code>|<code>h</code>|<code>H</code>|<code>b</code>|<code>B</code>|<code>s</code>|<code>S</code>|<code>k</code>|<code>K</code>|<code>m</code>|<code>M</code>|<code>g</code>|<code>G</code>|<code>t</code>|<code>T</code>|<code>p</code>|<code>P</code>|<code>e</code>|<code>E</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>VG</i>|<i>Tag</i> &#8230; ]</dl>
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
<dt> <code>-A</code>|<code>&#8211;activevolumegroups</code></p>
<dd>
<dd>Only select active VGs. The VG is considered active if at least one of its LVs is active.</p>
<dt> <code>&#8211;aligned</code></p>
<dd>
<dd>Use with &#8211;separator to align the output columns</p>
<dt> <code>&#8211;binary</code></p>
<dd>
<dd>Use binary values &quot;0&quot; or &quot;1&quot; instead of descriptive literal values for columns that have exactly two valid values to report (not counting the &quot;unknown&quot; value which denotes that the value could not be determined).</p>
<dt> <code>-c</code>|<code>&#8211;colon</code></p>
<dd>
<dd>Generate colon separated output for easier parsing in scripts or programs. Also see <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) which provides considerably more control over the output.</p>
<dt> <code>-C</code>|<code>&#8211;columns</code></p>
<dd>
<dd>Display output in columns, the equivalent of <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8). Options listed are the same as options given in <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8).</p>
<dt> <code>&#8211;commandprofile</code> <i>String</i></p>
<dd>
<dd>The command profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;config</code> <i>String</i></p>
<dd>
<dd>Config settings for the command. These override lvm.conf settings. The String arg uses the same format as lvm.conf, or may use section/field syntax. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about config.</p>
<dt> <code>&#8211;configreport</code> <code>log</code>|<code>vg</code>|<code>lv</code>|<code>pv</code>|<code>pvseg</code>|<code>seg</code></p>
<dd>
<dd>See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7).</p>
<dt> <code>-d</code>|<code>&#8211;debug</code> &#8230;</p>
<dd>
<dd>Set debug level. Repeat from 1 to 6 times to increase the detail of messages sent to the log file and/or syslog (if configured).</p>
<dt> <code>&#8211;driverloaded</code> <code>y</code>|<code>n</code></p>
<dd>
<dd>If set to no, the command will not attempt to use device-mapper. For testing and debugging.</p>
<dt> <code>&#8211;foreign</code></p>
<dd>
<dd>Report/display foreign VGs that would otherwise be skipped. See <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) for more information about foreign VGs.</p>
<dt> <code>-h</code>|<code>&#8211;help</code></p>
<dd>
<dd>Display help text.</p>
<dt> <code>&#8211;ignorelockingfailure</code></p>
<dd>
<dd>Allows a command to continue with read-only metadata operations after locking failures.</p>
<dt> <code>&#8211;lockopt</code> <i>String</i></p>
<dd>
<dd>Used to pass options for special cases to lvmlockd. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</p>
<dt> <code>&#8211;logonly</code></p>
<dd>
<dd>Suppress command report and display only log report.</p>
<dt> <code>&#8211;longhelp</code></p>
<dd>
<dd>Display long help text.</p>
<dt> <code>&#8211;noheadings</code></p>
<dd>
<dd>Suppress the headings line that is normally the first line of output. Useful if grepping the output.</p>
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;nosuffix</code></p>
<dd>
<dd>Suppress the suffix on output sizes. Use with &#8211;units (except h and H) if processing the output.</p>
<dt> <code>-o</code>|<code>&#8211;options</code> <i>String</i></p>
<dd>
<dd>Comma-separated, ordered list of fields to display in columns. String arg syntax is: [+|-|#]Field1[,Field2 &#8230;] The prefix <code>+</code> will append the specified fields to the default fields, <code>&#8211;</code> will remove the specified fields from the default fields, and <code>#</code> will compact specified fields (removing them when empty for all rows.) Use <code>-o help</code> to view the list of all available fields. Use separate lists of fields to add, remove or compact by repeating the -o option: -o+field1,field2 -o-field3,field4 -o#field5. These lists are evaluated from left to right. Use field name <code>lv_all</code> to view all LV fields, <code>vg_all</code> all VG fields, <code>pv_all</code> all PV fields, <code>pvseg_all</code> all PV segment fields, <code>seg_all</code> all LV segment fields, and <code>pvseg_all</code> all PV segment columns. See the lvm.conf report section for more config options. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information about reporting.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>&#8211;readonly</code></p>
<dd>
<dd>Run the command in a special read-only mode which will read on-disk metadata without needing to take any locks. This can be used to peek inside metadata used by a virtual machine image while the virtual machine is running. No attempt will be made to communicate with the device-mapper kernel driver, so this option is unable to report whether or not LVs are actually in use.</p>
<dt> <code>&#8211;reportformat</code> <code>basic</code>|<code>json</code></p>
<dd>
<dd>Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf. <code>basic</code> is the original format with columns and rows. If there is more than one report per command, each report is prefixed with the report name for identification. <code>json</code> produces report output in JSON format. See <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) for more information.</p>
<dt> <code>-S</code>|<code>&#8211;select</code> <i>String</i></p>
<dd>
<dd>Select objects for processing and reporting based on specified criteria. The criteria syntax is described by <code>&#8211;select help</code> and <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7). For reporting commands, one row is displayed for each object matching the criteria. See <code>&#8211;options help</code> for selectable object fields. Rows can be displayed with an additional &quot;selected&quot; field (-o selected) showing 1 if the row matches the selection and 0 otherwise. For non-reporting commands which process LVM entities, the selection is used to choose items to process.</p>
<dt> <code>&#8211;separator</code> <i>String</i></p>
<dd>
<dd>String to use to separate each column. Useful if grepping the output.</p>
<dt> <code>&#8211;shared</code></p>
<dd>
<dd>Report/display shared VGs that would otherwise be skipped when lvmlockd is not being used on the host. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information about shared VGs.</p>
<dt> <code>-s</code>|<code>&#8211;short</code></p>
<dd>
<dd>Give a short listing showing the existence of VGs.</p>
<dt> <code>-O</code>|<code>&#8211;sort</code> <i>String</i></p>
<dd>
<dd>Comma-separated ordered list of columns to sort by. Replaces the default selection. Precede any column with <code>&#8211;</code> for a reverse sort on that column.</p>
<dt> <code>-t</code>|<code>&#8211;test</code></p>
<dd>
<dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</p>
<dt> <code>&#8211;unbuffered</code></p>
<dd>
<dd>Produce output immediately without sorting or aligning the columns properly.</p>
<dt> <code>&#8211;units</code> <code>r</code>|<code>R</code>|<code>h</code>|<code>H</code>|<code>b</code>|<code>B</code>|<code>s</code>|<code>S</code>|<code>k</code>|<code>K</code>|<code>m</code>|<code>M</code>|<code>g</code>|<code>G</code>|<code>t</code>|<code>T</code>|<code>p</code>|<code>P</code>|<code>e</code>|<code>E</code></p>
<dd>
<dd>All sizes are output in these units: human-(r)eadable with &#8216;&lt;&#8216; rounding indicator, (h)uman-readable, (b)ytes, (s)ectors, (k)ilobytes, (m)egabytes, (g)igabytes, (t)erabytes, (p)etabytes, (e)xabytes. Capitalise to use multiples of 1000 (S.I.) instead of 1024. Custom units can be specified, e.g. &#8211;units 3M.</p>
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
<dt> <i>Tag</i></p>
<dd>
<dd>Tag name. See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about tag names and using tags in place of a VG, LV or PV.</p>
<dt> <i>String</i></p>
<dd>
<dd>See the option description for information about the string content.</p>
<dt> <i>Size</i>[UNIT]</p>
<dd>
<dd>Size is an input number that accepts an optional unit. Input units are always treated as base two values, regardless of capitalization, e.g. &#8216;k&#8217; and &#8216;K&#8217; both refer to 1024. The default input unit is specified by letter, followed by |UNIT. UNIT represents other possible input units: <code>bBsSkKmMgGtTpPeE</code>. b|B is bytes, s|S is sectors of 512 bytes, k|K is kilobytes, m|M is megabytes, g|G is gigabytes, t|T is terabytes, p|P is petabytes, e|E is exabytes. (This should not be confused with the output control &#8211;units, where capital letters mean multiple of 1000.)</dl>
<h2>Environment Variables</h2>
<p>See <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for information about environment variables used by lvm. For example, LVM_VG_NAME can generally be substituted for a required VG parameter.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) <code><a href="/docs/linux/man/8-pvchange/">pvchange</a></code>(8) <code><a href="/docs/linux/man/8-pvck/">pvck</a></code>(8) <code><a href="/docs/linux/man/8-pvcreate/">pvcreate</a></code>(8) <code><a href="/docs/linux/man/8-pvdisplay/">pvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-pvmove/">pvmove</a></code>(8) <code><a href="/docs/linux/man/8-pvremove/">pvremove</a></code>(8) <code><a href="/docs/linux/man/8-pvresize/">pvresize</a></code>(8) <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8) <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgbackup/">vgcfgbackup</a></code>(8) <code><a href="/docs/linux/man/8-vgcfgrestore/">vgcfgrestore</a></code>(8) <code><a href="/docs/linux/man/8-vgchange/">vgchange</a></code>(8) <code><a href="/docs/linux/man/8-vgck/">vgck</a></code>(8) <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) <code><a href="/docs/linux/man/8-vgconvert/">vgconvert</a></code>(8) <code><a href="/docs/linux/man/8-vgdisplay/">vgdisplay</a></code>(8) <code><a href="/docs/linux/man/8-vgexport/">vgexport</a></code>(8) <code><a href="/docs/linux/man/8-vgextend/">vgextend</a></code>(8) <code><a href="/docs/linux/man/8-vgimport/">vgimport</a></code>(8) <code><a href="/docs/linux/man/8-vgimportclone/">vgimportclone</a></code>(8) <code><a href="/docs/linux/man/8-vgmerge/">vgmerge</a></code>(8) <code><a href="/docs/linux/man/8-vgmknodes/">vgmknodes</a></code>(8) <code><a href="/docs/linux/man/8-vgreduce/">vgreduce</a></code>(8) <code><a href="/docs/linux/man/8-vgremove/">vgremove</a></code>(8) <code><a href="/docs/linux/man/8-vgrename/">vgrename</a></code>(8) <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8) <code><a href="/docs/linux/man/8-vgscan/">vgscan</a></code>(8) <code><a href="/docs/linux/man/8-vgsplit/">vgsplit</a></code>(8) <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) <code><a href="/docs/linux/man/8-lvchange/">lvchange</a></code>(8) <code><a href="/docs/linux/man/8-lvconvert/">lvconvert</a></code>(8) <code><a href="/docs/linux/man/8-lvdisplay/">lvdisplay</a></code>(8) <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) <code><a href="/docs/linux/man/8-lvreduce/">lvreduce</a></code>(8) <code><a href="/docs/linux/man/8-lvremove/">lvremove</a></code>(8) <code><a href="/docs/linux/man/8-lvrename/">lvrename</a></code>(8) <code><a href="/docs/linux/man/8-lvresize/">lvresize</a></code>(8) <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) <code><a href="/docs/linux/man/8-lvscan/">lvscan</a></code>(8) <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) <code><a href="/docs/linux/man/8-lvm-lvpoll/">lvm-lvpoll</a></code>(8) <code><a href="/docs/linux/man/8-lvm2-activation-generator/">lvm2-activation-generator</a></code>(8) <code><a href="/docs/linux/man/8-blkdeactivate/">blkdeactivate</a></code>(8) <code><a href="/docs/linux/man/8-lvmdump/">lvmdump</a></code>(8) <code><a href="/docs/linux/man/8-dmeventd/">dmeventd</a></code>(8) <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) <code><a href="/docs/linux/man/8-lvmlockctl/">lvmlockctl</a></code>(8) <code><a href="/docs/linux/man/8-cmirrord/">cmirrord</a></code>(8) <code><a href="/docs/linux/man/8-lvmdbusd/">lvmdbusd</a></code>(8) <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7) <code><a href="/docs/linux/man/7-lvmreport/">lvmreport</a></code>(7) <code><a href="/docs/linux/man/7-lvmraid/">lvmraid</a></code>(7) <code><a href="/docs/linux/man/7-lvmthin/">lvmthin</a></code>(7) <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7) </p>
