---
title: "systemd-scope(5)"
name: "systemd-scope"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-scope/"
description: "systemd.scope – Scope unit configuration"
---

<p>systemd.scope &#8211; Scope unit configuration</p>
<h2>Synopsis</h2>
<p><i>scope</i>.scope</p>
<h2>Description</h2>
<p>Scope units are not configured via unit configuration files, but are only created programmatically using the bus interfaces of systemd. They are named similar to filenames. A unit whose name ends in &quot;.scope&quot; refers to a scope unit. Scopes units manage a set of system processes. Unlike service units, scope units manage externally created processes, and do not fork off processes on its own. </p>
<p> The main purpose of scope units is grouping worker processes of a system service for organization and for managing resources. </p>
<p> <code>systemd-run </code><code>&#8211;scope</code> may be used to easily launch a command in a new scope unit from the command line. </p>
<p> See the m[blue]<code>New Control Group Interfaces</code>m[]<font SIZE="-2">[1]</font> for an introduction on how to make use of scope units from programs. </p>
<p> Note that, unlike service units, scope units have no &quot;main&quot; process: all processes in the scope are equivalent. The lifecycle of the scope unit is thus not bound to the lifetime of one specific process, but to the existence of at least one process in the scope. This also means that the exit statuses of these processes are not relevant for the scope unit failure state. Scope units may still enter a failure state, for example due to resource exhaustion or stop timeouts being reached, but not due to programs inside of them terminating uncleanly. Since processes managed as scope units generally remain children of the original process that forked them off, it is also the job of that process to collect their exit statuses and act on them as needed.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>Implicit dependencies may be added as result of resource control parameters as documented in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5).</p>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; Scope units will automatically have dependencies of type <i>Conflicts=</i> and <i>Before=</i> on shutdown.target. These ensure that scope units are removed prior to system shutdown. Only scope units involved with early boot or late system shutdown should disable <i>DefaultDependencies=</i> option.</dl>
<h2>Options</h2>
<p>Scope files may include a [Scope] section, which carries information about the scope and the units it contains. A number of options that may be used in this section are shared with other unit types. These options are documented in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5). The options specific to the [Scope] section of scope units are the following: </p>
<p> <i>RuntimeMaxSec=</i></p>
<dl>
<dd>Configures a maximum time for the scope to run. If this is used and the scope has been active for longer than the specified time it is terminated and put into a failure state. Pass &quot;infinity&quot; (the default) to configure no runtime limit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemd-run/">systemd-run</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7).</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>New Control Group Interfaces</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/ControlGroupInterface/">https://www.freedesktop.org/wiki/Software/systemd/ControlGroupInterface/</a></dl>
