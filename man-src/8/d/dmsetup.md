---
title: "dmsetup(8)"
name: "dmsetup"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dmsetup/"
description: "dmsetup — low level logical volume management"
---

<p>dmsetup &#8212; low level logical volume management</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dmsetup</code> <code>clear</code> <i>device_name</i></p>
<dt> <code>dmsetup</code> <code>create</code> <i>device_name</i> [<code>-u</code>|<code>&#8211;uuid</code> <i>uuid</i>] [<code>&#8211;addnodeoncreate</code>|<code>&#8211;addnodeonresume</code>] [<code>-n</code>|<code>&#8211;notable</code>|<code>&#8211;table</code> <i>table</i>|<i>table_file</i>] [<code>&#8211;readahead</code> [<code>+</code>]<i>sectors</i>|<code>auto</code>|<code>none</code>]</p>
<dt> <code>dmsetup</code> <code>create</code> <code>&#8211;concise</code> [<i>concise_device_specification</i>]</p>
<dt> <code>dmsetup</code> <code>deps</code> [<code>-o</code> <i>options</i>] [<i>device_name</i>&#8230;]</p>
<dt> <code>dmsetup</code> <code>help</code> [<code>-c</code>|<code>-C</code>|<code>&#8211;columns</code>]</p>
<dt> <code>dmsetup</code> <code>info</code> [<i>device_name</i>&#8230;]</p>
<dt> <code>dmsetup</code> <code>info</code> <code>-c</code>|<code>-C</code>|<code>&#8211;columns</code> [<code>&#8211;count</code> <i>count</i>] [<code>&#8211;interval</code> <i>seconds</i>] [<code>&#8211;nameprefixes</code>] [<code>&#8211;noheadings</code>] [<code>-o</code> <i>fields</i>] [<code>-O</code>|<code>&#8211;sort</code> <i>sort_fields</i>] [<code>&#8211;separator</code> <i>separator</i>] [<i>device_name</i>]</p>
<dt> <code>dmsetup</code> <code>load</code> <i>device_name</i> [<code>&#8211;table</code> <i>table</i>|<i>table_file</i>]</p>
<dt> <code>dmsetup</code> <code>ls</code> [<code>&#8211;target</code> <i>target_type</i>] [<code>&#8211;exec</code> <i>command</i>] [<code>&#8211;tree</code>] [<code>-o</code> <i>options</i>]</p>
<dt> <code>dmsetup</code> <code>mangle</code> [<i>device_name</i>&#8230;]</p>
<dt> <code>dmsetup</code> <code>message</code> <i>device_name</i> <i>sector</i> <i>message</i></p>
<dt> <code>dmsetup</code> <code>mknodes</code> [<i>device_name</i>&#8230;]</p>
<dt> <code>dmsetup</code> <code>reload</code> <i>device_name</i> [<code>&#8211;table</code> <i>table</i>|<i>table_file</i>]</p>
<dt> <code>dmsetup</code> <code>remove</code> [<code>-f</code>|<code>&#8211;force</code>] [<code>&#8211;retry</code>] [<code>&#8211;deferred</code>] <i>device_name</i>&#8230;</p>
<dt> <code>dmsetup</code> <code>remove_all</code> [<code>-f</code>|<code>&#8211;force</code>] [<code>&#8211;deferred</code>]</p>
<dt> <code>dmsetup</code> <code>rename</code> <i>device_name</i> <i>new_name</i></p>
<dt> <code>dmsetup</code> <code>rename</code> <i>device_name</i> <code>&#8211;setuuid</code> <i>uuid</i></p>
<dt> <code>dmsetup</code> <code>resume</code> <i>device_name</i>&#8230; [<code>&#8211;addnodeoncreate</code>|<code>&#8211;addnodeonresume</code>] [<code>&#8211;noflush</code>] [<code>&#8211;nolockfs</code>] [<code>&#8211;readahead</code> [<code>+</code>]<i>sectors</i>|<code>auto</code>|<code>none</code>]</p>
<dt> <code>dmsetup</code> <code>setgeometry</code> <i>device_name</i> <i>cyl</i> <i>head</i> <i>sect</i> <i>start</i></p>
<dt> <code>dmsetup</code> <code>splitname</code> <i>device_name</i> [<i>subsystem</i>]</p>
<dt> <code>dmsetup</code> <code>stats</code> <i>command</i> [<i>options</i>]</p>
<dt> <code>dmsetup</code> <code>status</code> [<code>&#8211;target</code> <i>target_type</i>] [<code>&#8211;noflush</code>] [<i>device_name</i>&#8230;]</p>
<dt> <code>dmsetup</code> <code>suspend</code> [<code>&#8211;nolockfs</code>] [<code>&#8211;noflush</code>] <i>device_name</i>&#8230;</p>
<dt> <code>dmsetup</code> <code>table</code> [<code>&#8211;concise</code>] [<code>&#8211;target</code> <i>target_type</i>] [<code>&#8211;showkeys</code>] [<i>device_name</i>&#8230;]</p>
<dt> <code>dmsetup</code> <code>targets</code></p>
<dt> <code>dmsetup</code> <code>udevcomplete</code> <i>cookie</i></p>
<dt> <code>dmsetup</code> <code>udevcomplete_all</code> [<i>age_in_minutes</i>]</p>
<dt> <code>dmsetup</code> <code>udevcookie</code></p>
<dt> <code>dmsetup</code> <code>udevcreatecookie</code></p>
<dt> <code>dmsetup</code> <code>udevflags</code> <i>cookie</i></p>
<dt> <code>dmsetup</code> <code>udevreleasecookie</code> [<i>cookie</i>]</p>
<dt> <code>dmsetup</code> <code>version</code></p>
<dt> <code>dmsetup</code> <code>wait</code> [<code>&#8211;noflush</code>] <i>device_name</i> [<i>event_nr</i>]</p>
<dt> <code>dmsetup</code> <code>wipe_table</code> <i>device_name</i>&#8230; [<code>-f</code>|<code>&#8211;force</code>] [<code>&#8211;noflush</code>] [<code>&#8211;nolockfs</code>]</dl>
<dl>
<dt> <code>devmap_name </code><i>major minor</i></p>
<dt> <code>devmap_name </code><i>major:minor</i></dl>
<h2>Description</h2>
<dd>dmsetup manages logical devices that use the device-mapper driver. Devices are created by loading a table that specifies a target for each sector (512 bytes) in the logical device. </p>
<p> The first argument to dmsetup is a command. The second argument is the logical device name or uuid. </p>
<p> Invoking the dmsetup tool as <code>devmap_name</code> (which is not normally distributed and is supported only for historical reasons) is equivalent to <code>dmsetup info -c &#8211;noheadings -j</code><i>&nbsp;major&nbsp;</i><code>-m</code><i>&nbsp;minor</i>.</p>
<h2>Options</h2>
<dl>
<dt> <code>&#8211;addnodeoncreate</code></p>
<dd>
<dd>Ensure <i>/dev/mapper</i> node exists after <code>dmsetup create</code>.</p>
<dt> <code>&#8211;addnodeonresume</code></p>
<dd>
<dd>Ensure <i>/dev/mapper</i> node exists after <code>dmsetup resume</code> (default with udev).</p>
<dt> <code>&#8211;checks</code></p>
<dd>
<dd>Perform additional checks on the operations requested and report potential problems. Useful when debugging scripts. In some cases these checks may slow down operations noticeably.</p>
<dt> <code>-c</code>|<code>-C</code>|<code>&#8211;columns</code></p>
<dd>
<dd>Display output in columns rather than as Field: Value lines.</p>
<dt> <code>&#8211;count</code> <i>count</i></p>
<dd>
<dd>Specify the number of times to repeat a report. Set this to zero continue until interrupted. The default interval is one second.</p>
<dt> <code>-f</code>|<code>&#8211;force</code></p>
<dd>
<dd>Try harder to complete operation.</p>
<dt> <code>-h</code>|<code>&#8211;help</code></p>
<dd>
<dd>Outputs a summary of the commands available, optionally including the list of report fields (synonym with <code>help</code> command).</p>
<dt> <code>&#8211;inactive</code></p>
<dd>
<dd>When returning any table information from the kernel report on the inactive table instead of the live table. Requires kernel driver version 4.16.0 or above.</p>
<dt> <code>&#8211;interval</code> <i>seconds</i></p>
<dd>
<dd>Specify the interval in seconds between successive iterations for repeating reports. If <code>&#8211;interval</code> is specified but <code>&#8211;count</code> is not, reports will continue to repeat until interrupted. The default interval is one second.</p>
<dt> <code>&#8211;manglename</code> <code>auto</code>|<code>hex</code>|<code>none</code></p>
<dd>
<dd>Mangle any character not on a whitelist using mangling_mode when processing device-mapper device names and UUIDs. The names and UUIDs are mangled on input and unmangled on output where the mangling mode is one of: <code>auto</code> (only do the mangling if not mangled yet, do nothing if already mangled, error on mixed), <code>hex</code> (always do the mangling) and <code>none</code> (no mangling). Default mode is <code>auto</code>. Character whitelist: 0-9, A-Z, a-z, #+-.:=@_. This whitelist is also supported by udev. Any character not on a whitelist is replaced with its hex value (two digits) prefixed by 
