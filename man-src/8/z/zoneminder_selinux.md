---
title: "zoneminder_selinux(8)"
name: "zoneminder_selinux"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zoneminder_selinux/"
description: "zoneminder_selinux – Security Enhanced Linux Policy for the zoneminder processes"
---

<p>zoneminder_selinux &#8211; Security Enhanced Linux Policy for the zoneminder processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the zoneminder processes via flexible mandatory access control. The zoneminder processes execute with the zoneminder_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep zoneminder_t</code> </p>
<h2>Entrypoints</h2>
<p>The zoneminder_t SELinux type can be entered via the <code>zoneminder_exec_t</code> file type. </p>
<p> The default entrypoint paths for the zoneminder_t domain are the following: </p>
<p> /usr/bin/zmpkg.pl</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux zoneminder policy is very flexible allowing users to setup their zoneminder processes in as secure a method as possible. </p>
<p> The following process types are defined for zoneminder: </p>
<p> zoneminder_t, zoneminder_script_t</code> </p>
<p> Note: <code>semanage permissive -a zoneminder_t</code> can be used to make the process type zoneminder_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. zoneminder policy is extremely flexible and has several booleans that allow you to manipulate the policy and run zoneminder with the tightest access possible. </p>
<p> If you want to allow ZoneMinder to run su/sudo, you must turn on the zoneminder_run_sudo boolean. Disabled by default. </p>
<p> <code>setsebool -P zoneminder_run_sudo 1</code> </p>
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
<h2>Managed Files</h2>
<p>The SELinux process type zoneminder_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>cluster_conf_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/cluster(/.*)?</p>
<p> <code>cluster_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/pcsd(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/cluster(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/openais(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/pengine(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/corosync(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/lib/heartbeat(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/heartbeat(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/pacemaker(/.*)?</p>
<p> <code>cluster_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/crm(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/cman_.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/rsctmp(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/aisexec.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/heartbeat(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/corosync-qnetd(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/corosync-qdevice(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/cpglockd.pid</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/corosync.pid</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/rgmanager.pid</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/cluster/rgmanager.sk</p>
<p> <code>faillog_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/btmp.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/faillog.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/tallylog.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/faillock(/.*)?</p>
<p> <code>lastlog_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/lastlog.*</p>
<p> <code>motion_data_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/motion(/.*)?</p>
<p> <code>motion_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/motion.log.*</p>
<p> <code>motion_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/motion.pid</p>
<p> <code>public_content_rw_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/abrt-upload(/.*)?</p>
<p> <code>root_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/initrd</p>
<p> <code>security_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/selinux</p>
<p> <code>zoneminder_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/zoneminder(/.*)?</p>
<p> <code>zoneminder_spool_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/zoneminder-upload(/.*)?</p>
<p> <code>zoneminder_tmpfs_t</code> </p>
<p> <code>zoneminder_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/zoneminder(/.*)?</p>
<p> <code>zoneminder_var_run_t</code></p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux zoneminder policy is very flexible allowing users to setup their zoneminder processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the zoneminder, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t zoneminder_var_run_t &#8216;/srv/myzoneminder_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myzoneminder_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for zoneminder:</i> </p>
<p> <code>zoneminder_content_t</code> </p>
<p> &#8211; Set files with the zoneminder_content_t type, if you want to treat the files as zoneminder content. </p>
<p> <code>zoneminder_exec_t</code> </p>
<p> &#8211; Set files with the zoneminder_exec_t type, if you want to transition an executable to the zoneminder_t domain. </p>
<p> <code>zoneminder_htaccess_t</code> </p>
<p> &#8211; Set files with the zoneminder_htaccess_t type, if you want to treat the file as a zoneminder access file. </p>
<p> <code>zoneminder_initrc_exec_t</code> </p>
<p> &#8211; Set files with the zoneminder_initrc_exec_t type, if you want to transition an executable to the zoneminder_initrc_t domain. </p>
<p> <code>zoneminder_log_t</code> </p>
<p> &#8211; Set files with the zoneminder_log_t type, if you want to treat the data as zoneminder log data, usually stored under the /var/log directory. </p>
<p> <code>zoneminder_ra_content_t</code> </p>
<p> &#8211; Set files with the zoneminder_ra_content_t type, if you want to treat the files as zoneminder read/append content. </p>
<p> <code>zoneminder_rw_content_t</code> </p>
<p> &#8211; Set files with the zoneminder_rw_content_t type, if you want to treat the files as zoneminder read/write content. </p>
<p> <code>zoneminder_script_exec_t</code> </p>
<p> &#8211; Set files with the zoneminder_script_exec_t type, if you want to transition an executable to the zoneminder_script_t domain. </p>
<p> <code>zoneminder_spool_t</code> </p>
<p> &#8211; Set files with the zoneminder_spool_t type, if you want to store the zoneminder files under the /var/spool directory. </p>
<p> <code>zoneminder_tmpfs_t</code> </p>
<p> &#8211; Set files with the zoneminder_tmpfs_t type, if you want to store zoneminder files on a tmpfs file system. </p>
<p> <code>zoneminder_unit_file_t</code> </p>
<p> &#8211; Set files with the zoneminder_unit_file_t type, if you want to treat the files as zoneminder unit content. </p>
<p> <code>zoneminder_var_lib_t</code> </p>
<p> &#8211; Set files with the zoneminder_var_lib_t type, if you want to store the zoneminder files under the /var/lib directory. </p>
<p> <code>zoneminder_var_run_t</code> </p>
<p> &#8211; Set files with the zoneminder_var_run_t type, if you want to store the zoneminder files under the /run or /var/run directory. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Sharing Files</h2>
<p>If you want to share files with multiple domains (Apache, FTP, rsync, Samba), you can set a file context of public_content_t and public_content_rw_t. These context allow any of the above domains to read the content. If you want a particular domain to write to the public_content_rw_t domain, you must set the appropriate boolean.</p>
<dl>
<dt>Allow zoneminder servers to read the /var/zoneminder directory by adding the public_content_t file type to the directory and by restoring the file type.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_t &quot;/var/zoneminder(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/zoneminder</code></p>
<dl>
<dt>Allow zoneminder servers to read and write /var/zoneminder/incoming by adding the public_content_rw_t type to the directory and by restoring the file type. You also need to turn on the zoneminder_anon_write boolean.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_rw_t &quot;/var/zoneminder/incoming(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/zoneminder/incoming</code><br />
 <code>setsebool -P zoneminder_anon_write 1</code> </p>
<p> If you want to allow ZoneMinder to modify public files used for public file transfer services., you must turn on the zoneminder_anon_write boolean. </p>
<p> <code>setsebool -P zoneminder_anon_write 1</code></p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-zoneminder/">zoneminder</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-zoneminder_script_selinux/">zoneminder_script_selinux</a>(8), <a href="/docs/linux/man/8-zoneminder_script_selinux/">zoneminder_script_selinux</a>(8) </p>
