---
title: "lvmdump(8)"
name: "lvmdump"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvmdump/"
description: "lvmdump — create lvm2 information dumps for diagnostic purposes"
---

<p>lvmdump &#8212; create lvm2 information dumps for diagnostic purposes</p>
<h2>Synopsis</h2>
<p><code>lvmdump</code> [<code>-a</code>] [<code>-c</code>] [<code>-d</code> <i>directory</i>] [<code>-h</code>] [<code>-l</code>] [<code>-m</code>] [<code>-p</code>] [<code>-s</code>] [<code>-u</code>]</p>
<h2>Description</h2>
<p>lvmdump is a tool to dump various information concerning LVM2. By default, it creates a tarball suitable for submission along with a problem report. </p>
<p> The content of the tarball is as follows:<br />
 &#8211; dmsetup info<br />
 &#8211; table of currently running processes<br />
 &#8211; recent entries from /var/log/messages (containing system messages)<br />
 &#8211; complete lvm configuration and cache (content of /etc/lvm)<br />
 &#8211; list of device nodes present under /dev<br />
 &#8211; list of files present /sys/block<br />
 &#8211; list of files present /sys/devices/virtual/block<br />
 &#8211; if enabled with -m, metadata dump will be also included<br />
 &#8211; if enabled with -a, debug output of vgscan, pvscan and list of all available volume groups, physical volumes and logical volumes will be included<br />
 &#8211; if enabled with -l, lvmetad state if running<br />
 &#8211; if enabled with -p, lvmpolld state if running<br />
 &#8211; if enabled with -s, system info and context<br />
 &#8211; if enabled with -u, udev info and context</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Advanced collection. <code>WARNING</code>: if lvm is already hung, then this script may hang as well if <code>-a</code> is used.</p>
<dt><code>-d </code><i>directory</i></p>
<dd>Dump into a directory instead of tarball By default, lvmdump will produce a single compressed tarball containing all the information. Using this option, it can be instructed to only produce the raw dump tree, rooted in <i>directory</i>.</p>
<dt><code>-h</code></p>
<dd>Print help message</p>
<dt><code>-l</code></p>
<dd>Include <code><a href="/docs/linux/man/8-lvmetad/">lvmetad</a></code>(8) daemon dump if it is running. The dump contains cached information that is currently stored in lvmetad: VG metadata, PV metadata and various mappings in between these metadata for quick access.</p>
<dt><code>-m</code></p>
<dd>Gather LVM metadata from the PVs This option generates a 1:1 dump of the metadata area from all PVs visible to the system, which can cause the dump to increase in size considerably. However, the metadata dump may represent a valuable diagnostic resource.</p>
<dt><code>-p</code></p>
<dd>Include <code><a href="/docs/linux/man/8-lvmpolld/">lvmpolld</a></code>(8) daemon dump if it is running. The dump contains all in-progress operation currently monitored by the daemon and partial history for all yet uncollected results of polling operations already finished including reason.</p>
<dt><code>-s</code></p>
<dd>Gather system info and context. Currently, this encompasses info gathered by calling lsblk command and various systemd info and context: overall state of systemd units present in the system, more detailed status of units controlling LVM functionality and the content of systemd journal for current boot.</p>
<dt><code>-u</code></p>
<dd>Gather udev info and context: /etc/udev/udev.conf file, udev daemon version (output of &#8216;udevadm info &#8211;version&#8217; command), udev rules currently used in the system (content of /lib/udev/rules.d and /etc/udev/rules.d directory), list of files in /lib/udev directory and dump of current udev database content (the output of &#8216;udevadm info &#8211;export-db&#8217; command).</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>LVM_BINARY</code></p>
<dd>The LVM2 binary to use. Defaults to &quot;lvm&quot;. Sometimes you might need to set this to &quot;/sbin/lvm.static&quot;, for example.</p>
<dt><code>DMSETUP_BINARY</code></p>
<dd>The dmsetup binary to use. Defaults to &quot;dmsetup&quot;.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) </p>
