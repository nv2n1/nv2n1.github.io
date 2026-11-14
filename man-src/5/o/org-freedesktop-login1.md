---
title: "org-freedesktop-login1(5)"
name: "org-freedesktop-login1"
section: "5"
letter: "o"
url: "/docs/linux/man/5-org-freedesktop-login1/"
description: "org.freedesktop.login1 – The D-Bus interface of systemd-logind"
---

<p>org.freedesktop.login1 &#8211; The D-Bus interface of systemd-logind</p>
<h2>Introduction</h2>
<p><code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8) is a system service that keeps track of user logins and seats. </p>
<p> The daemon provides both a C library interface as well as a D-Bus interface. The library interface may be used to introspect and watch the state of user logins and seats. The bus interface provides the same functionality but in addition may also be used to make changes to the system state. For more information please consult <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3).</p>
<h2>The Manager Object</h2>
<p>The service exposes the following interfaces on the Manager object on the bus: </p>
<dl>
<dd>
<pre>node /org/freedesktop/login1 {
 interface org.freedesktop.login1.Manager {
 methods:
 GetSession(in s session_id,
 out o object_path);
 GetSessionByPID(in u pid,
 out o object_path);
 GetUser(in u uid,
 out o object_path);
 GetUserByPID(in u pid,
 out o object_path);
 GetSeat(in s seat_id,
 out o object_path);
 ListSessions(out a(susso) sessions);
 ListUsers(out a(uso) users);
 ListSeats(out a(so) seats);
 ListInhibitors(out a(ssssuu) inhibitors);
 CreateSession(in u uid,
 in u pid,
 in s service,
 in s type,
 in s class,
 in s desktop,
 in s seat_id,
 in u vtnr,
 in s tty,
 in s display,
 in b remote,
 in s remote_user,
 in s remote_host,
 in a(sv) properties,
 out s session_id,
 out o object_path,
 out s runtime_path,
 out h fifo_fd,
 out u uid,
 out s seat_id,
 out u vtnr,
 out b existing);
 ReleaseSession(in s session_id);
 ActivateSession(in s session_id);
 ActivateSessionOnSeat(in s session_id,
 in s seat_id);
 LockSession(in s session_id);
 UnlockSession(in s session_id);
 LockSessions();
 UnlockSessions();
 KillSession(in s session_id,
 in s who,
 in i signal_number);
 KillUser(in u uid,
 in i signal_number);
 TerminateSession(in s session_id);
 TerminateUser(in u uid);
 TerminateSeat(in s seat_id);
 SetUserLinger(in u uid,
 in b enable,
 in b interactive);
 AttachDevice(in s seat_id,
 in s sysfs_path,
 in b interactive);
 FlushDevices(in b interactive);
 PowerOff(in b interactive);
 PowerOffWithFlags(in t flags);
 Reboot(in b interactive);
 RebootWithFlags(in t flags);
 Halt(in b interactive);
 HaltWithFlags(in t flags);
 Suspend(in b interactive);
 SuspendWithFlags(in t flags);
 Hibernate(in b interactive);
 HibernateWithFlags(in t flags);
 HybridSleep(in b interactive);
 HybridSleepWithFlags(in t flags);
 SuspendThenHibernate(in b interactive);
 SuspendThenHibernateWithFlags(in t flags);
 CanPowerOff(out s result);
 CanReboot(out s result);
 CanHalt(out s result);
 CanSuspend(out s result);
 CanHibernate(out s result);
 CanHybridSleep(out s result);
 CanSuspendThenHibernate(out s result);
 ScheduleShutdown(in s type,
 in t usec);
 CancelScheduledShutdown(out b cancelled);
 Inhibit(in s what,
 in s who,
 in s why,
 in s mode,
 out h pipe_fd);
 CanRebootParameter(out s result);
 SetRebootParameter(in s parameter);
 CanRebootToFirmwareSetup(out s result);
 SetRebootToFirmwareSetup(in b enable);
 CanRebootToBootLoaderMenu(out s result);
 SetRebootToBootLoaderMenu(in t timeout);
 CanRebootToBootLoaderEntry(out s result);
 SetRebootToBootLoaderEntry(in s boot_loader_entry);
 SetWallMessage(in s wall_message,
 in b enable);
 signals:
 SessionNew(s session_id,
 o object_path);
 SessionRemoved(s session_id,
 o object_path);
 UserNew(u uid,
 o object_path);
 UserRemoved(u uid,
 o object_path);
 SeatNew(s seat_id,
 o object_path);
 SeatRemoved(s seat_id,
 o object_path);
 PrepareForShutdown(b start);
 PrepareForSleep(b start);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
 readwrite b EnableWallMessages = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
 readwrite s WallMessage = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u NAutoVTs = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as KillOnlyUsers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as KillExcludeUsers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b KillUserProcesses = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s RebootParameter = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b RebootToFirmwareSetup = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t RebootToBootLoaderMenu = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s RebootToBootLoaderEntry = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as BootLoaderEntries = ['...', ...];
 readonly b IdleHint = ...;
 readonly t IdleSinceHint = ...;
 readonly t IdleSinceHintMonotonic = ...;
 readonly s BlockInhibited = '...';
 readonly s DelayInhibited = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InhibitDelayMaxUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t UserStopDelayUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s HandlePowerKey = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s HandleSuspendKey = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s HandleHibernateKey = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s HandleLidSwitch = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s HandleLidSwitchExternalPower = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s HandleLidSwitchDocked = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t HoldoffTimeoutUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s IdleAction = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t IdleActionUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b PreparingForShutdown = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b PreparingForSleep = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly (st) ScheduledShutdown = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b Docked = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b LidClosed = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b OnExternalPower = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RemoveIPC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RuntimeDirectorySize = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RuntimeDirectoryInodesMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InhibitorsMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t NCurrentInhibitors = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t SessionsMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t NCurrentSessions = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>GetSession()</code> may be used to get the session object path for the session with the specified ID. Similarly, <code>GetUser()</code> and <code>GetSeat()</code> get the user and seat objects, respectively. <code>GetSessionByPID()</code> and <code>GetUserByPID()</code> get the session/user object the specified PID belongs to if there is any. </p>
<p> <code>ListSessions()</code> returns an array of all current sessions. The structures in the array consist of the following fields: session id, user id, user name, seat id, session object path. If a session does not have a seat attached, the seat id field will be an empty string. </p>
<p> <code>ListUsers()</code> returns an array of all currently logged in users. The structures in the array consist of the following fields: user id, user name, user object path. </p>
<p> <code>ListSeats()</code> returns an array of all currently available seats. The structure in the array consists of the following fields: seat id, seat object path. </p>
<p> <code>ListInhibitors()</code> lists all currently active inhibitors. It returns an array of structures consisting of <i>what</i>, <i>who</i>, <i>why</i>, <i>mode</i>, <i>uid</i> (user ID), and <i>pid</i> (process ID). </p>
<p> <code>CreateSession()</code> and <code>ReleaseSession()</code> may be used to open or close login sessions. These calls should <i>never</i> be invoked directly by clients. Creating/closing sessions is exclusively the job of PAM and its <code><a href="/docs/linux/man/8-pam_systemd/">pam_systemd</a></code>(8) module. </p>
<p> <code>ActivateSession()</code> brings the session with the specified ID into the foreground. <code>ActivateSessionOnSeat()</code> does the same, but only if the seat id matches. </p>
<p> <code>LockSession()</code> asks the session with the specified ID to activate the screen lock. <code>UnlockSession()</code> asks the session with the specified ID to remove an active screen lock, if there is any. This is implemented by sending out the Lock() and Unlock() signals from the respective session object which session managers are supposed to listen on. </p>
<p> <code>LockSessions()</code> asks all sessions to activate their screen locks. This may be used to lock access to the entire machine in one action. Similarly, <code>UnlockSessions()</code> asks all sessions to deactivate their screen locks. </p>
<p> <code>KillSession()</code> may be used to send a Unix signal to one or all processes of a session. As arguments it takes the session id, either the string &quot;leader&quot; or &quot;all&quot; and a signal number. If &quot;leader&quot; is passed only the session &quot;leader&quot; is killed. If &quot;all&quot; is passed all processes of the session are killed. </p>
<p> <code>KillUser()</code> may be used to send a Unix signal to all processes of a user. As arguments it takes the user id and a signal number. </p>
<p> <code>TerminateSession()</code>, <code>TerminateUser()</code>, <code>TerminateSeat()</code> may be used to forcibly terminate one specific session, all processes of a user, and all sessions attached to a specific seat, respectively. The session, user, and seat are identified by their respective IDs. </p>
<p> <code>SetUserLinger()</code> enables or disables user lingering. If enabled, the runtime directory of a user is kept around and they may continue to run processes while logged out. If disabled, the runtime directory goes away as soon as they log out. <code>SetUserLinger()</code> expects three arguments: the UID, a boolean whether to enable/disable and a boolean controlling the m[blue]<code>polkit</code>m[]<font SIZE="-2">[1]</font> authorization interactivity (see below). Note that the user linger state is persistently stored on disk. </p>
<p> <code>AttachDevice()</code> may be used to assign a specific device to a specific seat. The device is identified by its /sys/ path and must be eligible for seat assignments. <code>AttachDevice()</code> takes three arguments: the seat id, the sysfs path, and a boolean for controlling polkit interactivity (see below). Device assignments are persistently stored on disk. To create a new seat, simply specify a previously unused seat id. For more information about the seat assignment logic see <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3). </p>
<p> <code>FlushDevices()</code> removes all explicit seat assignments for devices, resetting all assignments to the automatic defaults. The only argument it takes is the polkit interactivity boolean (see below). </p>
<p> <code>PowerOff()</code>, <code>Reboot()</code>, <code>Halt()</code>, <code>Suspend()</code>, and <code>Hibernate()</code> result in the system being powered off, rebooted, halted (shut down without turning off power), suspended (the system state is saved to RAM and the CPU is turned off), or hibernated (the system state is saved to disk and the machine is powered down). <code>HybridSleep()</code> results in the system entering a hybrid-sleep mode, i.e. the system is both hibernated and suspended. <code>SuspendThenHibernate()</code> results in the system being suspended, then later woken using an RTC timer and hibernated. The only argument is the polkit interactivity boolean <i>interactive</i> (see below). The main purpose of these calls is that they enforce polkit policy and hence allow powering off/rebooting/suspending/hibernating even by unprivileged users. They also enforce inhibition locks for non-privileged users. UIs should expose these calls as the primary mechanism to poweroff/reboot/suspend/hibernate the machine. Methods <code>PowerOffWithFlags()</code>, <code>RebootWithFlags()</code>, <code>HaltWithFlags()</code>, <code>SuspendWithFlags()</code>, <code>HibernateWithFlags()</code>, <code>HybridSleepWithFlags()</code> and <code>SuspendThenHibernateWithFlags()</code> add <i>flags</i> to allow for extendability, defined as follows: </p>
<dl>
<dd>
<pre>#define SD_LOGIND_ROOT_CHECK_INHIBITORS (<a href="//www.systutorials.com/docs/linux/man/1-UINT64_C/">UINT64_C</a>(1) &lt;&lt; 0)
#define SD_LOGIND_KEXEC_REBOOT (<a href="//www.systutorials.com/docs/linux/man/1-UINT64_C/">UINT64_C</a>(1) &lt;&lt; 1)</pre>
</dl>
<p> When the <i>flags</i> is 0 then these methods behave just like the versions without flags. When <code>SD_LOGIND_ROOT_CHECK_INHIBITORS</code> (0x01) is set, active inhibitors are honoured for privileged users too. When <code>SD_LOGIND_KEXEC_REBOOT</code> (0x02) is set, then <code>RebootWithFlags()</code> perform kexec reboot if kexec kernel is loaded. </p>
<p> <code>SetRebootParameter()</code> sets a parameter for a subsequent reboot operation. See the description of <code>reboot</code> in <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) and <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2) for more information. </p>
<p> <code>SetRebootToFirmwareSetup()</code>, <code>SetRebootToBootLoaderMenu()</code>, and <code>SetRebootToBootLoaderEntry()</code> configure the action to be taken from the boot loader after a reboot: respectively entering firmware setup mode, the boot loader menu, or a specific boot loader entry. See <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) for the corresponding command line interface. </p>
<p> <code>CanPowerOff()</code>, <code>CanReboot()</code>, <code>CanHalt()</code>, <code>CanSuspend()</code>, <code>CanHibernate()</code>, <code>CanHybridSleep()</code>, <code>CanSuspendThenHibernate()</code>, <code>CanRebootParameter()</code>, <code>CanRebootToFirmwareSetup()</code>, <code>CanRebootToBootLoaderMenu()</code>, and <code>CanRebootToBootLoaderEntry()</code> test whether the system supports the respective operation and whether the calling user is allowed to execute it. Returns one of &quot;na&quot;, &quot;yes&quot;, &quot;no&quot;, and &quot;challenge&quot;. If &quot;na&quot; is returned, the operation is not available because hardware, kernel, or drivers do not support it. If &quot;yes&quot; is returned, the operation is supported and the user may execute the operation without further authentication. If &quot;no&quot; is returned, the operation is available but the user is not allowed to execute the operation. If &quot;challenge&quot; is returned, the operation is available but only after authorization. </p>
<p> <code>ScheduleShutdown()</code> schedules a shutdown operation <i>type</i> at time <i>usec</i> in microseconds since the UNIX epoch. <i>type</i> can be one of &quot;poweroff&quot;, &quot;dry-poweroff&quot;, &quot;reboot&quot;, &quot;dry-reboot&quot;, &quot;halt&quot;, and &quot;dry-halt&quot;. (The &quot;dry-&quot; variants do not actually execute the shutdown action.) <code>CancelScheduledShutdown()</code> cancels a scheduled shutdown. The output parameter <i>cancelled</i> is true if a shutdown operation was scheduled. </p>
<p> <code>SetWallMessage()</code> sets the wall message (the message that will be sent out to all terminals and stored in a <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5) record) for a subsequent scheduled shutdown operation. The parameter <i>wall_message</i> specifies the shutdown reason (and may be empty) which will be included in the shutdown message. The parameter <i>enable</i> specifies whether to print a wall message on shutdown. </p>
<p> <code>Inhibit()</code> creates an inhibition lock. It takes four parameters: <i>what</i>, <i>who</i>, <i>why</i>, and <i>mode</i>. <i>what</i> is one or more of &quot;shutdown&quot;, &quot;sleep&quot;, &quot;idle&quot;, &quot;handle-power-key&quot;, &quot;handle-suspend-key&quot;, &quot;handle-hibernate-key&quot;, &quot;handle-lid-switch&quot;, separated by colons, for inhibiting poweroff/reboot, suspend/hibernate, the automatic idle logic, or hardware key handling. <i>who</i> should be a short human readable string identifying the application taking the lock. <i>why</i> should be a short human readable string identifying the reason why the lock is taken. Finally, <i>mode</i> is either &quot;block&quot; or &quot;delay&quot; which encodes whether the inhibit shall be consider mandatory or whether it should just delay the operation to a certain maximum time. The method returns a file descriptor. The lock is released the moment this file descriptor and all its duplicates are closed. For more information on the inhibition logic see m[blue]<code>Inhibitor Locks</code>m[]<font SIZE="-2">[2]</font>.</p>
<h3>Signals</h3>
<p>Whenever the inhibition state or idle hint changes, <code>PropertyChanged</code> signals are sent out to which clients can subscribe. </p>
<p> The <code>SessionNew</code>, <code>SessionRemoved</code>, <code>UserNew</code>, <code>UserRemoved</code>, <code>SeatNew</code>, and <code>SeatRemoved</code> signals are sent each time a session is created or removed, a user logs in or out, or a seat is added or removed. They each contain the ID of the object plus the object path. </p>
<p> The <code>PrepareForShutdown()</code> and <code>PrepareForSleep()</code> signals are sent right before (with the argument &quot;true&quot;) or after (with the argument &quot;false&quot;) the system goes down for reboot/poweroff and suspend/hibernate, respectively. This may be used by applications to save data on disk, release memory, or do other jobs that should be done shortly before shutdown/sleep, in conjunction with delay inhibitor locks. After completion of this work they should release their inhibition locks in order to not delay the operation any further. For more information see m[blue]<code>Inhibitor Locks</code>m[]<font SIZE="-2">[2]</font>.</p>
<h3>Properties</h3>
<p>Most properties simply reflect the configuration, see <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5). This includes: <i>NAutoVTs</i>, <i>KillOnlyUsers</i>, <i>KillExcludeUsers</i>, <i>KillUserProcesses</i>, <i>IdleAction</i>, <i>InhibitDelayMaxUSec</i>, <i>InhibitorsMax</i>, <i>UserStopDelayUSec</i>, <i>HandlePowerKey</i>, <i>HandleSuspendKey</i>, <i>HandleHibernateKey</i>, <i>HandleLidSwitch</i>, <i>HandleLidSwitchExternalPower</i>, <i>HandleLidSwitchDocked</i>, <i>IdleActionUSec</i>, <i>HoldoffTimeoutUSec</i>, <i>RemoveIPC</i>, <i>RuntimeDirectorySize</i>, <i>RuntimeDirectoryInodesMax</i>, <i>InhibitorsMax</i>, and <i>SessionsMax</i>. </p>
<p> The <i>IdleHint</i> property reflects the idle hint state of the system. If the system is idle it might get into automatic suspend or shutdown depending on the configuration. </p>
<p> <i>IdleSinceHint</i> and <i>IdleSinceHintMonotonic</i> encode the timestamps of the last change of the idle hint boolean, in <code>CLOCK_REALTIME</code> and <code>CLOCK_MONOTONIC</code> timestamps, respectively, in microseconds since the epoch. </p>
<p> The <i>BlockInhibited</i> and <i>DelayInhibited</i> properties encode the currently active locks of the respective modes. They are colon separated lists of &quot;shutdown&quot;, &quot;sleep&quot;, and &quot;idle&quot; (see above). </p>
<p> <i>NCurrentSessions</i> and <i>NCurrentInhibitors</i> contain the number of currently registered sessions and inhibitors. </p>
<p> The <i>BootLoaderEntries</i> property contains a list of boot loader entries. This includes boot loader entries defined in configuration and any additional loader entries reported by the boot loader. See <code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7) for more information. </p>
<p> The <i>PreparingForShutdown</i> and <i>PreparingForSleep</i> boolean properties are true during the interval between the two <code>PrepareForShutdown</code> and <code>PrepareForSleep</code> signals respectively. Note that these properties do not send out <code>PropertyChanged</code> signals. </p>
<p> The <i>RebootParameter</i> property shows the value set with the <code>SetRebootParameter()</code> method described above. </p>
<p> <i>ScheduledShutdown</i> shows the value pair set with the <code>ScheduleShutdown()</code> method described above. </p>
<p> <i>RebootToFirmwareSetup</i>, <i>RebootToBootLoaderMenu</i>, and <i>RebootToBootLoaderEntry</i> are true when the resprective post-reboot operation was selected with <code>SetRebootToFirmwareSetup</code>, <code>SetRebootToBootLoaderMenu</code>, or <code>SetRebootToBootLoaderEntry</code>. </p>
<p> The <i>WallMessage</i> and <i>EnableWallMessages</i> properties reflect the shutdown reason and wall message enablement switch which can be set with the <code>SetWallMessage()</code> method described above. </p>
<p> <i>Docked</i> is true if the machine is connected to a dock. <i>LidClosed</i> is true when the lid (of a laptop) is closed. <i>OnExternalPower</i> is true when the machine is connected to an external power supply.</p>
<h3>Security</h3>
<p>A number of operations are protected via the polkit privilege system. <code>SetUserLinger()</code> requires the org.freedesktop.login1.set-user-linger privilege. <code>AttachDevice()</code> requires org.freedesktop.login1.attach-device and <code>FlushDevices()</code> requires org.freedesktop.login1.flush-devices. <code>PowerOff()</code>, <code>Reboot()</code>, <code>Halt()</code>, <code>Suspend()</code>, <code>Hibernate()</code> require org.freedesktop.login1.power-off, org.freedesktop.login1.power-off-multiple-sessions, org.freedesktop.login1.power-off-ignore-inhibit, org.freedesktop.login1.reboot, org.freedesktop.login1.reboot-multiple-sessions, org.freedesktop.login1.reboot-ignore-inhibit, org.freedesktop.login1.halt, org.freedesktop.login1.halt-multiple-sessions, org.freedesktop.login1.halt-ignore-inhibit, org.freedesktop.login1.suspend, org.freedesktop.login1.suspend-multiple-sessions, org.freedesktop.login1.suspend-ignore-inhibit, org.freedesktop.login1.hibernate, org.freedesktop.login1.hibernate-multiple-sessions, org.freedesktop.login1.hibernate-ignore-inhibit, respectively depending on whether there are other sessions around or active inhibits are present. <code>HybridSleep()</code> and <code>SuspendThenHibernate()</code> use the same privileges as <code>Hibernate()</code>. <code>SetRebootParameter()</code> requires org.freedesktop.login1.set-reboot-parameter. </p>
<p> <code>SetRebootToFirmwareSetup</code> requires org.freedesktop.login1.set-reboot-to-firmware-setup. <code>SetRebootToBootLoaderMenu</code> requires org.freedesktop.login1.set-reboot-to-boot-loader-menu. <code>SetRebootToBootLoaderEntry</code> requires org.freedesktop.login1.set-reboot-to-boot-loader-entry. </p>
<p> <code>ScheduleShutdown</code> and <code>CancelScheduledShutdown</code> require the same privileges (listed above) as the immediate poweroff/reboot/halt operations. </p>
<p> <code>Inhibit()</code> is protected via one of org.freedesktop.login1.inhibit-block-shutdown, org.freedesktop.login1.inhibit-delay-shutdown, org.freedesktop.login1.inhibit-block-sleep, org.freedesktop.login1.inhibit-delay-sleep, org.freedesktop.login1.inhibit-block-idle, org.freedesktop.login1.inhibit-handle-power-key, org.freedesktop.login1.inhibit-handle-suspend-key, org.freedesktop.login1.inhibit-handle-hibernate-key, org.freedesktop.login1.inhibit-handle-lid-switch depending on the lock type and mode taken. </p>
<p> The <i>interactive</i> boolean parameters can be used to control whether polkit should interactively ask the user for authentication credentials if required.</p>
<h2>Seat Objects</h2>
<dl>
<dd>
<pre>node /org/freedesktop/login1/seat/seat0 {
 interface org.freedesktop.login1.Seat {
 methods:
 Terminate();
 ActivateSession(in s session_id);
 SwitchTo(in u vtnr);
 SwitchToNext();
 SwitchToPrevious();
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Id = '...';
 readonly (so) ActiveSession = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CanTTY = ...;
 readonly b CanGraphical = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(so) Sessions = [...];
 readonly b IdleHint = ...;
 readonly t IdleSinceHint = ...;
 readonly t IdleSinceHintMonotonic = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>Terminate()</code> and <code>ActivateSession()</code> work similar to TerminateSeat(), ActivationSessionOnSeat() on the Manager object. </p>
<p> <code>SwitchTo()</code> switches to the session on the virtual terminal <i>vtnr</i>. <code>SwitchToNext()</code> and <code>SwitchToPrevious()</code> switch to, respectively, the next and previous sessions on the seat in the order of virtual terminals. If there is no active session, they switch to, respectively, the first and last session on the seat.</p>
<h3>Signals</h3>
<p>Whenever <code>ActiveSession</code>, <code>Sessions</code>, <code>CanGraphical</code>, <code>CanTTY</code>, or the idle state changes, <code>PropertyChanged</code> signals are sent out to which clients can subscribe.</p>
<h3>Properties</h3>
<p>The <i>Id</i> property encodes the ID of the seat. </p>
<p> <i>ActiveSession</i> encodes the currently active session if there is one. It is a structure consisting of the session id and the object path. </p>
<p> <i>CanTTY</i> encodes whether the session is suitable for text logins, and <i>CanGraphical</i> whether it is suitable for graphical sessions. </p>
<p> The <i>Sessions</i> property is an array of all current sessions of this seat, each encoded in a structure consisting of the ID and the object path. </p>
<p> The <i>IdleHint</i>, <i>IdleSinceHint</i>, and <i>IdleSinceHintMonotonic</i> properties encode the idle state, similar to the ones exposed on the Manager object, but specific for this seat.</p>
<h2>User Objects</h2>
<dl>
<dd>
<pre>node /org/freedesktop/login1/user/_1000 {
 interface org.freedesktop.login1.User {
 methods:
 Terminate();
 Kill(in i signal_number);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u UID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u GID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Name = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t Timestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RuntimePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Service = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Slice = '...';
 readonly (so) Display = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s State = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(so) Sessions = [...];
 readonly b IdleHint = ...;
 readonly t IdleSinceHint = ...;
 readonly t IdleSinceHintMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b Linger = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>Terminate()</code> and <code>Kill()</code> work similar to the <code>TerminateUser()</code> and <code>KillUser()</code> methods on the manager object.</p>
<h3>Signals</h3>
<p>Whenever <i>Sessions</i> or the idle state changes, <code>PropertyChanged</code> signals are sent out to which clients can subscribe.</p>
<h3>Properties</h3>
<p>The <i>UID</i> and <i>GID</i> properties encode the Unix UID and primary GID of the user. </p>
<p> The <i>Name</i> property encodes the user name. </p>
<p> <i>Timestamp</i> and <i>TimestampMonotonic</i> encode the login time of the user in microseconds since the epoch, in the <code>CLOCK_REALTIME</code> and <code>CLOCK_MONOTONIC</code> clocks, respectively. </p>
<p> <i>RuntimePath</i> encodes the runtime path of the user, i.e. <i>$XDG_RUNTIME_DIR</i>. For details see the m[blue]<code>XDG Basedir Specification</code>m[]<font SIZE="-2">[3]</font>. </p>
<p> <i>Service</i> contains the unit name of the user systemd service of this user. Each logged in user is assigned a user service that runs a user systemd instance. This is usually an instance of user [at] .service. </p>
<p> <i>Slice</i> contains the unit name of the user systemd slice of this user. Each logged in user gets a private slice. </p>
<p> <i>Display</i> encodes which graphical session should be used as the primary UI display for the user. It is a structure encoding the session ID and the object path of the session to use. </p>
<p> <i>State</i> encodes the user state and is one of &quot;offline&quot;, &quot;lingering&quot;, &quot;online&quot;, &quot;active&quot;, or &quot;closing&quot;. See <code><a href="/docs/linux/man/3-sd_uid_get_state/">sd_uid_get_state</a></code>(3) for more information about the states. </p>
<p> <i>Sessions</i> is an array of structures encoding all current sessions of the user. Each structure consists of the ID and object path. </p>
<p> The <i>IdleHint</i>, <i>IdleSinceHint</i>, and <i>IdleSinceHintMonotonic</i> properties encode the idle hint state of the user, similar to the Manager&#8217;s properties, but specific for this user. </p>
<p> The <i>Linger</i> property shows whether lingering is enabled for this user.</p>
<h2>Session Objects</h2>
<dl>
<dd>
<pre>node /org/freedesktop/login1/session/1 {
 interface org.freedesktop.login1.Session {
 methods:
 Terminate();
 Activate();
 Lock();
 Unlock();
 SetIdleHint(in b idle);
 SetLockedHint(in b locked);
 Kill(in s who,
 in i signal_number);
 TakeControl(in b force);
 ReleaseControl();
 SetType(in s type);
 TakeDevice(in u major,
 in u minor,
 out h fd,
 out b inactive);
 ReleaseDevice(in u major,
 in u minor);
 PauseDeviceComplete(in u major,
 in u minor);
 SetBrightness(in s subsystem,
 in s name,
 in u brightness);
 signals:
 PauseDevice(u major,
 u minor,
 s type);
 ResumeDevice(u major,
 u minor,
 h fd);
 Lock();
 Unlock();
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Id = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (uo) User = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Name = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t Timestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u VTNr = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (so) Seat = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s TTY = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Display = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b Remote = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RemoteHost = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RemoteUser = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Service = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Desktop = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Scope = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u Leader = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u Audit = ...;
 readonly s Type = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Class = '...';
 readonly b Active = ...;
 readonly s State = '...';
 readonly b IdleHint = ...;
 readonly t IdleSinceHint = ...;
 readonly t IdleSinceHintMonotonic = ...;
 readonly b LockedHint = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>Terminate()</code>, <code>Activate()</code>, <code>Lock()</code>, <code>Unlock()</code>, and <code>Kill()</code> work similarly to the respective calls on the Manager object. </p>
<p> <code>SetIdleHint()</code> is called by the session object to update the idle state of the session whenever it changes. </p>
<p> <code>TakeControl()</code> allows a process to take exclusive managed device access-control for that session. Only one D-Bus connection can be a controller for a given session at any time. If the <i>force</i> argument is set (root only), an existing controller is kicked out and replaced. Otherwise, this method fails if there is already a controller. Note that this method is limited to D-Bus users with the effective UID set to the user of the session or root. </p>
<p> <code>ReleaseControl()</code> drops control of a given session. Closing the D-Bus connection implicitly releases control as well. See <code>TakeControl()</code> for more information. This method also releases all devices for which the controller requested ownership via <code>TakeDevice()</code>. </p>
<p> <code>SetType()</code> allows the type of the session to be changed dynamically. It can only be called by session&#8217;s current controller. If <code>TakeControl()</code> has not been called, this method will fail. In addition, the session type will be reset to its original value once control is released, either by calling <code>ReleaseControl()</code> or closing the D-Bus connection. This should help prevent a session from entering an inconsistent state, for example if the controller crashes. The only argument <i>type</i> is the new session type. </p>
<p> <code>TakeDevice()</code> allows a session controller to get a file descriptor for a specific device. Pass in the major and minor numbers of the character device and systemd-logind will return a file descriptor for the device. Only a limited set of device-types is currently supported (but may be extended). systemd-logind automatically mutes the file descriptor if the session is inactive and resumes it once the session is activated again. This guarantees that a session can only access session devices if the session is active. Note that this revoke/resume mechanism is asynchronous and may happen at any given time. This only works on devices that are attached to the seat of the given session. A process is not required to have direct access to the device node. systemd-logind only requires you to be the active session controller (see <code>TakeControl()</code>). Also note that any device can only be requested once. As long as you don&#8217;t release it, further <code>TakeDevice()</code> calls will fail. </p>
<p> <code>ReleaseDevice()</code> releases a device again (see <code>TakeDevice()</code>). This is also implicitly done by <code>ReleaseControl()</code> or when closing the D-Bus connection. </p>
<p> <code>PauseDeviceComplete()</code> allows a session controller to synchronously pause a device after receiving a <code>PauseDevice(</code><code>&quot;pause&quot;</code><code>)</code> signal. Forced signals (or after an internal timeout) are automatically completed by systemd-logind asynchronously. </p>
<p> <code>SetLockedHint()</code> may be used to set the &quot;locked hint&quot; to <i>locked</i>, i.e. information whether the session is locked. This is intended to be used by the desktop environment to tell <code>systemd-logind</code> when the session is locked and unlocked. </p>
<p> <code>SetBrightness()</code> may be used to set the display brightness. This is intended to be used by the desktop environment and allows unprivileged programs to access hardware settings in a controlled way. The <i>subsystem</i> parameter specifies a kernel subsystem, either &quot;backlight&quot; or &quot;leds&quot;. The <i>name</i> parameter specifies a device name under the specified subsystem. The <i>brightness</i> parameter specifies the brightness. The range is defined by individual drivers, see /sys/class/<i>subsystem</i>/<i>name</i>/max_brightness.</p>
<h3>Signals</h3>
<p>The active session controller exclusively gets <code>PauseDevice</code> and <code>ResumeDevice</code> events for any device it requested via <code>TakeDevice()</code>. They notify the controller whenever a device is paused or resumed. A device is never resumed if its session is inactive. Also note that <code>PauseDevice</code> signals are sent before the <code>PropertyChanged</code> signal for the <code>Active</code> state. The inverse is true for <code>ResumeDevice</code>. A device may remain paused for unknown reasons even though the Session is active. </p>
<p> A <code>PauseDevice</code> signal carries the major and minor numbers and a string describing the type as arguments. <code>force</code> means the device was already paused by systemd-logind and the signal is only an asynchronous notification. <code>pause</code> means systemd-logind grants you a limited amount of time to pause the device. You must respond to this via <code>PauseDeviceComplete()</code>. This synchronous pausing mechanism is used for backwards-compatibility to VTs and systemd-logind is free to not make use of it. It is also free to send a forced <code>PauseDevice</code> if you don&#8217;t respond in a timely manner (or for any other reason). <code>gone</code> means the device was unplugged from the system and you will no longer get any notifications about it. There is no need to call <code>ReleaseDevice()</code>. You may call <code>TakeDevice()</code> again if a new device is assigned the major+minor combination. </p>
<p> <code>ResumeDevice</code> is sent whenever a session is active and a device is resumed. It carries the major/minor numbers as arguments and provides a new open file descriptor. You should switch to the new descriptor and close the old one. They are not guaranteed to have the same underlying open file descriptor in the kernel (except for a limited set of device types). </p>
<p> Whenever <code>Active</code> or the idle state changes, <code>PropertyChanged</code> signals are sent out to which clients can subscribe. </p>
<p> <code>Lock</code>/<code>Unlock</code> is sent when the session is asked to be screen-locked/unlocked. A session manager of the session should listen to this signal and act accordingly. This signal is sent out as a result of the <code>Lock()</code> and <code>Unlock()</code> methods, respectively.</p>
<h3>Properties</h3>
<p><i>Id</i> encodes the session ID. </p>
<p> <i>User</i> encodes the user ID of the user this session belongs to. This is a structure consisting of the Unix UID and the object path. </p>
<p> <i>Name</i> encodes the user name. </p>
<p> <i>Timestamp</i> and <i>TimestampMonotonic</i> encode the microseconds since the epoch when the session was created, in <code>CLOCK_REALTIME</code> or <code>CLOCK_MONOTONIC</code>, respectively. </p>
<p> <i>VTNr</i> encodes the virtual terminal number of the session if there is any, 0 otherwise. </p>
<p> <i>Seat</i> encodes the seat this session belongs to if there is any. This is a structure consisting of the ID and the seat object path. </p>
<p> <i>TTY</i> encodes the kernel TTY path of the session if this is a text login. If not this is an empty string. </p>
<p> <i>Display</i> encodes the X11 display name if this is a graphical login. If not, this is an empty string. </p>
<p> <i>Remote</i> encodes whether the session is local or remote. </p>
<p> <i>RemoteHost</i> and <i>RemoteUser</i> encode the remote host and user if this is a remote session, or an empty string otherwise. </p>
<p> <i>Service</i> encodes the PAM service name that registered the session. </p>
<p> <i>Desktop</i> describes the desktop environment running in the session (if known). </p>
<p> <i>Scope</i> contains the systemd scope unit name of this session. </p>
<p> <i>Leader</i> encodes the PID of the process that registered the session. </p>
<p> <i>Audit</i> encodes the Kernel Audit session ID of the session if auditing is available. </p>
<p> <i>Type</i> encodes the session type. It&#8217;s one of &quot;unspecified&quot; (for cron PAM sessions and suchlike), &quot;tty&quot; (for text logins) or &quot;x11&quot;/&quot;mir&quot;/&quot;wayland&quot; (for graphical logins). </p>
<p> <i>Class</i> encodes the session class. It&#8217;s one of &quot;user&quot; (for normal user sessions), &quot;greeter&quot; (for display manager pseudo-sessions), or &quot;lock-screen&quot; (for display lock screens). </p>
<p> <i>Active</i> is a boolean that is true if the session is active, i.e. currently in the foreground. This field is semi-redundant due to <i>State</i>. </p>
<p> <i>State</i> encodes the session state and one of &quot;online&quot;, &quot;active&quot;, or &quot;closing&quot;. See <code><a href="/docs/linux/man/3-sd_session_get_state/">sd_session_get_state</a></code>(3) for more information about the states. </p>
<p> <i>IdleHint</i>, <i>IdleSinceHint</i>, and <i>IdleSinceHintMonotonic</i> encapsulate the idle hint state of this session, similarly to how the respective properties on the manager object do it for the whole system. </p>
<p> <i>LockedHint</i> shows the locked hint state of this session, as set by the <code>SetLockedHint()</code> method described above.</p>
<h2>Examples</h2>
<p><code>Example 1. Introspect org.freedesktop.login1.Manager on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system --dest org.freedesktop.login1 \
 --object-path /org/freedesktop/login1</pre>
</dl>
<p> <code>Example 2. Introspect org.freedesktop.login1.Seat on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system --dest org.freedesktop.login1 \
 --object-path /org/freedesktop/login1/seat/seat0</pre>
</dl>
<p> <code>Example 3. Introspect org.freedesktop.login1.User on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system --dest org.freedesktop.login1 \
 --object-path /org/freedesktop/login1/user/_1000</pre>
</dl>
<p> <code>Example 4. Introspect org.freedesktop.login1.Session on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system --dest org.freedesktop.login1 \
 --object-path /org/freedesktop/login1/session/45</pre>
</dl>
<h2>Versioning</h2>
<p>These D-Bus interfaces follow m[blue]<code>the usual interface versioning guidelines</code>m[]<font SIZE="-2">[4]</font>.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>polkit</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/software/polkit/docs/latest/">https://www.freedesktop.org/software/polkit/docs/latest/</a></dl>
<dt> 2.</p>
<dd>Inhibitor Locks</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/inhibit">https://www.freedesktop.org/wiki/Software/systemd/inhibit</a></dl>
<dt> 3.</p>
<dd>XDG Basedir Specification</p>
<dl>
<dd><a rel="nofollow" href="https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html">https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html</a></dl>
<dt> 4.</p>
<dd>the usual interface versioning guidelines</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/versioning-dbus.html">http://0pointer.de/blog/projects/versioning-dbus.html</a></dl>
