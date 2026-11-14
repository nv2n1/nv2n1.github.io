---
title: "daemon(7)"
name: "daemon"
section: "7"
letter: "d"
url: "/docs/linux/man/7-daemon/"
description: "daemon – Writing and packaging system daemons"
---

<p>daemon &#8211; Writing and packaging system daemons</p>
<h2>Description</h2>
<p>A daemon is a service process that runs in the background and supervises the system or provides functionality to other processes. Traditionally, daemons are implemented following a scheme originating in SysV Unix. Modern daemons should follow a simpler yet more powerful scheme (here called &quot;new-style&quot; daemons), as implemented by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1). This manual page covers both schemes, and in particular includes recommendations for daemons that shall be included in the systemd init system.</p>
<h3>SysV Daemons</h3>
<p>When a traditional SysV daemon starts, it should execute the following steps as part of the initialization. Note that these steps are unnecessary for new-style daemons (see below), and should only be implemented if compatibility with SysV is essential. </p>
<dl>
<dd>1. Close all open file descriptors except standard input, output, and error (i.e. the first three file descriptors 0, 1, 2). This ensures that no accidentally passed file descriptor stays around in the daemon process. On Linux, this is best implemented by iterating through /proc/self/fd, with a fallback of iterating from file descriptor 3 to the value returned by <code>getrlimit()</code> for <code>RLIMIT_NOFILE</code>.</dl>
<dl>
<dd>2. Reset all signal handlers to their default. This is best done by iterating through the available signals up to the limit of <code>_NSIG</code> and resetting them to <code>SIG_DFL</code>.</dl>
<dl>
<dd>3. Reset the signal mask using <code>sigprocmask()</code>.</dl>
<dl>
<dd>4. Sanitize the environment block, removing or resetting environment variables that might negatively impact daemon runtime.</dl>
<dl>
<dd>5. Call <code>fork()</code>, to create a background process.</dl>
<dl>
<dd>6. In the child, call <code>setsid()</code> to detach from any terminal and create an independent session.</dl>
<dl>
<dd>7. In the child, call <code>fork()</code> again, to ensure that the daemon can never re-acquire a terminal again. (This relevant if the program &#8212; and all its dependencies &#8212; does not carefully specify `O_NOCTTY` on each and every single `open()` call that might potentially open a TTY device node.)</dl>
<dl>
<dd>8. Call <code>exit()</code> in the first child, so that only the second child (the actual daemon process) stays around. This ensures that the daemon process is re-parented to init/PID 1, as all daemons should be.</dl>
<dl>
<dd>9. In the daemon process, connect /dev/null to standard input, output, and error.</dl>
<dl>
<dd>10. In the daemon process, reset the umask to 0, so that the file modes passed to <code>open()</code>, <code>mkdir()</code> and suchlike directly control the access mode of the created files and directories.</dl>
<dl>
<dd>11. In the daemon process, change the current directory to the root directory (/), in order to avoid that the daemon involuntarily blocks mount points from being unmounted.</dl>
<dl>
<dd>12. In the daemon process, write the daemon PID (as returned by <code>getpid()</code>) to a PID file, for example /run/foobar.pid (for a hypothetical daemon &quot;foobar&quot;) to ensure that the daemon cannot be started more than once. This must be implemented in race-free fashion so that the PID file is only updated when it is verified at the same time that the PID previously stored in the PID file no longer exists or belongs to a foreign process.</dl>
<dl>
<dd>13. In the daemon process, drop privileges, if possible and applicable.</dl>
<dl>
<dd>14. From the daemon process, notify the original process started that initialization is complete. This can be implemented via an unnamed pipe or similar communication channel that is created before the first <code>fork()</code> and hence available in both the original and the daemon process.</dl>
<dl>
<dd>15. Call <code>exit()</code> in the original process. The process that invoked the daemon must be able to rely on that this <code>exit()</code> happens after initialization is complete and all external communication channels are established and accessible.</dl>
<p> The BSD <code>daemon()</code> function should not be used, as it implements only a subset of these steps. </p>
<p> A daemon that needs to provide compatibility with SysV systems should implement the scheme pointed out above. However, it is recommended to make this behavior optional and configurable via a command line argument to ease debugging as well as to simplify integration into systems using systemd.</p>
<h3>New-Style Daemons</h3>
<p>Modern services for Linux should be implemented as new-style daemons. This makes it easier to supervise and control them at runtime and simplifies their implementation. </p>
<p> For developing a new-style daemon, none of the initialization steps recommended for SysV daemons need to be implemented. New-style init systems such as systemd make all of them redundant. Moreover, since some of these steps interfere with process monitoring, file descriptor passing and other functionality of the init system, it is recommended not to execute them when run as new-style service. </p>
<p> Note that new-style init systems guarantee execution of daemon processes in a clean process context: it is guaranteed that the environment block is sanitized, that the signal handlers and mask is reset and that no left-over file descriptors are passed. Daemons will be executed in their own session, with standard input connected to /dev/null and standard output/error connected to the <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8) logging service, unless otherwise configured. The umask is reset. </p>
<p> It is recommended for new-style daemons to implement the following: </p>
<dl>
<dd>1. If <code>SIGTERM</code> is received, shut down the daemon and exit cleanly.</dl>
<dl>
<dd>2. If <code>SIGHUP</code> is received, reload the configuration files, if this applies.</dl>
<dl>
<dd>3. Provide a correct exit code from the main daemon process, as this is used by the init system to detect service errors and problems. It is recommended to follow the exit code scheme as defined in the m[blue]<code>LSB recommendations for SysV init scripts</code>m[]<font SIZE="-2">[1]</font>.</dl>
<dl>
<dd>4. If possible and applicable, expose the daemon&#8217;s control interface via the D-Bus IPC system and grab a bus name as last step of initialization.</dl>
<dl>
<dd>5. For integration in systemd, provide a .service unit file that carries information about starting, stopping and otherwise maintaining the daemon. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details.</dl>
<dl>
<dd>6. As much as possible, rely on the init system&#8217;s functionality to limit the access of the daemon to files, services and other resources, i.e. in the case of systemd, rely on systemd&#8217;s resource limit control instead of implementing your own, rely on systemd&#8217;s privilege dropping code instead of implementing it in the daemon, and similar. See <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for the available controls.</dl>
<dl>
<dd>7. If D-Bus is used, make your daemon bus-activatable by supplying a D-Bus service activation configuration file. This has multiple advantages: your daemon may be started lazily on-demand; it may be started in parallel to other daemons requiring it &#8212; which maximizes parallelization and boot-up speed; your daemon can be restarted on failure without losing any bus requests, as the bus queues requests for activatable services. See below for details.</dl>
<dl>
<dd>8. If your daemon provides services to other local processes or remote clients via a socket, it should be made socket-activatable following the scheme pointed out below. Like D-Bus activation, this enables on-demand starting of services as well as it allows improved parallelization of service start-up. Also, for state-less protocols (such as syslog, DNS), a daemon implementing socket-based activation can be restarted without losing a single request. See below for details.</dl>
<dl>
<dd>9. If applicable, a daemon should notify the init system about startup completion or status updates via the <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3) interface.</dl>
<dl>
<dd>10. Instead of using the <code>syslog()</code> call to log directly to the system syslog service, a new-style daemon may choose to simply log to standard error via <code>fprintf()</code>, which is then forwarded to syslog by the init system. If log levels are necessary, these can be encoded by prefixing individual log lines with strings like &quot;&lt;4&gt;&quot; (for log level 4 &quot;WARNING&quot; in the syslog priority scheme), following a similar style as the Linux kernel&#8217;s <code>printk()</code> level system. For details, see <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3) and <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5).</dl>
<dl>
<dd>11. As new-style daemons are invoked without a controlling TTY (but as their own session leaders) care should be taken to always specify `O_NOCTTY` on `open()` calls that possibly reference a TTY device node, so that no controlling TTY is accidentally acquired.</dl>
<p> These recommendations are similar but not identical to the m[blue]<code>Apple MacOS X Daemon Requirements</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>Activation</h2>
<p>New-style init systems provide multiple additional mechanisms to activate services, as detailed below. It is common that services are configured to be activated via more than one mechanism at the same time. An example for systemd: bluetoothd.service might get activated either when Bluetooth hardware is plugged in, or when an application accesses its programming interfaces via D-Bus. Or, a print server daemon might get activated when traffic arrives at an IPP port, or when a printer is plugged in, or when a file is queued in the printer spool directory. Even for services that are intended to be started on system bootup unconditionally, it is a good idea to implement some of the various activation schemes outlined below, in order to maximize parallelization. If a daemon implements a D-Bus service or listening socket, implementing the full bus and socket activation scheme allows starting of the daemon with its clients in parallel (which speeds up boot-up), since all its communication channels are established already, and no request is lost because client requests will be queued by the bus system (in case of D-Bus) or the kernel (in case of sockets) until the activation is completed.</p>
<h3>Activation on Boot</h3>
<p>Old-style daemons are usually activated exclusively on boot (and manually by the administrator) via SysV init scripts, as detailed in the m[blue]<code>LSB Linux Standard Base Core Specification</code>m[]<font SIZE="-2">[1]</font>. This method of activation is supported ubiquitously on Linux init systems, both old-style and new-style systems. Among other issues, SysV init scripts have the disadvantage of involving shell scripts in the boot process. New-style init systems generally employ updated versions of activation, both during boot-up and during runtime and using more minimal service description files. </p>
<p> In systemd, if the developer or administrator wants to make sure that a service or other unit is activated automatically on boot, it is recommended to place a symlink to the unit file in the .wants/ directory of either multi-user.target or graphical.target, which are normally used as boot targets at system startup. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details about the .wants/ directories, and <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for details about the two boot targets.</p>
<h3>Socket-Based Activation</h3>
<p>In order to maximize the possible parallelization and robustness and simplify configuration and development, it is recommended for all new-style daemons that communicate via listening sockets to employ socket-based activation. In a socket-based activation scheme, the creation and binding of the listening socket as primary communication channel of daemons to local (and sometimes remote) clients is moved out of the daemon code and into the init system. Based on per-daemon configuration, the init system installs the sockets and then hands them off to the spawned process as soon as the respective daemon is to be started. Optionally, activation of the service can be delayed until the first inbound traffic arrives at the socket to implement on-demand activation of daemons. However, the primary advantage of this scheme is that all providers and all consumers of the sockets can be started in parallel as soon as all sockets are established. In addition to that, daemons can be restarted with losing only a minimal number of client transactions, or even any client request at all (the latter is particularly true for state-less protocols, such as DNS or syslog), because the socket stays bound and accessible during the restart, and all requests are queued while the daemon cannot process them. </p>
<p> New-style daemons which support socket activation must be able to receive their sockets from the init system instead of creating and binding them themselves. For details about the programming interfaces for this scheme provided by systemd, see <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3) and <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3). For details about porting existing daemons to socket-based activation, see below. With minimal effort, it is possible to implement socket-based activation in addition to traditional internal socket creation in the same codebase in order to support both new-style and old-style init systems from the same daemon binary. </p>
<p> systemd implements socket-based activation via .socket units, which are described in <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5). When configuring socket units for socket-based activation, it is essential that all listening sockets are pulled in by the special target unit sockets.target. It is recommended to place a <i>WantedBy=sockets.target</i> directive in the [Install] section to automatically add such a dependency on installation of a socket unit. Unless <i>DefaultDependencies=no</i> is set, the necessary ordering dependencies are implicitly created for all socket units. For more information about sockets.target, see <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7). It is not necessary or recommended to place any additional dependencies on socket units (for example from multi-user.target or suchlike) when one is installed in sockets.target.</p>
<h3>Bus-Based Activation</h3>
<p>When the D-Bus IPC system is used for communication with clients, new-style daemons should employ bus activation so that they are automatically activated when a client application accesses their IPC interfaces. This is configured in D-Bus service files (not to be confused with systemd service unit files!). To ensure that D-Bus uses systemd to start-up and maintain the daemon, use the <i>SystemdService=</i> directive in these service files to configure the matching systemd service for a D-Bus service. e.g.: For a D-Bus service whose D-Bus activation file is named org.freedesktop.RealtimeKit.service, make sure to set <i>SystemdService=rtkit-daemon.service</i> in that file to bind it to the systemd service rtkit-daemon.service. This is needed to make sure that the daemon is started in a race-free fashion when activated via multiple mechanisms simultaneously.</p>
<h3>Device-Based Activation</h3>
<p>Often, daemons that manage a particular type of hardware should be activated only when the hardware of the respective kind is plugged in or otherwise becomes available. In a new-style init system, it is possible to bind activation to hardware plug/unplug events. In systemd, kernel devices appearing in the sysfs/udev device tree can be exposed as units if they are tagged with the string &quot;systemd&quot;. Like any other kind of unit, they may then pull in other units when activated (i.e. plugged in) and thus implement device-based activation. systemd dependencies may be encoded in the udev database via the <i>SYSTEMD_WANTS=</i> property. See <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5) for details. Often, it is nicer to pull in services from devices only indirectly via dedicated targets. Example: Instead of pulling in bluetoothd.service from all the various bluetooth dongles and other hardware available, pull in bluetooth.target from them and bluetoothd.service from that target. This provides for nicer abstraction and gives administrators the option to enable bluetoothd.service via controlling a bluetooth.target.wants/ symlink uniformly with a command like <code>enable</code> of <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) instead of manipulating the udev ruleset.</p>
<h3>Path-Based Activation</h3>
<p>Often, runtime of daemons processing spool files or directories (such as a printing system) can be delayed until these file system objects change state, or become non-empty. New-style init systems provide a way to bind service activation to file system changes. systemd implements this scheme via path-based activation configured in .path units, as outlined in <code><a href="/docs/linux/man/5-systemd-path/">systemd.path</a></code>(5).</p>
<h3>Timer-Based Activation</h3>
<p>Some daemons that implement clean-up jobs that are intended to be executed in regular intervals benefit from timer-based activation. In systemd, this is implemented via .timer units, as described in <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5).</p>
<h3>Other Forms of Activation</h3>
<p>Other forms of activation have been suggested and implemented in some systems. However, there are often simpler or better alternatives, or they can be put together of combinations of the schemes above. Example: Sometimes, it appears useful to start daemons or .socket units when a specific IP address is configured on a network interface, because network sockets shall be bound to the address. However, an alternative to implement this is by utilizing the Linux <code>IP_FREEBIND</code>/<code>IPV6_FREEBIND</code> socket option, as accessible via <i>FreeBind=yes</i> in systemd socket files (see <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5) for details). This option, when enabled, allows sockets to be bound to a non-local, not configured IP address, and hence allows bindings to a particular IP address before it actually becomes available, making such an explicit dependency to the configured address redundant. Another often suggested trigger for service activation is low system load. However, here too, a more convincing approach might be to make proper use of features of the operating system, in particular, the CPU or I/O scheduler of Linux. Instead of scheduling jobs from userspace based on monitoring the OS scheduler, it is advisable to leave the scheduling of processes to the OS scheduler itself. systemd provides fine-grained access to the CPU and I/O schedulers. If a process executed by the init system shall not negatively impact the amount of CPU or I/O bandwidth available to other processes, it should be configured with <i>CPUSchedulingPolicy=idle</i> and/or <i>IOSchedulingClass=idle</i>. Optionally, this may be combined with timer-based activation to schedule background jobs during runtime and with minimal impact on the system, and remove it from the boot phase itself.</p>
<h2>Integration With Systemd</h2>
<h3>Writing systemd Unit Files</h3>
<p>When writing systemd unit files, it is recommended to consider the following suggestions: </p>
<dl>
<dd>1. If possible, do not use the <i>Type=forking</i> setting in service files. But if you do, make sure to set the PID file path using <i>PIDFile=</i>. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details.</dl>
<dl>
<dd>2. If your daemon registers a D-Bus name on the bus, make sure to use <i>Type=dbus</i> in the service file if possible.</dl>
<dl>
<dd>3. Make sure to set a good human-readable description string with <i>Description=</i>.</dl>
<dl>
<dd>4. Do not disable <i>DefaultDependencies=</i>, unless you really know what you do and your unit is involved in early boot or late system shutdown.</dl>
<dl>
<dd>5. Normally, little if any dependencies should need to be defined explicitly. However, if you do configure explicit dependencies, only refer to unit names listed on <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) or names introduced by your own package to keep the unit file operating system-independent.</dl>
<dl>
<dd>6. Make sure to include an [Install] section including installation information for the unit file. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. To activate your service on boot, make sure to add a <i>WantedBy=multi-user.target</i> or <i>WantedBy=graphical.target</i> directive. To activate your socket on boot, make sure to add <i>WantedBy=sockets.target</i>. Usually, you also want to make sure that when your service is installed, your socket is installed too, hence add <i>Also=foo.socket</i> in your service file foo.service, for a hypothetical program foo.</dl>
<h3>Installing systemd Service Files</h3>
<p>At the build installation time (e.g. <code>make install</code> during package build), packages are recommended to install their systemd unit files in the directory returned by <code>pkg-config systemd &#8211;variable=systemdsystemunitdir</code> (for system services) or <code>pkg-config systemd &#8211;variable=systemduserunitdir</code> (for user services). This will make the services available in the system on explicit request but not activate them automatically during boot. Optionally, during package installation (e.g. <code>rpm -i</code> by the administrator), symlinks should be created in the systemd configuration directories via the <code>enable</code> command of the <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) tool to activate them automatically on boot. </p>
<p> Packages using <code><a href="/docs/linux/man/1-autoconf/">autoconf</a></code>(1) are recommended to use a configure script excerpt like the following to determine the unit installation path during source configuration: </p>
<dl>
<dd>
<pre>PKG_PROG_PKG_CONFIG
AC_ARG_WITH([systemdsystemunitdir],
 [AS_HELP_STRING([--with-systemdsystemunitdir=DIR], [Directory for systemd service files])],,
 [with_systemdsystemunitdir=auto])
AS_IF([test &quot;x$with_systemdsystemunitdir&quot; = &quot;xyes&quot; -o &quot;x$with_systemdsystemunitdir&quot; = &quot;xauto&quot;], [
 def_systemdsystemunitdir=$($PKG_CONFIG --variable=systemdsystemunitdir systemd)
 AS_IF([test &quot;x$def_systemdsystemunitdir&quot; = &quot;x&quot;],
 [AS_IF([test &quot;x$with_systemdsystemunitdir&quot; = &quot;xyes&quot;],
 [AC_MSG_ERROR([systemd support requested but pkg-config unable to query systemd package])])
 with_systemdsystemunitdir=no],
 [with_systemdsystemunitdir=&quot;$def_systemdsystemunitdir&quot;])])
AS_IF([test &quot;x$with_systemdsystemunitdir&quot; != &quot;xno&quot;],
 [AC_SUBST([systemdsystemunitdir], [$with_systemdsystemunitdir])])
AM_CONDITIONAL([HAVE_SYSTEMD], [test &quot;x$with_systemdsystemunitdir&quot; != &quot;xno&quot;])</pre>
</dl>
<p> This snippet allows automatic installation of the unit files on systemd machines, and optionally allows their installation even on machines lacking systemd. (Modification of this snippet for the user unit directory is left as an exercise for the reader.) </p>
<p> Additionally, to ensure that <code>make distcheck</code> continues to work, it is recommended to add the following to the top-level Makefile.am file in <code><a href="/docs/linux/man/1-automake/">automake</a></code>(1)-based projects: </p>
<dl>
<dd>
<pre>AM_DISTCHECK_CONFIGURE_FLAGS = \
 --with-systemdsystemunitdir=$$dc_install_base/$(systemdsystemunitdir)</pre>
</dl>
<p> Finally, unit files should be installed in the system with an automake excerpt like the following: </p>
<dl>
<dd>
<pre>if HAVE_SYSTEMD
systemdsystemunit_DATA = \
 foobar.socket \
 foobar.service
endif</pre>
</dl>
<p> In the <code><a href="/docs/linux/man/8-rpm/">rpm</a></code>(8) .spec file, use snippets like the following to enable/disable the service during installation/deinstallation. This makes use of the RPM macros shipped along systemd. Consult the packaging guidelines of your distribution for details and the equivalent for other package managers. </p>
<p> At the top of the file: </p>
<dl>
<dd>
<pre>BuildRequires: systemd
%{?systemd_requires}</pre>
</dl>
<p> And as scriptlets, further down: </p>
<dl>
<dd>
<pre>%post
%systemd_post foobar.service foobar.socket
%preun
%systemd_preun foobar.service foobar.socket
%postun
%systemd_postun</pre>
</dl>
<p> If the service shall be restarted during upgrades, replace the &quot;%postun&quot; scriptlet above with the following: </p>
<dl>
<dd>
<pre>%postun
%systemd_postun_with_restart foobar.service</pre>
</dl>
<p> Note that &quot;%systemd_post&quot; and &quot;%systemd_preun&quot; expect the names of all units that are installed/removed as arguments, separated by spaces. &quot;%systemd_postun&quot; expects no arguments. &quot;%systemd_postun_with_restart&quot; expects the units to restart as arguments. </p>
<p> To facilitate upgrades from a package version that shipped only SysV init scripts to a package version that ships both a SysV init script and a native systemd service file, use a fragment like the following: </p>
<dl>
<dd>
<pre>%triggerun -- foobar &lt; 0.47.11-1
if /sbin/chkconfig --level 5 foobar ; then
 /bin/systemctl --no-reload enable foobar.service foobar.socket &gt;/dev/null 2&gt;&amp;1 || :
fi</pre>
</dl>
<p> Where 0.47.11-1 is the first package version that includes the native unit file. This fragment will ensure that the first time the unit file is installed, it will be enabled if and only if the SysV init script is enabled, thus making sure that the enable status is not changed. Note that <code>chkconfig</code> is a command specific to Fedora which can be used to check whether a SysV init script is enabled. Other operating systems will have to use different commands here.</p>
<h2>Porting Existing Daemons</h2>
<p>Since new-style init systems such as systemd are compatible with traditional SysV init systems, it is not strictly necessary to port existing daemons to the new style. However, doing so offers additional functionality to the daemons as well as simplifying integration into new-style init systems. </p>
<p> To port an existing SysV compatible daemon, the following steps are recommended: </p>
<dl>
<dd>1. If not already implemented, add an optional command line switch to the daemon to disable daemonization. This is useful not only for using the daemon in new-style init systems, but also to ease debugging.</dl>
<dl>
<dd>2. If the daemon offers interfaces to other software running on the local system via local <code>AF_UNIX</code> sockets, consider implementing socket-based activation (see above). Usually, a minimal patch is sufficient to implement this: Extend the socket creation in the daemon code so that <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3) is checked for already passed sockets first. If sockets are passed (i.e. when <code>sd_listen_fds()</code> returns a positive value), skip the socket creation step and use the passed sockets. Secondly, ensure that the file system socket nodes for local <code>AF_UNIX</code> sockets used in the socket-based activation are not removed when the daemon shuts down, if sockets have been passed. Third, if the daemon normally closes all remaining open file descriptors as part of its initialization, the sockets passed from the init system must be spared. Since new-style init systems guarantee that no left-over file descriptors are passed to executed processes, it might be a good choice to simply skip the closing of all remaining open file descriptors if sockets are passed.</dl>
<dl>
<dd>3. Write and install a systemd unit file for the service (and the sockets if socket-based activation is used, as well as a path unit file, if the daemon processes a spool directory), see above for details.</dl>
<dl>
<dd>4. If the daemon exposes interfaces via D-Bus, write and install a D-Bus activation file for the service, see above for details.</dl>
<h2>Placing Daemon Data</h2>
<p>It is recommended to follow the general guidelines for placing package files, as discussed in <code><a href="/docs/linux/man/7-file-hierarchy/">file-hierarchy</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3), <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-daemon/">daemon</a></code>(3), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/7-file-hierarchy/">file-hierarchy</a></code>(7)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>LSB recommendations for SysV init scripts</p>
<dl>
<dd><a rel="nofollow" href="http://refspecs.linuxbase.org/LSB_3.1.1/LSB-Core-generic/LSB-Core-generic/iniscrptact.html">http://refspecs.linuxbase.org/LSB_3.1.1/LSB-Core-generic/LSB-Core-generic/iniscrptact.html</a></dl>
<dt> 2.</p>
<dd>Apple MacOS X Daemon Requirements</p>
<dl>
<dd><a rel="nofollow" href="https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html">https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html</a></dl>
