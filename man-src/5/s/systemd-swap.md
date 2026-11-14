---
title: "systemd-swap(5)"
name: "systemd-swap"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-swap/"
description: "systemd.swap – Swap unit configuration"
---

<p>systemd.swap &#8211; Swap unit configuration</p>
<h2>Synopsis</h2>
<p><i>swap</i>.swap</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.swap&quot; encodes information about a swap device or file for memory paging controlled and supervised by systemd. </p>
<p> This man page lists the configuration options specific to this unit type. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. The swap specific configuration options are configured in the [Swap] section. </p>
<p> Additional options are listed in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), which define the execution environment the <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8) program is executed in, in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5), which define the way these processes are terminated, and in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), which configure resource control settings for these processes of the unit. </p>
<p> Swap units must be named after the devices or files they control. Example: the swap device /dev/sda5 must be configured in a unit file dev-sda5.swap. For details about the escaping logic used to convert a file system path to a unit name, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). Note that swap units cannot be templated, nor is possible to add multiple names to a swap unit by creating additional symlinks to it. </p>
<p> Note that swap support on Linux is privileged, swap units are hence only available in the system service manager (and root&#8217;s user service manager), but not in unprivileged user&#8217;s service manager.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>The following dependencies are implicitly added: </p>
<dl>
<dd>&bull; All swap units automatically get the <i>BindsTo=</i> and <i>After=</i> dependencies on the device units or the mount units of the files they are activated from.</dl>
<p> Additional implicit dependencies may be added as result of execution and resource control parameters as documented in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5).</p>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; Swap units automatically acquire a <i>Conflicts=</i> and a <i>Before=</i> dependency on umount.target so that they are deactivated at shutdown as well as a <i>Before=swap.target</i> dependency.</dl>
<h2>Fstab</h2>
<p>Swap units may either be configured via unit files, or via /etc/fstab (see <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) for details). Swaps listed in /etc/fstab will be converted into native units dynamically at boot and when the configuration of the system manager is reloaded. See <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8) for details about the conversion. </p>
<p> If a swap device or file is configured in both /etc/fstab and a unit file, the configuration in the latter takes precedence. </p>
<p> When reading /etc/fstab, a few special options are understood by systemd which influence how dependencies are created for swap units. </p>
<p> <code>noauto</code>, <code>auto</code></p>
<dl>
<dd>With <code>noauto</code>, the swap unit will not be added as a dependency for swap.target. This means that it will not be activated automatically during boot, unless it is pulled in by some other unit. The <code>auto</code> option has the opposite meaning and is the default.</dl>
<p> <code>nofail</code></p>
<dl>
<dd>With <code>nofail</code>, the swap unit will be only wanted, not required by swap.target. This means that the boot will continue even if this swap device is not activated successfully.</dl>
<p> <code>x-systemd.device-timeout=</code></p>
<dl>
<dd>Configure how long systemd should wait for a device to show up before giving up on an entry from /etc/fstab. Specify a time in seconds or explicitly append a unit such as &quot;s&quot;, &quot;min&quot;, &quot;h&quot;, &quot;ms&quot;. </p>
<p> Note that this option can only be used in /etc/fstab, and will be ignored when part of the <i>Options=</i> setting in a unit file.</dl>
<p> <code>x-systemd.makefs</code></p>
<dl>
<dd>The swap structure will be initialized on the device. If the device is not &quot;empty&quot;, i.e. it contains any signature, the operation will be skipped. It is hence expected that this option remains set even after the device has been initialized. </p>
<p> Note that this option can only be used in /etc/fstab, and will be ignored when part of the <i>Options=</i> setting in a unit file. </p>
<p> See <code>systemd-mkswap [at] .service</code>(8) and the discussion of <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8) in <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5).</dl>
<h2>Options</h2>
<p>Swap unit files must include a [Swap] section, which carries information about the swap device it supervises. A number of options that may be used in this section are shared with other unit types. These options are documented in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5). The options specific to the [Swap] section of swap units are the following: </p>
<p> <i>What=</i></p>
<dl>
<dd>Takes an absolute path of a device node or file to use for paging. See <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8) for details. If this refers to a device node, a dependency on the respective device unit is automatically created. (See <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5) for more information.) If this refers to a file, a dependency on the respective mount unit is automatically created. (See <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5) for more information.) This option is mandatory. Note that the usual specifier expansion is applied to this setting, literal percent characters should hence be written as &quot;%%&quot;.</dl>
<p> <i>Priority=</i></p>
<dl>
<dd>Swap priority to use when activating the swap device or file. This takes an integer. This setting is optional and ignored when the priority is set by <code>pri=</code> in the <i>Options=</i> key.</dl>
<p> <i>Options=</i></p>
<dl>
<dd>May contain an option string for the swap device. This may be used for controlling discard options among other functionality, if the swap backing device supports the discard or trim operation. (See <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8) for more information.) Note that the usual specifier expansion is applied to this setting, literal percent characters should hence be written as &quot;%%&quot;.</dl>
<p> <i>TimeoutSec=</i></p>
<dl>
<dd>Configures the time to wait for the swapon command to finish. If a command does not exit within the configured time, the swap will be considered failed and be shut down again. All commands still running will be terminated forcibly via <code>SIGTERM</code>, and after another delay of this time with <code>SIGKILL</code>. (See <code>KillMode=</code> in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5).) Takes a unit-less value in seconds, or a time span value such as &quot;5min 20s&quot;. Pass &quot;0&quot; to disable the timeout logic. Defaults to <i>DefaultTimeoutStartSec=</i> from the manager configuration file (see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5)).</dl>
<p> Check <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) for more settings.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
