---
title: "abrt_selinux(8)"
name: "abrt_selinux"
section: "8"
letter: "a"
url: "/docs/linux/man/8-abrt_selinux/"
description: "abrt_selinux – Security Enhanced Linux Policy for the abrt processes"
---

<p>abrt_selinux &#8211; Security Enhanced Linux Policy for the abrt processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the abrt processes via flexible mandatory access control. The abrt processes execute with the abrt_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep abrt_t</code> </p>
<h2>Entrypoints</h2>
<p>The abrt_t SELinux type can be entered via the <code>abrt_exec_t</code> file type. </p>
<p> The default entrypoint paths for the abrt_t domain are the following: </p>
<p> /usr/sbin/abrt-harvest.*, /usr/sbin/abrtd, /usr/sbin/abrt-dbus, /usr/sbin/abrt-install-ccpp-hook</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux abrt policy is very flexible allowing users to setup their abrt processes in as secure a method as possible. </p>
<p> The following process types are defined for abrt: </p>
<p> abrt_t, abrt_dump_oops_t, abrt_handle_event_t, abrt_helper_t, abrt_retrace_worker_t, abrt_retrace_coredump_t, abrt_watch_log_t, abrt_upload_watch_t</code> </p>
<p> Note: <code>semanage permissive -a abrt_t</code> can be used to make the process type abrt_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. abrt policy is extremely flexible and has several booleans that allow you to manipulate the policy and run abrt with the tightest access possible. </p>
<p> If you want to determine whether ABRT can run in the abrt_handle_event_t domain to handle ABRT event scripts, you must turn on the abrt_handle_event boolean. Disabled by default. </p>
<p> <code>setsebool -P abrt_handle_event 1</code> </p>
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
<p>The SELinux process type abrt_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>abrt_etc_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/abrt(/.*)?</p>
<p> <code>abrt_tmp_t</code> </p>
<p> <code>abrt_upload_watch_tmp_t</code> </p>
<p> <code>abrt_var_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/abrt(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/abrt(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/abrt(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/debug(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/abrt-di(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/rhsm/debug(/.*)?</p>
<p> <code>abrt_var_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/abrt-logger.*</p>
<p> <code>abrt_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/abrt(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/abrtd?.lock</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/abrtd?.socket</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/abrt.pid</p>
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
<p> <code>mock_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/mock(/.*)?</p>
<p> <code>public_content_rw_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/abrt-upload(/.*)?</p>
<p> <code>root_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/initrd</p>
<p> <code>rpm_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/yum.log.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/up2date.*</p>
<p> <code>rpm_var_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/yum(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/dnf(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/up2date(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/PackageKit(/.*)?</p>
<p> <code>rpm_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/yum.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/PackageKit(/.*)?</p>
<p> <code>sysfs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/sys(/.*)?</p>
<p> <code>usermodehelper_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/sys/kernel/uevent_helper</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux abrt policy is very flexible allowing users to setup their abrt processes in as secure a method as possible. </p>
<p> EQUIVALENCE DIRECTORIES</code> </p>
<p> abrt policy stores data with multiple different file context types under the /var/cache/abrt directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/cache/abrt /srv/abrt</code><br />
 <code>restorecon -R -v /srv/abrt</code> </p>
<p> abrt policy stores data with multiple different file context types under the /var/spool/abrt directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/spool/abrt /srv/abrt</code><br />
 <code>restorecon -R -v /srv/abrt</code> </p>
<p> abrt policy stores data with multiple different file context types under the /var/run/abrt directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/run/abrt /srv/abrt</code><br />
 <code>restorecon -R -v /srv/abrt</code> </p>
<p> <code>STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the abrt, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t abrt_var_run_t &#8216;/srv/myabrt_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myabrt_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for abrt:</i> </p>
<p> <code>abrt_dump_oops_exec_t</code> </p>
<p> &#8211; Set files with the abrt_dump_oops_exec_t type, if you want to transition an executable to the abrt_dump_oops_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/abrt-dump-.*, /usr/bin/abrt-uefioops-oops, /usr/libexec/abrt-hook-ccpp </p>
</dl>
<p> <code>abrt_etc_t</code> </p>
<p> &#8211; Set files with the abrt_etc_t type, if you want to store abrt files in the /etc directories. </p>
<p> <code>abrt_exec_t</code> </p>
<p> &#8211; Set files with the abrt_exec_t type, if you want to transition an executable to the abrt_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/abrt-harvest.*, /usr/sbin/abrtd, /usr/sbin/abrt-dbus, /usr/sbin/abrt-install-ccpp-hook </p>
</dl>
<p> <code>abrt_handle_event_exec_t</code> </p>
<p> &#8211; Set files with the abrt_handle_event_exec_t type, if you want to transition an executable to the abrt_handle_event_t domain. </p>
<p> <code>abrt_helper_exec_t</code> </p>
<p> &#8211; Set files with the abrt_helper_exec_t type, if you want to transition an executable to the abrt_helper_t domain. </p>
<p> <code>abrt_initrc_exec_t</code> </p>
<p> &#8211; Set files with the abrt_initrc_exec_t type, if you want to transition an executable to the abrt_initrc_t domain. </p>
<p> <code>abrt_retrace_cache_t</code> </p>
<p> &#8211; Set files with the abrt_retrace_cache_t type, if you want to store the files under the /var/cache directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/cache/abrt-retrace(/.*)?, /var/cache/retrace-server(/.*)? </p>
</dl>
<p> <code>abrt_retrace_coredump_exec_t</code> </p>
<p> &#8211; Set files with the abrt_retrace_coredump_exec_t type, if you want to transition an executable to the abrt_retrace_coredump_t domain. </p>
<p> <code>abrt_retrace_spool_t</code> </p>
<p> &#8211; Set files with the abrt_retrace_spool_t type, if you want to store the abrt retrace files under the /var/spool directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/spool/faf(/.*)?, /var/spool/abrt-retrace(/.*)?, /var/spool/retrace-server(/.*)? </p>
</dl>
<p> <code>abrt_retrace_worker_exec_t</code> </p>
<p> &#8211; Set files with the abrt_retrace_worker_exec_t type, if you want to transition an executable to the abrt_retrace_worker_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/abrt-retrace-worker, /usr/bin/retrace-server-worker </p>
</dl>
<p> <code>abrt_tmp_t</code> </p>
<p> &#8211; Set files with the abrt_tmp_t type, if you want to store abrt temporary files in the /tmp directories. </p>
<p> <code>abrt_unit_file_t</code> </p>
<p> &#8211; Set files with the abrt_unit_file_t type, if you want to treat the files as abrt unit content. </p>
<p> <code>abrt_upload_watch_exec_t</code> </p>
<p> &#8211; Set files with the abrt_upload_watch_exec_t type, if you want to transition an executable to the abrt_upload_watch_t domain. </p>
<p> <code>abrt_upload_watch_tmp_t</code> </p>
<p> &#8211; Set files with the abrt_upload_watch_tmp_t type, if you want to store abrt upload watch temporary files in the /tmp directories. </p>
<p> <code>abrt_var_cache_t</code> </p>
<p> &#8211; Set files with the abrt_var_cache_t type, if you want to store the files under the /var/cache directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/tmp/abrt(/.*)?, /var/cache/abrt(/.*)?, /var/spool/abrt(/.*)?, /var/spool/debug(/.*)?, /var/cache/abrt-di(/.*)?, /var/spool/rhsm/debug(/.*)? </p>
</dl>
<p> <code>abrt_var_lib_t</code> </p>
<p> &#8211; Set files with the abrt_var_lib_t type, if you want to store the abrt files under the /var/lib directory. </p>
<p> <code>abrt_var_log_t</code> </p>
<p> &#8211; Set files with the abrt_var_log_t type, if you want to treat the data as abrt var log data, usually stored under the /var/log directory. </p>
<p> <code>abrt_var_run_t</code> </p>
<p> &#8211; Set files with the abrt_var_run_t type, if you want to store the abrt files under the /run or /var/run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/abrt(/.*)?, /var/run/abrtd?.lock, /var/run/abrtd?.socket, /var/run/abrt.pid </p>
</dl>
<p> <code>abrt_watch_log_exec_t</code> </p>
<p> &#8211; Set files with the abrt_watch_log_exec_t type, if you want to transition an executable to the abrt_watch_log_t domain. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Sharing Files</h2>
<p>If you want to share files with multiple domains (Apache, FTP, rsync, Samba), you can set a file context of public_content_t and public_content_rw_t. These context allow any of the above domains to read the content. If you want a particular domain to write to the public_content_rw_t domain, you must set the appropriate boolean.</p>
<dl>
<dt>Allow abrt servers to read the /var/abrt directory by adding the public_content_t file type to the directory and by restoring the file type.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_t &quot;/var/abrt(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/abrt</code></p>
<dl>
<dt>Allow abrt servers to read and write /var/abrt/incoming by adding the public_content_rw_t type to the directory and by restoring the file type. You also need to turn on the abrt_anon_write boolean.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_rw_t &quot;/var/abrt/incoming(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/abrt/incoming</code><br />
 <code>setsebool -P abrt_anon_write 1</code> </p>
<p> If you want to allow ABRT to modify public files used for public file transfer services., you must turn on the abrt_anon_write boolean. </p>
<p> <code>setsebool -P abrt_anon_write 1</code></p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-abrt/">abrt</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-abrt_dump_oops_selinux/">abrt_dump_oops_selinux</a>(8), <a href="/docs/linux/man/8-abrt_dump_oops_selinux/">abrt_dump_oops_selinux</a>(8), <a href="/docs/linux/man/8-abrt_handle_event_selinux/">abrt_handle_event_selinux</a>(8), <a href="/docs/linux/man/8-abrt_handle_event_selinux/">abrt_handle_event_selinux</a>(8), <a href="/docs/linux/man/8-abrt_helper_selinux/">abrt_helper_selinux</a>(8), <a href="/docs/linux/man/8-abrt_helper_selinux/">abrt_helper_selinux</a>(8), <a href="/docs/linux/man/8-abrt_retrace_coredump_selinux/">abrt_retrace_coredump_selinux</a>(8), <a href="/docs/linux/man/8-abrt_retrace_coredump_selinux/">abrt_retrace_coredump_selinux</a>(8), <a href="/docs/linux/man/8-abrt_retrace_worker_selinux/">abrt_retrace_worker_selinux</a>(8), <a href="/docs/linux/man/8-abrt_retrace_worker_selinux/">abrt_retrace_worker_selinux</a>(8), <a href="/docs/linux/man/8-abrt_upload_watch_selinux/">abrt_upload_watch_selinux</a>(8), <a href="/docs/linux/man/8-abrt_upload_watch_selinux/">abrt_upload_watch_selinux</a>(8), <a href="/docs/linux/man/8-abrt_watch_log_selinux/">abrt_watch_log_selinux</a>(8), <a href="/docs/linux/man/8-abrt_watch_log_selinux/">abrt_watch_log_selinux</a>(8) </p>
