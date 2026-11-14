---
title: "systemd-exec(5)"
name: "systemd-exec"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-exec/"
description: "systemd.exec – Execution environment configuration"
---

<p>systemd.exec &#8211; Execution environment configuration</p>
<h2>Synopsis</h2>
<p><i>service</i>.service, <i>socket</i>.socket, <i>mount</i>.mount, <i>swap</i>.swap</p>
<h2>Description</h2>
<p>Unit configuration files for services, sockets, mount points, and swap devices share a subset of configuration options which define the execution environment of spawned processes. </p>
<p> This man page lists the configuration options shared by these four unit types. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files, and <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), and <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5) for more information on the specific unit configuration files. The execution specific configuration options are configured in the [Service], [Socket], [Mount], or [Swap] sections, depending on the unit type. </p>
<p> In addition, options which control resources through Linux Control Groups (cgroups) are listed in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5). Those options complement options listed here.</p>
<h2>Implicit Dependencies</h2>
<p>A few execution parameters result in additional, automatic dependencies to be added: </p>
<dl>
<dd>&bull; Units with <i>WorkingDirectory=</i>, <i>RootDirectory=</i>, <i>RootImage=</i>, <i>RuntimeDirectory=</i>, <i>StateDirectory=</i>, <i>CacheDirectory=</i>, <i>LogsDirectory=</i> or <i>ConfigurationDirectory=</i> set automatically gain dependencies of type <i>Requires=</i> and <i>After=</i> on all mount units required to access the specified paths. This is equivalent to having them listed explicitly in <i>RequiresMountsFor=</i>.</dl>
<dl>
<dd>&bull; Similarly, units with <i>PrivateTmp=</i> enabled automatically get mount unit dependencies for all mounts required to access /tmp/ and /var/tmp/. They will also gain an automatic <i>After=</i> dependency on <code><a href="/docs/linux/man/8-systemd-tmpfiles-setup-service/">systemd-tmpfiles-setup.service</a></code>(8).</dl>
<dl>
<dd>&bull; Units whose standard output or error output is connected to <code>journal</code> or <code>kmsg</code> (or their combinations with console output, see below) automatically acquire dependencies of type <i>After=</i> on systemd-journald.socket.</dl>
<dl>
<dd>&bull; Units using <i>LogNamespace=</i> will automatically gain ordering and requirement dependencies on the two socket units associated with systemd-journald [at] .service instances.</dl>
<h2>Paths</h2>
<p>The following settings may be used to change a service&#8217;s view of the filesystem. Please note that the paths must be absolute and must not contain a &quot;..&quot; path component. </p>
<p> <i>WorkingDirectory=</i></p>
<dl>
<dd>Takes a directory path relative to the service&#8217;s root directory specified by <i>RootDirectory=</i>, or the special value &quot;~&quot;. Sets the working directory for executed processes. If set to &quot;~&quot;, the home directory of the user specified in <i>User=</i> is used. If not set, defaults to the root directory when systemd is running as a system instance and the respective user&#8217;s home directory if run as user. If the setting is prefixed with the &quot;-&quot; character, a missing working directory is not considered fatal. If <i>RootDirectory=</i>/<i>RootImage=</i> is not set, then <i>WorkingDirectory=</i> is relative to the root of the system running the service manager. Note that setting this parameter might result in additional dependencies to be added to the unit (see above).</dl>
<p> <i>RootDirectory=</i></p>
<dl>
<dd>Takes a directory path relative to the host&#8217;s root directory (i.e. the root of the system running the service manager). Sets the root directory for executed processes, with the <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) system call. If this is used, it must be ensured that the process binary and all its auxiliary files are available in the <code>chroot()</code> jail. Note that setting this parameter might result in additional dependencies to be added to the unit (see above). </p>
<p> The <i>MountAPIVFS=</i> and <i>PrivateUsers=</i> settings are particularly useful in conjunction with <i>RootDirectory=</i>. For details, see below. </p>
<p> If <i>RootDirectory=</i>/<i>RootImage=</i> are used together with <i>NotifyAccess=</i> the notification socket is automatically mounted from the host into the root environment, to ensure the notification interface can work correctly. </p>
<p> Note that services using <i>RootDirectory=</i>/<i>RootImage=</i> will not be able to log via the syslog or journal protocols to the host logging infrastructure, unless the relevant sockets are mounted from the host, specifically: </p>
<p> <code>Example 1. Mounting logging sockets into root environment</code> </p>
<dl>
<dd>
<pre>BindReadOnlyPaths=/dev/log /run/systemd/journal/socket /run/systemd/journal/stdout</pre>
</dl>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>RootImage=</i></p>
<dl>
<dd>Takes a path to a block device node or regular file as argument. This call is similar to <i>RootDirectory=</i> however mounts a file system hierarchy from a block device node or loopback file instead of a directory. The device node or file system image file needs to contain a file system without a partition table, or a file system within an MBR/MS-DOS or GPT partition table with only a single Linux-compatible partition, or a set of file systems within a GPT partition table that follows the m[blue]<code>Discoverable Partitions Specification</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> When <i>DevicePolicy=</i> is set to &quot;closed&quot; or &quot;strict&quot;, or set to &quot;auto&quot; and <i>DeviceAllow=</i> is set, then this setting adds /dev/loop-control with <code>rw</code> mode, &quot;block-loop&quot; and &quot;block-blkext&quot; with <code>rwm</code> mode to <i>DeviceAllow=</i>. See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for the details about <i>DevicePolicy=</i> or <i>DeviceAllow=</i>. Also, see <i>PrivateDevices=</i> below, as it may change the setting of <i>DevicePolicy=</i>. </p>
<p> Units making use of <i>RootImage=</i> automatically gain an <i>After=</i> dependency on systemd-udevd.service. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>RootImageOptions=</i></p>
<dl>
<dd>Takes a comma-separated list of mount options that will be used on disk images specified by <i>RootImage=</i>. Optionally a partition name can be prefixed, followed by colon, in case the image has multiple partitions, otherwise partition name &quot;root&quot; is implied. Options for multiple partitions can be specified in a single line with space separators. Assigning an empty string removes previous assignments. Duplicated options are ignored. For a list of valid mount options, please refer to <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
<p> Valid partition names follow the m[blue]<code>Discoverable Partitions Specification</code>m[]<font SIZE="-2">[1]</font>: <code>root</code>, <code>usr</code>, <code>home</code>, <code>srv</code>, <code>esp</code>, <code>xbootldr</code>, <code>tmp</code>, <code>var</code>. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>RootHash=</i></p>
<dl>
<dd>Takes a data integrity (dm-verity) root hash specified in hexadecimal, or the path to a file containing a root hash in ASCII hexadecimal format. This option enables data integrity checks using dm-verity, if the used image contains the appropriate integrity data (see above) or if <i>RootVerity=</i> is used. The specified hash must match the root hash of integrity data, and is usually at least 256 bits (and hence 64 formatted hexadecimal characters) long (in case of SHA256 for example). If this option is not specified, but the image file carries the &quot;user.verity.roothash&quot; extended file attribute (see <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7)), then the root hash is read from it, also as formatted hexadecimal characters. If the extended file attribute is not found (or is not supported by the underlying file system), but a file with the .roothash suffix is found next to the image file, bearing otherwise the same name (except if the image has the .raw suffix, in which case the root hash file must not have it in its name), the root hash is read from it and automatically used, also as formatted hexadecimal characters. </p>
<p> If the disk image contains a separate /usr/ partition it may also be Verity protected, in which case the root hash may configured via an extended attribute &quot;user.verity.usrhash&quot; or a .usrhash file adjacent to the disk image. There&#8217;s currently no option to configure the root hash for the /usr/ file system via the unit file directly. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>RootHashSignature=</i></p>
<dl>
<dd>Takes a PKCS7 signature of the <i>RootHash=</i> option as a path to a DER-encoded signature file, or as an ASCII base64 string encoding of a DER-encoded signature prefixed by &quot;base64:&quot;. The dm-verity volume will only be opened if the signature of the root hash is valid and signed by a public key present in the kernel keyring. If this option is not specified, but a file with the .roothash.p7s suffix is found next to the image file, bearing otherwise the same name (except if the image has the .raw suffix, in which case the signature file must not have it in its name), the signature is read from it and automatically used. </p>
<p> If the disk image contains a separate /usr/ partition it may also be Verity protected, in which case the signature for the root hash may configured via a .usrhash.p7s file adjacent to the disk image. There&#8217;s currently no option to configure the root hash signature for the /usr/ via the unit file directly. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>RootVerity=</i></p>
<dl>
<dd>Takes the path to a data integrity (dm-verity) file. This option enables data integrity checks using dm-verity, if <i>RootImage=</i> is used and a root-hash is passed and if the used image itself does not contains the integrity data. The integrity data must be matched by the root hash. If this option is not specified, but a file with the .verity suffix is found next to the image file, bearing otherwise the same name (except if the image has the .raw suffix, in which case the verity data file must not have it in its name), the verity data is read from it and automatically used. </p>
<p> This option is supported only for disk images that contain a single file system, without an enveloping partition table. Images that contain a GPT partition table should instead include both root file system and matching Verity data in the same image, implementing the m[blue]<code>Discoverable Partitions Specification</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>MountAPIVFS=</i></p>
<dl>
<dd>Takes a boolean argument. If on, a private mount namespace for the unit&#8217;s processes is created and the API file systems /proc/, /sys/, /dev/ and /run/ (as an empty &quot;tmpfs&quot;) are mounted inside of it, unless they are already mounted. Note that this option has no effect unless used in conjunction with <i>RootDirectory=</i>/<i>RootImage=</i> as these four mounts are generally mounted in the host anyway, and unless the root directory is changed, the private mount namespace will be a 1:1 copy of the host&#8217;s, and include these four mounts. Note that the /dev/ file system of the host is bind mounted if this option is used without <i>PrivateDevices=</i>. To run the service with a private, minimal version of /dev/, combine this option with <i>PrivateDevices=</i>. </p>
<p> In order to allow propagating mounts at runtime in a safe manner, /run/systemd/propagate on the host will be used to set up new mounts, and /run/host/incoming/ in the private namespace will be used as an intermediate step to store them before being moved to the final mount point. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>ProtectProc=</i></p>
<dl>
<dd>Takes one of &quot;noaccess&quot;, &quot;invisible&quot;, &quot;ptraceable&quot; or &quot;default&quot; (which it defaults to). When set, this controls the &quot;hidepid=&quot; mount option of the &quot;procfs&quot; instance for the unit that controls which directories with process metainformation (/proc/<i>PID</i>) are visible and accessible: when set to &quot;noaccess&quot; the ability to access most of other users&#8217; process metadata in /proc/ is taken away for processes of the service. When set to &quot;invisible&quot; processes owned by other users are hidden from /proc/. If &quot;ptraceable&quot; all processes that cannot be <code>ptrace()</code>&#8216;ed by a process are hidden to it. If &quot;default&quot; no restrictions on /proc/ access or visibility are made. For further details see m[blue]<code>The /proc Filesystem</code>m[]<font SIZE="-2">[2]</font>. It is generally recommended to run most system services with this option set to &quot;invisible&quot;. This option is implemented via file system namespacing, and thus cannot be used with services that shall be able to install mount points in the host file system hierarchy. Note that the root user is unaffected by this option, so to be effective it has to be used together with <i>User=</i> or <i>DynamicUser=yes</i>, and also without the &quot;CAP_SYS_PTRACE&quot; capability, which also allows a process to bypass this feature. It cannot be used for services that need to access metainformation about other users&#8217; processes. This option implies <i>MountAPIVFS=</i>. </p>
<p> If the kernel doesn&#8217;t support per-mount point <code>hidepid=</code> mount options this setting remains without effect, and the unit&#8217;s processes will be able to access and see other process as if the option was not used. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>ProcSubset=</i></p>
<dl>
<dd>Takes one of &quot;all&quot; (the default) and &quot;pid&quot;. If &quot;pid&quot;, all files and directories not directly associated with process management and introspection are made invisible in the /proc/ file system configured for the unit&#8217;s processes. This controls the &quot;subset=&quot; mount option of the &quot;procfs&quot; instance for the unit. For further details see m[blue]<code>The /proc Filesystem</code>m[]<font SIZE="-2">[2]</font>. Note that Linux exposes various kernel APIs via /proc/, which are made unavailable with this setting. Since these APIs are used frequently this option is useful only in a few, specific cases, and is not suitable for most non-trivial programs. </p>
<p> Much like <i>ProtectProc=</i> above, this is implemented via file system mount namespacing, and hence the same restrictions apply: it is only available to system services, it disables mount propagation to the host mount table, and it implies <i>MountAPIVFS=</i>. Also, like <i>ProtectProc=</i> this setting is gracefully disabled if the used kernel does not support the &quot;subset=&quot; mount option of &quot;procfs&quot;.</dl>
<p> <i>BindPaths=</i>, <i>BindReadOnlyPaths=</i></p>
<dl>
<dd>Configures unit-specific bind mounts. A bind mount makes a particular file or directory available at an additional place in the unit&#8217;s view of the file system. Any bind mounts created with this option are specific to the unit, and are not visible in the host&#8217;s mount table. This option expects a whitespace separated list of bind mount definitions. Each definition consists of a colon-separated triple of source path, destination path and option string, where the latter two are optional. If only a source path is specified the source and destination is taken to be the same. The option string may be either &quot;rbind&quot; or &quot;norbind&quot; for configuring a recursive or non-recursive bind mount. If the destination path is omitted, the option string must be omitted too. Each bind mount definition may be prefixed with &quot;-&quot;, in which case it will be ignored when its source path does not exist. </p>
<p> <i>BindPaths=</i> creates regular writable bind mounts (unless the source file system mount is already marked read-only), while <i>BindReadOnlyPaths=</i> creates read-only bind mounts. These settings may be used more than once, each usage appends to the unit&#8217;s list of bind mounts. If the empty string is assigned to either of these two options the entire list of bind mounts defined prior to this is reset. Note that in this case both read-only and regular bind mounts are reset, regardless which of the two settings is used. </p>
<p> This option is particularly useful when <i>RootDirectory=</i>/<i>RootImage=</i> is used. In this case the source path refers to a path on the host file system, while the destination path refers to a path below the root directory of the unit. </p>
<p> Note that the destination directory must exist or systemd must be able to create it. Thus, it is not possible to use those options for mount points nested underneath paths specified in <i>InaccessiblePaths=</i>, or under /home/ and other protected directories if <i>ProtectHome=yes</i> is specified. <i>TemporaryFileSystem=</i> with &quot;:ro&quot; or <i>ProtectHome=tmpfs</i> should be used instead. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>MountImages=</i></p>
<dl>
<dd>This setting is similar to <i>RootImage=</i> in that it mounts a file system hierarchy from a block device node or loopback file, but the destination directory can be specified as well as mount options. This option expects a whitespace separated list of mount definitions. Each definition consists of a colon-separated tuple of source path and destination definitions, optionally followed by another colon and a list of mount options. </p>
<p> Mount options may be defined as a single comma-separated list of options, in which case they will be implicitly applied to the root partition on the image, or a series of colon-separated tuples of partition name and mount options. Valid partition names and mount options are the same as for <i>RootImageOptions=</i> setting described above. </p>
<p> Each mount definition may be prefixed with &quot;-&quot;, in which case it will be ignored when its source path does not exist. The source argument is a path to a block device node or regular file. If source or destination contain a &quot;:&quot;, it needs to be escaped as &quot;\:&quot;. The device node or file system image file needs to follow the same rules as specified for <i>RootImage=</i>. Any mounts created with this option are specific to the unit, and are not visible in the host&#8217;s mount table. </p>
<p> These settings may be used more than once, each usage appends to the unit&#8217;s list of mount paths. If the empty string is assigned, the entire list of mount paths defined prior to this is reset. </p>
<p> Note that the destination directory must exist or systemd must be able to create it. Thus, it is not possible to use those options for mount points nested underneath paths specified in <i>InaccessiblePaths=</i>, or under /home/ and other protected directories if <i>ProtectHome=yes</i> is specified. </p>
<p> When <i>DevicePolicy=</i> is set to &quot;closed&quot; or &quot;strict&quot;, or set to &quot;auto&quot; and <i>DeviceAllow=</i> is set, then this setting adds /dev/loop-control with <code>rw</code> mode, &quot;block-loop&quot; and &quot;block-blkext&quot; with <code>rwm</code> mode to <i>DeviceAllow=</i>. See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for the details about <i>DevicePolicy=</i> or <i>DeviceAllow=</i>. Also, see <i>PrivateDevices=</i> below, as it may change the setting of <i>DevicePolicy=</i>. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>ExtensionImages=</i></p>
<dl>
<dd>This setting is similar to <i>MountImages=</i> in that it mounts a file system hierarchy from a block device node or loopback file, but instead of providing a destination path, an overlay will be set up. This option expects a whitespace separated list of mount definitions. Each definition consists of a source path, optionally followed by a colon and a list of mount options. </p>
<p> A read-only OverlayFS will be set up on top of /usr/ and /opt/ hierarchies. The order in which the images are listed will determine the order in which the overlay is laid down: images specified first to last will result in overlayfs layers bottom to top. </p>
<p> Mount options may be defined as a single comma-separated list of options, in which case they will be implicitly applied to the root partition on the image, or a series of colon-separated tuples of partition name and mount options. Valid partition names and mount options are the same as for <i>RootImageOptions=</i> setting described above. </p>
<p> Each mount definition may be prefixed with &quot;-&quot;, in which case it will be ignored when its source path does not exist. The source argument is a path to a block device node or regular file. If the source path contains a &quot;:&quot;, it needs to be escaped as &quot;\:&quot;. The device node or file system image file needs to follow the same rules as specified for <i>RootImage=</i>. Any mounts created with this option are specific to the unit, and are not visible in the host&#8217;s mount table. </p>
<p> These settings may be used more than once, each usage appends to the unit&#8217;s list of image paths. If the empty string is assigned, the entire list of mount paths defined prior to this is reset. </p>
<p> When <i>DevicePolicy=</i> is set to &quot;closed&quot; or &quot;strict&quot;, or set to &quot;auto&quot; and <i>DeviceAllow=</i> is set, then this setting adds /dev/loop-control with <code>rw</code> mode, &quot;block-loop&quot; and &quot;block-blkext&quot; with <code>rwm</code> mode to <i>DeviceAllow=</i>. See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for the details about <i>DevicePolicy=</i> or <i>DeviceAllow=</i>. Also, see <i>PrivateDevices=</i> below, as it may change the setting of <i>DevicePolicy=</i>. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<h2>User/Group Identity</h2>
<p>These options are only available for system services and are not supported for services running in per-user instances of the service manager. </p>
<p> <i>User=</i>, <i>Group=</i></p>
<dl>
<dd>Set the UNIX user or group that the processes are executed as, respectively. Takes a single user or group name, or a numeric ID as argument. For system services (services run by the system service manager, i.e. managed by PID 1) and for user services of the root user (services managed by root&#8217;s instance of <code>systemd &#8211;user</code>), the default is &quot;root&quot;, but <i>User=</i> may be used to specify a different user. For user services of any other user, switching user identity is not permitted, hence the only valid setting is the same user the user&#8217;s service manager is running as. If no group is set, the default group of the user is used. This setting does not affect commands whose command line is prefixed with &quot;+&quot;. </p>
<p> Note that this enforces only weak restrictions on the user/group name syntax, but will generate warnings in many cases where user/group names do not adhere to the following rules: the specified name should consist only of the characters a-z, A-Z, 0-9, &quot;_&quot; and &quot;-&quot;, except for the first character which must be one of a-z, A-Z and &quot;_&quot; (i.e. digits and &quot;-&quot; are not permitted as first character). The user/group name must have at least one character, and at most 31. These restrictions are made in order to avoid ambiguities and to ensure user/group names and unit files remain portable among Linux systems. For further details on the names accepted and the names warned about see m[blue]<code>User/Group Name Syntax</code>m[]<font SIZE="-2">[3]</font>. </p>
<p> When used in conjunction with <i>DynamicUser=</i> the user/group name specified is dynamically allocated at the time the service is started, and released at the time the service is stopped &#8212; unless it is already allocated statically (see below). If <i>DynamicUser=</i> is not used the specified user and group must have been created statically in the user database no later than the moment the service is started, for example using the <code><a href="/docs/linux/man/5-sysusers-d/">sysusers.d</a></code>(5) facility, which is applied at boot or package install time. If the user does not exist by then program invocation will fail. </p>
<p> If the <i>User=</i> setting is used the supplementary group list is initialized from the specified user&#8217;s default group list, as defined in the system&#8217;s user and group database. Additional groups may be configured through the <i>SupplementaryGroups=</i> setting (see below).</dl>
<p> <i>DynamicUser=</i></p>
<dl>
<dd>Takes a boolean parameter. If set, a UNIX user and group pair is allocated dynamically when the unit is started, and released as soon as it is stopped. The user and group will not be added to /etc/passwd or /etc/group, but are managed transiently during runtime. The <code><a href="/docs/linux/man/8-nss-systemd/">nss-systemd</a></code>(8) glibc NSS module provides integration of these dynamic users/groups into the system&#8217;s user and group databases. The user and group name to use may be configured via <i>User=</i> and <i>Group=</i> (see above). If these options are not used and dynamic user/group allocation is enabled for a unit, the name of the dynamic user/group is implicitly derived from the unit name. If the unit name without the type suffix qualifies as valid user name it is used directly, otherwise a name incorporating a hash of it is used. If a statically allocated user or group of the configured name already exists, it is used and no dynamic user/group is allocated. Note that if <i>User=</i> is specified and the static group with the name exists, then it is required that the static user with the name already exists. Similarly, if <i>Group=</i> is specified and the static user with the name exists, then it is required that the static group with the name already exists. Dynamic users/groups are allocated from the UID/GID range 61184&#8230;65519. It is recommended to avoid this range for regular system or login users. At any point in time each UID/GID from this range is only assigned to zero or one dynamically allocated users/groups in use. However, UID/GIDs are recycled after a unit is terminated. Care should be taken that any processes running as part of a unit for which dynamic users/groups are enabled do not leave files or directories owned by these users/groups around, as a different unit might get the same UID/GID assigned later on, and thus gain access to these files or directories. If <i>DynamicUser=</i> is enabled, <i>RemoveIPC=</i> and <i>PrivateTmp=</i> are implied (and cannot be turned off). This ensures that the lifetime of IPC objects and temporary files created by the executed processes is bound to the runtime of the service, and hence the lifetime of the dynamic user/group. Since /tmp/ and /var/tmp/ are usually the only world-writable directories on a system this ensures that a unit making use of dynamic user/group allocation cannot leave files around after unit termination. Furthermore <i>NoNewPrivileges=</i> and <i>RestrictSUIDSGID=</i> are implicitly enabled (and cannot be disabled), to ensure that processes invoked cannot take benefit or create SUID/SGID files or directories. Moreover <i>ProtectSystem=strict</i> and <i>ProtectHome=read-only</i> are implied, thus prohibiting the service to write to arbitrary file system locations. In order to allow the service to write to certain directories, they have to be allow-listed using <i>ReadWritePaths=</i>, but care must be taken so that UID/GID recycling doesn&#8217;t create security issues involving files created by the service. Use <i>RuntimeDirectory=</i> (see below) in order to assign a writable runtime directory to a service, owned by the dynamic user/group and removed automatically when the unit is terminated. Use <i>StateDirectory=</i>, <i>CacheDirectory=</i> and <i>LogsDirectory=</i> in order to assign a set of writable directories for specific purposes to the service in a way that they are protected from vulnerabilities due to UID reuse (see below). If this option is enabled, care should be taken that the unit&#8217;s processes do not get access to directories outside of these explicitly configured and managed ones. Specifically, do not use <i>BindPaths=</i> and be careful with <code>AF_UNIX</code> file descriptor passing for directory file descriptors, as this would permit processes to create files or directories owned by the dynamic user/group that are not subject to the lifecycle and access guarantees of the service. Defaults to off.</dl>
<p> <i>SupplementaryGroups=</i></p>
<dl>
<dd>Sets the supplementary Unix groups the processes are executed as. This takes a space-separated list of group names or IDs. This option may be specified more than once, in which case all listed groups are set as supplementary groups. When the empty string is assigned, the list of supplementary groups is reset, and all assignments prior to this one will have no effect. In any way, this option does not override, but extends the list of supplementary groups configured in the system group database for the user. This does not affect commands prefixed with &quot;+&quot;.</dl>
<p> <i>PAMName=</i></p>
<dl>
<dd>Sets the PAM service name to set up a session as. If set, the executed process will be registered as a PAM session under the specified service name. This is only useful in conjunction with the <i>User=</i> setting, and is otherwise ignored. If not set, no PAM session will be opened for the executed processes. See <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) for details. </p>
<p> Note that for each unit making use of this option a PAM session handler process will be maintained as part of the unit and stays around as long as the unit is active, to ensure that appropriate actions can be taken when the unit and hence the PAM session terminates. This process is named &quot;(sd-pam)&quot; and is an immediate child process of the unit&#8217;s main process. </p>
<p> Note that when this option is used for a unit it is very likely (depending on PAM configuration) that the main unit process will be migrated to its own session scope unit when it is activated. This process will hence be associated with two units: the unit it was originally started from (and for which <i>PAMName=</i> was configured), and the session scope unit. Any child processes of that process will however be associated with the session scope unit only. This has implications when used in combination with <i>NotifyAccess=</i><code>all</code>, as these child processes will not be able to affect changes in the original unit through notification messages. These messages will be considered belonging to the session scope unit and not the original unit. It is hence not recommended to use <i>PAMName=</i> in combination with <i>NotifyAccess=</i><code>all</code>.</dl>
<h2>Capabilities</h2>
<p>These options are only available for system services and are not supported for services running in per-user instances of the service manager. </p>
<p> <i>CapabilityBoundingSet=</i></p>
<dl>
<dd>Controls which capabilities to include in the capability bounding set for the executed process. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for details. Takes a whitespace-separated list of capability names, e.g. <code>CAP_SYS_ADMIN</code>, <code>CAP_DAC_OVERRIDE</code>, <code>CAP_SYS_PTRACE</code>. Capabilities listed will be included in the bounding set, all others are removed. If the list of capabilities is prefixed with &quot;~&quot;, all but the listed capabilities will be included, the effect of the assignment inverted. Note that this option also affects the respective capabilities in the effective, permitted and inheritable capability sets. If this option is not used, the capability bounding set is not modified on process execution, hence no limits on the capabilities of the process are enforced. This option may appear more than once, in which case the bounding sets are merged by <code>OR</code>, or by <code>AND</code> if the lines are prefixed with &quot;~&quot; (see below). If the empty string is assigned to this option, the bounding set is reset to the empty capability set, and all prior settings have no effect. If set to &quot;~&quot; (without any further argument), the bounding set is reset to the full set of available capabilities, also undoing any previous settings. This does not affect commands prefixed with &quot;+&quot;. </p>
<p> Use <code><a href="/docs/linux/man/1-systemd-analyze/">systemd-analyze</a></code>(1)&#8217;s <code>capability</code> command to retrieve a list of capabilities defined on the local system. </p>
<p> Example: if a unit has the following, </p>
<dl>
<dd>
<pre>CapabilityBoundingSet=CAP_A CAP_B
CapabilityBoundingSet=CAP_B CAP_C</pre>
</dl>
<p> then <code>CAP_A</code>, <code>CAP_B</code>, and <code>CAP_C</code> are set. If the second line is prefixed with &quot;~&quot;, e.g., </p>
<dl>
<dd>
<pre>CapabilityBoundingSet=CAP_A CAP_B
CapabilityBoundingSet=~CAP_B CAP_C</pre>
</dl>
<p> then, only <code>CAP_A</code> is set.</dl>
<p> <i>AmbientCapabilities=</i></p>
<dl>
<dd>Controls which capabilities to include in the ambient capability set for the executed process. Takes a whitespace-separated list of capability names, e.g. <code>CAP_SYS_ADMIN</code>, <code>CAP_DAC_OVERRIDE</code>, <code>CAP_SYS_PTRACE</code>. This option may appear more than once in which case the ambient capability sets are merged (see the above examples in <i>CapabilityBoundingSet=</i>). If the list of capabilities is prefixed with &quot;~&quot;, all but the listed capabilities will be included, the effect of the assignment inverted. If the empty string is assigned to this option, the ambient capability set is reset to the empty capability set, and all prior settings have no effect. If set to &quot;~&quot; (without any further argument), the ambient capability set is reset to the full set of available capabilities, also undoing any previous settings. Note that adding capabilities to ambient capability set adds them to the process&#8217;s inherited capability set. </p>
<p> Ambient capability sets are useful if you want to execute a process as a non-privileged user but still want to give it some capabilities. Note that in this case option <code>keep-caps</code> is automatically added to <i>SecureBits=</i> to retain the capabilities over the user change. <i>AmbientCapabilities=</i> does not affect commands prefixed with &quot;+&quot;.</dl>
<h2>Security</h2>
<p><i>NoNewPrivileges=</i></p>
<dl>
<dd>Takes a boolean argument. If true, ensures that the service process and all its children can never gain new privileges through <code>execve()</code> (e.g. via setuid or setgid bits, or filesystem capabilities). This is the simplest and most effective way to ensure that a process and its children can never elevate privileges again. Defaults to false, but certain settings override this and ignore the value of this setting. This is the case when <i>DynamicUser=</i>, <i>LockPersonality=</i>, <i>MemoryDenyWriteExecute=</i>, <i>PrivateDevices=</i>, <i>ProtectClock=</i>, <i>ProtectHostname=</i>, <i>ProtectKernelLogs=</i>, <i>ProtectKernelModules=</i>, <i>ProtectKernelTunables=</i>, <i>RestrictAddressFamilies=</i>, <i>RestrictNamespaces=</i>, <i>RestrictRealtime=</i>, <i>RestrictSUIDSGID=</i>, <i>SystemCallArchitectures=</i>, <i>SystemCallFilter=</i>, or <i>SystemCallLog=</i> are specified. Note that even if this setting is overridden by them, <code>systemctl show</code> shows the original value of this setting. In case the service will be run in a new mount namespace anyway and SELinux is disabled, all file systems are mounted with <code>MS_NOSUID</code> flag. Also see m[blue]<code>No New Privileges Flag</code>m[]<font SIZE="-2">[4]</font>.</dl>
<p> <i>SecureBits=</i></p>
<dl>
<dd>Controls the secure bits set for the executed process. Takes a space-separated combination of options from the following list: <code>keep-caps</code>, <code>keep-caps-locked</code>, <code>no-setuid-fixup</code>, <code>no-setuid-fixup-locked</code>, <code>noroot</code>, and <code>noroot-locked</code>. This option may appear more than once, in which case the secure bits are ORed. If the empty string is assigned to this option, the bits are reset to 0. This does not affect commands prefixed with &quot;+&quot;. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for details.</dl>
<h2>Mandatory Access Control</h2>
<p>These options are only available for system services and are not supported for services running in per-user instances of the service manager. </p>
<p> <i>SELinuxContext=</i></p>
<dl>
<dd>Set the SELinux security context of the executed process. If set, this will override the automated domain transition. However, the policy still needs to authorize the transition. This directive is ignored if SELinux is disabled. If prefixed by &quot;-&quot;, all errors will be ignored. This does not affect commands prefixed with &quot;+&quot;. See <code><a href="/docs/linux/man/3-setexeccon/">setexeccon</a></code>(3) for details.</dl>
<p> <i>AppArmorProfile=</i></p>
<dl>
<dd>Takes a profile name as argument. The process executed by the unit will switch to this profile when started. Profiles must already be loaded in the kernel, or the unit will fail. If prefixed by &quot;-&quot;, all errors will be ignored. This setting has no effect if AppArmor is not enabled. This setting does not affect commands prefixed with &quot;+&quot;.</dl>
<p> <i>SmackProcessLabel=</i></p>
<dl>
<dd>Takes a <code>SMACK64</code> security label as argument. The process executed by the unit will be started under this label and SMACK will decide whether the process is allowed to run or not, based on it. The process will continue to run under the label specified here unless the executable has its own <code>SMACK64EXEC</code> label, in which case the process will transition to run under that label. When not specified, the label that systemd is running under is used. This directive is ignored if SMACK is disabled. </p>
<p> The value may be prefixed by &quot;-&quot;, in which case all errors will be ignored. An empty value may be specified to unset previous assignments. This does not affect commands prefixed with &quot;+&quot;.</dl>
<h2>Process Properties</h2>
<p><i>LimitCPU=</i>, <i>LimitFSIZE=</i>, <i>LimitDATA=</i>, <i>LimitSTACK=</i>, <i>LimitCORE=</i>, <i>LimitRSS=</i>, <i>LimitNOFILE=</i>, <i>LimitAS=</i>, <i>LimitNPROC=</i>, <i>LimitMEMLOCK=</i>, <i>LimitLOCKS=</i>, <i>LimitSIGPENDING=</i>, <i>LimitMSGQUEUE=</i>, <i>LimitNICE=</i>, <i>LimitRTPRIO=</i>, <i>LimitRTTIME=</i></p>
<dl>
<dd>Set soft and hard limits on various resources for executed processes. See <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2) for details on the resource limit concept. Resource limits may be specified in two formats: either as single value to set a specific soft and hard limit to the same value, or as colon-separated pair <code>soft:hard</code> to set both limits individually (e.g. &quot;LimitAS=4G:16G&quot;). Use the string <code>infinity</code> to configure no limit on a specific resource. The multiplicative suffixes K, M, G, T, P and E (to the base 1024) may be used for resource limits measured in bytes (e.g. &quot;LimitAS=16G&quot;). For the limits referring to time values, the usual time units ms, s, min, h and so on may be used (see <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7) for details). Note that if no time unit is specified for <i>LimitCPU=</i> the default unit of seconds is implied, while for <i>LimitRTTIME=</i> the default unit of microseconds is implied. Also, note that the effective granularity of the limits might influence their enforcement. For example, time limits specified for <i>LimitCPU=</i> will be rounded up implicitly to multiples of 1s. For <i>LimitNICE=</i> the value may be specified in two syntaxes: if prefixed with &quot;+&quot; or &quot;-&quot;, the value is understood as regular Linux nice value in the range -20&#8230;19. If not prefixed like this the value is understood as raw resource limit parameter in the range 0&#8230;40 (with 0 being equivalent to 1). </p>
<p> Note that most process resource limits configured with these options are per-process, and processes may fork in order to acquire a new set of resources that are accounted independently of the original process, and may thus escape limits set. Also note that <i>LimitRSS=</i> is not implemented on Linux, and setting it has no effect. Often it is advisable to prefer the resource controls listed in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) over these per-process limits, as they apply to services as a whole, may be altered dynamically at runtime, and are generally more expressive. For example, <i>MemoryMax=</i> is a more powerful (and working) replacement for <i>LimitRSS=</i>. </p>
<p> Resource limits not configured explicitly for a unit default to the value configured in the various <i>DefaultLimitCPU=</i>, <i>DefaultLimitFSIZE=</i>, &#8230; options available in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), and &#8211; if not configured there &#8211; the kernel or per-user defaults, as defined by the OS (the latter only for user services, see below). </p>
<p> For system units these resource limits may be chosen freely. When these settings are configured in a user service (i.e. a service run by the per-user instance of the service manager) they cannot be used to raise the limits above those set for the user manager itself when it was first invoked, as the user&#8217;s service manager generally lacks the privileges to do so. In user context these configuration options are hence only useful to lower the limits passed in or to raise the soft limit to the maximum of the hard limit as configured for the user. To raise the user&#8217;s limits further, the available configuration mechanisms differ between operating systems, but typically require privileges. In most cases it is possible to configure higher per-user resource limits via PAM or by setting limits on the system service encapsulating the user&#8217;s service manager, i.e. the user&#8217;s instance of user [at] .service. After making such changes, make sure to restart the user&#8217;s service manager. </p>
<p> <code>Table 1. Resource limit directives, their equivalent ulimit shell commands and the unit used</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Directive </code></td>
<td><code> <code>ulimit</code> equivalent </code></td>
<td><code> Unit </code>
</td>
</tr>
<tr VALIGN=top>
<td> LimitCPU= </td>
<td> ulimit -t </td>
<td> Seconds
</td>
</tr>
<tr VALIGN=top>
<td> LimitFSIZE= </td>
<td> ulimit -f </td>
<td> Bytes
</td>
</tr>
<tr VALIGN=top>
<td> LimitDATA= </td>
<td> ulimit -d </td>
<td> Bytes
</td>
</tr>
<tr VALIGN=top>
<td> LimitSTACK= </td>
<td> ulimit -s </td>
<td> Bytes
</td>
</tr>
<tr VALIGN=top>
<td> LimitCORE= </td>
<td> ulimit -c </td>
<td> Bytes
</td>
</tr>
<tr VALIGN=top>
<td> LimitRSS= </td>
<td> ulimit -m </td>
<td> Bytes
</td>
</tr>
<tr VALIGN=top>
<td> LimitNOFILE= </td>
<td> ulimit -n </td>
<td> Number of File Descriptors
</td>
</tr>
<tr VALIGN=top>
<td> LimitAS= </td>
<td> ulimit -v </td>
<td> Bytes
</td>
</tr>
<tr VALIGN=top>
<td> LimitNPROC= </td>
<td> ulimit -u </td>
<td> Number of Processes
</td>
</tr>
<tr VALIGN=top>
<td> LimitMEMLOCK= </td>
<td> ulimit -l </td>
<td> Bytes
</td>
</tr>
<tr VALIGN=top>
<td> LimitLOCKS= </td>
<td> ulimit -x </td>
<td> Number of Locks
</td>
</tr>
<tr VALIGN=top>
<td> LimitSIGPENDING= </td>
<td> ulimit -i </td>
<td> Number of Queued Signals
</td>
</tr>
<tr VALIGN=top>
<td> LimitMSGQUEUE= </td>
<td> ulimit -q </td>
<td> Bytes
</td>
</tr>
<tr VALIGN=top>
<td> LimitNICE= </td>
<td> ulimit -e </td>
<td> Nice Level
</td>
</tr>
<tr VALIGN=top>
<td> LimitRTPRIO= </td>
<td> ulimit -r </td>
<td> Realtime Priority
</td>
</tr>
<tr VALIGN=top>
<td> LimitRTTIME= </td>
<td> No equivalent </td>
<td> Microseconds
</td>
</tr>
</table>
</dl>
<p> <i>UMask=</i></p>
<dl>
<dd>Controls the file mode creation mask. Takes an access mode in octal notation. See <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) for details. Defaults to 0022 for system units. For user units the default value is inherited from the per-user service manager (whose default is in turn inherited from the system service manager, and thus typically also is 0022 &#8212; unless overridden by a PAM module). In order to change the per-user mask for all user services, consider setting the <i>UMask=</i> setting of the user&#8217;s user [at] .service system service instance. The per-user umask may also be set via the <i>umask</i> field of a user&#8217;s m[blue]<code>JSON User Record</code>m[]<font SIZE="-2">[5]</font> (for users managed by <code><a href="/docs/linux/man/8-systemd-homed-service/">systemd-homed.service</a></code>(8) this field may be controlled via <code>homectl &#8211;umask=</code>). It may also be set via a PAM module, such as <code><a href="/docs/linux/man/8-pam_umask/">pam_umask</a></code>(8).</dl>
<p> <i>CoredumpFilter=</i></p>
<dl>
<dd>Controls which types of memory mappings will be saved if the process dumps core (using the /proc/<i>pid</i>/coredump_filter file). Takes a whitespace-separated combination of mapping type names or numbers (with the default base 16). Mapping type names are <code>private-anonymous</code>, <code>shared-anonymous</code>, <code>private-file-backed</code>, <code>shared-file-backed</code>, <code>elf-headers</code>, <code>private-huge</code>, <code>shared-huge</code>, <code>private-dax</code>, <code>shared-dax</code>, and the special values <code>all</code> (all types) and <code>default</code> (the kernel default of &quot;<code>private-anonymous</code> <code>shared-anonymous</code> <code>elf-headers</code> <code>private-huge</code>&quot;). See <code><a href="/docs/linux/man/5-core/">core</a></code>(5) for the meaning of the mapping types. When specified multiple times, all specified masks are ORed. When not set, or if the empty value is assigned, the inherited value is not changed. </p>
<p> <code>Example 2. Add DAX pages to the dump filter</code> </p>
<dl>
<dd>
<pre>CoredumpFilter=default private-dax shared-dax</pre>
</dl>
</dl>
<p> <i>KeyringMode=</i></p>
<dl>
<dd>Controls how the kernel session keyring is set up for the service (see <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7) for details on the session keyring). Takes one of <code>inherit</code>, <code>private</code>, <code>shared</code>. If set to <code>inherit</code> no special keyring setup is done, and the kernel&#8217;s default behaviour is applied. If <code>private</code> is used a new session keyring is allocated when a service process is invoked, and it is not linked up with any user keyring. This is the recommended setting for system services, as this ensures that multiple services running under the same system user ID (in particular the root user) do not share their key material among each other. If <code>shared</code> is used a new session keyring is allocated as for <code>private</code>, but the user keyring of the user configured with <i>User=</i> is linked into it, so that keys assigned to the user may be requested by the unit&#8217;s processes. In this modes multiple units running processes under the same user ID may share key material. Unless <code>inherit</code> is selected the unique invocation ID for the unit (see below) is added as a protected key by the name &quot;invocation_id&quot; to the newly created session keyring. Defaults to <code>private</code> for services of the system service manager and to <code>inherit</code> for non-service units and for services of the user service manager.</dl>
<p> <i>OOMScoreAdjust=</i></p>
<dl>
<dd>Sets the adjustment value for the Linux kernel&#8217;s Out-Of-Memory (OOM) killer score for executed processes. Takes an integer between -1000 (to disable OOM killing of processes of this unit) and 1000 (to make killing of processes of this unit under memory pressure very likely). See m[blue]<code>proc.txt</code>m[]<font SIZE="-2">[6]</font> for details. If not specified defaults to the OOM score adjustment level of the service manager itself, which is normally at 0. </p>
<p> Use the <i>OOMPolicy=</i> setting of service units to configure how the service manager shall react to the kernel OOM killer terminating a process of the service. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details.</dl>
<p> <i>TimerSlackNSec=</i></p>
<dl>
<dd>Sets the timer slack in nanoseconds for the executed processes. The timer slack controls the accuracy of wake-ups triggered by timers. See <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) for more information. Note that in contrast to most other time span definitions this parameter takes an integer value in nano-seconds if no unit is specified. The usual time units are understood too.</dl>
<p> <i>Personality=</i></p>
<dl>
<dd>Controls which kernel architecture <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2) shall report, when invoked by unit processes. Takes one of the architecture identifiers <code>x86</code>, <code>x86-64</code>, <code>ppc</code>, <code>ppc-le</code>, <code>ppc64</code>, <code>ppc64-le</code>, <code>s390</code> or <code>s390x</code>. Which personality architectures are supported depends on the system architecture. Usually the 64bit versions of the various system architectures support their immediate 32bit personality architecture counterpart, but no others. For example, <code>x86-64</code> systems support the <code>x86-64</code> and <code>x86</code> personalities but no others. The personality feature is useful when running 32-bit services on a 64-bit host system. If not specified, the personality is left unmodified and thus reflects the personality of the host system&#8217;s kernel.</dl>
<p> <i>IgnoreSIGPIPE=</i></p>
<dl>
<dd>Takes a boolean argument. If true, causes <code>SIGPIPE</code> to be ignored in the executed process. Defaults to true because <code>SIGPIPE</code> generally is useful only in shell pipelines.</dl>
<h2>Scheduling</h2>
<p><i>Nice=</i></p>
<dl>
<dd>Sets the default nice level (scheduling priority) for executed processes. Takes an integer between -20 (highest priority) and 19 (lowest priority). In case of resource contention, smaller values mean more resources will be made available to the unit&#8217;s processes, larger values mean less resources will be made available. See <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2) for details.</dl>
<p> <i>CPUSchedulingPolicy=</i></p>
<dl>
<dd>Sets the CPU scheduling policy for executed processes. Takes one of <code>other</code>, <code>batch</code>, <code>idle</code>, <code>fifo</code> or <code>rr</code>. See <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2) for details.</dl>
<p> <i>CPUSchedulingPriority=</i></p>
<dl>
<dd>Sets the CPU scheduling priority for executed processes. The available priority range depends on the selected CPU scheduling policy (see above). For real-time scheduling policies an integer between 1 (lowest priority) and 99 (highest priority) can be used. In case of CPU resource contention, smaller values mean less CPU time is made available to the service, larger values mean more. See <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2) for details.</dl>
<p> <i>CPUSchedulingResetOnFork=</i></p>
<dl>
<dd>Takes a boolean argument. If true, elevated CPU scheduling priorities and policies will be reset when the executed processes call <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), and can hence not leak into child processes. See <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2) for details. Defaults to false.</dl>
<p> <i>CPUAffinity=</i></p>
<dl>
<dd>Controls the CPU affinity of the executed processes. Takes a list of CPU indices or ranges separated by either whitespace or commas. Alternatively, takes a special &quot;numa&quot; value in which case systemd automatically derives allowed CPU range based on the value of <i>NUMAMask=</i> option. CPU ranges are specified by the lower and upper CPU indices separated by a dash. This option may be specified more than once, in which case the specified CPU affinity masks are merged. If the empty string is assigned, the mask is reset, all assignments prior to this will have no effect. See <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2) for details.</dl>
<p> <i>NUMAPolicy=</i></p>
<dl>
<dd>Controls the NUMA memory policy of the executed processes. Takes a policy type, one of: <code>default</code>, <code>preferred</code>, <code>bind</code>, <code>interleave</code> and <code>local</code>. A list of NUMA nodes that should be associated with the policy must be specified in <i>NUMAMask=</i>. For more details on each policy please see, <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2). For overall overview of NUMA support in Linux see, <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7).</dl>
<p> <i>NUMAMask=</i></p>
<dl>
<dd>Controls the NUMA node list which will be applied alongside with selected NUMA policy. Takes a list of NUMA nodes and has the same syntax as a list of CPUs for <i>CPUAffinity=</i> option or special &quot;all&quot; value which will include all available NUMA nodes in the mask. Note that the list of NUMA nodes is not required for <code>default</code> and <code>local</code> policies and for <code>preferred</code> policy we expect a single NUMA node.</dl>
<p> <i>IOSchedulingClass=</i></p>
<dl>
<dd>Sets the I/O scheduling class for executed processes. Takes one of the strings <code>realtime</code>, <code>best-effort</code> or <code>idle</code>. The kernel&#8217;s default scheduling class is <code>best-effort</code> at a priority of 4. If the empty string is assigned to this option, all prior assignments to both <i>IOSchedulingClass=</i> and <i>IOSchedulingPriority=</i> have no effect. See <code><a href="/docs/linux/man/2-ioprio_set/">ioprio_set</a></code>(2) for details.</dl>
<p> <i>IOSchedulingPriority=</i></p>
<dl>
<dd>Sets the I/O scheduling priority for executed processes. Takes an integer between 0 (highest priority) and 7 (lowest priority). In case of I/O contention, smaller values mean more I/O bandwidth is made available to the unit&#8217;s processes, larger values mean less bandwidth. The available priorities depend on the selected I/O scheduling class (see above). If the empty string is assigned to this option, all prior assignments to both <i>IOSchedulingClass=</i> and <i>IOSchedulingPriority=</i> have no effect. For the kernel&#8217;s default scheduling class (<code>best-effort</code>) this defaults to 4. See <code><a href="/docs/linux/man/2-ioprio_set/">ioprio_set</a></code>(2) for details.</dl>
<h2>Sandboxing</h2>
<p>The following sandboxing options are an effective way to limit the exposure of the system towards the unit&#8217;s processes. It is recommended to turn on as many of these options for each unit as is possible without negatively affecting the process&#8217; ability to operate. Note that many of these sandboxing features are gracefully turned off on systems where the underlying security mechanism is not available. For example, <i>ProtectSystem=</i> has no effect if the kernel is built without file system namespacing or if the service manager runs in a container manager that makes file system namespacing unavailable to its payload. Similar, <i>RestrictRealtime=</i> has no effect on systems that lack support for SECCOMP system call filtering, or in containers where support for this is turned off. </p>
<p> Also note that some sandboxing functionality is generally not available in user services (i.e. services run by the per-user service manager). Specifically, the various settings requiring file system namespacing support (such as <i>ProtectSystem=</i>) are not available, as the underlying kernel functionality is only accessible to privileged processes. However, most namespacing settings, that will not work on their own in user services, will work when used in conjunction with <i>PrivateUsers=</i><code>true</code>. </p>
<p> <i>ProtectSystem=</i></p>
<dl>
<dd>Takes a boolean argument or the special values &quot;full&quot; or &quot;strict&quot;. If true, mounts the /usr/ and the boot loader directories (/boot and /efi) read-only for processes invoked by this unit. If set to &quot;full&quot;, the /etc/ directory is mounted read-only, too. If set to &quot;strict&quot; the entire file system hierarchy is mounted read-only, except for the API file system subtrees /dev/, /proc/ and /sys/ (protect these directories using <i>PrivateDevices=</i>, <i>ProtectKernelTunables=</i>, <i>ProtectControlGroups=</i>). This setting ensures that any modification of the vendor-supplied operating system (and optionally its configuration, and local mounts) is prohibited for the service. It is recommended to enable this setting for all long-running services, unless they are involved with system updates or need to modify the operating system in other ways. If this option is used, <i>ReadWritePaths=</i> may be used to exclude specific directories from being made read-only. This setting is implied if <i>DynamicUser=</i> is set. This setting cannot ensure protection in all cases. In general it has the same limitations as <i>ReadOnlyPaths=</i>, see below. Defaults to off.</dl>
<p> <i>ProtectHome=</i></p>
<dl>
<dd>Takes a boolean argument or the special values &quot;read-only&quot; or &quot;tmpfs&quot;. If true, the directories /home/, /root, and /run/user are made inaccessible and empty for processes invoked by this unit. If set to &quot;read-only&quot;, the three directories are made read-only instead. If set to &quot;tmpfs&quot;, temporary file systems are mounted on the three directories in read-only mode. The value &quot;tmpfs&quot; is useful to hide home directories not relevant to the processes invoked by the unit, while still allowing necessary directories to be made visible when listed in <i>BindPaths=</i> or <i>BindReadOnlyPaths=</i>. </p>
<p> Setting this to &quot;yes&quot; is mostly equivalent to set the three directories in <i>InaccessiblePaths=</i>. Similarly, &quot;read-only&quot; is mostly equivalent to <i>ReadOnlyPaths=</i>, and &quot;tmpfs&quot; is mostly equivalent to <i>TemporaryFileSystem=</i> with &quot;:ro&quot;. </p>
<p> It is recommended to enable this setting for all long-running services (in particular network-facing ones), to ensure they cannot get access to private user data, unless the services actually require access to the user&#8217;s private data. This setting is implied if <i>DynamicUser=</i> is set. This setting cannot ensure protection in all cases. In general it has the same limitations as <i>ReadOnlyPaths=</i>, see below. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>RuntimeDirectory=</i>, <i>StateDirectory=</i>, <i>CacheDirectory=</i>, <i>LogsDirectory=</i>, <i>ConfigurationDirectory=</i></p>
<dl>
<dd>These options take a whitespace-separated list of directory names. The specified directory names must be relative, and may not include &quot;..&quot;. If set, when the unit is started, one or more directories by the specified names will be created (including their parents) below the locations defined in the following table. Also, the corresponding environment variable will be defined with the full paths of the directories. If multiple directories are set, then in the environment variable the paths are concatenated with colon (&quot;:&quot;). </p>
<p> <code>Table 2. Automatic directory creation and environment variables</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Directory </code></td>
<td><code> Below path for system units </code></td>
<td><code> Below path for user units </code></td>
<td><code> Environment variable set </code>
</td>
</tr>
<tr VALIGN=top>
<td> <i>RuntimeDirectory=</i> </td>
<td> /run/ </td>
<td> <i>$XDG_RUNTIME_DIR</i> </td>
<td> <i>$RUNTIME_DIRECTORY</i>
</td>
</tr>
<tr VALIGN=top>
<td> <i>StateDirectory=</i> </td>
<td> /var/lib/ </td>
<td> <i>$XDG_CONFIG_HOME</i> </td>
<td> <i>$STATE_DIRECTORY</i>
</td>
</tr>
<tr VALIGN=top>
<td> <i>CacheDirectory=</i> </td>
<td> /var/cache/ </td>
<td> <i>$XDG_CACHE_HOME</i> </td>
<td> <i>$CACHE_DIRECTORY</i>
</td>
</tr>
<tr VALIGN=top>
<td> <i>LogsDirectory=</i> </td>
<td> /var/log/ </td>
<td> <i>$XDG_CONFIG_HOME</i>/log/ </td>
<td> <i>$LOGS_DIRECTORY</i>
</td>
</tr>
<tr VALIGN=top>
<td> <i>ConfigurationDirectory=</i> </td>
<td> /etc/ </td>
<td> <i>$XDG_CONFIG_HOME</i> </td>
<td> <i>$CONFIGURATION_DIRECTORY</i>
</td>
</tr>
</table>
<p> In case of <i>RuntimeDirectory=</i> the innermost subdirectories are removed when the unit is stopped. It is possible to preserve the specified directories in this case if <i>RuntimeDirectoryPreserve=</i> is configured to <code>restart</code> or <code>yes</code> (see below). The directories specified with <i>StateDirectory=</i>, <i>CacheDirectory=</i>, <i>LogsDirectory=</i>, <i>ConfigurationDirectory=</i> are not removed when the unit is stopped. </p>
<p> Except in case of <i>ConfigurationDirectory=</i>, the innermost specified directories will be owned by the user and group specified in <i>User=</i> and <i>Group=</i>. If the specified directories already exist and their owning user or group do not match the configured ones, all files and directories below the specified directories as well as the directories themselves will have their file ownership recursively changed to match what is configured. As an optimization, if the specified directories are already owned by the right user and group, files and directories below of them are left as-is, even if they do not match what is requested. The innermost specified directories will have their access mode adjusted to the what is specified in <i>RuntimeDirectoryMode=</i>, <i>StateDirectoryMode=</i>, <i>CacheDirectoryMode=</i>, <i>LogsDirectoryMode=</i> and <i>ConfigurationDirectoryMode=</i>. </p>
<p> These options imply <i>BindPaths=</i> for the specified paths. When combined with <i>RootDirectory=</i> or <i>RootImage=</i> these paths always reside on the host and are mounted from there into the unit&#8217;s file system namespace. </p>
<p> If <i>DynamicUser=</i> is used, the logic for <i>CacheDirectory=</i>, <i>LogsDirectory=</i> and <i>StateDirectory=</i> is slightly altered: the directories are created below /var/cache/private, /var/log/private and /var/lib/private, respectively, which are host directories made inaccessible to unprivileged users, which ensures that access to these directories cannot be gained through dynamic user ID recycling. Symbolic links are created to hide this difference in behaviour. Both from perspective of the host and from inside the unit, the relevant directories hence always appear directly below /var/cache, /var/log and /var/lib. </p>
<p> Use <i>RuntimeDirectory=</i> to manage one or more runtime directories for the unit and bind their lifetime to the daemon runtime. This is particularly useful for unprivileged daemons that cannot create runtime directories in /run/ due to lack of privileges, and to make sure the runtime directory is cleaned up automatically after use. For runtime directories that require more complex or different configuration or lifetime guarantees, please consider using <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5). </p>
<p> The directories defined by these options are always created under the standard paths used by systemd (/var/, /run/, /etc/, &#8230;). If the service needs directories in a different location, a different mechanism has to be used to create them. </p>
<p> <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) provides functionality that overlaps with these options. Using these options is recommended, because the lifetime of the directories is tied directly to the lifetime of the unit, and it is not necessary to ensure that the tmpfiles.d configuration is executed before the unit is started. </p>
<p> To remove any of the directories created by these settings, use the <code>systemctl clean &#8230;</code> command on the relevant units, see <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) for details. </p>
<p> Example: if a system service unit has the following, </p>
<dl>
<dd>
<pre>RuntimeDirectory=foo/bar baz</pre>
</dl>
<p> the service manager creates /run/foo (if it does not exist), /run/foo/bar, and /run/baz. The directories /run/foo/bar and /run/baz except /run/foo are owned by the user and group specified in <i>User=</i> and <i>Group=</i>, and removed when the service is stopped. </p>
<p> Example: if a system service unit has the following, </p>
<dl>
<dd>
<pre>RuntimeDirectory=foo/bar
StateDirectory=aaa/bbb ccc</pre>
</dl>
<p> then the environment variable &quot;RUNTIME_DIRECTORY&quot; is set with &quot;/run/foo/bar&quot;, and &quot;STATE_DIRECTORY&quot; is set with &quot;/var/lib/aaa/bbb:/var/lib/ccc&quot;.</dl>
<p> <i>RuntimeDirectoryMode=</i>, <i>StateDirectoryMode=</i>, <i>CacheDirectoryMode=</i>, <i>LogsDirectoryMode=</i>, <i>ConfigurationDirectoryMode=</i></p>
<dl>
<dd>Specifies the access mode of the directories specified in <i>RuntimeDirectory=</i>, <i>StateDirectory=</i>, <i>CacheDirectory=</i>, <i>LogsDirectory=</i>, or <i>ConfigurationDirectory=</i>, respectively, as an octal number. Defaults to <code>0755</code>. See &quot;Permissions&quot; in <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7) for a discussion of the meaning of permission bits.</dl>
<p> <i>RuntimeDirectoryPreserve=</i></p>
<dl>
<dd>Takes a boolean argument or <code>restart</code>. If set to <code>no</code> (the default), the directories specified in <i>RuntimeDirectory=</i> are always removed when the service stops. If set to <code>restart</code> the directories are preserved when the service is both automatically and manually restarted. Here, the automatic restart means the operation specified in <i>Restart=</i>, and manual restart means the one triggered by <code>systemctl restart foo.service</code>. If set to <code>yes</code>, then the directories are not removed when the service is stopped. Note that since the runtime directory /run/ is a mount point of &quot;tmpfs&quot;, then for system services the directories specified in <i>RuntimeDirectory=</i> are removed when the system is rebooted.</dl>
<p> <i>TimeoutCleanSec=</i></p>
<dl>
<dd>Configures a timeout on the clean-up operation requested through <code>systemctl clean &#8230;</code>, see <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) for details. Takes the usual time values and defaults to <code>infinity</code>, i.e. by default no timeout is applied. If a timeout is configured the clean operation will be aborted forcibly when the timeout is reached, potentially leaving resources on disk.</dl>
<p> <i>ReadWritePaths=</i>, <i>ReadOnlyPaths=</i>, <i>InaccessiblePaths=</i>, <i>ExecPaths=</i>, <i>NoExecPaths=</i></p>
<dl>
<dd>Sets up a new file system namespace for executed processes. These options may be used to limit access a process has to the file system. Each setting takes a space-separated list of paths relative to the host&#8217;s root directory (i.e. the system running the service manager). Note that if paths contain symlinks, they are resolved relative to the root directory set with <i>RootDirectory=</i>/<i>RootImage=</i>. </p>
<p> Paths listed in <i>ReadWritePaths=</i> are accessible from within the namespace with the same access modes as from outside of it. Paths listed in <i>ReadOnlyPaths=</i> are accessible for reading only, writing will be refused even if the usual file access controls would permit this. Nest <i>ReadWritePaths=</i> inside of <i>ReadOnlyPaths=</i> in order to provide writable subdirectories within read-only directories. Use <i>ReadWritePaths=</i> in order to allow-list specific paths for write access if <i>ProtectSystem=strict</i> is used. </p>
<p> Paths listed in <i>InaccessiblePaths=</i> will be made inaccessible for processes inside the namespace along with everything below them in the file system hierarchy. This may be more restrictive than desired, because it is not possible to nest <i>ReadWritePaths=</i>, <i>ReadOnlyPaths=</i>, <i>BindPaths=</i>, or <i>BindReadOnlyPaths=</i> inside it. For a more flexible option, see <i>TemporaryFileSystem=</i>. </p>
<p> Content in paths listed in <i>NoExecPaths=</i> are not executable even if the usual file access controls would permit this. Nest <i>ExecPaths=</i> inside of <i>NoExecPaths=</i> in order to provide executable content within non-executable directories. </p>
<p> Non-directory paths may be specified as well. These options may be specified more than once, in which case all paths listed will have limited access from within the namespace. If the empty string is assigned to this option, the specific list is reset, and all prior assignments have no effect. </p>
<p> Paths in <i>ReadWritePaths=</i>, <i>ReadOnlyPaths=</i>, <i>InaccessiblePaths=</i>, <i>ExecPaths=</i> and <i>NoExecPaths=</i> may be prefixed with &quot;-&quot;, in which case they will be ignored when they do not exist. If prefixed with &quot;+&quot; the paths are taken relative to the root directory of the unit, as configured with <i>RootDirectory=</i>/<i>RootImage=</i>, instead of relative to the root directory of the host (see above). When combining &quot;-&quot; and &quot;+&quot; on the same path make sure to specify &quot;-&quot; first, and &quot;+&quot; second. </p>
<p> Note that these settings will disconnect propagation of mounts from the unit&#8217;s processes to the host. This means that this setting may not be used for services which shall be able to install mount points in the main mount namespace. For <i>ReadWritePaths=</i> and <i>ReadOnlyPaths=</i> propagation in the other direction is not affected, i.e. mounts created on the host generally appear in the unit processes&#8217; namespace, and mounts removed on the host also disappear there too. In particular, note that mount propagation from host to unit will result in unmodified mounts to be created in the unit&#8217;s namespace, i.e. writable mounts appearing on the host will be writable in the unit&#8217;s namespace too, even when propagated below a path marked with <i>ReadOnlyPaths=</i>! Restricting access with these options hence does not extend to submounts of a directory that are created later on. This means the lock-down offered by that setting is not complete, and does not offer full protection. </p>
<p> Note that the effect of these settings may be undone by privileged processes. In order to set up an effective sandboxed environment for a unit it is thus recommended to combine these settings with either <i>CapabilityBoundingSet=~CAP_SYS_ADMIN</i> or <i>SystemCallFilter=~@mount</i>. </p>
<p> Simple allow-list example using these directives: </p>
<dl>
<dd>
<pre>[Service]
ReadOnlyPaths=/
ReadWritePaths=/var /run
InaccessiblePaths=-/lost+found
NoExecPaths=/
ExecPaths=/usr/sbin/my_daemon /lib /lib64</pre>
</dl>
<p> These options are only available for system services and are not supported for services running in per-user instances of the service manager.</dl>
<p> <i>TemporaryFileSystem=</i></p>
<dl>
<dd>Takes a space-separated list of mount points for temporary file systems (tmpfs). If set, a new file system namespace is set up for executed processes, and a temporary file system is mounted on each mount point. This option may be specified more than once, in which case temporary file systems are mounted on all listed mount points. If the empty string is assigned to this option, the list is reset, and all prior assignments have no effect. Each mount point may optionally be suffixed with a colon (&quot;:&quot;) and mount options such as &quot;size=10%&quot; or &quot;ro&quot;. By default, each temporary file system is mounted with &quot;nodev,strictatime,mode=0755&quot;. These can be disabled by explicitly specifying the corresponding mount options, e.g., &quot;dev&quot; or &quot;nostrictatime&quot;. </p>
<p> This is useful to hide files or directories not relevant to the processes invoked by the unit, while necessary files or directories can be still accessed by combining with <i>BindPaths=</i> or <i>BindReadOnlyPaths=</i>: </p>
<p> Example: if a unit has the following, </p>
<dl>
<dd>
<pre>TemporaryFileSystem=/var:ro
BindReadOnlyPaths=/var/lib/systemd</pre>
</dl>
<p> then the invoked processes by the unit cannot see any files or directories under /var/ except for /var/lib/systemd or its contents. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>PrivateTmp=</i></p>
<dl>
<dd>Takes a boolean argument. If true, sets up a new file system namespace for the executed processes and mounts private /tmp/ and /var/tmp/ directories inside it that are not shared by processes outside of the namespace. This is useful to secure access to temporary files of the process, but makes sharing between processes via /tmp/ or /var/tmp/ impossible. If true, all temporary files created by a service in these directories will be removed after the service is stopped. Defaults to false. It is possible to run two or more units within the same private /tmp/ and /var/tmp/ namespace by using the <i>JoinsNamespaceOf=</i> directive, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. This setting is implied if <i>DynamicUser=</i> is set. For this setting the same restrictions regarding mount propagation and privileges apply as for <i>ReadOnlyPaths=</i> and related calls, see above. Enabling this setting has the side effect of adding <i>Requires=</i> and <i>After=</i> dependencies on all mount units necessary to access /tmp/ and /var/tmp/. Moreover an implicitly <i>After=</i> ordering on <code><a href="/docs/linux/man/8-systemd-tmpfiles-setup-service/">systemd-tmpfiles-setup.service</a></code>(8) is added. </p>
<p> Note that the implementation of this setting might be impossible (for example if mount namespaces are not available), and the unit should be written in a way that does not solely rely on this setting for security. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>PrivateDevices=</i></p>
<dl>
<dd>Takes a boolean argument. If true, sets up a new /dev/ mount for the executed processes and only adds API pseudo devices such as /dev/null, /dev/zero or /dev/random (as well as the pseudo TTY subsystem) to it, but no physical devices such as /dev/sda, system memory /dev/mem, system ports /dev/port and others. This is useful to securely turn off physical device access by the executed process. Defaults to false. Enabling this option will install a system call filter to block low-level I/O system calls that are grouped in the <i>@raw-io</i> set, will also remove <code>CAP_MKNOD</code> and <code>CAP_SYS_RAWIO</code> from the capability bounding set for the unit (see above), and set <i>DevicePolicy=closed</i> (see <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for details). Note that using this setting will disconnect propagation of mounts from the service to the host (propagation in the opposite direction continues to work). This means that this setting may not be used for services which shall be able to install mount points in the main mount namespace. The new /dev/ will be mounted read-only and &#8216;noexec&#8217;. The latter may break old programs which try to set up executable memory by using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) of /dev/zero instead of using <code>MAP_ANON</code>. For this setting the same restrictions regarding mount propagation and privileges apply as for <i>ReadOnlyPaths=</i> and related calls, see above. If turned on and if running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied. </p>
<p> Note that the implementation of this setting might be impossible (for example if mount namespaces are not available), and the unit should be written in a way that does not solely rely on this setting for security. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>PrivateNetwork=</i></p>
<dl>
<dd>Takes a boolean argument. If true, sets up a new network namespace for the executed processes and configures only the loopback network device &quot;lo&quot; inside it. No other network devices will be available to the executed process. This is useful to turn off network access by the executed process. Defaults to false. It is possible to run two or more units within the same private network namespace by using the <i>JoinsNamespaceOf=</i> directive, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. Note that this option will disconnect all socket families from the host, including <code>AF_NETLINK</code> and <code>AF_UNIX</code>. Effectively, for <code>AF_NETLINK</code> this means that device configuration events received from <code><a href="/docs/linux/man/8-systemd-udevd-service/">systemd-udevd.service</a></code>(8) are not delivered to the unit&#8217;s processes. And for <code>AF_UNIX</code> this has the effect that <code>AF_UNIX</code> sockets in the abstract socket namespace of the host will become unavailable to the unit&#8217;s processes (however, those located in the file system will continue to be accessible). </p>
<p> Note that the implementation of this setting might be impossible (for example if network namespaces are not available), and the unit should be written in a way that does not solely rely on this setting for security. </p>
<p> When this option is used on a socket unit any sockets bound on behalf of this unit will be bound within a private network namespace. This may be combined with <i>JoinsNamespaceOf=</i> to listen on sockets inside of network namespaces of other services. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>NetworkNamespacePath=</i></p>
<dl>
<dd>Takes an absolute file system path refererring to a Linux network namespace pseudo-file (i.e. a file like /proc/$PID/ns/net or a bind mount or symlink to one). When set the invoked processes are added to the network namespace referenced by that path. The path has to point to a valid namespace file at the moment the processes are forked off. If this option is used <i>PrivateNetwork=</i> has no effect. If this option is used together with <i>JoinsNamespaceOf=</i> then it only has an effect if this unit is started before any of the listed units that have <i>PrivateNetwork=</i> or <i>NetworkNamespacePath=</i> configured, as otherwise the network namespace of those units is reused. </p>
<p> When this option is used on a socket unit any sockets bound on behalf of this unit will be bound within the specified network namespace. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>PrivateIPC=</i></p>
<dl>
<dd>Takes a boolean argument. If true, sets up a new IPC namespace for the executed processes. Each IPC namespace has its own set of System V IPC identifiers and its own POSIX message queue file system. This is useful to avoid name clash of IPC identifiers. Defaults to false. It is possible to run two or more units within the same private IPC namespace by using the <i>JoinsNamespaceOf=</i> directive, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. </p>
<p> Note that IPC namespacing does not have an effect on <code>AF_UNIX</code> sockets, which are the most common form of IPC used on Linux. Instead, <code>AF_UNIX</code> sockets in the file system are subject to mount namespacing, and those in the abstract namespace are subject to network namespacing. IPC namespacing only has an effect on SysV IPC (which is mostly legacy) as well as POSIX message queues (for which <code>AF_UNIX</code>/<code>SOCK_SEQPACKET</code> sockets are typically a better replacement). IPC namespacing also has no effect on POSIX shared memory (which is subject to mount namespacing) either. See <code><a href="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></code>(7) for the details. </p>
<p> Note that the implementation of this setting might be impossible (for example if IPC namespaces are not available), and the unit should be written in a way that does not solely rely on this setting for security. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>IPCNamespacePath=</i></p>
<dl>
<dd>Takes an absolute file system path refererring to a Linux IPC namespace pseudo-file (i.e. a file like /proc/$PID/ns/ipc or a bind mount or symlink to one). When set the invoked processes are added to the network namespace referenced by that path. The path has to point to a valid namespace file at the moment the processes are forked off. If this option is used <i>PrivateIPC=</i> has no effect. If this option is used together with <i>JoinsNamespaceOf=</i> then it only has an effect if this unit is started before any of the listed units that have <i>PrivateIPC=</i> or <i>IPCNamespacePath=</i> configured, as otherwise the network namespace of those units is reused. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>PrivateUsers=</i></p>
<dl>
<dd>Takes a boolean argument. If true, sets up a new user namespace for the executed processes and configures a minimal user and group mapping, that maps the &quot;root&quot; user and group as well as the unit&#8217;s own user and group to themselves and everything else to the &quot;nobody&quot; user and group. This is useful to securely detach the user and group databases used by the unit from the rest of the system, and thus to create an effective sandbox environment. All files, directories, processes, IPC objects and other resources owned by users/groups not equaling &quot;root&quot; or the unit&#8217;s own will stay visible from within the unit but appear owned by the &quot;nobody&quot; user and group. If this mode is enabled, all unit processes are run without privileges in the host user namespace (regardless if the unit&#8217;s own user/group is &quot;root&quot; or not). Specifically this means that the process will have zero process capabilities on the host&#8217;s user namespace, but full capabilities within the service&#8217;s user namespace. Settings such as <i>CapabilityBoundingSet=</i> will affect only the latter, and there&#8217;s no way to acquire additional capabilities in the host&#8217;s user namespace. Defaults to off. </p>
<p> When this setting is set up by a per-user instance of the service manager, the mapping of the &quot;root&quot; user and group to itself is omitted (unless the user manager is root). Additionally, in the per-user instance manager case, the user namespace will be set up before most other namespaces. This means that combining <i>PrivateUsers=</i><code>true</code> with other namespaces will enable use of features not normally supported by the per-user instances of the service manager. </p>
<p> This setting is particularly useful in conjunction with <i>RootDirectory=</i>/<i>RootImage=</i>, as the need to synchronize the user and group databases in the root directory and on the host is reduced, as the only users and groups who need to be matched are &quot;root&quot;, &quot;nobody&quot; and the unit&#8217;s own user and group. </p>
<p> Note that the implementation of this setting might be impossible (for example if user namespaces are not available), and the unit should be written in a way that does not solely rely on this setting for security.</dl>
<p> <i>ProtectHostname=</i></p>
<dl>
<dd>Takes a boolean argument. When set, sets up a new UTS namespace for the executed processes. In addition, changing hostname or domainname is prevented. Defaults to off. </p>
<p> Note that the implementation of this setting might be impossible (for example if UTS namespaces are not available), and the unit should be written in a way that does not solely rely on this setting for security. </p>
<p> Note that when this option is enabled for a service hostname changes no longer propagate from the system into the service, it is hence not suitable for services that need to take notice of system hostname changes dynamically. </p>
<p> If this setting is on, but the unit doesn&#8217;t have the <code>CAP_SYS_ADMIN</code> capability (e.g. services for which <i>User=</i> is set), <i>NoNewPrivileges=yes</i> is implied. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>ProtectClock=</i></p>
<dl>
<dd>Takes a boolean argument. If set, writes to the hardware clock or system clock will be denied. It is recommended to turn this on for most services that do not need modify the clock. Defaults to off. Enabling this option removes <code>CAP_SYS_TIME</code> and <code>CAP_WAKE_ALARM</code> from the capability bounding set for this unit, installs a system call filter to block calls that can set the clock, and <i>DeviceAllow=char-rtc r</i> is implied. This ensures /dev/rtc0, /dev/rtc1, etc. are made read-only to the service. See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for the details about <i>DeviceAllow=</i>. If this setting is on, but the unit doesn&#8217;t have the <code>CAP_SYS_ADMIN</code> capability (e.g. services for which <i>User=</i> is set), <i>NoNewPrivileges=yes</i> is implied. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>ProtectKernelTunables=</i></p>
<dl>
<dd>Takes a boolean argument. If true, kernel variables accessible through /proc/sys/, /sys/, /proc/sysrq-trigger, /proc/latency_stats, /proc/acpi, /proc/timer_stats, /proc/fs and /proc/irq will be made read-only to all processes of the unit. Usually, tunable kernel variables should be initialized only at boot-time, for example with the <code><a href="/docs/linux/man/5-sysctl-d/">sysctl.d</a></code>(5) mechanism. Few services need to write to these at runtime; it is hence recommended to turn this on for most services. For this setting the same restrictions regarding mount propagation and privileges apply as for <i>ReadOnlyPaths=</i> and related calls, see above. Defaults to off. If this setting is on, but the unit doesn&#8217;t have the <code>CAP_SYS_ADMIN</code> capability (e.g. services for which <i>User=</i> is set), <i>NoNewPrivileges=yes</i> is implied. Note that this option does not prevent indirect changes to kernel tunables effected by IPC calls to other processes. However, <i>InaccessiblePaths=</i> may be used to make relevant IPC file system objects inaccessible. If <i>ProtectKernelTunables=</i> is set, <i>MountAPIVFS=yes</i> is implied. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>ProtectKernelModules=</i></p>
<dl>
<dd>Takes a boolean argument. If true, explicit module loading will be denied. This allows module load and unload operations to be turned off on modular kernels. It is recommended to turn this on for most services that do not need special file systems or extra kernel modules to work. Defaults to off. Enabling this option removes <code>CAP_SYS_MODULE</code> from the capability bounding set for the unit, and installs a system call filter to block module system calls, also /usr/lib/modules is made inaccessible. For this setting the same restrictions regarding mount propagation and privileges apply as for <i>ReadOnlyPaths=</i> and related calls, see above. Note that limited automatic module loading due to user configuration or kernel mapping tables might still happen as side effect of requested user operations, both privileged and unprivileged. To disable module auto-load feature please see <code><a href="/docs/linux/man/5-sysctl-d/">sysctl.d</a></code>(5) <code>kernel.modules_disabled</code> mechanism and /proc/sys/kernel/modules_disabled documentation. If this setting is on, but the unit doesn&#8217;t have the <code>CAP_SYS_ADMIN</code> capability (e.g. services for which <i>User=</i> is set), <i>NoNewPrivileges=yes</i> is implied. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>ProtectKernelLogs=</i></p>
<dl>
<dd>Takes a boolean argument. If true, access to the kernel log ring buffer will be denied. It is recommended to turn this on for most services that do not need to read from or write to the kernel log ring buffer. Enabling this option removes <code>CAP_SYSLOG</code> from the capability bounding set for this unit, and installs a system call filter to block the <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) system call (not to be confused with the libc API <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for userspace logging). The kernel exposes its log buffer to userspace via /dev/kmsg and /proc/kmsg. If enabled, these are made inaccessible to all the processes in the unit. If this setting is on, but the unit doesn&#8217;t have the <code>CAP_SYS_ADMIN</code> capability (e.g. services for which <i>User=</i> is set), <i>NoNewPrivileges=yes</i> is implied. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>ProtectControlGroups=</i></p>
<dl>
<dd>Takes a boolean argument. If true, the Linux Control Groups (<code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7)) hierarchies accessible through /sys/fs/cgroup/ will be made read-only to all processes of the unit. Except for container managers no services should require write access to the control groups hierarchies; it is hence recommended to turn this on for most services. For this setting the same restrictions regarding mount propagation and privileges apply as for <i>ReadOnlyPaths=</i> and related calls, see above. Defaults to off. If <i>ProtectControlGroups=</i> is set, <i>MountAPIVFS=yes</i> is implied. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>RestrictAddressFamilies=</i></p>
<dl>
<dd>Restricts the set of socket address families accessible to the processes of this unit. Takes &quot;none&quot;, or a space-separated list of address family names to allow-list, such as <code>AF_UNIX</code>, <code>AF_INET</code> or <code>AF_INET6</code>. When &quot;none&quot; is specified, then all address families will be denied. When prefixed with &quot;~&quot; the listed address families will be applied as deny list, otherwise as allow list. Note that this restricts access to the <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) system call only. Sockets passed into the process by other means (for example, by using socket activation with socket units, see <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5)) are unaffected. Also, sockets created with <code>socketpair()</code> (which creates connected AF_UNIX sockets only) are unaffected. Note that this option has no effect on 32-bit x86, s390, s390x, mips, mips-le, ppc, ppc-le, ppc64, ppc64-le and is ignored (but works correctly on other ABIs, including x86-64). Note that on systems supporting multiple ABIs (such as x86/x86-64) it is recommended to turn off alternative ABIs for services, so that they cannot be used to circumvent the restrictions of this option. Specifically, it is recommended to combine this option with <i>SystemCallArchitectures=native</i> or similar. If running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied. By default, no restrictions apply, all address families are accessible to processes. If assigned the empty string, any previous address family restriction changes are undone. This setting does not affect commands prefixed with &quot;+&quot;. </p>
<p> Use this option to limit exposure of processes to remote access, in particular via exotic and sensitive network protocols, such as <code>AF_PACKET</code>. Note that in most cases, the local <code>AF_UNIX</code> address family should be included in the configured allow list as it is frequently used for local communication, including for <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) logging.</dl>
<p> <i>RestrictNamespaces=</i></p>
<dl>
<dd>Restricts access to Linux namespace functionality for the processes of this unit. For details about Linux namespaces, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7). Either takes a boolean argument, or a space-separated list of namespace type identifiers. If false (the default), no restrictions on namespace creation and switching are made. If true, access to any kind of namespacing is prohibited. Otherwise, a space-separated list of namespace type identifiers must be specified, consisting of any combination of: <code>cgroup</code>, <code>ipc</code>, <code>net</code>, <code>mnt</code>, <code>pid</code>, <code>user</code> and <code>uts</code>. Any namespace type listed is made accessible to the unit&#8217;s processes, access to namespace types not listed is prohibited (allow-listing). By prepending the list with a single tilde character (&quot;~&quot;) the effect may be inverted: only the listed namespace types will be made inaccessible, all unlisted ones are permitted (deny-listing). If the empty string is assigned, the default namespace restrictions are applied, which is equivalent to false. This option may appear more than once, in which case the namespace types are merged by <code>OR</code>, or by <code>AND</code> if the lines are prefixed with &quot;~&quot; (see examples below). Internally, this setting limits access to the <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) system calls, taking the specified flags parameters into account. Note that &#8212; if this option is used &#8212; in addition to restricting creation and switching of the specified types of namespaces (or all of them, if true) access to the <code>setns()</code> system call with a zero flags parameter is prohibited. This setting is only supported on x86, x86-64, mips, mips-le, mips64, mips64-le, mips64-n32, mips64-le-n32, ppc64, ppc64-le, s390 and s390x, and enforces no restrictions on other architectures. If running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied. </p>
<p> Example: if a unit has the following, </p>
<dl>
<dd>
<pre>RestrictNamespaces=cgroup ipc
RestrictNamespaces=cgroup net</pre>
</dl>
<p> then <code>cgroup</code>, <code>ipc</code>, and <code>net</code> are set. If the second line is prefixed with &quot;~&quot;, e.g., </p>
<dl>
<dd>
<pre>RestrictNamespaces=cgroup ipc
RestrictNamespaces=~cgroup net</pre>
</dl>
<p> then, only <code>ipc</code> is set.</dl>
<p> <i>LockPersonality=</i></p>
<dl>
<dd>Takes a boolean argument. If set, locks down the <code><a href="/docs/linux/man/2-personality/">personality</a></code>(2) system call so that the kernel execution domain may not be changed from the default or the personality selected with <i>Personality=</i> directive. This may be useful to improve security, because odd personality emulations may be poorly tested and source of vulnerabilities. If running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied.</dl>
<p> <i>MemoryDenyWriteExecute=</i></p>
<dl>
<dd>Takes a boolean argument. If set, attempts to create memory mappings that are writable and executable at the same time, or to change existing memory mappings to become executable, or mapping shared memory segments as executable are prohibited. Specifically, a system call filter is added that rejects <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) system calls with both <code>PROT_EXEC</code> and <code>PROT_WRITE</code> set, <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2) or <code><a href="/docs/linux/man/2-pkey_mprotect/">pkey_mprotect</a></code>(2) system calls with <code>PROT_EXEC</code> set and <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) system calls with <code>SHM_EXEC</code> set. Note that this option is incompatible with programs and libraries that generate program code dynamically at runtime, including JIT execution engines, executable stacks, and code &quot;trampoline&quot; feature of various C compilers. This option improves service security, as it makes harder for software exploits to change running code dynamically. However, the protection can be circumvented, if the service can write to a filesystem, which is not mounted with <code>noexec</code> (such as /dev/shm), or it can use <code>memfd_create()</code>. This can be prevented by making such file systems inaccessible to the service (e.g. <i>InaccessiblePaths=/dev/shm</i>) and installing further system call filters (<i>SystemCallFilter=~memfd_create</i>). Note that this feature is fully available on x86-64, and partially on x86. Specifically, the <code>shmat()</code> protection is not available on x86. Note that on systems supporting multiple ABIs (such as x86/x86-64) it is recommended to turn off alternative ABIs for services, so that they cannot be used to circumvent the restrictions of this option. Specifically, it is recommended to combine this option with <i>SystemCallArchitectures=native</i> or similar. If running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied.</dl>
<p> <i>RestrictRealtime=</i></p>
<dl>
<dd>Takes a boolean argument. If set, any attempts to enable realtime scheduling in a process of the unit are refused. This restricts access to realtime task scheduling policies such as <code>SCHED_FIFO</code>, <code>SCHED_RR</code> or <code>SCHED_DEADLINE</code>. See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) for details about these scheduling policies. If running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied. Realtime scheduling policies may be used to monopolize CPU time for longer periods of time, and may hence be used to lock up or otherwise trigger Denial-of-Service situations on the system. It is hence recommended to restrict access to realtime scheduling to the few programs that actually require them. Defaults to off.</dl>
<p> <i>RestrictSUIDSGID=</i></p>
<dl>
<dd>Takes a boolean argument. If set, any attempts to set the set-user-ID (SUID) or set-group-ID (SGID) bits on files or directories will be denied (for details on these bits see <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7)). If running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied. As the SUID/SGID bits are mechanisms to elevate privileges, and allows users to acquire the identity of other users, it is recommended to restrict creation of SUID/SGID files to the few programs that actually require them. Note that this restricts marking of any type of file system object with these bits, including both regular files and directories (where the SGID is a different meaning than for files, see documentation). This option is implied if <i>DynamicUser=</i> is enabled. Defaults to off.</dl>
<p> <i>RemoveIPC=</i></p>
<dl>
<dd>Takes a boolean parameter. If set, all System V and POSIX IPC objects owned by the user and group the processes of this unit are run as are removed when the unit is stopped. This setting only has an effect if at least one of <i>User=</i>, <i>Group=</i> and <i>DynamicUser=</i> are used. It has no effect on IPC objects owned by the root user. Specifically, this removes System V semaphores, as well as System V and POSIX shared memory segments and message queues. If multiple units use the same user or group the IPC objects are removed when the last of these units is stopped. This setting is implied if <i>DynamicUser=</i> is set. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>PrivateMounts=</i></p>
<dl>
<dd>Takes a boolean parameter. If set, the processes of this unit will be run in their own private file system (mount) namespace with all mount propagation from the processes towards the host&#8217;s main file system namespace turned off. This means any file system mount points established or removed by the unit&#8217;s processes will be private to them and not be visible to the host. However, file system mount points established or removed on the host will be propagated to the unit&#8217;s processes. See <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7) for details on file system namespaces. Defaults to off. </p>
<p> When turned on, this executes three operations for each invoked process: a new <code>CLONE_NEWNS</code> namespace is created, after which all existing mounts are remounted to <code>MS_SLAVE</code> to disable propagation from the unit&#8217;s processes to the host (but leaving propagation in the opposite direction in effect). Finally, the mounts are remounted again to the propagation mode configured with <i>MountFlags=</i>, see below. </p>
<p> File system namespaces are set up individually for each process forked off by the service manager. Mounts established in the namespace of the process created by <i>ExecStartPre=</i> will hence be cleaned up automatically as soon as that process exits and will not be available to subsequent processes forked off for <i>ExecStart=</i> (and similar applies to the various other commands configured for units). Similarly, <i>JoinsNamespaceOf=</i> does not permit sharing kernel mount namespaces between units, it only enables sharing of the /tmp/ and /var/tmp/ directories. </p>
<p> Other file system namespace unit settings &#8212; <i>PrivateMounts=</i>, <i>PrivateTmp=</i>, <i>PrivateDevices=</i>, <i>ProtectSystem=</i>, <i>ProtectHome=</i>, <i>ReadOnlyPaths=</i>, <i>InaccessiblePaths=</i>, <i>ReadWritePaths=</i>, &#8230; &#8212; also enable file system namespacing in a fashion equivalent to this option. Hence it is primarily useful to explicitly request this behaviour if none of the other settings are used. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>MountFlags=</i></p>
<dl>
<dd>Takes a mount propagation setting: <code>shared</code>, <code>slave</code> or <code>private</code>, which controls whether file system mount points in the file system namespaces set up for this unit&#8217;s processes will receive or propagate mounts and unmounts from other file system namespaces. See <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) for details on mount propagation, and the three propagation flags in particular. </p>
<p> This setting only controls the <i>final</i> propagation setting in effect on all mount points of the file system namespace created for each process of this unit. Other file system namespacing unit settings (see the discussion in <i>PrivateMounts=</i> above) will implicitly disable mount and unmount propagation from the unit&#8217;s processes towards the host by changing the propagation setting of all mount points in the unit&#8217;s file system namespace to <code>slave</code> first. Setting this option to <code>shared</code> does not reestablish propagation in that case. </p>
<p> If not set &#8211; but file system namespaces are enabled through another file system namespace unit setting &#8211; <code>shared</code> mount propagation is used, but &#8212; as mentioned &#8212; as <code>slave</code> is applied first, propagation from the unit&#8217;s processes to the host is still turned off. </p>
<p> It is not recommended to use <code>private</code> mount propagation for units, as this means temporary mounts (such as removable media) of the host will stay mounted and thus indefinitely busy in forked off processes, as unmount propagation events won&#8217;t be received by the file system namespace of the unit. </p>
<p> Usually, it is best to leave this setting unmodified, and use higher level file system namespacing options instead, in particular <i>PrivateMounts=</i>, see above. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<h2>System Call Filtering</h2>
<p><i>SystemCallFilter=</i></p>
<dl>
<dd>Takes a space-separated list of system call names. If this setting is used, all system calls executed by the unit processes except for the listed ones will result in immediate process termination with the <code>SIGSYS</code> signal (allow-listing). (See <i>SystemCallErrorNumber=</i> below for changing the default action). If the first character of the list is &quot;~&quot;, the effect is inverted: only the listed system calls will result in immediate process termination (deny-listing). Deny-listed system calls and system call groups may optionally be suffixed with a colon (&quot;:&quot;) and &quot;errno&quot; error number (between 0 and 4095) or errno name such as <code>EPERM</code>, <code>EACCES</code> or <code>EUCLEAN</code> (see <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3) for a full list). This value will be returned when a deny-listed system call is triggered, instead of terminating the processes immediately. Special setting &quot;kill&quot; can be used to explicitly specify killing. This value takes precedence over the one given in <i>SystemCallErrorNumber=</i>, see below. If running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied. This feature makes use of the Secure Computing Mode 2 interfaces of the kernel (&#8216;seccomp filtering&#8217;) and is useful for enforcing a minimal sandboxing environment. Note that the <code>execve()</code>, <code>exit()</code>, <code>exit_group()</code>, <code>getrlimit()</code>, <code>rt_sigreturn()</code>, <code>sigreturn()</code> system calls and the system calls for querying time and sleeping are implicitly allow-listed and do not need to be listed explicitly. This option may be specified more than once, in which case the filter masks are merged. If the empty string is assigned, the filter is reset, all prior assignments will have no effect. This does not affect commands prefixed with &quot;+&quot;. </p>
<p> Note that on systems supporting multiple ABIs (such as x86/x86-64) it is recommended to turn off alternative ABIs for services, so that they cannot be used to circumvent the restrictions of this option. Specifically, it is recommended to combine this option with <i>SystemCallArchitectures=native</i> or similar. </p>
<p> Note that strict system call filters may impact execution and error handling code paths of the service invocation. Specifically, access to the <code>execve()</code> system call is required for the execution of the service binary &#8212; if it is blocked service invocation will necessarily fail. Also, if execution of the service binary fails for some reason (for example: missing service executable), the error handling logic might require access to an additional set of system calls in order to process and log this failure correctly. It might be necessary to temporarily disable system call filters in order to simplify debugging of such failures. </p>
<p> If you specify both types of this option (i.e. allow-listing and deny-listing), the first encountered will take precedence and will dictate the default action (termination or approval of a system call). Then the next occurrences of this option will add or delete the listed system calls from the set of the filtered system calls, depending of its type and the default action. (For example, if you have started with an allow list rule for <code>read()</code> and <code>write()</code>, and right after it add a deny list rule for <code>write()</code>, then <code>write()</code> will be removed from the set.) </p>
<p> As the number of possible system calls is large, predefined sets of system calls are provided. A set starts with &quot;@&quot; character, followed by name of the set. </p>
<p> <code>Table 3. Currently predefined system call sets</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Set </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> @aio </td>
<td> Asynchronous I/O (<code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2), <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2), and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @basic-io </td>
<td> System calls for basic I/O: reading, writing, seeking, file descriptor duplication and closing (<code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @chown </td>
<td> Changing file ownership (<code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-fchownat/">fchownat</a></code>(2), and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @clock </td>
<td> System calls for changing the system clock (<code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2), <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @cpu-emulation </td>
<td> System calls for CPU emulation functionality (<code><a href="/docs/linux/man/2-vm86/">vm86</a></code>(2) and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @debug </td>
<td> Debugging, performance monitoring and tracing functionality (<code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2), <code><a href="/docs/linux/man/2-perf_event_open/">perf_event_open</a></code>(2) and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @file-system </td>
<td> File system operations: opening, creating files and directories for read and write, renaming and removing them, reading file properties, or creating hard and symbolic links
</td>
</tr>
<tr VALIGN=top>
<td> @io-event </td>
<td> Event loop system calls (<code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), <code><a href="/docs/linux/man/2-eventfd/">eventfd</a></code>(2) and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @ipc </td>
<td> Pipes, SysV IPC, POSIX Message Queues and other IPC (<code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7), <code><a href="/docs/linux/man/7-svipc/">svipc</a></code>(7))
</td>
</tr>
<tr VALIGN=top>
<td> @keyring </td>
<td> Kernel keyring access (<code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @memlock </td>
<td> Locking of memory in RAM (<code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2) and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @module </td>
<td> Loading and unloading of kernel modules (<code><a href="/docs/linux/man/2-init_module/">init_module</a></code>(2), <code><a href="/docs/linux/man/2-delete_module/">delete_module</a></code>(2) and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @mount </td>
<td> Mounting and unmounting of file systems (<code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @network-io </td>
<td> Socket I/O (including local AF_UNIX): <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> @obsolete </td>
<td> Unusual, obsolete or unimplemented (<code><a href="/docs/linux/man/2-create_module/">create_module</a></code>(2), <code><a href="/docs/linux/man/2-gtty/">gtty</a></code>(2), &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td> @privileged </td>
<td> All system calls which need super-user capabilities (<code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7))
</td>
</tr>
<tr VALIGN=top>
<td> @process </td>
<td> Process control, execution, namespacing operations (<code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td> @raw-io </td>
<td> Raw I/O port access (<code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2), <code><a href="/docs/linux/man/2-iopl/">iopl</a></code>(2), <code>pciconfig_read()</code>, &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td> @reboot </td>
<td> System calls for rebooting and reboot preparation (<code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2), <code>kexec()</code>, &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td> @resources </td>
<td> System calls for changing resource limits, memory and scheduling parameters (<code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2), &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td> @setuid </td>
<td> System calls for changing user ID and group ID credentials, (<code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2), <code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2), &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td> @signal </td>
<td> System calls for manipulating and handling process signals (<code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td> @swap </td>
<td> System calls for enabling/disabling swap devices (<code><a href="/docs/linux/man/2-swapon/">swapon</a></code>(2), <code><a href="/docs/linux/man/2-swapoff/">swapoff</a></code>(2))
</td>
</tr>
<tr VALIGN=top>
<td> @sync </td>
<td> Synchronizing files and memory to disk (<code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), and related calls)
</td>
</tr>
<tr VALIGN=top>
<td> @system-service </td>
<td> A reasonable set of system calls used by common system services, excluding any special purpose calls. This is the recommended starting point for allow-listing system calls for system services, as it contains what is typically needed by system services, but excludes overly specific interfaces. For example, the following APIs are excluded: &quot;@clock&quot;, &quot;@mount&quot;, &quot;@swap&quot;, &quot;@reboot&quot;.
</td>
</tr>
<tr VALIGN=top>
<td> @timer </td>
<td> System calls for scheduling operations by time (<code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td> @known </td>
<td> All system calls defined by the kernel. This list is defined statically in systemd based on a kernel version that was available when this systemd version was released. It will become progressively more out-of-date as the kernel is updated.
</td>
</tr>
</table>
<p> Note, that as new system calls are added to the kernel, additional system calls might be added to the groups above. Contents of the sets may also change between systemd versions. In addition, the list of system calls depends on the kernel version and architecture for which systemd was compiled. Use <code>systemd-analyze syscall-filter</code> to list the actual list of system calls in each filter. </p>
<p> Generally, allow-listing system calls (rather than deny-listing) is the safer mode of operation. It is recommended to enforce system call allow lists for all long-running system services. Specifically, the following lines are a relatively safe basic choice for the majority of system services: </p>
<dl>
<dd>
<pre>[Service]
SystemCallFilter=@system-service
SystemCallErrorNumber=EPERM</pre>
</dl>
<p> Note that various kernel system calls are defined redundantly: there are multiple system calls for executing the same operation. For example, the <code>pidfd_send_signal()</code> system call may be used to execute operations similar to what can be done with the older <code>kill()</code> system call, hence blocking the latter without the former only provides weak protection. Since new system calls are added regularly to the kernel as development progresses, keeping system call deny lists comprehensive requires constant work. It is thus recommended to use allow-listing instead, which offers the benefit that new system calls are by default implicitly blocked until the allow list is updated. </p>
<p> Also note that a number of system calls are required to be accessible for the dynamic linker to work. The dynamic linker is required for running most regular programs (specifically: all dynamic ELF binaries, which is how most distributions build packaged programs). This means that blocking these system calls (which include <code>open()</code>, <code>openat()</code> or <code>mmap()</code>) will make most programs typically shipped with generic distributions unusable. </p>
<p> It is recommended to combine the file system namespacing related options with <i>SystemCallFilter=~@mount</i>, in order to prohibit the unit&#8217;s processes to undo the mappings. Specifically these are the options <i>PrivateTmp=</i>, <i>PrivateDevices=</i>, <i>ProtectSystem=</i>, <i>ProtectHome=</i>, <i>ProtectKernelTunables=</i>, <i>ProtectControlGroups=</i>, <i>ProtectKernelLogs=</i>, <i>ProtectClock=</i>, <i>ReadOnlyPaths=</i>, <i>InaccessiblePaths=</i> and <i>ReadWritePaths=</i>.</dl>
<p> <i>SystemCallErrorNumber=</i></p>
<dl>
<dd>Takes an &quot;errno&quot; error number (between 1 and 4095) or errno name such as <code>EPERM</code>, <code>EACCES</code> or <code>EUCLEAN</code>, to return when the system call filter configured with <i>SystemCallFilter=</i> is triggered, instead of terminating the process immediately. See <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3) for a full list of error codes. When this setting is not used, or when the empty string or the special setting &quot;kill&quot; is assigned, the process will be terminated immediately when the filter is triggered.</dl>
<p> <i>SystemCallArchitectures=</i></p>
<dl>
<dd>Takes a space-separated list of architecture identifiers to include in the system call filter. The known architecture identifiers are the same as for <i>ConditionArchitecture=</i> described in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), as well as <code>x32</code>, <code>mips64-n32</code>, <code>mips64-le-n32</code>, and the special identifier <code>native</code>. The special identifier <code>native</code> implicitly maps to the native architecture of the system (or more precisely: to the architecture the system manager is compiled for). If running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied. By default, this option is set to the empty list, i.e. no filtering is applied. </p>
<p> If this setting is used, processes of this unit will only be permitted to call native system calls, and system calls of the specified architectures. For the purposes of this option, the x32 architecture is treated as including x86-64 system calls. However, this setting still fulfills its purpose, as explained below, on x32. </p>
<p> System call filtering is not equally effective on all architectures. For example, on x86 filtering of network socket-related calls is not possible, due to ABI limitations &#8212; a limitation that x86-64 does not have, however. On systems supporting multiple ABIs at the same time &#8212; such as x86/x86-64 &#8212; it is hence recommended to limit the set of permitted system call architectures so that secondary ABIs may not be used to circumvent the restrictions applied to the native ABI of the system. In particular, setting <i>SystemCallArchitectures=native</i> is a good choice for disabling non-native ABIs. </p>
<p> System call architectures may also be restricted system-wide via the <i>SystemCallArchitectures=</i> option in the global configuration. See <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5) for details.</dl>
<p> <i>SystemCallLog=</i></p>
<dl>
<dd>Takes a space-separated list of system call names. If this setting is used, all system calls executed by the unit processes for the listed ones will be logged. If the first character of the list is &quot;~&quot;, the effect is inverted: all system calls except the listed system calls will be logged. If running in user mode, or in system mode, but without the <code>CAP_SYS_ADMIN</code> capability (e.g. setting <i>User=</i>), <i>NoNewPrivileges=yes</i> is implied. This feature makes use of the Secure Computing Mode 2 interfaces of the kernel (&#8216;seccomp filtering&#8217;) and is useful for auditing or setting up a minimal sandboxing environment. This option may be specified more than once, in which case the filter masks are merged. If the empty string is assigned, the filter is reset, all prior assignments will have no effect. This does not affect commands prefixed with &quot;+&quot;.</dl>
<h2>Environment</h2>
<p><i>Environment=</i></p>
<dl>
<dd>Sets environment variables for executed processes. Each line is unquoted using the rules described in &quot;Quoting&quot; section in <code><a href="/docs/linux/man/7-systemd-syntax/">systemd.syntax</a></code>(7) and becomes a list of variable assignments. If you need to assign a value containing spaces or the equals sign to a variable, put quotes around the whole assignment. Variable expansion is not performed inside the strings and the &quot;$&quot; character has no special meaning. Specifier expansion is performed, see the &quot;Specifiers&quot; section in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). </p>
<p> This option may be specified more than once, in which case all listed variables will be set. If the same variable is listed twice, the later setting will override the earlier setting. If the empty string is assigned to this option, the list of environment variables is reset, all prior assignments have no effect. </p>
<p> The names of the variables can contain ASCII letters, digits, and the underscore character. Variable names cannot be empty or start with a digit. In variable values, most characters are allowed, but non-printable characters are currently rejected. </p>
<p> Example: </p>
<dl>
<dd>
<pre>Environment=&quot;VAR1=word1 word2&quot; VAR2=word3 &quot;VAR3=$word 5 6&quot;</pre>
</dl>
<p> gives three variables &quot;VAR1&quot;, &quot;VAR2&quot;, &quot;VAR3&quot; with the values &quot;word1 word2&quot;, &quot;word3&quot;, &quot;$word 5 6&quot;. </p>
<p> See <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) for details about environment variables. </p>
<p> Note that environment variables are not suitable for passing secrets (such as passwords, key material, &#8230;) to service processes. Environment variables set for a unit are exposed to unprivileged clients via D-Bus IPC, and generally not understood as being data that requires protection. Moreover, environment variables are propagated down the process tree, including across security boundaries (such as setuid/setgid executables), and hence might leak to processes that should not have access to the secret data. Use <i>LoadCredential=</i> (see below) to pass data to unit processes securely.</dl>
<p> <i>EnvironmentFile=</i></p>
<dl>
<dd>Similar to <i>Environment=</i> but reads the environment variables from a text file. The text file should contain new-line-separated variable assignments. Empty lines, lines without an &quot;=&quot; separator, or lines starting with ; or # will be ignored, which may be used for commenting. A line ending with a backslash will be concatenated with the following one, allowing multiline variable definitions. The parser strips leading and trailing whitespace from the values of assignments, unless you use double quotes (&quot;). </p>
<p> m[blue]<code>C escapes</code>m[]<font SIZE="-2">[7]</font> are supported, but not m[blue]<code>most control characters</code>m[]<font SIZE="-2">[8]</font>. &quot;	&quot; and &quot;
&quot; can be used to insert tabs and newlines within <i>EnvironmentFile=</i>. </p>
<p> The argument passed should be an absolute filename or wildcard expression, optionally prefixed with &quot;-&quot;, which indicates that if the file does not exist, it will not be read and no error or warning message is logged. This option may be specified more than once in which case all specified files are read. If the empty string is assigned to this option, the list of file to read is reset, all prior assignments have no effect. </p>
<p> The files listed with this directive will be read shortly before the process is executed (more specifically, after all processes from a previous unit state terminated. This means you can generate these files in one unit state, and read it with this option in the next. The files are read from the file system of the service manager, before any file system changes like bind mounts take place). </p>
<p> Settings from these files override settings made with <i>Environment=</i>. If the same variable is set twice from these files, the files will be read in the order they are specified and the later setting will override the earlier setting.</dl>
<p> <i>PassEnvironment=</i></p>
<dl>
<dd>Pass environment variables set for the system service manager to executed processes. Takes a space-separated list of variable names. This option may be specified more than once, in which case all listed variables will be passed. If the empty string is assigned to this option, the list of environment variables to pass is reset, all prior assignments have no effect. Variables specified that are not set for the system manager will not be passed and will be silently ignored. Note that this option is only relevant for the system service manager, as system services by default do not automatically inherit any environment variables set for the service manager itself. However, in case of the user service manager all environment variables are passed to the executed processes anyway, hence this option is without effect for the user service manager. </p>
<p> Variables set for invoked processes due to this setting are subject to being overridden by those configured with <i>Environment=</i> or <i>EnvironmentFile=</i>. </p>
<p> m[blue]<code>C escapes</code>m[]<font SIZE="-2">[7]</font> are supported, but not m[blue]<code>most control characters</code>m[]<font SIZE="-2">[8]</font>. &quot;	&quot; and &quot;
&quot; can be used to insert tabs and newlines within <i>EnvironmentFile=</i>. </p>
<p> Example: </p>
<dl>
<dd>
<pre>PassEnvironment=VAR1 VAR2 VAR3</pre>
</dl>
<p> passes three variables &quot;VAR1&quot;, &quot;VAR2&quot;, &quot;VAR3&quot; with the values set for those variables in PID1. </p>
<p> See <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) for details about environment variables.</dl>
<p> <i>UnsetEnvironment=</i></p>
<dl>
<dd>Explicitly unset environment variable assignments that would normally be passed from the service manager to invoked processes of this unit. Takes a space-separated list of variable names or variable assignments. This option may be specified more than once, in which case all listed variables/assignments will be unset. If the empty string is assigned to this option, the list of environment variables/assignments to unset is reset. If a variable assignment is specified (that is: a variable name, followed by &quot;=&quot;, followed by its value), then any environment variable matching this precise assignment is removed. If a variable name is specified (that is a variable name without any following &quot;=&quot; or value), then any assignment matching the variable name, regardless of its value is removed. Note that the effect of <i>UnsetEnvironment=</i> is applied as final step when the environment list passed to executed processes is compiled. That means it may undo assignments from any configuration source, including assignments made through <i>Environment=</i> or <i>EnvironmentFile=</i>, inherited from the system manager&#8217;s global set of environment variables, inherited via <i>PassEnvironment=</i>, set by the service manager itself (such as <i>$NOTIFY_SOCKET</i> and such), or set by a PAM module (in case <i>PAMName=</i> is used). </p>
<p> See &quot;Environment Variables in Spawned Processes&quot; below for a description of how those settings combine to form the inherited environment. See <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) for general information about environment variables.</dl>
<h2>Logging And Standard Input/Output</h2>
<p><i>StandardInput=</i></p>
<dl>
<dd>Controls where file descriptor 0 (STDIN) of the executed processes is connected to. Takes one of <code>null</code>, <code>tty</code>, <code>tty-force</code>, <code>tty-fail</code>, <code>data</code>, <code>file:</code><i>path</i>, <code>socket</code> or <code>fd:</code><i>name</i>. </p>
<p> If <code>null</code> is selected, standard input will be connected to /dev/null, i.e. all read attempts by the process will result in immediate EOF. </p>
<p> If <code>tty</code> is selected, standard input is connected to a TTY (as configured by <i>TTYPath=</i>, see below) and the executed process becomes the controlling process of the terminal. If the terminal is already being controlled by another process, the executed process waits until the current controlling process releases the terminal. </p>
<p> <code>tty-force</code> is similar to <code>tty</code>, but the executed process is forcefully and immediately made the controlling process of the terminal, potentially removing previous controlling processes from the terminal. </p>
<p> <code>tty-fail</code> is similar to <code>tty</code>, but if the terminal already has a controlling process start-up of the executed process fails. </p>
<p> The <code>data</code> option may be used to configure arbitrary textual or binary data to pass via standard input to the executed process. The data to pass is configured via <i>StandardInputText=</i>/<i>StandardInputData=</i> (see below). Note that the actual file descriptor type passed (memory file, regular file, UNIX pipe, &#8230;) might depend on the kernel and available privileges. In any case, the file descriptor is read-only, and when read returns the specified data followed by EOF. </p>
<p> The <code>file:</code><i>path</i> option may be used to connect a specific file system object to standard input. An absolute path following the &quot;:&quot; character is expected, which may refer to a regular file, a FIFO or special file. If an <code>AF_UNIX</code> socket in the file system is specified, a stream socket is connected to it. The latter is useful for connecting standard input of processes to arbitrary system services. </p>
<p> The <code>socket</code> option is valid in socket-activated services only, and requires the relevant socket unit file (see <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5) for details) to have <i>Accept=yes</i> set, or to specify a single socket only. If this option is set, standard input will be connected to the socket the service was activated from, which is primarily useful for compatibility with daemons designed for use with the traditional <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) socket activation daemon. </p>
<p> The <code>fd:</code><i>name</i> option connects standard input to a specific, named file descriptor provided by a socket unit. The name may be specified as part of this option, following a &quot;:&quot; character (e.g. &quot;fd:foobar&quot;). If no name is specified, the name &quot;stdin&quot; is implied (i.e. &quot;fd&quot; is equivalent to &quot;fd:stdin&quot;). At least one socket unit defining the specified name must be provided via the <i>Sockets=</i> option, and the file descriptor name may differ from the name of its containing socket unit. If multiple matches are found, the first one will be used. See <i>FileDescriptorName=</i> in <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5) for more details about named file descriptors and their ordering. </p>
<p> This setting defaults to <code>null</code>, unless <i>StandardInputText=</i>/<i>StandardInputData=</i> are set, in which case it defaults to <code>data</code>.</dl>
<p> <i>StandardOutput=</i></p>
<dl>
<dd>Controls where file descriptor 1 (stdout) of the executed processes is connected to. Takes one of <code>inherit</code>, <code>null</code>, <code>tty</code>, <code>journal</code>, <code>kmsg</code>, <code>journal+console</code>, <code>kmsg+console</code>, <code>file:</code><i>path</i>, <code>append:</code><i>path</i>, <code>truncate:</code><i>path</i>, <code>socket</code> or <code>fd:</code><i>name</i>. </p>
<p> <code>inherit</code> duplicates the file descriptor of standard input for standard output. </p>
<p> <code>null</code> connects standard output to /dev/null, i.e. everything written to it will be lost. </p>
<p> <code>tty</code> connects standard output to a tty (as configured via <i>TTYPath=</i>, see below). If the TTY is used for output only, the executed process will not become the controlling process of the terminal, and will not fail or wait for other processes to release the terminal. </p>
<p> <code>journal</code> connects standard output with the journal, which is accessible via <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1). Note that everything that is written to kmsg (see below) is implicitly stored in the journal as well, the specific option listed below is hence a superset of this one. (Also note that any external, additional syslog daemons receive their log data from the journal, too, hence this is the option to use when logging shall be processed with such a daemon.) </p>
<p> <code>kmsg</code> connects standard output with the kernel log buffer which is accessible via <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1), in addition to the journal. The journal daemon might be configured to send all logs to kmsg anyway, in which case this option is no different from <code>journal</code>. </p>
<p> <code>journal+console</code> and <code>kmsg+console</code> work in a similar way as the two options above but copy the output to the system console as well. </p>
<p> The <code>file:</code><i>path</i> option may be used to connect a specific file system object to standard output. The semantics are similar to the same option of <i>StandardInput=</i>, see above. If <i>path</i> refers to a regular file on the filesystem, it is opened (created if it doesn&#8217;t exist yet) for writing at the beginning of the file, but without truncating it. If standard input and output are directed to the same file path, it is opened only once, for reading as well as writing and duplicated. This is particularly useful when the specified path refers to an <code>AF_UNIX</code> socket in the file system, as in that case only a single stream connection is created for both input and output. </p>
<p> <code>append:</code><i>path</i> is similar to <code>file:</code><i>path</i> above, but it opens the file in append mode. </p>
<p> <code>truncate:</code><i>path</i> is similar to <code>file:</code><i>path</i> above, but it truncates the file when opening it. For units with multiple command lines, e.g. <i>Type=oneshot</i> services with multiple <i>ExecStart=</i>, or services with <i>ExecCondition=</i>, <i>ExecStartPre=</i> or <i>ExecStartPost=</i>, the output file is reopened and therefore re-truncated for each command line. If the output file is truncated while another process still has the file open, e.g. by an <i>ExecReload=</i> running concurrently with an <i>ExecStart=</i>, and the other process continues writing to the file without adjusting its offset, then the space between the file pointers of the two processes may be filled with <code>NUL</code> bytes, producing a sparse file. Thus, <code>truncate:</code><i>path</i> is typically only useful for units where only one process runs at a time, such as services with a single <i>ExecStart=</i> and no <i>ExecStartPost=</i>, <i>ExecReload=</i>, <i>ExecStop=</i> or similar. </p>
<p> <code>socket</code> connects standard output to a socket acquired via socket activation. The semantics are similar to the same option of <i>StandardInput=</i>, see above. </p>
<p> The <code>fd:</code><i>name</i> option connects standard output to a specific, named file descriptor provided by a socket unit. A name may be specified as part of this option, following a &quot;:&quot; character (e.g. &quot;fd:foobar&quot;). If no name is specified, the name &quot;stdout&quot; is implied (i.e. &quot;fd&quot; is equivalent to &quot;fd:stdout&quot;). At least one socket unit defining the specified name must be provided via the <i>Sockets=</i> option, and the file descriptor name may differ from the name of its containing socket unit. If multiple matches are found, the first one will be used. See <i>FileDescriptorName=</i> in <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5) for more details about named descriptors and their ordering. </p>
<p> If the standard output (or error output, see below) of a unit is connected to the journal or the kernel log buffer, the unit will implicitly gain a dependency of type <i>After=</i> on systemd-journald.socket (also see the &quot;Implicit Dependencies&quot; section above). Also note that in this case stdout (or stderr, see below) will be an <code>AF_UNIX</code> stream socket, and not a pipe or FIFO that can be re-opened. This means when executing shell scripts the construct <code>echo &quot;hello&quot; &gt; /dev/stderr</code> for writing text to stderr will not work. To mitigate this use the construct <code>echo &quot;hello&quot; &gt;&amp;2</code> instead, which is mostly equivalent and avoids this pitfall. </p>
<p> This setting defaults to the value set with <i>DefaultStandardOutput=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), which defaults to <code>journal</code>. Note that setting this parameter might result in additional dependencies to be added to the unit (see above).</dl>
<p> <i>StandardError=</i></p>
<dl>
<dd>Controls where file descriptor 2 (stderr) of the executed processes is connected to. The available options are identical to those of <i>StandardOutput=</i>, with some exceptions: if set to <code>inherit</code> the file descriptor used for standard output is duplicated for standard error, while <code>fd:</code><i>name</i> will use a default file descriptor name of &quot;stderr&quot;. </p>
<p> This setting defaults to the value set with <i>DefaultStandardError=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), which defaults to <code>inherit</code>. Note that setting this parameter might result in additional dependencies to be added to the unit (see above).</dl>
<p> <i>StandardInputText=</i>, <i>StandardInputData=</i></p>
<dl>
<dd>Configures arbitrary textual or binary data to pass via file descriptor 0 (STDIN) to the executed processes. These settings have no effect unless <i>StandardInput=</i> is set to <code>data</code> (which is the default if <i>StandardInput=</i> is not set otherwise, but <i>StandardInputText=</i>/<i>StandardInputData=</i> is). Use this option to embed process input data directly in the unit file. </p>
<p> <i>StandardInputText=</i> accepts arbitrary textual data. C-style escapes for special characters as well as the usual &quot;%&quot;-specifiers are resolved. Each time this setting is used the specified text is appended to the per-unit data buffer, followed by a newline character (thus every use appends a new line to the end of the buffer). Note that leading and trailing whitespace of lines configured with this option is removed. If an empty line is specified the buffer is cleared (hence, in order to insert an empty line, add an additional &quot;
&quot; to the end or beginning of a line). </p>
<p> <i>StandardInputData=</i> accepts arbitrary binary data, encoded in m[blue]<code>Base64</code>m[]<font SIZE="-2">[9]</font>. No escape sequences or specifiers are resolved. Any whitespace in the encoded version is ignored during decoding. </p>
<p> Note that <i>StandardInputText=</i> and <i>StandardInputData=</i> operate on the same data buffer, and may be mixed in order to configure both binary and textual data for the same input stream. The textual or binary data is joined strictly in the order the settings appear in the unit file. Assigning an empty string to either will reset the data buffer. </p>
<p> Please keep in mind that in order to maintain readability long unit file settings may be split into multiple lines, by suffixing each line (except for the last) with a &quot;\&quot; character (see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details). This is particularly useful for large data configured with these two options. Example: </p>
<dl>
<dd>
<pre>...
StandardInput=data
StandardInputData=SWNrIHNpdHplIGRhIHVuJyBlc3NlIEtsb3BzLAp1ZmYgZWVtYWwga2xvcHAncy4KSWNrIGtpZWtl \
 LCBzdGF1bmUsIHd1bmRyZSBtaXIsCnVmZiBlZW1hbCBqZWh0IHNlIHVmZiBkaWUgVMO8ci4KTmFu \
 dSwgZGVuayBpY2ssIGljayBkZW5rIG5hbnUhCkpldHogaXNzZSB1ZmYsIGVyc2NodCB3YXIgc2Ug \
 enUhCkljayBqZWhlIHJhdXMgdW5kIGJsaWNrZSDigJQKdW5kIHdlciBzdGVodCBkcmF1w59lbj8g \
 SWNrZSEK
...</pre>
</dl>
</dl>
<p> <i>LogLevelMax=</i></p>
<dl>
<dd>Configures filtering by log level of log messages generated by this unit. Takes a <code>syslog</code> log level, one of <code>emerg</code> (lowest log level, only highest priority messages), <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code> (highest log level, also lowest priority messages). See <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for details. By default no filtering is applied (i.e. the default maximum log level is <code>debug</code>). Use this option to configure the logging system to drop log messages of a specific service above the specified level. For example, set <i>LogLevelMax=</i><code>info</code> in order to turn off debug logging of a particularly chatty unit. Note that the configured level is applied to any log messages written by any of the processes belonging to this unit, as well as any log messages written by the system manager process (PID 1) in reference to this unit, sent via any supported logging protocol. The filtering is applied early in the logging pipeline, before any kind of further processing is done. Moreover, messages which pass through this filter successfully might still be dropped by filters applied at a later stage in the logging subsystem. For example, <i>MaxLevelStore=</i> configured in <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) might prohibit messages of higher log levels to be stored on disk, even though the per-unit <i>LogLevelMax=</i> permitted it to be processed.</dl>
<p> <i>LogExtraFields=</i></p>
<dl>
<dd>Configures additional log metadata fields to include in all log records generated by processes associated with this unit. This setting takes one or more journal field assignments in the format &quot;FIELD=VALUE&quot; separated by whitespace. See <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7) for details on the journal field concept. Even though the underlying journal implementation permits binary field values, this setting accepts only valid UTF-8 values. To include space characters in a journal field value, enclose the assignment in double quotes (&quot;). The usual specifiers are expanded in all assignments (see below). Note that this setting is not only useful for attaching additional metadata to log records of a unit, but given that all fields and values are indexed may also be used to implement cross-unit log record matching. Assign an empty string to reset the list.</dl>
<p> <i>LogRateLimitIntervalSec=</i>, <i>LogRateLimitBurst=</i></p>
<dl>
<dd>Configures the rate limiting that is applied to messages generated by this unit. If, in the time interval defined by <i>LogRateLimitIntervalSec=</i>, more messages than specified in <i>LogRateLimitBurst=</i> are logged by a service, all further messages within the interval are dropped until the interval is over. A message about the number of dropped messages is generated. The time specification for <i>LogRateLimitIntervalSec=</i> may be specified in the following units: &quot;s&quot;, &quot;min&quot;, &quot;h&quot;, &quot;ms&quot;, &quot;us&quot; (see <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7) for details). The default settings are set by <i>RateLimitIntervalSec=</i> and <i>RateLimitBurst=</i> configured in <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5).</dl>
<p> <i>LogNamespace=</i></p>
<dl>
<dd>Run the unit&#8217;s processes in the specified journal namespace. Expects a short user-defined string identifying the namespace. If not used the processes of the service are run in the default journal namespace, i.e. their log stream is collected and processed by systemd-journald.service. If this option is used any log data generated by processes of this unit (regardless if via the <code>syslog()</code>, journal native logging or stdout/stderr logging) is collected and processed by an instance of the systemd-journald [at] .service template unit, which manages the specified namespace. The log data is stored in a data store independent from the default log namespace&#8217;s data store. See <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8) for details about journal namespaces. </p>
<p> Internally, journal namespaces are implemented through Linux mount namespacing and over-mounting the directory that contains the relevant <code>AF_UNIX</code> sockets used for logging in the unit&#8217;s mount namespace. Since mount namespaces are used this setting disconnects propagation of mounts from the unit&#8217;s processes to the host, similar to how <i>ReadOnlyPaths=</i> and similar settings (see above) work. Journal namespaces may hence not be used for services that need to establish mount points on the host. </p>
<p> When this option is used the unit will automatically gain ordering and requirement dependencies on the two socket units associated with the systemd-journald [at] .service instance so that they are automatically established prior to the unit starting up. Note that when this option is used log output of this service does not appear in the regular <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) output, unless the <code>&#8211;namespace=</code> option is used. </p>
<p> This option is only available for system services and is not supported for services running in per-user instances of the service manager.</dl>
<p> <i>SyslogIdentifier=</i></p>
<dl>
<dd>Sets the process name (&quot;<code>syslog</code> tag&quot;) to prefix log lines sent to the logging system or the kernel log buffer with. If not set, defaults to the process name of the executed process. This option is only useful when <i>StandardOutput=</i> or <i>StandardError=</i> are set to <code>journal</code> or <code>kmsg</code> (or to the same settings in combination with <code>+console</code>) and only applies to log messages written to stdout or stderr.</dl>
<p> <i>SyslogFacility=</i></p>
<dl>
<dd>Sets the <code>syslog</code> facility identifier to use when logging. One of <code>kern</code>, <code>user</code>, <code>mail</code>, <code>daemon</code>, <code>auth</code>, <code>syslog</code>, <code>lpr</code>, <code>news</code>, <code>uucp</code>, <code>cron</code>, <code>authpriv</code>, <code>ftp</code>, <code>local0</code>, <code>local1</code>, <code>local2</code>, <code>local3</code>, <code>local4</code>, <code>local5</code>, <code>local6</code> or <code>local7</code>. See <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for details. This option is only useful when <i>StandardOutput=</i> or <i>StandardError=</i> are set to <code>journal</code> or <code>kmsg</code> (or to the same settings in combination with <code>+console</code>), and only applies to log messages written to stdout or stderr. Defaults to <code>daemon</code>.</dl>
<p> <i>SyslogLevel=</i></p>
<dl>
<dd>The default <code>syslog</code> log level to use when logging to the logging system or the kernel log buffer. One of <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code>. See <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for details. This option is only useful when <i>StandardOutput=</i> or <i>StandardError=</i> are set to <code>journal</code> or <code>kmsg</code> (or to the same settings in combination with <code>+console</code>), and only applies to log messages written to stdout or stderr. Note that individual lines output by executed processes may be prefixed with a different log level which can be used to override the default log level specified here. The interpretation of these prefixes may be disabled with <i>SyslogLevelPrefix=</i>, see below. For details, see <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3). Defaults to <code>info</code>.</dl>
<p> <i>SyslogLevelPrefix=</i></p>
<dl>
<dd>Takes a boolean argument. If true and <i>StandardOutput=</i> or <i>StandardError=</i> are set to <code>journal</code> or <code>kmsg</code> (or to the same settings in combination with <code>+console</code>), log lines written by the executed process that are prefixed with a log level will be processed with this log level set but the prefix removed. If set to false, the interpretation of these prefixes is disabled and the logged lines are passed on as-is. This only applies to log messages written to stdout or stderr. For details about this prefixing see <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3). Defaults to true.</dl>
<p> <i>TTYPath=</i></p>
<dl>
<dd>Sets the terminal device node to use if standard input, output, or error are connected to a TTY (see above). Defaults to /dev/console.</dl>
<p> <i>TTYReset=</i></p>
<dl>
<dd>Reset the terminal device specified with <i>TTYPath=</i> before and after execution. Defaults to &quot;no&quot;.</dl>
<p> <i>TTYVHangup=</i></p>
<dl>
<dd>Disconnect all clients which have opened the terminal device specified with <i>TTYPath=</i> before and after execution. Defaults to &quot;no&quot;.</dl>
<p> <i>TTYVTDisallocate=</i></p>
<dl>
<dd>If the terminal device specified with <i>TTYPath=</i> is a virtual console terminal, try to deallocate the TTY before and after execution. This ensures that the screen and scrollback buffer is cleared. Defaults to &quot;no&quot;.</dl>
<h2>Credentials</h2>
<p><i>LoadCredential=</i><i>ID</i>[:<i>PATH</i>]</p>
<dl>
<dd>Pass a credential to the unit. Credentials are limited-size binary or textual objects that may be passed to unit processes. They are primarily used for passing cryptographic keys (both public and private) or certificates, user account information or identity information from host to services. The data is accessible from the unit&#8217;s processes via the file system, at a read-only location that (if possible and permitted) is backed by non-swappable memory. The data is only accessible to the user associated with the unit, via the <i>User=</i>/<i>DynamicUser=</i> settings (as well as the superuser). When available, the location of credentials is exported as the <i>$CREDENTIALS_DIRECTORY</i> environment variable to the unit&#8217;s processes. </p>
<p> The <i>LoadCredential=</i> setting takes a textual ID to use as name for a credential plus a file system path, separated by a colon. The ID must be a short ASCII string suitable as filename in the filesystem, and may be chosen freely by the user. If the specified path is absolute it is opened as regular file and the credential data is read from it. If the absolute path refers to an <code>AF_UNIX</code> stream socket in the file system a connection is made to it (only once at unit start-up) and the credential data read from the connection, providing an easy IPC integration point for dynamically providing credentials from other services. If the specified path is not absolute and itself qualifies as valid credential identifier it is understood to refer to a credential that the service manager itself received via the <i>$CREDENTIALS_DIRECTORY</i> environment variable, which may be used to propagate credentials from an invoking environment (e.g. a container manager that invoked the service manager) into a service. The contents of the file/socket may be arbitrary binary or textual data, including newline characters and <code>NUL</code> bytes. If the file system path is omitted it is chosen identical to the credential name, i.e. this is a terse way do declare credentials to inherit from the service manager into a service. This option may be used multiple times, each time defining an additional credential to pass to the unit. </p>
<p> The credential files/IPC sockets must be accessible to the service manager, but don&#8217;t have to be directly accessible to the unit&#8217;s processes: the credential data is read and copied into separate, read-only copies for the unit that are accessible to appropriately privileged processes. This is particularly useful in combination with <i>DynamicUser=</i> as this way privileged data can be made available to processes running under a dynamic UID (i.e. not a previously known one) without having to open up access to all users. </p>
<p> In order to reference the path a credential may be read from within a <i>ExecStart=</i> command line use &quot;${CREDENTIALS_DIRECTORY}/mycred&quot;, e.g. &quot;ExecStart=cat ${CREDENTIALS_DIRECTORY}/mycred&quot;. </p>
<p> Currently, an accumulated credential size limit of 1 MB per unit is enforced. </p>
<p> If referencing an <code>AF_UNIX</code> stream socket to connect to, the connection will originate from an abstract namespace socket, that includes information about the unit and the credential ID in its socket name. Use <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2) to query this information. The returned socket name is formatted as <code>NUL</code> <i>RANDOM</i> &quot;/unit/&quot; <i>UNIT</i> &quot;/&quot; <i>ID</i>, i.e. a <code>NUL</code> byte (as required for abstract namespace socket names), followed by a random string (consisting of alphadecimal characters), followed by the literal string &quot;/unit/&quot;, followed by the requesting unit name, followed by the literal character &quot;/&quot;, followed by the textual credential ID requested. Example: &quot;
