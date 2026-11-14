---
title: "logind(5)"
name: "logind"
section: "5"
letter: "l"
url: "/docs/linux/man/5-logind/"
description: "logind.conf – Login manager configuration file"
---

<p>logind.conf &#8211; Login manager configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/logind.conf</p>
<h2>Description</h2>
<p>This file configures various parameters of the systemd login manager, <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8).</p>
<h2>Options</h2>
<p>All options are configured in the &quot;[Login]&quot; section: </p>
<p> <i>NAutoVTs=</i></p>
<dl>
<dd>Takes a positive integer. Configures how many virtual terminals (VTs) to allocate by default that, when switched to and are previously unused, &quot;autovt&quot; services are automatically spawned on. These services are instantiated from the template unit autovt [at] .service for the respective VT TTY name, for example, autovt [at] tty4.service. By default, autovt [at] .service is linked to getty [at] .service. In other words, login prompts are started dynamically as the user switches to unused virtual terminals. Hence, this parameter controls how many login &quot;gettys&quot; are available on the VTs. If a VT is already used by some other subsystem (for example, a graphical login), this kind of activation will not be attempted. Note that the VT configured in <i>ReserveVT=</i> is always subject to this kind of activation, even if it is not one of the VTs configured with the <i>NAutoVTs=</i> directive. Defaults to 6. When set to 0, automatic spawning of &quot;autovt&quot; services is disabled.</dl>
<p> <i>ReserveVT=</i></p>
<dl>
<dd>Takes a positive integer. Identifies one virtual terminal that shall unconditionally be reserved for autovt [at] .service activation (see above). The VT selected with this option will be marked busy unconditionally, so that no other subsystem will allocate it. This functionality is useful to ensure that, regardless of how many VTs are allocated by other subsystems, one login &quot;getty&quot; is always available. Defaults to 6 (in other words, there will always be a &quot;getty&quot; available on Alt-F6.). When set to 0, VT reservation is disabled.</dl>
<p> <i>KillUserProcesses=</i></p>
<dl>
<dd>Takes a boolean argument. Configures whether the processes of a user should be killed when the user completely logs out (i.e. after the user&#8217;s last session ended). Defaults to &quot;no&quot;. </p>
<p> Note that setting <i>KillUserProcesses=1</i> will break tools like <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1).</dl>
<p> <i>KillOnlyUsers=</i>, <i>KillExcludeUsers=</i></p>
<dl>
<dd>These settings take space-separated lists of usernames that influence the effect of <i>KillUserProcesses=</i>. If not empty, only processes of users listed in <i>KillOnlyUsers=</i> will be killed when they log out entirely. Processes of users listed in <i>KillExcludeUsers=</i> are excluded from being killed. <i>KillExcludeUsers=</i> defaults to &quot;root&quot; and takes precedence over <i>KillOnlyUsers=</i>, which defaults to the empty list.</dl>
<p> <i>IdleAction=</i></p>
<dl>
<dd>Configures the action to take when the system is idle. Takes one of &quot;ignore&quot;, &quot;poweroff&quot;, &quot;reboot&quot;, &quot;halt&quot;, &quot;kexec&quot;, &quot;suspend&quot;, &quot;hibernate&quot;, &quot;hybrid-sleep&quot;, and &quot;lock&quot;. Defaults to &quot;ignore&quot;. </p>
<p> Note that this requires that user sessions correctly report the idle status to the system. The system will execute the action after all sessions report that they are idle, no idle inhibitor lock is active, and subsequently, the time configured with <i>IdleActionSec=</i> (see below) has expired.</dl>
<p> <i>IdleActionSec=</i></p>
<dl>
<dd>Configures the delay after which the action configured in <i>IdleAction=</i> (see above) is taken after the system is idle.</dl>
<p> <i>InhibitDelayMaxSec=</i></p>
<dl>
<dd>Specifies the maximum time a system shutdown or sleep request is delayed due to an inhibitor lock of type &quot;delay&quot; being active before the inhibitor is ignored and the operation executes anyway. Defaults to 5.</dl>
<p> <i>HandlePowerKey=</i>, <i>HandleSuspendKey=</i>, <i>HandleHibernateKey=</i>, <i>HandleLidSwitch=</i>, <i>HandleLidSwitchDocked=</i></p>
<dl>
<dd>Controls whether logind shall handle the system power and sleep keys and the lid switch to trigger actions such as system power-off or suspend. Can be one of &quot;ignore&quot;, &quot;poweroff&quot;, &quot;reboot&quot;, &quot;halt&quot;, &quot;kexec&quot;, &quot;suspend&quot;, &quot;hibernate&quot;, &quot;hybrid-sleep&quot;, and &quot;lock&quot;. If &quot;ignore&quot;, logind will never handle these keys. If &quot;lock&quot;, all running sessions will be screen-locked; otherwise, the specified action will be taken in the respective event. Only input devices with the &quot;power-switch&quot; udev tag will be watched for key/lid switch events. <i>HandlePowerKey=</i> defaults to &quot;poweroff&quot;. <i>HandleSuspendKey=</i> and <i>HandleLidSwitch=</i> default to &quot;suspend&quot;. <i>HandleLidSwitchDocked=</i> defaults to &quot;ignore&quot;. <i>HandleHibernateKey=</i> defaults to &quot;hibernate&quot;. If the system is inserted in a docking station, or if more than one display is connected, the action specified by <i>HandleLidSwitchDocked=</i> occurs; otherwise the <i>HandleLidSwitch=</i> action occurs.</dl>
<p> <i>PowerKeyIgnoreInhibited=</i>, <i>SuspendKeyIgnoreInhibited=</i>, <i>HibernateKeyIgnoreInhibited=</i>, <i>LidSwitchIgnoreInhibited=</i></p>
<dl>
<dd>Controls whether actions triggered by the power and sleep keys and the lid switch are subject to inhibitor locks. These settings take boolean arguments. If &quot;off&quot;, the inhibitor locks taken by applications in order to block the requested operation are respected. If &quot;on&quot;, the requested operation is executed in any case. <i>PowerKeyIgnoreInhibited=</i>, <i>SuspendKeyIgnoreInhibited=</i> and <i>HibernateKeyIgnoreInhibited=</i> default to &quot;off&quot;. <i>LidSwitchIgnoreInhibited=</i> defaults to &quot;yes&quot;. This means that the lid switch does not respect suspend blockers by default, but the power and sleep keys do.</dl>
<p> <i>RuntimeDirectorySize=</i></p>
<dl>
<dd>Sets the size limit on the <i>$XDG_RUNTIME_DIR</i> runtime directory for each user who logs in. Takes a size in bytes, optionally suffixed with the usual K, G, M, and T suffixes, to the base 1024 (IEC). Alternatively, a numerical percentage suffixed by &quot;%&quot; may be specified, which sets the size limit relative to the amount of physical RAM. Defaults to 10%. Note that this size is a safety limit only. As each runtime directory is a tmpfs file system, it will only consume as much memory as is needed.</dl>
<p> <i>RemoveIPC=</i></p>
<dl>
<dd>Controls whether System V and POSIX IPC objects belonging to the user shall be removed when the user fully logs out. Takes a boolean argument. If enabled, the user may not consume IPC resources after the last of the user&#8217;s sessions terminated. This covers System V semaphores, shared memory and message queues, as well as POSIX shared memory and message queues. Note that IPC objects of the root user are excluded from the effect of this setting. Defaults to &quot;yes&quot;.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8), <code><a href="/docs/linux/man/1-loginctl/">loginctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5) </p>
