---
title: "systemd-fstab-generator(8)"
name: "systemd-fstab-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-fstab-generator/"
description: "systemd-fstab-generator – Unit generator for /etc/fstab"
---

<p>systemd-fstab-generator &#8211; Unit generator for /etc/fstab</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-fstab-generator</p>
<h2>Description</h2>
<p>systemd-fstab-generator is a generator that translates /etc/fstab (see <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) for details) into native systemd units early at boot and when configuration of the system manager is reloaded. This will instantiate mount and swap units as necessary. </p>
<p> The <i>passno</i> field is treated like a simple boolean, and the ordering information is discarded. However, if the root file system is checked, it is checked before all the other file systems. </p>
<p> See <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5) for more information about special /etc/fstab mount options this generator understands. </p>
<p> One special topic is handling of symbolic links. Historical init implementations supported symlinks in /etc/fstab. Because mount units will refuse mounts where the target is a symbolic link, this generator will resolve any symlinks as far as possible when processing /etc/fstab in order to enhance backwards compatibility. If a symlink target does not exist at the time that this generator runs, it is assumed that the symlink target is the final target of the mount. </p>
<p> systemd-fstab-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>Kernel Command Line</h2>
<p>systemd-fstab-generator understands the following kernel command line parameters: </p>
<p> <i>fstab=</i>, <i>rd.fstab=</i></p>
<dl>
<dd>Takes a boolean argument. Defaults to &quot;yes&quot;. If &quot;no&quot;, causes the generator to ignore any mounts or swap devices configured in /etc/fstab. <i>rd.fstab=</i> is honored only by the initial RAM disk (initrd) while <i>fstab=</i> is honored by both the main system and the initrd.</dl>
<p> <i>root=</i></p>
<dl>
<dd>Configures the operating system&#8217;s root filesystem to mount when running in the initrd. This accepts a device node path (usually /dev/disk/by-uuid/&#8230; or /dev/disk/by-label/&#8230; or similar), or the special values &quot;gpt-auto&quot; and &quot;tmpfs&quot;. </p>
<p> Use &quot;gpt-auto&quot; to explicitly request automatic root file system discovery via <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8). </p>
<p> Use &quot;tmpfs&quot; in order to mount a <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) file system as root file system of the OS. This is useful in combination with <i>mount.usr=</i> (see below) in order to combine a volatile root file system with a separate, immutable /usr/ file system. Also see <i>systemd.volatile=</i> below.</dl>
<p> <i>rootfstype=</i></p>
<dl>
<dd>Takes the root filesystem type that will be passed to the mount command. <i>rootfstype=</i> is honored by the initrd.</dl>
<p> <i>rootflags=</i></p>
<dl>
<dd>Takes the root filesystem mount options to use. <i>rootflags=</i> is honored by the initrd. </p>
<p> Note that unlike most kernel command line options this setting does not override settings made in configuration files (specifically: the mount option string in /etc/fstab). See <code><a href="/docs/linux/man/8-systemd-remount-fs-service/">systemd-remount-fs.service</a></code>(8).</dl>
<p> <i>mount.usr=</i></p>
<dl>
<dd>Takes the /usr/ filesystem to be mounted by the initrd. If <i>mount.usrfstype=</i> or <i>mount.usrflags=</i> is set, then <i>mount.usr=</i> will default to the value set in <i>root=</i>. </p>
<p> Otherwise, this parameter defaults to the /usr/ entry found in /etc/fstab on the root filesystem. </p>
<p> <i>mount.usr=</i> is honored by the initrd.</dl>
<p> <i>mount.usrfstype=</i></p>
<dl>
<dd>Takes the /usr/ filesystem type that will be passed to the mount command. If <i>mount.usr=</i> or <i>mount.usrflags=</i> is set, then <i>mount.usrfstype=</i> will default to the value set in <i>rootfstype=</i>. </p>
<p> Otherwise, this value will be read from the /usr/ entry in /etc/fstab on the root filesystem. </p>
<p> <i>mount.usrfstype=</i> is honored by the initrd.</dl>
<p> <i>mount.usrflags=</i></p>
<dl>
<dd>Takes the /usr/ filesystem mount options to use. If <i>mount.usr=</i> or <i>mount.usrfstype=</i> is set, then <i>mount.usrflags=</i> will default to the value set in <i>rootflags=</i>. </p>
<p> Otherwise, this value will be read from the /usr/ entry in /etc/fstab on the root filesystem. </p>
<p> <i>mount.usrflags=</i> is honored by the initrd.</dl>
<p> <i>systemd.volatile=</i></p>
<dl>
<dd>Controls whether the system shall boot up in volatile mode. Takes a boolean argument or the special value <code>state</code>. </p>
<p> If false (the default), this generator makes no changes to the mount tree and the system is booted up in normal mode. </p>
<p> If true the generator ensures <code><a href="/docs/linux/man/8-systemd-volatile-root-service/">systemd-volatile-root.service</a></code>(8) is run as part of the initial RAM disk (&quot;initrd&quot;). This service changes the mount table before transitioning to the host system, so that a volatile memory file system (&quot;tmpfs&quot;) is used as root directory, with only /usr/ mounted into it from the configured root file system, in read-only mode. This way the system operates in fully stateless mode, with all configuration and state reset at boot and lost at shutdown, as /etc/ and /var/ will be served from the (initially unpopulated) volatile memory file system. </p>
<p> If set to <code>state</code> the generator will leave the root directory mount point unaltered, however will mount a &quot;tmpfs&quot; file system to /var/. In this mode the normal system configuration (i.e. the contents of &quot;/etc/&quot;) is in effect (and may be modified during system runtime), however the system state (i.e. the contents of &quot;/var/&quot;) is reset at boot and lost at shutdown. </p>
<p> If this setting is set to &quot;overlay&quot; the root file system is set up as &quot;overlayfs&quot; mount combining the read-only root directory with a writable &quot;tmpfs&quot;, so that no modifications are made to disk, but the file system may be modified nonetheless with all changes being lost at reboot. </p>
<p> Note that in none of these modes the root directory, /etc/, /var/ or any other resources stored in the root file system are physically removed. It&#8217;s thus safe to boot a system that is normally operated in non-volatile mode temporarily into volatile mode, without losing data. </p>
<p> Note that with the exception of &quot;overlay&quot; mode, enabling this setting will only work correctly on operating systems that can boot up with only /usr/ mounted, and are able to automatically populate /etc/, and also /var/ in case of &quot;systemd.volatile=yes&quot;. </p>
<p> Also see <i>root=tmpfs</i> above, for a method to combine a &quot;tmpfs&quot; file system with a regular /usr/ file system (as configured via <i>mount.usr=</i>). The main distinction between <i>systemd.volatile=yes</i>, and <i>root=tmpfs</i> in combination <i>mount.usr=</i> is that the former operates on top of a regular root file system and temporarily obstructs the files and directories above its /usr/ subdirectory, while the latter does not hide any files, but simply mounts a unpopulated tmpfs as root file system and combines it with a user picked /usr/ file system.</dl>
<p> <i>systemd.swap</i></p>
<dl>
<dd>Takes a boolean argument or enables the option if specified without an argument. If disabled, causes the generator to ignore any swap devices configured in /etc/fstab. Defaults to enabled.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/8-systemd-cryptsetup-generator/">systemd-cryptsetup-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8), <code><a href="/docs/linux/man/7-kernel-command-line/">kernel-command-line</a></code>(7) </p>
