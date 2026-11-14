---
title: "systemd-systemctl(1)"
name: "systemd-systemctl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-systemctl/"
description: "systemctl, systemd-systemctl – Control the systemd system and service manager"
---

<h2 class="name">NAME</h2>
<p> systemctl, systemd-systemctl &#8211; Control the systemd system and service manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemctl </code><code>[OPTIONS&#8230;]</code><code>{COMMAND}</code><code>[NAME&#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>systemctl</code></p>
<dd>may be used to introspect and control the state of the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) system and service manager.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;help</code>, <code>-h</code></p>
<dl>
<dt>
<dd> Prints a short help text and exits.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints a short version string and exits.</dl>
<p> <code>&#8211;type=</code>, <code>-t</code></p>
<dl>
<dt>
<dd> The argument should be a unit type name such as <code>service</code> and <code>socket</code>, or a unit load state such as <code>loaded</code> and <code>masked</code>. </p>
<p> If the argument is a unit type, when listing units, limit display to certain unit types. If not specified units of all types will be shown. </p>
<p> If the argument is a unit load state, when listing units, limit display to certain unit types. If not specified units of in all load states will be shown.</dl>
<p> <code>&#8211;property=</code>, <code>-p</code></p>
<dl>
<dt>
<dd> When showing unit/job/manager properties, limit display to certain properties as specified as argument. If not specified all set properties are shown. The argument should be a property name, such as MainPID. If specified more than once all properties with the specified names are shown.</dl>
<p> <code>&#8211;all</code>, <code>-a</code></p>
<dl>
<dt>
<dd> When listing units, show all units, regardless of their state, including inactive units. When showing unit/job/manager properties, show all properties regardless whether they are set or not.</dl>
<p> <code>&#8211;failed</code></p>
<dl>
<dt>
<dd> When listing units, show only failed units. Do not confuse with <code>&#8211;fail</code>.</dl>
<p> <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Do not ellipsize unit names and truncate unit descriptions in the output of <code>list-units</code> and <code>list-jobs</code>.</dl>
<p> <code>&#8211;fail</code></p>
<dl>
<dt>
<dd> If the requested operation conflicts with a pending unfinished job, fail the command. If this is not specified the requested operation will replace the pending job, if necessary. Do not confuse with <code>&#8211;failed</code>.</dl>
<p> <code>&#8211;ignore-dependencies</code></p>
<dl>
<dt>
<dd> When enqueuing a new job ignore all its dependencies and execute it immediately. If passed no required units of the unit passed will be pulled in, and no ordering dependencies will be honoured. This is mostly a debugging and rescue tool for the administrator and should not be used by applications.</dl>
<p> <code>&#8211;quiet</code>, <code>-q</code></p>
<dl>
<dt>
<dd> Suppress output to STDOUT in <code>snapshot</code>, <code>is-active</code>, <code>enable</code> and <code>disable</code>.</dl>
<p> <code>&#8211;no-block</code></p>
<dl>
<dt>
<dd> Do not synchronously wait for the requested operation to finish. If this is not specified the job will be verified, enqueued and <code>systemctl</code> will wait until it is completed. By passing this argument it is only verified and enqueued.</dl>
<p> <code>&#8211;no-legend</code></p>
<dl>
<dt>
<dd> Do not print a legend, i.e. the column headers and the footer with hints.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Talk to the systemd system manager. (Default)</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Talk to the systemd manager of the calling user.</dl>
<p> <code>&#8211;order</code>, <code>&#8211;require</code></p>
<dl>
<dt>
<dd> When used in conjunction with the <code>dot</code> command (see below), selects which dependencies are shown in the dependency graph. If <code>&#8211;order</code> is passed only dependencies of type <i>After=</i> or <i>Before=</i> are shown. If <code>&#8211;require</code> is passed only dependencies of type <i>Requires=</i>, <i>RequiresOverridable=</i>, <i>Requisite=</i>, <i>RequisiteOverridable=</i>, <i>Wants=</i> and <i>Conflicts=</i> are shown. If neither is passed, shows dependencies of all these types.</dl>
<p> <code>&#8211;no-wall</code></p>
<dl>
<dt>
<dd> Don&#8217;t send wall message before halt, power-off, reboot.</dl>
<p> <code>&#8211;global</code></p>
<dl>
<dt>
<dd> When used with <code>enable</code> and <code>disable</code>, operate on the global user configuration directory, thus enabling or disabling a unit file globally for all future logins of all users.</dl>
<p> <code>&#8211;no-reload</code></p>
<dl>
<dt>
<dd> When used with <code>enable</code> and <code>disable</code>, do not implicitly reload daemon configuration after executing the changes.</dl>
<p> <code>&#8211;no-ask-password</code></p>
<dl>
<dt>
<dd> When used with <code>start</code> and related commands, disables asking for passwords. Background services may require input of a password or passphrase string, for example to unlock system hard disks or cryptographic certificates. Unless this option is specified and the command is invoked from a terminal <code>systemctl</code> will query the user on the terminal for the necessary secrets. Use this option to switch this behavior off. In this case the password must be supplied by some other means (for example graphical password agents) or the service might fail. This also disables querying the user for authentication for privileged operations.</dl>
<p> <code>&#8211;kill-who=</code></p>
<dl>
<dt>
<dd> When used with <code>kill</code>, choose which processes to kill. Must be one of <code>main</code>, <code>control</code> or <code>all</code> to select whether to kill only the main process of the unit, the control process or all processes of the unit. If omitted defaults to <code>all</code>.</dl>
<p> <code>&#8211;signal=</code>, <code>-s</code></p>
<dl>
<dt>
<dd> When used with <code>kill</code>, choose which signal to send to selected processes. Must be one of the well known signal specifiers such as SIGTERM, SIGINT or SIGSTOP. If omitted defaults to <code>SIGTERM</code>.</dl>
<p> <code>&#8211;force</code>, <code>-f</code></p>
<dl>
<dt>
<dd> When used with <code>enable</code>, overwrite any existing conflicting symlinks. When used with <code>halt</code>, <code>poweroff</code>, <code>reboot</code> or <code>kexec</code> execute the selected operation without shutting down all units. However, all processes will be killed forcibly and all file systems are unmounted or remounted read-only. This is hence a drastic but relatively safe option to request an immediate reboot. If <code>&#8211;force</code> is specified twice for these operations, they will be executed immediately without terminating any processes or umounting any file systems. Warning: specifying <code>&#8211;force</code> twice with any of these operations might result in data loss.</dl>
<p> <code>&#8211;root=</code></p>
<dl>
<dt>
<dd> When used with <code>enable</code>/<code>disable</code>/<code>is-enabled</code> (and related commands), use alternative root path when looking for unit files.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> When used with <code>enable</code>/<code>disable</code>/<code>is-enabled</code> (and related commands), make changes only temporarily, so that they are dropped on the next reboot. This will have the effect that changes are not made in subdirectories of /etc but in /run, with identical immediate effects, however, since the latter is lost on reboot, the changes are lost too.</dl>
<p> <code>-H</code>, <code>&#8211;host</code></p>
<dl>
<dt>
<dd> Execute operation remotely. Specify a hostname, or username and hostname separated by @, to connect to. This will use SSH to talk to the remote systemd instance.</dl>
<p> <code>-P</code>, <code>&#8211;privileged</code></p>
<dl>
<dt>
<dd> Acquire privileges via PolicyKit before executing the operation.</dl>
<p> <code>&#8211;lines=</code>, <code>-n</code></p>
<dl>
<dt>
<dd> When used with <code>status</code> controls the number of journal lines to show, counting from the most recent ones. Takes a positive integer argument. Defaults to 10.</dl>
<p> <code>&#8211;follow</code>, <code>-f</code></p>
<dl>
<dt>
<dd> When used with <code>status</code> continously prints new journal entries as they are appended to the journal.</dl>
<p> <code>&#8211;output=</code>, <code>-o</code></p>
<dl>
<dt>
<dd> When used with <code>status</code> controls the formatting of the journal entries that are shown. For the available choices see <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1). Defaults to short.</dl>
<p> The following commands are understood: </p>
<p> <code>list-units</code></p>
<dl>
<dt>
<dd> List known units.</dl>
<p> <code>start [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Start (activate) one or more units specified on the command line.</dl>
<p> <code>stop [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Stop (deactivate) one or more units specified on the command line.</dl>
<p> <code>reload [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Asks all units listed on the command line to reload their configuration. Note that this will reload the service-specific configuration, not the unit configuration file of systemd. If you want systemd to reload the configuration file of a unit use the <code>daemon-reload</code> command. In other words: for the example case of Apache, this will reload Apache&#8217;s httpd.conf in the web server, not the apache.service systemd unit file. </p>
<p> This command should not be confused with the <code>daemon-reload</code> or <code>load</code> commands.</dl>
<p> <code>restart [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Restart one or more units specified on the command line. If the units are not running yet they will be started.</dl>
<p> <code>try-restart [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Restart one or more units specified on the command line if the units are running. Do nothing if units are not running. Note that for compatibility with Red Hat init scripts <code>condrestart</code> is equivalent to this command.</dl>
<p> <code>reload-or-restart [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Reload one or more units if they support it. If not, restart them instead. If the units are not running yet they will be started.</dl>
<p> <code>reload-or-try-restart [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Reload one or more units if they support it. If not, restart them instead. Do nothing if the units are not running. Note that for compatibility with SysV init scripts <code>force-reload</code> is equivalent to this command.</dl>
<p> <code>isolate [NAME]</code></p>
<dl>
<dt>
<dd> Start the unit specified on the command line and its dependencies and stop all others. </p>
<p> This is similar to changing the runlevel in a traditional init system. The <code>isolate</code> command will immediately stop processes that are not enabled in the new unit, possibly including the graphical environment or terminal you are currently using. </p>
<p> Note that this works only on units where <code>AllowIsolate=</code> is enabled. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details.</dl>
<p> <code>kill [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Send a signal to one or more processes of the unit. Use <code>&#8211;kill-who=</code> to select which process to kill. Use <code>&#8211;kill-mode=</code> to select the kill mode and <code>&#8211;signal=</code> to select the signal to send.</dl>
<p> <code>is-active [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Check whether any of the specified units are active (i.e. running). Returns an exit code 0 if at least one is active, non-zero otherwise. Unless <code>&#8211;quiet</code> is specified this will also print the current unit state to STDOUT.</dl>
<p> <code>status [NAME&#8230;|PID&#8230;]</code></p>
<dl>
<dt>
<dd> Show terse runtime status information about one or more units, followed by its most recent log data from the journal. This function is intended to generate human-readable output. If you are looking for computer-parsable output, use <code>show</code> instead. If a PID is passed information about the unit the process of the PID belongs to is shown.</dl>
<p> <code>show [NAME&#8230;|JOB&#8230;]</code></p>
<dl>
<dt>
<dd> Show properties of one or more units, jobs or the manager itself. If no argument is specified properties of the manager will be shown. If a unit name is specified properties of the unit is shown, and if a job id is specified properties of the job is shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>status</code> if you are looking for formatted human-readable output.</dl>
<p> <code>help [NAME&#8230;|PID&#8230;]</code></p>
<dl>
<dt>
<dd> Show manual pages for one or more units, if available. If a PID is passed the manual pages for the unit the process of the PID belongs to is shown.</dl>
<p> <code>reset-failed [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Reset the &#8216;failed&#8217; state of the specified units, or if no unit name is passed of all units. When a unit fails in some way (i.e. process exiting with non-zero error code, terminating abnormally or timing out) it will automatically enter the &#8216;failed&#8217; state and its exit code and status is recorded for introspection by the administrator until the service is restarted or reset with this command.</dl>
<p> <code>list-unit-files</code></p>
<dl>
<dt>
<dd> List installed unit files.</dl>
<p> <code>enable [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Enable one or more unit files or unit file instances, as specified on the command line. This will create a number of symlinks as encoded in the [Install] sections of the unit files. After the symlinks have been created the systemd configuration is reloaded (in a way that is equivalent to <code>daemon-reload</code>) to ensure the changes are taken into account immediately. Note that this does not have the effect that any of the units enabled are also started at the same time. If this is desired a separate <code>start</code> command must be invoked for the unit. Also note that in case of instance enablement, symlinks named same as instances are created in install location, however they all point to the same template unit file. </p>
<p> This command will print the actions executed. This output may be suppressed by passing <code>&#8211;quiet</code>. </p>
<p> Note that this operation creates only the suggested symlinks for the units. While this command is the recommended way to manipulate the unit configuration directory, the administrator is free to make additional changes manually, by placing or removing symlinks in the directory. This is particularly useful to create configurations that deviate from the suggested default installation. In this case the administrator must make sure to invoke <code>daemon-reload</code> manually as necessary, to ensure his changes are taken into account. </p>
<p> Enabling units should not be confused with starting (activating) units, as done by the <code>start</code> command. Enabling and starting units is orthogonal: units may be enabled without being started and started without being enabled. Enabling simply hooks the unit into various suggested places (for example, so that the unit is automatically started on boot or when a particular kind of hardware is plugged in). Starting actually spawns the daemon process (in case of service units), or binds the socket (in case of socket units), and so on. </p>
<p> Depending on whether <code>&#8211;system</code>, <code>&#8211;user</code> or <code>&#8211;global</code> is specified this enables the unit for the system, for the calling user only or for all future logins of all users. Note that in the latter case no systemd daemon configuration is reloaded.</dl>
<p> <code>disable [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Disables one or more units. This removes all symlinks to the specified unit files from the unit configuration directory, and hence undoes the changes made by <code>enable</code>. Note however that this removes all symlinks to the unit files (i.e. including manual additions), not just those actually created by <code>enable</code>. This call implicitly reloads the systemd daemon configuration after completing the disabling of the units. Note that this command does not implicitly stop the units that is being disabled. If this is desired an additional <code>stop</code> command should be executed afterwards. </p>
<p> This command will print the actions executed. This output may be suppressed by passing <code>&#8211;quiet</code>. </p>
<p> This command honors <code>&#8211;system</code>, <code>&#8211;user</code>, <code>&#8211;global</code> in a similar way as <code>enable</code>.</dl>
<p> <code>is-enabled [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Checks whether any of the specified unit files is enabled (as with <code>enable</code>). Returns an exit code of 0 if at least one is enabled, non-zero otherwise. Prints the current enable status. To suppress this output use <code>&#8211;quiet</code>.</dl>
<p> <code>reenable [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Reenable one or more unit files, as specified on the command line. This is a combination of <code>disable</code> and <code>enable</code> and is useful to reset the symlinks a unit is enabled with to the defaults configured in the [Install] section of the unit file.</dl>
<p> <code>preset [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Reset one or more unit files, as specified on the command line, to the defaults configured in a preset file. This has the same effect as <code>disable</code> or <code>enable</code>, depending how the unit is listed in the preset files.</dl>
<p> <code>mask [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Mask one or more unit files, as specified on the command line. This will link these units to /dev/null, making it impossible to start them. This is a stronger version of <code>disable</code>, since it prohibits all kinds of activation of the unit, including manual activation. Use this option with care.</dl>
<p> <code>unmask [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Unmask one or more unit files, as specified on the command line. This will undo the effect of <code>mask</code>.</dl>
<p> <code>link [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Link a unit file that is not in the unit file search paths into the unit file search path. This requires an absolute path to a unit file. The effect of this can be undone with <code>disable</code>. The effect of this command is that a unit file is available for <code>start</code> and other commands although it isn&#8217;t installed directly in the unit search path.</dl>
<p> <code>load [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Load one or more units specified on the command line. This will simply load their configuration from disk, but not start them. To start them you need to use the <code>start</code> command which will implicitly load a unit that has not been loaded yet. Note that systemd garbage collects loaded units that are not active or referenced by an active unit. This means that units loaded this way will usually not stay loaded for long. Also note that this command cannot be used to reload unit configuration. Use the <code>daemon-reload</code> command for that. All in all, this command is of little use except for debugging. </p>
<p> This command should not be confused with the <code>daemon-reload</code> or <code>reload</code> commands.</dl>
<p> <code>list-jobs</code></p>
<dl>
<dt>
<dd> List jobs that are in progress.</dl>
<p> <code>cancel [JOB&#8230;]</code></p>
<dl>
<dt>
<dd> Cancel one or more jobs specified on the command line by their numeric job IDs. If no job id is specified, cancel all pending jobs.</dl>
<p> <code>dump</code></p>
<dl>
<dt>
<dd> Dump server status. This will output a (usually very long) human readable manager status dump. Its format is subject to change without notice and should not be parsed by applications.</dl>
<p> <code>dot</code></p>
<dl>
<dt>
<dd> Generate textual dependency graph description in dot format for further processing with the GraphViz <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1) tool. Use a command line like <code>systemctl dot | dot -Tsvg &gt; systemd.svg</code> to generate a graphical dependency tree. Unless <code>&#8211;order</code> or <code>&#8211;require</code> is passed the generated graph will show both ordering and requirement dependencies.</dl>
<p> <code>snapshot [NAME]</code></p>
<dl>
<dt>
<dd> Create a snapshot. If a snapshot name is specified, the new snapshot will be named after it. If none is specified an automatic snapshot name is generated. In either case, the snapshot name used is printed to STDOUT, unless <code>&#8211;quiet</code> is specified. </p>
<p> A snapshot refers to a saved state of the systemd manager. It is implemented itself as a unit that is generated dynamically with this command and has dependencies on all units active at the time. At a later time the user may return to this state by using the <code>isolate</code> command on the snapshot unit. </p>
<p> Snapshots are only useful for saving and restoring which units are running or are stopped, they do not save/restore any other state. Snapshots are dynamic and lost on reboot.</dl>
<p> <code>delete [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Remove a snapshot previously created with <code>snapshot</code>.</dl>
<p> <code>daemon-reload</code></p>
<dl>
<dt>
<dd> Reload systemd manager configuration. This will reload all unit files and recreate the entire dependency tree. While the daemon is reloaded, all sockets systemd listens on on behalf of user configuration will stay accessible. </p>
<p> This command should not be confused with the <code>load</code> or <code>reload</code> commands.</dl>
<p> <code>daemon-reexec</code></p>
<dl>
<dt>
<dd> Reexecute the systemd manager. This will serialize the manager state, reexecute the process and deserialize the state again. This command is of little use except for debugging and package upgrades. Sometimes it might be helpful as a heavy-weight <code>daemon-reload</code>. While the daemon is reexecuted all sockets systemd listens on on behalf of user configuration will stay accessible.</dl>
<p> <code>show-environment</code></p>
<dl>
<dt>
<dd> Dump the systemd manager environment block. The environment block will be dumped in straight-forward form suitable for sourcing into a shell script. This environment block will be passed to all processes the manager spawns.</dl>
<p> <code>set-environment [NAME=VALUE&#8230;]</code></p>
<dl>
<dt>
<dd> Set one or more systemd manager environment variables, as specified on the command line.</dl>
<p> <code>unset-environment [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Unset one or more systemd manager environment variables. If only a variable name is specified it will be removed regardless of its value. If a variable and a value are specified the variable is only removed if it has the specified value.</dl>
<p> <code>default</code></p>
<dl>
<dt>
<dd> Enter default mode. This is mostly equivalent to <code>start default.target</code>.</dl>
<p> <code>rescue</code></p>
<dl>
<dt>
<dd> Enter rescue mode. This is mostly equivalent to <code>isolate rescue.target</code> but also prints a wall message to all users.</dl>
<p> <code>emergency</code></p>
<dl>
<dt>
<dd> Enter emergency mode. This is mostly equivalent to <code>isolate emergency.target</code> but also prints a wall message to all users.</dl>
<p> <code>halt</code></p>
<dl>
<dt>
<dd> Shut down and halt the system. This is mostly equivalent to <code>start halt.target</code> but also prints a wall message to all users. If combined with <code>&#8211;force</code> shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the system halt. If <code>&#8211;force</code> is specified twice the the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss.</dl>
<p> <code>poweroff</code></p>
<dl>
<dt>
<dd> Shut down and power-off the system. This is mostly equivalent to <code>start poweroff.target</code> but also prints a wall message to all users. If combined with <code>&#8211;force</code> shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the powering off. If <code>&#8211;force</code> is specified twice the the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss.</dl>
<p> <code>reboot</code></p>
<dl>
<dt>
<dd> Shut down and reboot the system. This is mostly equivalent to <code>start reboot.target</code> but also prints a wall message to all users. If combined with <code>&#8211;force</code> shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the reboot. If <code>&#8211;force</code> is specified twice the the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss.</dl>
<p> <code>kexec</code></p>
<dl>
<dt>
<dd> Shut down and reboot the system via kexec. This is mostly equivalent to <code>start kexec.target</code> but also prints a wall message to all users. If combined with <code>&#8211;force</code> shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the reboot.</dl>
<p> <code>exit</code></p>
<dl>
<dt>
<dd> Ask the systemd manager to quit. This is only supported for user service managers (i.e. in conjunction with the <code>&#8211;user</code> option) and will fail otherwise.</dl>
<p> <code>suspend</code></p>
<dl>
<dt>
<dd> Suspend the system.</dl>
<p> <code>hibernate</code></p>
<dl>
<dt>
<dd> Hibernate the system.</dl>
<p> <code>switch-root [ROOT] [INIT]</code></p>
<dl>
<dt>
<dd> Switches to a different root directory and executes a new system manager process below it. This is intended for usage in initial RAM disks (&quot;initrd&quot;), and will transition from the initrd&#8217;s system manager process (a.k.a &quot;init&quot; process) to the main system manager process. Takes two arguments: the directory to make the new root directory, and the path to the new system manager binary below it to execute as PID 1. If the latter is ommitted or the empty string, a systemd binary will automatically be searched for and used as init. If the system manager path is ommitted or equal the empty string the state of the initrd&#8217;s system manager process is passed to the main system manager, which allows later introspection of the state of the services involved in the initrd boot.</dl>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>ENVIRONMENT</h2>
<p> <i>$SYSTEMD_PAGER</i></p>
<dl>
<dt>
<dd> Pager to use when <code>&#8211;no-pager</code> is not given; overrides <i>$PAGER</i>. Setting this to an empty string or the value cat is equivalent to passing <code>&#8211;no-pager</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemadm/">systemadm</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/1-loginctl/">loginctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Lennart Poettering</code> &lt;lennart [at] poettering.net&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<h2>Index</h2>
