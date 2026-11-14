---
title: "nagios_selinux(8)"
name: "nagios_selinux"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nagios_selinux/"
description: "nagios_selinux – Security Enhanced Linux Policy for the nagios processes"
---

<p>nagios_selinux &#8211; Security Enhanced Linux Policy for the nagios processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the nagios processes via flexible mandatory access control. The nagios processes execute with the nagios_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep nagios_t</code> </p>
<h2>Entrypoints</h2>
<p>The nagios_t SELinux type can be entered via the <code>nagios_exec_t</code> file type. </p>
<p> The default entrypoint paths for the nagios_t domain are the following: </p>
<p> /usr/bin/nagios, /usr/bin/icinga, /usr/sbin/nagios, /usr/sbin/icinga</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux nagios policy is very flexible allowing users to setup their nagios processes in as secure a method as possible. </p>
<p> The following process types are defined for nagios: </p>
<p> nagios_t, nagios_admin_plugin_t, nagios_checkdisk_plugin_t, nagios_mail_plugin_t, nagios_services_plugin_t, nagios_system_plugin_t, nagios_unconfined_plugin_t, nagios_eventhandler_plugin_t, nagios_openshift_plugin_t, nagios_script_t</code> </p>
<p> Note: <code>semanage permissive -a nagios_t</code> can be used to make the process type nagios_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. nagios policy is extremely flexible and has several booleans that allow you to manipulate the policy and run nagios with the tightest access possible. </p>
<p> If you want to allow nagios run in conjunction with PNP4Nagios, you must turn on the nagios_run_pnp4nagios boolean. Disabled by default. </p>
<p> <code>setsebool -P nagios_run_pnp4nagios 1</code> </p>
<p> If you want to allow nagios/nrpe to call sudo from NRPE utils scripts, you must turn on the nagios_run_sudo boolean. Disabled by default. </p>
<p> <code>setsebool -P nagios_run_sudo 1</code> </p>
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
<p>The SELinux process type nagios_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
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
<p> <code>nagios_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/nagios(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/icinga(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/netsaint(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/pnp4nagios(/.*)?</p>
<p> <code>nagios_spool_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/nagios(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/icinga(/.*)?</p>
<p> <code>nagios_tmp_t</code> </p>
<p> <code>nagios_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/pnp4nagios(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/lib/pnp4nagios(/.*)?</p>
<p> <code>nagios_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/nagios.*</p>
<p> <code>root_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/initrd</p>
<p> <code>security_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/selinux</p>
<p> <code>sudo_db_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/db/sudo(/.*)?</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux nagios policy is very flexible allowing users to setup their nagios processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the nagios, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t nagios_var_run_t &#8216;/srv/mynagios_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mynagios_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for nagios:</i> </p>
<p> <code>nagios_admin_plugin_exec_t</code> </p>
<p> &#8211; Set files with the nagios_admin_plugin_exec_t type, if you want to transition an executable to the nagios_admin_plugin_t domain. </p>
<p> <code>nagios_checkdisk_plugin_exec_t</code> </p>
<p> &#8211; Set files with the nagios_checkdisk_plugin_exec_t type, if you want to transition an executable to the nagios_checkdisk_plugin_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/nagios/plugins/check_disk, /usr/lib/nagios/plugins/check_disk_smb, /usr/lib/nagios/plugins/check_ide_smart, /usr/lib/nagios/plugins/check_linux_raid </p>
</dl>
<p> <code>nagios_content_t</code> </p>
<p> &#8211; Set files with the nagios_content_t type, if you want to treat the files as nagios content. </p>
<p> <code>nagios_etc_t</code> </p>
<p> &#8211; Set files with the nagios_etc_t type, if you want to store nagios files in the /etc directories. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/nagios(/.*)?, /etc/icinga(/.*)?, /etc/pnp4nagios(/.*)? </p>
</dl>
<p> <code>nagios_eventhandler_plugin_exec_t</code> </p>
<p> &#8211; Set files with the nagios_eventhandler_plugin_exec_t type, if you want to transition an executable to the nagios_eventhandler_plugin_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/nagios/plugins/eventhandlers(/.*), /usr/lib/icinga/plugins/eventhandlers(/.*) </p>
</dl>
<p> <code>nagios_eventhandler_plugin_tmp_t</code> </p>
<p> &#8211; Set files with the nagios_eventhandler_plugin_tmp_t type, if you want to store nagios eventhandler plugin temporary files in the /tmp directories. </p>
<p> <code>nagios_exec_t</code> </p>
<p> &#8211; Set files with the nagios_exec_t type, if you want to transition an executable to the nagios_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/nagios, /usr/bin/icinga, /usr/sbin/nagios, /usr/sbin/icinga </p>
</dl>
<p> <code>nagios_htaccess_t</code> </p>
<p> &#8211; Set files with the nagios_htaccess_t type, if you want to treat the file as a nagios access file. </p>
<p> <code>nagios_initrc_exec_t</code> </p>
<p> &#8211; Set files with the nagios_initrc_exec_t type, if you want to transition an executable to the nagios_initrc_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/rc.d/init.d/nrpe, /etc/rc.d/init.d/nagios </p>
</dl>
<p> <code>nagios_log_t</code> </p>
<p> &#8211; Set files with the nagios_log_t type, if you want to treat the data as nagios log data, usually stored under the /var/log directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/log/nagios(/.*)?, /var/log/icinga(/.*)?, /var/log/netsaint(/.*)?, /var/log/pnp4nagios(/.*)? </p>
</dl>
<p> <code>nagios_mail_plugin_exec_t</code> </p>
<p> &#8211; Set files with the nagios_mail_plugin_exec_t type, if you want to transition an executable to the nagios_mail_plugin_t domain. </p>
<p> <code>nagios_openshift_plugin_exec_t</code> </p>
<p> &#8211; Set files with the nagios_openshift_plugin_exec_t type, if you want to transition an executable to the nagios_openshift_plugin_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib64/nagios/plugins/check_node_accept_status, /usr/lib64/nagios/plugins/check_number_openshift_apps </p>
</dl>
<p> <code>nagios_openshift_plugin_tmp_t</code> </p>
<p> &#8211; Set files with the nagios_openshift_plugin_tmp_t type, if you want to store nagios openshift plugin temporary files in the /tmp directories. </p>
<p> <code>nagios_ra_content_t</code> </p>
<p> &#8211; Set files with the nagios_ra_content_t type, if you want to treat the files as nagios read/append content. </p>
<p> <code>nagios_rw_content_t</code> </p>
<p> &#8211; Set files with the nagios_rw_content_t type, if you want to treat the files as nagios read/write content. </p>
<p> <code>nagios_script_exec_t</code> </p>
<p> &#8211; Set files with the nagios_script_exec_t type, if you want to transition an executable to the nagios_script_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/nagios/cgi(/.*)?, /usr/lib/icinga/cgi(/.*)?, /usr/lib/cgi-bin/nagios(/.+)?, /usr/lib/nagios/cgi-bin(/.*)?, /usr/lib/cgi-bin/netsaint(/.*)? </p>
</dl>
<p> <code>nagios_services_plugin_exec_t</code> </p>
<p> &#8211; Set files with the nagios_services_plugin_exec_t type, if you want to transition an executable to the nagios_services_plugin_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/nagios/plugins/check_ntp.*, /usr/lib/nagios/plugins/check_snmp.*, /usr/lib/nagios/plugins/check_nt, /usr/lib/nagios/plugins/check_dig, /usr/lib/nagios/plugins/check_dns, /usr/lib/nagios/plugins/check_rpc, /usr/lib/nagios/plugins/check_tcp, /usr/lib/nagios/plugins/check_sip, /usr/lib/nagios/plugins/check_ssh, /usr/lib/nagios/plugins/check_ups, /usr/lib/nagios/plugins/check_dhcp, /usr/lib/nagios/plugins/check_game, /usr/lib/nagios/plugins/check_hpjd, /usr/lib/nagios/plugins/check_http, /usr/lib/nagios/plugins/check_icmp, /usr/lib/nagios/plugins/check_ircd, /usr/lib/nagios/plugins/check_ldap, /usr/lib/nagios/plugins/check_nrpe, /usr/lib/nagios/plugins/check_ping, /usr/lib/nagios/plugins/check_real, /usr/lib/nagios/plugins/check_time, /usr/lib/nagios/plugins/check_smtp, /usr/lib/nagios/plugins/check_dummy, /usr/lib/nagios/plugins/check_fping, /usr/lib/nagios/plugins/check_mysql, /usr/lib/nagios/plugins/check_pgsql, /usr/lib/nagios/plugins/check_breeze, /usr/lib/nagios/plugins/check_oracle, /usr/lib/nagios/plugins/check_radius, /usr/lib/nagios/plugins/check_cluster, /usr/lib/nagios/plugins/check_mysql_query </p>
</dl>
<p> <code>nagios_spool_t</code> </p>
<p> &#8211; Set files with the nagios_spool_t type, if you want to store the nagios files under the /var/spool directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/spool/nagios(/.*)?, /var/spool/icinga(/.*)? </p>
</dl>
<p> <code>nagios_system_plugin_exec_t</code> </p>
<p> &#8211; Set files with the nagios_system_plugin_exec_t type, if you want to transition an executable to the nagios_system_plugin_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/nagios/plugins/check_log, /usr/lib/nagios/plugins/check_load, /usr/lib/nagios/plugins/check_mrtg, /usr/lib/nagios/plugins/check_swap, /usr/lib/nagios/plugins/check_wave, /usr/lib/nagios/plugins/check_procs, /usr/lib/nagios/plugins/check_users, /usr/lib/nagios/plugins/check_flexlm, /usr/lib/nagios/plugins/check_nagios, /usr/lib/nagios/plugins/check_nwstat, /usr/lib/nagios/plugins/check_overcr, /usr/lib/nagios/plugins/check_sensors, /usr/lib/nagios/plugins/check_ifstatus, /usr/lib/nagios/plugins/check_mrtgtraf, /usr/lib/nagios/plugins/check_ifoperstatus </p>
</dl>
<p> <code>nagios_system_plugin_tmp_t</code> </p>
<p> &#8211; Set files with the nagios_system_plugin_tmp_t type, if you want to store nagios system plugin temporary files in the /tmp directories. </p>
<p> <code>nagios_tmp_t</code> </p>
<p> &#8211; Set files with the nagios_tmp_t type, if you want to store nagios temporary files in the /tmp directories. </p>
<p> <code>nagios_unconfined_plugin_exec_t</code> </p>
<p> &#8211; Set files with the nagios_unconfined_plugin_exec_t type, if you want to transition an executable to the nagios_unconfined_plugin_t domain. </p>
<p> <code>nagios_var_lib_t</code> </p>
<p> &#8211; Set files with the nagios_var_lib_t type, if you want to store the nagios files under the /var/lib directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/pnp4nagios(/.*)?, /usr/lib/pnp4nagios(/.*)? </p>
</dl>
<p> <code>nagios_var_run_t</code> </p>
<p> &#8211; Set files with the nagios_var_run_t type, if you want to store the nagios files under the /run or /var/run directory. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-nagios/">nagios</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-nagios_admin_plugin_selinux/">nagios_admin_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_admin_plugin_selinux/">nagios_admin_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_checkdisk_plugin_selinux/">nagios_checkdisk_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_checkdisk_plugin_selinux/">nagios_checkdisk_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_eventhandler_plugin_selinux/">nagios_eventhandler_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_eventhandler_plugin_selinux/">nagios_eventhandler_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_mail_plugin_selinux/">nagios_mail_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_mail_plugin_selinux/">nagios_mail_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_openshift_plugin_selinux/">nagios_openshift_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_openshift_plugin_selinux/">nagios_openshift_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_script_selinux/">nagios_script_selinux</a>(8), <a href="/docs/linux/man/8-nagios_script_selinux/">nagios_script_selinux</a>(8), <a href="/docs/linux/man/8-nagios_services_plugin_selinux/">nagios_services_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_services_plugin_selinux/">nagios_services_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_system_plugin_selinux/">nagios_system_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_system_plugin_selinux/">nagios_system_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_unconfined_plugin_selinux/">nagios_unconfined_plugin_selinux</a>(8), <a href="/docs/linux/man/8-nagios_unconfined_plugin_selinux/">nagios_unconfined_plugin_selinux</a>(8) </p>
