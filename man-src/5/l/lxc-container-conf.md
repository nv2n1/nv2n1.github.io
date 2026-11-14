---
title: "lxc-container-conf(5)"
name: "lxc-container-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lxc-container-conf/"
description: "lxc.container.conf – LXC container configuration file"
---

<p>lxc.container.conf &#8211; LXC container configuration file</p>
<h2>Description</h2>
<p>The linux containers (<code>lxc</code>) are always created before being used. This creation defines a set of system resources to be virtualized / isolated when a process is using the container. By default, the pids, sysv ipc and mount points are virtualized and isolated. The other system resources are shared across containers, until they are explicitly defined in the configuration file. For example, if there is no network configuration, the network will be shared between the creator of the container and the container itself, but if the network is specified, a new network stack is created for the container and the container can no longer use the network of its ancestor. </p>
<p> The configuration file defines the different system resources to be assigned for the container. At present, the utsname, the network, the mount points, the root file system, the user namespace, and the control groups are supported. </p>
<p> Each option in the configuration file has the form <code>key = value</code> fitting in one line. The &#8216;#&#8217; character means the line is a comment. List options, like capabilities and cgroups options, can be used with no value to clear any previously defined values of that option.</p>
<h3>Configuration</h3>
<p>In order to ease administration of multiple related containers, it is possible to have a container configuration file cause another file to be loaded. For instance, network configuration can be defined in one common file which is included by multiple containers. Then, if the containers are moved to another host, only one file may need to be updated.</p>
<dl>
<dt><code>lxc.include</code></p>
<dd>Specify the file to be included. The included file must be in the same valid lxc configuration file format.</dl>
<h3>Architecture</h3>
<p>Allows one to set the architecture for the container. For example, set a 32bits architecture for a container running 32bits binaries on a 64bits host. This fixes the container scripts which rely on the architecture to do some work like downloading the packages.</p>
<dl>
<dt><code>lxc.arch</code></p>
<dd>Specify the architecture for the container. </p>
<p> Valid options are <code>x86</code>, <code>i686</code>, <code>x86_64</code>, <code>amd64</code></dl>
<h3>Hostname</h3>
<p>The utsname section defines the hostname to be set for the container. That means the container can set its own hostname without changing the one from the system. That makes the hostname private for the container.</p>
<dl>
<dt><code>lxc.utsname</code></p>
<dd>specify the hostname for the container</dl>
<h3>Halt Signal</h3>
<p>Allows one to specify signal name or number, sent by lxc-stop to the container&#8217;s init process to cleanly shutdown the container. Different init systems could use different signals to perform clean shutdown sequence. This option allows the signal to be specified in <a href="/docs/linux/man/1-kill/">kill</a>(1) fashion, e.g. SIGPWR, SIGRTMIN+14, SIGRTMAX-10 or plain number. The default signal is SIGPWR.</p>
<dl>
<dt><code>lxc.haltsignal</code></p>
<dd>specify the signal used to halt the container</dl>
<h3>Stop Signal</h3>
<p>Allows one to specify signal name or number, sent by lxc-stop to forcibly shutdown the container. This option allows signal to be specified in <a href="/docs/linux/man/1-kill/">kill</a>(1) fashion, e.g. SIGKILL, SIGRTMIN+14, SIGRTMAX-10 or plain number. The default signal is SIGKILL.</p>
<dl>
<dt><code>lxc.stopsignal</code></p>
<dd>specify the signal used to stop the container</dl>
<h3>Network</h3>
<p>The network section defines how the network is virtualized in the container. The network virtualization acts at layer two. In order to use the network virtualization, parameters must be specified to define the network interfaces of the container. Several virtual interfaces can be assigned and used in a container even if the system has only one physical network interface.</p>
<dl>
<dt><code>lxc.network</code></p>
<dd>may be used without a value to clear all previous network options.</p>
<dt><code>lxc.network.type</code></p>
<dd>specify what kind of network virtualization to be used for the container. Each time a <code>lxc.network.type</code> field is found a new round of network configuration begins. In this way, several network virtualization types can be specified for the same container, as well as assigning several network interfaces for one container. The different virtualization types can be: </p>
<p> <code>none:</code> will cause the container to share the host&#8217;s network namespace. This means the host network devices are usable in the container. It also means that if both the container and host have upstart as init, &#8216;halt&#8217; in a container (for instance) will shut down the host. </p>
<p> <code>empty:</code> will create only the loopback interface. </p>
<p> <code>veth:</code> a virtual ethernet pair device is created with one side assigned to the container and the other side attached to a bridge specified by the <code>lxc.network.link</code> option. If the bridge is not specified, then the veth pair device will be created but not attached to any bridge. Otherwise, the bridge has to be created on the system before starting the container. <code>lxc</code> won&#8217;t handle any configuration outside of the container. By default, <code>lxc</code> chooses a name for the network device belonging to the outside of the container, but if you wish to handle this name yourselves, you can tell <code>lxc</code> to set a specific name with the <code>lxc.network.veth.pair</code> option (except for unprivileged containers where this option is ignored for security reasons). </p>
<p> <code>vlan:</code> a vlan interface is linked with the interface specified by the <code>lxc.network.link</code> and assigned to the container. The vlan identifier is specified with the option <code>lxc.network.vlan.id</code>. </p>
<p> <code>macvlan:</code> a macvlan interface is linked with the interface specified by the <code>lxc.network.link</code> and assigned to the container. <code>lxc.network.macvlan.mode</code> specifies the mode the macvlan will use to communicate between different macvlan on the same upper device. The accepted modes are <code>private</code>, the device never communicates with any other device on the same upper_dev (default), <code>vepa</code>, the new Virtual Ethernet Port Aggregator (VEPA) mode, it assumes that the adjacent bridge returns all frames where both source and destination are local to the macvlan port, i.e. the bridge is set up as a reflective relay. Broadcast frames coming in from the upper_dev get flooded to all macvlan interfaces in VEPA mode, local frames are not delivered locally, or <code>bridge</code>, it provides the behavior of a simple bridge between different macvlan interfaces on the same port. Frames from one interface to another one get delivered directly and are not sent out externally. Broadcast frames get flooded to all other bridge ports and to the external interface, but when they come back from a reflective relay, we don&#8217;t deliver them again. Since we know all the MAC addresses, the macvlan bridge mode does not require learning or STP like the bridge module does. </p>
<p> <code>phys:</code> an already existing interface specified by the <code>lxc.network.link</code> is assigned to the container.</p>
<dt><code>lxc.network.flags</code></p>
<dd>specify an action to do for the network. </p>
<p> <code>up:</code> activates the interface.</p>
<dt><code>lxc.network.link</code></p>
<dd>specify the interface to be used for real network traffic.</p>
<dt><code>lxc.network.mtu</code></p>
<dd>specify the maximum transfer unit for this interface.</p>
<dt><code>lxc.network.name</code></p>
<dd>the interface name is dynamically allocated, but if another name is needed because the configuration files being used by the container use a generic name, eg. eth0, this option will rename the interface in the container.</p>
<dt><code>lxc.network.hwaddr</code></p>
<dd>the interface mac address is dynamically allocated by default to the virtual interface, but in some cases, this is needed to resolve a mac address conflict or to always have the same link-local ipv6 address. Any &quot;x&quot; in address will be replaced by random value, this allows setting hwaddr templates.</p>
<dt><code>lxc.network.ipv4</code></p>
<dd>specify the ipv4 address to assign to the virtualized interface. Several lines specify several ipv4 addresses. The address is in format x.y.z.t/m, eg. 192.168.1.123/24. The broadcast address should be specified on the same line, right after the ipv4 address.</p>
<dt><code>lxc.network.ipv4.gateway</code></p>
<dd>specify the ipv4 address to use as the gateway inside the container. The address is in format x.y.z.t, eg. 192.168.1.123. Can also have the special value <code>auto</code>, which means to take the primary address from the bridge interface (as specified by the <code>lxc.network.link</code> option) and use that as the gateway. <code>auto</code> is only available when using the <code>veth</code> and <code>macvlan</code> network types.</p>
<dt><code>lxc.network.ipv6</code></p>
<dd>specify the ipv6 address to assign to the virtualized interface. Several lines specify several ipv6 addresses. The address is in format x::y/m, eg. 2003:db8:1:0:214:1234:fe0b:3596/64</p>
<dt><code>lxc.network.ipv6.gateway</code></p>
<dd>specify the ipv6 address to use as the gateway inside the container. The address is in format x::y, eg. 2003:db8:1:0::1 Can also have the special value <code>auto</code>, which means to take the primary address from the bridge interface (as specified by the <code>lxc.network.link</code> option) and use that as the gateway. <code>auto</code> is only available when using the <code>veth</code> and <code>macvlan</code> network types.</p>
<dt><code>lxc.network.script.up</code></p>
<dd>add a configuration option to specify a script to be executed after creating and configuring the network used from the host side. The following arguments are passed to the script: container name and config section name (net) Additional arguments depend on the config section employing a script hook; the following are used by the network system: execution context (up), network type (empty/veth/macvlan/phys), Depending on the network type, other arguments may be passed: veth/macvlan/phys. And finally (host-sided) device name. </p>
<p> Standard output from the script is logged at debug level. Standard error is not logged, but can be captured by the hook redirecting its standard error to standard output.</p>
<dt><code>lxc.network.script.down</code></p>
<dd>add a configuration option to specify a script to be executed before destroying the network used from the host side. The following arguments are passed to the script: container name and config section name (net) Additional arguments depend on the config section employing a script hook; the following are used by the network system: execution context (down), network type (empty/veth/macvlan/phys), Depending on the network type, other arguments may be passed: veth/macvlan/phys. And finally (host-sided) device name. </p>
<p> Standard output from the script is logged at debug level. Standard error is not logged, but can be captured by the hook redirecting its standard error to standard output.</dl>
<h3>New Pseudo Tty Instance (Devpts)</h3>
<p>For stricter isolation the container can have its own private instance of the pseudo tty.</p>
<dl>
<dt><code>lxc.pts</code></p>
<dd>If set, the container will have a new pseudo tty instance, making this private to it. The value specifies the maximum number of pseudo ttys allowed for a pts instance (this limitation is not implemented yet).</dl>
<h3>Container System Console</h3>
<p>If the container is configured with a root filesystem and the inittab file is setup to use the console, you may want to specify where the output of this console goes.</p>
<dl>
<dt><code>lxc.console.logfile</code></p>
<dd>Specify a path to a file where the console output will be written.</p>
<dt><code>lxc.console</code></p>
<dd>Specify a path to a device to which the console will be attached. The keyword &#8216;none&#8217; will simply disable the console. This is dangerous once if have a rootfs with a console device file where the application can write, the messages will fall in the host.</dl>
<h3>Console Through The Ttys</h3>
<p>This option is useful if the container is configured with a root filesystem and the inittab file is setup to launch a getty on the ttys. The option specifies the number of ttys to be available for the container. The number of gettys in the inittab file of the container should not be greater than the number of ttys specified in this option, otherwise the excess getty sessions will die and respawn indefinitely giving annoying messages on the console or in <i>/var/log/messages</i>.</p>
<dl>
<dt><code>lxc.tty</code></p>
<dd>Specify the number of tty to make available to the container.</dl>
<h3>Console Devices Location</h3>
<p>LXC consoles are provided through Unix98 PTYs created on the host and bind-mounted over the expected devices in the container. By default, they are bind-mounted over <i>/dev/console</i> and <i>/dev/ttyN</i>. This can prevent package upgrades in the guest. Therefore you can specify a directory location (under <i>/dev</i> under which LXC will create the files and bind-mount over them. These will then be symbolically linked to <i>/dev/console</i> and <i>/dev/ttyN</i>. A package upgrade can then succeed as it is able to remove and replace the symbolic links.</p>
<dl>
<dt><code>lxc.devttydir</code></p>
<dd>Specify a directory under <i>/dev</i> under which to create the container console devices.</dl>
<h3>/Dev Directory</h3>
<p>By default, lxc creates a few symbolic links (fd,stdin,stdout,stderr) in the container&#8217;s <i>/dev</i> directory but does not automatically create device node entries. This allows the container&#8217;s <i>/dev</i> to be set up as needed in the container rootfs. If lxc.autodev is set to 1, then after mounting the container&#8217;s rootfs LXC will mount a fresh tmpfs under <i>/dev</i> (limited to 500k) and fill in a minimal set of initial devices. This is generally required when starting a container containing a &quot;systemd&quot; based &quot;init&quot; but may be optional at other times. Additional devices in the containers /dev directory may be created through the use of the <code>lxc.hook.autodev</code> hook.</p>
<dl>
<dt><code>lxc.autodev</code></p>
<dd>Set this to 1 to have LXC mount and populate a minimal <i>/dev</i> when starting the container.</dl>
<h3>Enable Kmsg Symlink</h3>
<p>Enable creating /dev/kmsg as symlink to /dev/console. This defaults to 1.</p>
<dl>
<dt><code>lxc.kmsg</code></p>
<dd>Set this to 0 to disable /dev/kmsg symlinking.</dl>
<h3>Mount Points</h3>
<p>The mount points section specifies the different places to be mounted. These mount points will be private to the container and won&#8217;t be visible by the processes running outside of the container. This is useful to mount /etc, /var or /home for examples. </p>
<p> NOTE &#8211; LXC will generally ensure that mount targets and relative bind-mount sources are properly confined under the container root, to avoid attacks involving over-mounting host directories and files. (Symbolic links in absolute mount sources are ignored) However, if the container configuration first mounts a directory which is under the control of the container user, such as /home/joe, into the container at some <i>path</i>, and then mounts under <i>path</i>, then a TOCTTOU attack would be possible where the container user modifies a symbolic link under his home directory at just the right time.</p>
<dl>
<dt><code>lxc.mount</code></p>
<dd>specify a file location in the <i>fstab</i> format, containing the mount information. The mount target location can and in most cases should be a relative path, which will become relative to the mounted container root. For instance, </p>
<pre>proc proc proc nodev,noexec,nosuid 0 0
.fi
Will mount a proc filesystem under the container's /proc,
regardless of where the root filesystem comes from. This
is resilient to block device backed filesystems as well as
container cloning.
Note that when mounting a filesystem from an
image file or block device the third field (fs_vfstype)
cannot be auto as with
<code><a href="//www.systutorials.com/docs/linux/man/8-mount/">mount</a></code>(8)
but must be explicitly specified.
<dt><code>lxc.mount.entry</code> <dd>specify a mount point corresponding to a line in the
fstab format.
Moreover lxc add two options to mount.
<code>optional</code> don't fail if mount does not work.
<code>create=dir</code> or <code>create=file</code>
to create dir (or file) when the point will be mounted.
<dt><code>lxc.mount.auto</code> <dd>specify which standard kernel file systems should be
automatically mounted. This may dramatically simplify
the configuration. The file systems are:
<dl><dt><dd><dl><dt>&bull;<dd><code>proc:mixed</code> (or <code>proc</code>):
mount <i>/proc</i> as read-write, but
remount <i>/proc/sys</i> and
<i>/proc/sysrq-trigger</i> read-only
for security / container isolation purposes.
<dt>&bull;<dd><code>proc:rw</code>: mount
<i>/proc</i> as read-write
<dt>&bull;<dd><code>sys:ro</code> (or <code>sys</code>):
mount <i>/sys</i> as read-only
for security / container isolation purposes.
<dt>&bull;<dd><code>sys:rw</code>: mount
<i>/sys</i> as read-write
<dt>&bull;<dd><code>cgroup:mixed</code>:
mount a tmpfs to <i>/sys/fs/cgroup</i>,
create directories for all hierarchies to which
the container is added, create subdirectories
there with the name of the cgroup, and bind-mount
the container's own cgroup into that directory.
The container will be able to write to its own
cgroup directory, but not the parents, since they
will be remounted read-only
<dt>&bull;<dd><code>cgroup:ro</code>: similar to
<code>cgroup:mixed</code>, but everything will
be mounted read-only.
<dt>&bull;<dd><code>cgroup:rw</code>: similar to
<code>cgroup:mixed</code>, but everything will
be mounted read-write. Note that the paths leading
up to the container's own cgroup will be writable,
but will not be a cgroup filesystem but just part
of the tmpfs of <i>/sys/fs/cgroup</i>
<dt>&bull;<dd><code>cgroup</code> (without specifier):
defaults to <code>cgroup:rw</code> if the
container retains the CAP_SYS_ADMIN capability,
<code>cgroup:mixed</code> otherwise.
<dt>&bull;<dd><code>cgroup-full:mixed</code>:
mount a tmpfs to <i>/sys/fs/cgroup</i>,
create directories for all hierarchies to which
the container is added, bind-mount the hierarchies
from the host to the container and make everything
read-only except the container's own cgroup. Note
that compared to <code>cgroup</code>, where
all paths leading up to the container's own cgroup
are just simple directories in the underlying
tmpfs, here
<i>/sys/fs/cgroup/$hierarchy</i>
will contain the host's full cgroup hierarchy,
albeit read-only outside the container's own cgroup.
This may leak quite a bit of information into the
container.
<dt>&bull;<dd><code>cgroup-full:ro</code>: similar to
<code>cgroup-full:mixed</code>, but everything
will be mounted read-only.
<dt>&bull;<dd><code>cgroup-full:rw</code>: similar to
<code>cgroup-full:mixed</code>, but everything
will be mounted read-write. Note that in this case,
the container may escape its own cgroup. (Note also
that if the container has CAP_SYS_ADMIN support
and can mount the cgroup filesystem itself, it may
do so anyway.)
<dt>&bull;<dd><code>cgroup-full</code> (without specifier):
defaults to <code>cgroup-full:rw</code> if the
container retains the CAP_SYS_ADMIN capability,
<code>cgroup-full:mixed</code> otherwise.
</dl></dl>
Note that if automatic mounting of the cgroup filesystem
is enabled, the tmpfs under
<i>/sys/fs/cgroup</i> will always be
mounted read-write (but for the <code>:mixed</code>
and <code>:ro</code> cases, the individual
hierarchies,
<i>/sys/fs/cgroup/$hierarchy</i>, will be
read-only). This is in order to work around a quirk in
Ubuntu's
<code><a href="//www.systutorials.com/docs/linux/man/8-mountall/">mountall</a></code>(8)
command that will cause containers to wait for user
input at boot if
<i>/sys/fs/cgroup</i> is mounted read-only
and the container can't remount it read-write due to a
lack of CAP_SYS_ADMIN.
Examples:
 lxc.mount.auto = proc sys cgroup
 lxc.mount.auto = proc:rw sys:rw cgroup-full:rw</pre>
</dl>
<h3>Root File System</h3>
<p>The root file system of the container can be different than that of the host system.</p>
<dl>
<dt><code>lxc.rootfs</code></p>
<dd>specify the root file system for the container. It can be an image file, a directory or a block device. If not specified, the container shares its root file system with the host.</p>
<dt><code>lxc.rootfs.mount</code></p>
<dd>where to recursively bind <code>lxc.rootfs</code> before pivoting. This is to ensure success of the <code><a href="/docs/linux/man/8-pivot_root/">pivot_root</a></code>(8) syscall. Any directory suffices, the default should generally work.</p>
<dt><code>lxc.rootfs.options</code></p>
<dd>extra mount options to use when mounting the rootfs.</p>
<dt><code>lxc.pivotdir</code></p>
<dd>where to pivot the original root file system under <code>lxc.rootfs</code>, specified relatively to that. The default is <i>mnt</i>. It is created if necessary, and also removed after unmounting everything from it during container setup.</dl>
<h3>Control Group</h3>
<p>The control group section contains the configuration for the different subsystem. <code>lxc</code> does not check the correctness of the subsystem name. This has the disadvantage of not detecting configuration errors until the container is started, but has the advantage of permitting any future subsystem.</p>
<dl>
<dt><code>lxc.cgroup.[subsystem name]</code></p>
<dd>specify the control group value to be set. The subsystem name is the literal name of the control group subsystem. The permitted names and the syntax of their values is not dictated by LXC, instead it depends on the features of the Linux kernel running at the time the container is started, eg. <code>lxc.cgroup.cpuset.cpus</code></dl>
<h3>Capabilities</h3>
<p>The capabilities can be dropped in the container if this one is run as root.</p>
<dl>
<dt><code>lxc.cap.drop</code></p>
<dd>Specify the capability to be dropped in the container. A single line defining several capabilities with a space separation is allowed. The format is the lower case of the capability definition without the &quot;CAP_&quot; prefix, eg. CAP_SYS_MODULE should be specified as sys_module. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7). If used with no value, lxc will clear any drop capabilities specified up to this point.</p>
<dt><code>lxc.cap.keep</code></p>
<dd>Specify the capability to be kept in the container. All other capabilities will be dropped.</dl>
<h3>Apparmor Profile</h3>
<p>If lxc was compiled and installed with apparmor support, and the host system has apparmor enabled, then the apparmor profile under which the container should be run can be specified in the container configuration. The default is <code>lxc-container-default</code>.</p>
<dl>
<dt><code>lxc.aa_profile</code></p>
<dd>Specify the apparmor profile under which the container should be run. To specify that the container should be unconfined, use </p>
<pre>lxc.aa_profile = unconfined</pre>
</dl>
<h3>Selinux Context</h3>
<p>If lxc was compiled and installed with SELinux support, and the host system has SELinux enabled, then the SELinux context under which the container should be run can be specified in the container configuration. The default is <code>unconfined_t</code>, which means that lxc will not attempt to change contexts. See /usr/share/lxc/selinux/lxc.te for an example policy and more information.</p>
<dl>
<dt><code>lxc.se_context</code></p>
<dd>Specify the SELinux context under which the container should be run or <code>unconfined_t</code>. For example </p>
<pre>lxc.se_context = system_u:system_r:lxc_t:s0:c22</pre>
</dl>
<h3>Seccomp Configuration</h3>
<p>A container can be started with a reduced set of available system calls by loading a seccomp profile at startup. The seccomp configuration file must begin with a version number on the first line, a policy type on the second line, followed by the configuration. </p>
<p> Versions 1 and 2 are currently supported. In version 1, the policy is a simple whitelist. The second line therefore must read &quot;whitelist&quot;, with the rest of the file containing one (numeric) sycall number per line. Each syscall number is whitelisted, while every unlisted number is blacklisted for use in the container </p>
<p> In version 2, the policy may be blacklist or whitelist, supports per-rule and per-policy default actions, and supports per-architecture system call resolution from textual names. </p>
<p> An example blacklist policy, in which all system calls are allowed except for mknod, which will simply do nothing and return 0 (success), looks like: </p>
<pre>2
blacklist
mknod errno 0
.fi
<dl><dt><code>lxc.seccomp</code> <dd>Specify a file containing the seccomp configuration to
load before the container starts.
</dl></pre>
<h3>Uid Mappings</h3>
<p>A container can be started in a private user namespace with user and group id mappings. For instance, you can map userid 0 in the container to userid 200000 on the host. The root user in the container will be privileged in the container, but unprivileged on the host. Normally a system container will want a range of ids, so you would map, for instance, user and group ids 0 through 20,000 in the container to the ids 200,000 through 220,000.</p>
<dl>
<dt><code>lxc.id_map</code></p>
<dd>Four values must be provided. First a character, either &#8216;u&#8217;, or &#8216;g&#8217;, to specify whether user or group ids are being mapped. Next is the first userid as seen in the user namespace of the container. Next is the userid as seen on the host. Finally, a range indicating the number of consecutive ids to map.</dl>
<h3>Container Hooks</h3>
<p>Container hooks are programs or scripts which can be executed at various times in a container&#8217;s lifetime. </p>
<p> When a container hook is executed, information is passed both as command line arguments and through environment variables. The arguments are:</p>
<dl>
<dt>&bull;</p>
<dd>Container name.</p>
<dt>&bull;</p>
<dd>Section (always &#8216;lxc&#8217;).</p>
<dt>&bull;</p>
<dd>The hook type (i.e. &#8216;clone&#8217; or &#8216;pre-mount&#8217;).</p>
<dt>&bull;</p>
<dd>Additional arguments In the case of the clone hook, any extra arguments passed to lxc-clone will appear as further arguments to the hook.</dl>
<p> The following environment variables are set:</p>
<dl>
<dt>&bull;</p>
<dd>LXC_NAME: is the container&#8217;s name.</p>
<dt>&bull;</p>
<dd>LXC_ROOTFS_MOUNT: the path to the mounted root filesystem.</p>
<dt>&bull;</p>
<dd>LXC_CONFIG_FILE: the path to the container configuration file.</p>
<dt>&bull;</p>
<dd>LXC_SRC_NAME: in the case of the clone hook, this is the original container&#8217;s name.</p>
<dt>&bull;</p>
<dd>LXC_ROOTFS_PATH: this is the lxc.rootfs entry for the container. Note this is likely not where the mounted rootfs is to be found, use LXC_ROOTFS_MOUNT for that.</dl>
<p> Standard output from the hooks is logged at debug level. Standard error is not logged, but can be captured by the hook redirecting its standard error to standard output.</p>
<dl>
<dt><code>lxc.hook.pre-start</code></p>
<dd>A hook to be run in the host&#8217;s namespace before the container ttys, consoles, or mounts are up.</p>
<dt><code>lxc.hook.pre-mount</code></p>
<dd>A hook to be run in the container&#8217;s fs namespace but before the rootfs has been set up. This allows for manipulation of the rootfs, i.e. to mount an encrypted filesystem. Mounts done in this hook will not be reflected on the host (apart from mounts propagation), so they will be automatically cleaned up when the container shuts down.</p>
<dt><code>lxc.hook.mount</code></p>
<dd>A hook to be run in the container&#8217;s namespace after mounting has been done, but before the pivot_root.</p>
<dt><code>lxc.hook.autodev</code></p>
<dd>A hook to be run in the container&#8217;s namespace after mounting has been done and after any mount hooks have run, but before the pivot_root, if <code>lxc.autodev</code> == 1. The purpose of this hook is to assist in populating the /dev directory of the container when using the autodev option for systemd based containers. The container&#8217;s /dev directory is relative to the ${<code>LXC_ROOTFS_MOUNT</code>} environment variable available when the hook is run.</p>
<dt><code>lxc.hook.start</code></p>
<dd>A hook to be run in the container&#8217;s namespace immediately before executing the container&#8217;s init. This requires the program to be available in the container.</p>
<dt><code>lxc.hook.post-stop</code></p>
<dd>A hook to be run in the host&#8217;s namespace after the container has been shut down.</p>
<dt><code>lxc.hook.clone</code></p>
<dd>A hook to be run when the container is cloned to a new one. See <code><a href="/docs/linux/man/1-lxc-clone/">lxc-clone</a></code>(1) for more information.</dl>
<h3>Container Hooks Environment Variables</h3>
<p>A number of environment variables are made available to the startup hooks to provide configuration information and assist in the functioning of the hooks. Not all variables are valid in all contexts. In particular, all paths are relative to the host system and, as such, not valid during the <code>lxc.hook.start</code> hook.</p>
<dl>
<dt><code>LXC_NAME</code></p>
<dd>The LXC name of the container. Useful for logging messages in common log environments. [<code>-n</code>]</p>
<dt><code>LXC_CONFIG_FILE</code></p>
<dd>Host relative path to the container configuration file. This gives the container to reference the original, top level, configuration file for the container in order to locate any additional configuration information not otherwise made available. [<code>-f</code>]</p>
<dt><code>LXC_CONSOLE</code></p>
<dd>The path to the console output of the container if not NULL. [<code>-c</code>] [<code>lxc.console</code>]</p>
<dt><code>LXC_CONSOLE_LOGPATH</code></p>
<dd>The path to the console log output of the container if not NULL. [<code>-L</code>]</p>
<dt><code>LXC_ROOTFS_MOUNT</code></p>
<dd>The mount location to which the container is initially bound. This will be the host relative path to the container rootfs for the container instance being started and is where changes should be made for that instance. [<code>lxc.rootfs.mount</code>]</p>
<dt><code>LXC_ROOTFS_PATH</code></p>
<dd>The host relative path to the container root which has been mounted to the rootfs.mount location. [<code>lxc.rootfs</code>]</dl>
<h3>Logging</h3>
<p>Logging can be configured on a per-container basis. By default, depending upon how the lxc package was compiled, container startup is logged only at the ERROR level, and logged to a file named after the container (with &#8216;.log&#8217; appended) either under the container path, or under /var/log/lxc. </p>
<p> Both the default log level and the log file can be specified in the container configuration file, overriding the default behavior. Note that the configuration file entries can in turn be overridden by the command line options to <code>lxc-start</code>.</p>
<dl>
<dt><code>lxc.loglevel</code></p>
<dd>The level at which to log. The log level is an integer in the range of 0..8 inclusive, where a lower number means more verbose debugging. In particular 0 = trace, 1 = debug, 2 = info, 3 = notice, 4 = warn, 5 = error, 6 = critical, 7 = alert, and 8 = fatal. If unspecified, the level defaults to 5 (error), so that only errors and above are logged. </p>
<p> Note that when a script (such as either a hook script or a network interface up or down script) is called, the script&#8217;s standard output is logged at level 1, debug.</p>
<dt><code>lxc.logfile</code></p>
<dd>The file to which logging info should be written.</dl>
<h3>Autostart</h3>
<p>The autostart options support marking which containers should be auto-started and in what order. These options may be used by LXC tools directly or by external tooling provided by the distributions.</p>
<dl>
<dt><code>lxc.start.auto</code></p>
<dd>Whether the container should be auto-started. Valid values are 0 (off) and 1 (on).</p>
<dt><code>lxc.start.delay</code></p>
<dd>How long to wait (in seconds) after the container is started before starting the next one.</p>
<dt><code>lxc.start.order</code></p>
<dd>An integer used to sort the containers when auto-starting a series of containers at once.</p>
<dt><code>lxc.group</code></p>
<dd>A multi-value key (can be used multiple times) to put the container in a container group. Those groups can then be used (amongst other things) to start a series of related containers.</dl>
<h3>Autostart And System Boot</h3>
<p>Each container can be part of any number of groups or no group at all. Two groups are special. One is the NULL group, i.e. the container does not belong to any group. The other group is the &quot;onboot&quot; group. </p>
<p> When the system boots with the LXC service enabled, it will first attempt to boot any containers with lxc.start.auto == 1 that is a member of the &quot;onboot&quot; group. The startup will be in order of lxc.start.order. If an lxc.start.delay has been specified, that delay will be honored before attempting to start the next container to give the current container time to begin initialization and reduce overloading the host system. After starting the members of the &quot;onboot&quot; group, the LXC system will proceed to boot containers with lxc.start.auto == 1 which are not members of any group (the NULL group) and proceed as with the onboot group.</p>
<h2>Examples</h2>
<p>In addition to the few examples given below, you will find some other examples of configuration file in /usr/share/doc/lxc-1.0.11/examples</p>
<h3>Network</h3>
<p>This configuration sets up a container to use a veth pair device with one side plugged to a bridge br0 (which has been configured before on the system by the administrator). The virtual network device visible in the container is renamed to eth0. </p>
<pre> lxc.utsname = myhostname
 lxc.network.type = veth
 lxc.network.flags = up
 lxc.network.link = br0
 lxc.network.name = eth0
 lxc.network.hwaddr = 4a:49:43:49:79:bf
 lxc.network.ipv4 = 10.2.3.5/24 10.2.3.255
 lxc.network.ipv6 = 2003:db8:1:0:214:1234:fe0b:3597</pre>
<h3>Uid/Gid Mapping</h3>
<p>This configuration will map both user and group ids in the range 0-9999 in the container to the ids 100000-109999 on the host. </p>
<pre> lxc.id_map = u 0 100000 10000
 lxc.id_map = g 0 100000 10000</pre>
<h3>Control Group</h3>
<p>This configuration will setup several control groups for the application, cpuset.cpus restricts usage of the defined cpu, cpus.share prioritize the control group, devices.allow makes usable the specified devices. </p>
<pre> lxc.cgroup.cpuset.cpus = 0,1
 lxc.cgroup.cpu.shares = 1234
 lxc.cgroup.devices.deny = a
 lxc.cgroup.devices.allow = c 1:3 rw
 lxc.cgroup.devices.allow = b 8:0 rw</pre>
<h3>Complex Configuration</h3>
<p>This example show a complex configuration making a complex network stack, using the control groups, setting a new hostname, mounting some locations and a changing root file system. </p>
<pre> lxc.utsname = complex
 lxc.network.type = veth
 lxc.network.flags = up
 lxc.network.link = br0
 lxc.network.hwaddr = 4a:49:43:49:79:bf
 lxc.network.ipv4 = 10.2.3.5/24 10.2.3.255
 lxc.network.ipv6 = 2003:db8:1:0:214:1234:fe0b:3597
 lxc.network.ipv6 = 2003:db8:1:0:214:5432:feab:3588
 lxc.network.type = macvlan
 lxc.network.flags = up
 lxc.network.link = eth0
 lxc.network.hwaddr = 4a:49:43:49:79:bd
 lxc.network.ipv4 = 10.2.3.4/24
 lxc.network.ipv4 = 192.168.10.125/24
 lxc.network.ipv6 = 2003:db8:1:0:214:1234:fe0b:3596
 lxc.network.type = phys
 lxc.network.flags = up
 lxc.network.link = dummy0
 lxc.network.hwaddr = 4a:49:43:49:79:ff
 lxc.network.ipv4 = 10.2.3.6/24
 lxc.network.ipv6 = 2003:db8:1:0:214:1234:fe0b:3297
 lxc.cgroup.cpuset.cpus = 0,1
 lxc.cgroup.cpu.shares = 1234
 lxc.cgroup.devices.deny = a
 lxc.cgroup.devices.allow = c 1:3 rw
 lxc.cgroup.devices.allow = b 8:0 rw
 lxc.mount = /etc/fstab.complex
 lxc.mount.entry = /lib /root/myrootfs/lib none ro,bind 0 0
 lxc.rootfs = /mnt/rootfs.complex
 lxc.cap.drop = sys_module mknod setuid net_raw
 lxc.cap.drop = mac_override</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1), <code><a href="/docs/linux/man/8-pivot_root/">pivot_root</a></code>(8), <i><a href="/docs/linux/man/5-fstab/">fstab</a></i>(5), <i><a href="/docs/linux/man/7-capabilities/">capabilities</a></i>(7)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt;</p>
