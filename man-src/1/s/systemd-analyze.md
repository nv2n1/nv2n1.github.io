---
title: "systemd-analyze(1)"
name: "systemd-analyze"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-analyze/"
description: "systemd-analyze – Analyze and debug system manager"
---

<h2 class="name">NAME</h2>
<p> systemd-analyze &#8211; Analyze and debug system manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] [time]</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] blame</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] critical-chain [<i>UNIT</i>&#8230;]</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] dump</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] plot [&gt;file.svg]</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] dot [<i>PATTERN</i>&#8230;] [&gt;file.dot]</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] unit-paths</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] exit-status [<i>STATUS</i>&#8230;]</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] capability [<i>CAPABILITY</i>&#8230;]</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] condition <i>CONDITION</i>&#8230;</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] syscall-filter [<i>SET</i>&#8230;]</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] calendar <i>SPEC</i>&#8230;</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] timestamp <i>TIMESTAMP</i>&#8230;</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] timespan <i>SPAN</i>&#8230;</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] cat-config <i>NAME</i>|<i>PATH</i>&#8230;</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] verify [<i>FILE</i>&#8230;]</p>
<dt> <code>systemd-analyze</code> [OPTIONS&#8230;] security <i>UNIT</i>&#8230;</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-analyze</code></p>
<dd>may be used to determine system boot-up performance statistics and retrieve other state and tracing information from the system and service manager, and to verify the correctness of unit files. It is also used to access special functions useful for advanced system manager debugging. </p>
<p> If no command is passed, <code>systemd-analyze time</code> is implied.</p>
<h3>systemd-analyze time</h3>
<p> This command prints the time spent in the kernel before userspace has been reached, the time spent in the initial RAM disk (initrd) before normal system userspace has been reached, and the time normal system userspace took to initialize. Note that these measurements simply measure the time passed up to the point where all system services have been spawned, but not necessarily until they fully finished initialization or the disk is idle. </p>
<p> <code>Example 1. Show how long the boot took</code> </p>
<dl>
<dt>
<dd>
<pre>
# in a container
$ systemd-analyze time
Startup finished in 296ms (userspace)
multi-user.target reached after 275ms in userspace
# on a real machine
$ systemd-analyze time
Startup finished in 2.584s (kernel) + 19.176s (initrd) + 47.847s (userspace) = 1min 9.608s
multi-user.target reached after 47.820s in userspace
</pre>
</dl>
<h3>systemd-analyze blame</h3>
<p> This command prints a list of all running units, ordered by the time they took to initialize. This information may be used to optimize boot-up times. Note that the output might be misleading as the initialization of one service might be slow simply because it waits for the initialization of another service to complete. Also note: <code>systemd-analyze blame</code> doesn&#8217;t display results for services with <i>Type=simple</i>, because systemd considers such services to be started immediately, hence no measurement of the initialization delays can be done. Also note that this command only shows the time units took for starting up, it does not show how long unit jobs spent in the execution queue. In particular it shows the time units spent in &quot;activating&quot; state, which is not defined for units such as device units that transition directly from &quot;inactive&quot; to &quot;active&quot;. This command hence gives an impression of the performance of program code, but cannot accurately reflect latency introduced by waiting for hardware and similar events. </p>
<p> <code>Example 2. Show which units took the most time during boot</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze blame
         32.875s pmlogger.service
         20.905s systemd-networkd-wait-online.service
         13.299s dev-vda1.device
         ...
            23ms sysroot.mount
            11ms initrd-udevadm-cleanup-db.service
             3ms sys-kernel-config.mount
        
</pre>
</dl>
<h3>systemd-analyze critical-chain [<i>UNIT</i>&#8230;]</h3>
<p> This command prints a tree of the time-critical chain of units (for each of the specified <i>UNIT</i>s or for the default target otherwise). The time after the unit is active or started is printed after the &quot;@&quot; character. The time the unit takes to start is printed after the &quot;+&quot; character. Note that the output might be misleading as the initialization of services might depend on socket activation and because of the parallel execution of units. Also, similar to the <code>blame</code> command, this only takes into account the time units spent in &quot;activating&quot; state, and hence does not cover units that never went through an &quot;activating&quot; state (such as device units that transition directly from &quot;inactive&quot; to &quot;active&quot;). Moreover it does not show information on jobs (and in particular not jobs that timed out). </p>
<p> <code>Example 3. systemd-analyze critical-chain</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze critical-chain
multi-user.target @47.820s
└─pmie.service @35.968s +548ms
  └─pmcd.service @33.715s +2.247s
    └─network-online.target @33.712s
      └─systemd-networkd-wait-online.service @12.804s +20.905s
        └─systemd-networkd.service @11.109s +1.690s
          └─systemd-udevd.service @9.201s +1.904s
            └─systemd-tmpfiles-setup-dev.service @7.306s +1.776s
              └─kmod-static-nodes.service @6.976s +177ms
                └─systemd-journald.socket
                  └─system.slice
                    └─-.slice
</pre>
</dl>
<h3>systemd-analyze dump</h3>
<p> This command outputs a (usually very long) human-readable serialization of the complete server state. Its format is subject to change without notice and should not be parsed by applications. </p>
<p> <code>Example 4. Show the internal state of user manager</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze --user dump
Timestamp userspace: Thu 2019-03-14 23:28:07 CET
Timestamp finish: Thu 2019-03-14 23:28:07 CET
Timestamp generators-start: Thu 2019-03-14 23:28:07 CET
Timestamp generators-finish: Thu 2019-03-14 23:28:07 CET
Timestamp units-load-start: Thu 2019-03-14 23:28:07 CET
Timestamp units-load-finish: Thu 2019-03-14 23:28:07 CET
-&gt; Unit proc-timer_list.mount:
        Description: /proc/timer_list
        ...
-&gt; Unit default.target:
        Description: Main user target
...
</pre>
</dl>
<h3>systemd-analyze plot</h3>
<p> This command prints an SVG graphic detailing which system services have been started at what time, highlighting the time they spent on initialization. </p>
<p> <code>Example 5. Plot a bootchart</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze plot &gt;bootup.svg
$ eog bootup.svg&amp;
</pre>
</dl>
<h3>systemd-analyze dot [<i>pattern</i>&#8230;]</h3>
<p> This command generates textual dependency graph description in dot format for further processing with the GraphViz <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1) tool. Use a command line like <code>systemd-analyze dot | dot -Tsvg &gt;systemd.svg</code> to generate a graphical dependency tree. Unless <code>&#8211;order</code> or <code>&#8211;require</code> is passed, the generated graph will show both ordering and requirement dependencies. Optional pattern globbing style specifications (e.g. *.target) may be given at the end. A unit dependency is included in the graph if any of these patterns match either the origin or destination node. </p>
<p> <code>Example 6. Plot all dependencies of any unit whose name starts with &quot;avahi-daemon&quot;</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze dot 'avahi-daemon.*' | dot -Tsvg &gt;avahi.svg
$ eog avahi.svg
</pre>
</dl>
<p> <code>Example 7. Plot the dependencies between all known target units</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze dot --to-pattern='*.target' --from-pattern='*.target' \
      | dot -Tsvg &gt;targets.svg
$ eog targets.svg
</pre>
</dl>
<h3>systemd-analyze unit-paths</h3>
<p> This command outputs a list of all directories from which unit files, .d overrides, and .wants, .requires symlinks may be loaded. Combine with <code>&#8211;user</code> to retrieve the list for the user manager instance, and <code>&#8211;global</code> for the global configuration of user manager instances. </p>
<p> <code>Example 8. Show all paths for generated units</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze unit-paths | grep '^/run'
/run/systemd/system.control
/run/systemd/transient
/run/systemd/generator.early
/run/systemd/system
/run/systemd/system.attached
/run/systemd/generator
/run/systemd/generator.late
</pre>
</dl>
<p> Note that this verb prints the list that is compiled into <code>systemd-analyze</code> itself, and does not communicate with the running manager. Use </p>
<dl>
<dt>
<dd>
<pre><code>
systemctl[--user][--global] show - p UnitPath-- value
</code></pre>
</dl>
<p> to retrieve the actual list that the manager uses, with any empty directories omitted.</p>
<h3>systemd-analyze exit-status [<i>STATUS</i>&#8230;]</h3>
<p> This command prints a list of exit statuses along with their &quot;class&quot;, i.e. the source of the definition (one of &quot;glibc&quot;, &quot;systemd&quot;, &quot;LSB&quot;, or &quot;BSD&quot;), see the Process Exit Codes section in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5). If no additional arguments are specified, all known statuses are shown. Otherwise, only the definitions for the specified codes are shown. </p>
<p> <code>Example 9. Show some example exit status names</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze exit-status 0 1 {63..65}
NAME    STATUS CLASS
SUCCESS 0      glibc
FAILURE 1      glibc
-       63     -
USAGE   64     BSD
DATAERR 65     BSD
</pre>
</dl>
<h3>systemd-analyze capability [<i>CAPABILITY</i>&#8230;]</h3>
<p> This command prints a list of Linux capabilities along with their numeric IDs. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for details. If no argument is specified the full list of capabilities known to the service manager and the kernel is shown. Capabilities defined by the kernel but not known to the service manager are shown as &quot;cap_???&quot;. Optionally, if arguments are specified they may refer to specific cabilities by name or numeric ID, in which case only the indicated capabilities are shown in the table. </p>
<p> <code>Example 10. Show some example capability names</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze capability 0 1 {30..32}
NAME              NUMBER
cap_chown              0
cap_dac_override       1
cap_audit_control     30
cap_setfcap           31
cap_mac_override      32
</pre>
</dl>
<h3>systemd-analyze condition <i>CONDITION</i>&#8230;</h3>
<p> This command will evaluate <i>Condition*=&#8230;</i> and <i>Assert*=&#8230;</i> assignments, and print their values, and the resulting value of the combined condition set. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for a list of available conditions and asserts. </p>
<p> <code>Example 11. Evaluate conditions that check kernel versions</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze condition 'ConditionKernelVersion = ! &lt;4.0' \
        'ConditionKernelVersion = &gt;=5.1' \
        'ConditionACPower=|false' \
        'ConditionArchitecture=|!arm' \
        'AssertPathExists=/etc/os-release'
test.service: AssertPathExists=/etc/os-release succeeded.
Asserts succeeded.
test.service: ConditionArchitecture=|!arm succeeded.
test.service: ConditionACPower=|false failed.
test.service: ConditionKernelVersion=&gt;=5.1 succeeded.
test.service: ConditionKernelVersion=!&lt;4.0 succeeded.
Conditions succeeded.
</pre>
</dl>
<h3>systemd-analyze syscall-filter [<i>SET</i>&#8230;]</h3>
<p> This command will list system calls contained in the specified system call set <i>SET</i>, or all known sets if no sets are specified. Argument <i>SET</i> must include the &quot;@&quot; prefix.</p>
<h3>systemd-analyze calendar <i>EXPRESSION</i>&#8230;</h3>
<p> This command will parse and normalize repetitive calendar time events, and will calculate when they elapse next. This takes the same input as the <i>OnCalendar=</i> setting in <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5), following the syntax described in <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7). By default, only the next time the calendar expression will elapse is shown; use <code>&#8211;iterations=</code> to show the specified number of next times the expression elapses. Each time the expression elapses forms a timestamp, see the <code>timestamp</code> verb below. </p>
<p> <code>Example 12. Show leap days in the near future</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze calendar --iterations=5 '*-2-29 0:0:0'
  Original form: *-2-29 0:0:0
Normalized form: *-02-29 00:00:00
    Next elapse: Sat 2020-02-29 00:00:00 UTC
       From now: 11 months 15 days left
       Iter. #2: Thu 2024-02-29 00:00:00 UTC
       From now: 4 years 11 months left
       Iter. #3: Tue 2028-02-29 00:00:00 UTC
       From now: 8 years 11 months left
       Iter. #4: Sun 2032-02-29 00:00:00 UTC
       From now: 12 years 11 months left
       Iter. #5: Fri 2036-02-29 00:00:00 UTC
       From now: 16 years 11 months left
</pre>
</dl>
<h3>systemd-analyze timestamp <i>TIMESTAMP</i>&#8230;</h3>
<p> This command parses a timestamp (i.e. a single point in time) and outputs the normalized form and the difference between this timestamp and now. The timestamp should adhere to the syntax documented in <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7), section &quot;PARSING TIMESTAMPS&quot;. </p>
<p> <code>Example 13. Show parsing of timestamps</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze timestamp yesterday now tomorrow
  Original form: yesterday
Normalized form: Mon 2019-05-20 00:00:00 CEST
       (in UTC): Sun 2019-05-19 22:00:00 UTC
   UNIX seconds: @15583032000
       From now: 1 day 9h ago
  Original form: now
Normalized form: Tue 2019-05-21 09:48:39 CEST
       (in UTC): Tue 2019-05-21 07:48:39 UTC
   UNIX seconds: @1558424919.659757
       From now: 43us ago
  Original form: tomorrow
Normalized form: Wed 2019-05-22 00:00:00 CEST
       (in UTC): Tue 2019-05-21 22:00:00 UTC
   UNIX seconds: @15584760000
       From now: 14h left
</pre>
</dl>
<h3>systemd-analyze timespan <i>EXPRESSION</i>&#8230;</h3>
<p> This command parses a time span (i.e. a difference between two timestamps) and outputs the normalized form and the equivalent value in microseconds. The time span should adhere to the syntax documented in <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7), section &quot;PARSING TIME SPANS&quot;. Values without units are parsed as seconds. </p>
<p> <code>Example 14. Show parsing of timespans</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze timespan 1s 300s '1year 0.000001s'
Original: 1s
      μs: 1000000
   Human: 1s
Original: 300s
      μs: 300000000
   Human: 5min
Original: 1year 0.000001s
      μs: 31557600000001
   Human: 1y 1us
</pre>
</dl>
<h3>systemd-analyze cat-config <i>NAME</i>|<i>PATH</i>&#8230;</h3>
<p> This command is similar to <code>systemctl cat</code>, but operates on config files. It will copy the contents of a config file and any drop-ins to standard output, using the usual systemd set of directories and rules for precedence. Each argument must be either an absolute path including the prefix (such as /etc/systemd/logind.conf or /usr/lib/systemd/logind.conf), or a name relative to the prefix (such as systemd/logind.conf). </p>
<p> <code>Example 15. Showing logind configuration</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze cat-config systemd/logind.conf
# /etc/systemd/logind.conf
...
[Login]
NAutoVTs=8
...
# /usr/lib/systemd/logind.conf.d/20-test.conf
... some override from another package
# /etc/systemd/logind.conf.d/50-override.conf
... some administrator override
        
</pre>
</dl>
<h3>systemd-analyze verify <i>FILE</i>&#8230;</h3>
<p> This command will load unit files and print warnings if any errors are detected. Files specified on the command line will be loaded, but also any other units referenced by them. The full unit search path is formed by combining the directories for all command line arguments, and the usual unit load paths. The variable <i>$SYSTEMD_UNIT_PATH</i> is supported, and may be used to replace or augment the compiled in set of unit load paths; see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). All units files present in the directories containing the command line arguments will be used in preference to the other paths. </p>
<p> The following errors are currently detected: </p>
<dl>
<dt>
<dd> &bull; unknown sections and directives,</dl>
<dl>
<dt>
<dd> &bull; missing dependencies which are required to start the given unit,</dl>
<dl>
<dt>
<dd> &bull; man pages listed in <i>Documentation=</i> which are not found in the system,</dl>
<dl>
<dt>
<dd> &bull; commands listed in <i>ExecStart=</i> and similar which are not found in the system or not executable.</dl>
<p> <code>Example 16. Misspelt directives</code> </p>
<dl>
<dt>
<dd>
$ cat./ user.slice<br />
            [Unit] WhatIsThis = 11 Documentation = man : nosuchfile(1)<br />
                                                             Requires = different.service<br />
                                                                            [Service] Description = x<br />
                                                                                                            $ systemd &#8211;<br />
                                                                                                        analyze verify./ user.slice<br />
                                                                                                                         [./ user.slice:9] Unknown lvalue &#8216;WhatIsThis&#8217; in section &#8216;Unit&#8217;<br />
                                                                                                                         [./ user.slice:13] Unknown section &#8216;Service&#8217;.Ignoring.Error : org.freedesktop.systemd1.LoadFailed : Unit different.service failed to load : No such file or<br />
                                                                                                    directory.Failed to create user.slice / start : Invalid argument<br />
                                                                                                                                                        user.slice : man nosuchfile(1) command failed with code 16
</dl>
<p> <code>Example 17. Missing service units</code> </p>
<dl>
<dt>
<dd>
<pre><code>
$ tail./ a.socket./ b.socket == &gt;./ a.socket &lt;= =
                                                    [Socket] ListenStream = 100 == &gt;./ b.socket &lt;= =
                                                                                                       [Socket] ListenStream = 100 Accept = yes
                                                                                                                                                $ systemd -
                                                                                                                                            analyze verify./ a.socket./ b.socket Service a.service not loaded,
                                             a.socket cannot be started.Service b @0.service not loaded, b.socket cannot be started.
</code></pre>
</dl>
<h3>systemd-analyze security [<i>UNIT</i>&#8230;]</h3>
<p> This command analyzes the security and sandboxing settings of one or more specified service units. If at least one unit name is specified the security settings of the specified service units are inspected and a detailed analysis is shown. If no unit name is specified, all currently loaded, long-running service units are inspected and a terse table with results shown. The command checks for various security-related service settings, assigning each a numeric &quot;exposure level&quot; value, depending on how important a setting is. It then calculates an overall exposure level for the whole unit, which is an estimation in the range 0.0&#8230;10.0 indicating how exposed a service is security-wise. High exposure levels indicate very little applied sandboxing. Low exposure levels indicate tight sandboxing and strongest security restrictions. Note that this only analyzes the per-service security features systemd itself implements. This means that any additional security mechanisms applied by the service code itself are not accounted for. The exposure level determined this way should not be misunderstood: a high exposure level neither means that there is no effective sandboxing applied by the service code itself, nor that the service is actually vulnerable to remote or local attacks. High exposure levels do indicate however that most likely the service might benefit from additional settings applied to them. </p>
<p> Please note that many of the security and sandboxing settings individually can be circumvented &#8212; unless combined with others. For example, if a service retains the privilege to establish or undo mount points many of the sandboxing options can be undone by the service code itself. Due to that is essential that each service uses the most comprehensive and strict sandboxing and security settings possible. The tool will take into account some of these combinations and relationships between the settings, but not all. Also note that the security and sandboxing settings analyzed here only apply to the operations executed by the service code itself. If a service has access to an IPC system (such as D-Bus) it might request operations from other services that are not subject to the same restrictions. Any comprehensive security and sandboxing analysis is hence incomplete if the IPC access policy is not validated too. </p>
<p> <code>Example 18. Analyze systemd-logind.service</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-analyze security --no-pager systemd-logind.service
  NAME                DESCRIPTION                              EXPOSURE
✗ PrivateNetwork=     Service has access to the host's network      0.5
✗ User=/DynamicUser=  Service runs as root user                     0.4
✗ DeviceAllow=        Service has no device ACL                     0.2
✓ IPAddressDeny=      Service blocks all IP address ranges
...
→ Overall exposure level for systemd-logind.service: 4.1 OK 
</pre>
</dl>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Operates on the system systemd instance. This is the implied default.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Operates on the user systemd instance.</dl>
<p> <code>&#8211;global</code></p>
<dl>
<dt>
<dd> Operates on the system-wide configuration for user systemd instance.</dl>
<p> <code>&#8211;order</code>, <code>&#8211;require</code></p>
<dl>
<dt>
<dd> When used in conjunction with the <code>dot</code> command (see above), selects which dependencies are shown in the dependency graph. If <code>&#8211;order</code> is passed, only dependencies of type <i>After=</i> or <i>Before=</i> are shown. If <code>&#8211;require</code> is passed, only dependencies of type <i>Requires=</i>, <i>Requisite=</i>, <i>Wants=</i> and <i>Conflicts=</i> are shown. If neither is passed, this shows dependencies of all these types.</dl>
<p> <code>&#8211;from-pattern=</code>, <code>&#8211;to-pattern=</code></p>
<dl>
<dt>
<dd> When used in conjunction with the <code>dot</code> command (see above), this selects which relationships are shown in the dependency graph. Both options require a <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) pattern as an argument, which will be matched against the left-hand and the right-hand, respectively, nodes of a relationship. </p>
<p> Each of these can be used more than once, in which case the unit name must match one of the values. When tests for both sides of the relation are present, a relation must pass both tests to be shown. When patterns are also specified as positional arguments, they must match at least one side of the relation. In other words, patterns specified with those two options will trim the list of edges matched by the positional arguments, if any are given, and fully determine the list of edges shown otherwise.</dl>
<p> <code>&#8211;fuzz=</code><i>timespan</i></p>
<dl>
<dt>
<dd> When used in conjunction with the <code>critical-chain</code> command (see above), also show units, which finished <i>timespan</i> earlier, than the latest unit in the same level. The unit of <i>timespan</i> is seconds unless specified with a different unit, e.g. &quot;50ms&quot;.</dl>
<p> <code>&#8211;man=no</code></p>
<dl>
<dt>
<dd> Do not invoke <code><a href="/docs/linux/man/1-man/">man</a></code>(1) to verify the existence of man pages listed in <i>Documentation=</i>.</dl>
<p> <code>&#8211;generators</code></p>
<dl>
<dt>
<dd> Invoke unit generators, see <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7). Some generators require root privileges. Under a normal user, running with generators enabled will generally result in some warnings.</dl>
<p> <code>&#8211;root=</code><i>PATH</i></p>
<dl>
<dt>
<dd> With <code>cat-files</code>, show config files underneath the specified root path <i>PATH</i>.</dl>
<p> <code>&#8211;iterations=</code><i>NUMBER</i></p>
<dl>
<dt>
<dd> When used with the <code>calendar</code> command, show the specified number of iterations the specified calendar expression will elapse next. Defaults to 1.</dl>
<p> <code>&#8211;base-time=</code><i>TIMESTAMP</i></p>
<dl>
<dt>
<dd> When used with the <code>calendar</code> command, show next iterations relative to the specified point in time. If not specified defaults to the current time.</dl>
<p> <code>-H</code>, <code>&#8211;host=</code></p>
<dl>
<dt>
<dd> Execute the operation remotely. Specify a hostname, or a username and hostname separated by &quot;@&quot;, to connect to. The hostname may optionally be suffixed by a port ssh is listening on, separated by &quot;:&quot;, and then a container name, separated by &quot;/&quot;, which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with <code>machinectl -H </code><i>HOST</i>. Put IPv6 addresses in brackets.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Execute operation on a local container. Specify a container name to connect to, optionally prefixed by a user name to connect as and a separating &quot;@&quot; character. If the special string &quot;.host&quot; is used in place of the container name, a connection to the local system is made (which is useful to connect to a specific user&#8217;s user bus: &quot;&#8211;user &#8211;machine=lennart [at] .host&quot;). If the &quot;@&quot; syntax is not used, the connection is made as root user. If the &quot;@&quot; syntax is used either the left hand side or the right hand side may be omitted (but not both) in which case the local user name and &quot;.host&quot; are implied.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>ENVIRONMENT</h2>
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
<p> <i>$SYSTEMD_LOG_TID</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages will be prefixed with the current numerical thread ID (TID). </p>
<p> Note that the this information is attached as metadata to journal entries anyway. Including it directly in the message text can nevertheless be convenient when debugging programs.</dl>
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
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) </p>
<h2>Index</h2>
<dt><a href="#lbAV">OPTIONS</a></p>
<dd>
<dt><a href="#lbAW">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAX">ENVIRONMENT</a></p>
<dd>
<dt><a href="#lbAY">SEE ALSO</a></p>
<dd></dl>
