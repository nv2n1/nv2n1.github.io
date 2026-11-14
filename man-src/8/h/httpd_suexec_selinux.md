---
title: "httpd_suexec_selinux(8)"
name: "httpd_suexec_selinux"
section: "8"
letter: "h"
url: "/docs/linux/man/8-httpd_suexec_selinux/"
description: "httpd_suexec_selinux – Security Enhanced Linux Policy for the httpd_suexec processes"
---

<p>httpd_suexec_selinux &#8211; Security Enhanced Linux Policy for the httpd_suexec processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the httpd_suexec processes via flexible mandatory access control. The httpd_suexec processes execute with the httpd_suexec_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep httpd_suexec_t</code> </p>
<h2>Entrypoints</h2>
<p>The httpd_suexec_t SELinux type can be entered via the <code>httpd_suexec_exec_t</code> file type. </p>
<p> The default entrypoint paths for the httpd_suexec_t domain are the following: </p>
<p> /usr/lib/<a href="/docs/linux/man/2-apache/">apache</a>(2)?/<a href="/docs/linux/man/2-suexec/">suexec</a>(2)?, /usr/lib/cgi-bin/(nph-)?cgiwrap(d)?, /usr/sbin/suexec</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux httpd_suexec policy is very flexible allowing users to setup their httpd_suexec processes in as secure a method as possible. </p>
<p> The following process types are defined for httpd_suexec: </p>
<p> httpd_suexec_t</code> </p>
<p> Note: <code>semanage permissive -a httpd_suexec_t</code> can be used to make the process type httpd_suexec_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. httpd_suexec policy is extremely flexible and has several booleans that allow you to manipulate the policy and run httpd_suexec with the tightest access possible. </p>
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
<p> If you want to allow httpd to use built in scripting (usually php), you must turn on the httpd_builtin_scripting boolean. Enabled by default. </p>
<p> <code>setsebool -P httpd_builtin_scripting 1</code> </p>
<p> If you want to allow HTTPD scripts and modules to connect to the network using TCP, you must turn on the httpd_can_network_connect boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_network_connect 1</code> </p>
<p> If you want to allow HTTPD scripts and modules to connect to databases over the network, you must turn on the httpd_can_network_connect_db boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_network_connect_db 1</code> </p>
<p> If you want to allow http daemon to send mail, you must turn on the httpd_can_sendmail boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_sendmail 1</code> </p>
<p> If you want to allow httpd cgi support, you must turn on the httpd_enable_cgi boolean. Enabled by default. </p>
<p> <code>setsebool -P httpd_enable_cgi 1</code> </p>
<p> If you want to allow httpd to read home directories, you must turn on the httpd_enable_homedirs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_enable_homedirs 1</code> </p>
<p> If you want to allow httpd scripts and modules execmem/execstack, you must turn on the httpd_execmem boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_execmem 1</code> </p>
<p> If you want to allow httpd to read user content, you must turn on the httpd_read_user_content boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_read_user_content 1</code> </p>
<p> If you want to unify HTTPD to communicate with the terminal. Needed for entering the passphrase for certificates at the terminal, you must turn on the httpd_tty_comm boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_tty_comm 1</code> </p>
<p> If you want to unify HTTPD handling of all content files, you must turn on the httpd_unified boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_unified 1</code> </p>
<p> If you want to allow httpd to access cifs file systems, you must turn on the httpd_use_cifs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_cifs 1</code> </p>
<p> If you want to allow httpd to access FUSE file systems, you must turn on the httpd_use_fusefs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_fusefs 1</code> </p>
<p> If you want to allow httpd to access nfs file systems, you must turn on the httpd_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_nfs 1</code> </p>
<p> If you want to allow confined applications to run with kerberos, you must turn on the kerberos_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P kerberos_enabled 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to allow unprivileged users to execute DDL statement, you must turn on the postgresql_selinux_users_ddl boolean. Enabled by default. </p>
<p> <code>setsebool -P postgresql_selinux_users_ddl 1</code> </p>
<p> If you want to support NFS home directories, you must turn on the use_nfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_nfs_home_dirs 1</code> </p>
<p> If you want to support SAMBA home directories, you must turn on the use_samba_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_samba_home_dirs 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type httpd_suexec_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>cifs_t</code> </p>
<p> <code>fusefs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user/[^/]*/gvfs</p>
<p> <code>httpd_suexec_tmp_t</code> </p>
<p> <code>nfs_t</code></p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux httpd_suexec policy is very flexible allowing users to setup their httpd_suexec processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the httpd_suexec, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t httpd_suexec_tmp_t &#8216;/srv/myhttpd_suexec_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myhttpd_suexec_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for httpd_suexec:</i> </p>
<p> <code>httpd_suexec_exec_t</code> </p>
<p> &#8211; Set files with the httpd_suexec_exec_t type, if you want to transition an executable to the httpd_suexec_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/<a href="/docs/linux/man/2-apache/">apache</a>(2)?/<a href="/docs/linux/man/2-suexec/">suexec</a>(2)?, /usr/lib/cgi-bin/(nph-)?cgiwrap(d)?, /usr/sbin/suexec </p>
</dl>
<p> <code>httpd_suexec_tmp_t</code> </p>
<p> &#8211; Set files with the httpd_suexec_tmp_t type, if you want to store httpd suexec temporary files in the /tmp directories. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-httpd_suexec/">httpd_suexec</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
