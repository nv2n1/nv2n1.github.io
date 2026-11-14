---
title: "rssh_chroot_helper_selinux(8)"
name: "rssh_chroot_helper_selinux"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rssh_chroot_helper_selinux/"
description: "rssh_chroot_helper_selinux – Security Enhanced Linux Policy for the rssh_chroot_helper processes"
---

<p>rssh_chroot_helper_selinux &#8211; Security Enhanced Linux Policy for the rssh_chroot_helper processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the rssh_chroot_helper processes via flexible mandatory access control. The rssh_chroot_helper processes execute with the rssh_chroot_helper_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep rssh_chroot_helper_t</code> </p>
<h2>Entrypoints</h2>
<p>The rssh_chroot_helper_t SELinux type can be entered via the <code>rssh_chroot_helper_exec_t</code> file type. </p>
<p> The default entrypoint paths for the rssh_chroot_helper_t domain are the following: </p>
<p> /usr/libexec/rssh_chroot_helper</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux rssh_chroot_helper policy is very flexible allowing users to setup their rssh_chroot_helper processes in as secure a method as possible. </p>
<p> The following process types are defined for rssh_chroot_helper: </p>
<p> rssh_chroot_helper_t</code> </p>
<p> Note: <code>semanage permissive -a rssh_chroot_helper_t</code> can be used to make the process type rssh_chroot_helper_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. rssh_chroot_helper policy is extremely flexible and has several booleans that allow you to manipulate the policy and run rssh_chroot_helper with the tightest access possible. </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
<p> If you want to allow all daemons the ability to read/write terminals, you must turn on the daemons_use_tty boolean. Disabled by default. </p>
<p> <code>setsebool -P daemons_use_tty 1</code> </p>
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
<p> <code>setsebool -P nscd_use_shm 1</code></p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux rssh_chroot_helper policy is very flexible allowing users to setup their rssh_chroot_helper processes in as secure a method as possible. </p>
<p> </code><i>The following file types are defined for rssh_chroot_helper:</i> </p>
<p> <code>rssh_chroot_helper_exec_t</code> </p>
<p> &#8211; Set files with the rssh_chroot_helper_exec_t type, if you want to transition an executable to the rssh_chroot_helper_t domain. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-rssh_chroot_helper/">rssh_chroot_helper</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
