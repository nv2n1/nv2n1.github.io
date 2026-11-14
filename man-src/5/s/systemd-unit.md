---
title: "systemd-unit(5)"
name: "systemd-unit"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-unit/"
description: "systemd.unit – Unit configuration"
---

<p>systemd.unit &#8211; Unit configuration</p>
<h2>Synopsis</h2>
<p><i>service</i>.service, <i>socket</i>.socket, <i>device</i>.device, <i>mount</i>.mount, <i>automount</i>.automount, <i>swap</i>.swap, <i>target</i>.target, <i>path</i>.path, <i>timer</i>.timer, <i>slice</i>.slice, <i>scope</i>.scope</p>
<h3>System Unit Search Path</h3>
<pre>/etc/systemd/system.control/*
/run/systemd/system.control/*
/run/systemd/transient/*
/run/systemd/generator.early/*
/etc/systemd/system/*
/etc/systemd/system.attached/*
/run/systemd/system/*
/run/systemd/system.attached/*
/run/systemd/generator/*
...
/lib/systemd/system/*
/run/systemd/generator.late/*</pre>
<h3>User Unit Search Path</h3>
<pre>~/.config/systemd/user.control/*
$XDG_RUNTIME_DIR/systemd/user.control/*
$XDG_RUNTIME_DIR/systemd/transient/*
$XDG_RUNTIME_DIR/systemd/generator.early/*
~/.config/systemd/user/*
$XDG_CONFIG_DIRS/systemd/user/*
/etc/systemd/user/*
$XDG_RUNTIME_DIR/systemd/user/*
/run/systemd/user/*
$XDG_RUNTIME_DIR/systemd/generator/*
$XDG_DATA_HOME/systemd/user/*
$XDG_DATA_DIRS/systemd/user/*
...
/usr/lib/systemd/user/*
$XDG_RUNTIME_DIR/systemd/generator.late/*</pre>
<h2>Description</h2>
<p>A unit file is a plain text ini-style file that encodes information about a service, a socket, a device, a mount point, an automount point, a swap file or partition, a start-up target, a watched file system path, a timer controlled and supervised by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), a resource management slice or a group of externally created processes. See <code><a href="/docs/linux/man/7-systemd-syntax/">systemd.syntax</a></code>(7) for a general description of the syntax. </p>
<p> This man page lists the common configuration options of all the unit types. These options need to be configured in the [Unit] or [Install] sections of the unit files. </p>
<p> In addition to the generic [Unit] and [Install] sections described here, each unit may have a type-specific section, e.g. [Service] for a service unit. See the respective man pages for more information: <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5), <code><a href="/docs/linux/man/5-systemd-path/">systemd.path</a></code>(5), <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5). </p>
<p> Unit files are loaded from a set of paths determined during compilation, described in the next section. </p>
<p> Valid unit names consist of a &quot;name prefix&quot; and a dot and a suffix specifying the unit type. The &quot;unit prefix&quot; must consist of one or more valid characters (ASCII letters, digits, &quot;:&quot;, &quot;-&quot;, &quot;_&quot;, &quot;.&quot;, and &quot;\&quot;). The total length of the unit name including the suffix must not exceed 256 characters. The type suffix must be one of &quot;.service&quot;, &quot;.socket&quot;, &quot;.device&quot;, &quot;.mount&quot;, &quot;.automount&quot;, &quot;.swap&quot;, &quot;.target&quot;, &quot;.path&quot;, &quot;.timer&quot;, &quot;.slice&quot;, or &quot;.scope&quot;. </p>
<p> Units names can be parameterized by a single argument called the &quot;instance name&quot;. The unit is then constructed based on a &quot;template file&quot; which serves as the definition of multiple services or other units. A template unit must have a single &quot;@&quot; at the end of the name (right before the type suffix). The name of the full unit is formed by inserting the instance name between &quot;@&quot; and the unit type suffix. In the unit file itself, the instance parameter may be referred to using &quot;%i&quot; and other specifiers, see below. </p>
<p> Unit files may contain additional options on top of those listed here. If systemd encounters an unknown option, it will write a warning log message but continue loading the unit. If an option or section name is prefixed with <code>X-</code>, it is ignored completely by systemd. Options within an ignored section do not need the prefix. Applications may use this to include additional information in the unit files. To access those options, applications need to parse the unit files on their own. </p>
<p> Units can be aliased (have an alternative name), by creating a symlink from the new name to the existing name in one of the unit search paths. For example, systemd-networkd.service has the alias dbus-org.freedesktop.network1.service, created during installation as a symlink, so when <code>systemd</code> is asked through D-Bus to load dbus-org.freedesktop.network1.service, it&#8217;ll load systemd-networkd.service. As another example, default.target &#8212; the default system target started at boot &#8212; is commonly symlinked (aliased) to either multi-user.target or graphical.target to select what is started by default. Alias names may be used in commands like <code>disable</code>, <code>start</code>, <code>stop</code>, <code>status</code>, and similar, and in all unit dependency directives, including <i>Wants=</i>, <i>Requires=</i>, <i>Before=</i>, <i>After=</i>. Aliases cannot be used with the <code>preset</code> command. </p>
<p> Aliases obey the following restrictions: a unit of a certain type (&quot;.service&quot;, &quot;.socket&quot;, &#8230;) can only be aliased by a name with the same type suffix. A plain unit (not a template or an instance), may only be aliased by a plain name. A template instance may only be aliased by another template instance, and the instance part must be identical. A template may be aliased by another template (in which case the alias applies to all instances of the template). As a special case, a template instance (e.g. &quot;alias [at] inst.service&quot;) may be a symlink to different template (e.g. &quot;template [at] inst.service&quot;). In that case, just this specific instance is aliased, while other instances of the template (e.g. &quot;alias [at] foo.service&quot;, &quot;alias [at] bar.service&quot;) are not aliased. Those rule preserve the requirement that the instance (if any) is always uniquely defined for a given unit and all its aliases. </p>
<p> Unit files may specify aliases through the <i>Alias=</i> directive in the [Install] section. When the unit is enabled, symlinks will be created for those names, and removed when the unit is disabled. For example, reboot.target specifies <i>Alias=ctrl-alt-del.target</i>, so when enabled, the symlink /etc/systemd/system/ctrl-alt-del.service pointing to the reboot.target file will be created, and when Ctrl+Alt+Del is invoked, <code>systemd</code> will look for the ctrl-alt-del.service and execute reboot.service. <code>systemd</code> does not look at the [Install] section at all during normal operation, so any directives in that section only have an effect through the symlinks created during enablement. </p>
<p> Along with a unit file foo.service, the directory foo.service.wants/ may exist. All unit files symlinked from such a directory are implicitly added as dependencies of type <i>Wants=</i> to the unit. Similar functionality exists for <i>Requires=</i> type dependencies as well, the directory suffix is .requires/ in this case. This functionality is useful to hook units into the start-up of other units, without having to modify their unit files. For details about the semantics of <i>Wants=</i>, see below. The preferred way to create symlinks in the .wants/ or .requires/ directory of a unit file is by embedding the dependency in [Install] section of the target unit, and creating the symlink in the file system with the <code>enable</code> or <code>preset</code> commands of <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1). </p>
<p> Along with a unit file foo.service, a &quot;drop-in&quot; directory foo.service.d/ may exist. All files with the suffix &quot;.conf&quot; from this directory will be merged in the alphanumeric order and parsed after the main unit file itself has been parsed. This is useful to alter or add configuration settings for a unit, without having to modify unit files. Each drop-in file must contain appropriate section headers. For instantiated units, this logic will first look for the instance &quot;.d/&quot; subdirectory (e.g. &quot;foo [at] bar.service.d/&quot;) and read its &quot;.conf&quot; files, followed by the template &quot;.d/&quot; subdirectory (e.g. &quot;foo [at] .service.d/&quot;) and the &quot;.conf&quot; files there. Moreover for unit names containing dashes (&quot;-&quot;), the set of directories generated by repeatedly truncating the unit name after all dashes is searched too. Specifically, for a unit name foo-bar-baz.service not only the regular drop-in directory foo-bar-baz.service.d/ is searched but also both foo-bar-.service.d/ and foo-.service.d/. This is useful for defining common drop-ins for a set of related units, whose names begin with a common prefix. This scheme is particularly useful for mount, automount and slice units, whose systematic naming structure is built around dashes as component separators. Note that equally named drop-in files further down the prefix hierarchy override those further up, i.e. foo-bar-.service.d/10-override.conf overrides foo-.service.d/10-override.conf. </p>
<p> In cases of unit aliases (described above), dropins for the aliased name and all aliases are loaded. In the example of default.target aliasing graphical.target, default.target.d/, default.target.wants/, default.target.requires/, graphical.target.d/, graphical.target.wants/, graphical.target.requires/ would all be read. For templates, dropins for the template, any template aliases, the template instance, and all alias instances are read. When just a specific template instance is aliased, then the dropins for the target template, the target template instance, and the alias template instance are read. </p>
<p> In addition to /etc/systemd/system, the drop-in &quot;.d/&quot; directories for system services can be placed in /lib/systemd/system or /run/systemd/system directories. Drop-in files in /etc/ take precedence over those in /run/ which in turn take precedence over those in /lib/. Drop-in files under any of these directories take precedence over unit files wherever located. Multiple drop-in files with different names are applied in lexicographic order, regardless of which of the directories they reside in. </p>
<p> Units also support a top-level drop-in with <i>type</i>.d/, where <i>type</i> may be e.g. &quot;service&quot; or &quot;socket&quot;, that allows altering or adding to the settings of all corresponding unit files on the system. The formatting and precedence of applying drop-in configurations follow what is defined above. Files in <i>type</i>.d/ have lower precedence compared to files in name-specific override directories. The usual rules apply: multiple drop-in files with different names are applied in lexicographic order, regardless of which of the directories they reside in, so a file in <i>type</i>.d/ applies to a unit only if there are no drop-ins or masks with that name in directories with higher precedence. See Examples. </p>
<p> Note that while systemd offers a flexible dependency system between units it is recommended to use this functionality only sparingly and instead rely on techniques such as bus-based or socket-based activation which make dependencies implicit, resulting in a both simpler and more flexible system. </p>
<p> As mentioned above, a unit may be instantiated from a template file. This allows creation of multiple units from a single configuration file. If systemd looks for a unit configuration file, it will first search for the literal unit name in the file system. If that yields no success and the unit name contains an &quot;@&quot; character, systemd will look for a unit template that shares the same name but with the instance string (i.e. the part between the &quot;@&quot; character and the suffix) removed. Example: if a service getty [at] tty3.service is requested and no file by that name is found, systemd will look for getty [at] .service and instantiate a service from that configuration file if it is found. </p>
<p> To refer to the instance string from within the configuration file you may use the special &quot;%i&quot; specifier in many of the configuration options. See below for details. </p>
<p> If a unit file is empty (i.e. has the file size 0) or is symlinked to /dev/null, its configuration will not be loaded and it appears with a load state of &quot;masked&quot;, and cannot be activated. Use this as an effective way to fully disable a unit, making it impossible to start it even manually. </p>
<p> The unit file format is covered by the m[blue]<code>Interface Portability and Stability Promise</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>String Escaping For Inclusion In Unit Names</h2>
<p>Sometimes it is useful to convert arbitrary strings into unit names. To facilitate this, a method of string escaping is used, in order to map strings containing arbitrary byte values (except <code>NUL</code>) into valid unit names and their restricted character set. A common special case are unit names that reflect paths to objects in the file system hierarchy. Example: a device unit dev-sda.device refers to a device with the device node /dev/sda in the file system. </p>
<p> The escaping algorithm operates as follows: given a string, any &quot;/&quot; character is replaced by &quot;-&quot;, and all other characters which are not ASCII alphanumerics, &quot;:&quot;, &quot;_&quot; or &quot;.&quot; are replaced by C-style &quot;-&quot; escapes. In addition, &quot;.&quot; is replaced with such a C-style escape when it would appear as the first character in the escaped string. </p>
<p> When the input qualifies as absolute file system path, this algorithm is extended slightly: the path to the root directory &quot;/&quot; is encoded as single dash &quot;-&quot;. In addition, any leading, trailing or duplicate &quot;/&quot; characters are removed from the string before transformation. Example: /foo//bar/baz/ becomes &quot;foo-bar-baz&quot;. </p>
<p> This escaping is fully reversible, as long as it is known whether the escaped string was a path (the unescaping results are different for paths and non-path strings). The <code><a href="/docs/linux/man/1-systemd-escape/">systemd-escape</a></code>(1) command may be used to apply and reverse escaping on arbitrary strings. Use <code>systemd-escape &#8211;path</code> to escape path strings, and <code>systemd-escape</code> without <code>&#8211;path</code> otherwise.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>A number of unit dependencies are implicitly established, depending on unit type and unit configuration. These implicit dependencies can make unit configuration file cleaner. For the implicit dependencies in each unit type, please refer to section &quot;Implicit Dependencies&quot; in respective man pages. </p>
<p> For example, service units with <i>Type=dbus</i> automatically acquire dependencies of type <i>Requires=</i> and <i>After=</i> on dbus.socket. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details.</p>
<h3>Default Dependencies</h3>
<p>Default dependencies are similar to implicit dependencies, but can be turned on and off by setting <i>DefaultDependencies=</i> to <i>yes</i> (the default) and <i>no</i>, while implicit dependencies are always in effect. See section &quot;Default Dependencies&quot; in respective man pages for the effect of enabling <i>DefaultDependencies=</i> in each unit types. </p>
<p> For example, target units will complement all configured dependencies of type <i>Wants=</i> or <i>Requires=</i> with dependencies of type <i>After=</i> unless <i>DefaultDependencies=no</i> is set in the specified units. See <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5) for details. Note that this behavior can be turned off by setting <i>DefaultDependencies=no</i>.</p>
<h2>Unit File Load Path</h2>
<p>Unit files are loaded from a set of paths determined during compilation, described in the two tables below. Unit files found in directories listed earlier override files with the same name in directories lower in the list. </p>
<p> When the variable <i>$SYSTEMD_UNIT_PATH</i> is set, the contents of this variable overrides the unit load path. If <i>$SYSTEMD_UNIT_PATH</i> ends with an empty component (&quot;:&quot;), the usual unit load path will be appended to the contents of the variable. </p>
<p> <code>Table 1.&nbsp; Load path when running in system mode (&#8211;system).</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Path </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> /etc/systemd/system.control </td>
<td VALIGN=center ROWSPAN=2> Persistent and transient configuration created using the dbus API
</td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/system.control </td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/transient </td>
<td> Dynamic configuration for transient units
</td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/generator.early </td>
<td> Generated units with high priority (see <i>early-dir</i> in <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7))
</td>
</tr>
<tr VALIGN=top>
<td> /etc/systemd/system </td>
<td> System units created by the administrator
</td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/system </td>
<td> Runtime units
</td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/generator </td>
<td> Generated units with medium priority (see <i>normal-dir</i> in <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7))
</td>
</tr>
<tr VALIGN=top>
<td> /usr/local/lib/systemd/system </td>
<td> System units installed by the administrator
</td>
</tr>
<tr VALIGN=top>
<td> /lib/systemd/system </td>
<td> System units installed by the distribution package manager
</td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/generator.late </td>
<td> Generated units with low priority (see <i>late-dir</i> in <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7))
</td>
</tr>
</table>
<p> <code>Table 2.&nbsp; Load path when running in user mode (&#8211;user).</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Path </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_CONFIG_HOME/systemd/user.control or ~/.config/systemd/user.control </td>
<td VALIGN=center ROWSPAN=2> Persistent and transient configuration created using the dbus API (<i>$XDG_CONFIG_HOME</i> is used if set, ~/.config otherwise)
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_RUNTIME_DIR/systemd/user.control </td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/transient </td>
<td> Dynamic configuration for transient units
</td>
</tr>
<tr VALIGN=top>
<td> /run/systemd/generator.early </td>
<td> Generated units with high priority (see <i>early-dir</i> in <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7))
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_CONFIG_HOME/systemd/user or $HOME/.config/systemd/user </td>
<td> User configuration (<i>$XDG_CONFIG_HOME</i> is used if set, ~/.config otherwise)
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_CONFIG_DIRS/systemd/user or /etc/xdg/systemd/user </td>
<td> Additional configuration directories as specified by the XDG base directory specification (<i>$XDG_CONFIG_DIRS</i> is used if set, /etc/xdg otherwise)
</td>
</tr>
<tr VALIGN=top>
<td> /etc/systemd/user </td>
<td> User units created by the administrator
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
<td> $XDG_RUNTIME_DIR/systemd/generator </td>
<td> Generated units with medium priority (see <i>normal-dir</i> in <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7))
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_DATA_HOME/systemd/user or $HOME/.local/share/systemd/user </td>
<td> Units of packages that have been installed in the home directory (<i>$XDG_DATA_HOME</i> is used if set, ~/.local/share otherwise)
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_DATA_DIRS/systemd/user or /usr/local/share/systemd/user and /usr/share/systemd/user </td>
<td> Additional data directories as specified by the XDG base directory specification (<i>$XDG_DATA_DIRS</i> is used if set, /usr/local/share and /usr/share otherwise)
</td>
</tr>
<tr VALIGN=top>
<td> $dir/systemd/user for each <i>$dir</i> in <i>$XDG_DATA_DIRS</i> </td>
<td> Additional locations for installed user units, one for each entry in <i>$XDG_DATA_DIRS</i>
</td>
</tr>
<tr VALIGN=top>
<td> /usr/local/lib/systemd/user </td>
<td> User units installed by the administrator
</td>
</tr>
<tr VALIGN=top>
<td> /usr/lib/systemd/user </td>
<td> User units installed by the distribution package manager
</td>
</tr>
<tr VALIGN=top>
<td> $XDG_RUNTIME_DIR/systemd/generator.late </td>
<td> Generated units with low priority (see <i>late-dir</i> in <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7))
</td>
</tr>
</table>
<p> The set of load paths for the user manager instance may be augmented or changed using various environment variables. And environment variables may in turn be set using environment generators, see <code><a href="/docs/linux/man/7-systemd-environment-generator/">systemd.environment-generator</a></code>(7). In particular, <i>$XDG_DATA_HOME</i> and <i>$XDG_DATA_DIRS</i> may be easily set using <code><a href="/docs/linux/man/8-systemd-environment-d-generator/">systemd-environment-d-generator</a></code>(8). Thus, directories listed here are just the defaults. To see the actual list that would be used based on compilation options and current environment use </p>
<dl>
<dd>
<pre>systemd-analyze --user unit-paths</pre>
</dl>
<p> Moreover, additional units might be loaded into systemd from directories not on the unit load path by creating a symlink pointing to a unit file in the directories. You can use <code>systemctl link</code> for this operation. See <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) for its usage and precaution.</p>
<h2>Unit Garbage Collection</h2>
<p>The system and service manager loads a unit&#8217;s configuration automatically when a unit is referenced for the first time. It will automatically unload the unit configuration and state again when the unit is not needed anymore (&quot;garbage collection&quot;). A unit may be referenced through a number of different mechanisms: </p>
<dl>
<dd>1. Another loaded unit references it with a dependency such as <i>After=</i>, <i>Wants=</i>, &#8230;</dl>
<dl>
<dd>2. The unit is currently starting, running, reloading or stopping.</dl>
<dl>
<dd>3. The unit is currently in the <code>failed</code> state. (But see below.)</dl>
<dl>
<dd>4. A job for the unit is pending.</dl>
<dl>
<dd>5. The unit is pinned by an active IPC client program.</dl>
<dl>
<dd>6. The unit is a special &quot;perpetual&quot; unit that is always active and loaded. Examples for perpetual units are the root mount unit -.mount or the scope unit init.scope that the service manager itself lives in.</dl>
<dl>
<dd>7. The unit has running processes associated with it.</dl>
<p> The garbage collection logic may be altered with the <i>CollectMode=</i> option, which allows configuration whether automatic unloading of units that are in <code>failed</code> state is permissible, see below. </p>
<p> Note that when a unit&#8217;s configuration and state is unloaded, all execution results, such as exit codes, exit signals, resource consumption and other statistics are lost, except for what is stored in the log subsystem. </p>
<p> Use <code>systemctl daemon-reload</code> or an equivalent command to reload unit configuration while the unit is already loaded. In this case all configuration settings are flushed out and replaced with the new configuration (which however might not be in effect immediately), however all runtime state is saved/restored.</p>
<h2>[Unit] Section Options</h2>
<p>The unit file may include a [Unit] section, which carries generic information about the unit that is not dependent on the type of unit: </p>
<p> <i>Description=</i></p>
<dl>
<dd>A short human readable title of the unit. This may be used by <code>systemd</code> (and other UIs) as a user-visible label for the unit, so this string should identify the unit rather than describe it, despite the name. This string also shouldn&#8217;t just repeat the unit name. &quot;Apache2 Web Server&quot; is a good example. Bad examples are &quot;high-performance light-weight HTTP server&quot; (too generic) or &quot;Apache2&quot; (meaningless for people who do not know Apache, duplicates the unit name). <code>systemd</code> may use this string as a noun in status messages (&quot;Starting <i>description</i>&#8230;&quot;, &quot;Started <i>description</i>.&quot;, &quot;Reached target <i>description</i>.&quot;, &quot;Failed to start <i>description</i>.&quot;), so it should be capitalized, and should not be a full sentence, or a phrase with a continuous verb. Bad examples include &quot;exiting the container&quot; or &quot;updating the database once per day.&quot;.</dl>
<p> <i>Documentation=</i></p>
<dl>
<dd>A space-separated list of URIs referencing documentation for this unit or its configuration. Accepted are only URIs of the types &quot;http://&quot;, &quot;https://&quot;, &quot;file:&quot;, &quot;info:&quot;, &quot;man:&quot;. For more information about the syntax of these URIs, see <code><a href="/docs/linux/man/7-uri/">uri</a></code>(7). The URIs should be listed in order of relevance, starting with the most relevant. It is a good idea to first reference documentation that explains what the unit&#8217;s purpose is, followed by how it is configured, followed by any other related documentation. This option may be specified more than once, in which case the specified list of URIs is merged. If the empty string is assigned to this option, the list is reset and all prior assignments will have no effect.</dl>
<p> <i>Wants=</i></p>
<dl>
<dd>Configures (weak) requirement dependencies on other units. This option may be specified more than once or multiple space-separated units may be specified in one option in which case dependencies for all listed names will be created. Dependencies of this type may also be configured outside of the unit configuration file by adding a symlink to a .wants/ directory accompanying the unit file. For details, see above. </p>
<p> Units listed in this option will be started if the configuring unit is. However, if the listed units fail to start or cannot be added to the transaction, this has no impact on the validity of the transaction as a whole, and this unit will still be started. This is the recommended way to hook the start-up of one unit to the start-up of another unit. </p>
<p> Note that requirement dependencies do not influence the order in which services are started or stopped. This has to be configured independently with the <i>After=</i> or <i>Before=</i> options. If unit foo.service pulls in unit bar.service as configured with <i>Wants=</i> and no ordering is configured with <i>After=</i> or <i>Before=</i>, then both units will be started simultaneously and without any delay between them if foo.service is activated.</dl>
<p> <i>Requires=</i></p>
<dl>
<dd>Similar to <i>Wants=</i>, but declares a stronger requirement dependency. Dependencies of this type may also be configured by adding a symlink to a .requires/ directory accompanying the unit file. </p>
<p> If this unit gets activated, the units listed will be activated as well. If one of the other units fails to activate, and an ordering dependency <i>After=</i> on the failing unit is set, this unit will not be started. Besides, with or without specifying <i>After=</i>, this unit will be stopped if one of the other units is explicitly stopped. </p>
<p> Often, it is a better choice to use <i>Wants=</i> instead of <i>Requires=</i> in order to achieve a system that is more robust when dealing with failing services. </p>
<p> Note that this dependency type does not imply that the other unit always has to be in active state when this unit is running. Specifically: failing condition checks (such as <i>ConditionPathExists=</i>, <i>ConditionPathIsSymbolicLink=</i>, &#8230; &#8212; see below) do not cause the start job of a unit with a <i>Requires=</i> dependency on it to fail. Also, some unit types may deactivate on their own (for example, a service process may decide to exit cleanly, or a device may be unplugged by the user), which is not propagated to units having a <i>Requires=</i> dependency. Use the <i>BindsTo=</i> dependency type together with <i>After=</i> to ensure that a unit may never be in active state without a specific other unit also in active state (see below).</dl>
<p> <i>Requisite=</i></p>
<dl>
<dd>Similar to <i>Requires=</i>. However, if the units listed here are not started already, they will not be started and the starting of this unit will fail immediately. <i>Requisite=</i> does not imply an ordering dependency, even if both units are started in the same transaction. Hence this setting should usually be combined with <i>After=</i>, to ensure this unit is not started before the other unit. </p>
<p> When <i>Requisite=b.service</i> is used on a.service, this dependency will show as <i>RequisiteOf=a.service</i> in property listing of b.service. <i>RequisiteOf=</i> dependency cannot be specified directly.</dl>
<p> <i>BindsTo=</i></p>
<dl>
<dd>Configures requirement dependencies, very similar in style to <i>Requires=</i>. However, this dependency type is stronger: in addition to the effect of <i>Requires=</i> it declares that if the unit bound to is stopped, this unit will be stopped too. This means a unit bound to another unit that suddenly enters inactive state will be stopped too. Units can suddenly, unexpectedly enter inactive state for different reasons: the main process of a service unit might terminate on its own choice, the backing device of a device unit might be unplugged or the mount point of a mount unit might be unmounted without involvement of the system and service manager. </p>
<p> When used in conjunction with <i>After=</i> on the same unit the behaviour of <i>BindsTo=</i> is even stronger. In this case, the unit bound to strictly has to be in active state for this unit to also be in active state. This not only means a unit bound to another unit that suddenly enters inactive state, but also one that is bound to another unit that gets skipped due to a failed condition check (such as <i>ConditionPathExists=</i>, <i>ConditionPathIsSymbolicLink=</i>, &#8230; &#8212; see below) will be stopped, should it be running. Hence, in many cases it is best to combine <i>BindsTo=</i> with <i>After=</i>. </p>
<p> When <i>BindsTo=b.service</i> is used on a.service, this dependency will show as <i>BoundBy=a.service</i> in property listing of b.service. <i>BoundBy=</i> dependency cannot be specified directly.</dl>
<p> <i>PartOf=</i></p>
<dl>
<dd>Configures dependencies similar to <i>Requires=</i>, but limited to stopping and restarting of units. When systemd stops or restarts the units listed here, the action is propagated to this unit. Note that this is a one-way dependency &#8212; changes to this unit do not affect the listed units. </p>
<p> When <i>PartOf=b.service</i> is used on a.service, this dependency will show as <i>ConsistsOf=a.service</i> in property listing of b.service. <i>ConsistsOf=</i> dependency cannot be specified directly.</dl>
<p> <i>Upholds=</i></p>
<dl>
<dd>Configures dependencies similar to <i>Wants=</i>, but as long a this unit is up, all units listed in <i>Upholds=</i> are started whenever found to be inactive or failed, and no job is queued for them. While a <i>Wants=</i> dependency on another unit has a one-time effect when this units started, a <i>Upholds=</i> dependency on it has a continuous effect, constantly restarting the unit if necessary. This is an alternative to the <i>Restart=</i> setting of service units, to ensure they are kept running whatever happens. </p>
<p> When <i>Upholds=b.service</i> is used on a.service, this dependency will show as <i>UpheldBy=a.service</i> in the property listing of b.service. The <i>UpheldBy=</i> dependency cannot be specified directly.</dl>
<p> <i>Conflicts=</i></p>
<dl>
<dd>A space-separated list of unit names. Configures negative requirement dependencies. If a unit has a <i>Conflicts=</i> setting on another unit, starting the former will stop the latter and vice versa. </p>
<p> Note that this setting does not imply an ordering dependency, similarly to the <i>Wants=</i> and <i>Requires=</i> dependencies described above. This means that to ensure that the conflicting unit is stopped before the other unit is started, an <i>After=</i> or <i>Before=</i> dependency must be declared. It doesn&#8217;t matter which of the two ordering dependencies is used, because stop jobs are always ordered before start jobs, see the discussion in <i>Before=</i>/<i>After=</i> below. </p>
<p> If unit A that conflicts with unit B is scheduled to be started at the same time as B, the transaction will either fail (in case both are required parts of the transaction) or be modified to be fixed (in case one or both jobs are not a required part of the transaction). In the latter case, the job that is not required will be removed, or in case both are not required, the unit that conflicts will be started and the unit that is conflicted is stopped.</dl>
<p> <i>Before=</i>, <i>After=</i></p>
<dl>
<dd>These two settings expect a space-separated list of unit names. They may be specified more than once, in which case dependencies for all listed names are created. </p>
<p> Those two settings configure ordering dependencies between units. If unit foo.service contains the setting <code>Before=bar.service</code> and both units are being started, bar.service&#8217;s start-up is delayed until foo.service has finished starting up. <i>After=</i> is the inverse of <i>Before=</i>, i.e. while <i>Before=</i> ensures that the configured unit is started before the listed unit begins starting up, <i>After=</i> ensures the opposite, that the listed unit is fully started up before the configured unit is started. </p>
<p> When two units with an ordering dependency between them are shut down, the inverse of the start-up order is applied. I.e. if a unit is configured with <i>After=</i> on another unit, the former is stopped before the latter if both are shut down. Given two units with any ordering dependency between them, if one unit is shut down and the other is started up, the shutdown is ordered before the start-up. It doesn&#8217;t matter if the ordering dependency is <i>After=</i> or <i>Before=</i>, in this case. It also doesn&#8217;t matter which of the two is shut down, as long as one is shut down and the other is started up; the shutdown is ordered before the start-up in all cases. If two units have no ordering dependencies between them, they are shut down or started up simultaneously, and no ordering takes place. It depends on the unit type when precisely a unit has finished starting up. Most importantly, for service units start-up is considered completed for the purpose of <i>Before=</i>/<i>After=</i> when all its configured start-up commands have been invoked and they either failed or reported start-up success. Note that this does includes <i>ExecStartPost=</i> (or <i>ExecStopPost=</i> for the shutdown case). </p>
<p> Note that those settings are independent of and orthogonal to the requirement dependencies as configured by <i>Requires=</i>, <i>Wants=</i>, <i>Requisite=</i>, or <i>BindsTo=</i>. It is a common pattern to include a unit name in both the <i>After=</i> and <i>Wants=</i> options, in which case the unit listed will be started before the unit that is configured with these options. </p>
<p> Note that <i>Before=</i> dependencies on device units have no effect and are not supported. Devices generally become available as a result of an external hotplug event, and systemd creates the corresponding device unit without delay.</dl>
<p> <i>OnFailure=</i></p>
<dl>
<dd>A space-separated list of one or more units that are activated when this unit enters the &quot;failed&quot; state. A service unit using <i>Restart=</i> enters the failed state only after the start limits are reached.</dl>
<p> <i>OnSuccess=</i></p>
<dl>
<dd>A space-separated list of one or more units that are activated when this unit enters the &quot;inactive&quot; state.</dl>
<p> <i>PropagatesReloadTo=</i>, <i>ReloadPropagatedFrom=</i></p>
<dl>
<dd>A space-separated list of one or more units to which reload requests from this unit shall be propagated to, or units from which reload requests shall be propagated to this unit, respectively. Issuing a reload request on a unit will automatically also enqueue reload requests on all units that are linked to it using these two settings.</dl>
<p> <i>PropagatesStopTo=</i>, <i>StopPropagatedFrom=</i></p>
<dl>
<dd>A space-separated list of one or more units to which stop requests from this unit shall be propagated to, or units from which stop requests shall be propagated to this unit, respectively. Issuing a stop request on a unit will automatically also enqueue stop requests on all units that are linked to it using these two settings.</dl>
<p> <i>JoinsNamespaceOf=</i></p>
<dl>
<dd>For units that start processes (such as service units), lists one or more other units whose network and/or temporary file namespace to join. This only applies to unit types which support the <i>PrivateNetwork=</i>, <i>NetworkNamespacePath=</i>, <i>PrivateIPC=</i>, <i>IPCNamespacePath=</i>, and <i>PrivateTmp=</i> directives (see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details). If a unit that has this setting set is started, its processes will see the same /tmp/, /var/tmp/, IPC namespace and network namespace as one listed unit that is started. If multiple listed units are already started, it is not defined which namespace is joined. Note that this setting only has an effect if <i>PrivateNetwork=</i>/<i>NetworkNamespacePath=</i>, <i>PrivateIPC=</i>/<i>IPCNamespacePath=</i> and/or <i>PrivateTmp=</i> is enabled for both the unit that joins the namespace and the unit whose namespace is joined.</dl>
<p> <i>RequiresMountsFor=</i></p>
<dl>
<dd>Takes a space-separated list of absolute paths. Automatically adds dependencies of type <i>Requires=</i> and <i>After=</i> for all mount units required to access the specified path. </p>
<p> Mount points marked with <code>noauto</code> are not mounted automatically through local-fs.target, but are still honored for the purposes of this option, i.e. they will be pulled in by this unit.</dl>
<p> <i>OnFailureJobMode=</i></p>
<dl>
<dd>Takes a value of &quot;fail&quot;, &quot;replace&quot;, &quot;replace-irreversibly&quot;, &quot;isolate&quot;, &quot;flush&quot;, &quot;ignore-dependencies&quot; or &quot;ignore-requirements&quot;. Defaults to &quot;replace&quot;. Specifies how the units listed in <i>OnFailure=</i> will be enqueued. See <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1)&#8217;s <code>&#8211;job-mode=</code> option for details on the possible values. If this is set to &quot;isolate&quot;, only a single unit may be listed in <i>OnFailure=</i>.</dl>
<p> <i>IgnoreOnIsolate=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, this unit will not be stopped when isolating another unit. Defaults to <code>false</code> for service, target, socket, timer, and path units, and <code>true</code> for slice, scope, device, swap, mount, and automount units.</dl>
<p> <i>StopWhenUnneeded=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, this unit will be stopped when it is no longer used. Note that, in order to minimize the work to be executed, systemd will not stop units by default unless they are conflicting with other units, or the user explicitly requested their shut down. If this option is set, a unit will be automatically cleaned up if no other active unit requires it. Defaults to <code>false</code>.</dl>
<p> <i>RefuseManualStart=</i>, <i>RefuseManualStop=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, this unit can only be activated or deactivated indirectly. In this case, explicit start-up or termination requested by the user is denied, however if it is started or stopped as a dependency of another unit, start-up or termination will succeed. This is mostly a safety feature to ensure that the user does not accidentally activate units that are not intended to be activated explicitly, and not accidentally deactivate units that are not intended to be deactivated. These options default to <code>false</code>.</dl>
<p> <i>AllowIsolate=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>true</code>, this unit may be used with the <code>systemctl isolate</code> command. Otherwise, this will be refused. It probably is a good idea to leave this disabled except for target units that shall be used similar to runlevels in SysV init systems, just as a precaution to avoid unusable system states. This option defaults to <code>false</code>.</dl>
<p> <i>DefaultDependencies=</i></p>
<dl>
<dd>Takes a boolean argument. If <code>yes</code>, (the default), a few default dependencies will implicitly be created for the unit. The actual dependencies created depend on the unit type. For example, for service units, these dependencies ensure that the service is started only after basic system initialization is completed and is properly terminated on system shutdown. See the respective man pages for details. Generally, only services involved with early boot or late shutdown should set this option to <code>no</code>. It is highly recommended to leave this option enabled for the majority of common units. If set to <code>no</code>, this option does not disable all implicit dependencies, just non-essential ones.</dl>
<p> <i>CollectMode=</i></p>
<dl>
<dd>Tweaks the &quot;garbage collection&quot; algorithm for this unit. Takes one of <code>inactive</code> or <code>inactive-or-failed</code>. If set to <code>inactive</code> the unit will be unloaded if it is in the <code>inactive</code> state and is not referenced by clients, jobs or other units &#8212; however it is not unloaded if it is in the <code>failed</code> state. In <code>failed</code> mode, failed units are not unloaded until the user invoked <code>systemctl reset-failed</code> on them to reset the <code>failed</code> state, or an equivalent command. This behaviour is altered if this option is set to <code>inactive-or-failed</code>: in this case the unit is unloaded even if the unit is in a <code>failed</code> state, and thus an explicitly resetting of the <code>failed</code> state is not necessary. Note that if this mode is used unit results (such as exit codes, exit signals, consumed resources, &#8230;) are flushed out immediately after the unit completed, except for what is stored in the logging subsystem. Defaults to <code>inactive</code>.</dl>
<p> <i>FailureAction=</i>, <i>SuccessAction=</i></p>
<dl>
<dd>Configure the action to take when the unit stops and enters a failed state or inactive state. Takes one of <code>none</code>, <code>reboot</code>, <code>reboot-force</code>, <code>reboot-immediate</code>, <code>poweroff</code>, <code>poweroff-force</code>, <code>poweroff-immediate</code>, <code>exit</code>, and <code>exit-force</code>. In system mode, all options are allowed. In user mode, only <code>none</code>, <code>exit</code>, and <code>exit-force</code> are allowed. Both options default to <code>none</code>. </p>
<p> If <code>none</code> is set, no action will be triggered. <code>reboot</code> causes a reboot following the normal shutdown procedure (i.e. equivalent to <code>systemctl reboot</code>). <code>reboot-force</code> causes a forced reboot which will terminate all processes forcibly but should cause no dirty file systems on reboot (i.e. equivalent to <code>systemctl reboot -f</code>) and <code>reboot-immediate</code> causes immediate execution of the <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2) system call, which might result in data loss (i.e. equivalent to <code>systemctl reboot -ff</code>). Similarly, <code>poweroff</code>, <code>poweroff-force</code>, <code>poweroff-immediate</code> have the effect of powering down the system with similar semantics. <code>exit</code> causes the manager to exit following the normal shutdown procedure, and <code>exit-force</code> causes it terminate without shutting down services. When <code>exit</code> or <code>exit-force</code> is used by default the exit status of the main process of the unit (if this applies) is returned from the service manager. However, this may be overridden with <i>FailureActionExitStatus=</i>/<i>SuccessActionExitStatus=</i>, see below.</dl>
<p> <i>FailureActionExitStatus=</i>, <i>SuccessActionExitStatus=</i></p>
<dl>
<dd>Controls the exit status to propagate back to an invoking container manager (in case of a system service) or service manager (in case of a user manager) when the <i>FailureAction=</i>/<i>SuccessAction=</i> are set to <code>exit</code> or <code>exit-force</code> and the action is triggered. By default the exit status of the main process of the triggering unit (if this applies) is propagated. Takes a value in the range 0&#8230;255 or the empty string to request default behaviour.</dl>
<p> <i>JobTimeoutSec=</i>, <i>JobRunningTimeoutSec=</i></p>
<dl>
<dd><i>JobTimeoutSec=</i> specifies a timeout for the whole job that starts running when the job is queued. <i>JobRunningTimeoutSec=</i> specifies a timeout that starts running when the queued job is actually started. If either limit is reached, the job will be cancelled, the unit however will not change state or even enter the &quot;failed&quot; mode. </p>
<p> Both settings take a time span with the default unit of seconds, but other units may be specified, see <code><a href="/docs/linux/man/5-systemd-time/">systemd.time</a></code>(5). The default is &quot;infinity&quot; (job timeouts disabled), except for device units where <i>JobRunningTimeoutSec=</i> defaults to <i>DefaultTimeoutStartSec=</i>. </p>
<p> Note: these timeouts are independent from any unit-specific timeouts (for example, the timeout set with <i>TimeoutStartSec=</i> in service units). The job timeout has no effect on the unit itself. Or in other words: unit-specific timeouts are useful to abort unit state changes, and revert them. The job timeout set with this option however is useful to abort only the job waiting for the unit state to change.</dl>
<p> <i>JobTimeoutAction=</i>, <i>JobTimeoutRebootArgument=</i></p>
<dl>
<dd><i>JobTimeoutAction=</i> optionally configures an additional action to take when the timeout is hit, see description of <i>JobTimeoutSec=</i> and <i>JobRunningTimeoutSec=</i> above. It takes the same values as <i>StartLimitAction=</i>. Defaults to <code>none</code>. </p>
<p> <i>JobTimeoutRebootArgument=</i> configures an optional reboot string to pass to the <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2) system call.</dl>
<p> <i>StartLimitIntervalSec=</i><i>interval</i>, <i>StartLimitBurst=</i><i>burst</i></p>
<dl>
<dd>Configure unit start rate limiting. Units which are started more than <i>burst</i> times within an <i>interval</i> time span are not permitted to start any more. Use <i>StartLimitIntervalSec=</i> to configure the checking interval and <i>StartLimitBurst=</i> to configure how many starts per interval are allowed. </p>
<p> <i>interval</i> is a time span with the default unit of seconds, but other units may be specified, see <code><a href="/docs/linux/man/5-systemd-time/">systemd.time</a></code>(5). Defaults to <i>DefaultStartLimitIntervalSec=</i> in manager configuration file, and may be set to 0 to disable any kind of rate limiting. <i>burst</i> is a number and defaults to <i>DefaultStartLimitBurst=</i> in manager configuration file. </p>
<p> These configuration options are particularly useful in conjunction with the service setting <i>Restart=</i> (see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5)); however, they apply to all kinds of starts (including manual), not just those triggered by the <i>Restart=</i> logic. </p>
<p> Note that units which are configured for <i>Restart=</i>, and which reach the start limit are not attempted to be restarted anymore; however, they may still be restarted manually or from a timer or socket at a later point, after the <i>interval</i> has passed. From that point on, the restart logic is activated again. <code>systemctl reset-failed</code> will cause the restart rate counter for a service to be flushed, which is useful if the administrator wants to manually start a unit and the start limit interferes with that. Rate-limiting is enforced after any unit condition checks are executed, and hence unit activations with failing conditions do not count towards the rate limit. </p>
<p> When a unit is unloaded due to the garbage collection logic (see above) its rate limit counters are flushed out too. This means that configuring start rate limiting for a unit that is not referenced continuously has no effect. </p>
<p> This setting does not apply to slice, target, device, and scope units, since they are unit types whose activation may either never fail, or may succeed only a single time.</dl>
<p> <i>StartLimitAction=</i></p>
<dl>
<dd>Configure an additional action to take if the rate limit configured with <i>StartLimitIntervalSec=</i> and <i>StartLimitBurst=</i> is hit. Takes the same values as the <i>FailureAction=</i>/<i>SuccessAction=</i> settings. If <code>none</code> is set, hitting the rate limit will trigger no action except that the start will not be permitted. Defaults to <code>none</code>.</dl>
<p> <i>RebootArgument=</i></p>
<dl>
<dd>Configure the optional argument for the <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2) system call if <i>StartLimitAction=</i> or <i>FailureAction=</i> is a reboot action. This works just like the optional argument to <code>systemctl reboot</code> command.</dl>
<p> <i>SourcePath=</i></p>
<dl>
<dd>A path to a configuration file this unit has been generated from. This is primarily useful for implementation of generator tools that convert configuration from an external configuration file format into native unit files. This functionality should not be used in normal units.</dl>
<h3>Conditions and Asserts</h3>
<p>Unit files may also include a number of <i>Condition&#8230;=</i> and <i>Assert&#8230;=</i> settings. Before the unit is started, systemd will verify that the specified conditions and asserts are true. If not, the starting of the unit will be (mostly silently) skipped (in case of conditions), or aborted with an error message (in case of asserts). Failing conditions or asserts will not result in the unit being moved into the &quot;failed&quot; state. The conditions and asserts are checked at the time the queued start job is to be executed. The ordering dependencies are still respected, so other units are still pulled in and ordered as if this unit was successfully activated, and the conditions and asserts are executed the precise moment the unit would normally start and thus can validate system state after the units ordered before completed initialization. Use condition expressions for skipping units that do not apply to the local system, for example because the kernel or runtime environment doesn&#8217;t require their functionality. </p>
<p> If multiple conditions are specified, the unit will be executed if all of them apply (i.e. a logical AND is applied). Condition checks can use a pipe symbol (&quot;|&quot;) after the equals sign (&quot;Condition&#8230;=|&#8230;&quot;), which causes the condition to become a <i>triggering</i> condition. If at least one triggering condition is defined for a unit, then the unit will be started if at least one of the triggering conditions of the unit applies and all of the regular (i.e. non-triggering) conditions apply. If you prefix an argument with the pipe symbol and an exclamation mark, the pipe symbol must be passed first, the exclamation second. If any of these options is assigned the empty string, the list of conditions is reset completely, all previous condition settings (of any kind) will have no effect. </p>
<p> The <i>AssertArchitecture=</i>, <i>AssertVirtualization=</i>, &#8230; options are similar to conditions but cause the start job to fail (instead of being skipped). The failed check is logged. Units with failed conditions are considered to be in a clean state and will be garbage collected if they are not referenced. This means that when queried, the condition failure may or may not show up in the state of the unit. </p>
<p> Note that neither assertion nor condition expressions result in unit state changes. Also note that both are checked at the time the job is to be executed, i.e. long after depending jobs and it itself were queued. Thus, neither condition nor assertion expressions are suitable for conditionalizing unit dependencies. </p>
<p> The <code>condition</code> verb of <code><a href="/docs/linux/man/1-systemd-analyze/">systemd-analyze</a></code>(1) can be used to test condition and assert expressions. </p>
<p> Except for <i>ConditionPathIsSymbolicLink=</i>, all path checks follow symlinks. </p>
<p> <i>ConditionArchitecture=</i></p>
<dl>
<dd>Check whether the system is running on a specific architecture. Takes one of &quot;x86&quot;, &quot;x86-64&quot;, &quot;ppc&quot;, &quot;ppc-le&quot;, &quot;ppc64&quot;, &quot;ppc64-le&quot;, &quot;ia64&quot;, &quot;parisc&quot;, &quot;parisc64&quot;, &quot;s390&quot;, &quot;s390x&quot;, &quot;sparc&quot;, &quot;sparc64&quot;, &quot;mips&quot;, &quot;mips-le&quot;, &quot;mips64&quot;, &quot;mips64-le&quot;, &quot;alpha&quot;, &quot;arm&quot;, &quot;arm-be&quot;, &quot;arm64&quot;, &quot;arm64-be&quot;, &quot;sh&quot;, &quot;sh64&quot;, &quot;m68k&quot;, &quot;tilegx&quot;, &quot;cris&quot;, &quot;arc&quot;, &quot;arc-be&quot;, or &quot;native&quot;. </p>
<p> The architecture is determined from the information returned by <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2) and is thus subject to <code><a href="/docs/linux/man/2-personality/">personality</a></code>(2). Note that a <i>Personality=</i> setting in the same unit file has no effect on this condition. A special architecture name &quot;native&quot; is mapped to the architecture the system manager itself is compiled for. The test may be negated by prepending an exclamation mark.</dl>
<p> <i>ConditionFirmware=</i></p>
<dl>
<dd>Check whether the system&#8217;s firmware is of a certain type. Possible values are: &quot;uefi&quot; (for systems with EFI), &quot;device-tree&quot; (for systems with a device tree) and &quot;device-tree-compatible(xyz)&quot; (for systems with a device tree that is compatible to &quot;xyz&quot;).</dl>
<p> <i>ConditionVirtualization=</i></p>
<dl>
<dd>Check whether the system is executed in a virtualized environment and optionally test whether it is a specific implementation. Takes either boolean value to check if being executed in any virtualized environment, or one of &quot;vm&quot; and &quot;container&quot; to test against a generic type of virtualization solution, or one of &quot;qemu&quot;, &quot;kvm&quot;, &quot;amazon&quot;, &quot;zvm&quot;, &quot;vmware&quot;, &quot;microsoft&quot;, &quot;oracle&quot;, &quot;powervm&quot;, &quot;xen&quot;, &quot;bochs&quot;, &quot;uml&quot;, &quot;bhyve&quot;, &quot;qnx&quot;, &quot;openvz&quot;, &quot;lxc&quot;, &quot;lxc-libvirt&quot;, &quot;systemd-nspawn&quot;, &quot;docker&quot;, &quot;podman&quot;, &quot;rkt&quot;, &quot;wsl&quot;, &quot;proot&quot;, &quot;pouch&quot;, &quot;acrn&quot; to test against a specific implementation, or &quot;private-users&quot; to check whether we are running in a user namespace. See <code><a href="/docs/linux/man/1-systemd-detect-virt/">systemd-detect-virt</a></code>(1) for a full list of known virtualization technologies and their identifiers. If multiple virtualization technologies are nested, only the innermost is considered. The test may be negated by prepending an exclamation mark.</dl>
<p> <i>ConditionHost=</i></p>
<dl>
<dd><i>ConditionHost=</i> may be used to match against the hostname or machine ID of the host. This either takes a hostname string (optionally with shell style globs) which is tested against the locally set hostname as returned by <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2), or a machine ID formatted as string (see <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5)). The test may be negated by prepending an exclamation mark.</dl>
<p> <i>ConditionKernelCommandLine=</i></p>
<dl>
<dd><i>ConditionKernelCommandLine=</i> may be used to check whether a specific kernel command line option is set (or if prefixed with the exclamation mark &#8212; unset). The argument must either be a single word, or an assignment (i.e. two words, separated by &quot;=&quot;). In the former case the kernel command line is searched for the word appearing as is, or as left hand side of an assignment. In the latter case, the exact assignment is looked for with right and left hand side matching. This operates on the kernel command line communicated to userspace via /proc/cmdline, except when the service manager is invoked as payload of a container manager, in which case the command line of PID 1 is used instead (i.e. /proc/1/cmdline).</dl>
<p> <i>ConditionKernelVersion=</i></p>
<dl>
<dd><i>ConditionKernelVersion=</i> may be used to check whether the kernel version (as reported by <code>uname -r</code>) matches a certain expression (or if prefixed with the exclamation mark does not match it). The argument must be a list of (potentially quoted) expressions. For each of the expressions, if it starts with one of &quot;&lt;&quot;, &quot;&lt;=&quot;, &quot;=&quot;, &quot;!=&quot;, &quot;&gt;=&quot;, &quot;&gt;&quot; a relative version comparison is done, otherwise the specified string is matched with shell-style globs. </p>
<p> Note that using the kernel version string is an unreliable way to determine which features are supported by a kernel, because of the widespread practice of backporting drivers, features, and fixes from newer upstream kernels into older versions provided by distributions. Hence, this check is inherently unportable and should not be used for units which may be used on different distributions.</dl>
<p> <i>ConditionEnvironment=</i></p>
<dl>
<dd><i>ConditionEnvironment=</i> may be used to check whether a specific environment variable is set (or if prefixed with the exclamation mark &#8212; unset) in the service manager&#8217;s environment block. The argument may be a single word, to check if the variable with this name is defined in the environment block, or an assignment (&quot;<i>name</i>=<i>value</i>&quot;), to check if the variable with this exact value is defined. Note that the environment block of the service manager itself is checked, i.e. not any variables defined with <i>Environment=</i> or <i>EnvironmentFile=</i>, as described above. This is particularly useful when the service manager runs inside a containerized environment or as per-user service manager, in order to check for variables passed in by the enclosing container manager or PAM.</dl>
<p> <i>ConditionSecurity=</i></p>
<dl>
<dd><i>ConditionSecurity=</i> may be used to check whether the given security technology is enabled on the system. Currently, the recognized values are &quot;selinux&quot;, &quot;apparmor&quot;, &quot;tomoyo&quot;, &quot;ima&quot;, &quot;smack&quot;, &quot;audit&quot;, &quot;uefi-secureboot&quot; and &quot;tpm2&quot;. The test may be negated by prepending an exclamation mark.</dl>
<p> <i>ConditionCapability=</i></p>
<dl>
<dd>Check whether the given capability exists in the capability bounding set of the service manager (i.e. this does not check whether capability is actually available in the permitted or effective sets, see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for details). Pass a capability name such as &quot;CAP_MKNOD&quot;, possibly prefixed with an exclamation mark to negate the check.</dl>
<p> <i>ConditionACPower=</i></p>
<dl>
<dd>Check whether the system has AC power, or is exclusively battery powered at the time of activation of the unit. This takes a boolean argument. If set to &quot;true&quot;, the condition will hold only if at least one AC connector of the system is connected to a power source, or if no AC connectors are known. Conversely, if set to &quot;false&quot;, the condition will hold only if there is at least one AC connector known and all AC connectors are disconnected from a power source.</dl>
<p> <i>ConditionNeedsUpdate=</i></p>
<dl>
<dd>Takes one of /var/ or /etc/ as argument, possibly prefixed with a &quot;!&quot; (to invert the condition). This condition may be used to conditionalize units on whether the specified directory requires an update because /usr/&#8217;s modification time is newer than the stamp file .updated in the specified directory. This is useful to implement offline updates of the vendor operating system resources in /usr/ that require updating of /etc/ or /var/ on the next following boot. Units making use of this condition should order themselves before <code><a href="/docs/linux/man/8-systemd-update-done-service/">systemd-update-done.service</a></code>(8), to make sure they run before the stamp file&#8217;s modification time gets reset indicating a completed update. </p>
<p> If the <i>systemd.condition-needs-update=</i> option is specified on the kernel command line (taking a boolean), it will override the result of this condition check, taking precedence over any file modification time checks. If the kernel command line option is used, systemd-update-done.service will not have immediate effect on any following <i>ConditionNeedsUpdate=</i> checks, until the system is rebooted where the kernel command line option is not specified anymore. </p>
<p> Note that to make this scheme effective, the timestamp of /usr/ should be explicitly updated after its contents are modified. The kernel will automatically update modification timestamp on a directory only when immediate children of a directory are modified; an modification of nested files will not automatically result in mtime of /usr/ being updated. </p>
<p> Also note that if the update method includes a call to execute appropriate post-update steps itself, it should not touch the timestamp of /usr/. In a typical distribution packaging scheme, packages will do any required update steps as part of the installation or upgrade, to make package contents immediately usable. <i>ConditionNeedsUpdate=</i> should be used with other update mechanisms where such an immediate update does not happen.</dl>
<p> <i>ConditionFirstBoot=</i></p>
<dl>
<dd>Takes a boolean argument. This condition may be used to conditionalize units on whether the system is booting up for the first time. This roughly means that /etc/ is unpopulated (for details, see &quot;First Boot Semantics&quot; in <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5)). This may be used to populate /etc/ on the first boot after factory reset, or when a new system instance boots up for the first time. </p>
<p> For robustness, units with <i>ConditionFirstBoot=yes</i> should order themselves before first-boot-complete.target and pull in this passive target with <i>Wants=</i>. This ensures that in a case of an aborted first boot, these units will be re-run during the next system startup. </p>
<p> If the <i>systemd.condition-first-boot=</i> option is specified on the kernel command line (taking a boolean), it will override the result of this condition check, taking precedence over /etc/machine-id existence checks.</dl>
<p> <i>ConditionPathExists=</i></p>
<dl>
<dd>Check for the existence of a file. If the specified absolute path name does not exist, the condition will fail. If the absolute path name passed to <i>ConditionPathExists=</i> is prefixed with an exclamation mark (&quot;!&quot;), the test is negated, and the unit is only started if the path does not exist.</dl>
<p> <i>ConditionPathExistsGlob=</i></p>
<dl>
<dd><i>ConditionPathExistsGlob=</i> is similar to <i>ConditionPathExists=</i>, but checks for the existence of at least one file or directory matching the specified globbing pattern.</dl>
<p> <i>ConditionPathIsDirectory=</i></p>
<dl>
<dd><i>ConditionPathIsDirectory=</i> is similar to <i>ConditionPathExists=</i> but verifies that a certain path exists and is a directory.</dl>
<p> <i>ConditionPathIsSymbolicLink=</i></p>
<dl>
<dd><i>ConditionPathIsSymbolicLink=</i> is similar to <i>ConditionPathExists=</i> but verifies that a certain path exists and is a symbolic link.</dl>
<p> <i>ConditionPathIsMountPoint=</i></p>
<dl>
<dd><i>ConditionPathIsMountPoint=</i> is similar to <i>ConditionPathExists=</i> but verifies that a certain path exists and is a mount point.</dl>
<p> <i>ConditionPathIsReadWrite=</i></p>
<dl>
<dd><i>ConditionPathIsReadWrite=</i> is similar to <i>ConditionPathExists=</i> but verifies that the underlying file system is readable and writable (i.e. not mounted read-only).</dl>
<p> <i>ConditionPathIsEncrypted=</i></p>
<dl>
<dd><i>ConditionPathIsEncrypted=</i> is similar to <i>ConditionPathExists=</i> but verifies that the underlying file system&#8217;s backing block device is encrypted using dm-crypt/LUKS. Note that this check does not cover ext4 per-directory encryption, and only detects block level encryption. Moreover, if the specified path resides on a file system on top of a loopback block device, only encryption above the loopback device is detected. It is not detected whether the file system backing the loopback block device is encrypted.</dl>
<p> <i>ConditionDirectoryNotEmpty=</i></p>
<dl>
<dd><i>ConditionDirectoryNotEmpty=</i> is similar to <i>ConditionPathExists=</i> but verifies that a certain path exists and is a non-empty directory.</dl>
<p> <i>ConditionFileNotEmpty=</i></p>
<dl>
<dd><i>ConditionFileNotEmpty=</i> is similar to <i>ConditionPathExists=</i> but verifies that a certain path exists and refers to a regular file with a non-zero size.</dl>
<p> <i>ConditionFileIsExecutable=</i></p>
<dl>
<dd><i>ConditionFileIsExecutable=</i> is similar to <i>ConditionPathExists=</i> but verifies that a certain path exists, is a regular file, and marked executable.</dl>
<p> <i>ConditionUser=</i></p>
<dl>
<dd><i>ConditionUser=</i> takes a numeric &quot;UID&quot;, a UNIX user name, or the special value &quot;@system&quot;. This condition may be used to check whether the service manager is running as the given user. The special value &quot;@system&quot; can be used to check if the user id is within the system user range. This option is not useful for system services, as the system manager exclusively runs as the root user, and thus the test result is constant.</dl>
<p> <i>ConditionGroup=</i></p>
<dl>
<dd><i>ConditionGroup=</i> is similar to <i>ConditionUser=</i> but verifies that the service manager&#8217;s real or effective group, or any of its auxiliary groups, match the specified group or GID. This setting does not support the special value &quot;@system&quot;.</dl>
<p> <i>ConditionControlGroupController=</i></p>
<dl>
<dd>Check whether given cgroup controllers (e.g. &quot;cpu&quot;) are available for use on the system or whether the legacy v1 cgroup or the modern v2 cgroup hierarchy is used. </p>
<p> Multiple controllers may be passed with a space separating them; in this case the condition will only pass if all listed controllers are available for use. Controllers unknown to systemd are ignored. Valid controllers are &quot;cpu&quot;, &quot;cpuacct&quot;, &quot;io&quot;, &quot;blkio&quot;, &quot;memory&quot;, &quot;devices&quot;, and &quot;pids&quot;. Even if available in the kernel, a particular controller may not be available if it was disabled on the kernel command line with <i>cgroup_disable=controller</i>. </p>
<p> Alternatively, two special strings &quot;v1&quot; and &quot;v2&quot; may be specified (without any controller names). &quot;v2&quot; will pass if the unified v2 cgroup hierarchy is used, and &quot;v1&quot; will pass if the legacy v1 hierarchy or the hybrid hierarchy are used (see the discussion of <i>systemd.unified_cgroup_hierarchy</i> and <i>systemd.legacy_systemd_cgroup_controller</i> in <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for more information).</dl>
<p> <i>ConditionMemory=</i></p>
<dl>
<dd>Verify that the specified amount of system memory is available to the current system. Takes a memory size in bytes as argument, optionally prefixed with a comparison operator &quot;&lt;&quot;, &quot;&lt;=&quot;, &quot;=&quot;, &quot;!=&quot;, &quot;&gt;=&quot;, &quot;&gt;&quot;. On bare-metal systems compares the amount of physical memory in the system with the specified size, adhering to the specified comparison operator. In containers compares the amount of memory assigned to the container instead.</dl>
<p> <i>ConditionCPUs=</i></p>
<dl>
<dd>Verify that the specified number of CPUs is available to the current system. Takes a number of CPUs as argument, optionally prefixed with a comparison operator &quot;&lt;&quot;, &quot;&lt;=&quot;, &quot;=&quot;, &quot;!=&quot;, &quot;&gt;=&quot;, &quot;&gt;&quot;. Compares the number of CPUs in the CPU affinity mask configured of the service manager itself with the specified number, adhering to the specified comparison operator. On physical systems the number of CPUs in the affinity mask of the service manager usually matches the number of physical CPUs, but in special and virtual environments might differ. In particular, in containers the affinity mask usually matches the number of CPUs assigned to the container and not the physically available ones.</dl>
<p> <i>ConditionCPUFeature=</i></p>
<dl>
<dd>Verify that a given CPU feature is available via the &quot;CPUID&quot; instruction. This condition only does something on i386 and x86-64 processors. On other processors it is assumed that the CPU does not support the given feature. It checks the leaves &quot;1&quot;, &quot;7&quot;, &quot;0x80000001&quot;, and &quot;0x80000007&quot;. Valid values are: &quot;fpu&quot;, &quot;vme&quot;, &quot;de&quot;, &quot;pse&quot;, &quot;tsc&quot;, &quot;msr&quot;, &quot;pae&quot;, &quot;mce&quot;, &quot;cx8&quot;, &quot;apic&quot;, &quot;sep&quot;, &quot;mtrr&quot;, &quot;pge&quot;, &quot;mca&quot;, &quot;cmov&quot;, &quot;pat&quot;, &quot;pse36&quot;, &quot;clflush&quot;, &quot;mmx&quot;, &quot;fxsr&quot;, &quot;sse&quot;, &quot;sse2&quot;, &quot;ht&quot;, &quot;pni&quot;, &quot;pclmul&quot;, &quot;monitor&quot;, &quot;ssse3&quot;, &quot;fma3&quot;, &quot;cx16&quot;, &quot;sse4_1&quot;, &quot;sse4_2&quot;, &quot;movbe&quot;, &quot;popcnt&quot;, &quot;aes&quot;, &quot;xsave&quot;, &quot;osxsave&quot;, &quot;avx&quot;, &quot;f16c&quot;, &quot;rdrand&quot;, &quot;bmi1&quot;, &quot;avx2&quot;, &quot;bmi2&quot;, &quot;rdseed&quot;, &quot;adx&quot;, &quot;sha_ni&quot;, &quot;syscall&quot;, &quot;rdtscp&quot;, &quot;lm&quot;, &quot;lahf_lm&quot;, &quot;abm&quot;, &quot;constant_tsc&quot;.</dl>
<p> <i>ConditionOSRelease=</i></p>
<dl>
<dd>Verify that a specific &quot;key=value&quot; pair is set in the host&#8217;s <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5). </p>
<p> Other than exact matching with &quot;=&quot;, and &quot;!=&quot;, relative comparisons are supported for versioned parameters (e.g. &quot;VERSION_ID&quot;). The comparator can be one of &quot;&lt;&quot;, &quot;&lt;=&quot;, &quot;=&quot;, &quot;!=&quot;, &quot;&gt;=&quot; and &quot;&gt;&quot;.</dl>
<p> <i>AssertArchitecture=</i>, <i>AssertVirtualization=</i>, <i>AssertHost=</i>, <i>AssertKernelCommandLine=</i>, <i>AssertKernelVersion=</i>, <i>AssertEnvironment=</i>, <i>AssertSecurity=</i>, <i>AssertCapability=</i>, <i>AssertACPower=</i>, <i>AssertNeedsUpdate=</i>, <i>AssertFirstBoot=</i>, <i>AssertPathExists=</i>, <i>AssertPathExistsGlob=</i>, <i>AssertPathIsDirectory=</i>, <i>AssertPathIsSymbolicLink=</i>, <i>AssertPathIsMountPoint=</i>, <i>AssertPathIsReadWrite=</i>, <i>AssertPathIsEncrypted=</i>, <i>AssertDirectoryNotEmpty=</i>, <i>AssertFileNotEmpty=</i>, <i>AssertFileIsExecutable=</i>, <i>AssertUser=</i>, <i>AssertGroup=</i>, <i>AssertControlGroupController=</i>, <i>AssertMemory=</i>, <i>AssertCPUs=</i>, <i>AssertOSRelease=</i></p>
<dl>
<dd>Similar to the <i>ConditionArchitecture=</i>, <i>ConditionVirtualization=</i>, &#8230;, condition settings described above, these settings add assertion checks to the start-up of the unit. However, unlike the conditions settings, any assertion setting that is not met results in failure of the start job (which means this is logged loudly). Note that hitting a configured assertion does not cause the unit to enter the &quot;failed&quot; state (or in fact result in any state change of the unit), it affects only the job queued for it. Use assertion expressions for units that cannot operate when specific requirements are not met, and when this is something the administrator or user should look into.</dl>
<h2>Mapping Of Unit Properties To Their Inverses</h2>
<p>Unit settings that create a relationship with a second unit usually show up in properties of both units, for example in <code>systemctl show</code> output. In some cases the name of the property is the same as the name of the configuration setting, but not always. This table lists the properties that are shown on two units which are connected through some dependency, and shows which property on &quot;source&quot; unit corresponds to which property on the &quot;target&quot; unit. </p>
<p> <code>Table 3.&nbsp; Forward and reverse unit properties</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> &quot;Forward&quot; property </code></td>
<td><code> &quot;Reverse&quot; property </code></td>
<td COLSPAN=2><code> Where used </code>
</td>
</tr>
<tr VALIGN=top>
<td> <i>Before=</i> </td>
<td> <i>After=</i> </td>
<td VALIGN=center COLSPAN=2 ROWSPAN=2> [Unit] section
</td>
</tr>
<tr VALIGN=top>
<td> <i>After=</i> </td>
<td> <i>Before=</i> </td>
</tr>
<tr VALIGN=top>
<td> <i>Requires=</i> </td>
<td> <i>RequiredBy=</i> </td>
<td> [Unit] section </td>
<td> [Install] section
</td>
</tr>
<tr VALIGN=top>
<td> <i>Wants=</i> </td>
<td> <i>WantedBy=</i> </td>
<td> [Unit] section </td>
<td> [Install] section
</td>
</tr>
<tr VALIGN=top>
<td> <i>PartOf=</i> </td>
<td> <i>ConsistsOf=</i> </td>
<td> [Unit] section </td>
<td> an automatic property
</td>
</tr>
<tr VALIGN=top>
<td> <i>BindsTo=</i> </td>
<td> <i>BoundBy=</i> </td>
<td> [Unit] section </td>
<td> an automatic property
</td>
</tr>
<tr VALIGN=top>
<td> <i>Requisite=</i> </td>
<td> <i>RequisiteOf=</i> </td>
<td> [Unit] section </td>
<td> an automatic property
</td>
</tr>
<tr VALIGN=top>
<td> <i>Triggers=</i> </td>
<td> <i>TriggeredBy=</i> </td>
<td COLSPAN=2> Automatic properties, see notes below
</td>
</tr>
<tr VALIGN=top>
<td> <i>Conflicts=</i> </td>
<td> <i>ConflictedBy=</i> </td>
<td> [Unit] section </td>
<td> an automatic property
</td>
</tr>
<tr VALIGN=top>
<td> <i>PropagatesReloadTo=</i> </td>
<td> <i>ReloadPropagatedFrom=</i> </td>
<td VALIGN=center COLSPAN=2 ROWSPAN=2> [Unit] section
</td>
</tr>
<tr VALIGN=top>
<td> <i>ReloadPropagatedFrom=</i> </td>
<td> <i>PropagatesReloadTo=</i> </td>
</tr>
<tr VALIGN=top>
<td> <i>Following=</i> </td>
<td> n/a </td>
<td> An automatic property </td>
<td> &nbsp;
</td>
</tr>
</table>
<p> Note: <i>WantedBy=</i> and <i>RequiredBy=</i> are used in the [Install] section to create symlinks in .wants/ and .requires/ directories. They cannot be used directly as a unit configuration setting. </p>
<p> Note: <i>ConsistsOf=</i>, <i>BoundBy=</i>, <i>RequisiteOf=</i>, <i>ConflictedBy=</i> are created implicitly along with their reverses and cannot be specified directly. </p>
<p> Note: <i>Triggers=</i> is created implicitly between a socket, path unit, or an automount unit, and the unit they activate. By default a unit with the same name is triggered, but this can be overridden using <i>Sockets=</i>, <i>Service=</i>, and <i>Unit=</i> settings. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-path/">systemd.path</a></code>(5), and <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5) for details. <i>TriggeredBy=</i> is created implicitly on the triggered unit. </p>
<p> Note: <i>Following=</i> is used to group device aliases and points to the &quot;primary&quot; device unit that systemd is using to track device state, usually corresponding to a sysfs path. It does not show up in the &quot;target&quot; unit.</p>
<h2>[Install] Section Options</h2>
<p>Unit files may include an [Install] section, which carries installation information for the unit. This section is not interpreted by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) during runtime; it is used by the <code>enable</code> and <code>disable</code> commands of the <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) tool during installation of a unit. </p>
<p> <i>Alias=</i></p>
<dl>
<dd>A space-separated list of additional names this unit shall be installed under. The names listed here must have the same suffix (i.e. type) as the unit filename. This option may be specified more than once, in which case all listed names are used. At installation time, <code>systemctl enable</code> will create symlinks from these names to the unit filename. Note that not all unit types support such alias names, and this setting is not supported for them. Specifically, mount, slice, swap, and automount units do not support aliasing.</dl>
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
<p> The following specifiers are interpreted in the Install section: %a, %b, %B, %g, %G, %H, %i, %j, %l, %m, %n, %N, %o, %p, %u, %U, %v, %w, %W, %%. For their meaning see the next section.</p>
<h2>Specifiers</h2>
<p>Many settings resolve specifiers which may be used to write generic unit files referring to runtime or unit parameters that are replaced when the unit files are loaded. Specifiers must be known and resolvable for the setting to be valid. The following specifiers are understood: </p>
<p> <code>Table 4. Specifiers available in unit files</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Specifier </code></td>
<td><code> Meaning </code></td>
<td><code> Details </code>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%a&quot; </td>
<td> Architecture </td>
<td> A short string identifying the architecture of the local system. A string such as <code>x86</code>, <code>x86-64</code> or <code>arm64</code>. See the architectures defined for <i>ConditionArchitecture=</i> above for a full list.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%A&quot; </td>
<td> Operating system image version </td>
<td> The operating system image version identifier of the running system, as read from the <i>IMAGE_VERSION=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%b&quot; </td>
<td> Boot ID </td>
<td> The boot ID of the running system, formatted as string. See <code><a href="/docs/linux/man/4-random/">random</a></code>(4) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%B&quot; </td>
<td> Operating system build ID </td>
<td> The operating system build identifier of the running system, as read from the <i>BUILD_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%C&quot; </td>
<td> Cache directory root </td>
<td> This is either /var/cache (for the system manager) or the path &quot;$XDG_CACHE_HOME&quot; resolves to (for user managers).
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%E&quot; </td>
<td> Configuration directory root </td>
<td> This is either /etc/ (for the system manager) or the path &quot;$XDG_CONFIG_HOME&quot; resolves to (for user managers).
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%f&quot; </td>
<td> Unescaped filename </td>
<td> This is either the unescaped instance name (if applicable) with / prepended (if applicable), or the unescaped prefix name prepended with /. This implements unescaping according to the rules for escaping absolute file system paths discussed above.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%g&quot; </td>
<td> User group </td>
<td> This is the name of the group running the service manager instance. In case of the system manager this resolves to &quot;root&quot;.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%G&quot; </td>
<td> User GID </td>
<td> This is the numeric GID of the user running the service manager instance. In case of the system manager this resolves to &quot;0&quot;.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%h&quot; </td>
<td> User home directory </td>
<td> This is the home directory of the <i>user running the service manager instance</i>. In case of the system manager this resolves to &quot;/root&quot;. </p>
<p> Note that this setting is <i>not</i> influenced by the <i>User=</i> setting configurable in the [Service] section of the service unit.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%H&quot; </td>
<td> Host name </td>
<td> The hostname of the running system at the point in time the unit configuration is loaded.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%i&quot; </td>
<td> Instance name </td>
<td> For instantiated units this is the string between the first &quot;@&quot; character and the type suffix. Empty for non-instantiated units.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%I&quot; </td>
<td> Unescaped instance name </td>
<td> Same as &quot;%i&quot;, but with escaping undone.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%j&quot; </td>
<td> Final component of the prefix </td>
<td> This is the string between the last &quot;-&quot; and the end of the prefix name. If there is no &quot;-&quot;, this is the same as &quot;%p&quot;.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%J&quot; </td>
<td> Unescaped final component of the prefix </td>
<td> Same as &quot;%j&quot;, but with escaping undone.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%l&quot; </td>
<td> Short host name </td>
<td> The hostname of the running system at the point in time the unit configuration is loaded, truncated at the first dot to remove any domain component.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%L&quot; </td>
<td> Log directory root </td>
<td> This is either /var/log (for the system manager) or the path &quot;$XDG_CONFIG_HOME&quot; resolves to with /log appended (for user managers).
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%m&quot; </td>
<td> Machine ID </td>
<td> The machine ID of the running system, formatted as string. See <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%M&quot; </td>
<td> Operating system image identifier </td>
<td> The operating system image identifier of the running system, as read from the <i>IMAGE_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%n&quot; </td>
<td> Full unit name </td>
<td> &nbsp;
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%N&quot; </td>
<td> Full unit name </td>
<td> Same as &quot;%n&quot;, but with the type suffix removed.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%o&quot; </td>
<td> Operating system ID </td>
<td> The operating system identifier of the running system, as read from the <i>ID=</i> field of /etc/os-release. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%p&quot; </td>
<td> Prefix name </td>
<td> For instantiated units, this refers to the string before the first &quot;@&quot; character of the unit name. For non-instantiated units, same as &quot;%N&quot;.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%P&quot; </td>
<td> Unescaped prefix name </td>
<td> Same as &quot;%p&quot;, but with escaping undone.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%s&quot; </td>
<td> User shell </td>
<td> This is the shell of the user running the service manager instance. In case of the system manager this resolves to &quot;/bin/sh&quot;.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%S&quot; </td>
<td> State directory root </td>
<td> This is either /var/lib (for the system manager) or the path &quot;$XDG_CONFIG_HOME&quot; resolves to (for user managers).
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%t&quot; </td>
<td> Runtime directory root </td>
<td> This is either /run/ (for the system manager) or the path &quot;$XDG_RUNTIME_DIR&quot; resolves to (for user managers).
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%T&quot; </td>
<td> Directory for temporary files </td>
<td> This is either /tmp or the path &quot;$TMPDIR&quot;, &quot;$TEMP&quot; or &quot;$TMP&quot; are set to. (Note that the directory may be specified without a trailing slash.)
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%u&quot; </td>
<td> User name </td>
<td> This is the name of the <i>user running the service manager instance</i>. In case of the system manager this resolves to &quot;root&quot;. </p>
<p> Note that this setting is <i>not</i> influenced by the <i>User=</i> setting configurable in the [Service] section of the service unit.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%U&quot; </td>
<td> User UID </td>
<td> This is the numeric UID of the <i>user running the service manager instance</i>. In case of the system manager this resolves to &quot;0&quot;. </p>
<p> Note that this setting is <i>not</i> influenced by the <i>User=</i> setting configurable in the [Service] section of the service unit.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%v&quot; </td>
<td> Kernel release </td>
<td> Identical to <code>uname -r</code> output.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%V&quot; </td>
<td> Directory for larger and persistent temporary files </td>
<td> This is either /var/tmp or the path &quot;$TMPDIR&quot;, &quot;$TEMP&quot; or &quot;$TMP&quot; are set to. (Note that the directory may be specified without a trailing slash.)
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%w&quot; </td>
<td> Operating system version ID </td>
<td> The operating system version identifier of the running system, as read from the <i>VERSION_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%W&quot; </td>
<td> Operating system variant ID </td>
<td> The operating system variant identifier of the running system, as read from the <i>VARIANT_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%%&quot; </td>
<td> Single percent sign </td>
<td> Use &quot;%%&quot; in place of &quot;%&quot; to specify a single percent sign.
</td>
</tr>
</table>
<h2>Examples</h2>
<p><code>Example 1. Allowing units to be enabled</code> </p>
<p> The following snippet (highlighted) allows a unit (e.g. foo.service) to be enabled via <code>systemctl enable</code>: </p>
<dl>
<dd>
<pre>[Unit]
Description=Foo
[Service]
ExecStart=/usr/sbin/foo-daemon
<i>[Install]</i>
<i>WantedBy=multi-user.target</i></pre>
</dl>
<p> After running <code>systemctl enable</code>, a symlink /etc/systemd/system/multi-user.target.wants/foo.service linking to the actual unit will be created. It tells systemd to pull in the unit when starting multi-user.target. The inverse <code>systemctl disable</code> will remove that symlink again. </p>
<p> <code>Example 2. Overriding vendor settings</code> </p>
<p> There are two methods of overriding vendor settings in unit files: copying the unit file from /lib/systemd/system to /etc/systemd/system and modifying the chosen settings. Alternatively, one can create a directory named <i>unit</i>.d/ within /etc/systemd/system and place a drop-in file <i>name</i>.conf there that only changes the specific settings one is interested in. Note that multiple such drop-in files are read if present, processed in lexicographic order of their filename. </p>
<p> The advantage of the first method is that one easily overrides the complete unit, the vendor unit is not parsed at all anymore. It has the disadvantage that improvements to the unit file by the vendor are not automatically incorporated on updates. </p>
<p> The advantage of the second method is that one only overrides the settings one specifically wants, where updates to the unit by the vendor automatically apply. This has the disadvantage that some future updates by the vendor might be incompatible with the local changes. </p>
<p> This also applies for user instances of systemd, but with different locations for the unit files. See the section on unit load paths for further details. </p>
<p> Suppose there is a vendor-supplied unit /lib/systemd/system/httpd.service with the following contents: </p>
<dl>
<dd>
<pre>[Unit]
Description=Some HTTP server
After=remote-fs.target sqldb.service
Requires=sqldb.service
AssertPathExists=/srv/webserver
[Service]
Type=notify
ExecStart=/usr/sbin/some-fancy-httpd-server
Nice=5
[Install]
WantedBy=multi-user.target</pre>
</dl>
<p> Now one wants to change some settings as an administrator: firstly, in the local setup, /srv/webserver might not exist, because the HTTP server is configured to use /srv/www instead. Secondly, the local configuration makes the HTTP server also depend on a memory cache service, memcached.service, that should be pulled in (<i>Requires=</i>) and also be ordered appropriately (<i>After=</i>). Thirdly, in order to harden the service a bit more, the administrator would like to set the <i>PrivateTmp=</i> setting (see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details). And lastly, the administrator would like to reset the niceness of the service to its default value of 0. </p>
<p> The first possibility is to copy the unit file to /etc/systemd/system/httpd.service and change the chosen settings: </p>
<dl>
<dd>
<pre>[Unit]
Description=Some HTTP server
After=remote-fs.target sqldb.service <i>memcached.service</i>
Requires=sqldb.service <i>memcached.service</i>
AssertPathExists=<i>/srv/www</i>
[Service]
Type=notify
ExecStart=/usr/sbin/some-fancy-httpd-server
<i>Nice=0</i>
<i>PrivateTmp=yes</i>
[Install]
WantedBy=multi-user.target</pre>
</dl>
<p> Alternatively, the administrator could create a drop-in file /etc/systemd/system/httpd.service.d/local.conf with the following contents: </p>
<dl>
<dd>
<pre>[Unit]
After=memcached.service
Requires=memcached.service
# Reset all assertions and then re-add the condition we want
AssertPathExists=
AssertPathExists=/srv/www
[Service]
Nice=0
PrivateTmp=yes</pre>
</dl>
<p> Note that for drop-in files, if one wants to remove entries from a setting that is parsed as a list (and is not a dependency), such as <i>AssertPathExists=</i> (or e.g. <i>ExecStart=</i> in service units), one needs to first clear the list before re-adding all entries except the one that is to be removed. Dependencies (<i>After=</i>, etc.) cannot be reset to an empty list, so dependencies can only be added in drop-ins. If you want to remove dependencies, you have to override the entire unit. </p>
<p> <code>Example 3. Top level drop-ins with template units</code> </p>
<p> Top level per-type drop-ins can be used to change some aspect of all units of a particular type. For example by creating the /etc/systemd/system/service.d/ directory with a drop-in file, the contents of the drop-in file can be applied to all service units. We can take this further by having the top-level drop-in instantiate a secondary helper unit. Consider for example the following set of units and drop-in files where we install an <i>OnFailure=</i> dependency for all service units. </p>
<p> /etc/systemd/system/failure-handler [at] .service: </p>
<dl>
<dd>
<pre>[Unit]
Description=My failure handler for %i
[Service]
Type=oneshot
# Perform some special action for when %i exits unexpectedly.
ExecStart=/usr/sbin/myfailurehandler %i</pre>
</dl>
<p> We can then add an instance of failure-handler [at] .service as an <i>OnFailure=</i> dependency for all service units. </p>
<p> /etc/systemd/system/service.d/10-all.conf: </p>
<dl>
<dd>
<pre>[Unit]
OnFailure=failure-handler@%N.service</pre>
</dl>
<p> Now, after running <code>systemctl daemon-reload</code> all services will have acquired an <i>OnFailure=</i> dependency on failure-handler@%N.service. The template instance units will also have gained the dependency which results in the creation of a recursive dependency chain. We can break the chain by disabling the drop-in for the template instance units via a symlink to /dev/null: </p>
<dl>
<dd>
<pre><code>mkdir /etc/systemd/system/failure-handler [at] .service.d/</code>
<code>ln -s /dev/null /etc/systemd/system/failure-handler [at] .service.d/10-all.conf</code>
<code>systemctl daemon-reload</code></pre>
</dl>
<p> This ensures that if a failure-handler [at] .service instance fails it will not trigger an instance named failure-handler [at] failure-handler.service.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5), <code><a href="/docs/linux/man/5-systemd-path/">systemd.path</a></code>(5), <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5), <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7), <code><a href="/docs/linux/man/1-systemd-analyze/">systemd-analyze</a></code>(1), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/1-uname/">uname</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Interface Portability and Stability Promise</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/PORTABILITY_AND_STABILITY/">https://systemd.io/PORTABILITY_AND_STABILITY/</a></dl>
