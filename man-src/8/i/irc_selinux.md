---
title: "irc_selinux(8)"
name: "irc_selinux"
section: "8"
letter: "i"
url: "/docs/linux/man/8-irc_selinux/"
description: "irc_selinux – Security Enhanced Linux Policy for the irc processes"
---

<p>irc_selinux &#8211; Security Enhanced Linux Policy for the irc processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the irc processes via flexible mandatory access control. The irc processes execute with the irc_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep irc_t</code> </p>
<h2>Entrypoints</h2>
<p>The irc_t SELinux type can be entered via the <code>irc_exec_t</code> file type. </p>
<p> The default entrypoint paths for the irc_t domain are the following: </p>
<p> /usr/bin/[st]irc, /usr/bin/ircII, /usr/bin/irssi, /usr/bin/tinyirc</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux irc policy is very flexible allowing users to setup their irc processes in as secure a method as possible. </p>
<p> The following process types are defined for irc: </p>
<p> irc_t</code> </p>
<p> Note: <code>semanage permissive -a irc_t</code> can be used to make the process type irc_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. irc policy is extremely flexible and has several booleans that allow you to manipulate the policy and run irc with the tightest access possible. </p>
<p> If you want to determine whether irc clients can listen on and connect to any unreserved TCP ports, you must turn on the irc_use_any_tcp_ports boolean. Disabled by default. </p>
<p> <code>setsebool -P irc_use_any_tcp_ports 1</code> </p>
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
<p> Policy governs the access confined processes have to these ports. SELinux irc policy is very flexible allowing users to setup their irc processes in as secure a method as possible. </p>
<p> The following port types are defined for irc: </p>
<dl>
<dt><code>ircd_port_t</code></p>
<dd>
<dd>Default Defined Ports: tcp 6667,6697</dl>
<h2>Managed Files</h2>
<p>The SELinux process type irc_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>cifs_t</code> </p>
<p> <code>ecryptfs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.Private(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.ecryptfs(/.*)?</p>
<p> <code>fusefs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user/[^/]*/gvfs</p>
<p> <code>irc_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.irssi(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/irclog(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.ircmotd</p>
<p> <code>irc_tmp_t</code> </p>
<p> <code>nfs_t</code> </p>
<p> <code>user_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.+</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux irc policy is very flexible allowing users to setup their irc processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the irc, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t irc_tmp_t &#8216;/srv/myirc_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myirc_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for irc:</i> </p>
<p> <code>irc_conf_t</code> </p>
<p> &#8211; Set files with the irc_conf_t type, if you want to treat the files as irc configuration data, usually stored under the /etc directory. </p>
<p> <code>irc_exec_t</code> </p>
<p> &#8211; Set files with the irc_exec_t type, if you want to transition an executable to the irc_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/[st]irc, /usr/bin/ircII, /usr/bin/irssi, /usr/bin/tinyirc </p>
</dl>
<p> <code>irc_home_t</code> </p>
<p> &#8211; Set files with the irc_home_t type, if you want to store irc files in the users home directory. </p>
<dl>
<dt>Paths:</p>
<dd>/home/[^/]+/.irssi(/.*)?, /home/[^/]+/irclog(/.*)?, /home/[^/]+/.ircmotd </p>
</dl>
<p> <code>irc_tmp_t</code> </p>
<p> &#8211; Set files with the irc_tmp_t type, if you want to store irc temporary files in the /tmp directories. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-irc/">irc</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
