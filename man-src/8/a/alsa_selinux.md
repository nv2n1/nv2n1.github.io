---
title: "alsa_selinux(8)"
name: "alsa_selinux"
section: "8"
letter: "a"
url: "/docs/linux/man/8-alsa_selinux/"
description: "alsa_selinux – Security Enhanced Linux Policy for the alsa processes"
---

<p>alsa_selinux &#8211; Security Enhanced Linux Policy for the alsa processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the alsa processes via flexible mandatory access control. The alsa processes execute with the alsa_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep alsa_t</code> </p>
<h2>Entrypoints</h2>
<p>The alsa_t SELinux type can be entered via the <code>alsa_exec_t</code> file type. </p>
<p> The default entrypoint paths for the alsa_t domain are the following: </p>
<p> /sbin/salsa, /sbin/alsactl, /usr/bin/ainit, /bin/alsaunmute, /usr/sbin/salsa, /usr/sbin/alsactl, /usr/bin/alsaunmute</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux alsa policy is very flexible allowing users to setup their alsa processes in as secure a method as possible. </p>
<p> The following process types are defined for alsa: </p>
<p> alsa_t</code> </p>
<p> Note: <code>semanage permissive -a alsa_t</code> can be used to make the process type alsa_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. alsa policy is extremely flexible and has several booleans that allow you to manipulate the policy and run alsa with the tightest access possible. </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
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
<p>The SELinux process type alsa_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>alsa_etc_rw_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/asound(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/alsa/pcm(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/alsa/pcm(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/asound.state</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/alsa/asound.state</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/alsa/alsa.conf</p>
<p> <code>alsa_lock_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lock/asound.state.lock</p>
<p> <code>alsa_tmp_t</code> </p>
<p> <code>alsa_tmpfs_t</code> </p>
<p> <code>alsa_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/alsa(/.*)?</p>
<p> <code>alsa_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/alsactl.pid</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux alsa policy is very flexible allowing users to setup their alsa processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the alsa, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t alsa_var_run_t &#8216;/srv/myalsa_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myalsa_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for alsa:</i> </p>
<p> <code>alsa_etc_rw_t</code> </p>
<p> &#8211; Set files with the alsa_etc_rw_t type, if you want to treat the files as alsa etc read/write content. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/asound(/.*)?, /etc/alsa/pcm(/.*)?, /usr/share/alsa/pcm(/.*)?, /etc/asound.state, /etc/alsa/asound.state, /usr/share/alsa/alsa.conf </p>
</dl>
<p> <code>alsa_exec_t</code> </p>
<p> &#8211; Set files with the alsa_exec_t type, if you want to transition an executable to the alsa_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/sbin/salsa, /sbin/alsactl, /usr/bin/ainit, /bin/alsaunmute, /usr/sbin/salsa, /usr/sbin/alsactl, /usr/bin/alsaunmute </p>
</dl>
<p> <code>alsa_home_t</code> </p>
<p> &#8211; Set files with the alsa_home_t type, if you want to store alsa files in the users home directory. </p>
<p> <code>alsa_lock_t</code> </p>
<p> &#8211; Set files with the alsa_lock_t type, if you want to treat the files as alsa lock data, stored under the /var/lock directory </p>
<p> <code>alsa_tmp_t</code> </p>
<p> &#8211; Set files with the alsa_tmp_t type, if you want to store alsa temporary files in the /tmp directories. </p>
<p> <code>alsa_tmpfs_t</code> </p>
<p> &#8211; Set files with the alsa_tmpfs_t type, if you want to store alsa files on a tmpfs file system. </p>
<p> <code>alsa_unit_file_t</code> </p>
<p> &#8211; Set files with the alsa_unit_file_t type, if you want to treat the files as alsa unit content. </p>
<p> <code>alsa_var_lib_t</code> </p>
<p> &#8211; Set files with the alsa_var_lib_t type, if you want to store the alsa files under the /var/lib directory. </p>
<p> <code>alsa_var_run_t</code> </p>
<p> &#8211; Set files with the alsa_var_run_t type, if you want to store the alsa files under the /run or /var/run directory. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-alsa/">alsa</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
