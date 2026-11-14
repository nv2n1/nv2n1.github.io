---
title: "org-freedesktop-systemd1(5)"
name: "org-freedesktop-systemd1"
section: "5"
letter: "o"
url: "/docs/linux/man/5-org-freedesktop-systemd1/"
description: "org.freedesktop.systemd1 – The D-Bus interface of systemd"
---

<p>org.freedesktop.systemd1 &#8211; The D-Bus interface of systemd</p>
<h2>Introduction</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) and its auxiliary daemons expose a number of APIs over D-Bus. This page only describes the various APIs exposed by the system and service manager itself. It does not cover the auxiliary daemons. </p>
<p> The service manager exposes a number of objects on the bus: one Manager object as a central entry point for clients along with individual objects for each unit and for each queued job. The unit objects implement a generic Unit interface as well as a type-specific interface. For example, service units implement both org.freedesktop.systemd1.Unit and org.freedesktop.system1.Service. The manager object can list unit and job objects or directly convert a unit name or job identifier to a bus path of the corresponding D-Bus object. </p>
<p> Properties exposing time values are usually encoded in microseconds (&micro;s) on the bus, even if their corresponding settings in the unit files are in seconds. </p>
<p> PID 1 uses m[blue]<code>polkit</code>m[]<font SIZE="-2">[1]</font> to allow access to privileged operations for unprivileged processes. Some operations (such as shutdown/reboot/suspend) are also available through the D-Bus API of logind, see <code><a href="/docs/linux/man/5-org-freedesktop-login1/">org.freedesktop.login1</a></code>(5).</p>
<h2>The Manager Object</h2>
<p>The main entry point object is available on the fixed <code>/org/freedesktop/systemd1</code> object path: </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1 {
 interface org.freedesktop.systemd1.Manager {
 methods:
 GetUnit(in s name,
 out o unit);
 GetUnitByPID(in u pid,
 out o unit);
 GetUnitByInvocationID(in ay invocation_id,
 out o unit);
 GetUnitByControlGroup(in s cgroup,
 out o unit);
 LoadUnit(in s name,
 out o unit);
 StartUnit(in s name,
 in s mode,
 out o job);
 StartUnitReplace(in s old_unit,
 in s new_unit,
 in s mode,
 out o job);
 StopUnit(in s name,
 in s mode,
 out o job);
 ReloadUnit(in s name,
 in s mode,
 out o job);
 RestartUnit(in s name,
 in s mode,
 out o job);
 TryRestartUnit(in s name,
 in s mode,
 out o job);
 ReloadOrRestartUnit(in s name,
 in s mode,
 out o job);
 ReloadOrTryRestartUnit(in s name,
 in s mode,
 out o job);
 EnqueueUnitJob(in s name,
 in s job_type,
 in s job_mode,
 out u job_id,
 out o job_path,
 out s unit_id,
 out o unit_path,
 out s job_type,
 out a(uosos) affected_jobs);
 KillUnit(in s name,
 in s whom,
 in i signal);
 CleanUnit(in s name,
 in as mask);
 FreezeUnit(in s name);
 ThawUnit(in s name);
 ResetFailedUnit(in s name);
 SetUnitProperties(in s name,
 in b runtime,
 in a(sv) properties);
 BindMountUnit(in s name,
 in s source,
 in s destination,
 in b read_only,
 in b mkdir);
 MountImageUnit(in s name,
 in s source,
 in s destination,
 in b read_only,
 in b mkdir,
 in a(ss) options);
 RefUnit(in s name);
 UnrefUnit(in s name);
 StartTransientUnit(in s name,
 in s mode,
 in a(sv) properties,
 in a(sa(sv)) aux,
 out o job);
 GetUnitProcesses(in s name,
 out a(sus) processes);
 AttachProcessesToUnit(in s unit_name,
 in s subcgroup,
 in au pids);
 AbandonScope(in s name);
 GetJob(in u id,
 out o job);
 GetJobAfter(in u id,
 out a(usssoo) jobs);
 GetJobBefore(in u id,
 out a(usssoo) jobs);
 CancelJob(in u id);
 ClearJobs();
 ResetFailed();
 SetShowStatus(in s mode);
 ListUnits(out a(ssssssouso) units);
 ListUnitsFiltered(in as states,
 out a(ssssssouso) units);
 ListUnitsByPatterns(in as states,
 in as patterns,
 out a(ssssssouso) units);
 ListUnitsByNames(in as names,
 out a(ssssssouso) units);
 ListJobs(out a(usssoo) jobs);
 Subscribe();
 Unsubscribe();
 Dump(out s output);
 DumpByFileDescriptor(out h fd);
 Reload();
 Reexecute();
 Exit();
 Reboot();
 PowerOff();
 Halt();
 KExec();
 SwitchRoot(in s new_root,
 in s init);
 SetEnvironment(in as assignments);
 UnsetEnvironment(in as names);
 UnsetAndSetEnvironment(in as names,
 in as assignments);
 EnqueueMarkedJobs(out ao jobs);
 ListUnitFiles(out a(ss) unit_files);
 ListUnitFilesByPatterns(in as states,
 in as patterns,
 out a(ss) unit_files);
 GetUnitFileState(in s file,
 out s state);
 EnableUnitFiles(in as files,
 in b runtime,
 in b force,
 out b carries_install_info,
 out a(sss) changes);
 DisableUnitFiles(in as files,
 in b runtime,
 out a(sss) changes);
 EnableUnitFilesWithFlags(in as files,
 in t flags,
 out b carries_install_info,
 out a(sss) changes);
 DisableUnitFilesWithFlags(in as files,
 in t flags,
 out a(sss) changes);
 ReenableUnitFiles(in as files,
 in b runtime,
 in b force,
 out b carries_install_info,
 out a(sss) changes);
 LinkUnitFiles(in as files,
 in b runtime,
 in b force,
 out a(sss) changes);
 PresetUnitFiles(in as files,
 in b runtime,
 in b force,
 out b carries_install_info,
 out a(sss) changes);
 PresetUnitFilesWithMode(in as files,
 in s mode,
 in b runtime,
 in b force,
 out b carries_install_info,
 out a(sss) changes);
 MaskUnitFiles(in as files,
 in b runtime,
 in b force,
 out a(sss) changes);
 UnmaskUnitFiles(in as files,
 in b runtime,
 out a(sss) changes);
 RevertUnitFiles(in as files,
 out a(sss) changes);
 SetDefaultTarget(in s name,
 in b force,
 out a(sss) changes);
 GetDefaultTarget(out s name);
 PresetAllUnitFiles(in s mode,
 in b runtime,
 in b force,
 out a(sss) changes);
 AddDependencyUnitFiles(in as files,
 in s target,
 in s type,
 in b runtime,
 in b force,
 out a(sss) changes);
 GetUnitFileLinks(in s name,
 in b runtime,
 out as links);
 SetExitCode(in y number);
 LookupDynamicUserByName(in s name,
 out u uid);
 LookupDynamicUserByUID(in u uid,
 out s name);
 GetDynamicUsers(out a(us) users);
 signals:
 UnitNew(s id,
 o unit);
 UnitRemoved(s id,
 o unit);
 JobNew(u id,
 o job,
 s unit);
 JobRemoved(u id,
 o job,
 s unit,
 s result);
 StartupFinished(t firmware,
 t loader,
 t kernel,
 t initrd,
 t userspace,
 t total);
 UnitFilesChanged();
 Reloading(b active);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Version = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Features = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Virtualization = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Architecture = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Tainted = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t FirmwareTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t FirmwareTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LoaderTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LoaderTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t KernelTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t KernelTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t UserspaceTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t UserspaceTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t FinishTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t FinishTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t SecurityStartTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t SecurityStartTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t SecurityFinishTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t SecurityFinishTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t GeneratorsStartTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t GeneratorsStartTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t GeneratorsFinishTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t GeneratorsFinishTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t UnitsLoadStartTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t UnitsLoadStartTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t UnitsLoadFinishTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t UnitsLoadFinishTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDSecurityStartTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDSecurityStartTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDSecurityFinishTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDSecurityFinishTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDGeneratorsStartTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDGeneratorsStartTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDGeneratorsFinishTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDGeneratorsFinishTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDUnitsLoadStartTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDUnitsLoadStartTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDUnitsLoadFinishTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t InitRDUnitsLoadFinishTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
 readwrite s LogLevel = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
 readwrite s LogTarget = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u NNames = ...;
 readonly u NFailedUnits = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u NJobs = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u NInstalledJobs = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u NFailedJobs = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly d Progress = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as Environment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ConfirmSpawn = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b ShowStatus = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as UnitPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s DefaultStandardOutput = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s DefaultStandardError = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
 readwrite t RuntimeWatchdogUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
 readwrite t RebootWatchdogUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
 readwrite t KExecWatchdogUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
 readwrite b ServiceWatchdogs = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ControlGroup = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s SystemState = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly y ExitCode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultTimerAccuracyUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultTimeoutStartUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultTimeoutStopUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultTimeoutAbortUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultRestartUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultStartLimitIntervalUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u DefaultStartLimitBurst = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b DefaultCPUAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b DefaultBlockIOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b DefaultMemoryAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b DefaultTasksAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitCPU = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitCPUSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitFSIZE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitFSIZESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitDATA = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitDATASoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitSTACK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitSTACKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitCORE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitCORESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitRSS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitRSSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitNOFILE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitNOFILESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitAS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitASSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitNPROC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitNPROCSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitMEMLOCK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitMEMLOCKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitLOCKS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitLOCKSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitSIGPENDING = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitSIGPENDINGSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitMSGQUEUE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitMSGQUEUESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitNICE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitNICESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitRTPRIO = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitRTPRIOSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitRTTIME = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DefaultLimitRTTIMESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultTasksMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimerSlackNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s DefaultOOMPolicy = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s CtrlAltDelBurstAction = '...';
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p>Note that many of the methods exist twice: once on the Manager object and once on the respective unit objects. This is to optimize access times so that methods that belong to unit objects do not have to be called with a resolved unit path, but can be called with only the unit id, too. </p>
<p> <code>GetUnit()</code> may be used to get the unit object path for a unit name. It takes the unit name and returns the object path. If a unit has not been loaded yet by this name this method will fail. </p>
<p> <code>GetUnitByPID()</code> may be used to get the unit object path of the unit a process ID belongs to. It takes a UNIX PID and returns the object path. The PID must refer to an existing system process. </p>
<p> <code>LoadUnit()</code> is similar to <code>GetUnit()</code> but will load the unit from disk if possible. </p>
<p> <code>StartUnit()</code> enqueues a start job and possibly depending jobs. It takes the unit to activate and a mode string as arguments. The mode needs to be one of &quot;replace&quot;, &quot;fail&quot;, &quot;isolate&quot;, &quot;ignore-dependencies&quot;, or &quot;ignore-requirements&quot;. If &quot;replace&quot;, the method will start the unit and its dependencies, possibly replacing already queued jobs that conflict with it. If &quot;fail&quot;, the method will start the unit and its dependencies, but will fail if this would change an already queued job. If &quot;isolate&quot;, the method will start the unit in question and terminate all units that aren&#8217;t dependencies of it. If &quot;ignore-dependencies&quot;, it will start a unit but ignore all its dependencies. If &quot;ignore-requirements&quot;, it will start a unit but only ignore the requirement dependencies. It is not recommended to make use of the latter two options. On completion, this method returns the newly created job object. </p>
<p> <code>StartUnitReplace()</code> is similar to <code>StartUnit()</code> but replaces a job that is queued for one unit by a job for another unit. </p>
<p> <code>StopUnit()</code> is similar to <code>StartUnit()</code> but stops the specified unit rather than starting it. Note that the &quot;isolate&quot; mode is invalid for this method. </p>
<p> <code>ReloadUnit()</code>, <code>RestartUnit()</code>, <code>TryRestartUnit()</code>, <code>ReloadOrRestartUnit()</code>, or <code>ReloadOrTryRestartUnit()</code> may be used to restart and/or reload a unit. These methods take similar arguments as <code>StartUnit()</code>. Reloading is done only if the unit is already running and fails otherwise. If a service is restarted that isn&#8217;t running, it will be started unless the &quot;Try&quot; flavor is used in which case a service that isn&#8217;t running is not affected by the restart. The &quot;ReloadOrRestart&quot; flavors attempt a reload if the unit supports it and use a restart otherwise. </p>
<p> <code>EnqueueMarkedJobs()</code> creates reload/restart jobs for units which have been appropriately marked, see <i>Marks</i> property above. This is equivalent to calling <code>TryRestartUnit()</code> or <code>ReloadOrTryRestartUnit()</code> for the marked units. </p>
<p> <code>BindMountUnit()</code> can be used to bind mount new files or directories into a running service mount namespace. </p>
<p> <code>MountImageUnit()</code> can be used to mount new images into a running service mount namespace. </p>
<p> <code>KillUnit()</code> may be used to kill (i.e. send a signal to) all processes of a unit. It takes the unit <i>name</i>, an enum <i>who</i> and a UNIX <i>signal</i> number to send. The <i>who</i> enum is one of &quot;main&quot;, &quot;control&quot; or &quot;all&quot;. If &quot;main&quot;, only the main process of the unit is killed. If &quot;control&quot;, only the control process of the unit is killed. If &quot;all&quot;, all processes are killed. A &quot;control&quot; process is for example a process that is configured via <i>ExecStop=</i> and is spawned in parallel to the main daemon process in order to shut it down. </p>
<p> <code>GetJob()</code> returns the job object path for a specific job, identified by its id. </p>
<p> <code>CancelJob()</code> cancels a specific job identified by its numeric ID. This operation is also available in the <code>Cancel()</code> method of Job objects (see below) and exists primarily to reduce the necessary round trips to execute this operation. Note that this will not have any effect on jobs whose execution has already begun. </p>
<p> <code>ClearJobs()</code> flushes the job queue, removing all jobs that are still queued. Note that this does not have any effect on jobs whose execution has already begun. It only flushes jobs that are queued and have not yet begun execution. </p>
<p> <code>ResetFailedUnit()</code> resets the &quot;failed&quot; state of a specific unit. </p>
<p> <code>ResetFailed()</code> resets the &quot;failed&quot; state of all units. </p>
<p> <code>ListUnits()</code> returns an array of all currently loaded units. Note that units may be known by multiple names at the same name, and hence there might be more unit names loaded than actual units behind them. The array consists of structures with the following elements: </p>
<dl>
<dd>&bull; The primary unit name as string</dl>
<dl>
<dd>&bull; The human readable description string</dl>
<dl>
<dd>&bull; The load state (i.e. whether the unit file has been loaded successfully)</dl>
<dl>
<dd>&bull; The active state (i.e. whether the unit is currently started or not)</dl>
<dl>
<dd>&bull; The sub state (a more fine-grained version of the active state that is specific to the unit type, which the active state is not)</dl>
<dl>
<dd>&bull; A unit that is being followed in its state by this unit, if there is any, otherwise the empty string.</dl>
<dl>
<dd>&bull; The unit object path</dl>
<dl>
<dd>&bull; If there is a job queued for the job unit, the numeric job id, 0 otherwise</dl>
<dl>
<dd>&bull; The job type as string</dl>
<dl>
<dd>&bull; The job object path</dl>
<p> <code>ListJobs()</code> returns an array with all currently queued jobs. Returns an array consisting of structures with the following elements: </p>
<dl>
<dd>&bull; The numeric job id</dl>
<dl>
<dd>&bull; The primary unit name for this job</dl>
<dl>
<dd>&bull; The job type as string</dl>
<dl>
<dd>&bull; The job state as string</dl>
<dl>
<dd>&bull; The job object path</dl>
<dl>
<dd>&bull; The unit object path</dl>
<p> <code>Subscribe()</code> enables most bus signals to be sent out. Clients which are interested in signals need to call this method. Signals are only sent out if at least one client invoked this method. <code>Unsubscribe()</code> reverts the signal subscription that <code>Subscribe()</code> implements. It is not necessary to invoke <code>Unsubscribe()</code> as clients are tracked. Signals are no longer sent out as soon as all clients which previously asked for <code>Subscribe()</code> either closed their connection to the bus or invoked <code>Unsubscribe()</code>. </p>
<p> <code>Reload()</code> may be invoked to reload all unit files. </p>
<p> <code>Reexecute()</code> may be invoked to reexecute the main manager process. It will serialize its state, reexecute, and deserizalize the state again. This is useful for upgrades and is a more comprehensive version of <code>Reload()</code>. </p>
<p> <code>Exit()</code> may be invoked to ask the manager to exit. This is not available for the system manager and is useful only for user session managers. </p>
<p> <code>Reboot()</code>, <code>PowerOff()</code>, <code>Halt()</code>, or <code>KExec()</code> may be used to ask for immediate reboot, powering down, halt or kexec based reboot of the system. Note that this does not shut down any services and immediately transitions into the reboot process. These functions are normally only called as the last step of shutdown and should not be called directly. To shut down the machine, it is generally a better idea to invoke <code>Reboot()</code> or <code>PowerOff()</code> on the systemd-logind manager object; see <code><a href="/docs/linux/man/5-org-freedesktop-login1/">org.freedesktop.login1</a></code>(5) for more information. </p>
<p> <code>SwitchRoot()</code> may be used to transition to a new root directory. This is intended to be used by initial RAM disks. The method takes two arguments: the new root directory (which needs to be specified) and an init binary path (which may be left empty, in which case it is automatically searched for). The state of the system manager will be serialized before the transition. After the transition, the manager binary on the main system is invoked and replaces the old PID 1. All state will then be deserialized. </p>
<p> <code>SetEnvironment()</code> may be used to alter the environment block that is passed to all spawned processes. It takes a string array of environment variable assignments. Any previously set environment variables will be overridden. </p>
<p> <code>UnsetEnvironment()</code> may be used to unset environment variables. It takes a string array of environment variable names. All variables specified will be unset (if they have been set previously) and no longer be passed to all spawned processes. This method has no effect for variables that were previously not set, but will not fail in that case. </p>
<p> <code>UnsetAndSetEnvironment()</code> is a combination of <code>UnsetEnvironment()</code> and <code>SetEnvironment()</code>. It takes two lists. The first list contains variables to unset, the second one contains assignments to set. If a variable is listed in both, the variable is set after this method returns, i.e. the set list overrides the unset list. </p>
<p> <code>ListUnitFiles()</code> returns an array of unit names and their enablement status. Note that <code>ListUnit()</code> returns a list of units currently loaded into memory, while <code>ListUnitFiles()</code> returns a list of unit <i>files</i> that were found on disk. Note that while most units are read directly from a unit file with the same name, some units are not backed by files and some files (templates) cannot directly be loaded as units but need to be instantiated instead. </p>
<p> <code>GetUnitFileState()</code> returns the current enablement status of a specific unit file. </p>
<p> <code>EnableUnitFiles()</code> may be used to enable one or more units in the system (by creating symlinks to them in /etc/ or /run/). It takes a list of unit files to enable (either just file names or full absolute paths if the unit files are residing outside the usual unit search paths) and two booleans: the first controls whether the unit shall be enabled for runtime only (true, /run/), or persistently (false, /etc/). The second one controls whether symlinks pointing to other units shall be replaced if necessary. This method returns one boolean and an array of the changes made. The boolean signals whether the unit files contained any enablement information (i.e. an [Install]) section. The changes array consists of structures with three strings: the type of the change (one of &quot;symlink&quot; or &quot;unlink&quot;), the file name of the symlink and the destination of the symlink. Note that most of the following calls return a changes list in the same format. </p>
<p> Similarly, <code>DisableUnitFiles()</code> disables one or more units in the system, i.e. removes all symlinks to them in /etc/ and /run/. </p>
<p> The <code>EnableUnitFilesWithFlags()</code> and <code>DisableUnitFilesWithFlags()</code> take in options as flags instead of booleans to allow for extendability, defined as follows: </p>
<dl>
<dd>
<pre>#define SD_SYSTEMD_UNIT_RUNTIME (<a href="//www.systutorials.com/docs/linux/man/1-UINT64_C/">UINT64_C</a>(1) &lt;&lt; 0)
#define SD_SYSTEMD_UNIT_FORCE (<a href="//www.systutorials.com/docs/linux/man/1-UINT64_C/">UINT64_C</a>(1) &lt;&lt; 1)
#define SD_SYSTEMD_UNIT_PORTABLE (<a href="//www.systutorials.com/docs/linux/man/1-UINT64_C/">UINT64_C</a>(1) &lt;&lt; 2)</pre>
</dl>
<p> <i>SD_SYSTEMD_UNIT_RUNTIME</i> will enable or disable the unit for runtime only, <i>SD_SYSTEMD_UNIT_FORCE</i> controls whether symlinks pointing to other units shall be replaced if necessary. <i>SD_SYSTEMD_UNIT_PORTABLE</i> will add or remove the symlinks in /etc/systemd/system.attached and /run/systemd/system.attached. </p>
<p> Similarly, <code>ReenableUnitFiles()</code> applies the changes to one or more units that would result from disabling and enabling the unit quickly one after the other in an atomic fashion. This is useful to apply updated [Install] information contained in unit files. </p>
<p> Similarly, <code>LinkUnitFiles()</code> links unit files (that are located outside of the usual unit search paths) into the unit search path. </p>
<p> Similarly, <code>PresetUnitFiles()</code> enables/disables one or more unit files according to the preset policy. See <code><a href="/docs/linux/man/7-systemd-preset/">systemd.preset</a></code>(7) for more information. </p>
<p> Similarly, <code>MaskUnitFiles()</code> masks unit files and <code>UnmaskUnitFiles()</code> unmasks them again. </p>
<p> <code>SetDefaultTarget()</code> changes the default.target link. See <code><a href="/docs/linux/man/7-bootup/">bootup</a></code>(7) for more information. </p>
<p> <code>GetDefaultTarget()</code> retrieves the name of the unit to which default.target is aliased. </p>
<p> <code>SetUnitProperties()</code> may be used to modify certain unit properties at runtime. Not all properties may be changed at runtime, but many resource management settings (primarily those listed in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5)) may. The changes are applied instantly and stored on disk for future boots, unless <i>runtime</i> is true, in which case the settings only apply until the next reboot. <i>name</i> is the name of the unit to modify. <i>properties</i> are the settings to set, encoded as an array of property name and value pairs. Note that this is not a dictionary! Also note that when setting array properties with this method usually results in appending to the pre-configured array. To reset the configured arrays, set the property to an empty array first and then append to it. </p>
<p> <code>StartTransientUnit()</code> may be used to create and start a transient unit which will be released as soon as it is not running or referenced anymore or the system is rebooted. <i>name</i> is the unit name including its suffix and must be unique. <i>mode</i> is the same as in <code>StartUnit()</code>, <i>properties</i> contains properties of the unit, specified like in <code>SetUnitProperties()</code>. <i>aux</i> is currently unused and should be passed as an empty array. See the m[blue]<code>New Control Group Interface</code>m[]<font SIZE="-2">[2]</font> for more information how to make use of this functionality for resource control purposes.</p>
<h3>Signals</h3>
<p>Note that most signals are sent out only after <code>Subscribe()</code> has been invoked by at least one client. Make sure to invoke this method when subscribing to these signals! </p>
<p> <code>UnitNew()</code> and <code>UnitRemoved()</code> are sent out each time a new unit is loaded or unloaded. Note that this has little to do with whether a unit is available on disk or not, and simply reflects the units that are currently loaded into memory. The signals take two parameters: the primary unit name and the object path. </p>
<p> <code>JobNew()</code> and <code>JobRemoved()</code> are sent out each time a new job is queued or dequeued. Both signals take the numeric job ID, the bus path and the primary unit name for this job as arguments. <code>JobRemoved()</code> also includes a result string which is one of &quot;done&quot;, &quot;canceled&quot;, &quot;timeout&quot;, &quot;failed&quot;, &quot;dependency&quot;, or &quot;skipped&quot;. &quot;done&quot; indicates successful execution of a job. &quot;canceled&quot; indicates that a job has been canceled (via <code>CancelJob()</code> above) before it finished execution (this doesn&#8217;t necessarily mean though that the job operation is actually cancelled too, see above). &quot;timeout&quot; indicates that the job timeout was reached. &quot;failed&quot; indicates that the job failed. &quot;dependency&quot; indicates that a job this job depended on failed and the job hence was removed as well. &quot;skipped&quot; indicates that a job was skipped because it didn&#8217;t apply to the unit&#8217;s current state. </p>
<p> <code>StartupFinished()</code> is sent out when startup finishes. It carries six microsecond timespan values, each indicating how much boot time has been spent in the firmware (if known), in the boot loader (if known), in the kernel initialization phase, in the initrd (if known), in userspace and in total. These values may also be calculated from the <i>FirmwareTimestampMonotonic</i>, <i>LoaderTimestampMonotonic</i>, <i>InitRDTimestampMonotonic</i>, <i>UserspaceTimestampMonotonic</i>, and <i>FinishTimestampMonotonic</i> properties (see below). </p>
<p> <code>UnitFilesChanged()</code> is sent out each time the list of enabled or masked unit files on disk have changed. </p>
<p> <code>Reloading()</code> is sent out immediately before a daemon reload is done (with the boolean parameter set to True) and after a daemon reload is completed (with the boolean parameter set to False). This may be used by UIs to optimize UI updates.</p>
<h3>Properties</h3>
<p>Most properties simply reflect the respective options in /etc/systemd/system.conf and the kernel command line. </p>
<p> The others: </p>
<p> <i>Version</i> encodes the version string of the running systemd instance. Note that the version string is purely informational. It should not be parsed and one may not assume the version to be formatted in any particular way. We take the liberty to change the versioning scheme at any time and it is not part of the public API. </p>
<p> <i>Features</i> encodes the features that have been enabled and disabled for this build. Enabled options are prefixed with +, disabled options with -. </p>
<p> <i>Tainted</i> encodes a couple of taint flags as a colon-separated list. When systemd detects it is running on a system with certain problems, it will set an appropriate taint flag. Taints may be used to lower the chance of bogus bug reports. The following taints are currently known: &quot;split-usr&quot;, &quot;mtab-not-symlink&quot;, &quot;cgroups-missing&quot;, &quot;local-hwclock&quot;. &quot;split-usr&quot; is set if /usr/ is not pre-mounted when systemd is first invoked. See m[blue]<code>Booting Without /usr is Broken</code>m[]<font SIZE="-2">[3]</font> for details why this is bad. &quot;mtab-not-symlink&quot; indicates that /etc/mtab is not a symlink to /proc/self/mounts as required. &quot;cgroups-missing&quot; indicates that control groups have not been enabled in the kernel. &quot;local-hwclock&quot; indicates that the local RTC is configured to be in local time rather than UTC. </p>
<p> <i>FirmwareTimestamp</i>, <i>FirmwareTimestampMonotonic</i>, <i>LoaderTimestamp</i>, <i>LoaderTimestampMonotonic</i>, <i>KernelTimestamp</i>, <i>KernelTimestampMonotonic</i>, <i>InitRDTimestamp</i>, <i>InitRDTimestampMonotonic</i>, <i>UserspaceTimestamp</i>, <i>UserspaceTimestampMonotonic</i>, <i>FinishTimestamp</i>, and <i>FinishTimestampMonotonic</i> encode <code>CLOCK_REALTIME</code> and <code>CLOCK_MONOTONIC</code> microsecond timestamps taken when the firmware first began execution, when the boot loader first began execution, when the kernel first began execution, when the initrd first began execution, when the main systemd instance began execution and finally, when all queued startup jobs finished execution. These values are useful for determining boot-time performance. Note that as monotonic time begins with the kernel startup, the <i>KernelTimestampMonotonic</i> timestamp will always be 0 and <i>FirmwareTimestampMonotonic</i> and <i>LoaderTimestampMonotonic</i> are to be read as negative values. Also, not all fields are always available, depending on the used firmware, boot loader or initrd implementation. In these cases the respective pairs of timestamps are both 0, indicating that no data is available. </p>
<p> Similarly, the <i>SecurityStartTimestamp</i>, <i>GeneratorsStartTimestamp</i> and <i>LoadUnitTimestamp</i> (as well as their monotonic and stop counterparts) expose performance data for uploading the security policies to the kernel (such as the SELinux, IMA, or SMACK policies), for running the generator tools and for loading the unit files. </p>
<p> <i>NNames</i> encodes how many unit names are currently known. This only includes names of units that are currently loaded and can be more than the amount of actually loaded units since units may have more than one name. </p>
<p> <i>NJobs</i> encodes how many jobs are currently queued. </p>
<p> <i>NInstalledJobs</i> encodes how many jobs have ever been queued in total. </p>
<p> <i>NFailedJobs</i> encodes how many jobs have ever failed in total. </p>
<p> <i>Progress</i> encodes boot progress as a floating point value between 0.0 and 1.0. This value begins at 0.0 at early-boot and ends at 1.0 when boot is finished and is based on the number of executed and queued jobs. After startup, this field is always 1.0 indicating a finished boot. </p>
<p> <i>Environment</i> encodes the environment block passed to all executed services. It may be altered with bus calls such as <code>SetEnvironment()</code> (see above). </p>
<p> <i>UnitPath</i> encodes the currently active unit file search path. It is an array of file system paths encoded as strings. </p>
<p> <i>Virtualization</i> contains a short ID string describing the virtualization technology the system runs in. On bare-metal hardware this is the empty string. Otherwise, it contains an identifier such as &quot;kvm&quot;, &quot;vmware&quot; and so on. For a full list of IDs see <code><a href="/docs/linux/man/1-systemd-detect-virt/">systemd-detect-virt</a></code>(1). Note that only the &quot;innermost&quot; virtualization technology is exported here. This detects both full-machine virtualizations (VMs) and shared-kernel virtualization (containers). </p>
<p> <i>Architecture</i> contains a short ID string describing the architecture the systemd instance is running on. This follows the same vocabulary as <i>ConditionArchitectures=</i>. </p>
<p> <i>ControlGroup</i> contains the root control group path of this system manager. Note that the root path is encoded as the empty string here (not as &quot;/&quot;!), so that it can be appended to /sys/fs/cgroup/systemd easily. This value will be set to the empty string for the host instance and some other string for container instances.</p>
<h3>Security</h3>
<p>Read access is generally granted to all clients. Additionally, for unprivileged clients, some operations are allowed through the polkit privilege system. Operations which modify unit state (<code>StartUnit()</code>, <code>StopUnit()</code>, <code>KillUnit()</code>, <code>RestartUnit()</code> and similar, <code>SetProperty()</code>) require org.freedesktop.systemd1.manage-units. Operations which modify unit file enablement state (<code>EnableUnitFiles()</code>, <code>DisableUnitFiles()</code>, <code>EnableUnitFilesWithFlags()</code>, <code>DisableUnitFilesWithFlags()</code>, <code>ReenableUnitFiles()</code>, <code>LinkUnitFiles()</code>, <code>PresetUnitFiles</code>, <code>MaskUnitFiles</code>, and similar) require org.freedesktop.systemd1.manage-unit-files. Operations which modify the exported environment (<code>SetEnvironment()</code>, <code>UnsetEnvironment()</code>, <code>UnsetAndSetEnvironment()</code>) require org.freedesktop.systemd1.set-environment. <code>Reload()</code> and <code>Reexecute()</code> require org.freedesktop.systemd1.reload-daemon.</p>
<h2>Unit Objects</h2>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/avahi_2ddaemon_2eservice {
 interface org.freedesktop.systemd1.Unit {
 methods:
 Start(in s mode,
 out o job);
 Stop(in s mode,
 out o job);
 Reload(in s mode,
 out o job);
 Restart(in s mode,
 out o job);
 TryRestart(in s mode,
 out o job);
 ReloadOrRestart(in s mode,
 out o job);
 ReloadOrTryRestart(in s mode,
 out o job);
 EnqueueJob(in s job_type,
 in s job_mode,
 out u job_id,
 out o job_path,
 out s unit_id,
 out o unit_path,
 out s job_type,
 out a(uosos) affected_jobs);
 Kill(in s whom,
 in i signal);
 ResetFailed();
 SetProperties(in b runtime,
 in a(sv) properties);
 Ref();
 Unref();
 Clean(in as mask);
 Freeze();
 Thaw();
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Id = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Names = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Following = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Requires = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Requisite = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Wants = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as BindsTo = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as PartOf = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as RequiredBy = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as RequisiteOf = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as WantedBy = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as BoundBy = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ConsistsOf = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Conflicts = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ConflictedBy = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Before = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as After = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as OnFailure = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as OnFailureOf = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as OnSuccess = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as OnSuccessOf = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Triggers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as TriggeredBy = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as PropagatesReloadTo = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ReloadPropagatedFrom = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as PropagatesStopTo = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as StopPropagatedFrom = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as JoinsNamespaceOf = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as SliceOf = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as RequiresMountsFor = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Documentation = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Description = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s LoadState = '...';
 readonly s ActiveState = '...';
 readonly s FreezerState = '...';
 readonly s SubState = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s FragmentPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SourcePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as DropInPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s UnitFileState = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s UnitFilePreset = '...';
 readonly t StateChangeTimestamp = ...;
 readonly t StateChangeTimestampMonotonic = ...;
 readonly t InactiveExitTimestamp = ...;
 readonly t InactiveExitTimestampMonotonic = ...;
 readonly t ActiveEnterTimestamp = ...;
 readonly t ActiveEnterTimestampMonotonic = ...;
 readonly t ActiveExitTimestamp = ...;
 readonly t ActiveExitTimestampMonotonic = ...;
 readonly t InactiveEnterTimestamp = ...;
 readonly t InactiveEnterTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CanStart = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CanStop = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CanReload = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CanIsolate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as CanClean = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CanFreeze = ...;
 readonly (uo) Job = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b StopWhenUnneeded = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RefuseManualStart = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RefuseManualStop = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b AllowIsolate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b DefaultDependencies = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s OnSuccessJobMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s OnFailureJobMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b IgnoreOnIsolate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b NeedDaemonReload = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as Markers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t JobTimeoutUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t JobRunningTimeoutUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s JobTimeoutAction = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s JobTimeoutRebootArgument = '...';
 readonly b ConditionResult = ...;
 readonly b AssertResult = ...;
 readonly t ConditionTimestamp = ...;
 readonly t ConditionTimestampMonotonic = ...;
 readonly t AssertTimestamp = ...;
 readonly t AssertTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sbbsi) Conditions = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sbbsi) Asserts = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (ss) LoadError = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b Transient = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b Perpetual = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t StartLimitIntervalUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u StartLimitBurst = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StartLimitAction = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s FailureAction = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i FailureActionExitStatus = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SuccessAction = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SuccessActionExitStatus = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RebootArgument = '...';
 readonly ay InvocationID = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s CollectMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as Refs = ['...', ...];
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>Start()</code>, <code>Stop()</code>, <code>Reload()</code>, <code>Restart()</code>, <code>TryRestart()</code>, <code>ReloadOrRestart()</code>, <code>ReloadOrTryRestart()</code>, <code>Kill()</code>, <code>ResetFailed()</code>, and <code>SetProperties()</code> implement the same operation as the respective methods on the Manager object (see above). However, these methods operate on the unit object and hence do not take a unit name parameter. Invoking the methods directly on the Manager object has the advantage of not requiring a <code>GetUnit()</code> call to get the unit object for a specific unit name. Calling the methods on the Manager object is hence a round trip optimization.</p>
<h3>Properties</h3>
<p><i>Id</i> contains the primary name of the unit. </p>
<p> <i>Names</i> contains all names of the unit, including the primary name that is also exposed in <i>Id</i>. </p>
<p> <i>Following</i> either contains the empty string or contains the name of another unit that this unit follows in state. This is used for some device units which reflect the unit state machine of another unit, and which other unit this is might possibly change. </p>
<p> <i>Requires</i>, <i>RequiresOverridable</i>, <i>Requisite</i>, <i>RequisiteOverridable</i>, <i>Wants</i>, <i>BindsTo</i>, <i>RequiredBy</i>, <i>RequiredByOverridable</i>, <i>WantedBy</i>, <i>BoundBy</i>, <i>Conflicts</i>, <i>ConflictedBy</i>, <i>Before</i>, <i>After</i>, <i>OnFailure</i>, <i>Triggers</i>, <i>TriggeredBy</i>, <i>PropagatesReloadTo</i>, and <i>RequiresMountsFor</i> contain arrays which encode the dependencies and their inverse dependencies (where this applies) as configured in the unit file or determined automatically. </p>
<p> <i>Description</i> contains the human readable description string for the unit. </p>
<p> <i>SourcePath</i> contains the path to a configuration file this unit is automatically generated from in case it is not a native unit (in which case it contains the empty string). For example, all mount units generated from /etc/fstab have this field set to /etc/fstab. </p>
<p> <i>Documentation</i> contains a string array with URLs of documentation for this unit. </p>
<p> <i>LoadState</i> contains a state value that reflects whether the configuration file of this unit has been loaded. The following states are currently defined: &quot;loaded&quot;, &quot;error&quot;, and &quot;masked&quot;. &quot;loaded&quot; indicates that the configuration was successfully loaded. &quot;error&quot; indicates that the configuration failed to load. The <i>LoadError</i> field (see below) contains information about the cause of this failure. &quot;masked&quot; indicates that the unit is currently masked out (i.e. symlinked to /dev/null or empty). Note that the <i>LoadState</i> is fully orthogonal to the <i>ActiveState</i> (see below) as units without valid loaded configuration might be active (because configuration might have been reloaded at a time where a unit was already active). </p>
<p> <i>ActiveState</i> contains a state value that reflects whether the unit is currently active or not. The following states are currently defined: &quot;active&quot;, &quot;reloading&quot;, &quot;inactive&quot;, &quot;failed&quot;, &quot;activating&quot;, and &quot;deactivating&quot;. &quot;active&quot; indicates that unit is active (obviously&#8230;). &quot;reloading&quot; indicates that the unit is active and currently reloading its configuration. &quot;inactive&quot; indicates that it is inactive and the previous run was successful or no previous run has taken place yet. &quot;failed&quot; indicates that it is inactive and the previous run was not successful (more information about the reason for this is available on the unit type specific interfaces, for example for services in the <i>Result</i> property, see below). &quot;activating&quot; indicates that the unit has previously been inactive but is currently in the process of entering an active state. Conversely &quot;deactivating&quot; indicates that the unit is currently in the process of deactivation. </p>
<p> <i>SubState</i> encodes states of the same state machine that <i>ActiveState</i> covers, but knows more fine-grained states that are unit-type-specific. Where <i>ActiveState</i> only covers six high-level states, <i>SubState</i> covers possibly many more low-level unit-type-specific states that are mapped to the six high-level states. Note that multiple low-level states might map to the same high-level state, but not vice versa. Not all high-level states have low-level counterparts on all unit types. At this point the low-level states are not documented here, and are more likely to be extended later on than the common high-level states explained above. </p>
<p> <i>FragmentPath</i> contains the unit file path this unit was read from, if there is one (if not, it contains the empty string). </p>
<p> <i>UnitFileState</i> encodes the install state of the unit file of <i>FragmentPath</i>. It currently knows the following states: &quot;enabled&quot;, &quot;enabled-runtime&quot;, &quot;linked&quot;, &quot;linked-runtime&quot;, &quot;masked&quot;, &quot;masked-runtime&quot;, &quot;static&quot;, &quot;disabled&quot;, and &quot;invalid&quot;. &quot;enabled&quot; indicates that a unit file is permanently enabled. &quot;enable-runtime&quot; indicates the unit file is only temporarily enabled and will no longer be enabled after a reboot (that means, it is enabled via /run/ symlinks, rather than /etc/). &quot;linked&quot; indicates that a unit is linked into /etc/ permanently. &quot;linked-runtime&quot; indicates that a unit is linked into /run/ temporarily (until the next reboot). &quot;masked&quot; indicates that the unit file is masked permanently. &quot;masked-runtime&quot; indicates that it is masked in /run/ temporarily (until the next reboot). &quot;static&quot; indicates that the unit is statically enabled, i.e. always enabled and doesn&#8217;t need to be enabled explicitly. &quot;invalid&quot; indicates that it could not be determined whether the unit file is enabled. </p>
<p> <i>InactiveExitTimestamp</i>, <i>InactiveExitTimestampMonotonic</i>, <i>ActiveEnterTimestamp</i>, <i>ActiveEnterTimestampMonotonic</i>, <i>ActiveExitTimestamp</i>, <i>ActiveExitTimestampMonotonic</i>, <i>InactiveEnterTimestamp</i>, and <i>InactiveEnterTimestampMonotonic</i> contain <code>CLOCK_REALTIME</code> and <code>CLOCK_MONOTONIC</code> 64-bit microsecond timestamps of the last time a unit left the inactive state, entered the active state, exited the active state, or entered an inactive state. These are the points in time where the unit transitioned &quot;inactive&quot;/&quot;failed&quot; → &quot;activating&quot;, &quot;activating&quot; → &quot;active&quot;, &quot;active&quot; → &quot;deactivating&quot;, and finally &quot;deactivating&quot; → &quot;inactive&quot;/&quot;failed&quot;. The fields are 0 in case such a transition has not yet been recorded on this boot. </p>
<p> <i>CanStart</i>, <i>CanStop</i>, and <i>CanReload</i> encode as booleans whether the unit supports the start, stop or reload operations. Even if a unit supports such an operation, the client might not necessary have the necessary privileges to execute them. </p>
<p> <i>CanIsolate</i> encodes as a boolean whether the unit may be started in isolation mode. </p>
<p> <i>Job</i> encodes the job ID and job object path of the job currently scheduled or executed for this unit, if there is any. If no job is scheduled or executed, the job id field will be 0. </p>
<p> <i>StopWhenUnneeded</i>, <i>RefuseManualStart</i>, <i>RefuseManualStop</i>, <i>AllowIsolate</i>, <i>DefaultDependencies</i>, <i>OnFailureIsolate</i>, <i>IgnoreOnIsolate</i>, <i>IgnoreOnSnapshot</i> map directly to the corresponding configuration booleans in the unit file. </p>
<p> <i>DefaultControlGroup</i> contains the main control group of this unit as a string. This refers to a group in systemd&#8217;s own &quot;name=systemd&quot; hierarchy, which systemd uses to watch and manipulate the unit and all its processes. </p>
<p> <i>NeedDaemonReload</i> is a boolean that indicates whether the configuration file this unit is loaded from (i.e. <i>FragmentPath</i> or <i>SourcePath</i>) has changed since the configuration was read and hence whether a configuration reload is recommended. </p>
<p> <i>Markers</i> is an array of string flags that can be set using <code>SetUnitProperties()</code> to indicate that the service should be reloaded or restarted. Currently known values are &quot;needs-restart&quot; and &quot;needs-reload&quot;. Package scripts may use the first to mark units for later restart when a new version of the package is installed. Configuration management scripts may use the second to mark units for a later reload when the configuration is adjusted. Those flags are not set by the manager, except to unset as appropriate when when the unit is stopped, restarted, or reloaded. </p>
<p> <i>JobTimeoutUSec</i> maps directly to the corresponding configuration setting in the unit file. </p>
<p> <i>ConditionTimestamp</i> and <i>ConditionTimestampMonotonic</i> contain the <code>CLOCK_REALTIME</code>/<code>CLOCK_MONOTONIC</code> microsecond timestamps of the last time the configured conditions of the unit have been checked or 0 if they have never been checked. Conditions are checked when a unit is requested to start. </p>
<p> <i>ConditionResult</i> contains the condition result of the last time the configured conditions of this unit were checked. </p>
<p> <i>Conditions</i> contains all configured conditions of the unit. For each condition, five fields are given: condition type (e.g. <i>ConditionPathExists</i>), whether the condition is a trigger condition, whether the condition is reversed, the right hand side of the condition (e.g. the path in case of <i>ConditionPathExists</i>), and the status. The status can be 0, in which case the condition hasn&#8217;t been checked yet, a positive value, in which case the condition passed, or a negative value, in which case the condition failed. Currently only 0, +1, and -1 are used, but additional values may be used in the future, retaining the meaning of zero/positive/negative values. </p>
<p> <i>LoadError</i> contains a pair of strings. If the unit failed to load (as encoded in <i>LoadState</i>, see above), then this will include a D-Bus error pair consisting of the error ID and an explanatory human readable string of what happened. If it loaded successfully, this will be a pair of empty strings. </p>
<p> <i>Transient</i> contains a boolean that indicates whether the unit was created as a transient unit (i.e. via <code>CreateTransientUnit()</code> on the manager object).</p>
<h3>Security</h3>
<p>Similarly to methods on the Manager object, read-only access is allowed for everyone. All operations are allowed for clients with the <code>CAP_SYS_ADMIN</code> capability or when the org.freedesktop.systemd1.manage-units privilege is granted by polkit.</p>
<h2>Service Unit Objects</h2>
<p>All service unit objects implement the org.freedesktop.systemd1.Service interface (described here) in addition to the generic org.freedesktop.systemd1.Unit interface (see above). </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/avahi_2ddaemon_2eservice {
 interface org.freedesktop.systemd1.Service {
 methods:
 BindMount(in s source,
 in s destination,
 in b read_only,
 in b mkdir);
 MountImage(in s source,
 in s destination,
 in b read_only,
 in b mkdir,
 in a(ss) options);
 GetProcesses(out a(sus) processes);
 AttachProcesses(in s subcgroup,
 in au pids);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Type = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Restart = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s PIDFile = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s NotifyAccess = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RestartUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutStartUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutStopUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TimeoutAbortUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s TimeoutStartFailureMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s TimeoutStopFailureMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RuntimeMaxUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t WatchdogUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t WatchdogTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t WatchdogTimestampMonotonic = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RootDirectoryStartOnly = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RemainAfterExit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b GuessMainPID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (aiai) RestartPreventExitStatus = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (aiai) RestartForceExitStatus = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (aiai) SuccessExitStatus = ...;
 readonly u MainPID = ...;
 readonly u ControlPID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s BusName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u FileDescriptorStoreMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u NFileDescriptorStore = ...;
 readonly s StatusText = '...';
 readonly i StatusErrno = ...;
 readonly s Result = '...';
 readonly s ReloadResult = '...';
 readonly s CleanResult = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s USBFunctionDescriptors = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s USBFunctionStrings = '...';
 readonly u UID = ...;
 readonly u GID = ...;
 readonly u NRestarts = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s OOMPolicy = '...';
 readonly t ExecMainStartTimestamp = ...;
 readonly t ExecMainStartTimestampMonotonic = ...;
 readonly t ExecMainExitTimestamp = ...;
 readonly t ExecMainExitTimestampMonotonic = ...;
 readonly u ExecMainPID = ...;
 readonly i ExecMainCode = ...;
 readonly i ExecMainStatus = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecCondition = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasasttttuii) ExecConditionEx = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecStartPre = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasasttttuii) ExecStartPreEx = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecStart = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasasttttuii) ExecStartEx = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecStartPost = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasasttttuii) ExecStartPostEx = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecReload = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasasttttuii) ExecReloadEx = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecStop = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasasttttuii) ExecStopEx = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecStopPost = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasasttttuii) ExecStopPostEx = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Slice = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ControlGroup = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryAvailable = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUUsageNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b Delegate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DelegateControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b CPUAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPerSecUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPeriodUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceLatencyTargetUSec = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b BlockIOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t BlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupBlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOReadBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOWriteBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b MemoryAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryHigh = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemorySwapMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s DevicePolicy = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) DeviceAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b TasksAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IPAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPIngressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPEgressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DisableControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMSwap = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMMemoryPressure = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u ManagedOOMMemoryPressureLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMPreference = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) BPFProgram = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Environment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(sb) EnvironmentFiles = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as PassEnvironment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as UnsetEnvironment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u UMask = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCPU = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCPUSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitFSIZE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitFSIZESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitDATA = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitDATASoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSTACK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSTACKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCORE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCORESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRSS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRSSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNOFILE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNOFILESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitAS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitASSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNPROC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNPROCSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMEMLOCK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMEMLOCKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitLOCKS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitLOCKSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSIGPENDING = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSIGPENDINGSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMSGQUEUE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMSGQUEUESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNICE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNICESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTPRIO = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTPRIOSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTTIME = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTTIMESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s WorkingDirectory = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootDirectory = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootImage = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) RootImageOptions = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay RootHash = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootHashPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay RootHashSignature = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootHashSignaturePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootVerity = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(sba(ss)) ExtensionImages = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssba(ss)) MountImages = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i OOMScoreAdjust = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t CoredumpFilter = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i Nice = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IOSchedulingClass = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IOSchedulingPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i CPUSchedulingPolicy = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i CPUSchedulingPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay CPUAffinity = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CPUAffinityFromNUMA = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i NUMAPolicy = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay NUMAMask = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimerSlackNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CPUSchedulingResetOnFork = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b NonBlocking = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardInput = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardInputFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay StandardInputData = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardOutput = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardOutputFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardError = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardErrorFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s TTYPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYReset = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYVHangup = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYVTDisallocate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SyslogIdentifier = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SyslogLevelPrefix = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogLevel = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogFacility = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i LogLevelMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LogRateLimitIntervalUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u LogRateLimitBurst = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly aay LogExtraFields = [[...], ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s LogNamespace = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SecureBits = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t CapabilityBoundingSet = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t AmbientCapabilities = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s User = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Group = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b DynamicUser = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RemoveIPC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(say) SetCredential = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) LoadCredential = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as SupplementaryGroups = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s PAMName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ReadWritePaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ReadOnlyPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as InaccessiblePaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ExecPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as NoExecPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t MountFlags = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateTmp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateDevices = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectClock = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelTunables = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelModules = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelLogs = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectControlGroups = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateNetwork = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateUsers = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateMounts = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateIPC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectHome = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectSystem = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SameProcessGroup = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s UtmpIdentifier = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s UtmpMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) SELinuxContext = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) AppArmorProfile = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) SmackProcessLabel = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b IgnoreSIGPIPE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b NoNewPrivileges = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) SystemCallFilter = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as SystemCallArchitectures = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SystemCallErrorNumber = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) SystemCallLog = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Personality = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b LockPersonality = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) RestrictAddressFamilies = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RuntimeDirectoryPreserve = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u RuntimeDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as RuntimeDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u StateDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as StateDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u CacheDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as CacheDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u LogsDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as LogsDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u ConfigurationDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ConfigurationDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutCleanUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b MemoryDenyWriteExecute = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RestrictRealtime = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RestrictSUIDSGID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RestrictNamespaces = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssbt) BindPaths = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssbt) BindReadOnlyPaths = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) TemporaryFileSystem = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b MountAPIVFS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KeyringMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectProc = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProcSubset = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectHostname = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s NetworkNamespacePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s IPCNamespacePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KillMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i KillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i RestartKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i FinalKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGKILL = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGHUP = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i WatchdogSignal = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>BindMount()</code> and <code>MountImage()</code> implement the same operations as the respective methods on the Manager object (see above). However, these methods operate on the service object and hence do not take a unit name parameter. Invoking the methods directly on the Manager object has the advantage of not requiring a <code>GetUnit()</code> call to get the unit object for a specific unit name. Calling the methods on the Manager object is hence a round trip optimization.</p>
<h3>Properties</h3>
<p>Most properties of the Service interface map directly to the corresponding settings in service unit files. For the sake of brevity, here&#8217;s a list of all exceptions only: </p>
<p> <i>TimeoutStartUSec</i>, <i>TimeoutStopUSec</i> and <i>TimeoutAbortUSec</i> contain the start, stop and abort timeouts, in microseconds. Note the slight difference in naming when compared to the matching unit file settings (see <code><a href="/docs/linux/man/7-systemd-service/">systemd.service</a></code>(7)): these bus properties strictly use microseconds (and thus are suffixed <i>&#8230;USec</i>) while the unit file settings default to a time unit of seconds (and thus are suffixed <i>&#8230;Sec</i>), unless a different unit is explicitly specified. This reflects that fact that internally the service manager deals in microsecond units only, and the bus properties are a relatively low-level (binary) concept exposing this. The unit file settings on the other hand are relatively high-level (string-based) concepts and thus support more user friendly time specifications which default to second time units but allow other units too, if specified. </p>
<p> <i>WatchdogTimestamp</i> and <i>WatchdogTimestampMonotonic</i> contain <code>CLOCK_REALTIME</code>/<code>CLOCK_MONOTONIC</code> microsecond timestamps of the last watchdog ping received from the service, or 0 if none was ever received. </p>
<p> <i>ExecStartPre</i>, <i>ExecStart</i>, <i>ExecStartPost</i>, <i>ExecReload</i>, <i>ExecStop</i>, and <i>ExecStop</i> are arrays of structures where each struct contains: the binary path to execute; an array with all arguments to pass to the executed command, starting with argument 0; a boolean whether it should be considered a failure if the process exits uncleanly; two pairs of <code>CLOCK_REALTIME</code>/<code>CLOCK_MONOTONIC</code> microsecond timestamps when the process began and finished running the last time, or 0 if it never ran or never finished running; the PID of the process, or 0 if it has not run yet; the exit code and status of the last run. This field hence maps more or less to the corresponding setting in the service unit file but is augmented with runtime data. </p>
<p> <i>LimitCPU</i> (and related properties) map more or less directly to the corresponding settings in the service unit files except that if they aren&#8217;t set, their value is 18446744073709551615 (i.e. -1). </p>
<p> <i>Capabilities</i> contains the configured capabilities, as formatted with <code><a href="/docs/linux/man/3-cap_to_text/">cap_to_text</a></code>(3). </p>
<p> <i>SecureBits</i>, <i>CapabilityBoundingSet</i>, <i>MountFlags</i> also correspond to the configured settings of the unit files, but instead of being formatted as strings, they are encoded as the actual binary flags they are. </p>
<p> <i>ExecMainStartTimestamp</i>, <i>ExecMainStartTimestampMonotonic</i>, <i>ExecMainExitTimestamp</i>, <i>ExecMainExitTimestampMonotonic</i>, <i>ExecMainPID</i>, <i>ExecMainCode</i>, <i>ExecMainStatus</i> contain information about the main process of the service as far as it is known. This is often the same runtime information that is stored in <i>ExecStart</i>. However, it deviates for <i>Type=forking</i> services where the main process of the service is not forked off systemd directly. These fields either contain information of the last run of the process or of the current running process. </p>
<p> <i>MainPID</i> and <i>ControlPID</i> contain the main and control PID of the service. The main PID is the current main PID of the service and is 0 when the service currently has no main PID. The control PID is the PID of the current start/stop/reload process running and is 0 if no such process is currently running. That means that <i>ExecMainPID</i> and <i>MainPID</i> differ in the way that the latter immediately reflects whether a main process is currently running while the latter possible contains information collected from the last run even if the process is no longer around. </p>
<p> <i>StatusText</i> contains the status text passed to the service manager via a call to <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3). This may be used by services to inform the service manager about its internal state with a nice explanatory string. </p>
<p> <i>Result</i> encodes the execution result of the last run of the service. It is useful to determine the reason a service failed if it is in the &quot;failed&quot; state (see <i>ActiveState</i> above). The following values are currently known: &quot;success&quot; is set if the unit didn&#8217;t fail. &quot;resources&quot; indicates that not enough resources were available to fork off and execute the service processes. &quot;timeout&quot; indicates that a timeout occurred while executing a service operation. &quot;exit-code&quot; indicates that a service process exited with an unclean exit code. &quot;signal&quot; indicates that a service process exited with an uncaught signal. &quot;core-dump&quot; indicates that a service process exited uncleanly and dumped core. &quot;watchdog&quot; indicates that a service did not send out watchdog ping messages often enough. &quot;start-limit&quot; indicates that a service has been started too frequently in a specific time frame (as configured in <i>StartLimitInterval</i>, <i>StartLimitBurst</i>). </p>
<p> <i>ControlGroup</i> indicates the control group path the processes of this service unit are placed in. </p>
<p> The following properties map 1:1 to corresponding settings in the unit file: <i>RootDirectory</i> <i>RootImage</i> <i>RootImageOptions</i> <i>RootVerity</i> <i>RootHash</i> <i>RootHashSignature</i> <i>MountImages</i> <i>ExtensionImages</i> see <a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a>(5) for their meaning. </p>
<p> <i>MemoryAvailable</i> indicates how much unused memory is available to the unit before the &quot;MemoryMax&quot; or &quot;MemoryHigh&quot; (whichever is lower) limit set by the cgroup memory controller is reached. It will take into consideration limits on all parent slices, other than the limits set on the unit itself.</p>
<h2>Socket Unit Objects</h2>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/avahi_2ddaemon_2esocket {
 interface org.freedesktop.systemd1.Socket {
 methods:
 GetProcesses(out a(sus) processes);
 AttachProcesses(in s subcgroup,
 in au pids);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s BindIPv6Only = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u Backlog = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s BindToDevice = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SocketUser = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SocketGroup = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u SocketMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u DirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b Accept = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b FlushPending = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b Writable = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b KeepAlive = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t KeepAliveTimeUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t KeepAliveIntervalUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u KeepAliveProbes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t DeferAcceptUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b NoDelay = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i Priority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t ReceiveBuffer = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t SendBuffer = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IPTOS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IPTTL = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t PipeSize = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b FreeBind = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b Transparent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b Broadcast = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PassCredentials = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PassSecurity = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PassPacketInfo = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Timestamping = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RemoveOnStop = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) Listen = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Symlinks = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i Mark = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u MaxConnections = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u MaxConnectionsPerSource = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly x MessageQueueMaxMessages = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly x MessageQueueMessageSize = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s TCPCongestion = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ReusePort = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SmackLabel = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SmackLabelIPIn = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SmackLabelIPOut = '...';
 readonly u ControlPID = ...;
 readonly s Result = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u NConnections = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u NAccepted = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u NRefused = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s FileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SocketProtocol = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TriggerLimitIntervalUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u TriggerLimitBurst = ...;
 readonly u UID = ...;
 readonly u GID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecStartPre = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecStartPost = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecStopPre = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecStopPost = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Slice = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ControlGroup = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryAvailable = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUUsageNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b Delegate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DelegateControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b CPUAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPerSecUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPeriodUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceLatencyTargetUSec = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b BlockIOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t BlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupBlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOReadBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOWriteBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b MemoryAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryHigh = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemorySwapMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s DevicePolicy = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) DeviceAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b TasksAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IPAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPIngressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPEgressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DisableControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMSwap = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMMemoryPressure = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u ManagedOOMMemoryPressureLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMPreference = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) BPFProgram = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Environment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(sb) EnvironmentFiles = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as PassEnvironment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as UnsetEnvironment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u UMask = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCPU = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCPUSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitFSIZE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitFSIZESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitDATA = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitDATASoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSTACK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSTACKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCORE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCORESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRSS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRSSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNOFILE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNOFILESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitAS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitASSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNPROC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNPROCSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMEMLOCK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMEMLOCKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitLOCKS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitLOCKSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSIGPENDING = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSIGPENDINGSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMSGQUEUE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMSGQUEUESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNICE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNICESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTPRIO = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTPRIOSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTTIME = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTTIMESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s WorkingDirectory = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootDirectory = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootImage = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) RootImageOptions = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay RootHash = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootHashPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay RootHashSignature = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootHashSignaturePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootVerity = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(sba(ss)) ExtensionImages = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssba(ss)) MountImages = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i OOMScoreAdjust = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t CoredumpFilter = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i Nice = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IOSchedulingClass = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IOSchedulingPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i CPUSchedulingPolicy = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i CPUSchedulingPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay CPUAffinity = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CPUAffinityFromNUMA = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i NUMAPolicy = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay NUMAMask = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimerSlackNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CPUSchedulingResetOnFork = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b NonBlocking = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardInput = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardInputFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay StandardInputData = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardOutput = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardOutputFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardError = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardErrorFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s TTYPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYReset = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYVHangup = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYVTDisallocate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SyslogIdentifier = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SyslogLevelPrefix = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogLevel = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogFacility = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i LogLevelMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LogRateLimitIntervalUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u LogRateLimitBurst = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly aay LogExtraFields = [[...], ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s LogNamespace = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SecureBits = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t CapabilityBoundingSet = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t AmbientCapabilities = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s User = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Group = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b DynamicUser = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RemoveIPC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(say) SetCredential = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) LoadCredential = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as SupplementaryGroups = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s PAMName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ReadWritePaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ReadOnlyPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as InaccessiblePaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ExecPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as NoExecPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t MountFlags = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateTmp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateDevices = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectClock = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelTunables = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelModules = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelLogs = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectControlGroups = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateNetwork = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateUsers = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateMounts = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateIPC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectHome = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectSystem = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SameProcessGroup = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s UtmpIdentifier = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s UtmpMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) SELinuxContext = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) AppArmorProfile = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) SmackProcessLabel = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b IgnoreSIGPIPE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b NoNewPrivileges = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) SystemCallFilter = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as SystemCallArchitectures = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SystemCallErrorNumber = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) SystemCallLog = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Personality = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b LockPersonality = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) RestrictAddressFamilies = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RuntimeDirectoryPreserve = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u RuntimeDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as RuntimeDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u StateDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as StateDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u CacheDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as CacheDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u LogsDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as LogsDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u ConfigurationDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ConfigurationDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutCleanUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b MemoryDenyWriteExecute = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RestrictRealtime = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RestrictSUIDSGID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RestrictNamespaces = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssbt) BindPaths = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssbt) BindReadOnlyPaths = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) TemporaryFileSystem = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b MountAPIVFS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KeyringMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectProc = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProcSubset = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectHostname = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s NetworkNamespacePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s IPCNamespacePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KillMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i KillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i RestartKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i FinalKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGKILL = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGHUP = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i WatchdogSignal = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Properties</h3>
<p>Most of the properties map directly to the corresponding settings in socket unit files. As socket units can include <i>ExecStartPre</i> (and similar) fields which contain information about processes to execute. They also share most of the fields related to the execution context that Service objects expose (see above). </p>
<p> In addition to these properties there are the following: </p>
<p> <i>NAccepted</i> contains the accumulated number of connections ever accepted on this socket. This only applies to sockets with <i>Accept</i> set to &quot;yes&quot;, i.e. those where systemd is responsible for accepted connections. </p>
<p> Similarly <i>NConnections</i> contains the number of currently open connections on this socket. It only applies only to socket units with <i>Accept</i> set to &quot;yes&quot;. </p>
<p> <i>Result</i> encodes the reason why a socket unit failed if it is in the &quot;failed&quot; state (see <i>ActiveState</i> above). The values &quot;success&quot;, &quot;resources&quot;, &quot;timeout&quot;, &quot;exit-code&quot;, &quot;signal&quot; and &quot;core-dump&quot; have the same meaning as they have for the corresponding field of service units (see above). In addition to that, the value &quot;service-failed-permanent&quot; indicates that the service of this socket failed continuously. </p>
<p> <i>FlushPending</i> specifies whether to flush the socket just before entering the listening state. This setting only applies to sockets with <i>Accept=</i> set to &quot;no&quot;.</p>
<h2>Target Unit Objects</h2>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/basic_2etarget {
 interface org.freedesktop.systemd1.Target {
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<p> Target units have neither type-specific methods nor properties.</p>
<h2>Device Unit Objects</h2>
<p>All device unit objects implement the org.freedesktop.systemd1.Device interface (described here) in addition to the generic org.freedesktop.systemd1.Unit interface (see above). </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/dev_2dttyS0_2edevice {
 interface org.freedesktop.systemd1.Device {
 properties:
 readonly s SysFSPath = '...';
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Properties</h3>
<p>Device units only expose a single type-specific property: </p>
<p> <i>SysFSPath</i> contains the sysfs path of the kernel device this object corresponds to.</p>
<h2>Mount Unit Objects</h2>
<p>All mount unit objects implement the org.freedesktop.systemd1.Mount interface (described here) in addition to the generic org.freedesktop.systemd1.Unit interface (see above). </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/home_2emount {
 interface org.freedesktop.systemd1.Mount {
 methods:
 GetProcesses(out a(sus) processes);
 AttachProcesses(in s subcgroup,
 in au pids);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Where = '...';
 readonly s What = '...';
 readonly s Options = '...';
 readonly s Type = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutUSec = ...;
 readonly u ControlPID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u DirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SloppyOptions = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b LazyUnmount = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ForceUnmount = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ReadWriteOnly = ...;
 readonly s Result = '...';
 readonly u UID = ...;
 readonly u GID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecMount = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecUnmount = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecRemount = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Slice = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ControlGroup = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryAvailable = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUUsageNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b Delegate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DelegateControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b CPUAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPerSecUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPeriodUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceLatencyTargetUSec = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b BlockIOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t BlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupBlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOReadBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOWriteBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b MemoryAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryHigh = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemorySwapMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s DevicePolicy = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) DeviceAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b TasksAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IPAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPIngressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPEgressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DisableControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMSwap = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMMemoryPressure = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u ManagedOOMMemoryPressureLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMPreference = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) BPFProgram = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Environment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(sb) EnvironmentFiles = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as PassEnvironment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as UnsetEnvironment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u UMask = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCPU = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCPUSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitFSIZE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitFSIZESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitDATA = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitDATASoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSTACK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSTACKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCORE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCORESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRSS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRSSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNOFILE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNOFILESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitAS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitASSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNPROC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNPROCSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMEMLOCK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMEMLOCKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitLOCKS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitLOCKSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSIGPENDING = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSIGPENDINGSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMSGQUEUE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMSGQUEUESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNICE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNICESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTPRIO = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTPRIOSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTTIME = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTTIMESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s WorkingDirectory = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootDirectory = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootImage = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) RootImageOptions = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay RootHash = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootHashPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay RootHashSignature = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootHashSignaturePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootVerity = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(sba(ss)) ExtensionImages = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssba(ss)) MountImages = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i OOMScoreAdjust = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t CoredumpFilter = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i Nice = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IOSchedulingClass = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IOSchedulingPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i CPUSchedulingPolicy = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i CPUSchedulingPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay CPUAffinity = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CPUAffinityFromNUMA = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i NUMAPolicy = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay NUMAMask = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimerSlackNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CPUSchedulingResetOnFork = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b NonBlocking = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardInput = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardInputFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay StandardInputData = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardOutput = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardOutputFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardError = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardErrorFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s TTYPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYReset = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYVHangup = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYVTDisallocate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SyslogIdentifier = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SyslogLevelPrefix = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogLevel = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogFacility = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i LogLevelMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LogRateLimitIntervalUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u LogRateLimitBurst = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly aay LogExtraFields = [[...], ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s LogNamespace = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SecureBits = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t CapabilityBoundingSet = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t AmbientCapabilities = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s User = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Group = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b DynamicUser = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RemoveIPC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(say) SetCredential = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) LoadCredential = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as SupplementaryGroups = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s PAMName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ReadWritePaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ReadOnlyPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as InaccessiblePaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ExecPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as NoExecPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t MountFlags = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateTmp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateDevices = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectClock = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelTunables = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelModules = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelLogs = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectControlGroups = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateNetwork = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateUsers = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateMounts = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateIPC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectHome = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectSystem = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SameProcessGroup = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s UtmpIdentifier = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s UtmpMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) SELinuxContext = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) AppArmorProfile = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) SmackProcessLabel = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b IgnoreSIGPIPE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b NoNewPrivileges = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) SystemCallFilter = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as SystemCallArchitectures = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SystemCallErrorNumber = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) SystemCallLog = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Personality = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b LockPersonality = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) RestrictAddressFamilies = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RuntimeDirectoryPreserve = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u RuntimeDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as RuntimeDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u StateDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as StateDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u CacheDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as CacheDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u LogsDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as LogsDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u ConfigurationDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ConfigurationDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutCleanUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b MemoryDenyWriteExecute = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RestrictRealtime = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RestrictSUIDSGID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RestrictNamespaces = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssbt) BindPaths = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssbt) BindReadOnlyPaths = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) TemporaryFileSystem = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b MountAPIVFS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KeyringMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectProc = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProcSubset = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectHostname = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s NetworkNamespacePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s IPCNamespacePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KillMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i KillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i RestartKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i FinalKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGKILL = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGHUP = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i WatchdogSignal = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Properties</h3>
<p>Most of the properties map directly to the corresponding settings in mount unit files. As mount units invoke the /usr/bin/mount command, their bus objects include implicit <i>ExecMount</i> (and similar) fields which contain information about processes to execute. They also share most of the fields related to the execution context that Service objects expose (see above). In addition to these properties there are the following: </p>
<p> <i>ControlPID</i> contains the PID of the currently running /usr/bin/mount or /usr/bin/umount command if there is one running, otherwise 0. </p>
<p> <i>Result</i> contains a value explaining why a mount unit failed if it failed. It can take the values &quot;success&quot;, &quot;resources&quot;, &quot;timeout&quot;, &quot;exit-code&quot;, &quot;signal&quot;, or &quot;core-dump&quot; which have the identical meaning as the corresponding values of the corresponding field of service unit objects (see above).</p>
<h2>Automount Unit Objects</h2>
<p>All automount unit objects implement the org.freedesktop.systemd1.Automount interface (described here) in addition to the generic org.freedesktop.systemd1.Unit interface (see above). </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/proc_2dsys_2dfs_2dbinfmt_5fmisc_2eautomount {
 interface org.freedesktop.systemd1.Automount {
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Where = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u DirectoryMode = ...;
 readonly s Result = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutIdleUSec = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Properties</h3>
<p>Most of the properties map directly to the corresponding settings in the automount unit files. </p>
<p> <i>Result</i> knows the values &quot;success&quot; and &quot;resources&quot; at this time. They have the same meanings as the corresponding values of the corresponding field of the Service object.</p>
<h2>Timer Unit Objects</h2>
<p>All timer unit objects implement the org.freedesktop.systemd1.Timer interface (described here) in addition to the generic org.freedesktop.systemd1.Unit interface (see above). </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/systemd_2dtmpfiles_2dclean_2etimer {
 interface org.freedesktop.systemd1.Timer {
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Unit = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(stt) TimersMonotonic = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sst) TimersCalendar = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b OnClockChange = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b OnTimezoneChange = ...;
 readonly t NextElapseUSecRealtime = ...;
 readonly t NextElapseUSecMonotonic = ...;
 readonly t LastTriggerUSec = ...;
 readonly t LastTriggerUSecMonotonic = ...;
 readonly s Result = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t AccuracyUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RandomizedDelayUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b FixedRandomDelay = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b Persistent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b WakeSystem = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RemainAfterElapse = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Properties</h3>
<p><i>Unit</i> contains the name of the unit to activate when the timer elapses. </p>
<p> <i>TimersMonotonic</i> contains an array of structs that contain information about all monotonic timers of this timer unit. The structs contain a string identifying the timer base, which is one of &quot;OnActiveUSec&quot;, &quot;OnBootUSec&quot;, &quot;OnStartupUSec&quot;, &quot;OnUnitActiveUSec&quot;, or &quot;OnUnitInactiveUSec&quot; which correspond to the settings of the same names in the timer unit files; the microsecond offset from this timer base in monotonic time; the next elapsation point on the <code>CLOCK_MONOTONIC</code> clock, relative to its epoch. </p>
<p> <i>TimersCalendar</i> contains an array of structs that contain information about all realtime/calendar timers of this timer unit. The structs contain a string identifying the timer base, which may only be &quot;OnCalendar&quot; for now; the calendar specification string; the next elapsation point on the <code>CLOCK_REALTIME</code> clock, relative to its epoch. </p>
<p> <i>NextElapseUSecRealtime</i> contains the next elapsation point on the <code>CLOCK_REALTIME</code> clock in miscroseconds since the epoch, or 0 if this timer event does not include at least one calendar event. </p>
<p> Similarly, <i>NextElapseUSecMonotonic</i> contains the next elapsation point on the <code>CLOCK_MONOTONIC</code> clock in microseconds since the epoch, or 0 if this timer event does not include at least one monotonic event. </p>
<p> <i>Result</i> knows the values &quot;success&quot; and &quot;resources&quot; with the same meanings as the matching values of the corresponding property of the service interface.</p>
<h2>Swap Unit Objects</h2>
<p>All swap unit objects implement the org.freedesktop.systemd1.Swap interface (described here) in addition to the generic org.freedesktop.systemd1.Unit interface (see above). </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/dev_2dsda3_2eswap {
 interface org.freedesktop.systemd1.Swap {
 methods:
 GetProcesses(out a(sus) processes);
 AttachProcesses(in s subcgroup,
 in au pids);
 properties:
 readonly s What = '...';
 readonly i Priority = ...;
 readonly s Options = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutUSec = ...;
 readonly u ControlPID = ...;
 readonly s Result = '...';
 readonly u UID = ...;
 readonly u GID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecActivate = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;invalidates&quot;)
 readonly a(sasbttttuii) ExecDeactivate = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Slice = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ControlGroup = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryAvailable = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUUsageNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b Delegate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DelegateControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b CPUAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPerSecUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPeriodUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceLatencyTargetUSec = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b BlockIOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t BlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupBlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOReadBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOWriteBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b MemoryAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryHigh = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemorySwapMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s DevicePolicy = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) DeviceAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b TasksAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IPAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPIngressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPEgressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DisableControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMSwap = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMMemoryPressure = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u ManagedOOMMemoryPressureLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMPreference = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) BPFProgram = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as Environment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(sb) EnvironmentFiles = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as PassEnvironment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as UnsetEnvironment = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u UMask = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCPU = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCPUSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitFSIZE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitFSIZESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitDATA = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitDATASoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSTACK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSTACKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCORE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitCORESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRSS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRSSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNOFILE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNOFILESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitAS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitASSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNPROC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNPROCSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMEMLOCK = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMEMLOCKSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitLOCKS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitLOCKSSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSIGPENDING = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitSIGPENDINGSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMSGQUEUE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitMSGQUEUESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNICE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitNICESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTPRIO = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTPRIOSoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTTIME = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LimitRTTIMESoft = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s WorkingDirectory = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootDirectory = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootImage = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) RootImageOptions = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay RootHash = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootHashPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay RootHashSignature = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootHashSignaturePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RootVerity = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(sba(ss)) ExtensionImages = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssba(ss)) MountImages = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i OOMScoreAdjust = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t CoredumpFilter = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i Nice = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IOSchedulingClass = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i IOSchedulingPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i CPUSchedulingPolicy = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i CPUSchedulingPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay CPUAffinity = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CPUAffinityFromNUMA = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i NUMAPolicy = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay NUMAMask = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimerSlackNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b CPUSchedulingResetOnFork = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b NonBlocking = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardInput = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardInputFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly ay StandardInputData = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardOutput = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardOutputFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardError = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s StandardErrorFileDescriptorName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s TTYPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYReset = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYVHangup = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b TTYVTDisallocate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogPriority = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s SyslogIdentifier = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SyslogLevelPrefix = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogLevel = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SyslogFacility = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i LogLevelMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t LogRateLimitIntervalUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u LogRateLimitBurst = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly aay LogExtraFields = [[...], ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s LogNamespace = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SecureBits = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t CapabilityBoundingSet = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t AmbientCapabilities = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s User = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Group = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b DynamicUser = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RemoveIPC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(say) SetCredential = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) LoadCredential = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as SupplementaryGroups = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s PAMName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ReadWritePaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ReadOnlyPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as InaccessiblePaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ExecPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as NoExecPaths = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t MountFlags = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateTmp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateDevices = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectClock = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelTunables = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelModules = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectKernelLogs = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectControlGroups = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateNetwork = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateUsers = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateMounts = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b PrivateIPC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectHome = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectSystem = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SameProcessGroup = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s UtmpIdentifier = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s UtmpMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) SELinuxContext = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) AppArmorProfile = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bs) SmackProcessLabel = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b IgnoreSIGPIPE = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b NoNewPrivileges = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) SystemCallFilter = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as SystemCallArchitectures = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i SystemCallErrorNumber = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) SystemCallLog = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Personality = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b LockPersonality = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (bas) RestrictAddressFamilies = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s RuntimeDirectoryPreserve = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u RuntimeDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as RuntimeDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u StateDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as StateDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u CacheDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as CacheDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u LogsDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as LogsDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u ConfigurationDirectoryMode = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly as ConfigurationDirectory = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutCleanUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b MemoryDenyWriteExecute = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RestrictRealtime = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b RestrictSUIDSGID = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RestrictNamespaces = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssbt) BindPaths = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ssbt) BindReadOnlyPaths = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) TemporaryFileSystem = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b MountAPIVFS = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KeyringMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProtectProc = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s ProcSubset = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b ProtectHostname = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s NetworkNamespacePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s IPCNamespacePath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KillMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i KillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i RestartKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i FinalKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGKILL = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGHUP = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i WatchdogSignal = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Properties</h3>
<p>Most of the properties map directly to the corresponding settings in swap unit files. As mount units invoke the <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8) command, their bus objects include implicit <i>ExecActivate</i> (and similar) fields which contain information about processes to execute. They also share most of the fields related to the execution context that Service objects expose (see above). In addition to these properties there are the following: </p>
<p> <i>ControlPID</i> contains the PID of the currently running <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8) or <code><a href="/docs/linux/man/8-swapoff/">swapoff</a></code>(8) command if there is one running, otherwise 0. </p>
<p> <i>Result</i> contains a value explaining why a mount unit failed if it failed. It can take the values &quot;success&quot;, &quot;resources&quot;, &quot;timeout&quot;, &quot;exit-code&quot;, &quot;signal&quot;, or &quot;core-dump&quot; which have the identical meanings as the corresponding values of the corresponding field of service unit objects (see above).</p>
<h2>Path Unit Objects</h2>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/cups_2epath {
 interface org.freedesktop.systemd1.Path {
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Unit = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly a(ss) Paths = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b MakeDirectory = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u DirectoryMode = ...;
 readonly s Result = '...';
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Properties</h3>
<p>Most properties correspond directly with the matching settings in path unit files. </p>
<p> The others: </p>
<p> <i>Paths</i> contains an array of structs. Each struct contains the condition to watch, which can be one of &quot;PathExists&quot;, &quot;PathExistsGlob&quot;, &quot;PathChanged&quot;, &quot;PathModified&quot;, or &quot;DirectoryNotEmpty&quot; which correspond directly to the matching settings in the path unit files; and the path to watch, possibly including glob expressions. </p>
<p> <i>Result</i> contains a result value which can be &quot;success&quot; or &quot;resources&quot; which have the same meaning as the corresponding field of the Service interface.</p>
<h2>Slice Unit Objects</h2>
<p>All slice unit objects implement the org.freedesktop.systemd1.Slice interface (described here) in addition to the generic org.freedesktop.systemd1.Unit interface (see above). </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/system_2eslice {
 interface org.freedesktop.systemd1.Slice {
 methods:
 GetProcesses(out a(sus) processes);
 AttachProcesses(in s subcgroup,
 in au pids);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Slice = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ControlGroup = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryAvailable = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUUsageNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b Delegate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DelegateControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b CPUAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPerSecUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPeriodUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceLatencyTargetUSec = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b BlockIOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t BlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupBlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOReadBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOWriteBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b MemoryAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryHigh = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemorySwapMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s DevicePolicy = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) DeviceAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b TasksAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IPAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPIngressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPEgressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DisableControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMSwap = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMMemoryPressure = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u ManagedOOMMemoryPressureLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMPreference = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) BPFProgram = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindDeny = [...];
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Properties</h3>
<p>Most properties correspond directly with the matching settings in slice unit files.</p>
<h2>Scope Unit Objects</h2>
<p>All scope unit objects implement the org.freedesktop.systemd1.Scope interface (described here) in addition to the generic org.freedesktop.systemd1.Unit interface (see above). </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/unit/session_2d1_2escope {
 interface org.freedesktop.systemd1.Scope {
 methods:
 Abandon();
 GetProcesses(out a(sus) processes);
 AttachProcesses(in s subcgroup,
 in au pids);
 signals:
 RequestStop();
 properties:
 readonly s Controller = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t TimeoutStopUSec = ...;
 readonly s Result = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly t RuntimeMaxUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Slice = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ControlGroup = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryAvailable = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUUsageNSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay EffectiveMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksCurrent = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPIngressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IPEgressPackets = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOReadOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteBytes = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWriteOperations = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b Delegate = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DelegateControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b CPUAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupCPUShares = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPerSecUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CPUQuotaPeriodUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedCPUs = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly ay AllowedMemoryNodes = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t IOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteBandwidthMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOReadIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IOWriteIOPSMax = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) IODeviceLatencyTargetUSec = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b BlockIOAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t BlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t StartupBlockIOWeight = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIODeviceWeight = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOReadBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(st) BlockIOWriteBandwidth = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b MemoryAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t DefaultMemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMin = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLow = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryHigh = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemorySwapMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t MemoryLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s DevicePolicy = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) DeviceAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b TasksAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TasksMax = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b IPAccounting = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iayu) IPAddressDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPIngressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as IPEgressFilterPath = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as DisableControllers = ['...', ...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMSwap = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMMemoryPressure = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly u ManagedOOMMemoryPressureLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s ManagedOOMPreference = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(ss) BPFProgram = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindAllow = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly a(iiqq) SocketBindDeny = [...];
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KillMode = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i KillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i RestartKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i FinalKillSignal = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGKILL = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly b SendSIGHUP = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly i WatchdogSignal = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
 interface org.freedesktop.systemd1.Unit { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>Abandon()</code> may be used to place a scope unit in the &quot;abandoned&quot; state. This may be used to inform the system manager that the manager that created the scope lost interest in the scope (for example, because it is terminating), without wanting to shut down the scope entirely.</p>
<h3>Signals</h3>
<p><code>RequestStop</code> is sent to the peer that is configured in the <i>Controller</i> property when systemd is requested to terminate the scope unit. A program registering a scope can use this to cleanly shut down the processes it added to the scope instead of letting systemd do it with the usual <code>SIGTERM</code> logic.</p>
<h3>Properties</h3>
<p>All properties correspond directly with the matching properties of service units. </p>
<p> <i>Controller</i> contains the bus name (unique or well-known) that is notified when the scope unit is to be shut down via a <code>RequestStop</code> signal (see below). This is set when the scope is created. If not set, the scope&#8217;s processes will terminated with <code>SIGTERM</code> directly.</p>
<h2>Job Objects</h2>
<p>Job objects encapsulate scheduled or running jobs. Each unit can have none or one jobs in the execution queue. Each job is attached to exactly one unit. </p>
<dl>
<dd>
<pre>node /org/freedesktop/systemd1/job/666 {
 interface org.freedesktop.systemd1.Job {
 methods:
 Cancel();
 GetAfter(out a(usssoo) jobs);
 GetBefore(out a(usssoo) jobs);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u Id = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly (so) Unit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s JobType = '...';
 readonly s State = '...';
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>Cancel()</code> cancels the job. Note that this will remove a job from the queue if it is not yet executed but generally will not cause a job that is already in the process of being executed to be aborted. This operation may also be requested via the <code>CancelJob()</code> method of the Manager object (see above), which is sometimes useful to reduce roundtrips.</p>
<h3>Properties</h3>
<p><i>Id</i> is the numeric Id of the job. During the runtime of a systemd instance each numeric ID is only assigned once. </p>
<p> <i>Unit</i> refers to the unit this job belongs to. It is a structure consisting of the name of the unit and a bus path to the unit&#8217;s object. </p>
<p> <i>JobType</i> refers to the job&#8217;s type and is one of &quot;start&quot;, &quot;verify-active&quot;, &quot;stop&quot;, &quot;reload&quot;, &quot;restart&quot;, &quot;try-restart&quot;, or &quot;reload-or-start&quot;. Note that later versions might define additional values. </p>
<p> <i>State</i> refers to the job&#8217;s state and is one of &quot;waiting&quot; and &quot;running&quot;. The former indicates that a job is currently queued but has not begun to execute yet. The latter indicates that a job is currently being executed.</p>
<h2>Examples</h2>
<p><code>Example 1. Introspect org.freedesktop.systemd1.Manager on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system \
 --dest org.freedesktop.systemd1 \
 --object-path /org/freedesktop/systemd1</pre>
</dl>
<p> <code>Example 2. Introspect a unit on the bus</code> </p>
<dl>
<dd>
<pre>$ busctl introspect org.freedesktop.systemd1 \
 $(busctl call org.freedesktop.systemd1 \
 /org/freedesktop/systemd1 \
 org.freedesktop.systemd1.Manager \
 GetUnit s systemd-resolved.service | cut -d'&quot;' -f2)</pre>
</dl>
<p> <code>Example 3. Introspect org.freedesktop.systemd1.Job on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system --dest org.freedesktop.systemd1 \
 --object-path /org/freedesktop/systemd1/job/1292</pre>
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
<dd>New Control Group Interface</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/ControlGroupInterface/">https://www.freedesktop.org/wiki/Software/systemd/ControlGroupInterface/</a></dl>
<dt> 3.</p>
<dd>Booting Without /usr is Broken</p>
<dl>
<dd><a rel="nofollow" href="http://freedesktop.org/wiki/Software/systemd/separate-usr-is-broken">http://freedesktop.org/wiki/Software/systemd/separate-usr-is-broken</a></dl>
<dt> 4.</p>
<dd>the usual interface versioning guidelines</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/versioning-dbus.html">http://0pointer.de/blog/projects/versioning-dbus.html</a></dl>
