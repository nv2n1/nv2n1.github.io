---
title: "rsync_selinux(8)"
name: "rsync_selinux"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rsync_selinux/"
description: "rsync_selinux – Security Enhanced Linux Policy for the rsync processes"
---

<p>rsync_selinux &#8211; Security Enhanced Linux Policy for the rsync processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the rsync processes via flexible mandatory access control. The rsync processes execute with the rsync_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep rsync_t</code> </p>
<h2>Entrypoints</h2>
<p>The rsync_t SELinux type can be entered via the <code>rsync_exec_t</code> file type. </p>
<p> The default entrypoint paths for the rsync_t domain are the following: </p>
<p> /usr/bin/rsync</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux rsync policy is very flexible allowing users to setup their rsync processes in as secure a method as possible. </p>
<p> The following process types are defined for rsync: </p>
<p> rsync_t</code> </p>
<p> Note: <code>semanage permissive -a rsync_t</code> can be used to make the process type rsync_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. rsync policy is extremely flexible and has several booleans that allow you to manipulate the policy and run rsync with the tightest access possible. </p>
<p> If you want to allow rsync to run as a client, you must turn on the rsync_client boolean. Disabled by default. </p>
<p> <code>setsebool -P rsync_client 1</code> </p>
<p> If you want to allow rsync to export any files/directories read only, you must turn on the rsync_export_all_ro boolean. Disabled by default. </p>
<p> <code>setsebool -P rsync_export_all_ro 1</code> </p>
<p> If you want to allow rsync server to manage all files/directories on the system, you must turn on the rsync_full_access boolean. Disabled by default. </p>
<p> <code>setsebool -P rsync_full_access 1</code> </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
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
<p> If you want to support ecryptfs home directories, you must turn on the use_ecryptfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_ecryptfs_home_dirs 1</code> </p>
<p> If you want to support fusefs home directories, you must turn on the use_fusefs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_fusefs_home_dirs 1</code> </p>
<p> If you want to support NFS home directories, you must turn on the use_nfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_nfs_home_dirs 1</code> </p>
<p> If you want to support SAMBA home directories, you must turn on the use_samba_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_samba_home_dirs 1</code></p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux rsync policy is very flexible allowing users to setup their rsync processes in as secure a method as possible. </p>
<p> The following port types are defined for rsync: </p>
<dl>
<dt><code>rsync_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 873 udp 873</dl>
<h2>Managed Files</h2>
<p>The SELinux process type rsync_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>cifs_t</code> </p>
<p> <code>non_auth_file_type</code></p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux rsync policy is very flexible allowing users to setup their rsync processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the rsync, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t rsync_var_run_t &#8216;/srv/myrsync_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myrsync_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for rsync:</i> </p>
<p> <code>rsync_data_t</code> </p>
<p> &#8211; Set files with the rsync_data_t type, if you want to treat the files as rsync content. </p>
<p> <code>rsync_etc_t</code> </p>
<p> &#8211; Set files with the rsync_etc_t type, if you want to store rsync files in the /etc directories. </p>
<p> <code>rsync_exec_t</code> </p>
<p> &#8211; Set files with the rsync_exec_t type, if you want to transition an executable to the rsync_t domain. </p>
<p> <code>rsync_log_t</code> </p>
<p> &#8211; Set files with the rsync_log_t type, if you want to treat the data as rsync log data, usually stored under the /var/log directory. </p>
<p> <code>rsync_tmp_t</code> </p>
<p> &#8211; Set files with the rsync_tmp_t type, if you want to store rsync temporary files in the /tmp directories. </p>
<p> <code>rsync_var_run_t</code> </p>
<p> &#8211; Set files with the rsync_var_run_t type, if you want to store the rsync files under the /run or /var/run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/rsyncd.lock, /var/run/swift_server.lock </p>
</dl>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Sharing Files</h2>
<p>If you want to share files with multiple domains (Apache, FTP, rsync, Samba), you can set a file context of public_content_t and public_content_rw_t. These context allow any of the above domains to read the content. If you want a particular domain to write to the public_content_rw_t domain, you must set the appropriate boolean.</p>
<dl>
<dt>Allow rsync servers to read the /var/rsync directory by adding the public_content_t file type to the directory and by restoring the file type.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_t &quot;/var/rsync(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/rsync</code></p>
<dl>
<dt>Allow rsync servers to read and write /var/rsync/incoming by adding the public_content_rw_t type to the directory and by restoring the file type. You also need to turn on the rsync_anon_write boolean.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_rw_t &quot;/var/rsync/incoming(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/rsync/incoming</code><br />
 <code>setsebool -P rsync_anon_write 1</code> </p>
<p> If you want to allow rsync to modify public files used for public file transfer services. Files/Directories must be labeled public_content_rw_t., you must turn on the rsync_anon_write boolean. </p>
<p> <code>setsebool -P rsync_anon_write 1</code></p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-rsync/">rsync</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
