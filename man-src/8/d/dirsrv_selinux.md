---
title: "dirsrv_selinux(8)"
name: "dirsrv_selinux"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dirsrv_selinux/"
description: "dirsrv_selinux – Security Enhanced Linux Policy for the dirsrv processes"
---

<p>dirsrv_selinux &#8211; Security Enhanced Linux Policy for the dirsrv processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the dirsrv processes via flexible mandatory access control. The dirsrv processes execute with the dirsrv_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep dirsrv_t</code> </p>
<h2>Entrypoints</h2>
<p>The dirsrv_t SELinux type can be entered via the <code>dirsrv_exec_t</code> file type. </p>
<p> The default entrypoint paths for the dirsrv_t domain are the following: </p>
<p> /usr/sbin/ns-slapd</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux dirsrv policy is very flexible allowing users to setup their dirsrv processes in as secure a method as possible. </p>
<p> The following process types are defined for dirsrv: </p>
<p> dirsrv_t, dirsrv_snmp_t, dirsrvadmin_t, dirsrvadmin_unconfined_script_t, dirsrvadmin_script_t</code> </p>
<p> Note: <code>semanage permissive -a dirsrv_t</code> can be used to make the process type dirsrv_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. dirsrv policy is extremely flexible and has several booleans that allow you to manipulate the policy and run dirsrv with the tightest access possible. </p>
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
<p>The SELinux process type dirsrv_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
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
<p> <code>dirsrv_config_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/dirsrv(/.*)?</p>
<p> <code>dirsrv_tmp_t</code> </p>
<p> <code>dirsrv_tmpfs_t</code> </p>
<p> <code>dirsrv_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/dirsrv(/.*)?</p>
<p> <code>dirsrv_var_lock_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lock/dirsrv(/.*)?</p>
<p> <code>dirsrv_var_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/dirsrv(/.*)?</p>
<p> <code>dirsrv_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/slapd.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/dirsrv(/.*)?</p>
<p> <code>faillog_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/btmp.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/faillog.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/tallylog.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/faillock(/.*)?</p>
<p> <code>krb5_host_rcache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/krb5rcache(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/nfs_0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/DNS_25</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/host_0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/imap_0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/HTTP_23</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/HTTP_48</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/ldap_55</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/ldap_487</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/ldapmap1_0</p>
<p> <code>lastlog_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/lastlog.*</p>
<p> <code>root_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/initrd</p>
<p> <code>security_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/selinux</p>
<p> <code>systemd_passwd_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/ask-password(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/ask-password-block(/.*)?</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux dirsrv policy is very flexible allowing users to setup their dirsrv processes in as secure a method as possible. </p>
<p> EQUIVALENCE DIRECTORIES</code> </p>
<p> dirsrv policy stores data with multiple different file context types under the /var/log/dirsrv directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/log/dirsrv /srv/dirsrv</code><br />
 <code>restorecon -R -v /srv/dirsrv</code> </p>
<p> <code>STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the dirsrv, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t dirsrvadmin_unit_file_t &#8216;/srv/mydirsrv_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mydirsrv_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for dirsrv:</i> </p>
<p> <code>dirsrv_config_t</code> </p>
<p> &#8211; Set files with the dirsrv_config_t type, if you want to treat the files as dirsrv configuration data, usually stored under the /etc directory. </p>
<p> <code>dirsrv_exec_t</code> </p>
<p> &#8211; Set files with the dirsrv_exec_t type, if you want to transition an executable to the dirsrv_t domain. </p>
<p> <code>dirsrv_share_t</code> </p>
<p> &#8211; Set files with the dirsrv_share_t type, if you want to treat the files as dirsrv share data. </p>
<p> <code>dirsrv_snmp_exec_t</code> </p>
<p> &#8211; Set files with the dirsrv_snmp_exec_t type, if you want to transition an executable to the dirsrv_snmp_t domain. </p>
<p> <code>dirsrv_snmp_var_log_t</code> </p>
<p> &#8211; Set files with the dirsrv_snmp_var_log_t type, if you want to treat the data as dirsrv snmp var log data, usually stored under the /var/log directory. </p>
<p> <code>dirsrv_snmp_var_run_t</code> </p>
<p> &#8211; Set files with the dirsrv_snmp_var_run_t type, if you want to store the dirsrv snmp files under the /run or /var/run directory. </p>
<p> <code>dirsrv_tmp_t</code> </p>
<p> &#8211; Set files with the dirsrv_tmp_t type, if you want to store dirsrv temporary files in the /tmp directories. </p>
<p> <code>dirsrv_tmpfs_t</code> </p>
<p> &#8211; Set files with the dirsrv_tmpfs_t type, if you want to store dirsrv files on a tmpfs file system. </p>
<p> <code>dirsrv_var_lib_t</code> </p>
<p> &#8211; Set files with the dirsrv_var_lib_t type, if you want to store the dirsrv files under the /var/lib directory. </p>
<p> <code>dirsrv_var_lock_t</code> </p>
<p> &#8211; Set files with the dirsrv_var_lock_t type, if you want to treat the files as dirsrv var lock data, stored under the /var/lock directory </p>
<p> <code>dirsrv_var_log_t</code> </p>
<p> &#8211; Set files with the dirsrv_var_log_t type, if you want to treat the data as dirsrv var log data, usually stored under the /var/log directory. </p>
<p> <code>dirsrv_var_run_t</code> </p>
<p> &#8211; Set files with the dirsrv_var_run_t type, if you want to store the dirsrv files under the /run or /var/run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/slapd.*, /var/run/dirsrv(/.*)? </p>
</dl>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-dirsrv/">dirsrv</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-dirsrv_snmp_selinux/">dirsrv_snmp_selinux</a>(8), <a href="/docs/linux/man/8-dirsrv_snmp_selinux/">dirsrv_snmp_selinux</a>(8) </p>
