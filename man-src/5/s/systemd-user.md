---
title: "systemd-user(5)"
name: "systemd-user"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-user/"
description: "systemd-system.conf, systemd-user.conf – System and session service manager configuration file"
---

<p>systemd-system.conf, systemd-user.conf &#8211; System and session service manager configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/system.conf </p>
<p> /etc/systemd/user.conf</p>
<h2>Description</h2>
<p>When run as system instance systemd reads the configuration file system.conf, otherwise user.conf. These configuration files contain a few settings controlling basic manager operations.</p>
<h2>Options</h2>
<p>All options are configured in the &quot;[Manager]&quot; section: </p>
<p> <i>LogLevel=</i>, <i>LogTarget=</i>, <i>LogColor=</i>, <i>LogLocation=</i>, <i>DumpCore=yes</i>, <i>CrashShell=no</i>, <i>ShowStatus=yes</i>, <i>CrashChVT=1</i>, <i>DefaultStandardOutput=journal</i>, <i>DefaultStandardError=inherit</i></p>
<dl>
<dd>Configures various parameters of basic manager operation. These options may be overridden by the respective command line arguments. See <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) for details about these command line arguments.</dl>
<p> <i>CPUAffinity=</i></p>
<dl>
<dd>Configures the initial CPU affinity for the init process. Takes a space-separated list of CPU indices.</dl>
<p> <i>JoinControllers=cpu,cpuacct net_cls,netprio</i></p>
<dl>
<dd>Configures controllers that shall be mounted in a single hierarchy. By default, systemd will mount all controllers which are enabled in the kernel in individual hierarchies, with the exception of those listed in this setting. Takes a space-separated list of comma-separated controller names, in order to allow multiple joined hierarchies. Defaults to &#8216;cpu,cpuacct&#8217;. Pass an empty string to ensure that systemd mounts all controllers in separate hierarchies. </p>
<p> Note that this option is only applied once, at very early boot. If you use an initial RAM disk (initrd) that uses systemd, it might hence be necessary to rebuild the initrd if this option is changed, and make sure the new configuration file is included in it. Otherwise, the initrd might mount the controller hierarchies in a different configuration than intended, and the main system cannot remount them anymore.</dl>
<p> <i>RuntimeWatchdogSec=</i>, <i>ShutdownWatchdogSec=</i></p>
<dl>
<dd>Configure the hardware watchdog at runtime and at reboot. Takes a timeout value in seconds (or in other time units if suffixed with &quot;ms&quot;, &quot;min&quot;, &quot;h&quot;, &quot;d&quot;, &quot;w&quot;). If <i>RuntimeWatchdogSec=</i> is set to a non-zero value, the watchdog hardware (/dev/watchdog) will be programmed to automatically reboot the system if it is not contacted within the specified timeout interval. The system manager will ensure to contact it at least once in half the specified timeout interval. This feature requires a hardware watchdog device to be present, as it is commonly the case in embedded and server systems. Not all hardware watchdogs allow configuration of the reboot timeout, in which case the closest available timeout is picked. <i>ShutdownWatchdogSec=</i> may be used to configure the hardware watchdog when the system is asked to reboot. It works as a safety net to ensure that the reboot takes place even if a clean reboot attempt times out. By default <i>RuntimeWatchdogSec=</i> defaults to 0 (off), and <i>ShutdownWatchdogSec=</i> to 10min. These settings have no effect if a hardware watchdog is not available.</dl>
<p> <i>CapabilityBoundingSet=</i></p>
<dl>
<dd>Controls which capabilities to include in the capability bounding set for PID 1 and its children. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for details. Takes a whitespace-separated list of capability names as read by <code><a href="/docs/linux/man/3-cap_from_name/">cap_from_name</a></code>(3). Capabilities listed will be included in the bounding set, all others are removed. If the list of capabilities is prefixed with ~, all but the listed capabilities will be included, the effect of the assignment inverted. Note that this option also affects the respective capabilities in the effective, permitted and inheritable capability sets. The capability bounding set may also be individually configured for units using the <i>CapabilityBoundingSet=</i> directive for units, but note that capabilities dropped for PID 1 cannot be regained in individual units, they are lost for good.</dl>
<p> <i>SystemCallArchitectures=</i></p>
<dl>
<dd>Takes a space-separated list of architecture identifiers. Selects from which architectures system calls may be invoked on this system. This may be used as an effective way to disable invocation of non-native binaries system-wide, for example to prohibit execution of 32-bit x86 binaries on 64-bit x86-64 systems. This option operates system-wide, and acts similar to the <i>SystemCallArchitectures=</i> setting of unit files, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details. This setting defaults to the empty list, in which case no filtering of system calls based on architecture is applied. Known architecture identifiers are &quot;x86&quot;, &quot;x86-64&quot;, &quot;x32&quot;, &quot;arm&quot; and the special identifier &quot;native&quot;. The latter implicitly maps to the native architecture of the system (or more specifically, the architecture the system manager was compiled for). Set this setting to &quot;native&quot; to prohibit execution of any non-native binaries. When a binary executes a system call of an architecture that is not listed in this setting, it will be immediately terminated with the SIGSYS signal.</dl>
<p> <i>TimerSlackNSec=</i></p>
<dl>
<dd>Sets the timer slack in nanoseconds for PID 1, which is inherited by all executed processes, unless overridden individually, for example with the <i>TimerSlackNSec=</i> setting in service units (for details see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5)). The timer slack controls the accuracy of wake-ups triggered by system timers. See <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) for more information. Note that in contrast to most other time span definitions this parameter takes an integer value in nano-seconds if no unit is specified. The usual time units are understood too.</dl>
<p> <i>DefaultTimerAccuracySec=</i></p>
<dl>
<dd>Sets the default accuracy of timer units. This controls the global default for the <i>AccuracySec=</i> setting of timer units, see <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5) for details. <i>AccuracySec=</i> set in individual units override the global default for the specific unit. Defaults to 1min. Note that the accuracy of timer units is also affected by the configured timer slack for PID 1, see <i>TimerSlackNSec=</i> above.</dl>
<p> <i>DefaultTimeoutStartSec=</i>, <i>DefaultTimeoutStopSec=</i>, <i>DefaultRestartSec=</i></p>
<dl>
<dd>Configures the default timeouts for starting and stopping of units, as well as the default time to sleep between automatic restarts of units, as configured per-unit in <i>TimeoutStartSec=</i>, <i>TimeoutStopSec=</i> and <i>RestartSec=</i> (for services, see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details on the per-unit settings). For non-service units, <i>DefaultTimeoutStartSec=</i> sets the default <i>TimeoutSec=</i> value.</dl>
<p> <i>DefaultStartLimitInterval=</i>, <i>DefaultStartLimitBurst=</i></p>
<dl>
<dd>Configure the default unit start rate limiting, as configured per-service by <i>StartLimitInterval=</i> and <i>StartLimitBurst=</i>. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details on the per-service settings.</dl>
<p> <i>DefaultEnvironment=</i></p>
<dl>
<dd>Sets manager environment variables passed to all executed processes. Takes a space-separated list of variable assignments. See <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) for details about environment variables. </p>
<p> Example: </p>
<dl>
<dd>
<pre>DefaultEnvironment=&quot;VAR1=word1 word2&quot; VAR2=word3 &quot;VAR3=word 5 6&quot;</pre>
</dl>
<p> Sets three variables &quot;VAR1&quot;, &quot;VAR2&quot;, &quot;VAR3&quot;.</dl>
<p> <i>DefaultCPUAccounting=</i>, <i>DefaultBlockIOAccounting=</i>, <i>DefaultMemoryAccounting=</i></p>
<dl>
<dd>Configure the default resource accounting settings, as configured per-unit by <i>CPUAccounting=</i>, <i>BlockIOAccounting=</i> and <i>MemoryAccounting=</i>. See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for details on the per-unit settings.</dl>
<p> <i>DefaultLimitCPU=</i>, <i>DefaultLimitFSIZE=</i>, <i>DefaultLimitDATA=</i>, <i>DefaultLimitSTACK=</i>, <i>DefaultLimitCORE=</i>, <i>DefaultLimitRSS=</i>, <i>DefaultLimitNOFILE=</i>, <i>DefaultLimitAS=</i>, <i>DefaultLimitNPROC=</i>, <i>DefaultLimitMEMLOCK=</i>, <i>DefaultLimitLOCKS=</i>, <i>DefaultLimitSIGPENDING=</i>, <i>DefaultLimitMSGQUEUE=</i>, <i>DefaultLimitNICE=</i>, <i>DefaultLimitRTPRIO=</i>, <i>DefaultLimitRTTIME=</i></p>
<dl>
<dd>These settings control various default resource limits for units. See <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2) for details. Use the string <i>infinity</i> to configure no limit on a specific resource. These settings may be overridden in individual units using the corresponding LimitXXX= directives. Note that these resource limits are only defaults for units, they are not applied to PID 1 itself.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) </p>
