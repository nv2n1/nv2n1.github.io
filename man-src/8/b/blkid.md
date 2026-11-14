---
title: "blkid(8)"
name: "blkid"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blkid/"
description: "blkid – locate/print block device attributes"
---

<p>blkid &#8211; locate/print block device attributes</p>
<h2>Synopsis</h2>
<p><code>blkid</code> <code>&#8211;label</code> <i>label</i> | <code>&#8211;uuid</code> <i>uuid</i> </p>
<p> <code>blkid</code> [<code>&#8211;no-encoding</code> <code>&#8211;garbage-collect</code> <code>&#8211;list-one</code> <code>&#8211;cache-file</code> <i>file</i>] [<code>&#8211;output</code> <i>format</i>] [<code>&#8211;match-tag</code> <i>tag</i>] [<code>&#8211;match-token</code> <i>NAME=value</i>] [<i>device</i>&#8230;] </p>
<p> <code>blkid</code> <code>&#8211;probe</code> [<code>&#8211;offset</code> <i>offset</i>] [<code>&#8211;output</code> <i>format</i>] [<code>&#8211;size</code> <i>size</i>] [<code>&#8211;match-tag</code> <i>tag</i>] [<code>&#8211;match-types</code> <i>list</i>] [<code>&#8211;usages</code> <i>list</i>] [<code>&#8211;no-part-details</code>] <i>device</i>&#8230; </p>
<p> <code>blkid</code> <code>&#8211;info</code> [<code>&#8211;output format</code>] [<code>&#8211;match-tag</code> <i>tag</i>] <i>device</i>&#8230;</p>
<h2>Description</h2>
<p>The <code>blkid</code> program is the command-line interface to working with the <code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3) library. It can determine the type of content (e.g., filesystem or swap) that a block device holds, and also the attributes (tokens, NAME=value pairs) from the content metadata (e.g., LABEL or UUID fields). </p>
<p> <code>It is recommended to use</code> <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8) <code>command to get information about block devices, or lsblk &#8211;fs to get an overview of filesystems, or</code> <code><a href="/docs/linux/man/8-findmnt/">findmnt</a></code>(8) <code>to search in already mounted filesystems.</code></p>
<dl>
<dd><code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8) provides more information, better control on output formatting, easy to use in scripts and it does not require root permissions to get actual information. <code>blkid</code> reads information directly from devices and for non-root users it returns cached unverified information. <code>blkid</code> is mostly designed for system services and to test <code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3) functionality.
</dl>
<p> When <i>device</i> is specified, tokens from only this device are displayed. It is possible to specify multiple <i>device</i> arguments on the command line. If none is given, all partitions or unpartitioned devices which appear in <i>/proc/partitions</i> are shown, if they are recognized. </p>
<p> <code>blkid</code> has two main forms of operation: either searching for a device with a specific NAME=value pair, or displaying NAME=value pairs for one or more specified devices. </p>
<p> For security reasons <code>blkid</code> silently ignores all devices where the probing result is ambivalent (multiple colliding filesystems are detected). The low-level probing mode (<code>-p</code>) provides more information and extra exit status in this case. It&#8217;s recommended to use <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8) to get a detailed overview and to erase obsolete stuff (magic strings) from the device.</p>
<h2>Options</h2>
<p>The <i>size</i> and <i>offset</i> arguments may be followed by the multiplicative suffixes like KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;), or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB. </p>
<p> <code>-c</code>, <code>&#8211;cache-file</code> <i>cachefile</i></p>
<dl>
<dd>Read from <i>cachefile</i> instead of reading from the default cache file (see the CONFIGURATION FILE section for more details). If you want to start with a clean cache (i.e., don&#8217;t report devices previously scanned but not necessarily available at this time), specify <i>/dev/null</i>.</dl>
<p> <code>-d</code>, <code>&#8211;no-encoding</code></p>
<dl>
<dd>Don&#8217;t encode non-printing characters. The non-printing characters are encoded by ^ and M- notation by default. Note that the <code>&#8211;output udev</code> output format uses a different encoding which cannot be disabled.</dl>
<p> <code>-D</code>, <code>&#8211;no-part-details</code></p>
<dl>
<dd>Don&#8217;t print information (PART_ENTRY_* tags) from partition table in low-level probing mode.</dl>
<p> <code>-g</code>, <code>&#8211;garbage-collect</code></p>
<dl>
<dd>Perform a garbage collection pass on the blkid cache to remove devices which no longer exist.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display a usage message and exit.</dl>
<p> <code>-H</code>, <code>&#8211;hint</code> <i>setting</i></p>
<dl>
<dd>Set probing hint. The hints are optional way how to force probing functions to check for example another location. The currently supported is &quot;session_offset=<i>number</i>&quot; to set session offset on multi-session UDF.</dl>
<p> <code>-i</code>, <code>&#8211;info</code></p>
<dl>
<dd>Display information about I/O Limits (aka I/O topology). The &#8216;export&#8217; output format is automatically enabled. This option can be used together with the <code>&#8211;probe</code> option.</dl>
<p> <code>-k</code>, <code>&#8211;list-filesystems</code></p>
<dl>
<dd>List all known filesystems and RAIDs and exit.</dl>
<p> <code>-l</code>, <code>&#8211;list-one</code></p>
<dl>
<dd>Look up only one device that matches the search parameter specified with the <code>&#8211;match-token</code> option. If there are multiple devices that match the specified search parameter, then the device with the highest priority is returned, and/or the first device found at a given priority (but see below note about udev). Device types in order of decreasing priority are: Device Mapper, EVMS, LVM, MD, and finally regular block devices. If this option is not specified, <code>blkid</code> will print all of the devices that match the search parameter. </p>
<p> This option forces <code>blkid</code> to use udev when used for LABEL or UUID tokens in <code>&#8211;match-token</code>. The goal is to provide output consistent with other utils (like <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), etc.) on systems where the same tag is used for multiple devices.</dl>
<p> <code>-L</code>, <code>&#8211;label</code> <i>label</i></p>
<dl>
<dd>Look up the device that uses this filesystem <i>label</i>; this is equal to <code>&#8211;list-one &#8211;output device &#8211;match-token LABEL=</code><i>label</i>. This lookup method is able to reliably use /dev/disk/by-label udev symlinks (dependent on a setting in <i>/etc/blkid.conf</i>). Avoid using the symlinks directly; it is not reliable to use the symlinks without verification. The <code>&#8211;label</code> option works on systems with and without udev. </p>
<p> Unfortunately, the original <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8) from e2fsprogs uses the <code>-L</code> option as a synonym for <code>-o list</code>. For better portability, use <code>-l -o device -t LABEL=</code><i>label</i> and <code>-o list</code> in your scripts rather than the <code>-L</code> option.</dl>
<p> <code>-n</code>, <code>&#8211;match-types</code> <i>list</i></p>
<dl>
<dd>Restrict the probing functions to the specified (comma-separated) <i>list</i> of superblock types (names). The list items may be prefixed with &quot;no&quot; to specify the types which should be ignored. For example: </p>
<p> <code>blkid &#8211;probe &#8211;match-types vfat,ext3,ext4 /dev/sda1</code> </p>
<p> probes for vfat, ext3 and ext4 filesystems, and </p>
<p> <code>blkid &#8211;probe &#8211;match-types nominix /dev/sda1</code> </p>
<p> probes for all supported formats except minix filesystems. This option is only useful together with <code>&#8211;probe</code>.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>format</i></p>
<dl>
<dd>Use the specified output format. Note that the order of variables and devices is not fixed. See also option <code>-s</code>. The <i>format</i> parameter may be: </p>
<p> <code>full</code></p>
<dl>
<dd>print all tags (the default)</dl>
<p> <code>value</code></p>
<dl>
<dd>print the value of the tags</dl>
<p> <code>list</code></p>
<dl>
<dd>print the devices in a user-friendly format; this output format is unsupported for low-level probing (<code>&#8211;probe</code> or <code>&#8211;info</code>). </p>
<p> This output format is <code>DEPRECATED</code> in favour of the <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8) command.</dl>
<p> <code>device</code></p>
<dl>
<dd>print the device name only; this output format is always enabled for the <code>&#8211;label</code> and <code>&#8211;uuid</code> options</dl>
<p> <code>udev</code></p>
<dl>
<dd>print key=&quot;value&quot; pairs for easy import into the udev environment; the keys are prefixed by ID_FS_ or ID_PART_ prefixes. The value may be modified to be safe for udev environment; allowed is plain ASCII, hex-escaping and valid UTF-8, everything else (including whitespaces) is replaced with &#8216;_&#8217;. The keys with <i>_ENC</i> postfix use hex-escaping for unsafe chars. </p>
<p> The udev output returns the ID_FS_AMBIVALENT tag if more superblocks are detected, and ID_PART_ENTRY_* tags are always returned for all partitions including empty partitions. </p>
<p> This output format is <code>DEPRECATED</code>.</dl>
<p> <code>export</code></p>
<dl>
<dd>print key=value pairs for easy import into the environment; this output format is automatically enabled when I/O Limits (<code>&#8211;info</code> option) are requested. </p>
<p> The non-printing characters are encoded by ^ and M- notation and all potentially unsafe characters are escaped.</dl>
</dl>
<p> <code>-O</code>, <code>&#8211;offset</code> <i>offset</i></p>
<dl>
<dd>Probe at the given <i>offset</i> (only useful with <code>&#8211;probe</code>). This option can be used together with the <code>&#8211;info</code> option.</dl>
<p> <code>-p</code>, <code>&#8211;probe</code></p>
<dl>
<dd>Switch to low-level superblock probing mode (bypassing the cache). </p>
<p> Note that low-level probing also returns information about partition table type (PTTYPE tag) and partitions (PART_ENTRY_* tags). The tag names produced by low-level probing are based on names used internally by libblkid and it may be different than when executed without <code>&#8211;probe</code> (for example PART_ENTRY_UUID= vs PARTUUID=). See also <code>&#8211;no-part-details</code>.</dl>
<p> <code>-s</code>, <code>&#8211;match-tag</code> <i>tag</i></p>
<dl>
<dd>For each (specified) device, show only the tags that match <i>tag</i>. It is possible to specify multiple <code>&#8211;match-tag</code> options. If no tag is specified, then all tokens are shown for all (specified) devices. In order to just refresh the cache without showing any tokens, use <code>&#8211;match-tag none</code> with no other options.</dl>
<p> <code>-S</code>, <code>&#8211;size</code> <i>size</i></p>
<dl>
<dd>Override the size of device/file (only useful with <code>&#8211;probe</code>).</dl>
<p> <code>-t</code>, <code>&#8211;match-token</code> <i>NAME=value</i></p>
<dl>
<dd>Search for block devices with tokens named <i>NAME</i> that have the value <i>value</i>, and display any devices which are found. Common values for <i>NAME</i> include <code>TYPE</code>, <code>LABEL</code>, and <code>UUID</code>. If there are no devices specified on the command line, all block devices will be searched; otherwise only the specified devices are searched.</dl>
<p> <code>-u</code>, <code>&#8211;usages</code> <i>list</i></p>
<dl>
<dd>Restrict the probing functions to the specified (comma-separated) <i>list</i> of &quot;usage&quot; types. Supported usage types are: filesystem, raid, crypto and other. The list items may be prefixed with &quot;no&quot; to specify the usage types which should be ignored. For example: </p>
<p> <code>blkid &#8211;probe &#8211;usages filesystem,other /dev/sda1</code> </p>
<p> probes for all filesystem and other (e.g., swap) formats, and </p>
<p> <code>blkid &#8211;probe &#8211;usages noraid /dev/sda1</code> </p>
<p> probes for all supported formats except RAIDs. This option is only useful together with <code>&#8211;probe</code>.</dl>
<p> <code>-U</code>, <code>&#8211;uuid</code> <i>uuid</i></p>
<dl>
<dd>Look up the device that uses this filesystem <i>uuid</i>. For more details see the <code>&#8211;label</code> option.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version number and exit.</dl>
<h2>Exit Status</h2>
<p>If the specified device or device addressed by specified token (option <code>&#8211;match-token</code>) was found and it&#8217;s possible to gather any information about the device, an exit status 0 is returned. Note the option <code>&#8211;match-tag</code> filters output tags, but it does not affect exit status. </p>
<p> If the specified token was not found, or no (specified) devices could be identified, or it is impossible to gather any information about the device identifiers or device content an exit status of 2 is returned. </p>
<p> For usage or other errors, an exit status of 4 is returned. </p>
<p> If an ambivalent probing result was detected by low-level probing mode (<code>-p</code>), an exit status of 8 is returned.</p>
<h2>Configuration File</h2>
<p>The standard location of the <i>/etc/blkid.conf</i> config file can be overridden by the environment variable BLKID_CONF. The following options control the libblkid library: </p>
<p> <i>SEND_UEVENT=&lt;yes|not&gt;</i></p>
<dl>
<dd>Sends uevent when <i>/dev/disk/by-{label,uuid,partuuid,partlabel}/</i> symlink does not match with LABEL, UUID, PARTUUID or PARTLABEL on the device. Default is &quot;yes&quot;.</dl>
<p> <i>CACHE_FILE=&lt;path&gt;</i></p>
<dl>
<dd>Overrides the standard location of the cache file. This setting can be overridden by the environment variable <code>BLKID_FILE</code>. Default is <i>/run/blkid/blkid.tab</i>, or <i>/etc/blkid.tab</i> on systems without a <i>/run</i> directory.</dl>
<p> <i>EVALUATE=&lt;methods&gt;</i></p>
<dl>
<dd>Defines LABEL and UUID evaluation method(s). Currently, the libblkid library supports the &quot;udev&quot; and &quot;scan&quot; methods. More than one method may be specified in a comma-separated list. Default is &quot;udev,scan&quot;. The &quot;udev&quot; method uses udev <i>/dev/disk/by-*</i> symlinks and the &quot;scan&quot; method scans all block devices from the <i>/proc/partitions</i> file.</dl>
<h2>Environment</h2>
<p>Setting <i>LIBBLKID_DEBUG=all</i> enables debug output.</p>
<h2>Authors</h2>
<p><code>blkid</code> was written by Andreas Dilger for libblkid and improved by Theodore Ts&#8217;o and Karel Zak.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3), <code><a href="/docs/linux/man/8-findfs/">findfs</a></code>(8), <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8), <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>blkid</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
