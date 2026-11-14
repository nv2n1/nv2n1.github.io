---
title: "systemd-target(5)"
name: "systemd-target"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-target/"
description: "systemd.target – Target unit configuration"
---

<p>systemd.target &#8211; Target unit configuration</p>
<h2>Synopsis</h2>
<p><i>target</i>.target</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.target&quot; encodes information about a target unit of systemd, which is used for grouping units and as well-known synchronization points during start-up. </p>
<p> This unit type has no specific options. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. A separate [Target] section does not exist, since no target-specific options may be configured. </p>
<p> Target units do not offer any additional functionality on top of the generic functionality provided by units. They exist merely to group units via dependencies (useful as boot targets), and to establish standardized names for synchronization points used in dependencies between units. Among other things, target units are a more flexible replacement for SysV runlevels in the classic SysV init system. (And for compatibility reasons special target units such as runlevel3.target exist which are used by the SysV runlevel compatibility code in systemd. See <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for details).</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>There are no implicit dependencies for target units.</p>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; Target units will automatically complement all configured dependencies of type <i>Wants=</i> or <i>Requires=</i> with dependencies of type <i>After=</i> unless <i>DefaultDependencies=no</i> is set in the specified units. Note that <i>Wants=</i> or <i>Requires=</i> must be defined in the target unit itself &#8212; if you for example define <i>Wants=</i>some.target in some.service, the automatic ordering will not be added.</dl>
<dl>
<dd>&bull; Target units automatically gain <i>Conflicts=</i> and <i>Before=</i> dependencies against shutdown.target.</dl>
<h2>Example</h2>
<p><code>Example 1. Simple standalone target</code> </p>
<dl>
<dd>
<pre># emergency-net.target
[Unit]
Description=Emergency Mode with Networking
Requires=emergency.target systemd-networkd.service
After=emergency.target systemd-networkd.service
AllowIsolate=yes</pre>
</dl>
<p> When adding dependencies to other units, it&#8217;s important to check if they set <i>DefaultDependencies=</i>. Service units, unless they set <i>DefaultDependencies=no</i>, automatically get a dependency on sysinit.target. In this case, both emergency.target and systemd-networkd.service have <i>DefaultDependencies=no</i>, so they are suitable for use in this target, and do not pull in sysinit.target. </p>
<p> You can now switch into this emergency mode by running <i>systemctl isolate emergency-net.target</i> or by passing the option <i>systemd.unit=emergency-net.target</i> on the kernel command line. </p>
<p> Other units can have <i>WantedBy=emergency-net.target</i> in the <i>[Install]</i> section. After they are enabled using <code>systemctl enable</code>, they will be started before <i>emergency-net.target</i> is started. It is also possible to add arbitrary units as dependencies of emergency.target without modifying them by using <code>systemctl add-wants</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
