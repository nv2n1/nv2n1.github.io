---
title: "apache_selinux(8)"
name: "apache_selinux"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apache_selinux/"
description: "httpd_selinux – Security Enhanced Linux Policy for the httpd processes"
---

<p>httpd_selinux &#8211; Security Enhanced Linux Policy for the httpd processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the httpd processes via flexible mandatory access control. The httpd processes execute with the httpd_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep httpd_t</code> </p>
<h2>Entrypoints</h2>
<p>The httpd_t SELinux type can be entered via the <code>httpd_exec_t</code> file type. </p>
<p> The default entrypoint paths for the httpd_t domain are the following: </p>
<p> /usr/sbin/httpd(.worker)?, /usr/sbin/<a href="/docs/linux/man/2-apache/">apache</a>(2)?, /usr/lib/apache-ssl/.+, /usr/sbin/<a href="/docs/linux/man/2-apache-ssl/">apache-ssl</a>(2)?, /usr/share/jetty/bin/jetty.sh, /usr/sbin/nginx, /usr/sbin/thttpd, /usr/sbin/php-fpm, /usr/sbin/cherokee, /usr/sbin/lighttpd, /usr/sbin/httpd.event, /usr/bin/mongrel_rails, /usr/sbin/htcacheclean</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux httpd policy is very flexible allowing users to setup their httpd processes in as secure a method as possible. </p>
<p> The following process types are defined for httpd: </p>
<p> httpd_t, httpd_helper_t, httpd_php_t, httpd_rotatelogs_t, httpd_suexec_t, httpd_sys_script_t, httpd_user_script_t, httpd_passwd_t, httpd_unconfined_script_t</code> </p>
<p> Note: <code>semanage permissive -a httpd_t</code> can be used to make the process type httpd_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. httpd policy is extremely flexible and has several booleans that allow you to manipulate the policy and run httpd with the tightest access possible. </p>
<p> If you want to allow httpd to use built in scripting (usually php), you must turn on the httpd_builtin_scripting boolean. Enabled by default. </p>
<p> <code>setsebool -P httpd_builtin_scripting 1</code> </p>
<p> If you want to allow http daemon to check spam, you must turn on the httpd_can_check_spam boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_check_spam 1</code> </p>
<p> If you want to allow httpd to act as a FTP client connecting to the ftp port and ephemeral ports, you must turn on the httpd_can_connect_ftp boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_connect_ftp 1</code> </p>
<p> If you want to allow httpd to connect to the ldap port, you must turn on the httpd_can_connect_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_connect_ldap 1</code> </p>
<p> If you want to allow http daemon to connect to mythtv, you must turn on the httpd_can_connect_mythtv boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_connect_mythtv 1</code> </p>
<p> If you want to allow http daemon to connect to zabbix, you must turn on the httpd_can_connect_zabbix boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_connect_zabbix 1</code> </p>
<p> If you want to allow HTTPD scripts and modules to connect to the network using TCP, you must turn on the httpd_can_network_connect boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_network_connect 1</code> </p>
<p> If you want to allow HTTPD scripts and modules to connect to cobbler over the network, you must turn on the httpd_can_network_connect_cobbler boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_network_connect_cobbler 1</code> </p>
<p> If you want to allow HTTPD scripts and modules to connect to databases over the network, you must turn on the httpd_can_network_connect_db boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_network_connect_db 1</code> </p>
<p> If you want to allow httpd to connect to memcache server, you must turn on the httpd_can_network_memcache boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_network_memcache 1</code> </p>
<p> If you want to allow httpd to act as a relay, you must turn on the httpd_can_network_relay boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_network_relay 1</code> </p>
<p> If you want to allow http daemon to send mail, you must turn on the httpd_can_sendmail boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_sendmail 1</code> </p>
<p> If you want to allow Apache to communicate with avahi service via dbus, you must turn on the httpd_dbus_avahi boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_dbus_avahi 1</code> </p>
<p> If you want to allow Apache to communicate with sssd service via dbus, you must turn on the httpd_dbus_sssd boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_dbus_sssd 1</code> </p>
<p> If you want to allow httpd cgi support, you must turn on the httpd_enable_cgi boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_enable_cgi 1</code> </p>
<p> If you want to allow httpd to act as a FTP server by listening on the ftp port, you must turn on the httpd_enable_ftp_server boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_enable_ftp_server 1</code> </p>
<p> If you want to allow httpd to read home directories, you must turn on the httpd_enable_homedirs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_enable_homedirs 1</code> </p>
<p> If you want to allow httpd scripts and modules execmem/execstack, you must turn on the httpd_execmem boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_execmem 1</code> </p>
<p> If you want to allow HTTPD to connect to port 80 for graceful shutdown, you must turn on the httpd_graceful_shutdown boolean. Enabled by default. </p>
<p> <code>setsebool -P httpd_graceful_shutdown 1</code> </p>
<p> If you want to allow httpd processes to manage IPA content, you must turn on the httpd_manage_ipa boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_manage_ipa 1</code> </p>
<p> If you want to allow Apache to use mod_auth_ntlm_winbind, you must turn on the httpd_mod_auth_ntlm_winbind boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_mod_auth_ntlm_winbind 1</code> </p>
<p> If you want to allow Apache to use mod_auth_pam, you must turn on the httpd_mod_auth_pam boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_mod_auth_pam 1</code> </p>
<p> If you want to allow httpd to read user content, you must turn on the httpd_read_user_content boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_read_user_content 1</code> </p>
<p> If you want to allow httpd processes to run IPA helper, you must turn on the httpd_run_ipa boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_run_ipa 1</code> </p>
<p> If you want to allow Apache to run preupgrade, you must turn on the httpd_run_preupgrade boolean. Enabled by default. </p>
<p> <code>setsebool -P httpd_run_preupgrade 1</code> </p>
<p> If you want to allow Apache to run in stickshift mode, not transition to passenger, you must turn on the httpd_run_stickshift boolean. Enabled by default. </p>
<p> <code>setsebool -P httpd_run_stickshift 1</code> </p>
<p> If you want to allow HTTPD scripts and modules to server cobbler files, you must turn on the httpd_serve_cobbler_files boolean. Enabled by default. </p>
<p> <code>setsebool -P httpd_serve_cobbler_files 1</code> </p>
<p> If you want to allow httpd daemon to change its resource limits, you must turn on the httpd_setrlimit boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_setrlimit 1</code> </p>
<p> If you want to allow HTTPD to run SSI executables in the same domain as system CGI scripts, you must turn on the httpd_ssi_exec boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_ssi_exec 1</code> </p>
<p> If you want to allow Apache to execute tmp content, you must turn on the httpd_tmp_exec boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_tmp_exec 1</code> </p>
<p> If you want to unify HTTPD to communicate with the terminal. Needed for entering the passphrase for certificates at the terminal, you must turn on the httpd_tty_comm boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_tty_comm 1</code> </p>
<p> If you want to unify HTTPD handling of all content files, you must turn on the httpd_unified boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_unified 1</code> </p>
<p> If you want to allow httpd to access cifs file systems, you must turn on the httpd_use_cifs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_cifs 1</code> </p>
<p> If you want to allow httpd to access FUSE file systems, you must turn on the httpd_use_fusefs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_fusefs 1</code> </p>
<p> If you want to allow httpd to run gpg, you must turn on the httpd_use_gpg boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_gpg 1</code> </p>
<p> If you want to allow httpd to access nfs file systems, you must turn on the httpd_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_nfs 1</code> </p>
<p> If you want to allow httpd to access openstack ports, you must turn on the httpd_use_openstack boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_openstack 1</code> </p>
<p> If you want to allow httpd to connect to sasl, you must turn on the httpd_use_sasl boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_sasl 1</code> </p>
<p> If you want to allow Apache to query NS records, you must turn on the httpd_verify_dns boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_verify_dns 1</code> </p>
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
<p> If you want to determine whether Git system daemon can access cifs file systems, you must turn on the git_system_use_cifs boolean. Disabled by default. </p>
<p> <code>setsebool -P git_system_use_cifs 1</code> </p>
<p> If you want to determine whether Git system daemon can access nfs file systems, you must turn on the git_system_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P git_system_use_nfs 1</code> </p>
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code> </p>
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
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server for the httpd_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
<p> If you want to allow confined applications to run with kerberos for the httpd_t, you must turn on the kerberos_enabled boolean. </p>
<p> <code>setsebool -P kerberos_enabled 1</code></p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux httpd policy is very flexible allowing users to setup their httpd processes in as secure a method as possible. </p>
<p> The following port types are defined for httpd: </p>
<dl>
<dt><code>http_cache_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 8080,8118,8123,10001-10010 udp 3130 </p>
<dt><code>http_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 80,81,443,488,8008,8009,8443,9000</dl>
<h2>Managed Files</h2>
<p>The SELinux process type httpd_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>abrt_retrace_spool_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/faf(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/abrt-retrace(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/retrace-server(/.*)?</p>
<p> <code>anon_inodefs_t</code> </p>
<p> <code>apcupsd_cgi_rw_content_t</code> </p>
<p> <code>awstats_rw_content_t</code> </p>
<p> <code>bugzilla_rw_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/bugzilla(/.*)?</p>
<p> <code>cifs_t</code> </p>
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
<p> <code>cobbler_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/cobbler(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/cobbler(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/cobbler(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/etc(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/ppc(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/boot(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/grub(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/s390x(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/images(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/aarch64(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/images2(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/pxelinux.cfg(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/yaboot</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/memdisk</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/menu.c32</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/tftpboot/pxelinux.0</p>
<p> <code>collectd_rw_content_t</code> </p>
<p> <code>cvs_rw_content_t</code> </p>
<p> <code>dirsrv_config_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/dirsrv(/.*)?</p>
<p> <code>dirsrv_var_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/dirsrv(/.*)?</p>
<p> <code>dirsrv_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/slapd.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/dirsrv(/.*)?</p>
<p> <code>dirsrvadmin_config_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/dirsrv/dsgw(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/dirsrv/admin-serv(/.*)?</p>
<p> <code>dirsrvadmin_rw_content_t</code> </p>
<p> <code>dirsrvadmin_tmp_t</code> </p>
<p> <code>dspam_rw_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/dspam/data(/.*)?</p>
<p> <code>fusefs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user/[^/]*/gvfs</p>
<p> <code>git_rw_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/cgit(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/gitweb-caching(/.*)?</p>
<p> <code>httpd_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/rt(3|4)(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/ssl.*.sem</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/mod_.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/php-.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/httpd(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/mason(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/mod_ssl(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/lighttpd(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/mediawiki(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/mod_proxy(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/mod_gnutls(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/php-mmcache(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/php-eaccelerator(/.*)?</p>
<p> <code>httpd_lock_t</code> </p>
<p> <code>httpd_squirrelmail_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/squirrelmail/prefs(/.*)?</p>
<p> <code>httpd_sys_rw_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/glpi(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/horde(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/drupal.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/z-push(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/svn(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/svn(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/owncloud(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/uploads(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/wp-content(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/wp_backups(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/sites/default/files(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/sites/default/settings.php</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/mock/koji(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/drupal.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/zabbix/web(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/moodle(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/z-push(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/gosa(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/WebCalendar(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/joomla(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/dokuwiki(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/owncloud(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/viewvc(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/pootle/po(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/moodledata(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/srv/gallery2/smarty(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/moodle/data(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/graphite-web(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/gallery/albums(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html/owncloud/data(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/wordpress-mu/wp-content(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/wordpress/wp-content/uploads(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/wordpress/wp-content/upgrade(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html/configuration.php</p>
<p> <code>httpd_tmp_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user/apache(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/openshift/console/tmp(/.*)?</p>
<p> <code>httpd_tmpfs_t</code> </p>
<p> <code>httpd_user_rw_content_t</code> </p>
<p> <code>httpd_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/rt(3|4)/data/RT-Shredder(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/dav(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/php(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/glpi(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/httpd(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/nginx(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/z-push(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/ganglia(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/ipsilon(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/cherokee(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/lighttpd(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/mod_security(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/roundcubemail(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/opt/rh/rh-nginx18/lib/nginx(/.*)?</p>
<p> <code>httpd_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/wsgi.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/mod_.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/httpd.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/nginx.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/apache.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/php-fpm(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/lighttpd(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/php/session(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/php/wsdlcache(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/dirsrv/admin-serv.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/opt/rh/rh-nginx18/run/nginx(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/openshift/broker/httpd/run(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/openshift/console/httpd/run(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/opt/dirsrv/var/run/dirsrv/dsgw/cookies(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/thttpd.pid</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/gcache_port</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/cherokee.pid</p>
<p> <code>httpdcontent</code> </p>
<p> <code>hugetlbfs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/hugepages</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/lib/udev/devices/hugepages</p>
<p> <code>jetty_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/jetty(/.*)?</p>
<p> <code>jetty_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/jetty(/.*)?</p>
<p> <code>jetty_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/jetty(/.*)?</p>
<p> <code>jetty_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/jetty(/.*)?</p>
<p> <code>keystone_cgi_rw_content_t</code> </p>
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
<p> <code>man2html_rw_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/man2html(/.*)?</p>
<p> <code>mediawiki_rw_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/wiki[0-9]?(/.*)?</p>
<p> <code>memcached_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/memcached(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/ipa_memcached(/.*)?</p>
<p> <code>mirrormanager_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/mirrormanager(/.*)?</p>
<p> <code>mojomojo_rw_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/mojomojo(/.*)?</p>
<p> <code>munin_rw_content_t</code> </p>
<p> <code>mythtv_rw_content_t</code> </p>
<p> <code>nagios_rw_content_t</code> </p>
<p> <code>nfs_t</code> </p>
<p> <code>nutups_cgi_rw_content_t</code> </p>
<p> <code>openshift_rw_content_t</code> </p>
<p> <code>passenger_tmp_t</code> </p>
<p> <code>passenger_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/passenger(/.*)?</p>
<p> <code>passenger_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/passenger(/.*)?</p>
<p> <code>pki_apache_config</code> </p>
<p> <code>pki_apache_var_lib</code> </p>
<p> <code>pki_apache_var_log</code> </p>
<p> <code>postfix_spool_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix/defer(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix/flush(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix/deferred(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix/maildrop(/.*)?</p>
<p> <code>preupgrade_data_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/preupgrade(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/preupgrade(/.*)?</p>
<p> <code>prewikka_rw_content_t</code> </p>
<p> <code>public_content_rw_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/abrt-upload(/.*)?</p>
<p> <code>root_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/initrd</p>
<p> <code>security_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/selinux</p>
<p> <code>smokeping_cgi_rw_content_t</code> </p>
<p> <code>squid_rw_content_t</code> </p>
<p> <code>squirrelmail_spool_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/squirrelmail(/.*)?</p>
<p> <code>systemd_passwd_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/ask-password(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/ask-password-block(/.*)?</p>
<p> <code>w3c_validator_rw_content_t</code> </p>
<p> <code>webalizer_rw_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/usage(/.*)?</p>
<p> <code>zarafa_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/zarafa(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/zarafa-webapp(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/zarafa-webaccess(/.*)?</p>
<p> <code>zoneminder_rw_content_t</code> </p>
<p> <code>zoneminder_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/zoneminder(/.*)?</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux httpd policy is very flexible allowing users to setup their httpd processes in as secure a method as possible. </p>
<p> EQUIVALENCE DIRECTORIES</code> </p>
<p> httpd policy stores data with multiple different file context types under the /var/lib/php directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/lib/php /srv/php</code><br />
 <code>restorecon -R -v /srv/php</code> </p>
<p> httpd policy stores data with multiple different file context types under the /var/www directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/www /srv/www</code><br />
 <code>restorecon -R -v /srv/www</code> </p>
<p> <code>STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the httpd, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t httpd_var_run_t &#8216;/srv/myhttpd_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myhttpd_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for httpd:</i> </p>
<p> <code>httpd_cache_t</code> </p>
<p> &#8211; Set files with the httpd_cache_t type, if you want to store the files under the /var/cache directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/cache/rt(3|4)(/.*)?, /var/cache/ssl.*.sem, /var/cache/mod_.*, /var/cache/php-.*, /var/cache/httpd(/.*)?, /var/cache/mason(/.*)?, /var/cache/mod_ssl(/.*)?, /var/cache/lighttpd(/.*)?, /var/cache/mediawiki(/.*)?, /var/cache/mod_proxy(/.*)?, /var/cache/mod_gnutls(/.*)?, /var/cache/php-mmcache(/.*)?, /var/cache/php-eaccelerator(/.*)? </p>
</dl>
<p> <code>httpd_config_t</code> </p>
<p> &#8211; Set files with the httpd_config_t type, if you want to treat the files as httpd configuration data, usually stored under the /etc directory. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/httpd(/.*)?, /etc/nginx(/.*)?, /etc/<a href="/docs/linux/man/2-apache/">apache</a>(2)?(/.*)?, /etc/cherokee(/.*)?, /etc/lighttpd(/.*)?, /etc/<a href="/docs/linux/man/2-apache-ssl/">apache-ssl</a>(2)?(/.*)?, /var/lib/openshift/.httpd.d(/.*)?, /etc/opt/rh/rh-nginx18/nginx(/.*)?, /var/lib/stickshift/.httpd.d(/.*)?, /etc/vhosts, /etc/thttpd.conf </p>
</dl>
<p> <code>httpd_exec_t</code> </p>
<p> &#8211; Set files with the httpd_exec_t type, if you want to transition an executable to the httpd_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/httpd(.worker)?, /usr/sbin/<a href="/docs/linux/man/2-apache/">apache</a>(2)?, /usr/lib/apache-ssl/.+, /usr/sbin/<a href="/docs/linux/man/2-apache-ssl/">apache-ssl</a>(2)?, /usr/share/jetty/bin/jetty.sh, /usr/sbin/nginx, /usr/sbin/thttpd, /usr/sbin/php-fpm, /usr/sbin/cherokee, /usr/sbin/lighttpd, /usr/sbin/httpd.event, /usr/bin/mongrel_rails, /usr/sbin/htcacheclean </p>
</dl>
<p> <code>httpd_helper_exec_t</code> </p>
<p> &#8211; Set files with the httpd_helper_exec_t type, if you want to transition an executable to the httpd_helper_t domain. </p>
<p> <code>httpd_initrc_exec_t</code> </p>
<p> &#8211; Set files with the httpd_initrc_exec_t type, if you want to transition an executable to the httpd_initrc_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/init.d/cherokee, /etc/rc.d/init.d/httpd, /etc/rc.d/init.d/lighttpd </p>
</dl>
<p> <code>httpd_keytab_t</code> </p>
<p> &#8211; Set files with the httpd_keytab_t type, if you want to treat the files as kerberos keytab files. </p>
<p> <code>httpd_lock_t</code> </p>
<p> &#8211; Set files with the httpd_lock_t type, if you want to treat the files as httpd lock data, stored under the /var/lock directory </p>
<p> <code>httpd_log_t</code> </p>
<p> &#8211; Set files with the httpd_log_t type, if you want to treat the data as httpd log data, usually stored under the /var/log directory. </p>
<dl>
<dt>Paths:</p>
<dd>/srv/([^/]*/)?www/logs(/.*)?, /var/www(/.*)?/logs(/.*)?, /var/log/glpi(/.*)?, /var/log/cacti(/.*)?, /var/log/httpd(/.*)?, /var/log/nginx(/.*)?, /var/log/<a href="/docs/linux/man/2-apache/">apache</a>(2)?(/.*)?, /var/log/horizon(/.*)?, /var/log/php-fpm(/.*)?, /var/log/cherokee(/.*)?, /var/log/lighttpd(/.*)?, /var/log/suphp.log.*, /var/log/thttpd.log.*, /var/log/<a href="/docs/linux/man/2-apache-ssl/">apache-ssl</a>(2)?(/.*)?, /var/log/cgiwrap.log.*, /var/www/stickshift/[^/]*/log(/.*)?, /var/log/graphite-web(/.*)?, /var/www/miq/vmdb/log(/.*)?, /var/log/roundcubemail(/.*)?, /var/log/php_errors.log.*, /var/opt/rh/rh-nginx18/log(/.*)?, /var/log/dirsrv/admin-serv(/.*)?, /var/lib/openshift/.log/httpd(/.*)?, /var/www/openshift/console/log(/.*)?, /var/www/openshift/broker/httpd/logs(/.*)?, /var/www/openshift/console/httpd/logs(/.*)?, /etc/httpd/logs </p>
</dl>
<p> <code>httpd_modules_t</code> </p>
<p> &#8211; Set files with the httpd_modules_t type, if you want to treat the files as httpd modules. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/httpd(/.*)?, /usr/lib/apache(/.*)?, /usr/lib/cherokee(/.*)?, /usr/lib/lighttpd(/.*)?, /usr/lib/apache2/modules(/.*)?, /etc/httpd/modules </p>
</dl>
<p> <code>httpd_passwd_exec_t</code> </p>
<p> &#8211; Set files with the httpd_passwd_exec_t type, if you want to transition an executable to the httpd_passwd_t domain. </p>
<p> <code>httpd_php_exec_t</code> </p>
<p> &#8211; Set files with the httpd_php_exec_t type, if you want to transition an executable to the httpd_php_t domain. </p>
<p> <code>httpd_php_tmp_t</code> </p>
<p> &#8211; Set files with the httpd_php_tmp_t type, if you want to store httpd php temporary files in the /tmp directories. </p>
<p> <code>httpd_rotatelogs_exec_t</code> </p>
<p> &#8211; Set files with the httpd_rotatelogs_exec_t type, if you want to transition an executable to the httpd_rotatelogs_t domain. </p>
<p> <code>httpd_squirrelmail_t</code> </p>
<p> &#8211; Set files with the httpd_squirrelmail_t type, if you want to treat the files as httpd squirrelmail data. </p>
<p> <code>httpd_suexec_exec_t</code> </p>
<p> &#8211; Set files with the httpd_suexec_exec_t type, if you want to transition an executable to the httpd_suexec_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/<a href="/docs/linux/man/2-apache/">apache</a>(2)?/<a href="/docs/linux/man/2-suexec/">suexec</a>(2)?, /usr/lib/cgi-bin/(nph-)?cgiwrap(d)?, /usr/sbin/suexec </p>
</dl>
<p> <code>httpd_suexec_tmp_t</code> </p>
<p> &#8211; Set files with the httpd_suexec_tmp_t type, if you want to store httpd suexec temporary files in the /tmp directories. </p>
<p> <code>httpd_sys_content_t</code> </p>
<p> &#8211; Set files with the httpd_sys_content_t type, if you want to treat the files as httpd sys content. </p>
<dl>
<dt>Paths:</p>
<dd>/srv/([^/]*/)?www(/.*)?, /var/www(/.*)?, /etc/htdig(/.*)?, /srv/gallery2(/.*)?, /var/lib/trac(/.*)?, /var/lib/htdig(/.*)?, /var/www/icons(/.*)?, /usr/share/glpi(/.*)?, /usr/share/htdig(/.*)?, /usr/share/drupal.*, /usr/share/z-push(/.*)?, /var/www/svn/conf(/.*)?, /usr/share/icecast(/.*)?, /var/lib/cacti/rra(/.*)?, /usr/share/ntop/html(/.*)?, /usr/share/nginx/html(/.*)?, /usr/share/doc/ghc/html(/.*)?, /usr/share/openca/htdocs(/.*)?, /usr/share/selinux-policy[^/]*/html(/.*)? </p>
</dl>
<p> <code>httpd_sys_htaccess_t</code> </p>
<p> &#8211; Set files with the httpd_sys_htaccess_t type, if you want to treat the file as a httpd sys access file. </p>
<p> <code>httpd_sys_ra_content_t</code> </p>
<p> &#8211; Set files with the httpd_sys_ra_content_t type, if you want to treat the files as httpd sys read/append content. </p>
<p> <code>httpd_sys_rw_content_t</code> </p>
<p> &#8211; Set files with the httpd_sys_rw_content_t type, if you want to treat the files as httpd sys read/write content. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/glpi(/.*)?, /etc/horde(/.*)?, /etc/drupal.*, /etc/z-push(/.*)?, /var/lib/svn(/.*)?, /var/www/svn(/.*)?, /etc/owncloud(/.*)?, /var/www/html(/.*)?/uploads(/.*)?, /var/www/html(/.*)?/wp-content(/.*)?, /var/www/html(/.*)?/wp_backups(/.*)?, /var/www/html(/.*)?/sites/default/files(/.*)?, /var/www/html(/.*)?/sites/default/settings.php, /etc/mock/koji(/.*)?, /var/lib/drupal.*, /etc/zabbix/web(/.*)?, /var/lib/moodle(/.*)?, /var/log/z-push(/.*)?, /var/spool/gosa(/.*)?, /etc/WebCalendar(/.*)?, /usr/share/joomla(/.*)?, /var/lib/dokuwiki(/.*)?, /var/lib/owncloud(/.*)?, /var/spool/viewvc(/.*)?, /var/lib/pootle/po(/.*)?, /var/www/moodledata(/.*)?, /srv/gallery2/smarty(/.*)?, /var/www/moodle/data(/.*)?, /var/lib/graphite-web(/.*)?, /var/www/gallery/albums(/.*)?, /var/www/html/owncloud/data(/.*)?, /usr/share/wordpress-mu/wp-content(/.*)?, /usr/share/wordpress/wp-content/uploads(/.*)?, /usr/share/wordpress/wp-content/upgrade(/.*)?, /var/www/html/configuration.php </p>
</dl>
<p> <code>httpd_sys_script_exec_t</code> </p>
<p> &#8211; Set files with the httpd_sys_script_exec_t type, if you want to transition an executable to the httpd_sys_script_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/.*.cgi, /opt/.*.cgi, /var/www/[^/]*/cgi-bin(/.*)?, /var/www/perl(/.*)?, /var/www/html/[^/]*/cgi-bin(/.*)?, /usr/lib/cgi-bin(/.*)?, /var/www/cgi-bin(/.*)?, /var/www/svn/hooks(/.*)?, /usr/share/wordpress/.*.php, /usr/local/nagios/sbin(/.*)?, /usr/share/wordpress/wp-includes/.*.php, /usr/share/wordpress-mu/wp-config.php </p>
</dl>
<p> <code>httpd_tmp_t</code> </p>
<p> &#8211; Set files with the httpd_tmp_t type, if you want to store httpd temporary files in the /tmp directories. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/user/apache(/.*)?, /var/www/openshift/console/tmp(/.*)? </p>
</dl>
<p> <code>httpd_tmpfs_t</code> </p>
<p> &#8211; Set files with the httpd_tmpfs_t type, if you want to store httpd files on a tmpfs file system. </p>
<p> <code>httpd_unconfined_script_exec_t</code> </p>
<p> &#8211; Set files with the httpd_unconfined_script_exec_t type, if you want to transition an executable to the httpd_unconfined_script_t domain. </p>
<p> <code>httpd_unit_file_t</code> </p>
<p> &#8211; Set files with the httpd_unit_file_t type, if you want to treat the files as httpd unit content. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/systemd/system/httpd.*, /usr/lib/systemd/system/jetty.*, /usr/lib/systemd/system/nginx.*, /usr/lib/systemd/system/thttpd.*, /usr/lib/systemd/system/php-fpm.* </p>
</dl>
<p> <code>httpd_user_content_t</code> </p>
<p> &#8211; Set files with the httpd_user_content_t type, if you want to treat the files as httpd user content. </p>
<p> <code>httpd_user_htaccess_t</code> </p>
<p> &#8211; Set files with the httpd_user_htaccess_t type, if you want to treat the file as a httpd user access file. </p>
<p> <code>httpd_user_ra_content_t</code> </p>
<p> &#8211; Set files with the httpd_user_ra_content_t type, if you want to treat the files as httpd user read/append content. </p>
<p> <code>httpd_user_rw_content_t</code> </p>
<p> &#8211; Set files with the httpd_user_rw_content_t type, if you want to treat the files as httpd user read/write content. </p>
<p> <code>httpd_user_script_exec_t</code> </p>
<p> &#8211; Set files with the httpd_user_script_exec_t type, if you want to transition an executable to the httpd_user_script_t domain. </p>
<p> <code>httpd_var_lib_t</code> </p>
<p> &#8211; Set files with the httpd_var_lib_t type, if you want to store the httpd files under the /var/lib directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/rt(3|4)/data/RT-Shredder(/.*)?, /var/lib/dav(/.*)?, /var/lib/php(/.*)?, /var/lib/glpi(/.*)?, /var/lib/httpd(/.*)?, /var/lib/nginx(/.*)?, /var/lib/z-push(/.*)?, /var/lib/ganglia(/.*)?, /var/lib/ipsilon(/.*)?, /var/lib/cherokee(/.*)?, /var/lib/lighttpd(/.*)?, /var/lib/mod_security(/.*)?, /var/lib/roundcubemail(/.*)?, /var/opt/rh/rh-nginx18/lib/nginx(/.*)? </p>
</dl>
<p> <code>httpd_var_run_t</code> </p>
<p> &#8211; Set files with the httpd_var_run_t type, if you want to store the httpd files under the /run or /var/run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/wsgi.*, /var/run/mod_.*, /var/run/httpd.*, /var/run/nginx.*, /var/run/apache.*, /var/run/php-fpm(/.*)?, /var/run/lighttpd(/.*)?, /var/lib/php/session(/.*)?, /var/lib/php/wsdlcache(/.*)?, /var/run/dirsrv/admin-serv.*, /var/opt/rh/rh-nginx18/run/nginx(/.*)?, /var/www/openshift/broker/httpd/run(/.*)?, /var/www/openshift/console/httpd/run(/.*)?, /opt/dirsrv/var/run/dirsrv/dsgw/cookies(/.*)?, /var/run/thttpd.pid, /var/run/gcache_port, /var/run/cherokee.pid </p>
</dl>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Sharing Files</h2>
<p>If you want to share files with multiple domains (Apache, FTP, rsync, Samba), you can set a file context of public_content_t and public_content_rw_t. These context allow any of the above domains to read the content. If you want a particular domain to write to the public_content_rw_t domain, you must set the appropriate boolean.</p>
<dl>
<dt>Allow httpd servers to read the /var/httpd directory by adding the public_content_t file type to the directory and by restoring the file type.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_t &quot;/var/httpd(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/httpd</code></p>
<dl>
<dt>Allow httpd servers to read and write /var/httpd/incoming by adding the public_content_rw_t type to the directory and by restoring the file type. You also need to turn on the httpd_anon_write boolean.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_rw_t &quot;/var/httpd/incoming(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/httpd/incoming</code><br />
 <code>setsebool -P httpd_anon_write 1</code> </p>
<p> If you want to allow Apache to modify public files used for public file transfer services. Directories/Files must be labeled public_content_rw_t., you must turn on the httpd_anon_write boolean. </p>
<p> <code>setsebool -P httpd_anon_write 1</code></p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-httpd/">httpd</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-httpd_helper_selinux/">httpd_helper_selinux</a>(8), <a href="/docs/linux/man/8-httpd_passwd_selinux/">httpd_passwd_selinux</a>(8), <a href="/docs/linux/man/8-httpd_php_selinux/">httpd_php_selinux</a>(8), <a href="/docs/linux/man/8-httpd_rotatelogs_selinux/">httpd_rotatelogs_selinux</a>(8), <a href="/docs/linux/man/8-httpd_suexec_selinux/">httpd_suexec_selinux</a>(8), <a href="/docs/linux/man/8-httpd_sys_script_selinux/">httpd_sys_script_selinux</a>(8), <a href="/docs/linux/man/8-httpd_unconfined_script_selinux/">httpd_unconfined_script_selinux</a>(8), <a href="/docs/linux/man/8-httpd_user_script_selinux/">httpd_user_script_selinux</a>(8) </p>
