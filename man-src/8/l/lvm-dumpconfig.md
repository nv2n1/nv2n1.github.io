---
title: "lvm-dumpconfig(8)"
name: "lvm-dumpconfig"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvm-dumpconfig/"
description: "lvmconfig – Display and manipulate configuration information"
---

<p>lvmconfig &#8211; Display and manipulate configuration information</p>
<h2>Synopsis</h2>
<p><code>lvmconfig</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>option_args</i>&nbsp;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&nbsp;<i>position_args</i>&nbsp;]</p>
<h2>Description</h2>
<p>lvmconfig, lvm config, lvm dumpconfig (for compatibility reasons, to be phased out) produce formatted output from the LVM configuration tree. The sources of the configuration data include <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) and command line settings from &#8211;config.</p>
<h2>Usage</h2>
<p><code>lvmconfig</code> </p>
<dl>
<dd>[ <code>-f</code>|<code>&#8211;file</code> <i>String</i> ]<br />
 [ <code>-l</code>|<code>&#8211;list</code> ]<br />
 [ <code>&#8211;atversion</code> <i>String</i> ]<br />
 [ <code>&#8211;typeconfig</code> <code>current</code>|<code>default</code>|<code>diff</code>|<code>full</code>|<code>list</code>|<code>missing</code>|<code>new</code>|<code>profilable</code>|<code>profilable-command</code>|<code>profilable-metadata</code> ]<br />
 [ <code>&#8211;ignoreadvanced</code> ]<br />
 [ <code>&#8211;ignoreunsupported</code> ]<br />
 [ <code>&#8211;ignorelocal</code> ]<br />
 [ <code>&#8211;mergedconfig</code> ]<br />
 [ <code>&#8211;metadataprofile</code> <i>String</i> ]<br />
 [ <code>&#8211;sinceversion</code> <i>String</i> ]<br />
 [ <code>&#8211;showdeprecated</code> ]<br />
 [ <code>&#8211;showunsupported</code> ]<br />
 [ <code>&#8211;validate</code> ]<br />
 [ <code>&#8211;withsummary</code> ]<br />
 [ <code>&#8211;withcomments</code> ]<br />
 [ <code>&#8211;withgeneralpreamble</code> ]<br />
 [ <code>&#8211;withlocalpreamble</code> ]<br />
 [ <code>&#8211;withspaces</code> ]<br />
 [ <code>&#8211;unconfigured</code> ]<br />
 [ <code>&#8211;withversions</code> ]<br />
 [ COMMON_OPTIONS ]</dl>
<dl>
<dd>[ <i>String</i> &#8230; ]</dl>
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
<dt> <code>&#8211;atversion</code> <i>String</i></p>
<dd>
<dd>Specify an LVM version in x.y.z format where x is the major version, the y is the minor version and z is the patchlevel (e.g. 2.2.106). When configuration is displayed, the configuration settings recognized at this LVM version will be considered only. This can be used to display a configuration that a certain LVM version understands and which does not contain any newer settings for which LVM would issue a warning message when checking the configuration.</p>
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
<dt> <code>-f</code>|<code>&#8211;file</code> <i>String</i></p>
<dd>
<dd>Write output to the named file.</p>
<dt> <code>-h</code>|<code>&#8211;help</code></p>
<dd>
<dd>Display help text.</p>
<dt> <code>&#8211;ignoreadvanced</code></p>
<dd>
<dd>Exclude advanced configuration settings from the output.</p>
<dt> <code>&#8211;ignorelocal</code></p>
<dd>
<dd>Ignore the local section. The local section should be defined in the lvmlocal.conf file, and should contain config settings specific to the local host which should not be copied to other hosts.</p>
<dt> <code>&#8211;ignoreunsupported</code></p>
<dd>
<dd>Exclude unsupported configuration settings from the output. These settings are either used for debugging and development purposes only or their support is not yet complete and they are not meant to be used in production. The <code>current</code> and <code>diff</code> types include unsupported settings in their output by default, all the other types ignore unsupported settings.</p>
<dt> <code>-l</code>|<code>&#8211;list</code></p>
<dd>
<dd>List config settings with summarizing comment. This is the same as using options &#8211;typeconfig list &#8211;withsummary.</p>
<dt> <code>&#8211;lockopt</code> <i>String</i></p>
<dd>
<dd>Used to pass options for special cases to lvmlockd. See <code><a href="/docs/linux/man/8-lvmlockd/">lvmlockd</a></code>(8) for more information.</p>
<dt> <code>&#8211;longhelp</code></p>
<dd>
<dd>Display long help text.</p>
<dt> <code>&#8211;mergedconfig</code></p>
<dd>
<dd>When the command is run with &#8211;config and/or &#8211;commandprofile (or using LVM_COMMAND_PROFILE environment variable), &#8211;profile, or &#8211;metadataprofile, merge all the contents of the &quot;config cascade&quot; before displaying it. Without merging, only the configuration at the front of the cascade is displayed. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about config.</p>
<dt> <code>&#8211;metadataprofile</code> <i>String</i></p>
<dd>
<dd>The metadata profile to use for command configuration. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) for more information about profiles.</p>
<dt> <code>&#8211;nolocking</code></p>
<dd>
<dd>Disable locking.</p>
<dt> <code>&#8211;profile</code> <i>String</i></p>
<dd>
<dd>An alias for &#8211;commandprofile or &#8211;metadataprofile, depending on the command.</p>
<dt> <code>-q</code>|<code>&#8211;quiet</code> &#8230;</p>
<dd>
<dd>Suppress output and log messages. Overrides &#8211;debug and &#8211;verbose. Repeat once to also suppress any prompts with answer &#8216;no&#8217;.</p>
<dt> <code>&#8211;showdeprecated</code></p>
<dd>
<dd>Include deprecated configuration settings in the output. These settings are deprecated after a certain version. If a concrete version is specified with &#8211;atversion, deprecated settings are automatically included if the specified version is lower than the version in which the settings were deprecated. The current and diff types include deprecated settings in their output by default, all the other types ignore deprecated settings.</p>
<dt> <code>&#8211;showunsupported</code></p>
<dd>
<dd>Include unsupported configuration settings in the output. These settings are either used for debugging or development purposes only, or their support is not yet complete and they are not meant to be used in production. The current and diff types include unsupported settings in their output by default, all the other types ignore unsupported settings.</p>
<dt> <code>&#8211;sinceversion</code> <i>String</i></p>
<dd>
<dd>Specify an LVM version in x.y.z format where x is the major version, the y is the minor version and z is the patchlevel (e.g. 2.2.106). This option is currently applicable only with &#8211;typeconfig new to display all configuration settings introduced since given version.</p>
<dt> <code>-t</code>|<code>&#8211;test</code></p>
<dd>
<dd>Run in test mode. Commands will not update metadata. This is implemented by disabling all metadata writing but nevertheless returning success to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes has changed but hasn&#8217;t.</p>
<dt> <code>&#8211;typeconfig</code> <code>current</code>|<code>default</code>|<code>diff</code>|<code>full</code>|<code>list</code>|<code>missing</code>|<code>new</code>|<code>profilable</code>|<code>profilable-command</code>|<code>profilable-metadata</code></p>
<dd><code>current</code> prints the config settings that would be applied</p>
<dd>to an lvm command (assuming the command does not override them on the command line.) This includes: settings that have been modified in lvm config files, settings that get their default values from config files, and default settings that have been uncommented in config files. <code>default</code> prints all settings with their default values. Changes made in lvm config files are not reflected in the output. Some settings get their default values internally, and these settings are printed as comments. Other settings get their default values from config files, and these settings are not printed as comments. <code>diff</code> prints only config settings that have been modified from their default values in config files (the difference between current and default.) <code>full</code> prints every setting uncommented and set to the current value, i.e. how it would be used by an lvm command. This includes settings modified in config files, settings that usually get defaults internally, and settings that get defaults from config files. <code>list</code> prints all config names without values. <code>missing</code> prints settings that are missing from the lvm config files. A missing setting that usually gets its default from config files is printed uncommented and set to the internal default. Settings that get their default internally and are not set in config files are printed commented with the internal default. <code>new</code> prints config settings that have been added since the lvm version specified by &#8211;sinceversion. They are printed with their default values. <code>profilable</code> prints settings with their default values that can be set from a profile. <code>profilable-command</code> prints settings with their default values that can be set from a command profile. <code>profilable-metadata</code> prints settings with their default values that can be set from a metadata profile. Also see <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5).</p>
<dt> <code>&#8211;unconfigured</code></p>
<dd>
<dd>Internal option used for generating config file during build.</p>
<dt> <code>&#8211;validate</code></p>
<dd>
<dd>Validate current configuration used and exit with appropriate return code. The validation is done only for the configuration at the front of the &quot;config cascade&quot;. To validate the whole merged configuration tree, also use &#8211;mergedconfig. The validation is done even if lvm.conf config/checks is disabled.</p>
<dt> <code>-v</code>|<code>&#8211;verbose</code> &#8230;</p>
<dd>
<dd>Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.</p>
<dt> <code>&#8211;version</code></p>
<dd>
<dd>Display version information.</p>
<dt> <code>&#8211;withcomments</code></p>
<dd>
<dd>Display a full comment for each configuration node. For deprecated settings, also display comments about deprecation.</p>
<dt> <code>&#8211;withgeneralpreamble</code></p>
<dd>
<dd>Include general config file preamble.</p>
<dt> <code>&#8211;withlocalpreamble</code></p>
<dd>
<dd>Include local config file preamble.</p>
<dt> <code>&#8211;withspaces</code></p>
<dd>
<dd>Where appropriate, add more spaces in output for better readability.</p>
<dt> <code>&#8211;withsummary</code></p>
<dd>
<dd>Display a one line comment for each configuration node.</p>
<dt> <code>&#8211;withversions</code></p>
<dd>
<dd>Also display a comment containing the version of introduction for each configuration node. If the setting is deprecated, also display the version since which it is deprecated.</p>
<dt> <code>-y</code>|<code>&#8211;yes</code></p>
<dd>
<dd>Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution. (For automatic no, see -qq.)</dl>
<h2>Variables</h2>
<dl>
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
