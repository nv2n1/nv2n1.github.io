---
title: "dirsrvadmin_selinux(8)"
name: "dirsrvadmin_selinux"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dirsrvadmin_selinux/"
description: "dirsrvadmin_selinux – Security Enhanced Linux Policy for the dirsrvadmin processes"
---

<p>dirsrvadmin_selinux &#8211; Security Enhanced Linux Policy for the dirsrvadmin processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the dirsrvadmin processes via flexible mandatory access control. The dirsrvadmin processes execute with the dirsrvadmin_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep dirsrvadmin_t</code> </p>
<h2>Entrypoints</h2>
<p>The dirsrvadmin_t SELinux type can be entered via the <code>shell_exec_t, dirsrvadmin_exec_t</code> file types. </p>
<p> The default entrypoint paths for the dirsrvadmin_t domain are the following: </p>
<p> /bin/d?ash, /bin/zsh.*, /bin/ksh.*, /usr/bin/d?ash, /usr/bin/zsh.*, /usr/bin/ksh.*, /bin/esh, /bin/mksh, /bin/sash, /bin/tcsh, /bin/yash, /bin/bash, /bin/fish, /bin/bash2, /usr/bin/esh, /usr/bin/tcsh, /usr/bin/yash, /usr/bin/sash, /usr/bin/mksh, /usr/bin/fish, /usr/bin/bash, /sbin/nologin, /usr/sbin/sesh, /usr/bin/bash2, /usr/sbin/smrsh, /usr/bin/scponly, /usr/sbin/nologin, /usr/libexec/sesh, /usr/sbin/scponlyc, /usr/bin/git-shell, /usr/bin/cockpit-bridge, /usr/libexec/cockpit-agent, /usr/libexec/git-core/git-shell, /usr/sbin/stop-ds-admin, /usr/sbin/start-ds-admin, /usr/sbin/restart-ds-admin</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux dirsrvadmin policy is very flexible allowing users to setup their dirsrvadmin processes in as secure a method as possible. </p>
<p> The following process types are defined for dirsrvadmin: </p>
<p> dirsrvadmin_t, dirsrvadmin_unconfined_script_t, dirsrvadmin_script_t</code> </p>
<p> Note: <code>semanage permissive -a dirsrvadmin_t</code> can be used to make the process type dirsrvadmin_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. dirsrvadmin policy is extremely flexible and has several booleans that allow you to manipulate the policy and run dirsrvadmin with the tightest access possible. </p>
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
<p> <code>setsebool -P global_ssp 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type dirsrvadmin_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
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
<p> <code>dirsrvadmin_tmp_t</code> </p>
<p> <code>root_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/initrd</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux dirsrvadmin policy is very flexible allowing users to setup their dirsrvadmin processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the dirsrvadmin, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t dirsrvadmin_unit_file_t &#8216;/srv/mydirsrvadmin_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mydirsrvadmin_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for dirsrvadmin:</i> </p>
<p> <code>dirsrvadmin_config_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_config_t type, if you want to treat the files as dirsrvadmin configuration data, usually stored under the /etc directory. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/dirsrv/dsgw(/.*)?, /etc/dirsrv/admin-serv(/.*)? </p>
</dl>
<p> <code>dirsrvadmin_content_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_content_t type, if you want to treat the files as dirsrvadmin content. </p>
<p> <code>dirsrvadmin_exec_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_exec_t type, if you want to transition an executable to the dirsrvadmin_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/stop-ds-admin, /usr/sbin/start-ds-admin, /usr/sbin/restart-ds-admin </p>
</dl>
<p> <code>dirsrvadmin_htaccess_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_htaccess_t type, if you want to treat the file as a dirsrvadmin access file. </p>
<p> <code>dirsrvadmin_lock_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_lock_t type, if you want to treat the files as dirsrvadmin lock data, stored under the /var/lock directory </p>
<p> <code>dirsrvadmin_ra_content_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_ra_content_t type, if you want to treat the files as dirsrvadmin read/append content. </p>
<p> <code>dirsrvadmin_rw_content_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_rw_content_t type, if you want to treat the files as dirsrvadmin read/write content. </p>
<p> <code>dirsrvadmin_script_exec_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_script_exec_t type, if you want to transition an executable to the dirsrvadmin_script_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/dirsrv/cgi-bin(/.*)?, /usr/lib/dirsrv/dsgw-cgi-bin(/.*)? </p>
</dl>
<p> <code>dirsrvadmin_tmp_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_tmp_t type, if you want to store dirsrvadmin temporary files in the /tmp directories. </p>
<p> <code>dirsrvadmin_unconfined_script_exec_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_unconfined_script_exec_t type, if you want to transition an executable to the dirsrvadmin_unconfined_script_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/dirsrv/cgi-bin/ds_create, /usr/lib/dirsrv/cgi-bin/ds_remove </p>
</dl>
<p> <code>dirsrvadmin_unit_file_t</code> </p>
<p> &#8211; Set files with the dirsrvadmin_unit_file_t type, if you want to treat the files as dirsrvadmin unit content. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-dirsrvadmin/">dirsrvadmin</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-dirsrvadmin_script_selinux/">dirsrvadmin_script_selinux</a>(8), <a href="/docs/linux/man/8-dirsrvadmin_script_selinux/">dirsrvadmin_script_selinux</a>(8), <a href="/docs/linux/man/8-dirsrvadmin_unconfined_script_selinux/">dirsrvadmin_unconfined_script_selinux</a>(8), <a href="/docs/linux/man/8-dirsrvadmin_unconfined_script_selinux/">dirsrvadmin_unconfined_script_selinux</a>(8) </p>
