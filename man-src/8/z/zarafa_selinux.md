---
title: "zarafa_selinux(8)"
name: "zarafa_selinux"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zarafa_selinux/"
description: "zarafa_selinux – Security Enhanced Linux Policy for the zarafa processes"
---

<p>zarafa_selinux &#8211; Security Enhanced Linux Policy for the zarafa processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the zarafa processes via flexible mandatory access control. </p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the zarafa_deliver_t, zarafa_spooler_t, zarafa_gateway_t, zarafa_ical_t, zarafa_server_t, zarafa_monitor_t, zarafa_indexer_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the zarafa_deliver_t, zarafa_spooler_t, zarafa_gateway_t, zarafa_ical_t, zarafa_server_t, zarafa_monitor_t, zarafa_indexer_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the zarafa_deliver_t, zarafa_spooler_t, zarafa_gateway_t, zarafa_ical_t, zarafa_server_t, zarafa_monitor_t, zarafa_indexer_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux zarafa policy is very flexible allowing users to setup their zarafa processes in as secure a method as possible. </p>
<p> The following file types are defined for zarafa: </p>
<p> zarafa_deliver_exec_t </code> </p>
<p> &#8211; Set files with the zarafa_deliver_exec_t type, if you want to transition an executable to the zarafa_deliver_t domain. </p>
<p> <code>zarafa_deliver_log_t </code> </p>
<p> &#8211; Set files with the zarafa_deliver_log_t type, if you want to treat the data as zarafa deliver log data, usually stored under the /var/log directory. </p>
<p> <code>zarafa_deliver_tmp_t </code> </p>
<p> &#8211; Set files with the zarafa_deliver_tmp_t type, if you want to store zarafa deliver temporary files in the /tmp directories. </p>
<p> <code>zarafa_deliver_var_run_t </code> </p>
<p> &#8211; Set files with the zarafa_deliver_var_run_t type, if you want to store the zarafa deliver files under the /run directory. </p>
<p> <code>zarafa_etc_t </code> </p>
<p> &#8211; Set files with the zarafa_etc_t type, if you want to store zarafa files in the /etc directories. </p>
<p> <code>zarafa_gateway_exec_t </code> </p>
<p> &#8211; Set files with the zarafa_gateway_exec_t type, if you want to transition an executable to the zarafa_gateway_t domain. </p>
<p> <code>zarafa_gateway_log_t </code> </p>
<p> &#8211; Set files with the zarafa_gateway_log_t type, if you want to treat the data as zarafa gateway log data, usually stored under the /var/log directory. </p>
<p> <code>zarafa_gateway_var_run_t </code> </p>
<p> &#8211; Set files with the zarafa_gateway_var_run_t type, if you want to store the zarafa gateway files under the /run directory. </p>
<p> <code>zarafa_ical_exec_t </code> </p>
<p> &#8211; Set files with the zarafa_ical_exec_t type, if you want to transition an executable to the zarafa_ical_t domain. </p>
<p> <code>zarafa_ical_log_t </code> </p>
<p> &#8211; Set files with the zarafa_ical_log_t type, if you want to treat the data as zarafa ical log data, usually stored under the /var/log directory. </p>
<p> <code>zarafa_ical_var_run_t </code> </p>
<p> &#8211; Set files with the zarafa_ical_var_run_t type, if you want to store the zarafa ical files under the /run directory. </p>
<p> <code>zarafa_indexer_exec_t </code> </p>
<p> &#8211; Set files with the zarafa_indexer_exec_t type, if you want to transition an executable to the zarafa_indexer_t domain. </p>
<p> <code>zarafa_indexer_log_t </code> </p>
<p> &#8211; Set files with the zarafa_indexer_log_t type, if you want to treat the data as zarafa indexer log data, usually stored under the /var/log directory. </p>
<p> <code>zarafa_indexer_tmp_t </code> </p>
<p> &#8211; Set files with the zarafa_indexer_tmp_t type, if you want to store zarafa indexer temporary files in the /tmp directories. </p>
<p> <code>zarafa_indexer_var_run_t </code> </p>
<p> &#8211; Set files with the zarafa_indexer_var_run_t type, if you want to store the zarafa indexer files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/zarafa-indexer.pid, /var/run/zarafa-indexer </p>
</dl>
<p> <code>zarafa_monitor_exec_t </code> </p>
<p> &#8211; Set files with the zarafa_monitor_exec_t type, if you want to transition an executable to the zarafa_monitor_t domain. </p>
<p> <code>zarafa_monitor_log_t </code> </p>
<p> &#8211; Set files with the zarafa_monitor_log_t type, if you want to treat the data as zarafa monitor log data, usually stored under the /var/log directory. </p>
<p> <code>zarafa_monitor_var_run_t </code> </p>
<p> &#8211; Set files with the zarafa_monitor_var_run_t type, if you want to store the zarafa monitor files under the /run directory. </p>
<p> <code>zarafa_server_exec_t </code> </p>
<p> &#8211; Set files with the zarafa_server_exec_t type, if you want to transition an executable to the zarafa_server_t domain. </p>
<p> <code>zarafa_server_log_t </code> </p>
<p> &#8211; Set files with the zarafa_server_log_t type, if you want to treat the data as zarafa server log data, usually stored under the /var/log directory. </p>
<p> <code>zarafa_server_tmp_t </code> </p>
<p> &#8211; Set files with the zarafa_server_tmp_t type, if you want to store zarafa server temporary files in the /tmp directories. </p>
<p> <code>zarafa_server_var_run_t </code> </p>
<p> &#8211; Set files with the zarafa_server_var_run_t type, if you want to store the zarafa server files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/zarafa, /var/run/zarafa-server.pid </p>
</dl>
<p> <code>zarafa_share_t </code> </p>
<p> &#8211; Set files with the zarafa_share_t type, if you want to treat the files as zarafa share data. </p>
<p> <code>zarafa_spooler_exec_t </code> </p>
<p> &#8211; Set files with the zarafa_spooler_exec_t type, if you want to transition an executable to the zarafa_spooler_t domain. </p>
<p> <code>zarafa_spooler_log_t </code> </p>
<p> &#8211; Set files with the zarafa_spooler_log_t type, if you want to treat the data as zarafa spooler log data, usually stored under the /var/log directory. </p>
<p> <code>zarafa_spooler_var_run_t </code> </p>
<p> &#8211; Set files with the zarafa_spooler_var_run_t type, if you want to store the zarafa spooler files under the /run directory. </p>
<p> <code>zarafa_var_lib_t </code> </p>
<p> &#8211; Set files with the zarafa_var_lib_t type, if you want to store the zarafa files under the /var/lib directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/zarafa-webaccess(/.*)?, /var/lib/zarafa(/.*)? </p>
</dl>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux zarafa policy is very flexible allowing users to setup their zarafa processes in as secure a method as possible. </p>
<p> The following port types are defined for zarafa: </p>
<dl>
<dt><code>zarafa_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 236,237</dl>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux zarafa policy is very flexible allowing users to setup their zarafa processes in as secure a method as possible. </p>
<p> The following process types are defined for zarafa: </p>
<p> zarafa_gateway_t, zarafa_spooler_t, zarafa_deliver_t, zarafa_monitor_t, zarafa_indexer_t, zarafa_server_t, zarafa_ical_t </code> </p>
<p> Note: <code>semanage permissive -a PROCESS_TYPE </code> can be used to make a process type permissive. Permissive process types are not denied access by SELinux. AVC messages will still be generated.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage port</code> can also be used to manipulate the port definitions </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-zarafa/">zarafa</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) </p>
