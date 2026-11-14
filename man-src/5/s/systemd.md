---
title: "systemd(5)"
name: "systemd"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd/"
description: "systemd.unit – Unit configuration"
---

<p>systemd.unit &#8211; Unit configuration</p>
<h2>Synopsis</h2>
<p><i>service</i>.service, <i>socket</i>.socket, <i>device</i>.device, <i>mount</i>.mount, <i>automount</i>.automount, <i>swap</i>.swap, <i>target</i>.target, <i>path</i>.path, <i>timer</i>.timer, <i>snapshot</i>.snapshot, <i>slice</i>.slice, <i>scope</i>.scope </p>
<pre>/etc/systemd/system/*
/run/systemd/system/*
/usr/lib/systemd/system/*
...</pre>
<pre>$XDG_CONFIG_HOME/systemd/user/*
$HOME/.config/systemd/user/*
/etc/systemd/user/*
$XDG_RUNTIME_DIR/systemd/user/*
/run/systemd/user/*
$XDG_DATA_HOME/systemd/user/*
$HOME/.local/share/systemd/user/*
/usr/lib/systemd/user/*
...</pre>
<h2>Description</h2>
<p>A unit configuration file encodes information about a service, a socket, a device, a mount point, an automount point, a swap file or partition, a start-up target, a watched file system path, a timer controlled and supervised by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), a temporary system state snapshot, a resource management slice or a group of externally created processes. The syntax is inspired by m[blue]<code>XDG Desktop Entry Specification</code>m[]<font SIZE="-2">[1]</font>.desktop files, which are in turn inspired by Microsoft Windows .ini files. </p>
<p> This man page lists the common configuration options of all the unit types. These options need to be configured in the [Unit] or [Install] sections of the unit files. </p>
<p> In addition to the generic [Unit] and [Install] sections described here, each unit may have a type-specific section, e.g. [Service] for a service unit. See the respective man pages for more information: <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5), <code><a href="/docs/linux/man/5-systemd-path/">systemd.path</a></code>(5), <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5), <code><a href="/docs/linux/man/5-systemd-snapshot/">systemd.snapshot</a></code>(5). <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5). <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5). </p>
<p> Various settings are allowed to be specified more than once, in which case the interpretation depends on the setting. Often, multiple settings form a list, and setting to an empty value &quot;resets&quot;, which means that previous assignments are ignored. When this is allowed, it is mentioned in the description of the setting. Note that using multiple assignments to the same value makes the unit file incompatible with parsers for the XDG .desktop file format. </p>
<p> Unit files are loaded from a set of paths determined during compilation, described in the next section. </p>
<p> Unit files may contain additional options on top of those listed here. If systemd encounters an unknown option, it will write a warning log message but continue loading the unit. If an option or section name is prefixed with <code>X-</code>, it is ignored completely by systemd. Options within an ignored section do not need the prefix. Applications may use this to include additional information in the unit files. </p>
<p> Boolean arguments used in unit files can be written in various formats. For positive settings the strings <code>1</code>, <code>yes</code>, <code>true</code> and <code>on</code> are equivalent. For negative settings, the strings <code>0</code>, <code>no</code>, <code>false</code> and <code>off</code> are equivalent. </p>
<p> Time span values encoded in unit files can be written in various formats. A stand-alone number specifies a time in seconds. If suffixed with a time unit, the unit is honored. A concatenation of multiple values with units is supported, in which case the values are added up. Example: &quot;50&quot; refers to 50 seconds; &quot;2min 200ms&quot; refers to 2 minutes plus 200 milliseconds, i.e. 120200ms. The following time units are understood: s, min, h, d, w, ms, us. For details see <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7). </p>
<p> Empty lines and lines starting with # or ; are ignored. This may be used for commenting. Lines ending in a backslash are concatenated with the following line while reading and the backslash is replaced by a space character. This may be used to wrap long lines. </p>
<p> Along with a unit file foo.service, the directory foo.service.wants/ may exist. All unit files symlinked from such a directory are implicitly added as dependencies of type <i>Wants=</i> to the unit. This is useful to hook units into the start-up of other units, without having to modify their unit files. For details about the semantics of <i>Wants=</i>, see below. The preferred way to create symlinks in the .wants/ directory of a unit file is with the <code>enable</code> command of the <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) tool which reads information from the [Install] section of unit files (see below). A similar functionality exists for <i>Requires=</i> type dependencies as well, the directory suffix is .requires/ in this case. </p>
<p> Along with a unit file foo.service, a directory foo.service.d/ may exist. All files with the suffix &quot;.conf&quot; from this directory will be parsed after the file itself is parsed. This is useful to alter or add configuration settings to a unit, without having to modify their unit files. Make sure that the file that is included has the appropriate section headers before any directive. Note that for instanced units this logic will first look for the instance &quot;.d/&quot; subdirectory and read its &quot;.conf&quot; files, followed by the template &quot;.d/&quot; subdirectory and reads its &quot;.conf&quot; files. </p>
<p> Note that while systemd offers a flexible dependency system between units it is recommended to use this functionality only sparingly and instead rely on techniques such as bus-based or socket-based activation which make dependencies implicit, resulting in a both simpler and more flexible system. </p>
<p> Some unit names reflect paths existing in the file system namespace. Example: a device unit dev-sda.device refers to a device with the device node /dev/sda in the file system namespace. If this applies, a special way to escape the path name is used, so that the result is usable as part of a filename. Basically, given a path, &quot;/&quot; is replaced by &quot;-&quot;, and all unprintable characters and the &quot;-&quot; are replaced by C-style &quot;-&quot; escapes. The root directory &quot;/&quot; is encoded as single dash, while otherwise the initial and ending &quot;/&quot; is removed from all paths during transformation. This escaping is reversible. </p>
<p> Optionally, units may be instantiated from a template file at runtime. This allows creation of multiple units from a single configuration file. If systemd looks for a unit configuration file, it will first search for the literal unit name in the file system. If that yields no success and the unit name contains an &quot;@&quot; character, systemd will look for a unit template that shares the same name but with the instance string (i.e. the part between the &quot;@&quot; character and the suffix) removed. Example: if a service getty [at] tty3.service is requested and no file by that name is found, systemd will look for getty [at] .service and instantiate a service from that configuration file if it is found. </p>
<p> To refer to the instance string from within the configuration file you may use the special &quot;%i&quot; specifier in many of the configuration options. See below for details. </p>
<p> If a unit file is empty (i.e. has the file size 0) or is symlinked to /dev/null, its configuration will not be loaded and it appears with a load state of &quot;masked&quot;, and cannot be activated. Use this as an effective way to fully disable a unit, making it impossible to start it even manually. </p>
<p> The unit file format is covered by the m[blue]<code>Interface Stability Promise</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>Unit Load Path</h2>
<p>Unit files are loaded from a set of paths determined during compilation, described in the two tables below. Unit files found in directories listed earlier override files with the same name in directories lower in the list. </p>
<p> When systemd is running in user mode (<code>&#8211;user</code>) and the variable <i>$SYSTEMD_UNIT_PATH</i> is set, this contents of this variable overrides the unit load path. If <i>$SYSTEMD_UNIT_PATH</i> ends with an empty component (&quot;:&quot;), the usual unit load path will be appended to the contents of the variable. </p>
<p> <code>Table 1.&nbsp;<wbr> Load path when running in system mode (&#8211;system).</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Path </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> /etc/systemd/system </td>
<td> Local configuration
</td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/system </td>
<td> Runtime units
</td>
</tr>
<tr VALIGN=top>
<td> /usr/lib/systemd/system </td>
<td> Units of installed packages
</td>
</tr>
</table>
<p> <code>Table 2.&nbsp;<wbr> Load path when running in user mode (&#8211;user).</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Path </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_CONFIG_HOME/systemd/user </td>
<td> User configuration (only used when $XDG_CONFIG_HOME is set)
</td>
</tr>
<tr VALIGN=top>
<td> $HOME/.config/systemd/user </td>
<td> User configuration (only used when $XDG_CONFIG_HOME is not set)
</td>
</tr>
<tr VALIGN=top>
<td> /etc/systemd/user </td>
<td> Local configuration
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_RUNTIME_DIR/systemd/user </td>
<td> Runtime units (only used when $XDG_RUNTIME_DIR is set)
</td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/user </td>
<td> Runtime units
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_DATA_HOME/systemd/user </td>
<td> Units of packages that have been installed in the home directory (only used when $XDG_DATA_HOME is set)
</td>
</tr>
<tr VALIGN=top>
<td> $HOME/.local/share/systemd/user </td>
<td> Units of packages that have been installed in the home directory (only used when $XDG_DATA_HOME is not set)
</td>
</tr>
<tr VALIGN=top>
<td> /usr/lib/systemd/user </td>
<td> Units of packages that have been installed system-wide
</td>
</tr>
</table>
<p> Additional units might be loaded into systemd (&quot;linked&quot;) from directories not on the unit load path. See the <code>link</code> command for <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1). Also, some units are dynamically created via generators m[blue]<code>Generators</code>m[]<font SIZE="-2">[3]</font>.</p>
<h2>[Unit] Section Options</h2>
<p>Unit file may include a [Unit] section, which carries generic information about the unit that is not dependent on the type of unit: </p>
<p> <i>Description=</i></p>
<dl>
<dd>A free-form string describing the unit. This is intended for use in UIs to show descriptive information along with the unit name. The description should contain a name that means something to the end user. &quot;Apache2 Web Server&quot; is a good example. Bad examples are &quot;high-performance light-weight HTTP server&quot; (too generic) or &quot;Apache2&quot; (too specific and meaningless for people who do not know Apache).</dl>
<p> <i>Documentation=</i></p>
<dl>
<dd>A space-separated list of URIs referencing documentation for this unit or its configuration. Accepted are only URIs of the types &quot;http://&quot;, &quot;https://&quot;, &quot;file:&quot;, &quot;info:&quot;, &quot;man:&quot;. For more information about the syntax of these URIs, see <code><a href="/docs/linux/man/7-uri/">uri</a></code>(7). The URIs should be listed in order of relevance, starting with the most relevant. It is a good idea to first reference documentation that explains what the unit&#8217;s purpose is, followed by how it is configured, followed by any other related documentation. This option may be specified more than once, in which case the specified list of URIs is merged. If the empty string is assigned to this option, the list is reset and all prior assignments will have no effect.</dl>
<p> <i>Requires=</i></p>
<dl>
<dd>Configures requirement dependencies on other units. If this unit gets activated, the units listed here will be activated as well. If one of the other units gets deactivated or its activation fails, this unit will be deactivated. This option may be specified more than once or multiple space-separated units may be specified in one option in which case requirement dependencies for all listed names will be created. Note that requirement dependencies do not influence the order in which services are started or stopped. This has to be configured independently with the <i>After=</i> or <i>Before=</i> options. If a unit foo.service requires a unit bar.service as configured with <i>Requires=</i> and no ordering is configured with <i>After=</i> or <i>Before=</i>, then both units will be started simultaneously and without any delay between them if foo.service is activated. Often it is a better choice to use <i>Wants=</i> instead of <i>Requires=</i> in order to achieve a system that is more robust when dealing with failing services. </p>
<p> Note that dependencies of this type may also be configured outside of the unit configuration file by adding a symlink to a .requires/ directory accompanying the unit file. For details see above.</dl>
<p> <i>RequiresOverridable=</i></p>
<dl>
<dd>Similar to <i>Requires=</i>. Dependencies listed in <i>RequiresOverridable=</i> which cannot be fulfilled or fail to start are ignored if the startup was explicitly requested by the user. If the start-up was pulled in indirectly by some dependency or automatic start-up of units that is not requested by the user, this dependency must be fulfilled and otherwise the transaction fails. Hence, this option may be used to configure dependencies that are normally honored unless the user explicitly starts up the unit, in which case whether they failed or not is irrelevant.</dl>
<p> <i>Requisite=</i>, <i>RequisiteOverridable=</i></p>
<dl>
<dd>Similar to <i>Requires=</i> and <i>RequiresOverridable=</i>, respectively. However, if the units listed here are not started already, they will not be started and the transaction will fail immediately.</dl>
<p> <i>Wants=</i></p>
<dl>
<dd>A weaker version of <i>Requires=</i>. Units listed in this option will be started if the configuring unit is. However, if the listed units fail to start or cannot be added to the transaction, this has no impact on the validity of the transaction as a whole. This is the recommended way to hook start-up of one unit to the start-up of another unit. </p>
<p> Note that dependencies of this type may also be configured outside of the unit configuration file by adding symlinks to a .wants/ directory accompanying the unit file. For details, see above.</dl>
<p> <i>BindsTo=</i></p>
<dl>
<dd>Configures requirement dependencies, very similar in style to <i>Requires=</i>, however in addition to this behavior, it also declares that this unit is stopped when any of the units listed suddenly disappears. Units can suddenly, unexpectedly disappear if a service terminates on its own choice, a device is unplugged or a mount point unmounted without involvement of systemd.</dl>
<p> <i>PartOf=</i></p>
<dl>
<dd>Configures dependencies similar to <i>Requires=</i>, but limited to stopping and restarting of units. When systemd stops or restarts the units listed here, the action is propagated to this unit. Note that this is a one-way dependency &#8212; changes to this unit do not affect the listed units.</dl>
<p> <i>Conflicts=</i></p>
<dl>
<dd>A space-separated list of unit names. Configures negative requirement dependencies. If a unit has a <i>Conflicts=</i> setting on another unit, starting the former will stop the latter and vice versa. Note that this setting is independent of and orthogonal to the <i>After=</i> and <i>Before=</i> ordering dependencies. </p>
<p> If a unit A that conflicts with a unit B is scheduled to be started at the same time as B, the transaction will either fail (in case both are required part of the transaction) or be modified to be fixed (in case one or both jobs are not a required part of the transaction). In the latter case, the job that is not the required will be removed, or in case both are not required, the unit that conflicts will be started and the unit that is conflicted is stopped.</dl>
<p> <i>Before=</i>, <i>After=</i></p>
<dl>
<dd>A space-separated list of unit names. Configures ordering dependencies between units. If a unit foo.service contains a setting <code>Before=bar.service</code> and both units are being started, bar.service&#8217;s start-up is delayed until foo.service is started up. Note that this setting is independent of and orthogonal to the requirement dependencies as configured by <i>Requires=</i>. It is a common pattern to include a unit name in both the <i>After=</i> and <i>Requires=</i> option, in which case the unit listed will be started before the unit that is configured with these options. This option may be specified more than once, in which case ordering dependencies for all listed names are created. <i>After=</i> is the inverse of <i>Before=</i>, i.e. while <i>After=</i> ensures that the configured unit is started after the listed unit finished starting up, <i>Before=</i> ensures the opposite, i.e. that the configured unit is fully started up before the listed unit is started. Note that when two units with an ordering dependency between them are shut down, the inverse of the start-up order is applied. i.e. if a unit is configured with <i>After=</i> on another unit, the former is stopped before the latter if both are shut down. If one unit with an ordering dependency on another unit is shut down while the latter is started up, the shut down is ordered before the start-up regardless of whether the ordering dependency is actually of type <i>After=</i> or <i>Before=</i>. If two units have no ordering dependencies between them, they are shut down or started up simultaneously, and no ordering takes place.</dl>
<p> <i>OnFailure=</i></p>
<dl>
<dd>A space-separated list of one or more units that are activated when this unit enters the &quot;failed&quot; state.</dl>
<p> <i>PropagatesReloadTo=</i>, <i>ReloadPropagatedFrom=</i></p>
<dl>
<dd>A space-separated list of one or more units where reload requests on this unit will be propagated to, or reload requests on the other unit will be propagated to this unit, respectively. Issuing a reload request on a unit will automatically also enqueue a reload request on all units that the reload request shall be propagated to via these two settings.</dl>
<p> <i>JoinsNamespaceOf=</i></p>
<dl>
<dd>For units that start processes (such as service units), lists one or more other units whose network and/or temporary file namespace to join. This only applies to unit types which support the <i>PrivateNetwork=</i> and <i>PrivateTmp=</i> directives (see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details). If a unit that has this setting set is started, its processes will see the same /tmp, /tmp/var and network namespace as one listed unit that is started. If multiple listed units are already started, it is not defined which namespace is joined. Note that this setting only has an effect if <i>PrivateNetwork=</i> and/or <i>PrivateTmp=</i> is enabled for both the unit that joins the namespace and the unit whose namespace is joined.</dl>
<p> <i>RequiresMountsFor=</i></p>
<dl>
<dd>Takes a space-separated list of absolute paths. Automatically adds dependencies of type <i>Requires=</i> and <i>After=</i> for all mount units required to access the specified path. </p>
<p> Mount points marked with <code>noauto</code> are not mounted automatically and will be ignored for the purposes of this option. If such a mount should be a requirement for this unit, direct dependencies on the mount units may be added (<i>Requires=</i> and <i>After=</i> or some other combination).</dl>
<p> <i>OnFailureJobMode=</i></p>
<dl>
<dd>Takes a value of &quot;fail&quot;, &quot;replace&quot;, &quot;replace-irreversibly&quot;, &quot;isolate&quot;, &quot;flush&quot;, &quot;ignore-dependencies&quot; or &quot;ignore-requirements&quot;. Defaults to &quot;replace&quot;. Specifies how the units listed in <i>OnFailure=</i> will be enqueued. See <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1)&#8217;s <code>&#8211;job-mode=</code> option for details on the possible values. If this is set to &quot;isolate&quot;, only a single unit may be listed in <i>OnFailure=</i>..</dl>
<p> <i>IgnoreOnIsolate=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, this unit will not be stopped when isolating another unit. Defaults to <code>false</code>.</dl>
<p> <i>IgnoreOnSnapshot=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, this unit will not be included in snapshots. Defaults to <code>true</code> for device and snapshot units, <code>false</code> for the others.</dl>
<p> <i>StopWhenUnneeded=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, this unit will be stopped when it is no longer used. Note that in order to minimize the work to be executed, systemd will not stop units by default unless they are conflicting with other units, or the user explicitly requested their shut down. If this option is set, a unit will be automatically cleaned up if no other active unit requires it. Defaults to <code>false</code>.</dl>
<p> <i>RefuseManualStart=</i>, <i>RefuseManualStop=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, this unit can only be activated or deactivated indirectly. In this case, explicit start-up or termination requested by the user is denied, however if it is started or stopped as a dependency of another unit, start-up or termination will succeed. This is mostly a safety feature to ensure that the user does not accidentally activate units that are not intended to be activated explicitly, and not accidentally deactivate units that are not intended to be deactivated. These options default to <code>false</code>.</dl>
<p> <i>AllowIsolate=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, this unit may be used with the <code>systemctl isolate</code> command. Otherwise, this will be refused. It probably is a good idea to leave this disabled except for target units that shall be used similar to runlevels in SysV init systems, just as a precaution to avoid unusable system states. This option defaults to <code>false</code>.</dl>
<p> <i>DefaultDependencies=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, (the default), a few default dependencies will implicitly be created for the unit. The actual dependencies created depend on the unit type. For example, for service units, these dependencies ensure that the service is started only after basic system initialization is completed and is properly terminated on system shutdown. See the respective man pages for details. Generally, only services involved with early boot or late shutdown should set this option to <code>false</code>. It is highly recommended to leave this option enabled for the majority of common units. If set to <code>false</code>, this option does not disable all implicit dependencies, just non-essential ones.</dl>
<p> <i>JobTimeoutSec=</i>, <i>JobTimeoutAction=</i>, <i>JobTimeoutRebootArgument=</i></p>
<dl>
<dd>When a job for this unit is queued a time-out may be configured. If this time limit is reached, the job will be cancelled, the unit however will not change state or even enter the &quot;failed&quot; mode. This value defaults to 0 (job timeouts disabled), except for device units. NB: this timeout is independent from any unit-specific timeout (for example, the timeout set with <i>StartTimeoutSec=</i> in service units) as the job timeout has no effect on the unit itself, only on the job that might be pending for it. Or in other words: unit-specific timeouts are useful to abort unit state changes, and revert them. The job timeout set with this option however is useful to abort only the job waiting for the unit state to change. </p>
<p> <i>JobTimeoutAction=</i> optionally configures an additional action to take when the time-out is hit. It takes the same values as the per-service <i>StartLimitAction=</i> setting, see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details. Defaults to <code>none</code>. <i>JobTimeoutRebootArgument=</i> configures an optional reboot string to pass to the <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2) system call.</dl>
<p> <i>ConditionArchitecture=</i>, <i>ConditionVirtualization=</i>, <i>ConditionHost=</i>, <i>ConditionKernelCommandLine=</i>, <i>ConditionSecurity=</i>, <i>ConditionCapability=</i>, <i>ConditionACPower=</i>, <i>ConditionNeedsUpdate=</i>, <i>ConditionFirstBoot=</i>, <i>ConditionPathExists=</i>, <i>ConditionPathExistsGlob=</i>, <i>ConditionPathIsDirectory=</i>, <i>ConditionPathIsSymbolicLink=</i>, <i>ConditionPathIsMountPoint=</i>, <i>ConditionPathIsReadWrite=</i>, <i>ConditionDirectoryNotEmpty=</i>, <i>ConditionFileNotEmpty=</i>, <i>ConditionFileIsExecutable=</i>, <i>ConditionNull=</i></p>
<dl>
<dd>Before starting a unit verify that the specified condition is true. If it is not true, the starting of the unit will be skipped, however all ordering dependencies of it are still respected. A failing condition will not result in the unit being moved into a failure state. The condition is checked at the time the queued start job is to be executed. </p>
<p> <i>ConditionArchitecture=</i> may be used to check whether the system is running on a specific architecture. Takes one of <i>x86</i>, <i>x86-64</i>, <i>ppc</i>, <i>ppc-le</i>, <i>ppc64</i>, <i>ppc64-le</i>, <i>ia64</i>, <i>parisc</i>, <i>parisc64</i>, <i>s390</i>, <i>s390x</i>, <i>sparc</i>, <i>sparc64</i>, <i>mips</i>, <i>mips-le</i>, <i>mips64</i>, <i>mips64-le</i>, <i>alpha</i>, <i>arm</i>, <i>arm-be</i>, <i>arm64</i>, <i>arm64-be</i>, <i>sh</i>, <i>sh64</i>, <i>m86k</i>, <i>tilegx</i>, <i>cris</i> to test against a specific architecture. The architecture is determined from the information returned by <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2) and is thus subject to <code><a href="/docs/linux/man/2-personality/">personality</a></code>(2). Note that a <i>Personality=</i> setting in the same unit file has no effect on this condition. A special architecture name <i>native</i> is mapped to the architecture the system manager itself is compiled for. The test may be negated by prepending an exclamation mark. </p>
<p> <i>ConditionVirtualization=</i> may be used to check whether the system is executed in a virtualized environment and optionally test whether it is a specific implementation. Takes either boolean value to check if being executed in any virtualized environment, or one of <i>vm</i> and <i>container</i> to test against a generic type of virtualization solution, or one of <i>qemu</i>, <i>kvm</i>, <i>zvm</i>, <i>vmware</i>, <i>microsoft</i>, <i>oracle</i>, <i>xen</i>, <i>bochs</i>, <i>uml</i>, <i>openvz</i>, <i>lxc</i>, <i>lxc-libvirt</i>, <i>systemd-nspawn</i>, <i>docker</i> to test against a specific implementation. See <code><a href="/docs/linux/man/1-systemd-detect-virt/">systemd-detect-virt</a></code>(1) for a full list of known virtualization technologies and their identifiers. If multiple virtualization technologies are nested, only the innermost is considered. The test may be negated by prepending an exclamation mark. </p>
<p> <i>ConditionHost=</i> may be used to match against the hostname or machine ID of the host. This either takes a hostname string (optionally with shell style globs) which is tested against the locally set hostname as returned by <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2), or a machine ID formatted as string (see <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5)). The test may be negated by prepending an exclamation mark. </p>
<p> <i>ConditionKernelCommandLine=</i> may be used to check whether a specific kernel command line option is set (or if prefixed with the exclamation mark unset). The argument must either be a single word, or an assignment (i.e. two words, separated &quot;=&quot;). In the former case the kernel command line is searched for the word appearing as is, or as left hand side of an assignment. In the latter case, the exact assignment is looked for with right and left hand side matching. </p>
<p> <i>ConditionSecurity=</i> may be used to check whether the given security module is enabled on the system. Currently the recognized values values are <i>selinux</i>, <i>apparmor</i>, <i>ima</i> and <i>smack</i>. The test may be negated by prepending an exclamation mark. </p>
<p> <i>ConditionCapability=</i> may be used to check whether the given capability exists in the capability bounding set of the service manager (i.e. this does not check whether capability is actually available in the permitted or effective sets, see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for details). Pass a capability name such as &quot;CAP_MKNOD&quot;, possibly prefixed with an exclamation mark to negate the check. </p>
<p> <i>ConditionACPower=</i> may be used to check whether the system has AC power, or is exclusively battery powered at the time of activation of the unit. This takes a boolean argument. If set to <i>true</i>, the condition will hold only if at least one AC connector of the system is connected to a power source, or if no AC connectors are known. Conversely, if set to <i>false</i>, the condition will hold only if there is at least one AC connector known and all AC connectors are disconnected from a power source. </p>
<p> <i>ConditionNeedsUpdate=</i> takes one of /var or /etc as argument, possibly prefixed with a &quot;!&quot; (for inverting the condition). This condition may be used to conditionalize units on whether the specified directory requires an update because /usr&#8217;s modification time is newer than the stamp file .updated in the specified directory. This is useful to implement offline updates of the vendor operating system resources in /usr that require updating of /etc or /var on the next following boot. Units making use of this condition should order themselves before <code><a href="/docs/linux/man/8-systemd-update-done-service/">systemd-update-done.service</a></code>(8), to make sure they run before the stamp files&#8217;s modification time gets reset indicating a completed update. </p>
<p> <i>ConditionFirstBoot=</i> takes a boolean argument. This condition may be used to conditionalize units on whether the system is booting up with an unpopulated /etc directory. This may be used to populate /etc on the first boot after factory reset, or when a new system instances boots up for the first time. </p>
<p> With <i>ConditionPathExists=</i> a file existence condition is checked before a unit is started. If the specified absolute path name does not exist, the condition will fail. If the absolute path name passed to <i>ConditionPathExists=</i> is prefixed with an exclamation mark (&quot;!&quot;), the test is negated, and the unit is only started if the path does not exist. </p>
<p> <i>ConditionPathExistsGlob=</i> is similar to <i>ConditionPathExists=</i>, but checks for the existence of at least one file or directory matching the specified globbing pattern. </p>
<p> <i>ConditionPathIsDirectory=</i> is similar to <i>ConditionPathExists=</i> but verifies whether a certain path exists and is a directory. </p>
<p> <i>ConditionPathIsSymbolicLink=</i> is similar to <i>ConditionPathExists=</i> but verifies whether a certain path exists and is a symbolic link. </p>
<p> <i>ConditionPathIsMountPoint=</i> is similar to <i>ConditionPathExists=</i> but verifies whether a certain path exists and is a mount point. </p>
<p> <i>ConditionPathIsReadWrite=</i> is similar to <i>ConditionPathExists=</i> but verifies whether the underlying file system is readable and writable (i.e. not mounted read-only). </p>
<p> <i>ConditionDirectoryNotEmpty=</i> is similar to <i>ConditionPathExists=</i> but verifies whether a certain path exists and is a non-empty directory. </p>
<p> <i>ConditionFileNotEmpty=</i> is similar to <i>ConditionPathExists=</i> but verifies whether a certain path exists and refers to a regular file with a non-zero size. </p>
<p> <i>ConditionFileIsExecutable=</i> is similar to <i>ConditionPathExists=</i> but verifies whether a certain path exists, is a regular file and marked executable. </p>
<p> Finally, <i>ConditionNull=</i> may be used to add a constant condition check value to the unit. It takes a boolean argument. If set to <i>false</i>, the condition will always fail, otherwise succeed. </p>
<p> If multiple conditions are specified, the unit will be executed if all of them apply (i.e. a logical AND is applied). Condition checks can be prefixed with a pipe symbol (|) in which case a condition becomes a triggering condition. If at least one triggering condition is defined for a unit, then the unit will be executed if at least one of the triggering conditions apply and all of the non-triggering conditions. If you prefix an argument with the pipe symbol and an exclamation mark, the pipe symbol must be passed first, the exclamation second. Except for <i>ConditionPathIsSymbolicLink=</i>, all path checks follow symlinks. If any of these options is assigned the empty string, the list of conditions is reset completely, all previous condition settings (of any kind) will have no effect.</dl>
<p> <i>SourcePath=</i></p>
<dl>
<dd>A path to a configuration file this unit has been generated from. This is primarily useful for implementation of generator tools that convert configuration from an external configuration file format into native unit files. This functionality should not be used in normal units.</dl>
<h2>[Install] Section Options</h2>
<p>Unit file may include an &quot;[Install]&quot; section, which carries installation information for the unit. This section is not interpreted by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) during runtime. It is used exclusively by the <code>enable</code> and <code>disable</code> commands of the <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) tool during installation of a unit: </p>
<p> <i>Alias=</i></p>
<dl>
<dd>A space-separated list of additional names this unit shall be installed under. The names listed here must have the same suffix (i.e. type) as the unit file name. This option may be specified more than once, in which case all listed names are used. At installation time, <code>systemctl enable</code> will create symlinks from these names to the unit filename.</dl>
<p> <i>WantedBy=</i>, <i>RequiredBy=</i></p>
<dl>
<dd>This option may be used more than once, or a space-separated list of unit names may be given. A symbolic link is created in the .wants/ or .requires/ directory of each of the listed units when this unit is installed by <code>systemctl enable</code>. This has the effect that a dependency of type <i>Wants=</i> or <i>Requires=</i> is added from the listed unit to the current unit. The primary result is that the current unit will be started when the listed unit is started. See the description of <i>Wants=</i> and <i>Requires=</i> in the [Unit] section for details. </p>
<p> <code>WantedBy=foo.service</code> in a service bar.service is mostly equivalent to <code>Alias=foo.service.wants/bar.service</code> in the same file. In case of template units, <code>systemctl enable</code> must be called with an instance name, and this instance will be added to the .wants/ or .requires/ list of the listed unit. E.g. <code>WantedBy=getty.target</code> in a service getty [at] .service will result in <code>systemctl enable getty [at] tty2.service</code> creating a getty.target.wants/getty [at] tty2.service link to getty [at] .service.</dl>
<p> <i>Also=</i></p>
<dl>
<dd>Additional units to install/deinstall when this unit is installed/deinstalled. If the user requests installation/deinstallation of a unit with this option configured, <code>systemctl enable</code> and <code>systemctl disable</code> will automatically install/uninstall units listed in this option as well. </p>
<p> This option may be used more than once, or a space-separated list of unit names may be given.</dl>
<p> <i>DefaultInstance=</i></p>
<dl>
<dd>In template unit files, this specifies for which instance the unit shall be enabled if the template is enabled without any explicitly set instance. This option has no effect in non-template unit files. The specified string must be usable as instance identifier.</dl>
<p> The following specifiers are interpreted in the Install section: %n, %N, %p, %i, %U, %u, %m, %H, %b, %v. For their meaning see the next section.</p>
<h2>Specifiers</h2>
<p>Many settings resolve specifiers which may be used to write generic unit files referring to runtime or unit parameters that are replaced when the unit files are loaded. The following specifiers are understood: </p>
<p> <code>Table 3. Specifiers available in unit files</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Specifier </code></td>
<td><code> Meaning </code></td>
<td><code> Details </code>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%n&quot; </td>
<td> Full unit name </td>
<td> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%N&quot; </td>
<td> Unescaped full unit name </td>
<td> Same as &quot;%n&quot;, but with escaping undone
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%p&quot; </td>
<td> Prefix name </td>
<td> For instantiated units, this refers to the string before the &quot;@&quot; character of the unit name. For non-instantiated units, this refers to the name of the unit with the type suffix removed.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%P&quot; </td>
<td> Unescaped prefix name </td>
<td> Same as &quot;%p&quot;, but with escaping undone
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%i&quot; </td>
<td> Instance name </td>
<td> For instantiated units: this is the string between the &quot;@&quot; character and the suffix of the unit name.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%I&quot; </td>
<td> Unescaped instance name </td>
<td> Same as &quot;%i&quot;, but with escaping undone
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%f&quot; </td>
<td> Unescaped filename </td>
<td> This is either the unescaped instance name (if applicable) with / prepended (if applicable), or the prefix name prepended with /.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%c&quot; </td>
<td> Control group path of the unit </td>
<td> This path does not include the /sys/fs/cgroup/systemd/ prefix.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%r&quot; </td>
<td> Control group path of the slice the unit is placed in </td>
<td> This usually maps to the parent cgroup path of &quot;%c&quot;.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%R&quot; </td>
<td> Root control group path below which slices and units are placed </td>
<td> For system instances, this resolves to /, except in containers, where this maps to the container&#8217;s root control group path.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%t&quot; </td>
<td> Runtime directory </td>
<td> This is either /run (for the system manager) or the path &quot;$XDG_RUNTIME_DIR&quot; resolves to (for user managers).
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%u&quot; </td>
<td> User name </td>
<td> This is the name of the configured user of the unit, or (if none is set) the user running the systemd instance.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%U&quot; </td>
<td> User UID </td>
<td> This is the numeric UID of the configured user of the unit, or (if none is set) the user running the systemd user instance. Note that this specifier is not available for units run by the systemd system instance (as opposed to those run by a systemd user instance), unless the user has been configured as a numeric UID in the first place or the configured user is the root user.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%h&quot; </td>
<td> User home directory </td>
<td> This is the home directory of the configured user of the unit, or (if none is set) the user running the systemd user instance. Similar to &quot;%U&quot;, this specifier is not available for units run by the systemd system instance, unless the configured user is the root user.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%s&quot; </td>
<td> User shell </td>
<td> This is the shell of the configured user of the unit, or (if none is set) the user running the systemd user instance. Similar to &quot;%U&quot;, this specifier is not available for units run by the systemd system instance, unless the configured user is the root user.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%m&quot; </td>
<td> Machine ID </td>
<td> The machine ID of the running system, formatted as string. See <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%b&quot; </td>
<td> Boot ID </td>
<td> The boot ID of the running system, formatted as string. See <code><a href="/docs/linux/man/4-random/">random</a></code>(4) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%H&quot; </td>
<td> Host name </td>
<td> The hostname of the running system at the point in time the unit configuation is loaded.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%v&quot; </td>
<td> Kernel release </td>
<td> Identical to <code>uname -r</code> output
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%%&quot; </td>
<td> Single percent sign </td>
<td> Use &quot;%%&quot; in place of &quot;%&quot; to specify a single percent sign.
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5), <code><a href="/docs/linux/man/5-systemd-path/">systemd.path</a></code>(5), <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5), <code><a href="/docs/linux/man/5-systemd-snapshot/">systemd.snapshot</a></code>(5), <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7), <code><a href="/docs/linux/man/1-systemd-verify/">systemd-verify</a></code>(1), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/1-uname/">uname</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>XDG Desktop Entry Specification</p>
<dl>
<dd><a rel="nofollow" href="http://standards.freedesktop.org/desktop-entry-spec/latest/">http://standards.freedesktop.org/desktop-entry-spec/latest/</a></dl>
<dt> 2.</p>
<dd>Interface Stability Promise</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/InterfaceStabilityPromise">http://www.freedesktop.org/wiki/Software/systemd/InterfaceStabilityPromise</a></dl>
<dt> 3.</p>
<dd>Generators</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/Generators/">http://www.freedesktop.org/wiki/Software/systemd/Generators/</a></dl>
