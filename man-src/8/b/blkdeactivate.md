---
title: "blkdeactivate(8)"
name: "blkdeactivate"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blkdeactivate/"
description: "blkdeactivate — utility to deactivate block devices"
---

<p>blkdeactivate &#8212; utility to deactivate block devices</p>
<h2>Synopsis</h2>
<p><code>blkdeactivate</code> [<code>-d</code>&nbsp;<i>dm_options</i>] [<code>-e</code>] [<code>-h</code>] [<code>-l</code>&nbsp;<i>lvm_options</i>] [<code>-m</code>&nbsp;<i>mpath_options</i>] [<code>-r</code>&nbsp;<i>mdraid_options</i>] [<code>-o</code>&nbsp;<i>vdo_options</i>] [<code>-u</code>] [<code>-v</code>] [<i>device</i>]</p>
<h2>Description</h2>
<p>The blkdeactivate utility deactivates block devices. For mounted block devices, it attempts to unmount it automatically before trying to deactivate. The utility currently supports device-mapper devices (DM), including LVM volumes and software RAID MD devices. LVM volumes are handled directly using the <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) command, the rest of device-mapper based devices are handled using the <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8) command. MD devices are handled using the <code><a href="/docs/linux/man/8-mdadm/">mdadm</a></code>(8) command.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;dmoptions</code>&nbsp;<i>dm_options</i></p>
<dd>Comma separated list of device-mapper specific options. Accepted <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8) options are:</p>
<dl>
<dd>
<dl>
<dt><i>retry</i></p>
<dd>Retry removal several times in case of failure.</p>
<dt><i>force</i></p>
<dd>Force device removal.</dl>
</dl>
<dt><code>-e</code>, <code>&#8211;errors</code></p>
<dd>Show errors reported from tools called by <code>blkdeactivate</code>. Without this option, any error messages from these external tools are suppressed and the <code>blkdeactivate</code> itself provides only a summary message to indicate the device was skipped.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display the help text.</p>
<dt><code>-l</code>, <code>&#8211;lvmoptions</code>&nbsp;<i>lvm_options</i></p>
<dd>Comma-separated list of LVM specific options:</p>
<dl>
<dd>
<dl>
<dt><i>retry</i></p>
<dd>Retry removal several times in case of failure.</p>
<dt><i>wholevg</i></p>
<dd>Deactivate the whole LVM Volume Group when processing a Logical Volume. Deactivating the Volume Group as a whole is quicker than deactivating each Logical Volume separately.</dl>
</dl>
<dt><code>-m</code>, <code>&#8211;mpathoptions</code>&nbsp;<i>mpath_options</i></p>
<dd>Comma-separated list of device-mapper multipath specific options:</p>
<dl>
<dd>
<dl>
<dt><i>disablequeueing</i></p>
<dd>Disable queueing on all multipath devices before deactivation. This avoids a situation where blkdeactivate may end up waiting if all the paths are unavailable for any underlying device-mapper multipath device.</dl>
</dl>
<dt><code>-r</code>, <code>&#8211;mdraidoptions</code>&nbsp;<i>mdraid_options</i></p>
<dd>Comma-separated list of MD RAID specific options:</p>
<dl>
<dd>
<dl>
<dt><i>wait</i></p>
<dd>Wait MD device&#8217;s resync, recovery or reshape action to complete before deactivation.</dl>
</dl>
<dt><code>-o</code>, <code>&#8211;vdooptions</code>&nbsp;<i>vdo_options</i></p>
<dd>Comma-separated list of VDO specific options:</p>
<dl>
<dd>
<dl>
<dt><i>configfile=file</i></p>
<dd>Use specified VDO configuration file.</dl>
</dl>
<dt><code>-u</code>, <code>&#8211;umount</code></p>
<dd>Unmount a mounted device before trying to deactivate it. Without this option used, a device that is mounted is not deactivated.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Run in verbose mode. Use &#8211;vv for even more verbose mode.</dl>
<h2>Examples</h2>
<p>Deactivate all supported block devices found in the system, skipping mounted devices. # <code>blkdeactivate</code> </p>
<p> Deactivate all supported block devices found in the system, unmounting any mounted devices first, if possible. # <code>blkdeactivate -u</code> </p>
<p> Deactivate the device /dev/vg/lvol0 together with all its holders, unmounting any mounted devices first, if possible. # <code>blkdeactivate -u /dev/vg/lvol0</code> </p>
<p> Deactivate all supported block devices found in the system. If the deactivation of a device-mapper device fails, retry it. Deactivate the whole Volume Group at once when processing an LVM Logical Volume. # <code>blkdeactivate -u -d retry -l wholevg</code> </p>
<p> Deactivate all supported block devices found in the system. If the deactivation of a device-mapper device fails, retry it and force removal. # <code>blkdeactivate -d force,retry</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8), <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8), <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/8-mdadm/">mdadm</a></code>(8), <code><a href="/docs/linux/man/8-multipathd/">multipathd</a></code>(8), <code><a href="/docs/linux/man/8-vdo/">vdo</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) </p>
