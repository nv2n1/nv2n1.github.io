---
title: "zabbix_selinux(8)"
name: "zabbix_selinux"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zabbix_selinux/"
description: "zabbix_selinux – Security Enhanced Linux Policy for the zabbix processes"
---

<p>zabbix_selinux &#8211; Security Enhanced Linux Policy for the zabbix processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the zabbix processes via flexible mandatory access control. The zabbix processes execute with the zabbix_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep zabbix_t</code> </p>
<h2>Entrypoints</h2>
<p>The zabbix_t SELinux type can be entered via the <code>zabbix_exec_t</code> file type. </p>
<p> The default entrypoint paths for the zabbix_t domain are the following: </p>
<p> /usr/bin/zabbix_server, /usr/sbin/zabbix_proxy, /usr/sbin/zabbix_server, /usr/sbin/zabbix_proxy_mysql, /usr/sbin/zabbix_proxy_pgsql, /usr/sbin/zabbix_server_mysql, /usr/sbin/zabbix_server_pgsql, /usr/sbin/zabbix_proxy_sqlite3, /usr/sbin/zabbix_server_sqlite3</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux zabbix policy is very flexible allowing users to setup their zabbix processes in as secure a method as possible. </p>
<p> The following process types are defined for zabbix: </p>
<p> zabbix_t, zabbix_agent_t, zabbix_script_t</code> </p>
<p> Note: <code>semanage permissive -a zabbix_t</code> can be used to make the process type zabbix_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. zabbix policy is extremely flexible and has several booleans that allow you to manipulate the policy and run zabbix with the tightest access possible. </p>
<p> If you want to determine whether zabbix can connect to all TCP ports, you must turn on the zabbix_can_network boolean. Disabled by default. </p>
<p> <code>setsebool -P zabbix_can_network 1</code> </p>
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
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux zabbix policy is very flexible allowing users to setup their zabbix processes in as secure a method as possible. </p>
<p> The following port types are defined for zabbix: </p>
<dl>
<dt><code>zabbix_agent_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 10050 </p>
<dt><code>zabbix_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 10051</dl>
<h2>Managed Files</h2>
<p>The SELinux process type zabbix_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
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
<p> <code>root_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/initrd</p>
<p> <code>zabbix_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/zabbix.*</p>
<p> <code>zabbix_tmp_t</code> </p>
<p> <code>zabbix_tmpfs_t</code> </p>
<p> <code>zabbix_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/zabbix(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/zabbixsrv(/.*)?</p>
<p> <code>zabbix_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/zabbix(/.*)?</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux zabbix policy is very flexible allowing users to setup their zabbix processes in as secure a method as possible. </p>
<p> EQUIVALENCE DIRECTORIES</code> </p>
<p> zabbix policy stores data with multiple different file context types under the /var/lib/zabbix directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/lib/zabbix /srv/zabbix</code><br />
 <code>restorecon -R -v /srv/zabbix</code> </p>
<p> <code>STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the zabbix, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t zabbixd_var_lib_t &#8216;/srv/myzabbix_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myzabbix_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for zabbix:</i> </p>
<p> <code>zabbix_agent_exec_t</code> </p>
<p> &#8211; Set files with the zabbix_agent_exec_t type, if you want to transition an executable to the zabbix_agent_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/zabbix_agentd, /usr/sbin/zabbix_agentd </p>
</dl>
<p> <code>zabbix_agent_initrc_exec_t</code> </p>
<p> &#8211; Set files with the zabbix_agent_initrc_exec_t type, if you want to transition an executable to the zabbix_agent_initrc_t domain. </p>
<p> <code>zabbix_exec_t</code> </p>
<p> &#8211; Set files with the zabbix_exec_t type, if you want to transition an executable to the zabbix_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/zabbix_server, /usr/sbin/zabbix_proxy, /usr/sbin/zabbix_server, /usr/sbin/zabbix_proxy_mysql, /usr/sbin/zabbix_proxy_pgsql, /usr/sbin/zabbix_server_mysql, /usr/sbin/zabbix_server_pgsql, /usr/sbin/zabbix_proxy_sqlite3, /usr/sbin/zabbix_server_sqlite3 </p>
</dl>
<p> <code>zabbix_initrc_exec_t</code> </p>
<p> &#8211; Set files with the zabbix_initrc_exec_t type, if you want to transition an executable to the zabbix_initrc_t domain. </p>
<p> <code>zabbix_log_t</code> </p>
<p> &#8211; Set files with the zabbix_log_t type, if you want to treat the data as zabbix log data, usually stored under the /var/log directory. </p>
<p> <code>zabbix_script_exec_t</code> </p>
<p> &#8211; Set files with the zabbix_script_exec_t type, if you want to transition an executable to the zabbix_script_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/zabbix/externalscripts(/.*)?, /var/lib/zabbix/externalscripts(/.*)? </p>
</dl>
<p> <code>zabbix_tmp_t</code> </p>
<p> &#8211; Set files with the zabbix_tmp_t type, if you want to store zabbix temporary files in the /tmp directories. </p>
<p> <code>zabbix_tmpfs_t</code> </p>
<p> &#8211; Set files with the zabbix_tmpfs_t type, if you want to store zabbix files on a tmpfs file system. </p>
<p> <code>zabbix_var_lib_t</code> </p>
<p> &#8211; Set files with the zabbix_var_lib_t type, if you want to store the zabbix files under the /var/lib directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/zabbix(/.*)?, /var/lib/zabbixsrv(/.*)? </p>
</dl>
<p> <code>zabbix_var_run_t</code> </p>
<p> &#8211; Set files with the zabbix_var_run_t type, if you want to store the zabbix files under the /run or /var/run directory. </p>
<p> <code>zabbixd_var_lib_t</code> </p>
<p> &#8211; Set files with the zabbixd_var_lib_t type, if you want to store the zabbixd files under the /var/lib directory. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-zabbix/">zabbix</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-zabbix_agent_selinux/">zabbix_agent_selinux</a>(8), <a href="/docs/linux/man/8-zabbix_agent_selinux/">zabbix_agent_selinux</a>(8), <a href="/docs/linux/man/8-zabbix_script_selinux/">zabbix_script_selinux</a>(8), <a href="/docs/linux/man/8-zabbix_script_selinux/">zabbix_script_selinux</a>(8) </p>
