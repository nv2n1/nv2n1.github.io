---
title: "unconfined_selinux(8)"
name: "unconfined_selinux"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unconfined_selinux/"
description: "unconfined_r – Unconfined user role – Security Enhanced Linux Policy"
---

<p>unconfined_r &#8211; <code>Unconfined user role</code> &#8211; Security Enhanced Linux Policy </p>
<h2>Description</h2>
<p>SELinux supports Roles Based Access Control (RBAC), some Linux roles are login roles, while other roles need to be transition into. <i>Note:</i> Examples in this man page will use the <code>staff_u</code> SELinux user. Non login roles are usually used for administrative tasks. For example, tasks that require root privileges. Roles control which types a user can run processes with. Roles often have default types assigned to them. The default type for the unconfined_r role is unconfined_t. The <code>newrole</code> program to transition directly to this role. <code>newrole -r unconfined_r -t unconfined_t</code> <code>sudo</code> is the preferred method to do transition from one role to another. You setup sudo to transition to unconfined_r by adding a similar line to the /etc/sudoers file. USERNAME ALL=(ALL) ROLE=unconfined_r TYPE=unconfined_t COMMAND<br />
 sudo will run COMMAND as staff_u:unconfined_r:unconfined_t:LEVEL When using a a non login role, you need to setup SELinux so that your SELinux user can reach unconfined_r role. Execute the following to see all of the assigned SELinux roles: <code>semanage user -l</code> You need to add unconfined_r to the staff_u user. You could setup the staff_u user to be able to use the unconfined_r role with a command like: <code>$ semanage user -m -R &#8216;staff_r system_r unconfined_r&#8217; staff_u</code> </p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. unconfined policy is extremely flexible and has several booleans that allow you to manipulate the policy and run unconfined with the tightest access possible. </p>
<p> If you want to allow unconfined users to transition to the chrome sandbox domains when running chrome-sandbox, you must turn on the unconfined_chrome_sandbox_transition boolean. Enabled by default. </p>
<p> <code>setsebool -P unconfined_chrome_sandbox_transition 1</code> </p>
<p> If you want to allow a user to login as an unconfined domain, you must turn on the unconfined_login boolean. Enabled by default. </p>
<p> <code>setsebool -P unconfined_login 1</code> </p>
<p> If you want to allow unconfined users to transition to the Mozilla plugin domain when running xulrunner plugin-container, you must turn on the unconfined_mozilla_plugin_transition boolean. Enabled by default. </p>
<p> <code>setsebool -P unconfined_mozilla_plugin_transition 1</code> </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
<p> If you want to determine whether crond can execute jobs in the user domain as opposed to the the generic cronjob domain, you must turn on the cron_userdomain_transition boolean. Enabled by default. </p>
<p> <code>setsebool -P cron_userdomain_transition 1</code> </p>
<p> If you want to deny user domains applications to map a memory region as both executable and writable, this is dangerous and the executable should be reported in bugzilla, you must turn on the deny_execmem boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_execmem 1</code> </p>
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
<p> If you want to allow logging in and using the system from /dev/console, you must turn on the login_console_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P login_console_enabled 1</code> </p>
<p> If you want to control the ability to mmap a low area of the address space, as configured by /proc/sys/vm/mmap_min_addr, you must turn on the mmap_low_allowed boolean. Disabled by default. </p>
<p> <code>setsebool -P mmap_low_allowed 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to disallow programs, such as newrole, from transitioning to administrative user domains, you must turn on the secure_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode 1</code> </p>
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
<p> If you want to allow ssh logins as sysadm_r:sysadm_t, you must turn on the ssh_sysadm_login boolean. Disabled by default. </p>
<p> <code>setsebool -P ssh_sysadm_login 1</code> </p>
<p> If you want to support NFS home directories, you must turn on the use_nfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_nfs_home_dirs 1</code> </p>
<p> If you want to support SAMBA home directories, you must turn on the use_samba_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_samba_home_dirs 1</code> </p>
<p> If you want to allow the graphical login program to login directly as sysadm_r:sysadm_t, you must turn on the xdm_sysadm_login boolean. Disabled by default. </p>
<p> <code>setsebool -P xdm_sysadm_login 1</code> </p>
<p> If you want to support X userspace object manager, you must turn on the xserver_object_manager boolean. Enabled by default. </p>
<p> <code>setsebool -P xserver_object_manager 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type unconfined_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>file_type</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all files on the system</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-unconfined/">unconfined</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-unconfined_cronjob_selinux/">unconfined_cronjob_selinux</a>(8), <a href="/docs/linux/man/8-unconfined_dbusd_selinux/">unconfined_dbusd_selinux</a>(8), <a href="/docs/linux/man/8-unconfined_mount_selinux/">unconfined_mount_selinux</a>(8), <a href="/docs/linux/man/8-unconfined_munin_plugin_selinux/">unconfined_munin_plugin_selinux</a>(8), <a href="/docs/linux/man/8-unconfined_sendmail_selinux/">unconfined_sendmail_selinux</a>(8), <a href="/docs/linux/man/8-unconfined_service_selinux/">unconfined_service_selinux</a>(8) </p>
