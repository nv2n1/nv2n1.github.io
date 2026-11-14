---
title: "systemd-mount(1)"
name: "systemd-mount"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-mount/"
description: "systemd-mount, systemd-umount – Establish and destroy transient mount or auto-mount points"
---

<h2 class="name">NAME</h2>
<p> systemd-mount, systemd-umount &#8211; Establish and destroy transient mount or auto-mount points </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-mount</code> [<i>OPTIONS</i>&#8230;] <i>WHAT</i> [<i>WHERE</i>]</p>
<dt> <code>systemd-mount</code> [<i>OPTIONS</i>&#8230;] <code>&#8211;list</code></p>
<dt> <code>systemd-mount</code> [<i>OPTIONS</i>&#8230;] <code>&#8211;umount</code> <i>WHAT|WHERE</i>&#8230;</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-mount</code></p>
<dd>may be used to create and start a transient .mount or .automount unit of the file system <i>WHAT</i> on the mount point <i>WHERE</i>. </p>
<p> In many ways, <code>systemd-mount</code> is similar to the lower-level <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command, however instead of executing the mount operation directly and immediately, <code>systemd-mount</code> schedules it through the service manager job queue, so that it may pull in further dependencies (such as parent mounts, or a file system checker to execute a priori), and may make use of the auto-mounting logic. </p>
<p> The command takes either one or two arguments. If only one argument is specified it should refer to a block device or regular file containing a file system (e.g. &quot;/dev/sdb1&quot; or &quot;/path/to/disk.img&quot;). The block device or image file is then probed for a file system label and other metadata, and is mounted to a directory below /run/media/system/ whose name is generated from the file system label. In this mode the block device or image file must exist at the time of invocation of the command, so that it may be probed. If the device is found to be a removable block device (e.g. a USB stick), an automount point is created instead of a regular mount point (i.e. the <code>&#8211;automount=</code> option is implied, see below). </p>
<p> If two arguments are specified, the first indicates the mount source (the <i>WHAT</i>) and the second indicates the path to mount it on (the <i>WHERE</i>). In this mode no probing of the source is attempted, and a backing device node doesn&#8217;t have to exist. However, if this mode is combined with <code>&#8211;discover</code>, device node probing for additional metadata is enabled, and &#8211; much like in the single-argument case discussed above &#8211; the specified device has to exist at the time of invocation of the command. </p>
<p> Use the <code>&#8211;list</code> command to show a terse table of all local, known block devices with file systems that may be mounted with this command. </p>
<p> <code>systemd-umount</code> can be used to unmount a mount or automount point. It is the same as <code>systemd-mount</code> <code>&#8211;umount</code>.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;no-block</code></p>
<dl>
<dt>
<dd> Do not synchronously wait for the requested operation to finish. If this is not specified, the job will be verified, enqueued and <code>systemd-mount</code> will wait until the mount or automount unit&#8217;s start-up is completed. By passing this argument, it is only verified and enqueued.</dl>
<p> <code>-l</code>, <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Do not ellipsize the output when <code>&#8211;list</code> is specified.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<p> <code>&#8211;no-legend</code></p>
<dl>
<dt>
<dd> Do not print the legend, i.e. column headers and the footer with hints.</dl>
<p> <code>&#8211;no-ask-password</code></p>
<dl>
<dt>
<dd> Do not query the user for authentication for privileged operations.</dl>
<p> <code>&#8211;quiet</code>, <code>-q</code></p>
<dl>
<dt>
<dd> Suppresses additional informational output while running.</dl>
<p> <code>&#8211;discover</code></p>
<dl>
<dt>
<dd> Enable probing of the mount source. This switch is implied if a single argument is specified on the command line. If passed, additional metadata is read from the device to enhance the unit to create. For example, a descriptive string for the transient units is generated from the file system label and device model. Moreover if a removable block device (e.g. USB stick) is detected an automount unit instead of a regular mount unit is created, with a short idle timeout, in order to ensure the file-system is placed in a clean state quickly after each access.</dl>
<p> <code>&#8211;type=</code>, <code>-t</code></p>
<dl>
<dt>
<dd> Specifies the file system type to mount (e.g. &quot;vfat&quot; or &quot;ext4&quot;). If omitted or set to &quot;auto&quot;, the file system type is determined automatically.</dl>
<p> <code>&#8211;options=</code>, <code>-o</code></p>
<dl>
<dt>
<dd> Additional mount options for the mount point.</dl>
<p> <code>&#8211;owner=</code><i>USER</i></p>
<dl>
<dt>
<dd> Let the specified user <i>USER</i> own the mounted file system. This is done by appending <code>uid=</code> and <code>gid=</code> options to the list of mount options. Only certain file systems support this option.</dl>
<p> <code>&#8211;fsck=</code></p>
<dl>
<dt>
<dd> Takes a boolean argument, defaults to on. Controls whether to run a file system check immediately before the mount operation. In the automount case (see <code>&#8211;automount=</code> below) the check will be run the moment the first access to the device is made, which might slightly delay the access.</dl>
<p> <code>&#8211;description=</code></p>
<dl>
<dt>
<dd> Provide a description for the mount or automount unit. See <i>Description=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5).</dl>
<p> <code>&#8211;property=</code>, <code>-p</code></p>
<dl>
<dt>
<dd> Sets a unit property for the mount unit that is created. This takes an assignment in the same format as <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1)&#8217;s <code>set-property</code> command.</dl>
<p> <code>&#8211;automount=</code></p>
<dl>
<dt>
<dd> Takes a boolean argument. Controls whether to create an automount point or a regular mount point. If true an automount point is created that is backed by the actual file system at the time of first access. If false a plain mount point is created that is backed by the actual file system immediately. Automount points have the benefit that the file system stays unmounted and hence in clean state until it is first accessed. In automount mode the <code>&#8211;timeout-idle-sec=</code> switch (see below) may be used to ensure the mount point is unmounted automatically after the last access and an idle period passed. </p>
<p> If this switch is not specified it defaults to false. If not specified and <code>&#8211;discover</code> is used (or only a single argument passed, which implies <code>&#8211;discover</code>, see above), and the file system block device is detected to be removable, it is set to true, in order to increase the chance that the file system is in a fully clean state if the device is unplugged abruptly.</dl>
<p> <code>-A</code></p>
<dl>
<dt>
<dd> Equivalent to <code>&#8211;automount=yes</code>.</dl>
<p> <code>&#8211;timeout-idle-sec=</code></p>
<dl>
<dt>
<dd> Takes a time value that controls the idle timeout in automount mode. If set to &quot;infinity&quot; (the default) no automatic unmounts are done. Otherwise the file system backing the automount point is detached after the last access and the idle timeout passed. See <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7) for details on the time syntax supported. This option has no effect if only a regular mount is established, and automounting is not used. </p>
<p> Note that if <code>&#8211;discover</code> is used (or only a single argument passed, which implies <code>&#8211;discover</code>, see above), and the file system block device is detected to be removable, <code>&#8211;timeout-idle-sec=1s</code> is implied.</dl>
<p> <code>&#8211;automount-property=</code></p>
<dl>
<dt>
<dd> Similar to <code>&#8211;property=</code>, but applies additional properties to the automount unit created, instead of the mount unit.</dl>
<p> <code>&#8211;bind-device</code></p>
<dl>
<dt>
<dd> This option only has an effect in automount mode, and controls whether the automount unit shall be bound to the backing device&#8217;s lifetime. If set, the automount point will be removed automatically when the backing device vanishes. By default the automount point stays around, and subsequent accesses will block until backing device is replugged. This option has no effect in case of non-device mounts, such as network or virtual file system mounts. </p>
<p> Note that if <code>&#8211;discover</code> is used (or only a single argument passed, which implies <code>&#8211;discover</code>, see above), and the file system block device is detected to be removable, this option is implied.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Instead of establishing a mount or automount point, print a terse list of block devices containing file systems that may be mounted with &quot;systemd-mount&quot;, along with useful metadata such as labels, etc.</dl>
<p> <code>-u</code>, <code>&#8211;umount</code></p>
<dl>
<dt>
<dd> Stop the mount and automount units corresponding to the specified mount points <i>WHERE</i> or the devices <i>WHAT</i>. <code>systemd-mount</code> with this option or <code>systemd-umount</code> can take multiple arguments which can be mount points, devices, /etc/fstab style node names, or backing files corresponding to loop devices, like <code>systemd-mount &#8211;umount /path/to/umount /dev/sda1 UUID=xxxxxx-xxxx LABEL=xxxxx /path/to/disk.img</code>. Note that when <code>-H</code> or <code>-M</code> is specified, only absolute paths to mount points are supported.</dl>
<p> <code>-G</code>, <code>&#8211;collect</code></p>
<dl>
<dt>
<dd> Unload the transient unit after it completed, even if it failed. Normally, without this option, all mount units that mount and failed are kept in memory until the user explicitly resets their failure state with <code>systemctl reset-failed</code> or an equivalent command. On the other hand, units that stopped successfully are unloaded immediately. If this option is turned on the &quot;garbage collection&quot; of units is more aggressive, and unloads units regardless if they exited successfully or failed. This option is a shortcut for <code>&#8211;property=CollectMode=inactive-or-failed</code>, see the explanation for <i>CollectMode=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for further information.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Talk to the service manager of the calling user, rather than the service manager of the system.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Talk to the service manager of the system. This is the implied default.</dl>
<p> <code>-H</code>, <code>&#8211;host=</code></p>
<dl>
<dt>
<dd> Execute the operation remotely. Specify a hostname, or a username and hostname separated by &quot;@&quot;, to connect to. The hostname may optionally be suffixed by a port ssh is listening on, separated by &quot;:&quot;, and then a container name, separated by &quot;/&quot;, which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with <code>machinectl -H </code><i>HOST</i>. Put IPv6 addresses in brackets.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Execute operation on a local container. Specify a container name to connect to, optionally prefixed by a user name to connect as and a separating &quot;@&quot; character. If the special string &quot;.host&quot; is used in place of the container name, a connection to the local system is made (which is useful to connect to a specific user&#8217;s user bus: &quot;&#8211;user &#8211;machine=lennart [at] .host&quot;). If the &quot;@&quot; syntax is not used, the connection is made as root user. If the &quot;@&quot; syntax is used either the left hand side or the right hand side may be omitted (but not both) in which case the local user name and &quot;.host&quot; are implied.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>THE UDEV DATABASE</h2>
<p> If <code>&#8211;discover</code> is used, <code>systemd-mount</code> honors a couple of additional udev properties of block devices: </p>
<p> <i>SYSTEMD_MOUNT_OPTIONS=</i></p>
<dl>
<dt>
<dd> The mount options to use, if <code>&#8211;options=</code> is not used.</dl>
<p> <i>SYSTEMD_MOUNT_WHERE=</i></p>
<dl>
<dt>
<dd> The file system path to place the mount point at, instead of the automatically generated one.</dl>
<h2>EXAMPLE</h2>
<p> Use a udev rule like the following to automatically mount all USB storage plugged in: </p>
<dl>
<dt>
<dd>
<pre><code>
ACTION == "add", SUBSYSTEMS == "usb", SUBSYSTEM == "block", ENV{ID_FS_USAGE} == "filesystem",
    RUN{program} += "/usr/bin/systemd-mount --no-block --automount=yes --collect $devnode"
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5), <code><a href="/docs/linux/man/1-systemd-run/">systemd-run</a></code>(1) </p>
<h2>Index</h2>
