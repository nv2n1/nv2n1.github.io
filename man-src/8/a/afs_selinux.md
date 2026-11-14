---
title: "afs_selinux(8)"
name: "afs_selinux"
section: "8"
letter: "a"
url: "/docs/linux/man/8-afs_selinux/"
description: "afs_selinux – Security Enhanced Linux Policy for the afs processes"
---

<p>afs_selinux &#8211; Security Enhanced Linux Policy for the afs processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the afs processes via flexible mandatory access control. The afs processes execute with the afs_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep afs_t</code> </p>
<h2>Entrypoints</h2>
<p>The afs_t SELinux type can be entered via the <code>afs_exec_t</code> file type. </p>
<p> The default entrypoint paths for the afs_t domain are the following: </p>
<p> /usr/sbin/afsd, /usr/vice/etc/afsd</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux afs policy is very flexible allowing users to setup their afs processes in as secure a method as possible. </p>
<p> The following process types are defined for afs: </p>
<p> afs_t, afs_bosserver_t, afs_fsserver_t, afs_kaserver_t, afs_ptserver_t, afs_vlserver_t</code> </p>
<p> Note: <code>semanage permissive -a afs_t</code> can be used to make the process type afs_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. afs policy is extremely flexible and has several booleans that allow you to manipulate the policy and run afs with the tightest access possible. </p>
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
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code></p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux afs policy is very flexible allowing users to setup their afs processes in as secure a method as possible. </p>
<p> The following port types are defined for afs: </p>
<dl>
<dt><code>afs3_callback_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 7001 udp 7001 </p>
<dt><code>afs_bos_port_t</code></p>
<dd>
<dd>Default Defined Ports: udp 7007 </p>
<dt><code>afs_fs_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 2040 udp 7000,7005 </p>
<dt><code>afs_ka_port_t</code></p>
<dd>
<dd>Default Defined Ports: udp 7004 </p>
<dt><code>afs_pt_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 7002 udp 7002 </p>
<dt><code>afs_vl_port_t</code></p>
<dd>
<dd>Default Defined Ports: udp 7003</dl>
<h2>Managed Files</h2>
<p>The SELinux process type afs_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>afs_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/(open)?afs(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/vice/cache(/.*)?</p>
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
<p> <code>etc_runtime_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/[^/]+</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/mtab.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/blkid(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/nologin.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/.fstab.hal..+</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/halt</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/fastboot</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/poweroff</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/cmtab</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/.autofsck</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/forcefsck</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/.suspended</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/fsckoptions</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/.updated</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/.updated</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/.autorelabel</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/securetty</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/nohotplug</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/killpower</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/ioctl.save</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/fstab.REVOKE</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/network/ifstate</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/sysconfig/hwconf</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/ptal/ptal-printd-like</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/sysconfig/iptables.save</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/xorg.conf.d/00-system-setup-keyboard.conf</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/X11/xorg.conf.d/00-system-setup-keyboard.conf</p>
<p> <code>root_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/initrd</p>
<p> <code>unlabeled_t</code></p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux afs policy is very flexible allowing users to setup their afs processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the afs, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t afs_vl_db_t &#8216;/srv/myafs_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myafs_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for afs:</i> </p>
<p> <code>afs_bosserver_exec_t</code> </p>
<p> &#8211; Set files with the afs_bosserver_exec_t type, if you want to transition an executable to the afs_bosserver_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/bosserver, /usr/afs/bin/bosserver </p>
</dl>
<p> <code>afs_cache_t</code> </p>
<p> &#8211; Set files with the afs_cache_t type, if you want to store the files under the /var/cache directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/cache/(open)?afs(/.*)?, /usr/vice/cache(/.*)? </p>
</dl>
<p> <code>afs_config_t</code> </p>
<p> &#8211; Set files with the afs_config_t type, if you want to treat the files as afs configuration data, usually stored under the /etc directory. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/(open)?afs(/.*)?, /usr/afs/etc(/.*)?, /usr/afs/local(/.*)? </p>
</dl>
<p> <code>afs_dbdir_t</code> </p>
<p> &#8211; Set files with the afs_dbdir_t type, if you want to treat the files as afs dbdir data. </p>
<p> <code>afs_exec_t</code> </p>
<p> &#8211; Set files with the afs_exec_t type, if you want to transition an executable to the afs_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/afsd, /usr/vice/etc/afsd </p>
</dl>
<p> <code>afs_files_t</code> </p>
<p> &#8211; Set files with the afs_files_t type, if you want to treat the files as afs content. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/afs(/.*)?, /vicepa, /vicepb, /vicepc </p>
</dl>
<p> <code>afs_fsserver_exec_t</code> </p>
<p> &#8211; Set files with the afs_fsserver_exec_t type, if you want to transition an executable to the afs_fsserver_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/afs/bin/salvager, /usr/afs/bin/volserver, /usr/afs/bin/fileserver, /usr/afs/bin/dasalvager, /usr/afs/bin/davolserver, /usr/afs/bin/dafileserver, /usr/afs/bin/salvageserver, /usr/libexec/openafs/salvager, /usr/libexec/openafs/volserver, /usr/libexec/openafs/fileserver </p>
</dl>
<p> <code>afs_initrc_exec_t</code> </p>
<p> &#8211; Set files with the afs_initrc_exec_t type, if you want to transition an executable to the afs_initrc_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/rc.d/init.d/(open)?afs, /etc/rc.d/init.d/openafs-client </p>
</dl>
<p> <code>afs_ka_db_t</code> </p>
<p> &#8211; Set files with the afs_ka_db_t type, if you want to treat the files as afs ka database content. </p>
<p> <code>afs_kaserver_exec_t</code> </p>
<p> &#8211; Set files with the afs_kaserver_exec_t type, if you want to transition an executable to the afs_kaserver_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/afs/bin/kaserver, /usr/libexec/openafs/kaserver </p>
</dl>
<p> <code>afs_logfile_t</code> </p>
<p> &#8211; Set files with the afs_logfile_t type, if you want to treat the files as afs logfile data. </p>
<p> <code>afs_pt_db_t</code> </p>
<p> &#8211; Set files with the afs_pt_db_t type, if you want to treat the files as afs pt database content. </p>
<p> <code>afs_ptserver_exec_t</code> </p>
<p> &#8211; Set files with the afs_ptserver_exec_t type, if you want to transition an executable to the afs_ptserver_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/afs/bin/ptserver, /usr/libexec/openafs/ptserver </p>
</dl>
<p> <code>afs_vl_db_t</code> </p>
<p> &#8211; Set files with the afs_vl_db_t type, if you want to treat the files as afs vl database content. </p>
<p> <code>afs_vlserver_exec_t</code> </p>
<p> &#8211; Set files with the afs_vlserver_exec_t type, if you want to transition an executable to the afs_vlserver_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/afs/bin/vlserver, /usr/libexec/openafs/vlserver </p>
</dl>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-afs/">afs</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-afs_bosserver_selinux/">afs_bosserver_selinux</a>(8), <a href="/docs/linux/man/8-afs_bosserver_selinux/">afs_bosserver_selinux</a>(8), <a href="/docs/linux/man/8-afs_fsserver_selinux/">afs_fsserver_selinux</a>(8), <a href="/docs/linux/man/8-afs_fsserver_selinux/">afs_fsserver_selinux</a>(8), <a href="/docs/linux/man/8-afs_kaserver_selinux/">afs_kaserver_selinux</a>(8), <a href="/docs/linux/man/8-afs_kaserver_selinux/">afs_kaserver_selinux</a>(8), <a href="/docs/linux/man/8-afs_ptserver_selinux/">afs_ptserver_selinux</a>(8), <a href="/docs/linux/man/8-afs_ptserver_selinux/">afs_ptserver_selinux</a>(8), <a href="/docs/linux/man/8-afs_vlserver_selinux/">afs_vlserver_selinux</a>(8), <a href="/docs/linux/man/8-afs_vlserver_selinux/">afs_vlserver_selinux</a>(8) </p>
