---
title: "smbd_selinux(8)"
name: "smbd_selinux"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbd_selinux/"
description: "smbd_selinux – Security Enhanced Linux Policy for the smbd processes"
---

<p>smbd_selinux &#8211; Security Enhanced Linux Policy for the smbd processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the smbd processes via flexible mandatory access control. The smbd processes execute with the smbd_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep smbd_t</code> </p>
<h2>Entrypoints</h2>
<p>The smbd_t SELinux type can be entered via the <code>smbd_exec_t</code> file type. </p>
<p> The default entrypoint paths for the smbd_t domain are the following: </p>
<p> /usr/sbin/smbd</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux smbd policy is very flexible allowing users to setup their smbd processes in as secure a method as possible. </p>
<p> The following process types are defined for smbd: </p>
<p> smbd_t</code> </p>
<p> Note: <code>semanage permissive -a smbd_t</code> can be used to make the process type smbd_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. smbd policy is extremely flexible and has several booleans that allow you to manipulate the policy and run smbd with the tightest access possible. </p>
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
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to allow samba to create new home directories (e.g. via PAM), you must turn on the samba_create_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P samba_create_home_dirs 1</code> </p>
<p> If you want to allow samba to act as the domain controller, add users, groups and change passwords, you must turn on the samba_domain_controller boolean. Disabled by default. </p>
<p> <code>setsebool -P samba_domain_controller 1</code> </p>
<p> If you want to allow samba to share users home directories, you must turn on the samba_enable_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P samba_enable_home_dirs 1</code> </p>
<p> If you want to allow samba to share any file/directory read only, you must turn on the samba_export_all_ro boolean. Disabled by default. </p>
<p> <code>setsebool -P samba_export_all_ro 1</code> </p>
<p> If you want to allow samba to share any file/directory read/write, you must turn on the samba_export_all_rw boolean. Disabled by default. </p>
<p> <code>setsebool -P samba_export_all_rw 1</code> </p>
<p> If you want to allow smbd to load libgfapi from gluster, you must turn on the samba_load_libgfapi boolean. Disabled by default. </p>
<p> <code>setsebool -P samba_load_libgfapi 1</code> </p>
<p> If you want to allow samba to act as a portmapper, you must turn on the samba_portmapper boolean. Disabled by default. </p>
<p> <code>setsebool -P samba_portmapper 1</code> </p>
<p> If you want to allow samba to run unconfined scripts, you must turn on the samba_run_unconfined boolean. Disabled by default. </p>
<p> <code>setsebool -P samba_run_unconfined 1</code> </p>
<p> If you want to allow samba to export ntfs/fusefs volumes, you must turn on the samba_share_fusefs boolean. Enabled by default. </p>
<p> <code>setsebool -P samba_share_fusefs 1</code> </p>
<p> If you want to allow samba to export NFS volumes, you must turn on the samba_share_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P samba_share_nfs 1</code></p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux smbd policy is very flexible allowing users to setup their smbd processes in as secure a method as possible. </p>
<p> The following port types are defined for smbd: </p>
<dl>
<dt><code>smbd_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 445,137-139</dl>
<h2>Managed Files</h2>
<p>The SELinux process type smbd_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
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
<p> <code>non_security_file_type</code> </p>
<p> <code>noxattrfs</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all files on file systems which do not support extended attributes</p>
<p> <code>user_home_type</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all user home files</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux smbd policy is very flexible allowing users to setup their smbd processes in as secure a method as possible. </p>
<p> EQUIVALENCE DIRECTORIES</code> </p>
<p> smbd policy stores data with multiple different file context types under the /var/run/samba directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/run/samba /srv/samba</code><br />
 <code>restorecon -R -v /srv/samba</code> </p>
<p> <code>STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the smbd, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t smbd_var_run_t &#8216;/srv/mysmbd_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mysmbd_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for smbd:</i> </p>
<p> <code>smbd_exec_t</code> </p>
<p> &#8211; Set files with the smbd_exec_t type, if you want to transition an executable to the smbd_t domain. </p>
<p> <code>smbd_keytab_t</code> </p>
<p> &#8211; Set files with the smbd_keytab_t type, if you want to treat the files as kerberos keytab files. </p>
<p> <code>smbd_tmp_t</code> </p>
<p> &#8211; Set files with the smbd_tmp_t type, if you want to store smbd temporary files in the /tmp directories. </p>
<p> <code>smbd_tmpfs_t</code> </p>
<p> &#8211; Set files with the smbd_tmpfs_t type, if you want to store smbd files on a tmpfs file system. </p>
<p> <code>smbd_var_run_t</code> </p>
<p> &#8211; Set files with the smbd_var_run_t type, if you want to store the smbd files under the /run or /var/run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/samba(/.*)?, /var/run/samba/smbd.pid, /var/run/samba/brlock.tdb, /var/run/samba/locking.tdb, /var/run/samba/gencache.tdb, /var/run/samba/sessionid.tdb, /var/run/samba/share_info.tdb, /var/run/samba/connections.tdb </p>
</dl>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Sharing Files</h2>
<p>If you want to share files with multiple domains (Apache, FTP, rsync, Samba), you can set a file context of public_content_t and public_content_rw_t. These context allow any of the above domains to read the content. If you want a particular domain to write to the public_content_rw_t domain, you must set the appropriate boolean.</p>
<dl>
<dt>Allow smbd servers to read the /var/smbd directory by adding the public_content_t file type to the directory and by restoring the file type.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_t &quot;/var/smbd(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/smbd</code></p>
<dl>
<dt>Allow smbd servers to read and write /var/smbd/incoming by adding the public_content_rw_t type to the directory and by restoring the file type. You also need to turn on the smbd_anon_write boolean.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_rw_t &quot;/var/smbd/incoming(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/smbd/incoming</code><br />
 <code>setsebool -P smbd_anon_write 1</code> </p>
<p> If you want to allow samba to modify public files used for public file transfer services. Files/Directories must be labeled public_content_rw_t., you must turn on the smbd_anon_write boolean. </p>
<p> <code>setsebool -P smbd_anon_write 1</code></p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-smbd/">smbd</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
