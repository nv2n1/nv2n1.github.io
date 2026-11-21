---
title: "dmsetup(8)"
name: "dmsetup"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dmsetup/"
description: "dmsetup — low level logical volume management"
---
<p>dmsetup --- low level logical volume management </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>dmsetup</code><code>clear</code><i>device_name</i></dt>
<dt><code>dmsetup</code><code>create</code><i>device_name</i> [<code>-u</code>|<code>--uuid</code><i>uuid</i>] [<code>--addnodeoncreate</code>|<code>--addnodeonresume</code>] [<code>-n</code>|<code>--notable</code>|<code>--table</code><i>table</i>|<i>table_file</i>] [<code>--readahead</code> [<code>+</code>]<i>sectors</i>|<code>auto</code>|<code>none</code>] </dt>
<dt><code>dmsetup</code><code>create</code><code>--concise</code> [<i>concise_device_specification</i>] </dt>
<dt><code>dmsetup</code><code>deps</code> [<code>-o</code><i>options</i>] [<i>device_name</i>...] </dt>
<dt><code>dmsetup</code><code>help</code> [<code>-c</code>|<code>-C</code>|<code>--columns</code>] </dt>
<dt><code>dmsetup</code><code>info</code> [<i>device_name</i>...] </dt>
<dt><code>dmsetup</code><code>info</code><code>-c</code>|<code>-C</code>|<code>--columns</code> [<code>--count</code><i>count</i>] [<code>--interval</code><i>seconds</i>] [<code>--nameprefixes</code>] [<code>--noheadings</code>] [<code>-o</code><i>fields</i>] [<code>-O</code>|<code>--sort</code><i>sort_fields</i>] [<code>--separator</code><i>separator</i>] [<i>device_name</i>] </dt>
<dt><code>dmsetup</code><code>load</code><i>device_name</i> [<code>--table</code><i>table</i>|<i>table_file</i>] </dt>
<dt><code>dmsetup</code><code>ls</code> [<code>--target</code><i>target_type</i>] [<code>--exec</code><i>command</i>] [<code>--tree</code>] [<code>-o</code><i>options</i>] </dt>
<dt><code>dmsetup</code><code>mangle</code> [<i>device_name</i>...] </dt>
<dt><code>dmsetup</code><code>message</code><i>device_name</i><i>sector</i><i>message</i></dt>
<dt><code>dmsetup</code><code>mknodes</code> [<i>device_name</i>...] </dt>
<dt><code>dmsetup</code><code>reload</code><i>device_name</i> [<code>--table</code><i>table</i>|<i>table_file</i>] </dt>
<dt><code>dmsetup</code><code>remove</code> [<code>-f</code>|<code>--force</code>] [<code>--retry</code>] [<code>--deferred</code>] <i>device_name</i>... </dt>
<dt><code>dmsetup</code><code>remove_all</code> [<code>-f</code>|<code>--force</code>] [<code>--deferred</code>] </dt>
<dt><code>dmsetup</code><code>rename</code><i>device_name</i><i>new_name</i></dt>
<dt><code>dmsetup</code><code>rename</code><i>device_name</i><code>--setuuid</code><i>uuid</i></dt>
<dt><code>dmsetup</code><code>resume</code><i>device_name</i>... [<code>--addnodeoncreate</code>|<code>--addnodeonresume</code>] [<code>--noflush</code>] [<code>--nolockfs</code>] [<code>--readahead</code> [<code>+</code>]<i>sectors</i>|<code>auto</code>|<code>none</code>] </dt>
<dt><code>dmsetup</code><code>setgeometry</code><i>device_name</i><i>cyl</i><i>head</i><i>sect</i><i>start</i></dt>
<dt><code>dmsetup</code><code>splitname</code><i>device_name</i> [<i>subsystem</i>] </dt>
<dt><code>dmsetup</code><code>stats</code><i>command</i> [<i>options</i>] </dt>
<dt><code>dmsetup</code><code>status</code> [<code>--target</code><i>target_type</i>] [<code>--noflush</code>] [<i>device_name</i>...] </dt>
<dt><code>dmsetup</code><code>suspend</code> [<code>--nolockfs</code>] [<code>--noflush</code>] <i>device_name</i>... </dt>
<dt><code>dmsetup</code><code>table</code> [<code>--concise</code>] [<code>--target</code><i>target_type</i>] [<code>--showkeys</code>] [<i>device_name</i>...] </dt>
<dt><code>dmsetup</code><code>targets</code></dt>
<dt><code>dmsetup</code><code>udevcomplete</code><i>cookie</i></dt>
<dt><code>dmsetup</code><code>udevcomplete_all</code> [<i>age_in_minutes</i>] </dt>
<dt><code>dmsetup</code><code>udevcookie</code></dt>
<dt><code>dmsetup</code><code>udevcreatecookie</code></dt>
<dt><code>dmsetup</code><code>udevflags</code><i>cookie</i></dt>
<dt><code>dmsetup</code><code>udevreleasecookie</code> [<i>cookie</i>] </dt>
<dt><code>dmsetup</code><code>version</code></dt>
<dt><code>dmsetup</code><code>wait</code> [<code>--noflush</code>] <i>device_name</i> [<i>event_nr</i>] </dt>
<dt><code>dmsetup</code><code>wipe_table</code><i>device_name</i>... [<code>-f</code>|<code>--force</code>] [<code>--noflush</code>] [<code>--nolockfs</code>] </dt>
</dl>
<dl>
<dt><code>devmap_name </code><i>major minor</i></dt>
<dt><code>devmap_name </code><i>major:minor</i></dt>
</dl>
<h2>DESCRIPTION</h2>
<dd> <p> dmsetup manages logical devices that use the device-mapper driver. Devices are created by loading a table that specifies a target for each sector (512 bytes) in the logical device. </p>
<p>The first argument to dmsetup is a command. The second argument is the logical device name or uuid. </p>
<p>Invoking the dmsetup tool as <code>devmap_name</code> (which is not normally distributed and is supported only for historical reasons) is equivalent to <code>dmsetup info -c --noheadings -j</code><i>&nbsp;major&nbsp;</i><code>-m</code><i>&nbsp;minor</i>.  </p>
<h2>OPTIONS</h2>
 </dd>
<dl>
<dt><code>--addnodeoncreate</code></dt>
<dd>  </dd>
<dd> <p> Ensure <i>/dev/mapper</i> node exists after <code>dmsetup create</code>. </p>
 </dd>
<dt><code>--addnodeonresume</code></dt>
<dd>  </dd>
<dd> <p> Ensure <i>/dev/mapper</i> node exists after <code>dmsetup resume</code> (default with udev). </p>
 </dd>
<dt><code>--checks</code></dt>
<dd>  </dd>
<dd> <p> Perform additional checks on the operations requested and report potential problems. Useful when debugging scripts. In some cases these checks may slow down operations noticeably. </p>
 </dd>
<dt><code>-c</code>|<code>-C</code>|<code>--columns</code></dt>
<dd>  </dd>
<dd> <p> Display output in columns rather than as Field: Value lines. </p>
 </dd>
<dt><code>--count</code><i>count</i></dt>
<dd>  </dd>
<dd> <p> Specify the number of times to repeat a report. Set this to zero continue until interrupted. The default interval is one second. </p>
 </dd>
<dt><code>-f</code>|<code>--force</code></dt>
<dd>  </dd>
<dd> <p> Try harder to complete operation. </p>
 </dd>
<dt><code>-h</code>|<code>--help</code></dt>
<dd>  </dd>
<dd> <p> Outputs a summary of the commands available, optionally including the list of report fields (synonym with <code>help</code> command). </p>
 </dd>
<dt><code>--inactive</code></dt>
<dd>  </dd>
<dd> <p> When returning any table information from the kernel report on the inactive table instead of the live table. Requires kernel driver version 4.16.0 or above. </p>
 </dd>
<dt><code>--interval</code><i>seconds</i></dt>
<dd>  </dd>
<dd> <p> Specify the interval in seconds between successive iterations for repeating reports. If <code>--interval</code> is specified but <code>--count</code> is not, reports will continue to repeat until interrupted. The default interval is one second. </p>
 </dd>
<dt><code>--manglename</code><code>auto</code>|<code>hex</code>|<code>none</code></dt>
<dd>  </dd>
<dd> <p> Mangle any character not on a whitelist using mangling_mode when processing device-mapper device names and UUIDs. The names and UUIDs are mangled on input and unmangled on output where the mangling mode is one of: <code>auto</code> (only do the mangling if not mangled yet, do nothing if already mangled, error on mixed), <code>hex</code> (always do the mangling) and <code>none</code> (no mangling). Default mode is <code>auto</code>. Character whitelist: 0-9, A-Z, a-z, #+-.:=@_. This whitelist is also supported by udev. Any character not on a whitelist is replaced with its hex value (two digits) prefixed by \x. Mangling mode could be also set through <code>DM_DEFAULT_NAME_MANGLING_MODE</code> environment variable. </p>
 </dd>
<dt><code>-j</code>|<code>--major</code><i>major</i></dt>
<dd>  </dd>
<dd> <p> Specify the major number. </p>
 </dd>
<dt><code>-m</code>|<code>--minor</code><i>minor</i></dt>
<dd>  </dd>
<dd> <p> Specify the minor number. </p>
 </dd>
<dt><code>-n</code>|<code>--notable</code></dt>
<dd>  </dd>
<dd> <p> When creating a device, don&#8217;t load any table. </p>
 </dd>
<dt><code>--nameprefixes</code></dt>
<dd>  </dd>
<dd> <p> Add a &quot;DM_&quot; prefix plus the field name to the output. Useful with <code>--noheadings</code> to produce a list of field=value pairs that can be used to set environment variables (for example, in <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) rules). </p>
 </dd>
<dt><code>--noheadings</code></dt>
<dd> <p> Suppress the headings line when using columnar output. </p>
 </dd>
<dt><code>--noflush</code></dt>
<dd> <p> Do not flush outstading I/O when suspending a device, or do not commit thin-pool metadata when obtaining thin-pool status. </p>
 </dd>
<dt><code>--nolockfs</code></dt>
<dd>  </dd>
<dd> <p> Do not attempt to synchronize filesystem eg, when suspending a device. </p>
 </dd>
<dt><code>--noopencount</code></dt>
<dd>  </dd>
<dd> <p> Tell the kernel not to supply the open reference count for the device. </p>
 </dd>
<dt><code>--noudevrules</code></dt>
<dd>  </dd>
<dd> <p> Do not allow udev to manage nodes for devices in device-mapper directory. </p>
 </dd>
<dt><code>--noudevsync</code></dt>
<dd>  </dd>
<dd> <p> Do not synchronise with udev when creating, renaming or removing devices. </p>
 </dd>
<dt><code>-o</code>|<code>--options</code><i>options</i></dt>
<dd>  </dd>
<dd> <p> Specify which fields to display. </p>
 </dd>
<dt><code>--readahead</code> [<code>+</code>]<i>sectors</i>|<code>auto</code>|<code>none</code></dt>
<dd>  </dd>
<dd> <p> Specify read ahead size in units of sectors. The default value is <code>auto</code> which allows the kernel to choose a suitable value automatically. The <code>+</code> prefix lets you specify a minimum value which will not be used if it is smaller than the value chosen by the kernel. The value <code>none</code> is equivalent to specifying zero. </p>
 </dd>
<dt><code>-r</code>|<code>--readonly</code></dt>
<dd>  </dd>
<dd> <p> Set the table being loaded read-only. </p>
 </dd>
<dt><code>-S</code>|<code>--select</code><i>selection</i></dt>
<dd>  </dd>
<dd> <p> Process only items that match <i>selection</i> criteria. If the command is producing report output, adding the &quot;selected&quot; column (<code>-o selected</code>) displays all rows and shows 1 if the row matches the <i>selection</i> and 0 otherwise. The selection criteria are defined by specifying column names and their valid values while making use of supported comparison operators. As a quick help and to see full list of column names that can be used in selection and the set of supported selection operators, check the output of <code>dmsetup info -c -S help</code> command. </p>
 </dd>
<dt><code>--table</code><i>table</i></dt>
<dd>  </dd>
<dd> <p> Specify a one-line table directly on the command line. See below for more information on the table format. </p>
 </dd>
<dt><code>--udevcookie</code><i>cookie</i></dt>
<dd>  </dd>
<dd> <p> Use cookie for udev synchronisation. Note: Same cookie should be used for same type of operations i.e. creation of multiple different devices. It&#8217;s not adviced to combine different operations on the single device. </p>
 </dd>
<dt><code>-u</code>|<code>--uuid</code></dt>
<dd>  </dd>
<dd> <p> Specify the <i>uuid</i>. </p>
 </dd>
<dt><code>-y</code>|<code>--yes</code></dt>
<dd>  </dd>
<dd> <p> Answer yes to all prompts automatically. </p>
 </dd>
<dt><code>-v</code>|<code>--verbose</code> [<code>-v</code>|<code>--verbose</code>] </dt>
<dd>  </dd>
<dd> <p> Produce additional output. </p>
 </dd>
<dt><code>--verifyudev</code></dt>
<dd>  </dd>
<dd> <p> If udev synchronisation is enabled, verify that udev operations get performed correctly and try to fix up the device nodes afterwards if not. </p>
 </dd>
<dt><code>--version</code></dt>
<dd>  </dd>
<dd> <p> Display the library and kernel driver version. <br />
 </p>
 </dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>clear</code><i>device_name</i></dt>
<dd>  </dd>
<dd> <p> Destroys the table in the inactive table slot for device_name. </p>
 </dd>
<dt><code>create</code><i>device_name</i> [<code>-u</code>|<code>--uuid</code><i>uuid</i>] [<code>--addnodeoncreate</code>|<code>--addnodeonresume</code>] [<code>-n</code>|<code>--notable</code>|<code>--table</code><i>table</i>|<i>table_file</i>] [<code>--readahead</code> [<code>+</code>]<i>sectors</i>|<code>auto</code>|<code>none</code>] </dt>
<dd>  </dd>
<dd> <p> Creates a device with the given name. If <i>table</i> or <i>table_file</i> is supplied, the table is loaded and made live. Otherwise a table is read from standard input unless <code>--notable</code> is used. The optional <i>uuid</i> can be used in place of device_name in subsequent dmsetup commands. If successful the device will appear in table and for live device the node <i>/dev/mapper/device_name</i> is created. See below for more information on the table format. </p>
 </dd>
<dt><code>create</code><code>--concise</code> [<i>concise_device_specification</i>] </dt>
<dd>  </dd>
<dd> <p> Creates one or more devices from a concise device specification. Each device is specified by a comma-separated list: name, uuid, minor number, flags, comma-separated table lines. Flags defaults to read-write (rw) or may be read-only (ro). Uuid, minor number and flags are optional so those fields may be empty. A semi-colon separates specifications of different devices. Use a backslash to escape the following character, for example a comma or semi-colon in a name or table. See also CONCISE FORMAT below. </p>
 </dd>
<dt><code>deps</code> [<code>-o</code><i>options</i>] [<i>device_name</i>...] </dt>
<dd>  </dd>
<dd> <p> Outputs a list of devices referenced by the live table for the specified device. Device names on output can be customised by following <i>options</i>: <code>devno</code> (major and minor pair, used by default), <code>blkdevname</code> (block device name), <code>devname</code> (map name for device-mapper devices, equal to blkdevname otherwise). </p>
 </dd>
<dt><code>help</code> [<code>-c</code>|<code>-C</code>|<code>--columns</code>] </dt>
<dd>  </dd>
<dd> <p> Outputs a summary of the commands available, optionally including the list of report fields. </p>
 </dd>
<dt><code>info</code> [<i>device_name</i>...] </dt>
<dd>  </dd>
<dd> <p> Outputs some brief information about the device in the form: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <br />
&nbsp;State: SUSPENDED|ACTIVE, READ-ONLY <br />
&nbsp;Tables present: LIVE and/or INACTIVE <br />
&nbsp;Open reference count <br />
&nbsp;Last event sequence number&nbsp;(used by&nbsp;<code>wait</code>) <br />
&nbsp;Major and minor device number <br />
&nbsp;Number of targets in the live table <br />
&nbsp;UUID </p>
 </dd></dl>
</dl>
<dt><code>info</code><code>-c</code>|<code>-C</code>|<code>--columns</code> [<code>--count</code><i>count</i>] [<code>--interval</code><i>seconds</i>] [<code>--nameprefixes</code>] [<code>--noheadings</code>] [<code>-o</code><i>fields</i>] [<code>-O</code>|<code>--sort</code><i>sort_fields</i>] [<code>--separator</code><i>separator</i>] [<i>device_name</i>] </dt>
<dd>  </dd>
<dd> <p> Output you can customise. Fields are comma-separated and chosen from the following list: <code>name</code>, <code>major</code>, <code>minor</code>, <code>attr</code>, <code>open</code>, <code>segments</code>, <code>events</code>, <code>uuid</code>. Attributes are: (<i>L</i>)ive, (<i>I</i>)nactive, (<i>s</i>)uspended, (<i>r</i>)ead-only, read-(<i>w</i>)rite. Precede the list with &#8216;<code>+</code>&#8216; to append to the default selection of columns instead of replacing it. Precede any sort field with &#8216;<code>-</code>&#8216; for a reverse sort on that column. </p>
 </dd>
<dt><code>ls</code> [<code>--target</code><i>target_type</i>] [<code>--exec</code><i>command</i>] [<code>--tree</code>] [<code>-o</code><i>options</i>] </dt>
<dd>  </dd>
<dd> <p> List device names. Optionally only list devices that have at least one target of the specified type. Optionally execute a command for each device. The device name is appended to the supplied command. Device names on output can be customised by following options: <code>devno</code> (major and minor pair, used by default), <code>blkdevname</code> (block device name), <code>devname</code> (map name for device-mapper devices, equal to blkdevname otherwise). <code>--tree</code> displays dependencies between devices as a tree. It accepts a comma-separate list of <i>options</i>. Some specify the information displayed against each node: <code>device</code>/<code>nodevice</code>; <code>blkdevname</code>; <code>active</code>, <code>open</code>, <code>rw</code>, <code>uuid</code>. Others specify how the tree is displayed: <code>ascii</code>, <code>utf</code>, <code>vt100</code>; <code>compact</code>, <code>inverted</code>, <code>notrunc</code>. </p>
 </dd>
<dt><code>load</code>| <code>reload</code><i>device_name</i> [<code>--table</code><i>table</i>|<i>table_file</i>] </dt>
<dd>  </dd>
<dd> <p> Loads <i>table</i> or <i>table_file</i> into the inactive table slot for device_name. If neither is supplied, reads a table from standard input. </p>
 </dd>
<dt><code>mangle</code> [<i>device_name</i>...] </dt>
<dd>  </dd>
<dd> <p> Ensure existing device-mapper <i>device_name</i> and UUID is in the correct mangled form containing only whitelisted characters (supported by udev) and do a rename if necessary. Any character not on the whitelist will be mangled based on the <code>--manglename</code> setting. Automatic rename works only for device names and not for device UUIDs because the kernel does not allow changing the UUID of active devices. Any incorrect UUIDs are reported only and they must be manually corrected by deactivating the device first and then reactivating it with proper mangling mode used (see also <code>--manglename</code>). </p>
 </dd>
<dt><code>message</code><i>device_name</i><i>sector</i><i>message</i></dt>
<dd>  </dd>
<dd> <p> Send message to target. If sector not needed use 0. </p>
 </dd>
<dt><code>mknodes</code> [<i>device_name</i>...] </dt>
<dd>  </dd>
<dd> <p> Ensure that the node in <i>/dev/mapper</i> for <i>device_name</i> is correct. If no device_name is supplied, ensure that all nodes in <i>/dev/mapper</i> correspond to mapped devices currently loaded by the device-mapper kernel driver, adding, changing or removing nodes as necessary. </p>
 </dd>
<dt><code>remove</code> [<code>-f</code>|<code>--force</code>] [<code>--retry</code>] [<code>--deferred</code>] <i>device_name</i>... </dt>
<dd>  </dd>
<dd> <p> Removes a device. It will no longer be visible to dmsetup. Open devices cannot be removed, but adding <code>--force</code> will replace the table with one that fails all I/O. <code>--deferred</code> will enable deferred removal of open devices - the device will be removed when the last user closes it. The deferred removal feature is supported since version 4.27.0 of the device-mapper driver available in upstream kernel version 3.13. (Use <code>dmsetup version</code> to check this.) If an attempt to remove a device fails, perhaps because a process run from a quick udev rule temporarily opened the device, the <code>--retry</code> option will cause the operation to be retried for a few seconds before failing. Do NOT combine <code>--force</code> and <code>--udevcookie</code>, as udev may start to process udev rules in the middle of error target replacement and result in nondeterministic result. </p>
 </dd>
<dt><code>remove_all</code> [<code>-f</code>|<code>--force</code>] [<code>--deferred</code>] </dt>
<dd>  </dd>
<dd> <p> Attempts to remove all device definitions i.e. reset the driver. This also runs <code>mknodes</code> afterwards. Use with care! Open devices cannot be removed, but adding <code>--force</code> will replace the table with one that fails all I/O. <code>--deferred</code> will enable deferred removal of open devices - the device will be removed when the last user closes it. The deferred removal feature is supported since version 4.27.0 of the device-mapper driver available in upstream kernel version 3.13. </p>
 </dd>
<dt><code>rename</code><i>device_name</i><i>new_name</i></dt>
<dd>  </dd>
<dd> <p> Renames a device. </p>
 </dd>
<dt><code>rename</code><i>device_name</i><code>--setuuid</code><i>uuid</i></dt>
<dd>  </dd>
<dd> <p> Sets the uuid of a device that was created without a uuid. After a uuid has been set it cannot be changed. </p>
 </dd>
<dt><code>resume</code><i>device_name</i>... [<code>--addnodeoncreate</code>|<code>--addnodeonresume</code>] [<code>--noflush</code>] [<code>--nolockfs</code>] [<code>--readahead</code> [<code>+</code>]<i>sectors</i>|<code>auto</code>|<code>none</code>] </dt>
<dd>  </dd>
<dd> <p> Un-suspends a device. If an inactive table has been loaded, it becomes live. Postponed I/O then gets re-queued for processing. </p>
 </dd>
<dt><code>setgeometry</code><i>device_name</i><i>cyl</i><i>head</i><i>sect</i><i>start</i></dt>
<dd>  </dd>
<dd> <p> Sets the device geometry to C/H/S. </p>
 </dd>
<dt><code>splitname</code><i>device_name</i> [<i>subsystem</i>] </dt>
<dd>  </dd>
<dd> <p> Splits given <i>device name</i> into <i>subsystem</i> constituents. The default subsystem is LVM. LVM currently generates device names by concatenating the names of the Volume Group, Logical Volume and any internal Layer with a hyphen as separator. Any hyphens within the names are doubled to escape them. The precise encoding might change without notice in any future release, so we recommend you always decode using the current version of this command. </p>
 </dd>
<dt><code>stats</code><i>command</i> [<i>options</i>] </dt>
<dd>  </dd>
<dd> <p> Manages IO statistics regions for devices. See <code><a href="/docs/linux/man/8-dmstats/">dmstats</a></code>(8) for more details. </p>
 </dd>
<dt><code>status</code> [<code>--target</code><i>target_type</i>] [<code>--noflush</code>] [<i>device_name</i>...] </dt>
<dd>  </dd>
<dd> <p> Outputs status information for each of the device&#8217;s targets. With <code>--target</code>, only information relating to the specified target type any is displayed. With <code>--noflush</code>, the thin target (from version 1.3.0) doesn&#8217;t commit any outstanding changes to disk before reporting its statistics. </p>
 </dd>
<dt><code>suspend</code> [<code>--nolockfs</code>] [<code>--noflush</code>] <i>device_name</i>... </dt>
<dd>  </dd>
<dd> <p> Suspends a device. Any I/O that has already been mapped by the device but has not yet completed will be flushed. Any further I/O to that device will be postponed for as long as the device is suspended. If there&#8217;s a filesystem on the device which supports the operation, an attempt will be made to sync it first unless <code>--nolockfs</code> is specified. Some targets such as recent (October 2006) versions of multipath may support the <code>--noflush</code> option. This lets outstanding I/O that has not yet reached the device to remain unflushed. </p>
 </dd>
<dt><code>table</code> [<code>--concise</code>] [<code>--target</code><i>target_type</i>] [<code>--showkeys</code>] [<i>device_name</i>...] </dt>
<dd>  </dd>
<dd> <p> Outputs the current table for the device in a format that can be fed back in using the create or load commands. With <code>--target</code>, only information relating to the specified target type is displayed. Real encryption keys are suppressed in the table output for crypt and integrity targets unless the <code>--showkeys</code> parameter is supplied. Kernel key references prefixed with <code>:</code> are not affected by the parameter and get displayed always (crypt target only). With <code>--concise</code>, the output is presented concisely on a single line. Commas then separate the name, uuid, minor device number, flags (&#8216;ro&#8217; or &#8216;rw&#8217;) and the table (if present). Semi-colons separate devices. Backslashes escape any commas, semi-colons or backslashes. See CONCISE FORMAT below. </p>
 </dd>
<dt><code>targets</code></dt>
<dd>  </dd>
<dd> <p> Displays the names and versions of the currently-loaded targets. </p>
 </dd>
<dt><code>udevcomplete</code><i>cookie</i></dt>
<dd>  </dd>
<dd> <p> Wake any processes that are waiting for udev to complete processing the specified cookie. </p>
 </dd>
<dt><code>udevcomplete_all</code> [<i>age_in_minutes</i>] </dt>
<dd>  </dd>
<dd> <p> Remove all cookies older than the specified number of minutes. Any process waiting on a cookie will be resumed immediately. </p>
 </dd>
<dt><code>udevcookie</code></dt>
<dd>  </dd>
<dd> <p> List all existing cookies. Cookies are system-wide semaphores with keys prefixed by two predefined bytes (0x0D4D). </p>
 </dd>
<dt><code>udevcreatecookie</code></dt>
<dd>  </dd>
<dd> <p> Creates a new cookie to synchronize actions with udev processing. The output is a cookie value. Normally we don&#8217;t need to create cookies since dmsetup creates and destroys them for each action automatically. However, we can generate one explicitly to group several actions together and use only one cookie instead. We can define a cookie to use for each relevant command by using <code>--udevcookie</code> option. Alternatively, we can export this value into the environment of the dmsetup process as <code>DM_UDEV_COOKIE</code> variable and it will be used automatically with all subsequent commands until it is unset. Invoking this command will create system-wide semaphore that needs to be cleaned up explicitly by calling udevreleasecookie command. </p>
 </dd>
<dt><code>udevflags</code><i>cookie</i></dt>
<dd>  </dd>
<dd> <p> Parses given <i>cookie</i> value and extracts any udev control flags encoded. The output is in environment key format that is suitable for use in udev rules. If the flag has its symbolic name assigned then the output is DM_UDEV_FLAG_&lt;flag_name&gt; = &#8216;1&#8217;, DM_UDEV_FLAG&lt;flag_position&gt; = &#8216;1&#8217; otherwise. Subsystem udev flags don&#8217;t have symbolic names assigned and these ones are always reported as DM_SUBSYSTEM_UDEV_FLAG&lt;flag_position&gt; = &#8216;1&#8217;. There are 16 udev flags altogether. </p>
 </dd>
<dt><code>udevreleasecookie</code> [<i>cookie</i>] </dt>
<dd>  </dd>
<dd> <p> Waits for all pending udev processing bound to given cookie value and clean up the cookie with underlying semaphore. If the cookie is not given directly, the command will try to use a value defined by <code>DM_UDEV_COOKIE</code> environment variable. </p>
 </dd>
<dt><code>version</code></dt>
<dd>  </dd>
<dd> <p> Outputs version information. </p>
 </dd>
<dt><code>wait</code> [<code>--noflush</code>] <i>device_name</i> [<i>event_nr</i>] </dt>
<dd>  </dd>
<dd> <p> Sleeps until the event counter for device_name exceeds event_nr. Use <code>-v</code> to see the event number returned. To wait until the next event is triggered, use <code>info</code> to find the last event number. With <code>--noflush</code>, the thin target (from version 1.3.0) doesn&#8217;t commit any outstanding changes to disk before reporting its statistics. </p>
 </dd>
<dt><code>wipe_table</code><i>device_name</i>... [<code>-f</code>|<code>--force</code>] [<code>--noflush</code>] [<code>--nolockfs</code>] </dt>
<dd>  </dd>
<dd> <p> Wait for any I/O in-flight through the device to complete, then replace the table with a new table that fails any new I/O sent to the device. If successful, this should release any devices held open by the device&#8217;s table(s). </p>
 </dd></dl>
<h2>TABLE FORMAT</h2>
<p> Each line of the table specifies a single target and is of the form: </p>
<p> <i>logical_start_sector num_sectors</i> <code>target_type</code> <i>target_args</i> </p>
<p>Simple target types and target args include: </p>
<dl>
<dt><code>linear </code><i>destination_device start_sector</i></dt>
<dd> <p> The traditional linear mapping. </p>
 </dd>
<dt><code>striped </code><i>num_stripes chunk_size </i>[<i>destination start_sector</i>]... </dt>
<dd> <p> Creates a striped area. <br />
 e.g. striped 2 32 /dev/hda1 0 /dev/hdb1 0 will map the first chunk (16k) as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <br />
&nbsp;LV chunk 1-&gt;&nbsp;hda1, chunk 1 <br />
&nbsp;LV chunk 2-&gt;&nbsp;hdb1, chunk 1 <br />
&nbsp;LV chunk 3-&gt;&nbsp;hda1, chunk 2 <br />
&nbsp;LV chunk 4-&gt;&nbsp;hdb1, chunk 2 <br />
&nbsp;etc. </p>
 </dd></dl>
</dl>
<dt><code>error</code></dt>
<dd> <p> Errors any I/O that goes to this area. Useful for testing or for creating devices with holes in them. </p>
 </dd>
<dt><code>zero</code></dt>
<dd> <p> Returns blocks of zeroes on reads. Any data written is discarded silently. This is a block-device equivalent of the <i>/dev/zero</i> character-device data sink described in <code><a href="/docs/linux/man/4-null/">null</a></code>(4). </p>
 </dd></dl>
<p>More complex targets include: </p>
<dl>
<dt><code>cache</code></dt>
<dd> <p> Improves performance of a block device (eg, a spindle) by dynamically migrating some of its data to a faster smaller device (eg, an SSD). </p>
 </dd>
<dt><code>crypt</code></dt>
<dd> <p> Transparent encryption of block devices using the kernel crypto API. </p>
 </dd>
<dt><code>delay</code></dt>
<dd> <p> Delays reads and/or writes to different devices. Useful for testing. </p>
 </dd>
<dt><code>flakey</code></dt>
<dd> <p> Creates a similar mapping to the linear target but exhibits unreliable behaviour periodically. Useful for simulating failing devices when testing. </p>
 </dd>
<dt><code>mirror</code></dt>
<dd> <p> Mirrors data across two or more devices. </p>
 </dd>
<dt><code>multipath</code></dt>
<dd> <p> Mediates access through multiple paths to the same device. </p>
 </dd>
<dt><code>raid</code></dt>
<dd> <p> Offers an interface to the kernel&#8217;s software raid driver, md. </p>
 </dd>
<dt><code>snapshot</code></dt>
<dd> <p> Supports snapshots of devices. </p>
 </dd>
<dt><code>thin</code>, <code>thin-pool</code></dt>
<dd> <p> Supports thin provisioning of devices and also provides a better snapshot support. </p>
 </dd></dl>
<p>To find out more about the various targets and their table formats and status lines, please read the files in the Documentation/device-mapper directory in the kernel source tree. (Your distribution might include a copy of this information in the documentation directory for the device-mapper package.)  </p>
<h2>EXAMPLES</h2>
<p> # A table to join two disks together <br />
 0 1028160 linear /dev/hda 0 <br />
 1028160 3903762 linear /dev/hdb 0 <br />
 # A table to stripe across the two disks, <br />
 # and add the spare space from <br />
 # hdb to the back of the volume <br />
 0 2056320 striped 2 32 /dev/hda 0 /dev/hdb 0 <br />
 2056320 2875602 linear /dev/hdb 1028160  </p>
<h2>CONCISE FORMAT</h2>
<p> A concise representation of one of more devices. </p>
<p> <br />
 - A comma separates the fields of each device. <br />
 - A semi-colon separates devices. </p>
<dl>
<dt>The representation of a device takes the form:</dt>
<dd> <p>&lt;name&gt;,&lt;uuid&gt;,&lt;minor&gt;,&lt;flags&gt;,&lt;table&gt;[,&lt;table&gt;+][;&lt;dev_name&gt;,&lt;uuid&gt;,&lt;minor&gt;,&lt;flags&gt;,&lt;table&gt;[,&lt;table&gt;+]] </p>
 </dd>
<dt>The fields are:</dt>
<dd>  </dd>
<dt><code>name</code></dt>
<dd> <p> The name of the device. </p>
 </dd>
<dt><code>uuid</code></dt>
<dd> <p> The UUID of the device (or empty). </p>
 </dd>
<dt><code>minor</code></dt>
<dd> <p> The minor number of the device. If empty, the kernel assigns a suitable minor number. </p>
 </dd>
<dt><code>flags</code></dt>
<dd> <p> Supported flags are: </p>
<p> <code>ro</code> Sets the table being loaded for the device read-only <br />
 <code>rw</code> Sets the table being loaded for the device read-write (default) </p>
 </dd>
<dt><code>table</code></dt>
<dd> <p> One line of the table. See TABLE FORMAT above. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> # A simple linear read-only device <br />
 test-linear-small,,,ro,0 2097152 linear /dev/loop0 0, 2097152 2097152 linear /dev/loop1 0 <br />
 </p>
<p># Two linear devices <br />
 test-linear-small,,,,0 2097152 linear /dev/loop0 0;test-linear-large,,,, 0 2097152 linear /dev/loop1 0, 2097152 2097152 linear /dev/loop2 0 <br />
  </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>DM_DEV_DIR</code></dt>
<dd> <p> The device directory name. Defaults to &quot;<i>/dev</i>&quot; and must be an absolute path. </p>
 </dd>
<dt><code>DM_UDEV_COOKIE</code></dt>
<dd> <p> A cookie to use for all relevant commands to synchronize with udev processing. It is an alternative to using <code>--udevcookie</code> option. </p>
 </dd>
<dt><code>DM_DEFAULT_NAME_MANGLING_MODE</code></dt>
<dd> <p> A default mangling mode. Defaults to &quot;<code>auto</code>&quot; and it is an alternative to using <code>--manglename</code> option. </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> Original version: Joe Thornber &lt;thornber [at] redhat.com&gt;  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-dmstats/">dmstats</a></code>(8), <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8) </p>
<p>LVM2 resource page: <a rel="nofollow" href="https://www.sourceware.org/lvm2/">https://www.sourceware.org/lvm2/</a> <br />
 Device-mapper resource page: <a rel="nofollow" href="http://sources.redhat.com/dm/">http://sources.redhat.com/dm/</a> </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">COMMANDS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">TABLE FORMAT</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">EXAMPLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">CONCISE FORMAT</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">EXAMPLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">ENVIRONMENT VARIABLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">SEE ALSO</a></dt>
<dd>  </dd></dl>
