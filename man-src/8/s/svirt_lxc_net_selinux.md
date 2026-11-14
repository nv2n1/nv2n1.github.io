---
title: "svirt_lxc_net_selinux(8)"
name: "svirt_lxc_net_selinux"
section: "8"
letter: "s"
url: "/docs/linux/man/8-svirt_lxc_net_selinux/"
description: "svirt_lxc_net_selinux – Security Enhanced Linux Policy for the svirt_lxc_net processes"
---

<p>svirt_lxc_net_selinux &#8211; Security Enhanced Linux Policy for the svirt_lxc_net processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the svirt_lxc_net processes via flexible mandatory access control. The svirt_lxc_net processes execute with the svirt_lxc_net_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep svirt_lxc_net_t</code> </p>
<h2>Entrypoints</h2>
<p>The svirt_lxc_net_t SELinux type can be entered via the <code>file_type</code> file type. </p>
<p> The default entrypoint paths for the svirt_lxc_net_t domain are the following: </p>
<p> all files on the system</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux svirt_lxc_net policy is very flexible allowing users to setup their svirt_lxc_net processes in as secure a method as possible. </p>
<p> The following process types are defined for svirt_lxc_net: </p>
<p> svirt_lxc_net_t</code> </p>
<p> Note: <code>semanage permissive -a svirt_lxc_net_t</code> can be used to make the process type svirt_lxc_net_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>MCS Constrained</h2>
<p>The SELinux process type svirt_lxc_net_t is an MCS (Multi Category Security) constrained type. Sometimes this separation is referred to as sVirt. These types are usually used for securing multi-tenant environments, such as virtualization, containers or separation of users. The tools used to launch MCS types, pick out a different MCS label for each process group. </p>
<p> For example one process might be launched with svirt_lxc_net_t:s0:c1,c2, and another process launched with svirt_lxc_net_t:s0:c3,c4. The SELinux kernel only allows these processes can only write to content with a matching MCS label, or a MCS Label of s0. A process running with the MCS level of s0:c1,c2 is not allowed to write to content with the MCS label of s0:c3,c4</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. svirt_lxc_net policy is extremely flexible and has several booleans that allow you to manipulate the policy and run svirt_lxc_net with the tightest access possible. </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
<p> If you want to deny any process from ptracing or debugging any other processes, you must turn on the deny_ptrace boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_ptrace 1</code> </p>
<p> If you want to allow all domains to use other domains file descriptors, you must turn on the domain_fd_use boolean. Enabled by default. </p>
<p> <code>setsebool -P domain_fd_use 1</code> </p>
<p> If you want to allow all domains to have the kernel load modules, you must turn on the domain_kernel_load_modules boolean. Disabled by default. </p>
<p> <code>setsebool -P domain_kernel_load_modules 1</code> </p>
<p> If you want to allow all domains to execute in fips_mode, you must turn on the fips_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P fips_mode 1</code> </p>
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code> </p>
<p> If you want to allow confined applications to run with kerberos, you must turn on the kerberos_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P kerberos_enabled 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to allow sandbox containers to use all capabilities, you must turn on the virt_sandbox_use_all_caps boolean. Enabled by default. </p>
<p> <code>setsebool -P virt_sandbox_use_all_caps 1</code> </p>
<p> If you want to allow sandbox containers to send audit messages, you must turn on the virt_sandbox_use_audit boolean. Enabled by default. </p>
<p> <code>setsebool -P virt_sandbox_use_audit 1</code> </p>
<p> If you want to allow sandbox containers manage fuse files, you must turn on the virt_sandbox_use_fusefs boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_sandbox_use_fusefs 1</code> </p>
<p> If you want to allow sandbox containers to use mknod system calls, you must turn on the virt_sandbox_use_mknod boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_sandbox_use_mknod 1</code> </p>
<p> If you want to allow sandbox containers to use netlink system calls, you must turn on the virt_sandbox_use_netlink boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_sandbox_use_netlink 1</code> </p>
<p> If you want to allow sandbox containers to use sys_admin system calls, for example mount, you must turn on the virt_sandbox_use_sys_admin boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_sandbox_use_sys_admin 1</code> </p>
<p> If you want to allow confined virtual guests to manage nfs files, you must turn on the virt_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_nfs 1</code> </p>
<p> If you want to allow confined virtual guests to manage cifs files, you must turn on the virt_use_samba boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_samba 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type svirt_lxc_net_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>cgroup_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/sys/fs/cgroup</p>
<p> <code>cifs_t</code> </p>
<p> <code>fusefs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user/[^/]*/gvfs</p>
<p> <code>hugetlbfs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/hugepages</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/lib/udev/devices/hugepages</p>
<p> <code>nfs_t</code> </p>
<p> <code>svirt_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.libvirt/qemu(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.cache/libvirt/qemu(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.config/libvirt/qemu(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.local/share/libvirt/boot(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.local/share/libvirt/images(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.local/share/gnome-boxes/images(/.*)?</p>
<p> <code>svirt_sandbox_file_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/kubelet(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/docker/vfs(/.*)?</p>
<p> <code>usermodehelper_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/sys/kernel/uevent_helper</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-svirt_lxc_net/">svirt_lxc_net</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
