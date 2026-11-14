---
title: "file-hierarchy(7)"
name: "file-hierarchy"
section: "7"
letter: "f"
url: "/docs/linux/man/7-file-hierarchy/"
description: "file-hierarchy – File system hierarchy overview"
---

<p>file-hierarchy &#8211; File system hierarchy overview</p>
<h2>Description</h2>
<p>Operating systems using the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) system and service manager are organized based on a file system hierarchy inspired by UNIX, more specifically the hierarchy described in the m[blue]<code>File System Hierarchy</code>m[]<font SIZE="-2">[1]</font> specification and <code><a href="/docs/linux/man/7-hier/">hier</a></code>(7), with various extensions, partially documented in the m[blue]<code>XDG Base Directory Specification</code>m[]<font SIZE="-2">[2]</font> and m[blue]<code>XDG User Directories</code>m[]<font SIZE="-2">[3]</font>. This manual page describes a more generalized, though minimal and modernized subset of these specifications that defines more strictly the suggestions and restrictions systemd makes on the file system hierarchy. </p>
<p> Many of the paths described here can be queried with the <code><a href="/docs/linux/man/1-systemd-path/">systemd-path</a></code>(1) tool.</p>
<h2>General Structure</h2>
<p>/</p>
<dl>
<dd>The file system root. Usually writable, but this is not required. Possibly a temporary file system (&quot;tmpfs&quot;). Not shared with other hosts (unless read-only).</dl>
<p> /boot/</p>
<dl>
<dd>The boot partition used for bringing up the system. On EFI systems, this is possibly the EFI System Partition (ESP), also see <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8). This directory is usually strictly local to the host, and should be considered read-only, except when a new kernel or boot loader is installed. This directory only exists on systems that run on physical or emulated hardware that requires boot loaders.</dl>
<p> /efi/</p>
<dl>
<dd>If the boot partition /boot/ is maintained separately from the EFI System Partition (ESP), the latter is mounted here. Tools that need to operate on the EFI system partition should look for it at this mount point first, and fall back to /boot/ &#8212; if the former doesn&#8217;t qualify (for example if it is not a mount point or does not have the correct file system type <code>MSDOS_SUPER_MAGIC</code>).</dl>
<p> /etc/</p>
<dl>
<dd>System-specific configuration. This directory may or may not be read-only. Frequently, this directory is pre-populated with vendor-supplied configuration files, but applications should not make assumptions about this directory being fully populated or populated at all, and should fall back to defaults if configuration is missing.</dl>
<p> /home/</p>
<dl>
<dd>The location for normal user&#8217;s home directories. Possibly shared with other systems, and never read-only. This directory should only be used for normal users, never for system users. This directory and possibly the directories contained within it might only become available or writable in late boot or even only after user authentication. This directory might be placed on limited-functionality network file systems, hence applications should not assume the full set of file API is available on this directory. Applications should generally not reference this directory directly, but via the per-user <i>$HOME</i> environment variable, or via the home directory field of the user database.</dl>
<p> /root/</p>
<dl>
<dd>The home directory of the root user. The root user&#8217;s home directory is located outside of /home/ in order to make sure the root user may log in even without /home/ being available and mounted.</dl>
<p> /srv/</p>
<dl>
<dd>The place to store general server payload, managed by the administrator. No restrictions are made how this directory is organized internally. Generally writable, and possibly shared among systems. This directory might become available or writable only very late during boot.</dl>
<p> /tmp/</p>
<dl>
<dd>The place for small temporary files. This directory is usually mounted as a &quot;tmpfs&quot; instance, and should hence not be used for larger files. (Use /var/tmp/ for larger files.) This directory is usually flushed at boot-up. Also, files that are not accessed within a certain time may be automatically deleted. </p>
<p> If applications find the environment variable <i>$TMPDIR</i> set, they should use the directory specified in it instead of /tmp/ (see <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) and m[blue]<code>IEEE Std 1003.1</code>m[]<font SIZE="-2">[4]</font> for details). </p>
<p> Since /tmp/ is accessible to other users of the system, it is essential that files and subdirectories under this directory are only created with <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3), <code><a href="/docs/linux/man/3-mkdtemp/">mkdtemp</a></code>(3), and similar calls. For more details, see m[blue]<code>Using /tmp/ and /var/tmp/ Safely</code>m[]<font SIZE="-2">[5]</font>.</dl>
<h2>Runtime Data</h2>
<p>/run/</p>
<dl>
<dd>A &quot;tmpfs&quot; file system for system packages to place runtime data in. This directory is flushed on boot, and generally writable for privileged programs only. Always writable.</dl>
<p> /run/log/</p>
<dl>
<dd>Runtime system logs. System components may place private logs in this directory. Always writable, even when /var/log/ might not be accessible yet.</dl>
<p> /run/user/</p>
<dl>
<dd>Contains per-user runtime directories, each usually individually mounted &quot;tmpfs&quot; instances. Always writable, flushed at each reboot and when the user logs out. User code should not reference this directory directly, but via the <i>$XDG_RUNTIME_DIR</i> environment variable, as documented in the m[blue]<code>XDG Base Directory Specification</code>m[]<font SIZE="-2">[2]</font>.</dl>
<h2>Vendor-Supplied Operating System Resources</h2>
<p>/usr/</p>
<dl>
<dd>Vendor-supplied operating system resources. Usually read-only, but this is not required. Possibly shared between multiple hosts. This directory should not be modified by the administrator, except when installing or removing vendor-supplied packages.</dl>
<p> /usr/bin/</p>
<dl>
<dd>Binaries and executables for user commands that shall appear in the <i>$PATH</i> search path. It is recommended not to place binaries in this directory that are not useful for invocation from a shell (such as daemon binaries); these should be placed in a subdirectory of /usr/lib/ instead.</dl>
<p> /usr/include/</p>
<dl>
<dd>C and C++ API header files of system libraries.</dl>
<p> /usr/lib/</p>
<dl>
<dd>Static, private vendor data that is compatible with all architectures (though not necessarily architecture-independent). Note that this includes internal executables or other binaries that are not regularly invoked from a shell. Such binaries may be for any architecture supported by the system. Do not place public libraries in this directory, use <i>$libdir</i> (see below), instead.</dl>
<p> /lib/<i>arch-id</i>/</p>
<dl>
<dd>Location for placing dynamic libraries into, also called <i>$libdir</i>. The architecture identifier to use is defined on m[blue]<code>Multiarch Architecture Specifiers (Tuples)</code>m[]<font SIZE="-2">[6]</font> list. Legacy locations of <i>$libdir</i> are /lib/, /lib64/. This directory should not be used for package-specific data, unless this data is architecture-dependent, too. To query <i>$libdir</i> for the primary architecture of the system, invoke: </p>
<dl>
<dd>
<pre># systemd-path system-library-arch</pre>
</dl>
</dl>
<p> /usr/share/</p>
<dl>
<dd>Resources shared between multiple packages, such as documentation, man pages, time zone information, fonts and other resources. Usually, the precise location and format of files stored below this directory is subject to specifications that ensure interoperability.</dl>
<p> /usr/share/doc/</p>
<dl>
<dd>Documentation for the operating system or system packages.</dl>
<p> /usr/share/factory/etc/</p>
<dl>
<dd>Repository for vendor-supplied default configuration files. This directory should be populated with pristine vendor versions of all configuration files that may be placed in /etc/. This is useful to compare the local configuration of a system with vendor defaults and to populate the local configuration with defaults.</dl>
<p> /usr/share/factory/var/</p>
<dl>
<dd>Similar to /usr/share/factory/etc/, but for vendor versions of files in the variable, persistent data directory /var/.</dl>
<h2>Persistent Variable System Data</h2>
<p>/var/</p>
<dl>
<dd>Persistent, variable system data. Must be writable. This directory might be pre-populated with vendor-supplied data, but applications should be able to reconstruct necessary files and directories in this subhierarchy should they be missing, as the system might start up without this directory being populated. Persistency is recommended, but optional, to support ephemeral systems. This directory might become available or writable only very late during boot. Components that are required to operate during early boot hence shall not unconditionally rely on this directory.</dl>
<p> /var/cache/</p>
<dl>
<dd>Persistent system cache data. System components may place non-essential data in this directory. Flushing this directory should have no effect on operation of programs, except for increased runtimes necessary to rebuild these caches.</dl>
<p> /var/lib/</p>
<dl>
<dd>Persistent system data. System components may place private data in this directory.</dl>
<p> /var/log/</p>
<dl>
<dd>Persistent system logs. System components may place private logs in this directory, though it is recommended to do most logging via the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) and <code><a href="/docs/linux/man/3-sd_journal_print/">sd_journal_print</a></code>(3) calls.</dl>
<p> /var/spool/</p>
<dl>
<dd>Persistent system spool data, such as printer or mail queues.</dl>
<p> /var/tmp/</p>
<dl>
<dd>The place for larger and persistent temporary files. In contrast to /tmp/, this directory is usually mounted from a persistent physical file system and can thus accept larger files. (Use /tmp/ for small ephemeral files.) This directory is generally not flushed at boot-up, but time-based cleanup of files that have not been accessed for a certain time is applied. </p>
<p> If applications find the environment variable <i>$TMPDIR</i> set, they should use the directory specified in it instead of /var/tmp/ (see <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) for details). </p>
<p> The same security restrictions as with /tmp/ apply: <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3), <code><a href="/docs/linux/man/3-mkdtemp/">mkdtemp</a></code>(3), and similar calls should be used. For further details about this directory, see m[blue]<code>Using /tmp/ and /var/tmp/ Safely</code>m[]<font SIZE="-2">[5]</font>.</dl>
<h2>Virtual Kernel And Api File Systems</h2>
<p>/dev/</p>
<dl>
<dd>The root directory for device nodes. Usually, this directory is mounted as a &quot;devtmpfs&quot; instance, but might be of a different type in sandboxed/containerized setups. This directory is managed jointly by the kernel and <code><a href="/docs/linux/man/8-systemd-udevd/">systemd-udevd</a></code>(8), and should not be written to by other components. A number of special purpose virtual file systems might be mounted below this directory.</dl>
<p> /dev/shm/</p>
<dl>
<dd>Place for POSIX shared memory segments, as created via <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3). This directory is flushed on boot, and is a &quot;tmpfs&quot; file system. Since all users have write access to this directory, special care should be taken to avoid name clashes and vulnerabilities. For normal users, shared memory segments in this directory are usually deleted when the user logs out. Usually, it is a better idea to use memory mapped files in /run/ (for system programs) or <i>$XDG_RUNTIME_DIR</i> (for user programs) instead of POSIX shared memory segments, since these directories are not world-writable and hence not vulnerable to security-sensitive name clashes.</dl>
<p> /proc/</p>
<dl>
<dd>A virtual kernel file system exposing the process list and other functionality. This file system is mostly an API to interface with the kernel and not a place where normal files may be stored. For details, see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5). A number of special purpose virtual file systems might be mounted below this directory.</dl>
<p> /proc/sys/</p>
<dl>
<dd>A hierarchy below /proc/ that exposes a number of kernel tunables. The primary way to configure the settings in this API file tree is via <code><a href="/docs/linux/man/5-sysctl-d/">sysctl.d</a></code>(5) files. In sandboxed/containerized setups, this directory is generally mounted read-only.</dl>
<p> /sys/</p>
<dl>
<dd>A virtual kernel file system exposing discovered devices and other functionality. This file system is mostly an API to interface with the kernel and not a place where normal files may be stored. In sandboxed/containerized setups, this directory is generally mounted read-only. A number of special purpose virtual file systems might be mounted below this directory.</dl>
<p> /sys/fs/cgroup/</p>
<dl>
<dd>A virtual kernel file system exposing process control groups (cgroups). This file system is an API to interface with the kernel and not a place where normal files may be stored. On current systems running in the default &quot;unified&quot; mode, this directory serves as the mount point for the &quot;cgroup2&quot; filesystem, which provides a unified cgroup hierarchy for all resource controllers. On systems with non-default configurations, this directory may instead be a tmpfs filesystem containing mount points for various &quot;cgroup&quot; (v1) resource controllers; in such configurations, if &quot;cgroup2&quot; is mounted it will be mounted on /sys/fs/cgroup/unified/, but cgroup2 will not have resource controllers attached. In sandboxed/containerized setups, this directory may either not exist or may include a subset of functionality.</dl>
<h2>Compatibility Symlinks</h2>
<p>/bin/, /sbin/, /usr/sbin/</p>
<dl>
<dd>These compatibility symlinks point to /usr/bin/, ensuring that scripts and binaries referencing these legacy paths correctly find their binaries.</dl>
<p> /lib/</p>
<dl>
<dd>This compatibility symlink points to /lib/, ensuring that programs referencing this legacy path correctly find their resources.</dl>
<p> /lib64/</p>
<dl>
<dd>On some architecture ABIs, this compatibility symlink points to <i>$libdir</i>, ensuring that binaries referencing this legacy path correctly find their dynamic loader. This symlink only exists on architectures whose ABI places the dynamic loader in this path.</dl>
<p> /var/run/</p>
<dl>
<dd>This compatibility symlink points to /run/, ensuring that programs referencing this legacy path correctly find their runtime data.</dl>
<h2>Home Directory</h2>
<p>User applications may want to place files and directories in the user&#8217;s home directory. They should follow the following basic structure. Note that some of these directories are also standardized (though more weakly) by the m[blue]<code>XDG Base Directory Specification</code>m[]<font SIZE="-2">[2]</font>. Additional locations for high-level user resources are defined by m[blue]<code>xdg-user-dirs</code>m[]<font SIZE="-2">[3]</font>. </p>
<p> ~/.cache/</p>
<dl>
<dd>Persistent user cache data. User programs may place non-essential data in this directory. Flushing this directory should have no effect on operation of programs, except for increased runtimes necessary to rebuild these caches. If an application finds <i>$XDG_CACHE_HOME</i> set, it should use the directory specified in it instead of this directory.</dl>
<p> ~/.config/</p>
<dl>
<dd>Application configuration and state. When a new user is created, this directory will be empty or not exist at all. Applications should fall back to defaults should their configuration or state in this directory be missing. If an application finds <i>$XDG_CONFIG_HOME</i> set, it should use the directory specified in it instead of this directory.</dl>
<p> ~/.local/bin/</p>
<dl>
<dd>Executables that shall appear in the user&#8217;s <i>$PATH</i> search path. It is recommended not to place executables in this directory that are not useful for invocation from a shell; these should be placed in a subdirectory of ~/.local/lib/ instead. Care should be taken when placing architecture-dependent binaries in this place, which might be problematic if the home directory is shared between multiple hosts with different architectures.</dl>
<p> ~/.local/lib/</p>
<dl>
<dd>Static, private vendor data that is compatible with all architectures.</dl>
<p> ~/.local/lib/<i>arch-id</i>/</p>
<dl>
<dd>Location for placing public dynamic libraries. The architecture identifier to use is defined on m[blue]<code>Multiarch Architecture Specifiers (Tuples)</code>m[]<font SIZE="-2">[6]</font> list.</dl>
<p> ~/.local/share/</p>
<dl>
<dd>Resources shared between multiple packages, such as fonts or artwork. Usually, the precise location and format of files stored below this directory is subject to specifications that ensure interoperability. If an application finds <i>$XDG_DATA_HOME</i> set, it should use the directory specified in it instead of this directory.</dl>
<h2>Unprivileged Write Access</h2>
<p>Unprivileged processes generally lack write access to most of the hierarchy. </p>
<p> The exceptions for normal users are /tmp/, /var/tmp/, /dev/shm/, as well as the home directory <i>$HOME</i> (usually found below /home/) and the runtime directory <i>$XDG_RUNTIME_DIR</i> (found below /run/user/) of the user, which are all writable. </p>
<p> For unprivileged system processes, only /tmp/, /var/tmp/ and /dev/shm/ are writable. If an unprivileged system process needs a private writable directory in /var/ or /run/, it is recommended to either create it before dropping privileges in the daemon code, to create it via <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) fragments during boot, or via the <i>StateDirectory=</i> and <i>RuntimeDirectory=</i> directives of service units (see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details). </p>
<p> /tmp/, /var/tmp/ and /dev/shm/ should be mounted <code>nosuid</code> and <code>nodev</code>, which means that set-user-id mode and character or block special devices are not interpreted on those file systems. In general it is not possible to mount them <code>noexec</code>, because various programs use those directories for dynamically generated or optimized code, and with that flag those use cases would break. Using this flag is OK on special-purpose installations or systems where all software that may be installed is known and doesn&#8217;t require such functionality. See the discussion of <code>nosuid</code>/<code>nodev</code>/<code>noexec</code> in <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) and <code>PROT_EXEC</code> in <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</p>
<h2>Node Types</h2>
<p>Unix file systems support different types of file nodes, including regular files, directories, symlinks, character and block device nodes, sockets and FIFOs. </p>
<p> It is strongly recommended that /dev/ is the only location below which device nodes shall be placed. Similarly, /run/ shall be the only location to place sockets and FIFOs. Regular files, directories and symlinks may be used in all directories.</p>
<h2>System Packages</h2>
<p>Developers of system packages should follow strict rules when placing their files in the file system. The following table lists recommended locations for specific types of files supplied by the vendor. </p>
<p> <code>Table 1. System package vendor files locations</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Directory </code></td>
<td><code> Purpose </code>
</td>
</tr>
<tr VALIGN=top>
<td> /usr/bin/ </td>
<td> Package executables that shall appear in the <i>$PATH</i> executable search path, compiled for any of the supported architectures compatible with the operating system. It is not recommended to place internal binaries or binaries that are not commonly invoked from the shell in this directory, such as daemon binaries. As this directory is shared with most other packages of the system, special care should be taken to pick unique names for files placed here, that are unlikely to clash with other package&#8217;s files.
</td>
</tr>
<tr VALIGN=top>
<td> /lib/<i>arch-id</i>/ </td>
<td> Public shared libraries of the package. As above, be careful with using too generic names, and pick unique names for your libraries to place here to avoid name clashes.
</td>
</tr>
<tr VALIGN=top>
<td> /lib/<i>package</i>/ </td>
<td> Private static vendor resources of the package, including private binaries and libraries, or any other kind of read-only vendor data.
</td>
</tr>
<tr VALIGN=top>
<td> /lib/<i>arch-id</i>/<i>package</i>/ </td>
<td> Private other vendor resources of the package that are architecture-specific and cannot be shared between architectures. Note that this generally does not include private executables since binaries of a specific architecture may be freely invoked from any other supported system architecture.
</td>
</tr>
<tr VALIGN=top>
<td> /usr/include/<i>package</i>/ </td>
<td> Public C/C++ APIs of public shared libraries of the package.
</td>
</tr>
</table>
<p> Additional static vendor files may be installed in the /usr/share/ hierarchy to the locations defined by the various relevant specifications. </p>
<p> The following directories shall be used by the package for local configuration and files created during runtime: </p>
<p> <code>Table 2. System package variable files locations</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Directory </code></td>
<td><code> Purpose </code>
</td>
</tr>
<tr VALIGN=top>
<td> /etc/<i>package</i>/ </td>
<td> System-specific configuration for the package. It is recommended to default to safe fallbacks if this configuration is missing, if this is possible. Alternatively, a <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) fragment may be used to copy or symlink the necessary files and directories from /usr/share/factory/ during boot, via the &quot;L&quot; or &quot;C&quot; directives.
</td>
</tr>
<tr VALIGN=top>
<td> /run/<i>package</i>/ </td>
<td> Runtime data for the package. Packages must be able to create the necessary subdirectories in this tree on their own, since the directory is flushed automatically on boot. Alternatively, a <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) fragment may be used to create the necessary directories during boot, or the <i>RuntimeDirectory=</i> directive of service units may be used to create them at service startup (see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details).
</td>
</tr>
<tr VALIGN=top>
<td> /run/log/<i>package</i>/ </td>
<td> Runtime log data for the package. As above, the package needs to make sure to create this directory if necessary, as it will be flushed on every boot.
</td>
</tr>
<tr VALIGN=top>
<td> /var/cache/<i>package</i>/ </td>
<td> Persistent cache data of the package. If this directory is flushed, the application should work correctly on next invocation, though possibly slowed down due to the need to rebuild any local cache files. The application must be capable of recreating this directory should it be missing and necessary. To create an empty directory, a <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) fragment or the <i>CacheDirectory=</i> directive of service units (see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5)) may be used.
</td>
</tr>
<tr VALIGN=top>
<td> /var/lib/<i>package</i>/ </td>
<td> Persistent private data of the package. This is the primary place to put persistent data that does not fall into the other categories listed. Packages should be able to create the necessary subdirectories in this tree on their own, since the directory might be missing on boot. To create an empty directory, a <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) fragment or the <i>StateDirectory=</i> directive of service units (see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5)) may be used.
</td>
</tr>
<tr VALIGN=top>
<td> /var/log/<i>package</i>/ </td>
<td> Persistent log data of the package. As above, the package should make sure to create this directory if necessary, possibly using <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) or <i>LogsDirectory=</i> (see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5)), as it might be missing.
</td>
</tr>
<tr VALIGN=top>
<td> /var/spool/<i>package</i>/ </td>
<td> Persistent spool/queue data of the package. As above, the package should make sure to create this directory if necessary, as it might be missing.
</td>
</tr>
</table>
<h2>User Packages</h2>
<p>Programs running in user context should follow strict rules when placing their own files in the user&#8217;s home directory. The following table lists recommended locations in the home directory for specific types of files supplied by the vendor if the application is installed in the home directory. (User applications installed system-wide are covered by the rules outlined above for vendor files.) </p>
<p> <code>Table 3. Vendor package file locations under the home directory of the user</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Directory </code></td>
<td><code> Purpose </code>
</td>
</tr>
<tr VALIGN=top>
<td> ~/.local/bin/ </td>
<td> Package executables that shall appear in the <i>$PATH</i> executable search path. It is not recommended to place internal executables or executables that are not commonly invoked from the shell in this directory, such as daemon executables. As this directory is shared with most other packages of the user, special care should be taken to pick unique names for files placed here, that are unlikely to clash with other package&#8217;s files.
</td>
</tr>
<tr VALIGN=top>
<td> ~/.local/lib/<i>arch-id</i>/ </td>
<td> Public shared libraries of the package. As above, be careful with using overly generic names, and pick unique names for your libraries to place here to avoid name clashes.
</td>
</tr>
<tr VALIGN=top>
<td> ~/.local/lib/<i>package</i>/ </td>
<td> Private, static vendor resources of the package, compatible with any architecture, or any other kind of read-only vendor data.
</td>
</tr>
<tr VALIGN=top>
<td> ~/.local/lib/<i>arch-id</i>/<i>package</i>/ </td>
<td> Private other vendor resources of the package that are architecture-specific and cannot be shared between architectures.
</td>
</tr>
</table>
<p> Additional static vendor files may be installed in the ~/.local/share/ hierarchy, mirroring the subdirectories specified in the section &quot;Vendor-supplied operating system resources&quot; above. </p>
<p> The following directories shall be used by the package for per-user local configuration and files created during runtime: </p>
<p> <code>Table 4. User package variable file locations</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Directory </code></td>
<td><code> Purpose </code>
</td>
</tr>
<tr VALIGN=top>
<td> ~/.config/<i>package</i>/ </td>
<td> User-specific configuration and state for the package. It is required to default to safe fallbacks if this configuration is missing.
</td>
</tr>
<tr VALIGN=top>
<td> <i>$XDG_RUNTIME_DIR</i>/<i>package</i>/ </td>
<td> User runtime data for the package.
</td>
</tr>
<tr VALIGN=top>
<td> ~/.cache/<i>package</i>/ </td>
<td> Persistent cache data of the package. If this directory is flushed, the application should work correctly on next invocation, though possibly slowed down due to the need to rebuild any local cache files. The application must be capable of recreating this directory should it be missing and necessary.
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-hier/">hier</a></code>(7), <code><a href="/docs/linux/man/1-systemd-path/">systemd-path</a></code>(1), <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8), <code><a href="/docs/linux/man/5-sysctl-d/">sysctl.d</a></code>(5), <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5), <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>File System Hierarchy</p>
<dl>
<dd><a rel="nofollow" href="http://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html">http://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html</a></dl>
<dt> 2.</p>
<dd>XDG Base Directory Specification</p>
<dl>
<dd><a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html">http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html</a></dl>
<dt> 3.</p>
<dd>XDG User Directories</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/xdg-user-dirs/">https://www.freedesktop.org/wiki/Software/xdg-user-dirs/</a></dl>
<dt> 4.</p>
<dd>IEEE Std 1003.1</p>
<dl>
<dd><a rel="nofollow" href="http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap08.html#tag_08_03">http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap08.html#tag_08_03</a></dl>
<dt> 5.</p>
<dd>Using /tmp/ and /var/tmp/ Safely</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/TEMPORARY_DIRECTORIES">https://systemd.io/TEMPORARY_DIRECTORIES</a></dl>
<dt> 6.</p>
<dd>Multiarch Architecture Specifiers (Tuples)</p>
<dl>
<dd><a rel="nofollow" href="https://wiki.debian.org/Multiarch/Tuples">https://wiki.debian.org/Multiarch/Tuples</a></dl>
