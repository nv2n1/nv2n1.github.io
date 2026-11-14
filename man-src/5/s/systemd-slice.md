---
title: "systemd-slice(5)"
name: "systemd-slice"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-slice/"
description: "systemd.slice – Slice unit configuration"
---

<p>systemd.slice &#8211; Slice unit configuration</p>
<h2>Synopsis</h2>
<p><i>slice</i>.slice</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.slice&quot; encodes information about a slice unit. A slice unit is a concept for hierarchically managing resources of a group of processes. This management is performed by creating a node in the Linux Control Group (cgroup) tree. Units that manage processes (primarily scope and service units) may be assigned to a specific slice. For each slice, certain resource limits may be set that apply to all processes of all units contained in that slice. Slices are organized hierarchically in a tree. The name of the slice encodes the location in the tree. The name consists of a dash-separated series of names, which describes the path to the slice from the root slice. The root slice is named -.slice. Example: foo-bar.slice is a slice that is located within foo.slice, which in turn is located in the root slice -.slice. </p>
<p> Note that slice units cannot be templated, nor is possible to add multiple names to a slice unit by creating additional symlinks to its unit file. </p>
<p> By default, service and scope units are placed in system.slice, virtual machines and containers registered with <code><a href="/docs/linux/man/8-systemd-machined/">systemd-machined</a></code>(8) are found in machine.slice, and user sessions handled by <code><a href="/docs/linux/man/8-systemd-logind/">systemd-logind</a></code>(8) in user.slice. See <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for more information. </p>
<p> See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. The slice specific configuration options are configured in the [Slice] section. Currently, only generic resource control settings as described in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) are allowed. </p>
<p> See the m[blue]<code>New Control Group Interfaces</code>m[]<font SIZE="-2">[1]</font> for an introduction on how to make use of slice units from programs.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>The following dependencies are implicitly added: </p>
<dl>
<dd>&bull; Slice units automatically gain dependencies of type <i>After=</i> and <i>Requires=</i> on their immediate parent slice unit.</dl>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; Slice units will automatically have dependencies of type <i>Conflicts=</i> and <i>Before=</i> on shutdown.target. These ensure that slice units are removed prior to system shutdown. Only slice units involved with late system shutdown should disable <i>DefaultDependencies=</i> option.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>New Control Group Interfaces</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/ControlGroupInterface/">https://www.freedesktop.org/wiki/Software/systemd/ControlGroupInterface/</a></dl>
