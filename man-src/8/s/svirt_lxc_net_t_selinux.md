---
title: "svirt_lxc_net_t_selinux(8)"
name: "svirt_lxc_net_t_selinux"
section: "8"
letter: "s"
url: "/docs/linux/man/8-svirt_lxc_net_t_selinux/"
description: "virtd_selinux – Security Enhanced Linux Policy for the virtd processes"
---

<p>virtd_selinux &#8211; Security Enhanced Linux Policy for the virtd processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the virtd processes via flexible mandatory access control. The virtd processes execute with the virtd_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep virtd_t</code> </p>
<h2>Entrypoints</h2>
<p>The virtd_t SELinux type can be entered via the <code>virtd_exec_t</code> file type. </p>
<p> The default entrypoint paths for the virtd_t domain are the following: </p>
<p> /usr/bin/virt-who, /usr/sbin/libvirtd, /usr/bin/imgfac.py, /usr/sbin/virtlockd, /usr/share/vdsm/vdsm, /usr/bin/imagefactory, /usr/bin/nova-compute, /usr/share/vdsm/respawn, /usr/sbin/condor_vm-gahp, /usr/bin/vios-proxy-host, /usr/bin/vios-proxy-guest, /usr/share/vdsm/daemonAdapter, /usr/share/vdsm/supervdsmServer</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux virtd policy is very flexible allowing users to setup their virtd processes in as secure a method as possible. </p>
<p> The following process types are defined for virtd: </p>
<p> virt_qemu_ga_unconfined_t, virtd_lxc_t, virt_qmf_t, virt_qemu_ga_t, virt_bridgehelper_t, virtd_t</code> </p>
<p> Note: <code>semanage permissive -a virtd_t</code> can be used to make the process type virtd_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. virtd policy is extremely flexible and has several booleans that allow you to manipulate the policy and run virtd with the tightest access possible. </p>
<p> If you want to allow virtual processes to run as userdomains, you must turn on the virt_transition_userdomain boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_transition_userdomain 1</code> </p>
<p> If you want to allow confined virtual guests to manage nfs files, you must turn on the virt_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_nfs 1</code> </p>
<p> If you want to allow confined virtual guests to manage cifs files, you must turn on the virt_use_samba boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_samba 1</code> </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
<p> If you want to allow all daemons to write corefiles to /, you must turn on the daemons_dump_core boolean. Disabled by default. </p>
<p> <code>setsebool -P daemons_dump_core 1</code> </p>
<p> If you want to enable cluster mode for daemons, you must turn on the daemons_enable_cluster_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P daemons_enable_cluster_mode 1</code> </p>
<p> If you want to allow all daemons to use tcp wrappers, you must turn on the daemons_use_tcp_wrapper boolean. Disabled by default. </p>
<p> <code>setsebool -P daemons_use_tcp_wrapper 1</code> </p>
<p> If you want to allow all daemons the ability to read/write terminals, you must turn on the daemons_use_tty boolean. Disabled by default. </p>
<p> <code>setsebool -P daemons_use_tty 1</code> </p>
<p> If you want to deny user domains applications to map a memory region as both executable and writable, this is dangerous and the executable should be reported in bugzilla, you must turn on the deny_execmem boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_execmem 1</code> </p>
<p> If you want to deny any process from ptracing or debugging any other processes, you must turn on the deny_ptrace boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_ptrace 1</code> </p>
<p> If you want to deny any process from ptracing or debugging any other processes, you must turn on the deny_ptrace boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_ptrace 1</code> </p>
<p> If you want to deny any process from ptracing or debugging any other processes, you must turn on the deny_ptrace boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_ptrace 1</code> </p>
<p> If you want to allow all domains to use other domains file descriptors, you must turn on the domain_fd_use boolean. Enabled by default. </p>
<p> <code>setsebool -P domain_fd_use 1</code> </p>
<p> If you want to allow all domains to use other domains file descriptors, you must turn on the domain_fd_use boolean. Enabled by default. </p>
<p> <code>setsebool -P domain_fd_use 1</code> </p>
<p> If you want to allow all domains to use other domains file descriptors, you must turn on the domain_fd_use boolean. Enabled by default. </p>
<p> <code>setsebool -P domain_fd_use 1</code> </p>
<p> If you want to allow all domains to have the kernel load modules, you must turn on the domain_kernel_load_modules boolean. Disabled by default. </p>
<p> <code>setsebool -P domain_kernel_load_modules 1</code> </p>
<p> If you want to allow all domains to have the kernel load modules, you must turn on the domain_kernel_load_modules boolean. Disabled by default. </p>
<p> <code>setsebool -P domain_kernel_load_modules 1</code> </p>
<p> If you want to allow all domains to have the kernel load modules, you must turn on the domain_kernel_load_modules boolean. Disabled by default. </p>
<p> <code>setsebool -P domain_kernel_load_modules 1</code> </p>
<p> If you want to allow all domains to execute in fips_mode, you must turn on the fips_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P fips_mode 1</code> </p>
<p> If you want to allow all domains to execute in fips_mode, you must turn on the fips_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P fips_mode 1</code> </p>
<p> If you want to allow all domains to execute in fips_mode, you must turn on the fips_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P fips_mode 1</code> </p>
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code> </p>
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code> </p>
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code> </p>
<p> If you want to allow confined applications to run with kerberos, you must turn on the kerberos_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P kerberos_enabled 1</code> </p>
<p> If you want to control the ability to mmap a low area of the address space, as configured by /proc/sys/vm/mmap_min_addr, you must turn on the mmap_low_allowed boolean. Disabled by default. </p>
<p> <code>setsebool -P mmap_low_allowed 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to disable kernel module loading, you must turn on the secure_mode_insmod boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode_insmod 1</code> </p>
<p> If you want to boolean to determine whether the system permits loading policy, setting enforcing mode, and changing boolean values. Set this to true and you have to reboot to set it back, you must turn on the secure_mode_policyload boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode_policyload 1</code> </p>
<p> If you want to allow unconfined executables to make their heap memory executable. Doing this is a really bad idea. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla, you must turn on the selinuxuser_execheap boolean. Disabled by default. </p>
<p> <code>setsebool -P selinuxuser_execheap 1</code> </p>
<p> If you want to allow all unconfined executables to use libraries requiring text relocation that are not labeled textrel_shlib_t, you must turn on the selinuxuser_execmod boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_execmod 1</code> </p>
<p> If you want to allow unconfined executables to make their stack executable. This should never, ever be necessary. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla, you must turn on the selinuxuser_execstack boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_execstack 1</code> </p>
<p> If you want to allow confined virtual guests to use serial/parallel communication ports, you must turn on the virt_use_comm boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_comm 1</code> </p>
<p> If you want to allow confined virtual guests to use serial/parallel communication ports, you must turn on the virt_use_comm boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_comm 1</code> </p>
<p> If you want to allow confined virtual guests to use executable memory and executable stack, you must turn on the virt_use_execmem boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_execmem 1</code> </p>
<p> If you want to allow confined virtual guests to use executable memory and executable stack, you must turn on the virt_use_execmem boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_execmem 1</code> </p>
<p> If you want to allow confined virtual guests to read fuse files, you must turn on the virt_use_fusefs boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_fusefs 1</code> </p>
<p> If you want to allow confined virtual guests to read fuse files, you must turn on the virt_use_fusefs boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_fusefs 1</code> </p>
<p> If you want to allow confined virtual guests to manage nfs files, you must turn on the virt_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_nfs 1</code> </p>
<p> If you want to allow confined virtual guests to manage nfs files, you must turn on the virt_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_nfs 1</code> </p>
<p> If you want to allow confined virtual guests to interact with rawip sockets, you must turn on the virt_use_rawip boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_rawip 1</code> </p>
<p> If you want to allow confined virtual guests to interact with rawip sockets, you must turn on the virt_use_rawip boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_rawip 1</code> </p>
<p> If you want to allow confined virtual guests to manage cifs files, you must turn on the virt_use_samba boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_samba 1</code> </p>
<p> If you want to allow confined virtual guests to manage cifs files, you must turn on the virt_use_samba boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_samba 1</code> </p>
<p> If you want to allow confined virtual guests to interact with the sanlock, you must turn on the virt_use_sanlock boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_sanlock 1</code> </p>
<p> If you want to allow confined virtual guests to interact with the sanlock, you must turn on the virt_use_sanlock boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_sanlock 1</code> </p>
<p> If you want to allow confined virtual guests to use usb devices, you must turn on the virt_use_usb boolean. Enabled by default. </p>
<p> <code>setsebool -P virt_use_usb 1</code> </p>
<p> If you want to allow confined virtual guests to use usb devices, you must turn on the virt_use_usb boolean. Enabled by default. </p>
<p> <code>setsebool -P virt_use_usb 1</code> </p>
<p> If you want to allow confined virtual guests to interact with the xserver, you must turn on the virt_use_xserver boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_xserver 1</code> </p>
<p> If you want to allow confined virtual guests to interact with the xserver, you must turn on the virt_use_xserver boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_xserver 1</code> </p>
<p> If you want to support X userspace object manager, you must turn on the xserver_object_manager boolean. Enabled by default. </p>
<p> <code>setsebool -P xserver_object_manager 1</code></p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux virtd policy is very flexible allowing users to setup their virtd processes in as secure a method as possible. </p>
<p> The following port types are defined for virtd: </p>
<dl>
<dt><code>virt_migration_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 49152-49216 </p>
<dt><code>virt_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 16509,16514 udp 16509,16514</dl>
<h2>Managed Files</h2>
<p>The SELinux process type virtd_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>file_type</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all files on the system</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux virtd policy is very flexible allowing users to setup their virtd processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the virtd, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t virtd_unit_file_t &#8216;/srv/myvirtd_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myvirtd_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for virtd:</i> </p>
<p> <code>virtd_exec_t</code> </p>
<p> &#8211; Set files with the virtd_exec_t type, if you want to transition an executable to the virtd_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/virt-who, /usr/sbin/libvirtd, /usr/bin/imgfac.py, /usr/sbin/virtlockd, /usr/share/vdsm/vdsm, /usr/bin/imagefactory, /usr/bin/nova-compute, /usr/share/vdsm/respawn, /usr/sbin/condor_vm-gahp, /usr/bin/vios-proxy-host, /usr/bin/vios-proxy-guest, /usr/share/vdsm/daemonAdapter, /usr/share/vdsm/supervdsmServer </p>
</dl>
<p> <code>virtd_initrc_exec_t</code> </p>
<p> &#8211; Set files with the virtd_initrc_exec_t type, if you want to transition an executable to the virtd_initrc_t domain. </p>
<p> <code>virtd_keytab_t</code> </p>
<p> &#8211; Set files with the virtd_keytab_t type, if you want to treat the files as kerberos keytab files. </p>
<p> <code>virtd_lxc_exec_t</code> </p>
<p> &#8211; Set files with the virtd_lxc_exec_t type, if you want to transition an executable to the virtd_lxc_t domain. </p>
<p> <code>virtd_unit_file_t</code> </p>
<p> &#8211; Set files with the virtd_unit_file_t type, if you want to treat the files as virtd unit content. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/systemd/system/.*xen.*.service, /usr/lib/systemd/system/virt.*.service, /usr/lib/systemd/system/libvirt.*.service </p>
</dl>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage port</code> can also be used to manipulate the port definitions </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-virtd/">virtd</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-virt_bridgehelper_selinux/">virt_bridgehelper_selinux</a>(8), <a href="/docs/linux/man/8-virt_qemu_ga_selinux/">virt_qemu_ga_selinux</a>(8), <a href="/docs/linux/man/8-virt_qemu_ga_unconfined_selinux/">virt_qemu_ga_unconfined_selinux</a>(8), <a href="/docs/linux/man/8-virt_qmf_selinux/">virt_qmf_selinux</a>(8), <a href="/docs/linux/man/8-virtd_lxc_selinux/">virtd_lxc_selinux</a>(8)</p>
