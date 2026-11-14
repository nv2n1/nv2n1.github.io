---
title: "systemd-automount(5)"
name: "systemd-automount"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-automount/"
description: "systemd.automount – Automount unit configuration"
---

<p>systemd.automount &#8211; Automount unit configuration</p>
<h2>Synopsis</h2>
<p><i>automount</i>.automount</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.automount&quot; encodes information about a file system automount point controlled and supervised by systemd. </p>
<p> This man page lists the configuration options specific to this unit type. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. The automount specific configuration options are configured in the [Automount] section. </p>
<p> Automount units must be named after the automount directories they control. Example: the automount point /home/lennart must be configured in a unit file home-lennart.automount. For details about the escaping logic used to convert a file system path to a unit name see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). Note that automount units cannot be templated, nor is it possible to add multiple names to an automount unit by creating additional symlinks to its unit file. </p>
<p> For each automount unit file a matching mount unit file (see <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5) for details) must exist which is activated when the automount path is accessed. Example: if an automount unit home-lennart.automount is active and the user accesses /home/lennart the mount unit home-lennart.mount will be activated. </p>
<p> Automount units may be used to implement on-demand mounting as well as parallelized mounting of file systems. </p>
<p> Note that automount units are separate from the mount itself, so you should not set <i>After=</i> or <i>Requires=</i> for mount dependencies here. For example, you should not set <i>After=network-online.target</i> or similar on network filesystems. Doing so may result in an ordering cycle. </p>
<p> Note that automount support on Linux is privileged, automount units are hence only available in the system service manager (and root&#8217;s user service manager), but not in unprivileged user&#8217;s service manager.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>The following dependencies are implicitly added: </p>
<dl>
<dd>&bull; If an automount unit is beneath another mount unit in the file system hierarchy, both a requirement and an ordering dependency between both units are created automatically.</dl>
<dl>
<dd>&bull; An implicit <i>Before=</i> dependency is created between an automount unit and the mount unit it activates.</dl>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; Automount units acquire automatic <i>Before=</i> and <i>Conflicts=</i> on umount.target in order to be stopped during shutdown.</dl>
<dl>
<dd>&bull; Automount units automatically gain an <i>After=</i> dependency on local-fs-pre.target, and a <i>Before=</i> dependency on local-fs.target.</dl>
<h2>Fstab</h2>
<p>Automount units may either be configured via unit files, or via /etc/fstab (see <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) for details). </p>
<p> For details how systemd parses /etc/fstab see <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5). </p>
<p> If an automount point is configured in both /etc/fstab and a unit file, the configuration in the latter takes precedence.</p>
<h2>Options</h2>
<p>Automount files must include an [Automount] section, which carries information about the file system automount points it supervises. The options specific to the [Automount] section of automount units are the following: </p>
<p> <i>Where=</i></p>
<dl>
<dd>Takes an absolute path of a directory of the automount point. If the automount point does not exist at time that the automount point is installed, it is created. This string must be reflected in the unit filename. (See above.) This option is mandatory.</dl>
<p> <i>DirectoryMode=</i></p>
<dl>
<dd>Directories of automount points (and any parent directories) are automatically created if needed. This option specifies the file system access mode used when creating these directories. Takes an access mode in octal notation. Defaults to 0755.</dl>
<p> <i>TimeoutIdleSec=</i></p>
<dl>
<dd>Configures an idle timeout. Once the mount has been idle for the specified time, systemd will attempt to unmount. Takes a unit-less value in seconds, or a time span value such as &quot;5min 20s&quot;. Pass 0 to disable the timeout logic. The timeout is disabled by default.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
