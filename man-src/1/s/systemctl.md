---
title: "systemctl(1)"
name: "systemctl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemctl/"
description: "systemctl – Control the systemd system and service manager"
---

<h2 class="name">NAME</h2>
<p> systemctl &#8211; Control the systemd system and service manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemctl</code> [OPTIONS&#8230;] COMMAND [UNIT&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemctl</code></p>
<dd>may be used to introspect and control the state of the &quot;systemd&quot; system and service manager. Please refer to <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) for an introduction into the basic concepts and functionality this tool manages.</p>
<h2>COMMANDS</h2>
<p> The following commands are understood:</p>
<h3>Unit Commands (Introspection and Modification)</h3>
<p> <code>list-units</code> [<i>PATTERN</i>&#8230;]</p>
<dl>
<dt>
<dd> List units that <code>systemd</code> currently has in memory. This includes units that are either referenced directly or through a dependency, units that are pinned by applications programmatically, or units that were active in the past and have failed. By default only units which are active, have pending jobs, or have failed are shown; this can be changed with option <code>&#8211;all</code>. If one or more <i>PATTERN</i>s are specified, only units matching one of them are shown. The units that are shown are additionally filtered by <code>&#8211;type=</code> and <code>&#8211;state=</code> if those options are specified. </p>
<p> Note that this command does not show unit templates, but only instances of unit templates. Units templates that aren&#8217;t instantiated are not runnable, and will thus never show up in the output of this command. Specifically this means that foo [at] .service will never be shown in this list &#8212; unless instantiated, e.g. as foo [at] bar.service. Use <code>list-unit-files</code> (see below) for listing installed unit template files. </p>
<p> Produces output similar to </p>
<dl>
<dt>
<dd>
<pre><code>
  UNIT                         LOAD   ACTIVE SUB     DESCRIPTION
  sys-module-fuse.device       loaded active plugged /sys/module/fuse
  -.mount                      loaded active mounted Root Mount
  boot-efi.mount               loaded active mounted /boot/efi
  systemd-journald.service     loaded active running Journal Service
  systemd-logind.service       loaded active running Login Service
● user [at] 1000.service            loaded failed failed  User Manager for UID 1000
  ...
  systemd-tmpfiles-clean.timer loaded active waiting Daily Cleanup of Temporary Directories
LOAD   = Reflects whether the unit definition was properly loaded.
ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
SUB    = The low-level unit activation state, values depend on unit type.
123 loaded units listed. Pass --all to see loaded but inactive units, too.
To show all installed unit files use 'systemctl list-unit-files'.
</code></pre>
</dl>
<p> The header and the last unit of a given type are underlined if the terminal supports that. A colored dot is shown next to services which were masked, not found, or otherwise failed. </p>
<p> The LOAD column shows the load state, one of <code>loaded</code>, <code>not-found</code>, <code>bad-setting</code>, <code>error</code>, <code>masked</code>. The ACTIVE columns shows the general unit state, one of <code>active</code>, <code>reloading</code>, <code>inactive</code>, <code>failed</code>, <code>activating</code>, <code>deactivating</code>. The SUB column shows the unit-type-specific detailed state of the unit, possible values vary by unit type. The list of possible LOAD, ACTIVE, and SUB states is not constant and new systemd releases may both add and remove values. </p>
<dl>
<dt>
<dd>
<pre>
systemctl --state=help
</pre>
</dl>
<p> command maybe be used to display the current set of possible values. </p>
<p> This is the default command.</dl>
<p> <code>list-sockets</code> [<i>PATTERN</i>&#8230;]</p>
<dl>
<dt>
<dd> List socket units currently in memory, ordered by listening address. If one or more <i>PATTERN</i>s are specified, only socket units matching one of them are shown. Produces output similar to </p>
<dl>
<dt>
<dd>
<pre>
LISTEN           UNIT                        ACTIVATES
/dev/initctl     systemd-initctl.socket      systemd-initctl.service
...
[::]:22          sshd.socket                 sshd.service
kobject-uevent 1 systemd-udevd-kernel.socket systemd-udevd.service
5 sockets listed.
</pre>
</dl>
<p> Note: because the addresses might contains spaces, this output is not suitable for programmatic consumption. </p>
<p> Also see <code>&#8211;show-types</code>, <code>&#8211;all</code>, and <code>&#8211;state=</code>.</dl>
<p> <code>list-timers</code> [<i>PATTERN</i>&#8230;]</p>
<dl>
<dt>
<dd> List timer units currently in memory, ordered by the time they elapse next. If one or more <i>PATTERN</i>s are specified, only units matching one of them are shown. Produces output similar to </p>
<dl>
<dt>
<dd>
<pre>
NEXT                         LEFT          LAST                         PASSED     UNIT                         ACTIVATES
n/a                          n/a           Thu 2017-02-23 13:40:29 EST  3 days ago ureadahead-stop.timer        ureadahead-stop.service
Sun 2017-02-26 18:55:42 EST  1min 14s left Thu 2017-02-23 13:54:44 EST  3 days ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Sun 2017-02-26 20:37:16 EST  1h 42min left Sun 2017-02-26 11:56:36 EST  6h ago     apt-daily.timer              apt-daily.service
Sun 2017-02-26 20:57:49 EST  2h 3min left  Sun 2017-02-26 11:56:36 EST  6h ago     snapd.refresh.timer          snapd.refresh.service
            
</pre>
</dl>
<p> <i>NEXT</i> shows the next time the timer will run. </p>
<p> <i>LEFT</i> shows how long till the next time the timer runs. </p>
<p> <i>LAST</i> shows the last time the timer ran. </p>
<p> <i>PASSED</i> shows how long has passed since the timer last ran. </p>
<p> <i>UNIT</i> shows the name of the timer </p>
<p> <i>ACTIVATES</i> shows the name the service the timer activates when it runs. </p>
<p> Also see <code>&#8211;all</code> and <code>&#8211;state=</code>.</dl>
<p> <code>is-active </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Check whether any of the specified units are active (i.e. running). Returns an exit code <code>0</code> if at least one is active, or non-zero otherwise. Unless <code>&#8211;quiet</code> is specified, this will also print the current unit state to standard output.</dl>
<p> <code>is-failed </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Check whether any of the specified units are in a &quot;failed&quot; state. Returns an exit code <code>0</code> if at least one has failed, non-zero otherwise. Unless <code>&#8211;quiet</code> is specified, this will also print the current unit state to standard output.</dl>
<p> <code>status</code> [<i>PATTERN</i>&#8230;|<i>PID</i>&#8230;]]</p>
<dl>
<dt>
<dd> Show terse runtime status information about one or more units, followed by most recent log data from the journal. If no units are specified, show system status. If combined with <code>&#8211;all</code>, also show the status of all units (subject to limitations specified with <code>-t</code>). If a PID is passed, show information about the unit the process belongs to. </p>
<p> This function is intended to generate human-readable output. If you are looking for computer-parsable output, use <code>show</code> instead. By default, this function only shows 10 lines of output and ellipsizes lines to fit in the terminal window. This can be changed with <code>&#8211;lines</code> and <code>&#8211;full</code>, see above. In addition, <code>journalctl &#8211;unit=</code><i>NAME</i> or <code>journalctl &#8211;user-unit=</code><i>NAME</i> use a similar filter for messages and might be more convenient. </p>
<p> systemd implicitly loads units as necessary, so just running the <code>status</code> will attempt to load a file. The command is thus not useful for determining if something was already loaded or not. The units may possibly also be quickly unloaded after the operation is completed if there&#8217;s no reason to keep it in memory thereafter. </p>
<p> <code>Example 1. Example output from systemctl status</code> </p>
<dl>
<dt>
<dd>
<pre><code>
$ systemctl status bluetooth
● bluetooth.service - Bluetooth service Loaded : loaded(/ lib / systemd / system / bluetooth.service; enabled; vendor preset
                                                         : enabled) Active : active(running) since Wed 2017 -
                                                                             01 - 04 13 : 54 : 04 EST;
1 weeks 0 days ago
            Docs : man : bluetoothd(8)
                             Main PID : 930(bluetoothd)
                                 Status : "Running" Tasks : 1 Memory : 648.0K CPU : 435ms CGroup : /
                                                                                                   system.slice / bluetooth.service
           └─930 / usr / lib / bluetooth / bluetoothd Jan 12 10 : 46 : 45 example.com bluetoothd[8900] : Not enough free handles to register service Jan 12 10 : 46 : 45 example.com bluetoothd[8900] : Current Time Service could not be registered Jan 12 10 : 46 : 45 example.com bluetoothd[8900] : gatt
    - time - server : Input / output error(5)
</code></pre>
</dl>
<p> The dot (&quot;●&quot;) uses color on supported terminals to summarize the unit state at a glance. Along with its color, its shape varies according to its state: &quot;inactive&quot; or &quot;maintenance&quot; is a white circle (&quot;○&quot;), &quot;active&quot; is a green dot (&quot;●&quot;), &quot;deactivating&quot; is a white dot, &quot;failed&quot; or &quot;error&quot; is a red cross (&quot;&#215;&quot;), and &quot;reloading&quot; is a green clockwise circle arrow (&quot;↻&quot;). </p>
<p> The &quot;Loaded:&quot; line in the output will show &quot;loaded&quot; if the unit has been loaded into memory. Other possible values for &quot;Loaded:&quot; include: &quot;error&quot; if there was a problem loading it, &quot;not-found&quot; if no unit file was found for this unit, &quot;bad-setting&quot; if an essential unit file setting could not be parsed and &quot;masked&quot; if the unit file has been masked. Along with showing the path to the unit file, this line will also show the enablement state. Enabled commands start at boot. See the full table of possible enablement states &#8212; including the definition of &quot;masked&quot; &#8212; in the documentation for the <code>is-enabled</code> command. </p>
<p> The &quot;Active:&quot; line shows active state. The value is usually &quot;active&quot; or &quot;inactive&quot;. Active could mean started, bound, plugged in, etc depending on the unit type. The unit could also be in process of changing states, reporting a state of &quot;activating&quot; or &quot;deactivating&quot;. A special &quot;failed&quot; state is entered when the service failed in some way, such as a crash, exiting with an error code or timing out. If the failed state is entered the cause will be logged for later reference.</dl>
<p> <code>show</code> [<i>PATTERN</i>&#8230;|<i>JOB</i>&#8230;]</p>
<dl>
<dt>
<dd> Show properties of one or more units, jobs, or the manager itself. If no argument is specified, properties of the manager will be shown. If a unit name is specified, properties of the unit are shown, and if a job ID is specified, properties of the job are shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show, use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>status</code> if you are looking for formatted human-readable output. </p>
<p> Many properties shown by <code>systemctl show</code> map directly to configuration settings of the system and service manager and its unit files. Note that the properties shown by the command are generally more low-level, normalized versions of the original configuration settings and expose runtime state in addition to configuration. For example, properties shown for service units include the service&#8217;s current main process identifier as &quot;MainPID&quot; (which is runtime state), and time settings are always exposed as properties ending in the &quot;&#8230;USec&quot; suffix even if a matching configuration options end in &quot;&#8230;Sec&quot;, because microseconds is the normalized time unit used internally by the system and service manager. </p>
<p> For details about many of these properties, see the documentation of the D-Bus interface backing these properties, see <code><a href="/docs/linux/man/5-org-freedesktop-systemd1/">org.freedesktop.systemd1</a></code>(5).</dl>
<p> <code>cat </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Show backing files of one or more units. Prints the &quot;fragment&quot; and &quot;drop-ins&quot; (source files) of units. Each file is preceded by a comment which includes the file name. Note that this shows the contents of the backing files on disk, which may not match the system manager&#8217;s understanding of these units if any unit files were updated on disk and the <code>daemon-reload</code> command wasn&#8217;t issued since.</dl>
<p> <code>help </code><i>PATTERN</i><code>&#8230;|</code><i>PID</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Show manual pages for one or more units, if available. If a PID is given, the manual pages for the unit the process belongs to are shown.</dl>
<p> <code>list-dependencies</code> [<i>UNIT</i>&#8230;]</p>
<dl>
<dt>
<dd> Shows units required and wanted by the specified units. This recursively lists units following the <i>Requires=</i>, <i>Requisite=</i>, <i>ConsistsOf=</i>, <i>Wants=</i>, <i>BindsTo=</i> dependencies. If no units are specified, default.target is implied. </p>
<p> By default, only target units are recursively expanded. When <code>&#8211;all</code> is passed, all other units are recursively expanded as well. </p>
<p> Options <code>&#8211;reverse</code>, <code>&#8211;after</code>, <code>&#8211;before</code> may be used to change what types of dependencies are shown. </p>
<p> Note that this command only lists units currently loaded into memory by the service manager. In particular, this command is not suitable to get a comprehensive list at all reverse dependencies on a specific unit, as it won&#8217;t list the dependencies declared by units currently not loaded.</dl>
<p> <code>start </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Start (activate) one or more units specified on the command line. </p>
<p> Note that unit glob patterns expand to names of units currently in memory. Units which are not active and are not in a failed state usually are not in memory, and will not be matched by any pattern. In addition, in case of instantiated units, systemd is often unaware of the instance name until the instance has been started. Therefore, using glob patterns with <code>start</code> has limited usefulness. Also, secondary alias names of units are not considered. </p>
<p> Option <code>&#8211;all</code> may be used to also operate on inactive units which are referenced by other loaded units. Note that this is not the same as operating on &quot;all&quot; possible units, because as the previous paragraph describes, such a list is ill-defined. Nevertheless, <code>systemctl start &#8211;all </code><i>GLOB</i> may be useful if all the units that should match the pattern are pulled in by some target which is known to be loaded.</dl>
<p> <code>stop </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Stop (deactivate) one or more units specified on the command line. </p>
<p> This command will fail if the unit does not exist or if stopping of the unit is prohibited (see <i>RefuseManualStop=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5)). It will <i>not</i> fail if any of the commands configured to stop the unit (<i>ExecStop=</i>, etc.) fail, because the manager will still forcibly terminate the unit.</dl>
<p> <code>reload </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Asks all units listed on the command line to reload their configuration. Note that this will reload the service-specific configuration, not the unit configuration file of systemd. If you want systemd to reload the configuration file of a unit, use the <code>daemon-reload</code> command. In other words: for the example case of Apache, this will reload Apache&#8217;s httpd.conf in the web server, not the apache.service systemd unit file. </p>
<p> This command should not be confused with the <code>daemon-reload</code> command.</dl>
<p> <code>restart </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Stop and then start one or more units specified on the command line. If the units are not running yet, they will be started. </p>
<p> Note that restarting a unit with this command does not necessarily flush out all of the unit&#8217;s resources before it is started again. For example, the per-service file descriptor storage facility (see <i>FileDescriptorStoreMax=</i> in <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5)) will remain intact as long as the unit has a job pending, and is only cleared when the unit is fully stopped and no jobs are pending anymore. If it is intended that the file descriptor store is flushed out, too, during a restart operation an explicit <code>systemctl stop</code> command followed by <code>systemctl start</code> should be issued.</dl>
<p> <code>try-restart </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Stop and then start one or more units specified on the command line if the units are running. This does nothing if units are not running.</dl>
<p> <code>reload-or-restart </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Reload one or more units if they support it. If not, stop and then start them instead. If the units are not running yet, they will be started.</dl>
<p> <code>try-reload-or-restart </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Reload one or more units if they support it. If not, stop and then start them instead. This does nothing if the units are not running.</dl>
<p> <code>isolate </code><i>UNIT</i></p>
<dl>
<dt>
<dd> Start the unit specified on the command line and its dependencies and stop all others, unless they have <code>IgnoreOnIsolate=yes</code> (see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5)). If a unit name with no extension is given, an extension of &quot;.target&quot; will be assumed. </p>
<p> This command is dangerous, since it will immediately stop processes that are not enabled in the new target, possibly including the graphical environment or terminal you are currently using. </p>
<p> Note that this is allowed only on units where <code>AllowIsolate=</code> is enabled. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details.</dl>
<p> <code>kill </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Send a signal to one or more processes of the unit. Use <code>&#8211;kill-who=</code> to select which process to kill. Use <code>&#8211;signal=</code> to select the signal to send.</dl>
<p> <code>clean </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Remove the configuration, state, cache, logs or runtime data of the specified units. Use <code>&#8211;what=</code> to select which kind of resource to remove. For service units this may be used to remove the directories configured with <i>ConfigurationDirectory=</i>, <i>StateDirectory=</i>, <i>CacheDirectory=</i>, <i>LogsDirectory=</i> and <i>RuntimeDirectory=</i>, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details. For timer units this may be used to clear out the persistent timestamp data if <i>Persistent=</i> is used and <code>&#8211;what=state</code> is selected, see <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5). This command only applies to units that use either of these settings. If <code>&#8211;what=</code> is not specified, both the cache and runtime data are removed (as these two types of data are generally redundant and reproducible on the next invocation of the unit).</dl>
<p> <code>freeze </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Freeze one or more units specified on the command line using cgroup freezer </p>
<p> Freezing the unit will cause all processes contained within the cgroup corresponding to the unit to be suspended. Being suspended means that unit&#8217;s processes won&#8217;t be scheduled to run on CPU until thawed. Note that this command is supported only on systems that use unified cgroup hierarchy. Unit is automatically thawed just before we execute a job against the unit, e.g. before the unit is stopped.</dl>
<p> <code>thaw </code><i>PATTERN</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Thaw (unfreeze) one or more units specified on the command line. </p>
<p> This is the inverse operation to the <code>freeze</code> command and resumes the execution of processes in the unit&#8217;s cgroup.</dl>
<p> <code>set-property </code><i>UNIT</i><i>PROPERTY</i><code>=</code><i>VALUE</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Set the specified unit properties at runtime where this is supported. This allows changing configuration parameter properties such as resource control settings at runtime. Not all properties may be changed at runtime, but many resource control settings (primarily those in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5)) may. The changes are applied immediately, and stored on disk for future boots, unless <code>&#8211;runtime</code> is passed, in which case the settings only apply until the next reboot. The syntax of the property assignment follows closely the syntax of assignments in unit files. </p>
<p> Example: <code>systemctl set-property foobar.service CPUWeight=200</code> </p>
<p> If the specified unit appears to be inactive, the changes will be only stored on disk as described previously hence they will be effective when the unit will be started. </p>
<p> Note that this command allows changing multiple properties at the same time, which is preferable over setting them individually. </p>
<p> Example: <code>systemctl set-property foobar.service CPUWeight=200 MemoryMax=2G IPAccounting=yes</code> </p>
<p> Like with unit file configuration settings, assigning an empty setting usually resets a property to its defaults. </p>
<p> Example: <code>systemctl set-property avahi-daemon.service IPAddressDeny=</code></dl>
<p> <code>bind</code> <i>UNIT</i> <i>PATH</i> [<i>PATH</i>]</p>
<dl>
<dt>
<dd> Bind-mounts a file or directory from the host into the specified unit&#8217;s mount namespace. The first path argument is the source file or directory on the host, the second path argument is the destination file or directory in the unit&#8217;s mount namespace. When the latter is omitted, the destination path in the unit&#8217;s mount namespace is the same as the source path on the host. When combined with the <code>&#8211;read-only</code> switch, a ready-only bind mount is created. When combined with the <code>&#8211;mkdir</code> switch, the destination path is first created before the mount is applied. </p>
<p> Note that this option is currently only supported for units that run within a mount namespace (e.g.: with <code>RootImage=</code>, <code>PrivateMounts=</code>, etc.). This command supports bind-mounting directories, regular files, device nodes, <code>AF_UNIX</code> socket nodes, as well as FIFOs. The bind mount is ephemeral, and it is undone as soon as the current unit process exists. Note that the namespace mentioned here, where the bind mount will be added to, is the one where the main service process runs. Other processes (those exececuted by <code>ExecReload=</code>, <code>ExecStartPre=</code>, etc.) run in distinct namespaces.</dl>
<p> <code>mount-image</code> <i>UNIT</i> <i>IMAGE</i> [<i>PATH</i> [<i>PARTITION_NAME</i>:<i>MOUNT_OPTIONS</i>]]</p>
<dl>
<dt>
<dd> Mounts an image from the host into the specified unit&#8217;s mount namespace. The first path argument is the source image on the host, the second path argument is the destination directory in the unit&#8217;s mount namespace (i.e. inside <code>RootImage=</code>/<code>RootDirectory=</code>). The following argument, if any, is interpreted as a colon-separated tuple of partition name and comma-separated list of mount options for that partition. The format is the same as the service <code>MountImages=</code> setting. When combined with the <code>&#8211;read-only</code> switch, a ready-only mount is created. When combined with the <code>&#8211;mkdir</code> switch, the destination path is first created before the mount is applied. </p>
<p> Note that this option is currently only supported for units that run within a mount namespace (i.e. with <code>RootImage=</code>, <code>PrivateMounts=</code>, etc.). Note that the namespace mentioned here where the image mount will be added to, is the one where the main service process runs. Note that the namespace mentioned here, where the bind mount will be added to, is the one where the main service process runs. Other processes (those exececuted by <code>ExecReload=</code>, <code>ExecStartPre=</code>, etc.) run in distinct namespaces. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
systemctl mount-image foo.service /tmp/img.raw /var/lib/image root:ro,nosuid
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
systemctl mount-image --mkdir bar.service /tmp/img.raw /var/lib/baz/img
</pre>
</dl>
</dl>
<p> <code>service-log-level</code> <i>SERVICE</i> [<i>LEVEL</i>]</p>
<dl>
<dt>
<dd> If the <i>LEVEL</i> argument is not given, print the current log level as reported by service <i>SERVICE</i>. </p>
<p> If the optional argument <i>LEVEL</i> is provided, then change the current log level of the service to <i>LEVEL</i>. The log level should be a typical syslog log level, i.e. a value in the range 0&#8230;7 or one of the strings <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code>; see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for details. </p>
<p> The service must have the appropriate <i>BusName=</i><i>destination</i> property and also implement the generic <code><a href="/docs/linux/man/5-org-freedesktop-logcontrol1/">org.freedesktop.LogControl1</a></code>(5) interface. (systemctl will use the generic D-Bus protocol to access the org.freedesktop.LogControl1.LogLevel interface for the D-Bus name <i>destination</i>.)</dl>
<p> <code>service-log-target</code> <i>SERVICE</i> [<i>TARGET</i>]</p>
<dl>
<dt>
<dd> If the <i>TARGET</i> argument is not given, print the current log target as reported by service <i>SERVICE</i>. </p>
<p> If the optional argument <i>TARGET</i> is provided, then change the current log target of the service to <i>TARGET</i>. The log target should be one of the strings <code>console</code> (for log output to the service&#8217;s standard error stream), <code>kmsg</code> (for log output to the kernel log buffer), <code>journal</code> (for log output to <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8) using the native journal protocol), <code>syslog</code> (for log output to the classic syslog socket /dev/log), <code>null</code> (for no log output whatsoever) or <code>auto</code> (for an automatically determined choice, typically equivalent to <code>console</code> if the service is invoked interactively, and <code>journal</code> or <code>syslog</code> otherwise). </p>
<p> For most services, only a small subset of log targets make sense. In particular, most &quot;normal&quot; services should only implement <code>console</code>, <code>journal</code>, and <code>null</code>. Anything else is only appropriate for low-level services that are active in very early boot before proper logging is established. </p>
<p> The service must have the appropriate <i>BusName=</i><i>destination</i> property and also implement the generic <code><a href="/docs/linux/man/5-org-freedesktop-logcontrol1/">org.freedesktop.LogControl1</a></code>(5) interface. (systemctl will use the generic D-Bus protocol to access the org.freedesktop.LogControl1.LogLevel interface for the D-Bus name <i>destination</i>.)</dl>
<p> <code>reset-failed [</code><i>PATTERN</i><code>&#8230;]</code></p>
<dl>
<dt>
<dd> Reset the &quot;failed&quot; state of the specified units, or if no unit name is passed, reset the state of all units. When a unit fails in some way (i.e. process exiting with non-zero error code, terminating abnormally or timing out), it will automatically enter the &quot;failed&quot; state and its exit code and status is recorded for introspection by the administrator until the service is stopped/re-started or reset with this command. </p>
<p> In addition to resetting the &quot;failed&quot; state of a unit it also resets various other per-unit properties: the start rate limit counter of all unit types is reset to zero, as is the restart counter of service units. Thus, if a unit&#8217;s start limit (as configured with <i>StartLimitIntervalSec=</i>/<i>StartLimitBurst=</i>) is hit and the unit refuses to be started again, use this command to make it startable again.</dl>
<h3>Unit File Commands</h3>
<p> <code>list-unit-files</code> [<i>PATTERN&#8230;</i>]</p>
<dl>
<dt>
<dd> List unit files installed on the system, in combination with their enablement state (as reported by <code>is-enabled</code>). If one or more <i>PATTERN</i>s are specified, only unit files whose name matches one of them are shown (patterns matching unit file system paths are not supported). </p>
<p> Unlike <code>list-units</code> this command will list template units in addition to explicitly instantiated units.</dl>
<p> <code>enable </code><i>UNIT</i><code>&#8230;</code>, <code>enable </code><i>PATH</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Enable one or more units or unit instances. This will create a set of symlinks, as encoded in the [Install] sections of the indicated unit files. After the symlinks have been created, the system manager configuration is reloaded (in a way equivalent to <code>daemon-reload</code>), in order to ensure the changes are taken into account immediately. Note that this does <i>not</i> have the effect of also starting any of the units being enabled. If this is desired, combine this command with the <code>&#8211;now</code> switch, or invoke <code>start</code> with appropriate arguments later. Note that in case of unit instance enablement (i.e. enablement of units of the form foo [at] bar.service), symlinks named the same as instances are created in the unit configuration directory, however they point to the single template unit file they are instantiated from. </p>
<p> This command expects either valid unit names (in which case various unit file directories are automatically searched for unit files with appropriate names), or absolute paths to unit files (in which case these files are read directly). If a specified unit file is located outside of the usual unit file directories, an additional symlink is created, linking it into the unit configuration path, thus ensuring it is found when requested by commands such as <code>start</code>. The file system where the linked unit files are located must be accessible when systemd is started (e.g. anything underneath /home/ or /var/ is not allowed, unless those directories are located on the root file system). </p>
<p> This command will print the file system operations executed. This output may be suppressed by passing <code>&#8211;quiet</code>. </p>
<p> Note that this operation creates only the symlinks suggested in the [Install] section of the unit files. While this command is the recommended way to manipulate the unit configuration directory, the administrator is free to make additional changes manually by placing or removing symlinks below this directory. This is particularly useful to create configurations that deviate from the suggested default installation. In this case, the administrator must make sure to invoke <code>daemon-reload</code> manually as necessary, in order to ensure the changes are taken into account. </p>
<p> Enabling units should not be confused with starting (activating) units, as done by the <code>start</code> command. Enabling and starting units is orthogonal: units may be enabled without being started and started without being enabled. Enabling simply hooks the unit into various suggested places (for example, so that the unit is automatically started on boot or when a particular kind of hardware is plugged in). Starting actually spawns the daemon process (in case of service units), or binds the socket (in case of socket units), and so on. </p>
<p> Depending on whether <code>&#8211;system</code>, <code>&#8211;user</code>, <code>&#8211;runtime</code>, or <code>&#8211;global</code> is specified, this enables the unit for the system, for the calling user only, for only this boot of the system, or for all future logins of all users. Note that in the last case, no systemd daemon configuration is reloaded. </p>
<p> Using <code>enable</code> on masked units is not supported and results in an error.</dl>
<p> <code>disable </code><i>UNIT</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Disables one or more units. This removes all symlinks to the unit files backing the specified units from the unit configuration directory, and hence undoes any changes made by <code>enable</code> or <code>link</code>. Note that this removes <i>all</i> symlinks to matching unit files, including manually created symlinks, and not just those actually created by <code>enable</code> or <code>link</code>. Note that while <code>disable</code> undoes the effect of <code>enable</code>, the two commands are otherwise not symmetric, as <code>disable</code> may remove more symlinks than a prior <code>enable</code> invocation of the same unit created. </p>
<p> This command expects valid unit names only, it does not accept paths to unit files. </p>
<p> In addition to the units specified as arguments, all units are disabled that are listed in the <i>Also=</i> setting contained in the [Install] section of any of the unit files being operated on. </p>
<p> This command implicitly reloads the system manager configuration after completing the operation. Note that this command does not implicitly stop the units that are being disabled. If this is desired, either combine this command with the <code>&#8211;now</code> switch, or invoke the <code>stop</code> command with appropriate arguments later. </p>
<p> This command will print information about the file system operations (symlink removals) executed. This output may be suppressed by passing <code>&#8211;quiet</code>. </p>
<p> This command honors <code>&#8211;system</code>, <code>&#8211;user</code>, <code>&#8211;runtime</code> and <code>&#8211;global</code> in a similar way as <code>enable</code>.</dl>
<p> <code>reenable </code><i>UNIT</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Reenable one or more units, as specified on the command line. This is a combination of <code>disable</code> and <code>enable</code> and is useful to reset the symlinks a unit file is enabled with to the defaults configured in its [Install] section. This command expects a unit name only, it does not accept paths to unit files.</dl>
<p> <code>preset </code><i>UNIT</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Reset the enable/disable status one or more unit files, as specified on the command line, to the defaults configured in the preset policy files. This has the same effect as <code>disable</code> or <code>enable</code>, depending how the unit is listed in the preset files. </p>
<p> Use <code>&#8211;preset-mode=</code> to control whether units shall be enabled and disabled, or only enabled, or only disabled. </p>
<p> If the unit carries no install information, it will be silently ignored by this command. <i>UNIT</i> must be the real unit name, any alias names are ignored silently. </p>
<p> For more information on the preset policy format, see <code><a href="/docs/linux/man/5-systemd-preset/">systemd.preset</a></code>(5).</dl>
<p> <code>preset-all</code></p>
<dl>
<dt>
<dd> Resets all installed unit files to the defaults configured in the preset policy file (see above). </p>
<p> Use <code>&#8211;preset-mode=</code> to control whether units shall be enabled and disabled, or only enabled, or only disabled.</dl>
<p> <code>is-enabled </code><i>UNIT</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Checks whether any of the specified unit files are enabled (as with <code>enable</code>). Returns an exit code of 0 if at least one is enabled, non-zero otherwise. Prints the current enable status (see table). To suppress this output, use <code>&#8211;quiet</code>. To show installation targets, use <code>&#8211;full</code>. </p>
<p> <code>Table 1.&nbsp; is-enabled output</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Description </code></td>
<td><code> Exit Code </code>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;enabled&quot; </td>
<td VALIGN=center ROWSPAN=2> Enabled via .wants/, .requires/ or <i>Alias=</i> symlinks (permanently in /etc/systemd/system/, or transiently in /run/systemd/system/). </td>
<td VALIGN=center ROWSPAN=2> 0
</td>
</tr>
<tr VALIGN=top>
<td> &quot;enabled-runtime&quot; </td>
</tr>
<tr VALIGN=top>
<td> &quot;linked&quot; </td>
<td VALIGN=center ROWSPAN=2> Made available through one or more symlinks to the unit file (permanently in /etc/systemd/system/ or transiently in /run/systemd/system/), even though the unit file might reside outside of the unit file search path. </td>
<td VALIGN=center ROWSPAN=2> &gt; 0
</td>
</tr>
<tr VALIGN=top>
<td> &quot;linked-runtime&quot; </td>
</tr>
<tr VALIGN=top>
<td> &quot;alias&quot; </td>
<td> The name is an alias (symlink to another unit file). </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> &quot;masked&quot; </td>
<td VALIGN=center ROWSPAN=2> Completely disabled, so that any start operation on it fails (permanently in /etc/systemd/system/ or transiently in /run/systemd/systemd/). </td>
<td VALIGN=center ROWSPAN=2> &gt; 0
</td>
</tr>
<tr VALIGN=top>
<td> &quot;masked-runtime&quot; </td>
</tr>
<tr VALIGN=top>
<td> &quot;static&quot; </td>
<td> The unit file is not enabled, and has no provisions for enabling in the [Install] unit file section. </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> &quot;indirect&quot; </td>
<td> The unit file itself is not enabled, but it has a non-empty <i>Also=</i> setting in the [Install] unit file section, listing other unit files that might be enabled, or it has an alias under a different name through a symlink that is not specified in <i>Also=</i>. For template unit files, an instance different than the one specified in <i>DefaultInstance=</i> is enabled. </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> &quot;disabled&quot; </td>
<td> The unit file is not enabled, but contains an [Install] section with installation instructions. </td>
<td> &gt; 0
</td>
</tr>
<tr VALIGN=top>
<td> &quot;generated&quot; </td>
<td> The unit file was generated dynamically via a generator tool. See <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7). Generated unit files may not be enabled, they are enabled implicitly by their generator. </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> &quot;transient&quot; </td>
<td> The unit file has been created dynamically with the runtime API. Transient units may not be enabled. </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> &quot;bad&quot; </td>
<td> The unit file is invalid or another error occurred. Note that <code>is-enabled</code> will not actually return this state, but print an error message instead. However the unit file listing printed by <code>list-unit-files</code> might show it. </td>
<td> &gt; 0
</td>
</tr>
</table>
</dl>
<p> <code>mask </code><i>UNIT</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Mask one or more units, as specified on the command line. This will link these unit files to /dev/null, making it impossible to start them. This is a stronger version of <code>disable</code>, since it prohibits all kinds of activation of the unit, including enablement and manual activation. Use this option with care. This honors the <code>&#8211;runtime</code> option to only mask temporarily until the next reboot of the system. The <code>&#8211;now</code> option may be used to ensure that the units are also stopped. This command expects valid unit names only, it does not accept unit file paths.</dl>
<p> <code>unmask </code><i>UNIT</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Unmask one or more unit files, as specified on the command line. This will undo the effect of <code>mask</code>. This command expects valid unit names only, it does not accept unit file paths.</dl>
<p> <code>link </code><i>PATH</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Link a unit file that is not in the unit file search paths into the unit file search path. This command expects an absolute path to a unit file. The effect of this may be undone with <code>disable</code>. The effect of this command is that a unit file is made available for commands such as <code>start</code>, even though it is not installed directly in the unit search path. The file system where the linked unit files are located must be accessible when systemd is started (e.g. anything underneath /home/ or /var/ is not allowed, unless those directories are located on the root file system).</dl>
<p> <code>revert </code><i>UNIT</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Revert one or more unit files to their vendor versions. This command removes drop-in configuration files that modify the specified units, as well as any user-configured unit file that overrides a matching vendor supplied unit file. Specifically, for a unit &quot;foo.service&quot; the matching directories &quot;foo.service.d/&quot; with all their contained files are removed, both below the persistent and runtime configuration directories (i.e. below /etc/systemd/system and /run/systemd/system); if the unit file has a vendor-supplied version (i.e. a unit file located below /usr/) any matching persistent or runtime unit file that overrides it is removed, too. Note that if a unit file has no vendor-supplied version (i.e. is only defined below /etc/systemd/system or /run/systemd/system, but not in a unit file stored below /usr/), then it is not removed. Also, if a unit is masked, it is unmasked. </p>
<p> Effectively, this command may be used to undo all changes made with <code>systemctl edit</code>, <code>systemctl set-property</code> and <code>systemctl mask</code> and puts the original unit file with its settings back in effect.</dl>
<p> <code>add-wants </code><i>TARGET</i><i>UNIT</i><code>&#8230;</code>, <code>add-requires </code><i>TARGET</i><i>UNIT</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Adds &quot;Wants=&quot; or &quot;Requires=&quot; dependencies, respectively, to the specified <i>TARGET</i> for one or more units. </p>
<p> This command honors <code>&#8211;system</code>, <code>&#8211;user</code>, <code>&#8211;runtime</code> and <code>&#8211;global</code> in a way similar to <code>enable</code>.</dl>
<p> <code>edit </code><i>UNIT</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Edit a drop-in snippet or a whole replacement file if <code>&#8211;full</code> is specified, to extend or override the specified unit. </p>
<p> Depending on whether <code>&#8211;system</code> (the default), <code>&#8211;user</code>, or <code>&#8211;global</code> is specified, this command creates a drop-in file for each unit either for the system, for the calling user, or for all futures logins of all users. Then, the editor (see the &quot;Environment&quot; section below) is invoked on temporary files which will be written to the real location if the editor exits successfully. </p>
<p> If <code>&#8211;full</code> is specified, this will copy the original units instead of creating drop-in files. </p>
<p> If <code>&#8211;force</code> is specified and any units do not already exist, new unit files will be opened for editing. </p>
<p> If <code>&#8211;runtime</code> is specified, the changes will be made temporarily in /run/ and they will be lost on the next reboot. </p>
<p> If the temporary file is empty upon exit, the modification of the related unit is canceled. </p>
<p> After the units have been edited, systemd configuration is reloaded (in a way that is equivalent to <code>daemon-reload</code>). </p>
<p> Note that this command cannot be used to remotely edit units and that you cannot temporarily edit units which are in /etc/, since they take precedence over /run/.</dl>
<p> <code>get-default</code></p>
<dl>
<dt>
<dd> Return the default target to boot into. This returns the target unit name default.target is aliased (symlinked) to.</dl>
<p> <code>set-default </code><i>TARGET</i></p>
<dl>
<dt>
<dd> Set the default target to boot into. This sets (symlinks) the default.target alias to the given target unit.</dl>
<h3>Machine Commands</h3>
<p> <code>list-machines</code> [<i>PATTERN</i>&#8230;]</p>
<dl>
<dt>
<dd> List the host and all running local containers with their state. If one or more <i>PATTERN</i>s are specified, only containers matching one of them are shown.</dl>
<h3>Job Commands</h3>
<p> <code>list-jobs </code><code>[</code><i>PATTERN&#8230;</i>]</p>
<dl>
<dt>
<dd> List jobs that are in progress. If one or more <i>PATTERN</i>s are specified, only jobs for units matching one of them are shown. </p>
<p> When combined with <code>&#8211;after</code> or <code>&#8211;before</code> the list is augmented with information on which other job each job is waiting for, and which other jobs are waiting for it, see above.</dl>
<p> <code>cancel </code><i>JOB</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Cancel one or more jobs specified on the command line by their numeric job IDs. If no job ID is specified, cancel all pending jobs.</dl>
<h3>Environment Commands</h3>
<p> <code>systemd</code> supports an environment block that is passed to processes the manager spawns. The names of the variables can contain ASCII letters, digits, and the underscore character. Variable names cannot be empty or start with a digit. In variable values, most characters are allowed, but the whole sequence must be valid UTF-8. (Note that control characters like newline (<code>NL</code>), tab (<code>TAB</code>), or the escape character (<code>ESC</code>), <i>are</i> valid ASCII and thus valid UTF-8). The total length of the environment block is limited to <code>_SC_ARG_MAX</code> value defined by <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3). </p>
<p> <code>show-environment</code></p>
<dl>
<dt>
<dd> Dump the systemd manager environment block. This is the environment block that is passed to all processes the manager spawns. The environment block will be dumped in straight-forward form suitable for sourcing into most shells. If no special characters or whitespace is present in the variable values, no escaping is performed, and the assignments have the form &quot;VARIABLE=value&quot;. If whitespace or characters which have special meaning to the shell are present, dollar-single-quote escaping is used, and assignments have the form &quot;VARIABLE=$&#8217;value&#8217;&quot;. This syntax is known to be supported by <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-zsh/">zsh</a></code>(1), <code><a href="/docs/linux/man/1-ksh/">ksh</a></code>(1), and <code><a href="/docs/linux/man/1-busybox/">busybox</a></code>(1)&#8217;s <code><a href="/docs/linux/man/1-ash/">ash</a></code>(1), but not <code><a href="/docs/linux/man/1-dash/">dash</a></code>(1) or <code><a href="/docs/linux/man/1-fish/">fish</a></code>(1).</dl>
<p> <code>set-environment </code><i>VARIABLE=VALUE</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Set one or more systemd manager environment variables, as specified on the command line. This command will fail if variable names and values do not conform to the rules listed above.</dl>
<p> <code>unset-environment </code><i>VARIABLE</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Unset one or more systemd manager environment variables. If only a variable name is specified, it will be removed regardless of its value. If a variable and a value are specified, the variable is only removed if it has the specified value.</dl>
<p> <code>import-environment</code> <i>VARIABLE&#8230;</i></p>
<dl>
<dt>
<dd> Import all, one or more environment variables set on the client into the systemd manager environment block. If a list of environment variable names is passed, client-side values are then imported into the manager&#8217;s environment block. If any names are not valid environment variable names or have invalid values according to the rules described above, an error is raised. If no arguments are passed, the entire environment block inherited by the <code>systemctl</code> process is imported. In this mode, any inherited invalid environment variables are quietly ignored. </p>
<p> Importing of the full inherited environment block (calling this command without any arguments) is deprecated. A shell will set dozens of variables which only make sense locally and are only meant for processes which are descendants of the shell. Such variables in the global environment block are confusing to other processes.</dl>
<h3>Manager State Commands</h3>
<p> <code>daemon-reload</code></p>
<dl>
<dt>
<dd> Reload the systemd manager configuration. This will rerun all generators (see <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7)), reload all unit files, and recreate the entire dependency tree. While the daemon is being reloaded, all sockets systemd listens on behalf of user configuration will stay accessible. </p>
<p> This command should not be confused with the <code>reload</code> command.</dl>
<p> <code>daemon-reexec</code></p>
<dl>
<dt>
<dd> Reexecute the systemd manager. This will serialize the manager state, reexecute the process and deserialize the state again. This command is of little use except for debugging and package upgrades. Sometimes, it might be helpful as a heavy-weight <code>daemon-reload</code>. While the daemon is being reexecuted, all sockets systemd listening on behalf of user configuration will stay accessible.</dl>
<p> <code>log-level</code> [<i>LEVEL</i>]</p>
<dl>
<dt>
<dd> If no argument is given, print the current log level of the manager. If an optional argument <i>LEVEL</i> is provided, then the command changes the current log level of the manager to <i>LEVEL</i> (accepts the same values as <code>&#8211;log-level=</code> described in <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)).</dl>
<p> <code>log-target</code> [<i>TARGET</i>]</p>
<dl>
<dt>
<dd> If no argument is given, print the current log target of the manager. If an optional argument <i>TARGET</i> is provided, then the command changes the current log target of the manager to <i>TARGET</i> (accepts the same values as <code>&#8211;log-target=</code>, described in <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)).</dl>
<p> <code>service-watchdogs</code> [yes|no]</p>
<dl>
<dt>
<dd> If no argument is given, print the current state of service runtime watchdogs of the manager. If an optional boolean argument is provided, then globally enables or disables the service runtime watchdogs (<code>WatchdogSec=</code>) and emergency actions (e.g. <code>OnFailure=</code> or <code>StartLimitAction=</code>); see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5). The hardware watchdog is not affected by this setting.</dl>
<h3>System Commands</h3>
<p> <code>is-system-running</code></p>
<dl>
<dt>
<dd> Checks whether the system is operational. This returns success (exit code 0) when the system is fully up and running, specifically not in startup, shutdown or maintenance mode, and with no failed services. Failure is returned otherwise (exit code non-zero). In addition, the current state is printed in a short string to standard output, see the table below. Use <code>&#8211;quiet</code> to suppress this output. </p>
<p> Use <code>&#8211;wait</code> to wait until the boot process is completed before printing the current state and returning the appropriate error status. If <code>&#8211;wait</code> is in use, states <i>initializing</i> or <i>starting</i> will not be reported, instead the command will block until a later state (such as <i>running</i> or <i>degraded</i>) is reached. </p>
<p> <code>Table 2. is-system-running output</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Description </code></td>
<td><code> Exit Code </code>
</td>
</tr>
<tr VALIGN=top>
<td> <i>initializing</i> </td>
<td> Early bootup, before basic.target is reached or the <i>maintenance</i> state entered. </td>
<td> &gt; 0
</td>
</tr>
<tr VALIGN=top>
<td> <i>starting</i> </td>
<td> Late bootup, before the job queue becomes idle for the first time, or one of the rescue targets are reached. </td>
<td> &gt; 0
</td>
</tr>
<tr VALIGN=top>
<td> <i>running</i> </td>
<td> The system is fully operational. </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> <i>degraded</i> </td>
<td> The system is operational but one or more units failed. </td>
<td> &gt; 0
</td>
</tr>
<tr VALIGN=top>
<td> <i>maintenance</i> </td>
<td> The rescue or emergency target is active. </td>
<td> &gt; 0
</td>
</tr>
<tr VALIGN=top>
<td> <i>stopping</i> </td>
<td> The manager is shutting down. </td>
<td> &gt; 0
</td>
</tr>
<tr VALIGN=top>
<td> <i>offline</i> </td>
<td> The manager is not running. Specifically, this is the operational state if an incompatible program is running as system manager (PID 1). </td>
<td> &gt; 0
</td>
</tr>
<tr VALIGN=top>
<td> <i>unknown</i> </td>
<td> The operational state could not be determined, due to lack of resources or another error cause. </td>
<td> &gt; 0
</td>
</tr>
</table>
</dl>
<p> <code>default</code></p>
<dl>
<dt>
<dd> Enter default mode. This is equivalent to <code>systemctl isolate default.target</code>. This operation is blocking by default, use <code>&#8211;no-block</code> to request asynchronous behavior.</dl>
<p> <code>rescue</code></p>
<dl>
<dt>
<dd> Enter rescue mode. This is equivalent to <code>systemctl isolate rescue.target</code>. This operation is blocking by default, use <code>&#8211;no-block</code> to request asynchronous behavior.</dl>
<p> <code>emergency</code></p>
<dl>
<dt>
<dd> Enter emergency mode. This is equivalent to <code>systemctl isolate emergency.target</code>. This operation is blocking by default, use <code>&#8211;no-block</code> to request asynchronous behavior.</dl>
<p> <code>halt</code></p>
<dl>
<dt>
<dd> Shut down and halt the system. This is mostly equivalent to <code>systemctl start halt.target &#8211;job-mode=replace-irreversibly &#8211;no-block</code>, but also prints a wall message to all users. This command is asynchronous; it will return after the halt operation is enqueued, without waiting for it to complete. Note that this operation will simply halt the OS kernel after shutting down, leaving the hardware powered on. Use <code>systemctl poweroff</code> for powering off the system (see below). </p>
<p> If combined with <code>&#8211;force</code>, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the system halt. If <code>&#8211;force</code> is specified twice, the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss. Note that when <code>&#8211;force</code> is specified twice the halt operation is executed by <code>systemctl</code> itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.</dl>
<p> <code>poweroff</code></p>
<dl>
<dt>
<dd> Shut down and power-off the system. This is mostly equivalent to <code>systemctl start poweroff.target &#8211;job-mode=replace-irreversibly &#8211;no-block</code>, but also prints a wall message to all users. This command is asynchronous; it will return after the power-off operation is enqueued, without waiting for it to complete. </p>
<p> If combined with <code>&#8211;force</code>, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the powering off. If <code>&#8211;force</code> is specified twice, the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss. Note that when <code>&#8211;force</code> is specified twice the power-off operation is executed by <code>systemctl</code> itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.</dl>
<p> <code>reboot</code></p>
<dl>
<dt>
<dd> Shut down and reboot the system. This is mostly equivalent to <code>systemctl start reboot.target &#8211;job-mode=replace-irreversibly &#8211;no-block</code>, but also prints a wall message to all users. This command is asynchronous; it will return after the reboot operation is enqueued, without waiting for it to complete. </p>
<p> If combined with <code>&#8211;force</code>, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the reboot. If <code>&#8211;force</code> is specified twice, the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss. Note that when <code>&#8211;force</code> is specified twice the reboot operation is executed by <code>systemctl</code> itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed. </p>
<p> If the switch <code>&#8211;reboot-argument=</code> is given, it will be passed as the optional argument to the <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2) system call.</dl>
<p> <code>kexec</code></p>
<dl>
<dt>
<dd> Shut down and reboot the system via <code>kexec</code>. This is equivalent to <code>systemctl start kexec.target &#8211;job-mode=replace-irreversibly &#8211;no-block</code>. This command is asynchronous; it will return after the reboot operation is enqueued, without waiting for it to complete. </p>
<p> If combined with <code>&#8211;force</code>, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the reboot.</dl>
<p> <code>exit</code> [<i>EXIT_CODE</i>]</p>
<dl>
<dt>
<dd> Ask the service manager to quit. This is only supported for user service managers (i.e. in conjunction with the <code>&#8211;user</code> option) or in containers and is equivalent to <code>poweroff</code> otherwise. This command is asynchronous; it will return after the exit operation is enqueued, without waiting for it to complete. </p>
<p> The service manager will exit with the specified exit code, if <i>EXIT_CODE</i> is passed.</dl>
<p> <code>switch-root</code> <i>ROOT</i> [<i>INIT</i>]</p>
<dl>
<dt>
<dd> Switches to a different root directory and executes a new system manager process below it. This is intended for usage in initial RAM disks (&quot;initrd&quot;), and will transition from the initrd&#8217;s system manager process (a.k.a. &quot;init&quot; process) to the main system manager process which is loaded from the actual host volume. This call takes two arguments: the directory that is to become the new root directory, and the path to the new system manager binary below it to execute as PID 1. If the latter is omitted or the empty string, a systemd binary will automatically be searched for and used as init. If the system manager path is omitted, equal to the empty string or identical to the path to the systemd binary, the state of the initrd&#8217;s system manager process is passed to the main system manager, which allows later introspection of the state of the services involved in the initrd boot phase.</dl>
<p> <code>suspend</code></p>
<dl>
<dt>
<dd> Suspend the system. This will trigger activation of the special target unit suspend.target. This command is asynchronous, and will return after the suspend operation is successfully enqueued. It will not wait for the suspend/resume cycle to complete.</dl>
<p> <code>hibernate</code></p>
<dl>
<dt>
<dd> Hibernate the system. This will trigger activation of the special target unit hibernate.target. This command is asynchronous, and will return after the hibernation operation is successfully enqueued. It will not wait for the hibernate/thaw cycle to complete.</dl>
<p> <code>hybrid-sleep</code></p>
<dl>
<dt>
<dd> Hibernate and suspend the system. This will trigger activation of the special target unit hybrid-sleep.target. This command is asynchronous, and will return after the hybrid sleep operation is successfully enqueued. It will not wait for the sleep/wake-up cycle to complete.</dl>
<p> <code>suspend-then-hibernate</code></p>
<dl>
<dt>
<dd> Suspend the system and hibernate it after the delay specified in systemd-sleep.conf. This will trigger activation of the special target unit suspend-then-hibernate.target. This command is asynchronous, and will return after the hybrid sleep operation is successfully enqueued. It will not wait for the sleep/wake-up or hibernate/thaw cycle to complete.</dl>
<h3>Parameter Syntax</h3>
<p> Unit commands listed above take either a single unit name (designated as <i>UNIT</i>), or multiple unit specifications (designated as <i>PATTERN</i>&#8230;). In the first case, the unit name with or without a suffix must be given. If the suffix is not specified (unit name is &quot;abbreviated&quot;), systemctl will append a suitable suffix, &quot;.service&quot; by default, and a type-specific suffix in case of commands which operate only on specific unit types. For example, </p>
<dl>
<dt>
<dd>
<pre>
# systemctl start sshd
</pre>
</dl>
<p> and </p>
<dl>
<dt>
<dd>
<pre>
# systemctl start sshd.service
</pre>
</dl>
<p> are equivalent, as are </p>
<dl>
<dt>
<dd>
<pre>
# systemctl isolate default
</pre>
</dl>
<p> and </p>
<dl>
<dt>
<dd>
<pre>
# systemctl isolate default.target
</pre>
</dl>
<p> Note that (absolute) paths to device nodes are automatically converted to device unit names, and other (absolute) paths to mount unit names. </p>
<dl>
<dt>
<dd>
<pre>
# systemctl status /dev/sda
# systemctl status /home
</pre>
</dl>
<p> are equivalent to: </p>
<dl>
<dt>
<dd>
<pre>
# systemctl status dev-sda.device
# systemctl status home.mount
</pre>
</dl>
<p> In the second case, shell-style globs will be matched against the primary names of all units currently in memory; literal unit names, with or without a suffix, will be treated as in the first case. This means that literal unit names always refer to exactly one unit, but globs may match zero units and this is not considered an error. </p>
<p> Glob patterns use <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3), so normal shell-style globbing rules are used, and &quot;*&quot;, &quot;?&quot;, &quot;[]&quot; may be used. See <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) for more details. The patterns are matched against the primary names of units currently in memory, and patterns which do not match anything are silently skipped. For example: </p>
<dl>
<dt>
<dd>
<pre>
# systemctl stop sshd@*.service
</pre>
</dl>
<p> will stop all sshd [at] .service instances. Note that alias names of units, and units that aren&#8217;t in memory are not considered for glob expansion. </p>
<p> For unit file commands, the specified <i>UNIT</i> should be the name of the unit file (possibly abbreviated, see above), or the absolute path to the unit file: </p>
<dl>
<dt>
<dd>
<pre>
# systemctl enable foo.service
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
# systemctl link /path/to/foo.service
</pre>
</dl>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-t</code>, <code>&#8211;type=</code></p>
<dl>
<dt>
<dd> The argument should be a comma-separated list of unit types such as <code>service</code> and <code>socket</code>. </p>
<p> If one of the arguments is a unit type, when listing units, limit display to certain unit types. Otherwise, units of all types will be shown. </p>
<p> As a special case, if one of the arguments is <code>help</code>, a list of allowed values will be printed and the program will exit.</dl>
<p> <code>&#8211;state=</code></p>
<dl>
<dt>
<dd> The argument should be a comma-separated list of unit LOAD, SUB, or ACTIVE states. When listing units, show only those in the specified states. Use <code>&#8211;state=failed</code> to show only failed units. </p>
<p> As a special case, if one of the arguments is <code>help</code>, a list of allowed values will be printed and the program will exit.</dl>
<p> <code>-p</code>, <code>&#8211;property=</code></p>
<dl>
<dt>
<dd> When showing unit/job/manager properties with the <code>show</code> command, limit display to properties specified in the argument. The argument should be a comma-separated list of property names, such as &quot;MainPID&quot;. Unless specified, all known properties are shown. If specified more than once, all properties with the specified names are shown. Shell completion is implemented for property names. </p>
<p> For the manager itself, <code>systemctl show</code> will show all available properties, most of which are derived or closely match the options described in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5). </p>
<p> Properties for units vary by unit type, so showing any unit (even a non-existent one) is a way to list properties pertaining to this type. Similarly, showing any job will list properties pertaining to all jobs. Properties for units are documented in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), and the pages for individual unit types <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), etc.</dl>
<p> <code>-P</code></p>
<dl>
<dt>
<dd> Equivalent to <code>&#8211;value</code> <code>&#8211;property=</code>, i.e. shows the value of the property without the property name or &quot;=&quot;. Note that using <code>-P</code> once will also affect all properties listed with <code>-p</code>/<code>&#8211;property=</code>.</dl>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> When listing units with <code>list-units</code>, also show inactive units and units which are following other units. When showing unit/job/manager properties, show all properties regardless whether they are set or not. </p>
<p> To list all units installed in the file system, use the <code>list-unit-files</code> command instead. </p>
<p> When listing units with <code>list-dependencies</code>, recursively show dependencies of all dependent units (by default only dependencies of target units are shown). </p>
<p> When used with <code>status</code>, show journal messages in full, even if they include unprintable characters or are very long. By default, fields with unprintable characters are abbreviated as &quot;blob data&quot;. (Note that the pager may escape unprintable characters again.)</dl>
<p> <code>-r</code>, <code>&#8211;recursive</code></p>
<dl>
<dt>
<dd> When listing units, also show units of local containers. Units of local containers will be prefixed with the container name, separated by a single colon character (&quot;:&quot;).</dl>
<p> <code>&#8211;reverse</code></p>
<dl>
<dt>
<dd> Show reverse dependencies between units with <code>list-dependencies</code>, i.e. follow dependencies of type <i>WantedBy=</i>, <i>RequiredBy=</i>, <i>PartOf=</i>, <i>BoundBy=</i>, instead of <i>Wants=</i> and similar.</dl>
<p> <code>&#8211;after</code></p>
<dl>
<dt>
<dd> With <code>list-dependencies</code>, show the units that are ordered before the specified unit. In other words, recursively list units following the <i>After=</i> dependency. </p>
<p> Note that any <i>After=</i> dependency is automatically mirrored to create a <i>Before=</i> dependency. Temporal dependencies may be specified explicitly, but are also created implicitly for units which are <i>WantedBy=</i> targets (see <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5)), and as a result of other directives (for example <i>RequiresMountsFor=</i>). Both explicitly and implicitly introduced dependencies are shown with <code>list-dependencies</code>. </p>
<p> When passed to the <code>list-jobs</code> command, for each printed job show which other jobs are waiting for it. May be combined with <code>&#8211;before</code> to show both the jobs waiting for each job as well as all jobs each job is waiting for.</dl>
<p> <code>&#8211;before</code></p>
<dl>
<dt>
<dd> With <code>list-dependencies</code>, show the units that are ordered after the specified unit. In other words, recursively list units following the <i>Before=</i> dependency. </p>
<p> When passed to the <code>list-jobs</code> command, for each printed job show which other jobs it is waiting for. May be combined with <code>&#8211;after</code> to show both the jobs waiting for each job as well as all jobs each job is waiting for.</dl>
<p> <code>&#8211;with-dependencies</code></p>
<dl>
<dt>
<dd> When used with <code>status</code>, <code>cat</code>, <code>list-units</code>, and <code>list-unit-files</code>, those commands print all specified units and the dependencies of those units. </p>
<p> Options <code>&#8211;reverse</code>, <code>&#8211;after</code>, <code>&#8211;before</code> may be used to change what types of dependencies are shown.</dl>
<p> <code>-l</code>, <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Do not ellipsize unit names, process tree entries, journal output, or truncate unit descriptions in the output of <code>status</code>, <code>list-units</code>, <code>list-jobs</code>, and <code>list-timers</code>. </p>
<p> Also, show installation targets in the output of <code>is-enabled</code>.</dl>
<p> <code>&#8211;value</code></p>
<dl>
<dt>
<dd> When printing properties with <code>show</code>, only print the value, and skip the property name and &quot;=&quot;. Also see option <code>-P</code> above.</dl>
<p> <code>&#8211;show-types</code></p>
<dl>
<dt>
<dd> When showing sockets, show the type of the socket.</dl>
<p> <code>&#8211;job-mode=</code></p>
<dl>
<dt>
<dd> When queuing a new job, this option controls how to deal with already queued jobs. It takes one of &quot;fail&quot;, &quot;replace&quot;, &quot;replace-irreversibly&quot;, &quot;isolate&quot;, &quot;ignore-dependencies&quot;, &quot;ignore-requirements&quot;, &quot;flush&quot;, or &quot;triggering&quot;. Defaults to &quot;replace&quot;, except when the <code>isolate</code> command is used which implies the &quot;isolate&quot; job mode. </p>
<p> If &quot;fail&quot; is specified and a requested operation conflicts with a pending job (more specifically: causes an already pending start job to be reversed into a stop job or vice versa), cause the operation to fail. </p>
<p> If &quot;replace&quot; (the default) is specified, any conflicting pending job will be replaced, as necessary. </p>
<p> If &quot;replace-irreversibly&quot; is specified, operate like &quot;replace&quot;, but also mark the new jobs as irreversible. This prevents future conflicting transactions from replacing these jobs (or even being enqueued while the irreversible jobs are still pending). Irreversible jobs can still be cancelled using the <code>cancel</code> command. This job mode should be used on any transaction which pulls in shutdown.target. </p>
<p> &quot;isolate&quot; is only valid for start operations and causes all other units to be stopped when the specified unit is started. This mode is always used when the <code>isolate</code> command is used. </p>
<p> &quot;flush&quot; will cause all queued jobs to be canceled when the new job is enqueued. </p>
<p> If &quot;ignore-dependencies&quot; is specified, then all unit dependencies are ignored for this new job and the operation is executed immediately. If passed, no required units of the unit passed will be pulled in, and no ordering dependencies will be honored. This is mostly a debugging and rescue tool for the administrator and should not be used by applications. </p>
<p> &quot;ignore-requirements&quot; is similar to &quot;ignore-dependencies&quot;, but only causes the requirement dependencies to be ignored, the ordering dependencies will still be honored. </p>
<p> &quot;triggering&quot; may only be used with <code>systemctl stop</code>. In this mode, the specified unit and any active units that trigger it are stopped. See the discussion of <i>Triggers=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for more information about triggering units.</dl>
<p> <code>-T</code>, <code>&#8211;show-transaction</code></p>
<dl>
<dt>
<dd> When enqueuing a unit job (for example as effect of a <code>systemctl start</code> invocation or similar), show brief information about all jobs enqueued, covering both the requested job and any added because of unit dependencies. Note that the output will only include jobs immediately part of the transaction requested. It is possible that service start-up program code run as effect of the enqueued jobs might request further jobs to be pulled in. This means that completion of the listed jobs might ultimately entail more jobs than the listed ones.</dl>
<p> <code>&#8211;fail</code></p>
<dl>
<dt>
<dd> Shorthand for <code>&#8211;job-mode=</code>fail. </p>
<p> When used with the <code>kill</code> command, if no units were killed, the operation results in an error.</dl>
<p> <code>&#8211;check-inhibitors=</code></p>
<dl>
<dt>
<dd> When system shutdown or sleep state is request, this option controls how to deal with inhibitor locks. It takes one of &quot;auto&quot;, &quot;yes&quot; or &quot;no&quot;. Defaults to &quot;auto&quot;, which will behave like &quot;yes&quot; for interactive invocations (i.e. from a TTY) and &quot;no&quot; for non-interactive invocations. &quot;yes&quot; will let the request respect inhibitor locks. &quot;no&quot; will let the request ignore inhibitor locks. </p>
<p> Applications can establish inhibitor locks to avoid that certain important operations (such as CD burning or suchlike) are interrupted by system shutdown or a sleep state. Any user may take these locks and privileged users may override these locks. If any locks are taken, shutdown and sleep state requests will normally fail (unless privileged) and a list of active locks is printed. However, if &quot;no&quot; is specified or &quot;auto&quot; is specified on a non-interactive requests, the established locks are ignored and not shown, and the operation attempted anyway, possibly requiring additional privileges. May be overridden by <code>&#8211;force</code>.</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Shortcut for <code>&#8211;check-inhibitors=no</code>.</dl>
<p> <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Just print what would be done. Currently supported by verbs <code>halt</code>, <code>poweroff</code>, <code>reboot</code>, <code>kexec</code>, <code>suspend</code>, <code>hibernate</code>, <code>hybrid-sleep</code>, <code>suspend-then-hibernate</code>, <code>default</code>, <code>rescue</code>, <code>emergency</code>, and <code>exit</code>.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Suppress printing of the results of various commands and also the hints about truncated log lines. This does not suppress output of commands for which the printed output is the only result (like <code>show</code>). Errors are always printed.</dl>
<p> <code>&#8211;no-block</code></p>
<dl>
<dt>
<dd> Do not synchronously wait for the requested operation to finish. If this is not specified, the job will be verified, enqueued and <code>systemctl</code> will wait until the unit&#8217;s start-up is completed. By passing this argument, it is only verified and enqueued. This option may not be combined with <code>&#8211;wait</code>.</dl>
<p> <code>&#8211;wait</code></p>
<dl>
<dt>
<dd> Synchronously wait for started units to terminate again. This option may not be combined with <code>&#8211;no-block</code>. Note that this will wait forever if any given unit never terminates (by itself or by getting stopped explicitly); particularly services which use &quot;RemainAfterExit=yes&quot;. </p>
<p> When used with <code>is-system-running</code>, wait until the boot process is completed before returning.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Talk to the service manager of the calling user, rather than the service manager of the system.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Talk to the service manager of the system. This is the implied default.</dl>
<p> <code>&#8211;failed</code></p>
<dl>
<dt>
<dd> List units in failed state. This is equivalent to <code>&#8211;state=failed</code>.</dl>
<p> <code>&#8211;no-wall</code></p>
<dl>
<dt>
<dd> Do not send wall message before halt, power-off and reboot.</dl>
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
<dd> When used with <code>start</code> and related commands, disables asking for passwords. Background services may require input of a password or passphrase string, for example to unlock system hard disks or cryptographic certificates. Unless this option is specified and the command is invoked from a terminal, <code>systemctl</code> will query the user on the terminal for the necessary secrets. Use this option to switch this behavior off. In this case, the password must be supplied by some other means (for example graphical password agents) or the service might fail. This also disables querying the user for authentication for privileged operations.</dl>
<p> <code>&#8211;kill-who=</code></p>
<dl>
<dt>
<dd> When used with <code>kill</code>, choose which processes to send a signal to. Must be one of <code>main</code>, <code>control</code> or <code>all</code> to select whether to kill only the main process, the control process or all processes of the unit. The main process of the unit is the one that defines the life-time of it. A control process of a unit is one that is invoked by the manager to induce state changes of it. For example, all processes started due to the <i>ExecStartPre=</i>, <i>ExecStop=</i> or <i>ExecReload=</i> settings of service units are control processes. Note that there is only one control process per unit at a time, as only one state change is executed at a time. For services of type <i>Type=forking</i>, the initial process started by the manager for <i>ExecStart=</i> is a control process, while the process ultimately forked off by that one is then considered the main process of the unit (if it can be determined). This is different for service units of other types, where the process forked off by the manager for <i>ExecStart=</i> is always the main process itself. A service unit consists of zero or one main process, zero or one control process plus any number of additional processes. Not all unit types manage processes of these types however. For example, for mount units, control processes are defined (which are the invocations of /bin/mount and /bin/umount), but no main process is defined. If omitted, defaults to <code>all</code>.</dl>
<p> <code>-s</code>, <code>&#8211;signal=</code></p>
<dl>
<dt>
<dd> When used with <code>kill</code>, choose which signal to send to selected processes. Must be one of the well-known signal specifiers such as <code>SIGTERM</code>, <code>SIGINT</code> or <code>SIGSTOP</code>. If omitted, defaults to <code>SIGTERM</code>. </p>
<p> The special value &quot;help&quot; will list the known values and the program will exit immediately, and the special value &quot;list&quot; will list known values along with the numerical signal numbers and the program will exit immediately.</dl>
<p> <code>&#8211;what=</code></p>
<dl>
<dt>
<dd> Select what type of per-unit resources to remove when the <code>clean</code> command is invoked, see below. Takes one of <code>configuration</code>, <code>state</code>, <code>cache</code>, <code>logs</code>, <code>runtime</code> to select the type of resource. This option may be specified more than once, in which case all specified resource types are removed. Also accepts the special value <code>all</code> as a shortcut for specifying all five resource types. If this option is not specified defaults to the combination of <code>cache</code> and <code>runtime</code>, i.e. the two kinds of resources that are generally considered to be redundant and can be reconstructed on next invocation.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> When used with <code>enable</code>, overwrite any existing conflicting symlinks. </p>
<p> When used with <code>edit</code>, create all of the specified units which do not already exist. </p>
<p> When used with <code>halt</code>, <code>poweroff</code>, <code>reboot</code> or <code>kexec</code>, execute the selected operation without shutting down all units. However, all processes will be killed forcibly and all file systems are unmounted or remounted read-only. This is hence a drastic but relatively safe option to request an immediate reboot. If <code>&#8211;force</code> is specified twice for these operations (with the exception of <code>kexec</code>), they will be executed immediately, without terminating any processes or unmounting any file systems. Warning: specifying <code>&#8211;force</code> twice with any of these operations might result in data loss. Note that when <code>&#8211;force</code> is specified twice the selected operation is executed by <code>systemctl</code> itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.</dl>
<p> <code>&#8211;message=</code></p>
<dl>
<dt>
<dd> When used with <code>halt</code>, <code>poweroff</code> or <code>reboot</code>, set a short message explaining the reason for the operation. The message will be logged together with the default shutdown message.</dl>
<p> <code>&#8211;now</code></p>
<dl>
<dt>
<dd> When used with <code>enable</code>, the units will also be started. When used with <code>disable</code> or <code>mask</code>, the units will also be stopped. The start or stop operation is only carried out when the respective enable or disable operation has been successful.</dl>
<p> <code>&#8211;root=</code></p>
<dl>
<dt>
<dd> When used with <code>enable</code>/<code>disable</code>/<code>is-enabled</code> (and related commands), use the specified root path when looking for unit files. If this option is present, <code>systemctl</code> will operate on the file system directly, instead of communicating with the <code>systemd</code> daemon to carry out changes.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> When used with <code>enable</code>, <code>disable</code>, <code>edit</code>, (and related commands), make changes only temporarily, so that they are lost on the next reboot. This will have the effect that changes are not made in subdirectories of /etc/ but in /run/, with identical immediate effects, however, since the latter is lost on reboot, the changes are lost too. </p>
<p> Similarly, when used with <code>set-property</code>, make changes only temporarily, so that they are lost on the next reboot.</dl>
<p> <code>&#8211;preset-mode=</code></p>
<dl>
<dt>
<dd> Takes one of &quot;full&quot; (the default), &quot;enable-only&quot;, &quot;disable-only&quot;. When used with the <code>preset</code> or <code>preset-all</code> commands, controls whether units shall be disabled and enabled according to the preset rules, or only enabled, or only disabled.</dl>
<p> <code>-n</code>, <code>&#8211;lines=</code></p>
<dl>
<dt>
<dd> When used with <code>status</code>, controls the number of journal lines to show, counting from the most recent ones. Takes a positive integer argument, or 0 to disable journal output. Defaults to 10.</dl>
<p> <code>-o</code>, <code>&#8211;output=</code></p>
<dl>
<dt>
<dd> When used with <code>status</code>, controls the formatting of the journal entries that are shown. For the available choices, see <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1). Defaults to &quot;short&quot;.</dl>
<p> <code>&#8211;firmware-setup</code></p>
<dl>
<dt>
<dd> When used with the <code>reboot</code> command, indicate to the system&#8217;s firmware to reboot into the firmware setup interface. Note that this functionality is not available on all systems.</dl>
<p> <code>&#8211;boot-loader-menu=</code></p>
<dl>
<dt>
<dd> When used with the <code>reboot</code> command, indicate to the system&#8217;s boot loader to show the boot loader menu on the following boot. Takes a time value as parameter &#8212; indicating the menu timeout. Pass zero in order to disable the menu timeout. Note that not all boot loaders support this functionality.</dl>
<p> <code>&#8211;boot-loader-entry=</code></p>
<dl>
<dt>
<dd> When used with the <code>reboot</code> command, indicate to the system&#8217;s boot loader to boot into a specific boot loader entry on the following boot. Takes a boot loader entry identifier as argument, or &quot;help&quot; in order to list available entries. Note that not all boot loaders support this functionality.</dl>
<p> <code>&#8211;reboot-argument=</code></p>
<dl>
<dt>
<dd> This switch is used with <code>reboot</code>. The value is architecture and firmware specific. As an example, &quot;recovery&quot; might be used to trigger system recovery, and &quot;fota&quot; might be used to trigger a &#8220;firmware over the air&#8221; update.</dl>
<p> <code>&#8211;plain</code></p>
<dl>
<dt>
<dd> When used with <code>list-dependencies</code>, <code>list-units</code> or <code>list-machines</code>, the output is printed as a list instead of a tree, and the bullet circles are omitted.</dl>
<p> <code>&#8211;timestamp=</code></p>
<dl>
<dt>
<dd> Change the format of printed timestamps. The following values may be used: </p>
<p> <code>pretty</code> (this is the default)</p>
<dl>
<dt>
<dd> &quot;Day YYYY-MM-DD HH:MM:SS TZ&quot;</dl>
<p> <code>us</code>, <code>&micro;s</code></p>
<dl>
<dt>
<dd> &quot;Day YYYY-MM-DD HH:MM:SS.UUUUUU TZ&quot;</dl>
<p> <code>utc</code></p>
<dl>
<dt>
<dd> &quot;Day YYYY-MM-DD HH:MM:SS UTC&quot;</dl>
<p> <code>us+utc</code>, <code>&micro;s+utc</code></p>
<dl>
<dt>
<dd> &quot;Day YYYY-MM-DD HH:MM:SS.UUUUUU UTC&quot;</dl>
</dl>
<p> <code>&#8211;mkdir</code></p>
<dl>
<dt>
<dd> When used with <code>bind</code>, creates the destination file or directory before applying the bind mount. Note that even though the name of this option suggests that it is suitable only for directories, this option also creates the destination file node to mount over if the object to mount is not a directory, but a regular file, device node, socket or FIFO.</dl>
<p> <code>&#8211;marked</code></p>
<dl>
<dt>
<dd> Only allowed with <code>reload-or-restart</code>. Enqueues restart jobs for all units that have the &quot;needs-restart&quot; mark, and reload jobs for units that have the &quot;needs-reload&quot; mark. When a unit marked for reload does not support reload, restart will be queued. Those properties can be set using <code>set-property Marks</code>. </p>
<p> Unless <code>&#8211;no-block</code> is used, <code>systemctl</code> will wait for the queued jobs to finish.</dl>
<p> <code>&#8211;read-only</code></p>
<dl>
<dt>
<dd> When used with <code>bind</code>, creates a read-only bind mount.</dl>
<p> <code>-H</code>, <code>&#8211;host=</code></p>
<dl>
<dt>
<dd> Execute the operation remotely. Specify a hostname, or a username and hostname separated by &quot;@&quot;, to connect to. The hostname may optionally be suffixed by a port ssh is listening on, separated by &quot;:&quot;, and then a container name, separated by &quot;/&quot;, which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with <code>machinectl -H </code><i>HOST</i>. Put IPv6 addresses in brackets.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Execute operation on a local container. Specify a container name to connect to, optionally prefixed by a user name to connect as and a separating &quot;@&quot; character. If the special string &quot;.host&quot; is used in place of the container name, a connection to the local system is made (which is useful to connect to a specific user&#8217;s user bus: &quot;&#8211;user &#8211;machine=lennart [at] .host&quot;). If the &quot;@&quot; syntax is not used, the connection is made as root user. If the &quot;@&quot; syntax is used either the left hand side or the right hand side may be omitted (but not both) in which case the local user name and &quot;.host&quot; are implied.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<p> <code>&#8211;legend=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Enable or disable printing of the legend, i.e. column headers and the footer with hints. The legend is printed by default, unless disabled with <code>&#8211;quiet</code> or similar.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise. </p>
<p> <code>systemctl</code> uses the return codes defined by LSB, as defined in m[blue]<code>LSB 3.0.0</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> <code>Table 3. LSB return codes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Value </code></td>
<td><code> Description in LSB </code></td>
<td><code> Use in systemd </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>0</code> </td>
<td> &quot;program is running or service is OK&quot; </td>
<td> unit is active
</td>
</tr>
<tr VALIGN=top>
<td> <code>1</code> </td>
<td> &quot;program is dead and /var/run pid file exists&quot; </td>
<td> unit <i>not</i> failed (used by <code>is-failed</code>)
</td>
</tr>
<tr VALIGN=top>
<td> <code>2</code> </td>
<td> &quot;program is dead and /var/lock lock file exists&quot; </td>
<td> unused
</td>
</tr>
<tr VALIGN=top>
<td> <code>3</code> </td>
<td> &quot;program is not running&quot; </td>
<td> unit is not active
</td>
</tr>
<tr VALIGN=top>
<td> <code>4</code> </td>
<td> &quot;program or service status is unknown&quot; </td>
<td> no such unit
</td>
</tr>
</table>
<p> The mapping of LSB service states to systemd unit states is imperfect, so it is better to not rely on those return values but to look for specific unit states and substates instead.</p>
<h2>ENVIRONMENT</h2>
<p> <i>$SYSTEMD_EDITOR</i></p>
<dl>
<dt>
<dd> Editor to use when editing units; overrides <i>$EDITOR</i> and <i>$VISUAL</i>. If neither <i>$SYSTEMD_EDITOR</i> nor <i>$EDITOR</i> nor <i>$VISUAL</i> are present or if it is set to an empty string or if their execution failed, systemctl will try to execute well known editors in this order: <code><a href="/docs/linux/man/1-editor/">editor</a></code>(1), <code><a href="/docs/linux/man/1-nano/">nano</a></code>(1), <code><a href="/docs/linux/man/1-vim/">vim</a></code>(1), <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1).</dl>
<p> <i>$SYSTEMD_LOG_LEVEL</i></p>
<dl>
<dt>
<dd> The maximum log level of emitted messages (messages with a higher log level, i.e. less important ones, will be suppressed). Either one of (in order of decreasing importance) <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code>, or an integer in the range 0&#8230;7. See <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for more information.</dl>
<p> <i>$SYSTEMD_LOG_COLOR</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages written to the tty will be colored according to priority. </p>
<p> This setting is only useful when messages are written directly to the terminal, because <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and other tools that display logs will color messages based on the log level on their own.</dl>
<p> <i>$SYSTEMD_LOG_TIME</i></p>
<dl>
<dt>
<dd> A boolean. If true, console log messages will be prefixed with a timestamp. </p>
<p> This setting is only useful when messages are written directly to the terminal or a file, because <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and other tools that display logs will attach timestamps based on the entry metadata on their own.</dl>
<p> <i>$SYSTEMD_LOG_LOCATION</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages will be prefixed with a filename and line number in the source code where the message originates. </p>
<p> Note that the log location is often attached as metadata to journal entries anyway. Including it directly in the message text can nevertheless be convenient when debugging programs.</dl>
<p> <i>$SYSTEMD_LOG_TARGET</i></p>
<dl>
<dt>
<dd> The destination for log messages. One of <code>console</code> (log to the attached tty), <code>console-prefixed</code> (log to the attached tty but with prefixes encoding the log level and &quot;facility&quot;, see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code>kmsg</code> (log to the kernel circular log buffer), <code>journal</code> (log to the journal), <code>journal-or-kmsg</code> (log to the journal if available, and to kmsg otherwise), <code>auto</code> (determine the appropriate log target automatically, the default), <code>null</code> (disable log output).</dl>
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
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/1-loginctl/">loginctl</a></code>(1), <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1), <code><a href="/docs/linux/man/5-systemd-preset/">systemd.preset</a></code>(5), <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7), <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> LSB 3.0.0</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://refspecs.linuxbase.org/LSB_3.0.0/LSB-PDA/LSB-PDA/iniscrptact.html">http://refspecs.linuxbase.org/LSB_3.0.0/LSB-PDA/LSB-PDA/iniscrptact.html</a></dl>
</dl>
<h2>Index</h2>
