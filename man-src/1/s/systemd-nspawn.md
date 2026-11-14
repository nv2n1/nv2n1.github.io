---
title: "systemd-nspawn(1)"
name: "systemd-nspawn"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-nspawn/"
description: "systemd-nspawn – Spawn a namespace container for debugging, testing and building"
---

<h2 class="name">NAME</h2>
<p> systemd-nspawn &#8211; Spawn a namespace container for debugging, testing and building </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-nspawn</code> [OPTIONS&#8230;] [<i>COMMAND</i>&nbsp;<wbr>[ARGS&#8230;]]</p>
<dt> <code>systemd-nspawn</code> -b [OPTIONS&#8230;] [ARGS&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-nspawn</code></p>
<dd>may be used to run a command or OS in a light-weight namespace container. In many ways it is similar to <code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1), but more powerful since it fully virtualizes the file system hierarchy, as well as the process tree, the various IPC subsystems and the host and domain name. </p>
<p> <code>systemd-nspawn</code> limits access to various kernel interfaces in the container to read-only, such as /sys, /proc/sys or /sys/fs/selinux. Network interfaces and the system clock may not be changed from within the container. Device nodes may not be created. The host system cannot be rebooted and kernel modules may not be loaded from within the container. </p>
<p> Note that even though these security precautions are taken <code>systemd-nspawn</code> is not suitable for secure container setups. Many of the security features may be circumvented and are hence primarily useful to avoid accidental changes to the host system from the container. The intended use of this program is debugging and testing as well as building of packages, distributions and software involved with boot and systems management. </p>
<p> In contrast to <code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1)&nbsp;<wbr><code>systemd-nspawn</code> may be used to boot full Linux-based operating systems in a container. </p>
<p> Use a tool like <code><a href="/docs/linux/man/8-yum/">yum</a></code>(8), <code><a href="/docs/linux/man/8-debootstrap/">debootstrap</a></code>(8), or <code><a href="/docs/linux/man/8-pacman/">pacman</a></code>(8) to set up an OS directory tree suitable as file system hierarchy for <code>systemd-nspawn</code> containers. </p>
<p> Note that <code>systemd-nspawn</code> will mount file systems private to the container to /dev, /run and similar. These will not be visible outside of the container, and their contents will be lost when the container exits. </p>
<p> Note that running two <code>systemd-nspawn</code> containers from the same directory tree will not make processes in them see each other. The PID namespace separation of the two containers is complete and the containers will share very few runtime objects except for the underlying file system. Use <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1)&#8217;s <code>login</code> command to request an additional login prompt in a running container. </p>
<p> <code>systemd-nspawn</code> implements the m[blue]<code>Container Interface</code>m[]<font SIZE="-2">[1]</font> specification. </p>
<p> As a safety check <code>systemd-nspawn</code> will verify the existence of /usr/lib/os-release or /etc/os-release in the container tree before starting the container (see <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5)). It might be necessary to add this file to the container tree manually if the OS of the container is too old to contain this file out-of-the-box.</p>
<h2>OPTIONS</h2>
<p> If option <code>-b</code> is specified, the arguments are used as arguments for the init binary. Otherwise, <i>COMMAND</i> specifies the program to launch in the container, and the remaining arguments are used as arguments for this program. If <code>-b</code> is not used and no arguments are specifed, a shell is launched in the container. </p>
<p> The following options are understood: </p>
<p> <code>-D</code>, <code>&#8211;directory=</code></p>
<dl>
<dt>
<dd> Directory to use as file system root for the container. </p>
<p> If neither <code>&#8211;directory=</code>, nor <code>&#8211;image=</code> is specified the directory is determined as /var/lib/machines/ suffixed by the machine name as specified with <code>&#8211;machine=</code>. If neither <code>&#8211;directory=</code>, <code>&#8211;image=</code>, nor <code>&#8211;machine=</code> are specified, the current directory will be used. May not be specified together with <code>&#8211;image=</code>.</dl>
<p> <code>&#8211;template=</code></p>
<dl>
<dt>
<dd> Directory or &quot;btrfs&quot; subvolume to use as template for the container&#8217;s root directory. If this is specified and the container&#8217;s root directory (as configured by <code>&#8211;directory=</code>) does not yet exist it is created as &quot;btrfs&quot; subvolume and populated from this template tree. Ideally, the specified template path refers to the root of a &quot;btrfs&quot; subvolume, in which case a simple copy-on-write snapshot is taken, and populating the root directory is instant. If the specified template path does not refer to the root of a &quot;btrfs&quot; subvolume (or not even to a &quot;btrfs&quot; file system at all), the tree is copied, which can be substantially more time-consuming. Note that if this option is used the container&#8217;s root directory (in contrast to the template directory!) must be located on a &quot;btrfs&quot; file system, so that the &quot;btrfs&quot; subvolume may be created. May not be specified together with <code>&#8211;image=</code> or <code>&#8211;ephemeral</code>.</dl>
<p> <code>-x</code>, <code>&#8211;ephemeral</code></p>
<dl>
<dt>
<dd> If specified, the container is run with a temporary &quot;btrfs&quot; snapshot of its root directory (as configured with <code>&#8211;directory=</code>), that is removed immediately when the container terminates. This option is only supported if the root file system is &quot;btrfs&quot;. May not be specified together with <code>&#8211;image=</code> or <code>&#8211;template=</code>.</dl>
<p> <code>-i</code>, <code>&#8211;image=</code></p>
<dl>
<dt>
<dd> Disk image to mount the root directory for the container from. Takes a path to a regular file or to a block device node. The file or block device must contain either: </p>
<dl>
<dt>
<dd> &bull; An MBR partition table with a single partition of type 0x83 that is marked bootable.</dl>
<dl>
<dt>
<dd> &bull; A GUID partition table (GPT) with a single partition of type 0fc63daf-8483-4772-8e79-3d69d8477de4.</dl>
<dl>
<dt>
<dd> &bull; A GUID partition table (GPT) with a marked root partition which is mounted as the root directory of the container. Optionally, GPT images may contain a home and/or a server data partition which are mounted to the appropriate places in the container. All these partitions must be identified by the partition types defined by the m[blue]<code>Discoverable Partitions Specification</code>m[]<font SIZE="-2">[2]</font>.</dl>
<p> Any other partitions, such as foreign partitions, swap partitions or EFI system partitions are not mounted. May not be specified together with <code>&#8211;directory=</code>, <code>&#8211;template=</code> or <code>&#8211;ephemeral</code>.</dl>
<p> <code>-b</code>, <code>&#8211;boot</code></p>
<dl>
<dt>
<dd> Automatically search for an init binary and invoke it instead of a shell or a user supplied program. If this option is used, arguments specified on the command line are used as arguments for the init binary. This option may not be combined with <code>&#8211;share-system</code>.</dl>
<p> <code>-u</code>, <code>&#8211;user=</code></p>
<dl>
<dt>
<dd> After transitioning into the container, change to the specified user-defined in the container&#8217;s user database. Like all other systemd-nspawn features, this is not a security feature and provides protection against accidental destructive operations only.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Sets the machine name for this container. This name may be used to identify this container during its runtime (for example in tools like <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1) and similar), and is used to initialize the container&#8217;s hostname (which the container can choose to override, however). If not specified, the last component of the root directory path of the container is used, possibly suffixed with a random identifier in case <code>&#8211;ephemeral</code> mode is selected. If the root directory selected is the host&#8217;s root directory the host&#8217;s hostname is used as default instead.</dl>
<p> <code>&#8211;uuid=</code></p>
<dl>
<dt>
<dd> Set the specified UUID for the container. The init system will initialize /etc/machine-id from this if this file is not set yet.</dl>
<p> <code>&#8211;slice=</code></p>
<dl>
<dt>
<dd> Make the container part of the specified slice, instead of the default machine.slice.</dl>
<p> <code>&#8211;private-network</code></p>
<dl>
<dt>
<dd> Disconnect networking of the container from the host. This makes all network interfaces unavailable in the container, with the exception of the loopback device and those specified with <code>&#8211;network-interface=</code> and configured with <code>&#8211;network-veth</code>. If this option is specified, the CAP_NET_ADMIN capability will be added to the set of capabilities the container retains. The latter may be disabled by using <code>&#8211;drop-capability=</code>.</dl>
<p> <code>&#8211;network-interface=</code></p>
<dl>
<dt>
<dd> Assign the specified network interface to the container. This will remove the specified interface from the calling namespace and place it in the container. When the container terminates, it is moved back to the host namespace. Note that <code>&#8211;network-interface=</code> implies <code>&#8211;private-network</code>. This option may be used more than once to add multiple network interfaces to the container.</dl>
<p> <code>&#8211;network-macvlan=</code></p>
<dl>
<dt>
<dd> Create a &quot;macvlan&quot; interface of the specified Ethernet network interface and add it to the container. A &quot;macvlan&quot; interface is a virtual interface that adds a second MAC address to an existing physical Ethernet link. The interface in the container will be named after the interface on the host, prefixed with &quot;mv-&quot;. Note that <code>&#8211;network-macvlan=</code> implies <code>&#8211;private-network</code>. This option may be used more than once to add multiple network interfaces to the container.</dl>
<p> <code>&#8211;network-ipvlan=</code></p>
<dl>
<dt>
<dd> Create an &quot;ipvlan&quot; interface of the specified Ethernet network interface and add it to the container. An &quot;ipvlan&quot; interface is a virtual interface, similar to a &quot;macvlan&quot; interface, which uses the same MAC address as the underlying interface. The interface in the container will be named after the interface on the host, prefixed with &quot;iv-&quot;. Note that <code>&#8211;network-ipvlan=</code> implies <code>&#8211;private-network</code>. This option may be used more than once to add multiple network interfaces to the container.</dl>
<p> <code>-n</code>, <code>&#8211;network-veth</code></p>
<dl>
<dt>
<dd> Create a virtual Ethernet link (&quot;veth&quot;) between host and container. The host side of the Ethernet link will be available as a network interface named after the container&#8217;s name (as specified with <code>&#8211;machine=</code>), prefixed with &quot;ve-&quot;. The container side of the Ethernet link will be named &quot;host0&quot;. Note that <code>&#8211;network-veth</code> implies <code>&#8211;private-network</code>.</dl>
<p> <code>&#8211;network-bridge=</code></p>
<dl>
<dt>
<dd> Adds the host side of the Ethernet link created with <code>&#8211;network-veth</code> to the specified bridge. Note that <code>&#8211;network-bridge=</code> implies <code>&#8211;network-veth</code>. If this option is used, the host side of the Ethernet link will use the &quot;vb-&quot; prefix instead of &quot;ve-&quot;.</dl>
<p> <code>-p</code>, <code>&#8211;port=</code></p>
<dl>
<dt>
<dd> If private networking is enabled, maps an IP port on the host onto an IP port on the container. Takes a protocol specifier (either &quot;tcp&quot; or &quot;udp&quot;), separated by a colon from a host port number in the range 1 to 65535, separated by a colon from a container port number in the range from 1 to 65535. The protocol specifier and its separating colon may be omitted, in which case &quot;tcp&quot; is assumed. The container port number and its colon may be ommitted, in which case the same port as the host port is implied. This option is only supported if private networking is used, such as <code>&#8211;network-veth</code> or <code>&#8211;network-bridge=</code>.</dl>
<p> <code>-Z</code>, <code>&#8211;selinux-context=</code></p>
<dl>
<dt>
<dd> Sets the SELinux security context to be used to label processes in the container.</dl>
<p> <code>-L</code>, <code>&#8211;selinux-apifs-context=</code></p>
<dl>
<dt>
<dd> Sets the SELinux security context to be used to label files in the virtual API file systems in the container.</dl>
<p> <code>&#8211;capability=</code></p>
<dl>
<dt>
<dd> List one or more additional capabilities to grant the container. Takes a comma-separated list of capability names, see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for more information. Note that the following capabilities will be granted in any way: CAP_CHOWN, CAP_DAC_OVERRIDE, CAP_DAC_READ_SEARCH, CAP_FOWNER, CAP_FSETID, CAP_IPC_OWNER, CAP_KILL, CAP_LEASE, CAP_LINUX_IMMUTABLE, CAP_NET_BIND_SERVICE, CAP_NET_BROADCAST, CAP_NET_RAW, CAP_SETGID, CAP_SETFCAP, CAP_SETPCAP, CAP_SETUID, CAP_SYS_ADMIN, CAP_SYS_CHROOT, CAP_SYS_NICE, CAP_SYS_PTRACE, CAP_SYS_TTY_CONFIG, CAP_SYS_RESOURCE, CAP_SYS_BOOT, CAP_AUDIT_WRITE, CAP_AUDIT_CONTROL. Also CAP_NET_ADMIN is retained if <code>&#8211;private-network</code> is specified. If the special value &quot;all&quot; is passed, all capabilities are retained.</dl>
<p> <code>&#8211;drop-capability=</code></p>
<dl>
<dt>
<dd> Specify one or more additional capabilities to drop for the container. This allows running the container with fewer capabilities than the default (see above).</dl>
<p> <code>&#8211;link-journal=</code></p>
<dl>
<dt>
<dd> Control whether the container&#8217;s journal shall be made visible to the host system. If enabled, allows viewing the container&#8217;s journal files from the host (but not vice versa). Takes one of &quot;no&quot;, &quot;host&quot;, &quot;try-host&quot;, &quot;guest&quot;, &quot;try-guest&quot;, &quot;auto&quot;. If &quot;no&quot;, the journal is not linked. If &quot;host&quot;, the journal files are stored on the host file system (beneath /var/log/journal/<i>machine-id</i>) and the subdirectory is bind-mounted into the container at the same location. If &quot;guest&quot;, the journal files are stored on the guest file system (beneath /var/log/journal/<i>machine-id</i>) and the subdirectory is symlinked into the host at the same location. &quot;try-host&quot; and &quot;try-guest&quot; do the same but do not fail if the host does not have persistent journalling enabled. If &quot;auto&quot; (the default), and the right subdirectory of /var/log/journal exists, it will be bind mounted into the container. If the subdirectory does not exist, no linking is performed. Effectively, booting a container once with &quot;guest&quot; or &quot;host&quot; will link the journal persistently if further on the default of &quot;auto&quot; is used.</dl>
<p> <code>-j</code></p>
<dl>
<dt>
<dd> Equivalent to <code>&#8211;link-journal=try-guest</code>.</dl>
<p> <code>&#8211;read-only</code></p>
<dl>
<dt>
<dd> Mount the root file system read-only for the container.</dl>
<p> <code>&#8211;bind=</code>, <code>&#8211;bind-ro=</code></p>
<dl>
<dt>
<dd> Bind mount a file or directory from the host into the container. Either takes a path argument &#8212; in which case the specified path will be mounted from the host to the same path in the container &#8211;, or a colon-separated pair of paths &#8212; in which case the first specified path is the source in the host, and the second path is the destination in the container. The <code>&#8211;bind-ro=</code> option creates read-only bind mounts.</dl>
<p> <code>&#8211;tmpfs=</code></p>
<dl>
<dt>
<dd> Mount a tmpfs file system into the container. Takes a single absolute path argument that specifies where to mount the tmpfs instance to (in which case the directory access mode will be chosen as 0755, owned by root/root), or optionally a colon-separated pair of path and mount option string, that is used for mounting (in which case the kernel default for access mode and owner will be chosen, unless otherwise specified). This option is particularly useful for mounting directories such as /var as tmpfs, to allow state-less systems, in particular when combined with <code>&#8211;read-only</code>.</dl>
<p> <code>&#8211;setenv=</code></p>
<dl>
<dt>
<dd> Specifies an environment variable assignment to pass to the init process in the container, in the format &quot;NAME=VALUE&quot;. This may be used to override the default variables or to set additional variables. This parameter may be used more than once.</dl>
<p> <code>&#8211;share-system</code></p>
<dl>
<dt>
<dd> Allows the container to share certain system facilities with the host. More specifically, this turns off PID namespacing, UTS namespacing and IPC namespacing, and thus allows the guest to see and interact more easily with processes outside of the container. Note that using this option makes it impossible to start up a full Operating System in the container, as an init system cannot operate in this mode. It is only useful to run specific programs or applications this way, without involving an init system in the container. This option implies <code>&#8211;register=no</code>. This option may not be combined with <code>&#8211;boot</code>.</dl>
<p> <code>&#8211;register=</code></p>
<dl>
<dt>
<dd> Controls whether the container is registered with <code><a href="/docs/linux/man/8-systemd-machined/">systemd-machined</a></code>(8). Takes a boolean argument, defaults to &quot;yes&quot;. This option should be enabled when the container runs a full Operating System (more specifically: an init system), and is useful to ensure that the container is accessible via <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1) and shown by tools such as <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). If the container does not run an init system, it is recommended to set this option to &quot;no&quot;. Note that <code>&#8211;share-system</code> implies <code>&#8211;register=no</code>.</dl>
<p> <code>&#8211;keep-unit</code></p>
<dl>
<dt>
<dd> Instead of creating a transient scope unit to run the container in, simply register the service or scope unit <code>systemd-nspawn</code> has been invoked in with <code><a href="/docs/linux/man/8-systemd-machined/">systemd-machined</a></code>(8). This has no effect if <code>&#8211;register=no</code> is used. This switch should be used if <code>systemd-nspawn</code> is invoked from within a service unit, and the service unit&#8217;s sole purpose is to run a single <code>systemd-nspawn</code> container. This option is not available if run from a user session.</dl>
<p> <code>&#8211;personality=</code></p>
<dl>
<dt>
<dd> Control the architecture (&quot;personality&quot;) reported by <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2) in the container. Currently, only &quot;x86&quot; and &quot;x86-64&quot; are supported. This is useful when running a 32-bit container on a 64-bit host. If this setting is not used, the personality reported in the container is the same as the one reported on the host.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Turns off any status output by the tool itself. When this switch is used, the only output from nspawn will be the console output of the container OS itself.</dl>
<p> <code>&#8211;volatile</code><i>=MODE</i></p>
<dl>
<dt>
<dd> Boots the container in volatile mode. When no mode parameter is passed or when mode is specified as &quot;yes&quot; full volatile mode is enabled. This means the root directory is mounted as mostly unpopulated &quot;tmpfs&quot; instance, and /usr from the OS tree is mounted into it, read-only (the system thus starts up with read-only OS resources, but pristine state and configuration, any changes to the either are lost on shutdown). When the mode parameter is specified as &quot;state&quot; the OS tree is mounted read-only, but /var is mounted as &quot;tmpfs&quot; instance into it (the system thus starts up with read-only OS resources and configuration, but pristine state, any changes to the latter are lost on shutdown). When the mode parameter is specified as &quot;no&quot; (the default) the whole OS tree is made available writable. </p>
<p> Note that setting this to &quot;yes&quot; or &quot;state&quot; will only work correctly with operating systems in the container that can boot up with only /usr mounted, and are able to populate /var automatically, as needed.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Download a Fedora image and start a shell in it</code> </p>
<dl>
<dt>
<dd>
<pre>
# machinectl pull-raw --verify=no <a rel="nofollow" href="http://ftp.halifax.rwth-aachen.de/fedora/linux/releases/21/Cloud/Images/x86_64/Fedora-Cloud-Base-20141203-21.x86_64.raw.xz">http://ftp.halifax.rwth-aachen.de/fedora/linux/releases/21/Cloud/Images/x86_64/Fedora-Cloud-Base-20141203-21.x86_64.raw.xz</a>
# systemd-nspawn -M Fedora-Cloud-Base-20141203-21
</pre>
</dl>
<p> This downloads an image using <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1) and opens a shell in it. </p>
<p> <code>Example 2. Build and boot a minimal Fedora distribution in a container</code> </p>
<dl>
<dt>
<dd>
<pre><code>
#yum - y-- releasever = 21 --nogpg-- installroot = / srv / mycontainer-- disablerepo = '*' --enablerepo = fedora install systemd passwd yum fedora - release vim - minimal
#systemd - nspawn - bD / srv / mycontainer
</code></pre>
</dl>
<p> This installs a minimal Fedora distribution into the directory /srv/mycontainer/ and then boots an OS in a namespace container in it. </p>
<p> <code>Example 3. Spawn a shell in a container of a minimal Debian unstable distribution</code> </p>
<dl>
<dt>
<dd>
<pre>
# debootstrap --arch=amd64 unstable ~/debian-tree/
# systemd-nspawn -D ~/debian-tree/
</pre>
</dl>
<p> This installs a minimal Debian unstable distribution into the directory ~/debian-tree/ and then spawns a shell in a namespace container in it. </p>
<p> <code>Example 4. Boot a minimal Arch Linux distribution in a container</code> </p>
<dl>
<dt>
<dd>
<pre>
# pacstrap -c -d ~/arch-tree/ base
# systemd-nspawn -bD ~/arch-tree/
</pre>
</dl>
<p> This installs a mimimal Arch Linux distribution into the directory ~/arch-tree/ and then boots an OS in a namespace container in it. </p>
<p> <code>Example 5. Boot into an ephemeral &quot;btrfs&quot; snapshot of the host system</code> </p>
<dl>
<dt>
<dd>
<pre>
# systemd-nspawn -D / -xb
</pre>
</dl>
<p> This runs a copy of the host system in a &quot;btrfs&quot; snapshot which is removed immediately when the container exits. All file system changes made during runtime will be lost on shutdown, hence. </p>
<p> <code>Example 6. Run a container with SELinux sandbox security contexts</code> </p>
<dl>
<dt>
<dd>
<pre>
# chcon system_u:object_r:svirt_sandbox_file_t:s0:c0,c1 -R /srv/container
# systemd-nspawn -L system_u:object_r:svirt_sandbox_file_t:s0:c0,c1 -Z system_u:system_r:svirt_lxc_net_t:s0:c0,c1 -D /srv/container /bin/sh
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit code of the program executed in the container is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1), <code><a href="/docs/linux/man/8-yum/">yum</a></code>(8), <code><a href="/docs/linux/man/8-debootstrap/">debootstrap</a></code>(8), <code><a href="/docs/linux/man/8-pacman/">pacman</a></code>(8), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1), <code><a href="/docs/linux/man/8-btrfs/">btrfs</a></code>(8)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Container Interface</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/ContainerInterface">http://www.freedesktop.org/wiki/Software/systemd/ContainerInterface</a></dl>
<dt> 2.</p>
<dd> Discoverable Partitions Specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/DiscoverablePartitionsSpec/">http://www.freedesktop.org/wiki/Specifications/DiscoverablePartitionsSpec/</a></dl>
</dl>
<h2>Index</h2>
