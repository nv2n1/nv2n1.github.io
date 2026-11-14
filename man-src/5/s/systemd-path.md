---
title: "systemd-path(5)"
name: "systemd-path"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-path/"
description: "systemd.path – Path unit configuration"
---

<p>systemd.path &#8211; Path unit configuration</p>
<h2>Synopsis</h2>
<p><i>path</i>.path</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.path&quot; encodes information about a path monitored by systemd, for path-based activation. </p>
<p> This man page lists the configuration options specific to this unit type. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. The path specific configuration options are configured in the [Path] section. </p>
<p> For each path file, a matching unit file must exist, describing the unit to activate when the path changes. By default, a service by the same name as the path (except for the suffix) is activated. Example: a path file foo.path activates a matching service foo.service. The unit to activate may be controlled by <i>Unit=</i> (see below). </p>
<p> Internally, path units use the <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) API to monitor file systems. Due to that, it suffers by the same limitations as inotify, and for example cannot be used to monitor files or directories changed by other machines on remote NFS file systems. </p>
<p> When a service unit triggered by a path unit terminates (regardless whether it exited successfully or failed), monitored paths are checked immediately again, and the service accordingly restarted instantly. As protection against busy looping in this trigger/start cycle, a start rate limit is enforced on the service unit, see <i>StartLimitIntervalSec=</i> and <i>StartLimitBurst=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). Unlike other service failures, the error condition that the start rate limit is hit is propagated from the service unit to the path unit and causes the path unit to fail as well, thus ending the loop.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>The following dependencies are implicitly added: </p>
<dl>
<dd>&bull; If a path unit is beneath another mount unit in the file system hierarchy, both a requirement and an ordering dependency between both units are created automatically.</dl>
<dl>
<dd>&bull; An implicit <i>Before=</i> dependency is added between a path unit and the unit it is supposed to activate.</dl>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; Path units will automatically have dependencies of type <i>Before=</i> on paths.target, dependencies of type <i>After=</i> and <i>Requires=</i> on sysinit.target, and have dependencies of type <i>Conflicts=</i> and <i>Before=</i> on shutdown.target. These ensure that path units are terminated cleanly prior to system shutdown. Only path units involved with early boot or late system shutdown should disable <i>DefaultDependencies=</i> option.</dl>
<h2>Options</h2>
<p>Path files must include a [Path] section, which carries information about the path(s) it monitors. The options specific to the [Path] section of path units are the following: </p>
<p> <i>PathExists=</i>, <i>PathExistsGlob=</i>, <i>PathChanged=</i>, <i>PathModified=</i>, <i>DirectoryNotEmpty=</i></p>
<dl>
<dd>Defines paths to monitor for certain changes: <i>PathExists=</i> may be used to watch the mere existence of a file or directory. If the file specified exists, the configured unit is activated. <i>PathExistsGlob=</i> works similar, but checks for the existence of at least one file matching the globbing pattern specified. <i>PathChanged=</i> may be used to watch a file or directory and activate the configured unit whenever it changes. It is not activated on every write to the watched file but it is activated if the file which was open for writing gets closed. <i>PathModified=</i> is similar, but additionally it is activated also on simple writes to the watched file. <i>DirectoryNotEmpty=</i> may be used to watch a directory and activate the configured unit whenever it contains at least one file. </p>
<p> The arguments of these directives must be absolute file system paths. </p>
<p> Multiple directives may be combined, of the same and of different types, to watch multiple paths. If the empty string is assigned to any of these options, the list of paths to watch is reset, and any prior assignments of these options will not have any effect. </p>
<p> If a path already exists (in case of <i>PathExists=</i> and <i>PathExistsGlob=</i>) or a directory already is not empty (in case of <i>DirectoryNotEmpty=</i>) at the time the path unit is activated, then the configured unit is immediately activated as well. Something similar does not apply to <i>PathChanged=</i> and <i>PathModified=</i>. </p>
<p> If the path itself or any of the containing directories are not accessible, <code>systemd</code> will watch for permission changes and notice that conditions are satisfied when permissions allow that.</dl>
<p> <i>Unit=</i></p>
<dl>
<dd>The unit to activate when any of the configured paths changes. The argument is a unit name, whose suffix is not &quot;.path&quot;. If not specified, this value defaults to a service that has the same name as the path unit, except for the suffix. (See above.) It is recommended that the unit name that is activated and the unit name of the path unit are named identical, except for the suffix.</dl>
<p> <i>MakeDirectory=</i></p>
<dl>
<dd>Takes a boolean argument. If true, the directories to watch are created before watching. This option is ignored for <i>PathExists=</i> settings. Defaults to <code>false</code>.</dl>
<p> <i>DirectoryMode=</i></p>
<dl>
<dd>If <i>MakeDirectory=</i> is enabled, use the mode specified here to create the directories in question. Takes an access mode in octal notation. Defaults to <code>0755</code>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
