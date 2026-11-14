---
title: "systemd(1)"
name: "systemd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd/"
description: "systemd, init – systemd system and service manager"
---

<h2 class="name">NAME</h2>
<p> systemd, init &#8211; systemd system and service manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/lib/systemd/systemd</code> [OPTIONS&#8230;]</p>
<dt> <code>init</code> [OPTIONS&#8230;] {COMMAND}</dl>
<h2>DESCRIPTION</h2>
<dd>systemd is a system and service manager for Linux operating systems. When run as first process on boot (as PID 1), it acts as init system that brings up and maintains userspace services. Separate instances are started for logged-in users to start their services. </p>
<p> <code>systemd</code> is usually not invoked directly by the user, but is installed as the /sbin/init symlink and started during early boot. The user manager instances are started automatically through the <code>user [at] .service</code>(5) service. </p>
<p> For compatibility with SysV, if the binary is called as <code>init</code> and is not the first process on the machine (PID is not 1), it will execute <code>telinit</code> and pass all command line arguments unmodified. That means <code>init</code> and <code>telinit</code> are mostly equivalent when invoked from normal login sessions. See <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) for more information. </p>
<p> When run as a system instance, systemd interprets the configuration file system.conf and the files in system.conf.d directories; when run as a user instance, systemd interprets the configuration file user.conf and the files in user.conf.d directories. See <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5) for more information.</p>
<h2>CONCEPTS</h2>
<p> systemd provides a dependency system between various entities called &quot;units&quot; of 11 different types. Units encapsulate various objects that are relevant for system boot-up and maintenance. The majority of units are configured in unit configuration files, whose syntax and basic set of options is described in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), however some are created automatically from other configuration files, dynamically from system state or programmatically at runtime. Units may be &quot;active&quot; (meaning started, bound, plugged in, &#8230;, depending on the unit type, see below), or &quot;inactive&quot; (meaning stopped, unbound, unplugged, &#8230;), as well as in the process of being activated or deactivated, i.e. between the two states (these states are called &quot;activating&quot;, &quot;deactivating&quot;). A special &quot;failed&quot; state is available as well, which is very similar to &quot;inactive&quot; and is entered when the service failed in some way (process returned error code on exit, or crashed, an operation timed out, or after too many restarts). If this state is entered, the cause will be logged, for later reference. Note that the various unit types may have a number of additional substates, which are mapped to the five generalized unit states described here. </p>
<p> The following unit types are available: </p>
<dl>
<dt>
<dd> 1. Service units, which start and control daemons and the processes they consist of. For details, see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5).</dl>
<dl>
<dt>
<dd> 2. Socket units, which encapsulate local IPC or network sockets in the system, useful for socket-based activation. For details about socket units, see <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), for details on socket-based activation and other forms of activation, see <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7).</dl>
<dl>
<dt>
<dd> 3. Target units are useful to group units, or provide well-known synchronization points during boot-up, see <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5).</dl>
<dl>
<dt>
<dd> 4. Device units expose kernel devices in systemd and may be used to implement device-based activation. For details, see <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5).</dl>
<dl>
<dt>
<dd> 5. Mount units control mount points in the file system, for details see <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5).</dl>
<dl>
<dt>
<dd> 6. Automount units provide automount capabilities, for on-demand mounting of file systems as well as parallelized boot-up. See <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5).</dl>
<dl>
<dt>
<dd> 7. Timer units are useful for triggering activation of other units based on timers. You may find details in <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5).</dl>
<dl>
<dt>
<dd> 8. Swap units are very similar to mount units and encapsulate memory swap partitions or files of the operating system. They are described in <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5).</dl>
<dl>
<dt>
<dd> 9. Path units may be used to activate other services when file system objects change or are modified. See <code><a href="/docs/linux/man/5-systemd-path/">systemd.path</a></code>(5).</dl>
<dl>
<dt>
<dd> 10. Slice units may be used to group units which manage system processes (such as service and scope units) in a hierarchical tree for resource management purposes. See <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5).</dl>
<dl>
<dt>
<dd> 11. Scope units are similar to service units, but manage foreign processes instead of starting them as well. See <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5).</dl>
<p> Units are named as their configuration files. Some units have special semantics. A detailed list is available in <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7). </p>
<p> systemd knows various kinds of dependencies, including positive and negative requirement dependencies (i.e. <i>Requires=</i> and <i>Conflicts=</i>) as well as ordering dependencies (<i>After=</i> and <i>Before=</i>). NB: ordering and requirement dependencies are orthogonal. If only a requirement dependency exists between two units (e.g. foo.service requires bar.service), but no ordering dependency (e.g. foo.service after bar.service) and both are requested to start, they will be started in parallel. It is a common pattern that both requirement and ordering dependencies are placed between two units. Also note that the majority of dependencies are implicitly created and maintained by systemd. In most cases, it should be unnecessary to declare additional dependencies manually, however it is possible to do this. </p>
<p> Application programs and units (via dependencies) may request state changes of units. In systemd, these requests are encapsulated as &#8216;jobs&#8217; and maintained in a job queue. Jobs may succeed or can fail, their execution is ordered based on the ordering dependencies of the units they have been scheduled for. </p>
<p> On boot systemd activates the target unit default.target whose job is to activate on-boot services and other on-boot units by pulling them in via dependencies. Usually, the unit name is just an alias (symlink) for either graphical.target (for fully-featured boots into the UI) or multi-user.target (for limited console-only boots for use in embedded or server environments, or similar; a subset of graphical.target). However, it is at the discretion of the administrator to configure it as an alias to any other target unit. See <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for details about these target units. </p>
<p> systemd only keeps a minimal set of units loaded into memory. Specifically, the only units that are kept loaded into memory are those for which at least one of the following conditions is true: </p>
<dl>
<dt>
<dd> 1. It is in an active, activating, deactivating or failed state (i.e. in any unit state except for &quot;inactive&quot;)</dl>
<dl>
<dt>
<dd> 2. It has a job queued for it</dl>
<dl>
<dt>
<dd> 3. It is a dependency of at least one other unit that is loaded into memory</dl>
<dl>
<dt>
<dd> 4. It has some form of resource still allocated (e.g. a service unit that is inactive but for which a process is still lingering that ignored the request to be terminated)</dl>
<dl>
<dt>
<dd> 5. It has been pinned into memory programmatically by a D-Bus call</dl>
<p> systemd will automatically and implicitly load units from disk &#8212; if they are not loaded yet &#8212; as soon as operations are requested for them. Thus, in many respects, the fact whether a unit is loaded or not is invisible to clients. Use <code>systemctl list-units &#8211;all</code> to comprehensively list all units currently loaded. Any unit for which none of the conditions above applies is promptly unloaded. Note that when a unit is unloaded from memory its accounting data is flushed out too. However, this data is generally not lost, as a journal log record is generated declaring the consumed resources whenever a unit shuts down. </p>
<p> Processes systemd spawns are placed in individual Linux control groups named after the unit which they belong to in the private systemd hierarchy. (see m[blue]<code>cgroups.txt</code>m[]<font SIZE="-2">[1]</font> for more information about control groups, or short &quot;cgroups&quot;). systemd uses this to effectively keep track of processes. Control group information is maintained in the kernel, and is accessible via the file system hierarchy (beneath /sys/fs/cgroup/systemd/), or in tools such as <code><a href="/docs/linux/man/1-systemd-cgls/">systemd-cgls</a></code>(1) or <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) (<code>ps xawf -eo pid,user,cgroup,args</code> is particularly useful to list all processes and the systemd units they belong to.). </p>
<p> systemd is compatible with the SysV init system to a large degree: SysV init scripts are supported and simply read as an alternative (though limited) configuration file format. The SysV /dev/initctl interface is provided, and compatibility implementations of the various SysV client tools are available. In addition to that, various established Unix functionality such as /etc/fstab or the utmp database are supported. </p>
<p> systemd has a minimal transaction system: if a unit is requested to start up or shut down it will add it and all its dependencies to a temporary transaction. Then, it will verify if the transaction is consistent (i.e. whether the ordering of all units is cycle-free). If it is not, systemd will try to fix it up, and removes non-essential jobs from the transaction that might remove the loop. Also, systemd tries to suppress non-essential jobs in the transaction that would stop a running service. Finally it is checked whether the jobs of the transaction contradict jobs that have already been queued, and optionally the transaction is aborted then. If all worked out and the transaction is consistent and minimized in its impact it is merged with all already outstanding jobs and added to the run queue. Effectively this means that before executing a requested operation, systemd will verify that it makes sense, fixing it if possible, and only failing if it really cannot work. </p>
<p> Note that transactions are generated independently of a unit&#8217;s state at runtime, hence, for example, if a start job is requested on an already started unit, it will still generate a transaction and wake up any inactive dependencies (and cause propagation of other jobs as per the defined relationships). This is because the enqueued job is at the time of execution compared to the target unit&#8217;s state and is marked successful and complete when both satisfy. However, this job also pulls in other dependencies due to the defined relationships and thus leads to, in our example, start jobs for any of those inactive units getting queued as well. </p>
<p> systemd contains native implementations of various tasks that need to be executed as part of the boot process. For example, it sets the hostname or configures the loopback network device. It also sets up and mounts various API file systems, such as /sys/ or /proc/. </p>
<p> For more information about the concepts and ideas behind systemd, please refer to the m[blue]<code>Original Design Document</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> Note that some but not all interfaces provided by systemd are covered by the m[blue]<code>Interface Portability and Stability Promise</code>m[]<font SIZE="-2">[3]</font>. </p>
<p> Units may be generated dynamically at boot and system manager reload time, for example based on other configuration files or parameters passed on the kernel command line. For details, see <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7). </p>
<p> The D-Bus API of <code>systemd</code> is described in <code><a href="/docs/linux/man/5-org-freedesktop-systemd1/">org.freedesktop.systemd1</a></code>(5) and <code><a href="/docs/linux/man/5-org-freedesktop-logcontrol1/">org.freedesktop.LogControl1</a></code>(5). </p>
<p> Systems which invoke systemd in a container or initrd environment should implement the m[blue]<code>Container Interface</code>m[]<font SIZE="-2">[4]</font> or m[blue]<code>initrd Interface</code>m[]<font SIZE="-2">[5]</font> specifications, respectively.</p>
<h2>DIRECTORIES</h2>
<p> System unit directories</p>
<dl>
<dt>
<dd> The systemd system manager reads unit configuration from various directories. Packages that want to install unit files shall place them in the directory returned by <code>pkg-config systemd &#8211;variable=systemdsystemunitdir</code>. Other directories checked are /usr/local/lib/systemd/system and /lib/systemd/system. User configuration always takes precedence. <code>pkg-config systemd &#8211;variable=systemdsystemconfdir</code> returns the path of the system configuration directory. Packages should alter the content of these directories only with the <code>enable</code> and <code>disable</code> commands of the <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) tool. Full list of directories is provided in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5).</dl>
<p> User unit directories</p>
<dl>
<dt>
<dd> Similar rules apply for the user unit directories. However, here the m[blue]<code>XDG Base Directory specification</code>m[]<font SIZE="-2">[6]</font> is followed to find units. Applications should place their unit files in the directory returned by <code>pkg-config systemd &#8211;variable=systemduserunitdir</code>. Global configuration is done in the directory reported by <code>pkg-config systemd &#8211;variable=systemduserconfdir</code>. The <code>enable</code> and <code>disable</code> commands of the <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) tool can handle both global (i.e. for all users) and private (for one user) enabling/disabling of units. Full list of directories is provided in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5).</dl>
<p> SysV init scripts directory</p>
<dl>
<dt>
<dd> The location of the SysV init script directory varies between distributions. If systemd cannot find a native unit file for a requested service, it will look for a SysV init script of the same name (with the .service suffix removed).</dl>
<p> SysV runlevel link farm directory</p>
<dl>
<dt>
<dd> The location of the SysV runlevel link farm directory varies between distributions. systemd will take the link farm into account when figuring out whether a service shall be enabled. Note that a service unit with a native unit configuration file cannot be started by activating it in the SysV runlevel link farm.</dl>
<h2>SIGNALS</h2>
<p> <code>SIGTERM</code></p>
<dl>
<dt>
<dd> Upon receiving this signal the systemd system manager serializes its state, reexecutes itself and deserializes the saved state again. This is mostly equivalent to <code>systemctl daemon-reexec</code>. </p>
<p> systemd user managers will start the exit.target unit when this signal is received. This is mostly equivalent to <code>systemctl &#8211;user start exit.target &#8211;job-mode=replace-irreversibly</code>.</dl>
<p> <code>SIGINT</code></p>
<dl>
<dt>
<dd> Upon receiving this signal the systemd system manager will start the ctrl-alt-del.target unit. This is mostly equivalent to <code>systemctl start ctrl-alt-del.target &#8211;job-mode=replace-irreversibly</code>. If this signal is received more than 7 times per 2s, an immediate reboot is triggered. Note that pressing Ctrl+Alt+Del on the console will trigger this signal. Hence, if a reboot is hanging, pressing Ctrl+Alt+Del more than 7 times in 2 seconds is a relatively safe way to trigger an immediate reboot. </p>
<p> systemd user managers treat this signal the same way as <code>SIGTERM</code>.</dl>
<p> <code>SIGWINCH</code></p>
<dl>
<dt>
<dd> When this signal is received the systemd system manager will start the kbrequest.target unit. This is mostly equivalent to <code>systemctl start kbrequest.target</code>. </p>
<p> This signal is ignored by systemd user managers.</dl>
<p> <code>SIGPWR</code></p>
<dl>
<dt>
<dd> When this signal is received the systemd manager will start the sigpwr.target unit. This is mostly equivalent to <code>systemctl start sigpwr.target</code>.</dl>
<p> <code>SIGUSR1</code></p>
<dl>
<dt>
<dd> When this signal is received the systemd manager will try to reconnect to the D-Bus bus.</dl>
<p> <code>SIGUSR2</code></p>
<dl>
<dt>
<dd> When this signal is received the systemd manager will log its complete state in human-readable form. The data logged is the same as printed by <code>systemd-analyze dump</code>.</dl>
<p> <code>SIGHUP</code></p>
<dl>
<dt>
<dd> Reloads the complete daemon configuration. This is mostly equivalent to <code>systemctl daemon-reload</code>.</dl>
<p> <code>SIGRTMIN+0</code></p>
<dl>
<dt>
<dd> Enters default mode, starts the default.target unit. This is mostly equivalent to <code>systemctl isolate default.target</code>.</dl>
<p> <code>SIGRTMIN+1</code></p>
<dl>
<dt>
<dd> Enters rescue mode, starts the rescue.target unit. This is mostly equivalent to <code>systemctl isolate rescue.target</code>.</dl>
<p> <code>SIGRTMIN+2</code></p>
<dl>
<dt>
<dd> Enters emergency mode, starts the emergency.service unit. This is mostly equivalent to <code>systemctl isolate emergency.service</code>.</dl>
<p> <code>SIGRTMIN+3</code></p>
<dl>
<dt>
<dd> Halts the machine, starts the halt.target unit. This is mostly equivalent to <code>systemctl start halt.target &#8211;job-mode=replace-irreversibly</code>.</dl>
<p> <code>SIGRTMIN+4</code></p>
<dl>
<dt>
<dd> Powers off the machine, starts the poweroff.target unit. This is mostly equivalent to <code>systemctl start poweroff.target &#8211;job-mode=replace-irreversibly</code>.</dl>
<p> <code>SIGRTMIN+5</code></p>
<dl>
<dt>
<dd> Reboots the machine, starts the reboot.target unit. This is mostly equivalent to <code>systemctl start reboot.target &#8211;job-mode=replace-irreversibly</code>.</dl>
<p> <code>SIGRTMIN+6</code></p>
<dl>
<dt>
<dd> Reboots the machine via kexec, starts the kexec.target unit. This is mostly equivalent to <code>systemctl start kexec.target &#8211;job-mode=replace-irreversibly</code>.</dl>
<p> <code>SIGRTMIN+13</code></p>
<dl>
<dt>
<dd> Immediately halts the machine.</dl>
<p> <code>SIGRTMIN+14</code></p>
<dl>
<dt>
<dd> Immediately powers off the machine.</dl>
<p> <code>SIGRTMIN+15</code></p>
<dl>
<dt>
<dd> Immediately reboots the machine.</dl>
<p> <code>SIGRTMIN+16</code></p>
<dl>
<dt>
<dd> Immediately reboots the machine with kexec.</dl>
<p> <code>SIGRTMIN+20</code></p>
<dl>
<dt>
<dd> Enables display of status messages on the console, as controlled via <i>systemd.show_status=1</i> on the kernel command line.</dl>
<p> <code>SIGRTMIN+21</code></p>
<dl>
<dt>
<dd> Disables display of status messages on the console, as controlled via <i>systemd.show_status=0</i> on the kernel command line.</dl>
<p> <code>SIGRTMIN+22</code></p>
<dl>
<dt>
<dd> Sets the service manager&#8217;s log level to &quot;debug&quot;, in a fashion equivalent to <i>systemd.log_level=debug</i> on the kernel command line.</dl>
<p> <code>SIGRTMIN+23</code></p>
<dl>
<dt>
<dd> Restores the log level to its configured value. The configured value is derived from &#8211; in order of priority &#8211; the value specified with <i>systemd.log-level=</i> on the kernel command line, or the value specified with <code>LogLevel=</code> in the configuration file, or the built-in default of &quot;info&quot;.</dl>
<p> <code>SIGRTMIN+24</code></p>
<dl>
<dt>
<dd> Immediately exits the manager (only available for &#8211;user instances).</dl>
<p> <code>SIGRTMIN+26</code></p>
<dl>
<dt>
<dd> Restores the log target to its configured value. The configured value is derived from &#8211; in order of priority &#8211; the value specified with <i>systemd.log-target=</i> on the kernel command line, or the value specified with <code>LogTarget=</code> in the configuration file, or the built-in default.</dl>
<p> <code>SIGRTMIN+27</code>, <code>SIGRTMIN+28</code></p>
<dl>
<dt>
<dd> Sets the log target to &quot;console&quot; on <code>SIGRTMIN+27</code> (or &quot;kmsg&quot; on <code>SIGRTMIN+28</code>), in a fashion equivalent to <i>systemd.log_target=console</i> (or <i>systemd.log_target=kmsg</i> on <code>SIGRTMIN+28</code>) on the kernel command line.</dl>
<h2>ENVIRONMENT</h2>
<p> The environment block for the system manager is initially set by the kernel. (In particular, &quot;key=value&quot; assignments on the kernel command line are returned into environment variables for PID 1). For the user manager, the system manager sets the environment as described in the &quot;Environment Variables in Spawned Processes&quot; section of <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5). The <i>DefaultEnvironment=</i> setting in the system manager applies to all services including user [at] .service. Additional entries may be configured (as for any other service) through the <i>Environment=</i> and <i>EnvironmentFile=</i> settings for user [at] .service (see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5)). Also, additional environment variables may be set through the <i>ManagerEnvironment=</i> setting in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-user-conf/">systemd-user.conf</a></code>(5). </p>
<p> Some of the variables understood by <code>systemd</code>: </p>
<p> <i>$SYSTEMD_LOG_LEVEL</i></p>
<dl>
<dt>
<dd> The maximum log level of emitted messages (messages with a higher log level, i.e. less important ones, will be suppressed). Either one of (in order of decreasing importance) <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code>, or an integer in the range 0&#8230;7. See <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for more information. </p>
<p> This can be overridden with <code>&#8211;log-level=</code>.</dl>
<p> <i>$SYSTEMD_LOG_COLOR</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages written to the tty will be colored according to priority. </p>
<p> This can be overridden with <code>&#8211;log-color=</code>.</dl>
<p> <i>$SYSTEMD_LOG_TIME</i></p>
<dl>
<dt>
<dd> A boolean. If true, console log messages will be prefixed with a timestamp. </p>
<p> This can be overridden with <code>&#8211;log-time=</code>.</dl>
<p> <i>$SYSTEMD_LOG_LOCATION</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages will be prefixed with a filename and line number in the source code where the message originates. </p>
<p> This can be overridden with <code>&#8211;log-location=</code>.</dl>
<p> <i>$SYSTEMD_LOG_TID</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages will be prefixed with the current numerical thread ID (TID).</dl>
<p> <i>$SYSTEMD_LOG_TARGET</i></p>
<dl>
<dt>
<dd> The destination for log messages. One of <code>console</code> (log to the attached tty), <code>console-prefixed</code> (log to the attached tty but with prefixes encoding the log level and &quot;facility&quot;, see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code>kmsg</code> (log to the kernel circular log buffer), <code>journal</code> (log to the journal), <code>journal-or-kmsg</code> (log to the journal if available, and to kmsg otherwise), <code>auto</code> (determine the appropriate log target automatically, the default), <code>null</code> (disable log output). </p>
<p> This can be overridden with <code>&#8211;log-target=</code>.</dl>
<p> <i>$XDG_CONFIG_HOME</i>, <i>$XDG_CONFIG_DIRS</i>, <i>$XDG_DATA_HOME</i>, <i>$XDG_DATA_DIRS</i></p>
<dl>
<dt>
<dd> The systemd user manager uses these variables in accordance to the m[blue]<code>XDG Base Directory specification</code>m[]<font SIZE="-2">[6]</font> to find its configuration.</dl>
<p> <i>$SYSTEMD_UNIT_PATH</i>, <i>$SYSTEMD_GENERATOR_PATH</i>, <i>$SYSTEMD_ENVIRONMENT_GENERATOR_PATH</i></p>
<dl>
<dt>
<dd> Controls where systemd looks for unit files and generators. </p>
<p> These variables may contain a list of paths, separated by colons (&quot;:&quot;). When set, if the list ends with an empty component (&quot;&#8230;:&quot;), this list is prepended to the usual set of paths. Otherwise, the specified list replaces the usual set of paths.</dl>
<p> <i>$SYSTEMD_PAGER</i></p>
<dl>
<dt>
<dd> Pager to use when <code>&#8211;no-pager</code> is not given; overrides <i>$PAGER</i>. If neither <i>$SYSTEMD_PAGER</i> nor <i>$PAGER</i> are set, a set of well-known pager implementations are tried in turn, including <code><a href="/docs/linux/man/1-less/">less</a></code>(1) and <code><a href="/docs/linux/man/1-more/">more</a></code>(1), until one is found. If no pager implementation is discovered no pager is invoked. Setting this environment variable to an empty string or the value &quot;cat&quot; is equivalent to passing <code>&#8211;no-pager</code>.</dl>
<p> <i>$SYSTEMD_LESS</i></p>
<dl>
<dt>
<dd> Override the options passed to <code>less</code> (by default &quot;FRSXMK&quot;). </p>
<p> Users might want to change two options in particular: </p>
<p> <code>K</code></p>
<dl>
<dt>
<dd> This option instructs the pager to exit immediately when Ctrl+C is pressed. To allow <code>less</code> to handle Ctrl+C itself to switch back to the pager command prompt, unset this option. </p>
<p> If the value of <i>$SYSTEMD_LESS</i> does not include &quot;K&quot;, and the pager that is invoked is <code>less</code>, Ctrl+C will be ignored by the executable, and needs to be handled by the pager.</dl>
<p> <code>X</code></p>
<dl>
<dt>
<dd> This option instructs the pager to not send termcap initialization and deinitialization strings to the terminal. It is set by default to allow command output to remain visible in the terminal even after the pager exits. Nevertheless, this prevents some pager functionality from working, in particular paged output cannot be scrolled with the mouse.</dl>
<p> See <code><a href="/docs/linux/man/1-less/">less</a></code>(1) for more discussion.</dl>
<p> <i>$SYSTEMD_LESSCHARSET</i></p>
<dl>
<dt>
<dd> Override the charset passed to <code>less</code> (by default &quot;utf-8&quot;, if the invoking terminal is determined to be UTF-8 compatible).</dl>
<p> <i>$SYSTEMD_PAGERSECURE</i></p>
<dl>
<dt>
<dd> Takes a boolean argument. When true, the &quot;secure&quot; mode of the pager is enabled; if false, disabled. If <i>$SYSTEMD_PAGERSECURE</i> is not set at all, secure mode is enabled if the effective UID is not the same as the owner of the login session, see <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2) and <code><a href="/docs/linux/man/3-sd_pid_get_owner_uid/">sd_pid_get_owner_uid</a></code>(3). In secure mode, <code>LESSSECURE=1</code> will be set when invoking the pager, and the pager shall disable commands that open or create new files or start new subprocesses. When <i>$SYSTEMD_PAGERSECURE</i> is not set at all, pagers which are not known to implement secure mode will not be used. (Currently only <code><a href="/docs/linux/man/1-less/">less</a></code>(1) implements secure mode.) </p>
<p> Note: when commands are invoked with elevated privileges, for example under <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) or <code><a href="/docs/linux/man/1-pkexec/">pkexec</a></code>(1), care must be taken to ensure that unintended interactive features are not enabled. &quot;Secure&quot; mode for the pager may be enabled automatically as describe above. Setting <i>SYSTEMD_PAGERSECURE=0</i> or not removing it from the inherited environment allows the user to invoke arbitrary commands. Note that if the <i>$SYSTEMD_PAGER</i> or <i>$PAGER</i> variables are to be honoured, <i>$SYSTEMD_PAGERSECURE</i> must be set too. It might be reasonable to completely disable the pager using <code>&#8211;no-pager</code> instead.</dl>
<p> <i>$SYSTEMD_COLORS</i></p>
<dl>
<dt>
<dd> Takes a boolean argument. When true, <code>systemd</code> and related utilities will use colors in their output, otherwise the output will be monochrome. Additionally, the variable can take one of the following special values: &quot;16&quot;, &quot;256&quot; to restrict the use of colors to the base 16 or 256 ANSI colors, respectively. This can be specified to override the automatic decision based on <i>$TERM</i> and what the console is connected to.</dl>
<p> <i>$SYSTEMD_URLIFY</i></p>
<dl>
<dt>
<dd> The value must be a boolean. Controls whether clickable links should be generated in the output for terminal emulators supporting this. This can be specified to override the decision that <code>systemd</code> makes based on <i>$TERM</i> and other conditions.</dl>
<p> <i>$LISTEN_PID</i>, <i>$LISTEN_FDS</i>, <i>$LISTEN_FDNAMES</i></p>
<dl>
<dt>
<dd> Set by systemd for supervised processes during socket-based activation. See <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3) for more information.</dl>
<p> <i>$NOTIFY_SOCKET</i></p>
<dl>
<dt>
<dd> Set by systemd for supervised processes for status and start-up completion notification. See <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3) for more information.</dl>
<p> For further environment variables understood by systemd and its various components, see m[blue]<code>Known Environment Variables</code>m[]<font SIZE="-2">[7]</font>.</p>
<h2>KERNEL COMMAND LINE</h2>
<p> When run as the system instance systemd parses a number of options listed below. They can be specified as kernel command line arguments<font SIZE="-2">[8]</font>, or through the &quot;SystemdOptions&quot; EFI variable (on EFI systems). The kernel command line has higher priority. Following variables are understood: </p>
<p> <i>systemd.unit=</i>, <i>rd.systemd.unit=</i></p>
<dl>
<dt>
<dd> Overrides the unit to activate on boot. Defaults to default.target. This may be used to temporarily boot into a different boot unit, for example rescue.target or emergency.service. See <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for details about these units. The option prefixed with &quot;rd.&quot; is honored only in the initial RAM disk (initrd), while the one that is not prefixed only in the main system.</dl>
<p> <i>systemd.dump_core</i></p>
<dl>
<dt>
<dd> Takes a boolean argument or enables the option if specified without an argument. If enabled, the systemd manager (PID 1) dumps core when it crashes. Otherwise, no core dump is created. Defaults to enabled.</dl>
<p> <i>systemd.crash_chvt</i></p>
<dl>
<dt>
<dd> Takes a positive integer, or a boolean argument. Can be also specified without an argument, with the same effect as a positive boolean. If a positive integer (in the range 1-63) is specified, the system manager (PID 1) will activate the specified virtual terminal when it crashes. Defaults to disabled, meaning that no such switch is attempted. If set to enabled, the virtual terminal the kernel messages are written to is used instead.</dl>
<p> <i>systemd.crash_shell</i></p>
<dl>
<dt>
<dd> Takes a boolean argument or enables the option if specified without an argument. If enabled, the system manager (PID 1) spawns a shell when it crashes, after a 10s delay. Otherwise, no shell is spawned. Defaults to disabled, for security reasons, as the shell is not protected by password authentication.</dl>
<p> <i>systemd.crash_reboot</i></p>
<dl>
<dt>
<dd> Takes a boolean argument or enables the option if specified without an argument. If enabled, the system manager (PID 1) will reboot the machine automatically when it crashes, after a 10s delay. Otherwise, the system will hang indefinitely. Defaults to disabled, in order to avoid a reboot loop. If combined with <i>systemd.crash_shell</i>, the system is rebooted after the shell exits.</dl>
<p> <i>systemd.confirm_spawn</i></p>
<dl>
<dt>
<dd> Takes a boolean argument or a path to the virtual console where the confirmation messages should be emitted. Can be also specified without an argument, with the same effect as a positive boolean. If enabled, the system manager (PID 1) asks for confirmation when spawning processes using <code>/dev/console</code>. If a path or a console name (such as &quot;ttyS0&quot;) is provided, the virtual console pointed to by this path or described by the give name will be used instead. Defaults to disabled.</dl>
<p> <i>systemd.service_watchdogs=</i></p>
<dl>
<dt>
<dd> Takes a boolean argument. If disabled, all service runtime watchdogs (<code>WatchdogSec=</code>) and emergency actions (e.g. <code>OnFailure=</code> or <code>StartLimitAction=</code>) are ignored by the system manager (PID 1); see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5). Defaults to enabled, i.e. watchdogs and failure actions are processed normally. The hardware watchdog is not affected by this option.</dl>
<p> <i>systemd.show_status</i></p>
<dl>
<dt>
<dd> Takes a boolean argument or the constants <code>error</code> and <code>auto</code>. Can be also specified without an argument, with the same effect as a positive boolean. If enabled, the systemd manager (PID 1) shows terse service status updates on the console during bootup. With <code>error</code>, only messages about failures are shown, but boot is otherwise quiet. <code>auto</code> behaves like <code>false</code> until there is a significant delay in boot. Defaults to enabled, unless <code>quiet</code> is passed as kernel command line option, in which case it defaults to <code>error</code>. If specified overrides the system manager configuration file option <code>ShowStatus=</code>, see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> <i>systemd.status_unit_format=</i></p>
<dl>
<dt>
<dd> Takes <code>name</code>, <code>description</code> or <code>combined</code> as the value. If <code>name</code>, the system manager will use unit names in status messages. If <code>combined</code>, the system manager will use unit names and description in status messages. When specified, overrides the system manager configuration file option <code>StatusUnitFormat=</code>, see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> <i>systemd.log_color</i>, <i>systemd.log_level=</i>, <i>systemd.log_location</i>, <i>systemd.log_target=</i>, <i>systemd.log_time</i>, <i>systemd.log_tid</i></p>
<dl>
<dt>
<dd> Controls log output, with the same effect as the <i>$SYSTEMD_LOG_COLOR</i>, <i>$SYSTEMD_LOG_LEVEL</i>, <i>$SYSTEMD_LOG_LOCATION</i>, <i>$SYSTEMD_LOG_TARGET</i>, <i>$SYSTEMD_LOG_TIME</i>, and <i>$SYSTEMD_LOG_TID</i> environment variables described above. <i>systemd.log_color</i>, <i>systemd.log_location</i>, <i>systemd.log_time</i>, and <i>systemd.log_tid=</i> can be specified without an argument, with the same effect as a positive boolean.</dl>
<p> <i>systemd.default_standard_output=</i>, <i>systemd.default_standard_error=</i></p>
<dl>
<dt>
<dd> Controls default standard output and error output for services and sockets. That is, controls the default for <code>StandardOutput=</code> and <code>StandardError=</code> (see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details). Takes one of <code>inherit</code>, <code>null</code>, <code>tty</code>, <code>journal</code>, <code>journal+console</code>, <code>kmsg</code>, <code>kmsg+console</code>. If the argument is omitted <i>systemd.default-standard-output=</i> defaults to <code>journal</code> and <i>systemd.default-standard-error=</i> to <code>inherit</code>.</dl>
<p> <i>systemd.setenv=</i></p>
<dl>
<dt>
<dd> Takes a string argument in the form VARIABLE=VALUE. May be used to set default environment variables to add to forked child processes. May be used more than once to set multiple variables.</dl>
<p> <i>systemd.machine_id=</i></p>
<dl>
<dt>
<dd> Takes a 32 character hex value to be used for setting the machine-id. Intended mostly for network booting where the same machine-id is desired for every boot.</dl>
<p> <i>systemd.unified_cgroup_hierarchy</i></p>
<dl>
<dt>
<dd> When specified without an argument or with a true argument, enables the usage of m[blue]<code>unified cgroup hierarchy</code>m[]<font SIZE="-2">[9]</font> (a.k.a. cgroups-v2). When specified with a false argument, fall back to hybrid or full legacy cgroup hierarchy. </p>
<p> If this option is not specified, the default behaviour is determined during compilation (the <code>-Ddefault-hierarchy=</code> meson option). If the kernel does not support unified cgroup hierarchy, the legacy hierarchy will be used even if this option is specified.</dl>
<p> <i>systemd.legacy_systemd_cgroup_controller</i></p>
<dl>
<dt>
<dd> Takes effect if the full unified cgroup hierarchy is not used (see previous option). When specified without an argument or with a true argument, disables the use of &quot;hybrid&quot; cgroup hierarchy (i.e. a cgroups-v2 tree used for systemd, and m[blue]<code>legacy cgroup hierarchy</code>m[]<font SIZE="-2">[10]</font>, a.k.a. cgroups-v1, for other controllers), and forces a full &quot;legacy&quot; mode. When specified with a false argument, enables the use of &quot;hybrid&quot; hierarchy. </p>
<p> If this option is not specified, the default behaviour is determined during compilation (the <code>-Ddefault-hierarchy=</code> meson option). If the kernel does not support unified cgroup hierarchy, the legacy hierarchy will be used even if this option is specified.</dl>
<p> <i>quiet</i></p>
<dl>
<dt>
<dd> Turn off status output at boot, much like <i>systemd.show_status=no</i> would. Note that this option is also read by the kernel itself and disables kernel log output. Passing this option hence turns off the usual output from both the system manager and the kernel.</dl>
<p> <i>debug</i></p>
<dl>
<dt>
<dd> Turn on debugging output. This is equivalent to <i>systemd.log_level=debug</i>. Note that this option is also read by the kernel itself and enables kernel debug output. Passing this option hence turns on the debug output from both the system manager and the kernel.</dl>
<p> <i>emergency</i>, <i>rd.emergency</i>, <i>-b</i></p>
<dl>
<dt>
<dd> Boot into emergency mode. This is equivalent to <i>systemd.unit=emergency.target</i> or <i>rd.systemd.unit=emergency.target</i>, respectively, and provided for compatibility reasons and to be easier to type.</dl>
<p> <i>rescue</i>, <i>rd.rescue</i>, <i>single</i>, <i>s</i>, <i>S</i>, <i>1</i></p>
<dl>
<dt>
<dd> Boot into rescue mode. This is equivalent to <i>systemd.unit=rescue.target</i> or <i>rd.systemd.unit=rescue.target</i>, respectively, and provided for compatibility reasons and to be easier to type.</dl>
<p> <i>2</i>, <i>3</i>, <i>4</i>, <i>5</i></p>
<dl>
<dt>
<dd> Boot into the specified legacy SysV runlevel. These are equivalent to <i>systemd.unit=runlevel2.target</i>, <i>systemd.unit=runlevel3.target</i>, <i>systemd.unit=runlevel4.target</i>, and <i>systemd.unit=runlevel5.target</i>, respectively, and provided for compatibility reasons and to be easier to type.</dl>
<p> <i>locale.LANG=</i>, <i>locale.LANGUAGE=</i>, <i>locale.LC_CTYPE=</i>, <i>locale.LC_NUMERIC=</i>, <i>locale.LC_TIME=</i>, <i>locale.LC_COLLATE=</i>, <i>locale.LC_MONETARY=</i>, <i>locale.LC_MESSAGES=</i>, <i>locale.LC_PAPER=</i>, <i>locale.LC_NAME=</i>, <i>locale.LC_ADDRESS=</i>, <i>locale.LC_TELEPHONE=</i>, <i>locale.LC_MEASUREMENT=</i>, <i>locale.LC_IDENTIFICATION=</i></p>
<dl>
<dt>
<dd> Set the system locale to use. This overrides the settings in /etc/locale.conf. For more information, see <code><a href="/docs/linux/man/5-locale-conf/">locale.conf</a></code>(5) and <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7).</dl>
<p> For other kernel command line parameters understood by components of the core OS, please refer to <code><a href="/docs/linux/man/7-kernel-command-line/">kernel-command-line</a></code>(7).</p>
<h2>OPTIONS</h2>
<p> <code>systemd</code> is only very rarely invoked directly, since it is started early and is already running by the time users may interact with it. Normally, tools like <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) are used to give commands to the manager. Since <code>systemd</code> is usually not invoked directly, the options listed below are mostly useful for debugging and special purposes.</p>
<h3>Introspection and debugging options</h3>
<p> Those options are used for testing and introspection, and <code>systemd</code> may be invoked with them at any time: </p>
<p> <code>&#8211;dump-configuration-items</code></p>
<dl>
<dt>
<dd> Dump understood unit configuration items. This outputs a terse but complete list of configuration items understood in unit definition files.</dl>
<p> <code>&#8211;dump-bus-properties</code></p>
<dl>
<dt>
<dd> Dump exposed bus properties. This outputs a terse but complete list of properties exposed on D-Bus.</dl>
<p> <code>&#8211;test</code></p>
<dl>
<dt>
<dd> Determine the initial start-up transaction (i.e. the list of jobs enqueued at start-up), dump it and exit &#8212; without actually executing any of the determined jobs. This option is useful for debugging only. Note that during regular service manager start-up additional units not shown by this operation may be started, because hardware, socket, bus or other kinds of activation might add additional jobs as the transaction is executed. Use <code>&#8211;system</code> to request the initial transaction of the system service manager (this is also the implied default), combine with <code>&#8211;user</code> to request the initial transaction of the per-user service manager instead.</dl>
<p> <code>&#8211;system</code>, <code>&#8211;user</code></p>
<dl>
<dt>
<dd> When used in conjunction with <code>&#8211;test</code>, selects whether to calculate the initial transaction for the system instance or for a per-user instance. These options have no effect when invoked without <code>&#8211;test</code>, as during regular (i.e. non-<code>&#8211;test</code>) invocations the service manager will automatically detect whether it shall operate in system or per-user mode, by checking whether the PID it is run as is 1 or not. Note that it is not supported booting and maintaining a system with the service manager running in <code>&#8211;system</code> mode but with a PID other than 1.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h3>Options that duplicate kernel command line settings</h3>
<p> Those options correspond directly to options listed above in &quot;Kernel Command Line&quot;. Both forms may be used equivalently for the system manager, but it is recommended to use the forms listed above in this context, because they are properly namespaced. When an option is specified both on the kernel command line and as a normal command line argument, the latter has higher precedence. </p>
<p> When <code>systemd</code> is used as a user manager, the kernel command line is ignored and only the options described below are understood. Nevertheless, <code>systemd</code> is usually started in this mode through the <code>user [at] .service</code>(5) service, which is shared between all users. It may be more convenient to use configuration files to modify settings (see <code><a href="/docs/linux/man/5-systemd-user-conf/">systemd-user.conf</a></code>(5)), or environment variables. See the &quot;Environment&quot; section above for a discussion of how the environment block is set. </p>
<p> <code>&#8211;unit=</code></p>
<dl>
<dt>
<dd> Set default unit to activate on startup. If not specified, defaults to default.target. See <i>systemd.unit=</i> above.</dl>
<p> <code>&#8211;dump-core</code></p>
<dl>
<dt>
<dd> Enable core dumping on crash. This switch has no effect when running as user instance. Same as <i>systemd.dump_core=</i> above.</dl>
<p> <code>&#8211;crash-vt=</code><i>VT</i></p>
<dl>
<dt>
<dd> Switch to a specific virtual console (VT) on crash. This switch has no effect when running as user instance. Same as <i>systemd.crash_chvt=</i> above (but not the different spelling!).</dl>
<p> <code>&#8211;crash-shell</code></p>
<dl>
<dt>
<dd> Run a shell on crash. This switch has no effect when running as user instance. See <i>systemd.crash_shell=</i> above.</dl>
<p> <code>&#8211;crash-reboot</code></p>
<dl>
<dt>
<dd> Automatically reboot the system on crash. This switch has no effect when running as user instance. See <i>systemd.crash_reboot</i> above.</dl>
<p> <code>&#8211;confirm-spawn</code></p>
<dl>
<dt>
<dd> Ask for confirmation when spawning processes. This switch has no effect when run as user instance. See <i>systemd.confirm_spawn</i> above.</dl>
<p> <code>&#8211;show-status</code></p>
<dl>
<dt>
<dd> Show terse unit status information on the console during boot-up and shutdown. See <i>systemd.show_status</i> above.</dl>
<p> <code>&#8211;log-color</code></p>
<dl>
<dt>
<dd> Highlight important log messages. See <i>systemd.log_color</i> above.</dl>
<p> <code>&#8211;log-level=</code></p>
<dl>
<dt>
<dd> Set log level. See <i>systemd.log_level</i> above.</dl>
<p> <code>&#8211;log-location</code></p>
<dl>
<dt>
<dd> Include code location in log messages. See <i>systemd.log_location</i> above.</dl>
<p> <code>&#8211;log-target=</code></p>
<dl>
<dt>
<dd> Set log target. See <i>systemd.log_target</i> above.</dl>
<p> <code>&#8211;log-time=</code></p>
<dl>
<dt>
<dd> Prefix console messages with timestamp. See <i>systemd.log_time</i> above.</dl>
<p> <code>&#8211;machine-id=</code></p>
<dl>
<dt>
<dd> Override the machine-id set on the hard drive. See <i>systemd.machine_id=</i> above.</dl>
<p> <code>&#8211;service-watchdogs</code></p>
<dl>
<dt>
<dd> Globally enable/disable all service watchdog timeouts and emergency actions. See <i>systemd.service_watchdogs</i> above.</dl>
<p> <code>&#8211;default-standard-output=</code>, <code>&#8211;default-standard-error=</code></p>
<dl>
<dt>
<dd> Sets the default output or error output for all services and sockets, respectively. See <i>systemd.default_standard_output=</i> and <i>systemd.default_standard_error=</i> above.</dl>
<h2>SOCKETS AND FIFOS</h2>
<p> /run/systemd/notify</p>
<dl>
<dt>
<dd> Daemon status notification socket. This is an <code>AF_UNIX</code> datagram socket and is used to implement the daemon notification logic as implemented by <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3).</dl>
<p> /run/systemd/private</p>
<dl>
<dt>
<dd> Used internally as communication channel between <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) and the systemd process. This is an <code>AF_UNIX</code> stream socket. This interface is private to systemd and should not be used in external projects.</dl>
<p> /dev/initctl</p>
<dl>
<dt>
<dd> Limited compatibility support for the SysV client interface, as implemented by the systemd-initctl.service unit. This is a named pipe in the file system. This interface is obsolete and should not be used in new applications.</dl>
<h2>SEE ALSO</h2>
<p> The m[blue]<code>systemd Homepage</code>m[]<font SIZE="-2">[11]</font>, <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/5-locale-conf/">locale.conf</a></code>(5), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/1-systemd-notify/">systemd-notify</a></code>(1), <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7), <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3), <code><a href="/docs/linux/man/5-org-freedesktop-systemd1/">org.freedesktop.systemd1</a></code>(5), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1), <code><a href="/docs/linux/man/7-kernel-command-line/">kernel-command-line</a></code>(7), <code><a href="/docs/linux/man/7-bootup/">bootup</a></code>(7), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> cgroups.txt</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt">https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt</a></dl>
<dt> 2.</p>
<dd> Original Design Document</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://0pointer.de/blog/projects/systemd.html">http://0pointer.de/blog/projects/systemd.html</a></dl>
<dt> 3.</p>
<dd> Interface Portability and Stability Promise</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/PORTABILITY_AND_STABILITY/">https://systemd.io/PORTABILITY_AND_STABILITY/</a></dl>
<dt> 4.</p>
<dd> Container Interface</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/CONTAINER_INTERFACE">https://systemd.io/CONTAINER_INTERFACE</a></dl>
<dt> 5.</p>
<dd> initrd Interface</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/INITRD_INTERFACE/">https://systemd.io/INITRD_INTERFACE/</a></dl>
<dt> 6.</p>
<dd> XDG Base Directory specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html">http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html</a></dl>
<dt> 7.</p>
<dd> Known Environment Variables</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/ENVIRONMENT">https://systemd.io/ENVIRONMENT</a></dl>
<dt> 8.</p>
<dd> If run inside a Linux container these arguments may be passed as command line arguments to systemd itself, next to any of the command line options listed in the Options section above. If run outside of Linux containers, these arguments are parsed from /proc/cmdline instead.</p>
<dt> 9.</p>
<dd> unified cgroup hierarchy</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html">https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html</a></dl>
<dt>10.</p>
<dd> legacy cgroup hierarchy</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.kernel.org/doc/Documentation/cgroup-v1/">https://www.kernel.org/doc/Documentation/cgroup-v1/</a></dl>
<dt>11.</p>
<dd> systemd Homepage</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/">https://www.freedesktop.org/wiki/Software/systemd/</a></dl>
</dl>
<h2>Index</h2>
