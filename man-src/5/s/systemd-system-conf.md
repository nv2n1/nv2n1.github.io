---
title: "systemd-system-conf(5)"
name: "systemd-system-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-system-conf/"
description: "systemd-system.conf, system.conf.d, systemd-user.conf, user.conf.d – System and session service manager configuration files"
---

<p>systemd-system.conf, system.conf.d, systemd-user.conf, user.conf.d &#8211; System and session service manager configuration files</p>
<h2>Synopsis</h2>
<p>/etc/systemd/system.conf, /etc/systemd/system.conf.d/*.conf, /run/systemd/system.conf.d/*.conf, /lib/systemd/system.conf.d/*.conf </p>
<p> ~/.config/systemd/user.conf, /etc/systemd/user.conf, /etc/systemd/user.conf.d/*.conf, /run/systemd/user.conf.d/*.conf, /usr/lib/systemd/user.conf.d/*.conf</p>
<h2>Description</h2>
<p>When run as a system instance, <code>systemd</code> interprets the configuration file system.conf and the files in system.conf.d directories; when run as a user instance, it interprets the configuration file user.conf (either in the home directory of the user, or if not found, under /etc/systemd/) and the files in user.conf.d directories. These configuration files contain a few settings controlling basic manager operations. </p>
<p> See <code><a href="/docs/linux/man/7-systemd-syntax/">systemd.syntax</a></code>(7) for a general description of the syntax.</p>
<h2>Configuration Directories And Precedence</h2>
<p>The default configuration is set during compilation, so configuration is only needed when it is necessary to deviate from those defaults. Initially, the main configuration file in /etc/systemd/ contains commented out entries showing the defaults as a guide to the administrator. Local overrides can be created by editing this file or by creating drop-ins, as described below. Using drop-ins for local configuration is recommended over modifications to the main configuration file. </p>
<p> In addition to the &quot;main&quot; configuration file, drop-in configuration snippets are read from /usr/lib/systemd/*.conf.d/, /usr/local/lib/systemd/*.conf.d/, and /etc/systemd/*.conf.d/. Those drop-ins have higher precedence and override the main configuration file. Files in the *.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of in which of the subdirectories they reside. When multiple files specify the same option, for options which accept just a single value, the entry in the file sorted last takes precedence, and for options which accept a list of values, entries are collected as they occur in the sorted files. </p>
<p> When packages need to customize the configuration, they can install drop-ins under /usr/. Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. Drop-ins have to be used to override package drop-ins, since the main configuration file has lower precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file.</p>
<h2>Options</h2>
<p>All options are configured in the [Manager] section: </p>
<p> <i>LogColor=</i>, <i>LogLevel=</i>, <i>LogLocation=</i>, <i>LogTarget=</i>, <i>LogTime=</i>, <i>DumpCore=yes</i>, <i>CrashChangeVT=no</i>, <i>CrashShell=no</i>, <i>CrashReboot=no</i>, <i>ShowStatus=yes</i>, <i>DefaultStandardOutput=journal</i>, <i>DefaultStandardError=inherit</i></p>
<dl>
<dd>Configures various parameters of basic manager operation. These options may be overridden by the respective process and kernel command line arguments. See <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) for details.</dl>
<p> <i>CtrlAltDelBurstAction=</i></p>
<dl>
<dd>Defines what action will be performed if user presses Ctrl-Alt-Delete more than 7 times in 2s. Can be set to &quot;reboot-force&quot;, &quot;poweroff-force&quot;, &quot;reboot-immediate&quot;, &quot;poweroff-immediate&quot; or disabled with &quot;none&quot;. Defaults to &quot;reboot-force&quot;.</dl>
<p> <i>CPUAffinity=</i></p>
<dl>
<dd>Configures the CPU affinity for the service manager as well as the default CPU affinity for all forked off processes. Takes a list of CPU indices or ranges separated by either whitespace or commas. CPU ranges are specified by the lower and upper CPU indices separated by a dash. This option may be specified more than once, in which case the specified CPU affinity masks are merged. If the empty string is assigned, the mask is reset, all assignments prior to this will have no effect. Individual services may override the CPU affinity for their processes with the <i>CPUAffinity=</i> setting in unit files, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5).</dl>
<p> <i>NUMAPolicy=</i></p>
<dl>
<dd>Configures the NUMA memory policy for the service manager and the default NUMA memory policy for all forked off processes. Individual services may override the default policy with the <i>NUMAPolicy=</i> setting in unit files, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5).</dl>
<p> <i>NUMAMask=</i></p>
<dl>
<dd>Configures the NUMA node mask that will be associated with the selected NUMA policy. Note that <code>default</code> and <code>local</code> NUMA policies don&#8217;t require explicit NUMA node mask and value of the option can be empty. Similarly to <i>NUMAPolicy=</i>, value can be overridden by individual services in unit files, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5).</dl>
<p> <i>RuntimeWatchdogSec=</i>, <i>RebootWatchdogSec=</i>, <i>KExecWatchdogSec=</i></p>
<dl>
<dd>Configure the hardware watchdog at runtime and at reboot. Takes a timeout value in seconds (or in other time units if suffixed with &quot;ms&quot;, &quot;min&quot;, &quot;h&quot;, &quot;d&quot;, &quot;w&quot;). If <i>RuntimeWatchdogSec=</i> is set to a non-zero value, the watchdog hardware (/dev/watchdog or the path specified with <i>WatchdogDevice=</i> or the kernel option <i>systemd.watchdog-device=</i>) will be programmed to automatically reboot the system if it is not contacted within the specified timeout interval. The system manager will ensure to contact it at least once in half the specified timeout interval. This feature requires a hardware watchdog device to be present, as it is commonly the case in embedded and server systems. Not all hardware watchdogs allow configuration of all possible reboot timeout values, in which case the closest available timeout is picked. <i>RebootWatchdogSec=</i> may be used to configure the hardware watchdog when the system is asked to reboot. It works as a safety net to ensure that the reboot takes place even if a clean reboot attempt times out. Note that the <i>RebootWatchdogSec=</i> timeout applies only to the second phase of the reboot, i.e. after all regular services are already terminated, and after the system and service manager process (PID 1) got replaced by the systemd-shutdown binary, see system <code><a href="/docs/linux/man/7-bootup/">bootup</a></code>(7) for details. During the first phase of the shutdown operation the system and service manager remains running and hence <i>RuntimeWatchdogSec=</i> is still honoured. In order to define a timeout on this first phase of system shutdown, configure <i>JobTimeoutSec=</i> and <i>JobTimeoutAction=</i> in the [Unit] section of the shutdown.target unit. By default <i>RuntimeWatchdogSec=</i> defaults to 0 (off), and <i>RebootWatchdogSec=</i> to 10min. <i>KExecWatchdogSec=</i> may be used to additionally enable the watchdog when kexec is being executed rather than when rebooting. Note that if the kernel does not reset the watchdog on kexec (depending on the specific hardware and/or driver), in this case the watchdog might not get disabled after kexec succeeds and thus the system might get rebooted, unless <i>RuntimeWatchdogSec=</i> is also enabled at the same time. For this reason it is recommended to enable <i>KExecWatchdogSec=</i> only if <i>RuntimeWatchdogSec=</i> is also enabled. These settings have no effect if a hardware watchdog is not available.</dl>
<p> <i>WatchdogDevice=</i></p>
<dl>
<dd>Configure the hardware watchdog device that the runtime and shutdown watchdog timers will open and use. Defaults to /dev/watchdog. This setting has no effect if a hardware watchdog is not available.</dl>
<p> <i>CapabilityBoundingSet=</i></p>
<dl>
<dd>Controls which capabilities to include in the capability bounding set for PID 1 and its children. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for details. Takes a whitespace-separated list of capability names as read by <code><a href="/docs/linux/man/3-cap_from_name/">cap_from_name</a></code>(3). Capabilities listed will be included in the bounding set, all others are removed. If the list of capabilities is prefixed with ~, all but the listed capabilities will be included, the effect of the assignment inverted. Note that this option also affects the respective capabilities in the effective, permitted and inheritable capability sets. The capability bounding set may also be individually configured for units using the <i>CapabilityBoundingSet=</i> directive for units, but note that capabilities dropped for PID 1 cannot be regained in individual units, they are lost for good.</dl>
<p> <i>NoNewPrivileges=</i></p>
<dl>
<dd>Takes a boolean argument. If true, ensures that PID 1 and all its children can never gain new privileges through <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) (e.g. via setuid or setgid bits, or filesystem capabilities). Defaults to false. General purpose distributions commonly rely on executables with setuid or setgid bits and will thus not function properly with this option enabled. Individual units cannot disable this option. Also see m[blue]<code>No New Privileges Flag</code>m[]<font SIZE="-2">[1]</font>.</dl>
<p> <i>SystemCallArchitectures=</i></p>
<dl>
<dd>Takes a space-separated list of architecture identifiers. Selects from which architectures system calls may be invoked on this system. This may be used as an effective way to disable invocation of non-native binaries system-wide, for example to prohibit execution of 32-bit x86 binaries on 64-bit x86-64 systems. This option operates system-wide, and acts similar to the <i>SystemCallArchitectures=</i> setting of unit files, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details. This setting defaults to the empty list, in which case no filtering of system calls based on architecture is applied. Known architecture identifiers are &quot;x86&quot;, &quot;x86-64&quot;, &quot;x32&quot;, &quot;arm&quot; and the special identifier &quot;native&quot;. The latter implicitly maps to the native architecture of the system (or more specifically, the architecture the system manager was compiled for). Set this setting to &quot;native&quot; to prohibit execution of any non-native binaries. When a binary executes a system call of an architecture that is not listed in this setting, it will be immediately terminated with the SIGSYS signal.</dl>
<p> <i>TimerSlackNSec=</i></p>
<dl>
<dd>Sets the timer slack in nanoseconds for PID 1, which is inherited by all executed processes, unless overridden individually, for example with the <i>TimerSlackNSec=</i> setting in service units (for details see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5)). The timer slack controls the accuracy of wake-ups triggered by system timers. See <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) for more information. Note that in contrast to most other time span definitions this parameter takes an integer value in nano-seconds if no unit is specified. The usual time units are understood too.</dl>
<p> <i>StatusUnitFormat=</i></p>
<dl>
<dd>Takes <code>name</code>, <code>description</code> or <code>combined</code> as the value. If <code>name</code>, the system manager will use unit names in status messages (e.g. &quot;systemd-journald.service&quot;), instead of the longer and more informative descriptions set with <i>Description=</i> (e.g. &quot;Journal Logging Service&quot;). If <code>combined</code>, the system manager will use both unit names and descriptions in status messages (e.g. &quot;systemd-journald.service &#8211; Journal Logging Service&quot;). </p>
<p> See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details about unit names and <i>Description=</i>.</dl>
<p> <i>DefaultTimerAccuracySec=</i></p>
<dl>
<dd>Sets the default accuracy of timer units. This controls the global default for the <i>AccuracySec=</i> setting of timer units, see <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5) for details. <i>AccuracySec=</i> set in individual units override the global default for the specific unit. Defaults to 1min. Note that the accuracy of timer units is also affected by the configured timer slack for PID 1, see <i>TimerSlackNSec=</i> above.</dl>
<p> <i>DefaultTimeoutStartSec=</i>, <i>DefaultTimeoutStopSec=</i>, <i>DefaultTimeoutAbortSec=</i>, <i>DefaultRestartSec=</i></p>
<dl>
<dd>Configures the default timeouts for starting, stopping and aborting of units, as well as the default time to sleep between automatic restarts of units, as configured per-unit in <i>TimeoutStartSec=</i>, <i>TimeoutStopSec=</i>, <i>TimeoutAbortSec=</i> and <i>RestartSec=</i> (for services, see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details on the per-unit settings). Disabled by default, when service with <i>Type=oneshot</i> is used. For non-service units, <i>DefaultTimeoutStartSec=</i> sets the default <i>TimeoutSec=</i> value. <i>DefaultTimeoutStartSec=</i> and <i>DefaultTimeoutStopSec=</i> default to 90s. <i>DefaultTimeoutAbortSec=</i> is not set by default so that all units fall back to <i>TimeoutStopSec=</i>. <i>DefaultRestartSec=</i> defaults to 100ms.</dl>
<p> <i>DefaultStartLimitIntervalSec=</i>, <i>DefaultStartLimitBurst=</i></p>
<dl>
<dd>Configure the default unit start rate limiting, as configured per-service by <i>StartLimitIntervalSec=</i> and <i>StartLimitBurst=</i>. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details on the per-service settings. <i>DefaultStartLimitIntervalSec=</i> defaults to 10s. <i>DefaultStartLimitBurst=</i> defaults to 5.</dl>
<p> <i>DefaultEnvironment=</i></p>
<dl>
<dd>Configures environment variables passed to all executed processes. Takes a space-separated list of variable assignments. See <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) for details about environment variables. </p>
<p> Simple &quot;%&quot;-specifier expansion is supported, see below for a list of supported specifiers. </p>
<p> Example: </p>
<dl>
<dd>
<pre>DefaultEnvironment=&quot;VAR1=word1 word2&quot; VAR2=word3 &quot;VAR3=word 5 6&quot;</pre>
</dl>
<p> Sets three variables &quot;VAR1&quot;, &quot;VAR2&quot;, &quot;VAR3&quot;.</dl>
<p> <i>ManagerEnvironment=</i></p>
<dl>
<dd>Takes the same arguments as <i>DefaultEnvironment=</i>, see above. Sets environment variables just for the manager process itself. In contrast to user managers, these variables are not inherited by processes spawned by the system manager, use <i>DefaultEnvironment=</i> for that. Note that these variables are merged into the existing environment block. In particular, in case of the system manager, this includes variables set by the kernel based on the kernel command line. </p>
<p> Setting environment variables for the manager process may be useful to modify its behaviour. See m[blue]<code>ENVIRONMENT</code>m[]<font SIZE="-2">[2]</font> for a descriptions of some variables understood by <code>systemd</code>. </p>
<p> Simple &quot;%&quot;-specifier expansion is supported, see below for a list of supported specifiers.</dl>
<p> <i>DefaultCPUAccounting=</i>, <i>DefaultBlockIOAccounting=</i>, <i>DefaultMemoryAccounting=</i>, <i>DefaultTasksAccounting=</i>, <i>DefaultIOAccounting=</i>, <i>DefaultIPAccounting=</i></p>
<dl>
<dd>Configure the default resource accounting settings, as configured per-unit by <i>CPUAccounting=</i>, <i>BlockIOAccounting=</i>, <i>MemoryAccounting=</i>, <i>TasksAccounting=</i>, <i>IOAccounting=</i> and <i>IPAccounting=</i>. See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for details on the per-unit settings. <i>DefaultTasksAccounting=</i> defaults to yes, <i>DefaultMemoryAccounting=</i> to yes. <i>DefaultCPUAccounting=</i> defaults to yes if enabling CPU accounting doesn&#8217;t require the CPU controller to be enabled (Linux 4.15+ using the unified hierarchy for resource control), otherwise it defaults to no. The other three settings default to no.</dl>
<p> <i>DefaultTasksMax=</i></p>
<dl>
<dd>Configure the default value for the per-unit <i>TasksMax=</i> setting. See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for details. This setting applies to all unit types that support resource control settings, with the exception of slice units. Defaults to 15% of the minimum of <i>kernel.pid_max=</i>, <i>kernel.threads-max=</i> and root cgroup <i>pids.max</i>. Kernel has a default value for <i>kernel.pid_max=</i> and an algorithm of counting in case of more than 32 cores. For example with the default <i>kernel.pid_max=</i>, <i>DefaultTasksMax=</i> defaults to 4915, but might be greater in other systems or smaller in OS containers.</dl>
<p> <i>DefaultLimitCPU=</i>, <i>DefaultLimitFSIZE=</i>, <i>DefaultLimitDATA=</i>, <i>DefaultLimitSTACK=</i>, <i>DefaultLimitCORE=</i>, <i>DefaultLimitRSS=</i>, <i>DefaultLimitNOFILE=</i>, <i>DefaultLimitAS=</i>, <i>DefaultLimitNPROC=</i>, <i>DefaultLimitMEMLOCK=</i>, <i>DefaultLimitLOCKS=</i>, <i>DefaultLimitSIGPENDING=</i>, <i>DefaultLimitMSGQUEUE=</i>, <i>DefaultLimitNICE=</i>, <i>DefaultLimitRTPRIO=</i>, <i>DefaultLimitRTTIME=</i></p>
<dl>
<dd>These settings control various default resource limits for processes executed by units. See <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2) for details. These settings may be overridden in individual units using the corresponding <i>LimitXXX=</i> directives and they accept the same parameter syntax, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details. Note that these resource limits are only defaults for units, they are not applied to the service manager process (i.e. PID 1) itself. </p>
<p> Most of these settings are unset, which means the resource limits are inherited from the kernel or, if invoked in a container, from the container manager. However, the following have defaults: </p>
<dl>
<dd>&bull; <i>DefaultLimitNOFILE=</i> defaults to &quot;1024:524288&quot;.</dl>
<dl>
<dd>&bull; <i>DefaultLimitCORE=</i> does not have a default but it is worth mentioning that <i>RLIMIT_CORE</i> is set to &quot;infinity&quot; by PID 1 which is inherited by its children.</dl>
<dl>
<dd>&bull; Note that the service manager internally increases <i>RLIMIT_MEMLOCK</i> for itself, however the limit is reverted to the original value for child processes forked off.</dl>
</dl>
<p> <i>DefaultOOMPolicy=</i></p>
<dl>
<dd>Configure the default policy for reacting to processes being killed by the Linux Out-Of-Memory (OOM) killer. This may be used to pick a global default for the per-unit <i>OOMPolicy=</i> setting. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details. Note that this default is not used for services that have <i>Delegate=</i> turned on.</dl>
<h2>Specifiers</h2>
<p>Specifiers may be used in the <i>DefaultEnvironment=</i> and <i>ManagerEnvironment=</i> settings. The following expansions are understood: </p>
<p> <code>Table 1. Specifiers available</code> </p>
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
<td> A short string identifying the architecture of the local system. A string such as <code>x86</code>, <code>x86-64</code> or <code>arm64</code>. See the architectures defined for <i>ConditionArchitecture=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for a full list.
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
<td> &quot;%H&quot; </td>
<td> Host name </td>
<td> The hostname of the running system.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%l&quot; </td>
<td> Short host name </td>
<td> The hostname of the running system, truncated at the first dot to remove any domain component.
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
<td> &quot;%o&quot; </td>
<td> Operating system ID </td>
<td> The operating system identifier of the running system, as read from the <i>ID=</i> field of /etc/os-release. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%v&quot; </td>
<td> Kernel release </td>
<td> Identical to <code>uname -r</code> output.
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
<td> &quot;%T&quot; </td>
<td> Directory for temporary files </td>
<td> This is either /tmp or the path &quot;$TMPDIR&quot;, &quot;$TEMP&quot; or &quot;$TMP&quot; are set to. (Note that the directory may be specified without a trailing slash.)
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%V&quot; </td>
<td> Directory for larger and persistent temporary files </td>
<td> This is either /var/tmp or the path &quot;$TMPDIR&quot;, &quot;$TEMP&quot; or &quot;$TMP&quot; are set to. (Note that the directory may be specified without a trailing slash.)
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
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>No New Privileges Flag</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/userspace-api/no_new_privs.html">https://www.kernel.org/doc/html/latest/userspace-api/no_new_privs.html</a></dl>
<dt> 2.</p>
<dd>ENVIRONMENT</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/ENVIRONMENT">https://systemd.io/ENVIRONMENT</a></dl>
