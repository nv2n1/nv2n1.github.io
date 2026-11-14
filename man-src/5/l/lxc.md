---
title: "lxc(5)"
name: "lxc"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lxc/"
description: "lxc.conf – linux container configuration file"
---

<p>lxc.conf &#8211; linux container configuration file</p>
<h2>Description</h2>
<p>The linux containers (<code>lxc</code>) are always created before being used. This creation defines a set of system resources to be virtualized / isolated when a process is using the container. By default, the pids, sysv ipc and mount points are virtualized and isolated. The other system resources are shared across containers, until they are explicitly defined in the configuration file. For example, if there is no network configuration, the network will be shared between the creator of the container and the container itself, but if the network is specified, a new network stack is created for the container and the container can no longer use the network of its ancestor. </p>
<p> The configuration file defines the different system resources to be assigned for the container. At present, the utsname, the network, the mount points, the root file system and the control groups are supported. </p>
<p> Each option in the configuration file has the form <code>key = value</code> fitting in one line. The &#8216;#&#8217; character means the line is a comment.</p>
<h3>Hostname</h3>
<p>The utsname section defines the hostname to be set for the container. That means the container can set its own hostname without changing the one from the system. That makes the hostname private for the container.</p>
<dl>
<dt><code>lxc.utsname</code></p>
<dd>specify the hostname for the container</dl>
<h3>Network</h3>
<p>The network section defines how the network is virtualized in the container. The network virtualization acts at layer two. In order to use the network virtualization, parameters must be specified to define the network interfaces of the container. Several virtual interfaces can be assigned and used in a container even if the system has only one physical network interface.</p>
<dl>
<dt><code>lxc.network.type</code></p>
<dd>specify what kind of network virtualization to be used for the container. Each time a <code>lxc.network.type</code> field is found a new round of network configuration begins. In this way, several network virtualization types can be specified for the same container, as well as assigning several network interfaces for one container. The different virtualization types can be: </p>
<p> <code>empty:</code> will create only the loopback interface. </p>
<p> <code>veth:</code> a peer network device is created with one side assigned to the container and the other side is attached to a bridge specified by the <code>lxc.network.link</code>. If the bridge is not specified, then the veth pair device will be created but not attached to any bridge. Otherwise, the bridge has to be setup before on the system, <code>lxc</code> won&#8217;t handle any configuration outside of the container. By default <code>lxc</code> choose a name for the network device belonging to the outside of the container, this name is handled by <code>lxc</code>, but if you wish to handle this name yourself, you can tell <code>lxc</code> to set a specific name with the <code>lxc.network.veth.pair</code> option. </p>
<p> <code>vlan:</code> a vlan interface is linked with the interface specified by the <code>lxc.network.link</code> and assigned to the container. The vlan identifier is specified with the option <code>lxc.network.vlan.id</code>. </p>
<p> <code>macvlan:</code> a macvlan interface is linked with the interface specified by the <code>lxc.network.link</code> and assigned to the container. <code>lxc.network.macvlan.mode</code> specifies the mode the macvlan will use to communicate between different macvlan on the same upper device. The accepted modes are <code>private</code>, the device never communicates with any other device on the same upper_dev (default), <code>vepa</code>, the new Virtual Ethernet Port Aggregator (VEPA) mode, it assumes that the adjacent bridge returns all frames where both source and destination are local to the macvlan port, i.e. the bridge is set up as a reflective relay. Broadcast frames coming in from the upper_dev get flooded to all macvlan interfaces in VEPA mode, local frames are not delivered locallay, or <code>bridge</code>, it provides the behavior of a simple bridge between different macvlan interfaces on the same port. Frames from one interface to another one get delivered directly and are not sent out externally. Broadcast frames get flooded to all other bridge ports and to the external interface, but when they come back from a reflective relay, we don&#8217;t deliver them again. Since we know all the MAC addresses, the macvlan bridge mode does not require learning or STP like the bridge module does. </p>
<p> <code>phys:</code> an already existing interface specified by the <code>lxc.network.link</code> is assigned to the container.</p>
<dt><code>lxc.network.flags</code></p>
<dd>specify an action to do for the network. </p>
<p> <code>up:</code> activates the interface.</p>
<dt><code>lxc.network.link</code></p>
<dd>specify the interface to be used for real network traffic.</p>
<dt><code>lxc.network.name</code></p>
<dd>the interface name is dynamically allocated, but if another name is needed because the configuration files being used by the container use a generic name, eg. eth0, this option will rename the interface in the container.</p>
<dt><code>lxc.network.hwaddr</code></p>
<dd>the interface mac address is dynamically allocated by default to the virtual interface, but in some cases, this is needed to resolve a mac address conflict or to always have the same link-local ipv6 address</p>
<dt><code>lxc.network.ipv4</code></p>
<dd>specify the ipv4 address to assign to the virtualized interface. Several lines specify several ipv4 addresses. The address is in format x.y.z.t/m, eg. 192.168.1.123/24.</p>
<dt><code>lxc.network.ipv6</code></p>
<dd>specify the ipv6 address to assign to the virtualized interface. Several lines specify several ipv6 addresses. The address is in format x::y/m, eg. 2003:db8:1:0:214:1234:fe0b:3596/64</dl>
<h3>New Pseudo Tty Instance (Devpts)</h3>
<p>For stricter isolation the container can have its own private instance of the pseudo tty.</p>
<dl>
<dt><code>lxc.pts</code></p>
<dd>If set, the container will have a new pseudo tty instance, making this private to it. The value specifies the maximum number of pseudo ttys allowed for a pts instance (this limitation is not implemented yet).</dl>
<h3>Console Through The Ttys</h3>
<p>If the container is configured with a root filesystem and the inittab file is setup to launch a getty on the ttys. This option will specify the number of ttys to be available for the container. The number of getty in the inittab file of the container should not be greater than the number of ttys specified in this configuration file, otherwise the excess getty sessions will die and respawn indefinitly giving annoying messages on the console.</p>
<dl>
<dt><code>lxc.tty</code></p>
<dd>Specify the number of tty to make available to the container.</dl>
<h3>Mount Points</h3>
<p>The mount points section specifies the different places to be mounted. These mount points will be private to the container and won&#8217;t be visible by the processes running outside of the container. This is useful to mount /etc, /var or /home for examples.</p>
<dl>
<dt><code>lxc.mount</code></p>
<dd>specify a file location in the <i>fstab</i> format, containing the mount informations.</p>
<dt><code>lxc.mount.entry</code></p>
<dd>specify a mount point corresponding to a line in the fstab format.</dl>
<h3>Root File System</h3>
<p>The root file system is the location where the container will chroot.</p>
<dl>
<dt><code>lxc.rootfs</code></p>
<dd>specify a file location containing the new file tree for a root file system.</dl>
<h3>Control Group</h3>
<p>The control group section contains the configuration for the different subsystem. <code>lxc</code> does not check the correctness of the subsystem name. This has the disadvantage of not detecting configuration errors until the container is started, but has the advantage of permitting any future subsystem.</p>
<dl>
<dt><code>lxc.cgroup.[subsystem name]</code></p>
<dd>specify the control group value to be set. The subsystem name is the literal name of the control group subsystem. The permitted names and the syntax of their values is not dictated by LXC, instead it depends on the features of the Linux kernel running at the time the container is started, eg. <code>lxc.cgroup.cpuset.cpus</code></dl>
<h3>Capabilities</h3>
<p>The capabilities can be dropped in the container if this one is run as root.</p>
<dl>
<dt><code>lxc.cap.drop</code></p>
<dd>Specify the capability to be dropped in the container. A single line defining several capabilities with a space separation is allowed. The format is the lower case of the capability definition without the &quot;CAP_&quot; prefix, eg. CAP_SYS_MODULE should be specified as sys_module. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7),</dl>
<h2>Examples</h2>
<h3>Network</h3>
<p>This configuration sets up a container to use a veth pair device with one side plugged to a bridge br0 (which has been configured before on the system by the administrator). The virtual network device visible in the container is renamed to eth0.</p>
<dl>
<dt><code>lxc.utsname = myhostname</code></p>
<dd>
<dt><code>lxc.network.type = veth</code></p>
<dd>
<dt><code>lxc.network.flags = up</code></p>
<dd>
<dt><code>lxc.network.link = br0</code></p>
<dd>
<dt><code>lxc.network.name = eth0</code></p>
<dd>
<dt><code>lxc.network.hwaddr = 4a:49:43:49:79:bf</code></p>
<dd>
<dt><code>lxc.network.ipv4 = 1.2.3.5/24</code></p>
<dd>
<dt><code>lxc.network.ipv6 = 2003:db8:1:0:214:1234:fe0b:3597</code></p>
<dd></dl>
<h3>Control Group</h3>
<p>This configuration will setup several control groups for the application, cpuset.cpus restricts usage of the defined cpu, cpus.share prioritize the control group, devices.allow makes usable the specified devices.</p>
<dl>
<dt><code>lxc.cgroup.cpuset.cpus = 0,1</code></p>
<dd>
<dt><code>lxc.cgroup.cpu.shares = 1234</code></p>
<dd>
<dt><code>lxc.cgroup.devices.deny = a</code></p>
<dd>
<dt><code>lxc.cgroup.devices.allow = c 1:3 rw</code></p>
<dd>
<dt><code>lxc.cgroup.devices.allow = b 8:0 rw</code></p>
<dd></dl>
<h3>Complex Configuration</h3>
<p>This example show a complex configuration making a complex network stack, using the control groups, setting a new hostname, mounting some locations and a changing the root file system.</p>
<dl>
<dt><code>lxc.utsname = complex</code></p>
<dd>
<dt><code>lxc.network.type = veth</code></p>
<dd>
<dt><code>lxc.network.flags = up</code></p>
<dd>
<dt><code>lxc.network.link = br0</code></p>
<dd>
<dt><code>lxc.network.hwaddr = 4a:49:43:49:79:bf</code></p>
<dd>
<dt><code>lxc.network.ipv4 = 1.2.3.5/24</code></p>
<dd>
<dt><code>lxc.network.ipv6 = 2003:db8:1:0:214:1234:fe0b:3597</code></p>
<dd>
<dt><code>lxc.network.ipv6 = 2003:db8:1:0:214:5432:feab:3588</code></p>
<dd>
<dt><code>lxc.network.type = macvlan</code></p>
<dd>
<dt><code>lxc.network.flags = up</code></p>
<dd>
<dt><code>lxc.network.link = eth0</code></p>
<dd>
<dt><code>lxc.network.hwaddr = 4a:49:43:49:79:bd</code></p>
<dd>
<dt><code>lxc.network.ipv4 = 1.2.3.4/24</code></p>
<dd>
<dt><code>lxc.network.ipv4 = 192.168.10.125/24</code></p>
<dd>
<dt><code>lxc.network.ipv6 = 2003:db8:1:0:214:1234:fe0b:3596</code></p>
<dd>
<dt><code>lxc.network.type = phys</code></p>
<dd>
<dt><code>lxc.network.flags = up</code></p>
<dd>
<dt><code>lxc.network.link = dummy0</code></p>
<dd>
<dt><code>lxc.network.hwaddr = 4a:49:43:49:79:ff</code></p>
<dd>
<dt><code>lxc.network.ipv4 = 1.2.3.6/24</code></p>
<dd>
<dt><code>lxc.network.ipv6 = 2003:db8:1:0:214:1234:fe0b:3297</code></p>
<dd>
<dt><code>lxc.cgroup.cpuset.cpus = 0,1</code></p>
<dd>
<dt><code>lxc.cgroup.cpu.shares = 1234</code></p>
<dd>
<dt><code>lxc.cgroup.devices.deny = a</code></p>
<dd>
<dt><code>lxc.cgroup.devices.allow = c 1:3 rw</code></p>
<dd>
<dt><code>lxc.cgroup.devices.allow = b 8:0 rw</code></p>
<dd>
<dt><code>lxc.mount = /etc/fstab.complex</code></p>
<dd>
<dt><code>lxc.mount.entry = /lib /root/myrootfs/lib none ro,bind 0 0</code></p>
<dd>
<dt><code>lxc.rootfs = /mnt/rootfs.complex</code></p>
<dd>
<dt><code>lxc.cap.drop = sys_module mknod setuid net_raw</code></p>
<dd>
<dt><code>lxc.cap.drop = mac_override</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1), <code><a href="/docs/linux/man/8-pivot_root/">pivot_root</a></code>(8), <i><a href="/docs/linux/man/5-fstab/">fstab</a></i>(5)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lxc/">lxc</a></code>(1), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ps/">lxc-ps</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt;</p>
