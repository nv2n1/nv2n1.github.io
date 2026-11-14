---
title: "systemd-mount(5)"
name: "systemd-mount"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-mount/"
description: "systemd.mount – Mount unit configuration"
---

<p>systemd.mount &#8211; Mount unit configuration</p>
<h2>Synopsis</h2>
<p><i>mount</i>.mount</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.mount&quot; encodes information about a file system mount point controlled and supervised by systemd. </p>
<p> This man page lists the configuration options specific to this unit type. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. The mount specific configuration options are configured in the [Mount] section. </p>
<p> Additional options are listed in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), which define the execution environment the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) program is executed in, and in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5), which define the way the processes are terminated, and in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), which configure resource control settings for the processes of the service. </p>
<p> Note that the options <i>User=</i> and <i>Group=</i> are not useful for mount units. systemd passes two parameters to <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8); the values of <i>What=</i> and <i>Where=</i>. When invoked in this way, <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) does not read any options from /etc/fstab, and must be run as UID 0. </p>
<p> Mount units must be named after the mount point directories they control. Example: the mount point /home/lennart must be configured in a unit file home-lennart.mount. For details about the escaping logic used to convert a file system path to a unit name, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). Note that mount units cannot be templated, nor is possible to add multiple names to a mount unit by creating additional symlinks to it. </p>
<p> Optionally, a mount unit may be accompanied by an automount unit, to allow on-demand or parallelized mounting. See <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5). </p>
<p> Mount points created at runtime (independently of unit files or /etc/fstab) will be monitored by systemd and appear like any other mount unit in systemd. See /proc/self/mountinfo description in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5). </p>
<p> Some file systems have special semantics as API file systems for kernel-to-userspace and userspace-to-userspace interfaces. Some of them may not be changed via mount units, and cannot be disabled. For a longer discussion see m[blue]<code>API File Systems</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> The <code><a href="/docs/linux/man/1-systemd-mount/">systemd-mount</a></code>(1) command allows creating .mount and .automount units dynamically and transiently from the command line.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>The following dependencies are implicitly added: </p>
<dl>
<dd>&bull; If a mount unit is beneath another mount unit in the file system hierarchy, both a requirement dependency and an ordering dependency between both units are created automatically.</dl>
<dl>
<dd>&bull; Block device backed file systems automatically gain <i>BindsTo=</i> and <i>After=</i> type dependencies on the device unit encapsulating the block device (see below).</dl>
<dl>
<dd>&bull; If traditional file system quota is enabled for a mount unit, automatic <i>Wants=</i> and <i>Before=</i> dependencies on systemd-quotacheck.service and quotaon.service are added.</dl>
<dl>
<dd>&bull; Additional implicit dependencies may be added as result of execution and resource control parameters as documented in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5).</dl>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; All mount units acquire automatic <i>Before=</i> and <i>Conflicts=</i> on umount.target in order to be stopped during shutdown.</dl>
<dl>
<dd>&bull; Mount units referring to local file systems automatically gain an <i>After=</i> dependency on local-fs-pre.target, and a <i>Before=</i> dependency on local-fs.target unless <code>nofail</code> mount option is set.</dl>
<dl>
<dd>&bull; Network mount units automatically acquire <i>After=</i> dependencies on remote-fs-pre.target, network.target and network-online.target, and gain a <i>Before=</i> dependency on remote-fs.target unless <code>nofail</code> mount option is set. Towards the latter a <i>Wants=</i> unit is added as well.</dl>
<p> Mount units referring to local and network file systems are distinguished by their file system type specification. In some cases this is not sufficient (for example network block device based mounts, such as iSCSI), in which case <code>_netdev</code> may be added to the mount option string of the unit, which forces systemd to consider the mount unit a network mount.</p>
<h2>Fstab</h2>
<p>Mount units may either be configured via unit files, or via /etc/fstab (see <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) for details). Mounts listed in /etc/fstab will be converted into native units dynamically at boot and when the configuration of the system manager is reloaded. In general, configuring mount points through /etc/fstab is the preferred approach. See <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8) for details about the conversion. </p>
<p> The NFS mount option <code>bg</code> for NFS background mounts as documented in <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5) is detected by <code>systemd-fstab-generator</code> and the options are transformed so that systemd fulfills the job-control implications of that option. Specifically <code>systemd-fstab-generator</code> acts as though &quot;x-systemd.mount-timeout=infinity,retry=10000&quot; was prepended to the option list, and &quot;fg,nofail&quot; was appended. Depending on specific requirements, it may be appropriate to provide some of these options explicitly, or to make use of the &quot;x-systemd.automount&quot; option described below instead of using &quot;bg&quot;. </p>
<p> When reading /etc/fstab a few special mount options are understood by systemd which influence how dependencies are created for mount points. systemd will create a dependency of type <i>Wants=</i> or <code>Requires=</code> (see option <code>nofail</code> below), from either local-fs.target or remote-fs.target, depending whether the file system is local or remote. </p>
<p> <code>x-systemd.requires=</code></p>
<dl>
<dd>Configures a <i>Requires=</i> and an <i>After=</i> dependency between the created mount unit and another systemd unit, such as a device or mount unit. The argument should be a unit name, or an absolute path to a device node or mount point. This option may be specified more than once. This option is particularly useful for mount point declarations that need an additional device to be around (such as an external journal device for journal file systems) or an additional mount to be in place (such as an overlay file system that merges multiple mount points). See <i>After=</i> and <i>Requires=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. </p>
<p> Note that this option always applies to the created mount unit only regardless whether <code>x-systemd.automount</code> has been specified.</dl>
<p> <code>x-systemd.before=</code>, <code>x-systemd.after=</code></p>
<dl>
<dd>In the created mount unit, configures a <i>Before=</i> or <i>After=</i> dependency on another systemd unit, such as a mount unit. The argument should be a unit name or an absolute path to a mount point. This option may be specified more than once. This option is particularly useful for mount point declarations with <code>nofail</code> option that are mounted asynchronously but need to be mounted before or after some unit start, for example, before local-fs.target unit. See <i>Before=</i> and <i>After=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. </p>
<p> Note that these options always apply to the created mount unit only regardless whether <code>x-systemd.automount</code> has been specified.</dl>
<p> <code>x-systemd.wanted-by=</code>, <code>x-systemd.required-by=</code></p>
<dl>
<dd>In the created mount unit, configures a <i>WantedBy=</i> or <i>RequiredBy=</i> dependency on another unit. This option may be specified more than once. If this is specified, the normal automatic dependencies on the created mount unit, e.g., local-fs.target, are not automatically created. See <i>WantedBy=</i> and <i>RequiredBy=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details.</dl>
<p> <code>x-systemd.requires-mounts-for=</code></p>
<dl>
<dd>Configures a <i>RequiresMountsFor=</i> dependency between the created mount unit and other mount units. The argument must be an absolute path. This option may be specified more than once. See <i>RequiresMountsFor=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details.</dl>
<p> <code>x-systemd.device-bound</code></p>
<dl>
<dd>The block device backed file system will be upgraded to <i>BindsTo=</i> dependency. This option is only useful when mounting file systems manually with <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) as the default dependency in this case is <i>Requires=</i>. This option is already implied by entries in /etc/fstab or by mount units.</dl>
<p> <code>x-systemd.automount</code></p>
<dl>
<dd>An automount unit will be created for the file system. See <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5) for details.</dl>
<p> <code>x-systemd.idle-timeout=</code></p>
<dl>
<dd>Configures the idle timeout of the automount unit. See <i>TimeoutIdleSec=</i> in <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5) for details.</dl>
<p> <code>x-systemd.device-timeout=</code></p>
<dl>
<dd>Configure how long systemd should wait for a device to show up before giving up on an entry from /etc/fstab. Specify a time in seconds or explicitly append a unit such as &quot;s&quot;, &quot;min&quot;, &quot;h&quot;, &quot;ms&quot;. </p>
<p> Note that this option can only be used in /etc/fstab, and will be ignored when part of the <i>Options=</i> setting in a unit file.</dl>
<p> <code>x-systemd.mount-timeout=</code></p>
<dl>
<dd>Configure how long systemd should wait for the mount command to finish before giving up on an entry from /etc/fstab. Specify a time in seconds or explicitly append a unit such as &quot;s&quot;, &quot;min&quot;, &quot;h&quot;, &quot;ms&quot;. </p>
<p> Note that this option can only be used in /etc/fstab, and will be ignored when part of the <i>Options=</i> setting in a unit file. </p>
<p> See <i>TimeoutSec=</i> below for details.</dl>
<p> <code>x-systemd.makefs</code></p>
<dl>
<dd>The file system will be initialized on the device. If the device is not &quot;empty&quot;, i.e. it contains any signature, the operation will be skipped. It is hence expected that this option remains set even after the device has been initialized. </p>
<p> Note that this option can only be used in /etc/fstab, and will be ignored when part of the <i>Options=</i> setting in a unit file. </p>
<p> See <code>systemd-makefs [at] .service</code>(8). </p>
<p> <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8) may be used to remove any signatures from a block device to force <code>x-systemd.makefs</code> to reinitialize the device.</dl>
<p> <code>x-systemd.growfs</code></p>
<dl>
<dd>The file system will be grown to occupy the full block device. If the file system is already at maximum size, no action will be performed. It is hence expected that this option remains set even after the file system has been grown. Only certain file system types are supported, see <code>systemd-makefs [at] .service</code>(8) for details. </p>
<p> Note that this option can only be used in /etc/fstab, and will be ignored when part of the <i>Options=</i> setting in a unit file.</dl>
<p> <code>x-systemd.rw-only</code></p>
<dl>
<dd>If a mount operation fails to mount the file system read-write, it normally tries mounting the file system read-only instead. This option disables that behaviour, and causes the mount to fail immediately instead. This option is translated into the <i>ReadWriteOnly=</i> setting in a unit file.</dl>
<p> <code>_netdev</code></p>
<dl>
<dd>Normally the file system type is used to determine if a mount is a &quot;network mount&quot;, i.e. if it should only be started after the network is available. Using this option overrides this detection and specifies that the mount requires network. </p>
<p> Network mount units are ordered between remote-fs-pre.target and remote-fs.target, instead of local-fs-pre.target and local-fs.target. They also pull in network-online.target and are ordered after it and network.target.</dl>
<p> <code>noauto</code>, <code>auto</code></p>
<dl>
<dd>With <code>noauto</code>, the mount unit will not be added as a dependency for local-fs.target or remote-fs.target. This means that it will not be mounted automatically during boot, unless it is pulled in by some other unit. The <code>auto</code> option has the opposite meaning and is the default. </p>
<p> Note that if <code>x-systemd.automount</code> (see above) is used, neither <code>auto</code> nor <code>noauto</code> have any effect. The matching automount unit will be added as a dependency to the appropriate target.</dl>
<p> <code>nofail</code></p>
<dl>
<dd>With <code>nofail</code>, this mount will be only wanted, not required, by local-fs.target or remote-fs.target. Moreover the mount unit is not ordered before these target units. This means that the boot will continue without waiting for the mount unit and regardless whether the mount point can be mounted successfully.</dl>
<p> <code>x-initrd.mount</code></p>
<dl>
<dd>An additional filesystem to be mounted in the initramfs. See initrd-fs.target description in <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7).</dl>
<p> If a mount point is configured in both /etc/fstab and a unit file that is stored below /usr/, the former will take precedence. If the unit file is stored below /etc/, it will take precedence. This means: native unit files take precedence over traditional configuration files, but this is superseded by the rule that configuration in /etc/ will always take precedence over configuration in /usr/.</p>
<h2>Options</h2>
<p>Mount files must include a [Mount] section, which carries information about the file system mount points it supervises. A number of options that may be used in this section are shared with other unit types. These options are documented in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5). The options specific to the [Mount] section of mount units are the following: </p>
<p> <i>What=</i></p>
<dl>
<dd>Takes an absolute path of a device node, file or other resource to mount. See <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) for details. If this refers to a device node, a dependency on the respective device unit is automatically created. (See <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5) for more information.) This option is mandatory. Note that the usual specifier expansion is applied to this setting, literal percent characters should hence be written as &quot;%%&quot;. If this mount is a bind mount and the specified path does not exist yet it is created as directory.</dl>
<p> <i>Where=</i></p>
<dl>
<dd>Takes an absolute path of a file or directory for the mount point; in particular, the destination cannot be a symbolic link. If the mount point does not exist at the time of mounting, it is created as directory. This string must be reflected in the unit filename. (See above.) This option is mandatory.</dl>
<p> <i>Type=</i></p>
<dl>
<dd>Takes a string for the file system type. See <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) for details. This setting is optional.</dl>
<p> <i>Options=</i></p>
<dl>
<dd>Mount options to use when mounting. This takes a comma-separated list of options. This setting is optional. Note that the usual specifier expansion is applied to this setting, literal percent characters should hence be written as &quot;%%&quot;.</dl>
<p> <i>SloppyOptions=</i></p>
<dl>
<dd>Takes a boolean argument. If true, parsing of the options specified in <i>Options=</i> is relaxed, and unknown mount options are tolerated. This corresponds with <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)&#8217;s <i>-s</i> switch. Defaults to off.</dl>
<p> <i>LazyUnmount=</i></p>
<dl>
<dd>Takes a boolean argument. If true, detach the filesystem from the filesystem hierarchy at time of the unmount operation, and clean up all references to the filesystem as soon as they are not busy anymore. This corresponds with <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8)&#8217;s <i>-l</i> switch. Defaults to off.</dl>
<p> <i>ReadWriteOnly=</i></p>
<dl>
<dd>Takes a boolean argument. If false, a mount point that shall be mounted read-write but cannot be mounted so is retried to be mounted read-only. If true the operation will fail immediately after the read-write mount attempt did not succeed. This corresponds with <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)&#8217;s <i>-w</i> switch. Defaults to off.</dl>
<p> <i>ForceUnmount=</i></p>
<dl>
<dd>Takes a boolean argument. If true, force an unmount (in case of an unreachable NFS system). This corresponds with <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8)&#8217;s <i>-f</i> switch. Defaults to off.</dl>
<p> <i>DirectoryMode=</i></p>
<dl>
<dd>Directories of mount points (and any parent directories) are automatically created if needed. This option specifies the file system access mode used when creating these directories. Takes an access mode in octal notation. Defaults to 0755.</dl>
<p> <i>TimeoutSec=</i></p>
<dl>
<dd>Configures the time to wait for the mount command to finish. If a command does not exit within the configured time, the mount will be considered failed and be shut down again. All commands still running will be terminated forcibly via <code>SIGTERM</code>, and after another delay of this time with <code>SIGKILL</code>. (See <code>KillMode=</code> in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5).) Takes a unit-less value in seconds, or a time span value such as &quot;5min 20s&quot;. Pass 0 to disable the timeout logic. The default value is set from <i>DefaultTimeoutStartSec=</i> option in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> Check <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) for more settings.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/1-systemd-mount/">systemd-mount</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>API File Systems</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems">https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems</a></dl>
