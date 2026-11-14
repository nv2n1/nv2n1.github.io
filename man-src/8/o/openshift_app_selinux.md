---
title: "openshift_app_selinux(8)"
name: "openshift_app_selinux"
section: "8"
letter: "o"
url: "/docs/linux/man/8-openshift_app_selinux/"
description: "openshift_app_selinux – Security Enhanced Linux Policy for the openshift_app processes"
---

<p>openshift_app_selinux &#8211; Security Enhanced Linux Policy for the openshift_app processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the openshift_app processes via flexible mandatory access control. The openshift_app processes execute with the openshift_app_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep openshift_app_t</code> </p>
<h2>Entrypoints</h2>
<p>The openshift_app_t SELinux type can be entered via the <code>usr_t, bin_t, httpd_exec_t, shell_exec_t, gpg_exec_t, openshift_file_type, user_cron_spool_t</code> file types. </p>
<p> The default entrypoint paths for the openshift_app_t domain are the following: </p>
<p> All executeables with the default executable label, usually stored in /usr/bin and /usr/sbin. /usr/.*, /opt/.*, /emul/.*, /ostree(/.*)?, /export(/.*)?, /usr/doc(/.*)?/lib(/.*)?, /usr/inclu.e(/.*)?, /usr/share/doc(/.*)?/README.*, /usr, /opt, /emul, /usr/sbin/httpd(.worker)?, /usr/sbin/<a href="/docs/linux/man/2-apache/">apache</a>(2)?, /usr/lib/apache-ssl/.+, /usr/sbin/<a href="/docs/linux/man/2-apache-ssl/">apache-ssl</a>(2)?, /usr/share/jetty/bin/jetty.sh, /usr/sbin/nginx, /usr/sbin/thttpd, /usr/sbin/php-fpm, /usr/sbin/cherokee, /usr/sbin/lighttpd, /usr/sbin/httpd.event, /usr/bin/mongrel_rails, /usr/sbin/htcacheclean, /bin/d?ash, /bin/zsh.*, /bin/ksh.*, /usr/bin/d?ash, /usr/bin/zsh.*, /usr/bin/ksh.*, /bin/esh, /bin/mksh, /bin/sash, /bin/tcsh, /bin/yash, /bin/bash, /bin/fish, /bin/bash2, /usr/bin/esh, /usr/bin/tcsh, /usr/bin/yash, /usr/bin/sash, /usr/bin/mksh, /usr/bin/fish, /usr/bin/bash, /sbin/nologin, /usr/sbin/sesh, /usr/bin/bash2, /usr/sbin/smrsh, /usr/bin/scponly, /usr/sbin/nologin, /usr/libexec/sesh, /usr/sbin/scponlyc, /usr/bin/git-shell, /usr/bin/cockpit-bridge, /usr/libexec/cockpit-agent, /usr/libexec/git-core/git-shell, /usr/bin/<a href="/docs/linux/man/2-gpg/">gpg</a>(2)?, /usr/lib/gnupg/.*, /usr/bin/gpgsm, /var/spool/at(/.*)?, /var/spool/cron</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux openshift_app policy is very flexible allowing users to setup their openshift_app processes in as secure a method as possible. </p>
<p> The following process types are defined for openshift_app: </p>
<p> openshift_app_t</code> </p>
<p> Note: <code>semanage permissive -a openshift_app_t</code> can be used to make the process type openshift_app_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>MCS Constrained</h2>
<p>The SELinux process type openshift_app_t is an MCS (Multi Category Security) constrained type. Sometimes this separation is referred to as sVirt. These types are usually used for securing multi-tenant environments, such as virtualization, containers or separation of users. The tools used to launch MCS types, pick out a different MCS label for each process group. </p>
<p> For example one process might be launched with openshift_app_t:s0:c1,c2, and another process launched with openshift_app_t:s0:c3,c4. The SELinux kernel only allows these processes can only write to content with a matching MCS label, or a MCS Label of s0. A process running with the MCS level of s0:c1,c2 is not allowed to write to content with the MCS label of s0:c3,c4</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. openshift_app policy is extremely flexible and has several booleans that allow you to manipulate the policy and run openshift_app with the tightest access possible. </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
<p> If you want to determine whether crond can execute jobs in the user domain as opposed to the the generic cronjob domain, you must turn on the cron_userdomain_transition boolean. Enabled by default. </p>
<p> <code>setsebool -P cron_userdomain_transition 1</code> </p>
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
<p> If you want to allow openshift to access nfs file systems without labels, you must turn on the openshift_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P openshift_use_nfs 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type openshift_app_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>anon_inodefs_t</code> </p>
<p> <code>hugetlbfs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/hugepages</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/lib/udev/devices/hugepages</p>
<p> <code>nfs_t</code> </p>
<p> <code>openshift_rw_file_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/openshift/.*/data(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/stickshift/.*/data(/.*)?</p>
<p> <code>openshift_tmp_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/openshift/.*/.tmp(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/openshift/.*/.sandbox(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/stickshift/.*/.tmp(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/stickshift/.*/.sandbox(/.*)?</p>
<p> <code>openshift_tmpfs_t</code> </p>
<p> <code>security_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/selinux</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-openshift_app/">openshift_app</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
