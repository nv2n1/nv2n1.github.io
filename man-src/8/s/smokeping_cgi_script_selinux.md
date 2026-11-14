---
title: "smokeping_cgi_script_selinux(8)"
name: "smokeping_cgi_script_selinux"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smokeping_cgi_script_selinux/"
description: "smokeping_cgi_script_selinux – Security Enhanced Linux Policy for the smokeping_cgi_script processes"
---

<p>smokeping_cgi_script_selinux &#8211; Security Enhanced Linux Policy for the smokeping_cgi_script processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the smokeping_cgi_script processes via flexible mandatory access control. The smokeping_cgi_script processes execute with the smokeping_cgi_script_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep smokeping_cgi_script_t</code> </p>
<h2>Entrypoints</h2>
<p>The smokeping_cgi_script_t SELinux type can be entered via the <code>shell_exec_t, smokeping_cgi_script_exec_t, smokeping_cgi_script_exec_t</code> file types. </p>
<p> The default entrypoint paths for the smokeping_cgi_script_t domain are the following: </p>
<p> /bin/d?ash, /bin/zsh.*, /bin/ksh.*, /usr/bin/d?ash, /usr/bin/zsh.*, /usr/bin/ksh.*, /bin/esh, /bin/mksh, /bin/sash, /bin/tcsh, /bin/yash, /bin/bash, /bin/fish, /bin/bash2, /usr/bin/esh, /usr/bin/tcsh, /usr/bin/yash, /usr/bin/sash, /usr/bin/mksh, /usr/bin/fish, /usr/bin/bash, /sbin/nologin, /usr/sbin/sesh, /usr/bin/bash2, /usr/sbin/smrsh, /usr/bin/scponly, /usr/sbin/nologin, /usr/libexec/sesh, /usr/sbin/scponlyc, /usr/bin/git-shell, /usr/bin/cockpit-bridge, /usr/libexec/cockpit-agent, /usr/libexec/git-core/git-shell, /usr/share/smokeping/cgi(/.*)?, /usr/share/smokeping/cgi(/.*)?</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux smokeping_cgi_script policy is very flexible allowing users to setup their smokeping_cgi_script processes in as secure a method as possible. </p>
<p> The following process types are defined for smokeping_cgi_script: </p>
<p> smokeping_cgi_script_t</code> </p>
<p> Note: <code>semanage permissive -a smokeping_cgi_script_t</code> can be used to make the process type smokeping_cgi_script_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. smokeping_cgi_script policy is extremely flexible and has several booleans that allow you to manipulate the policy and run smokeping_cgi_script with the tightest access possible. </p>
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
<p> If you want to allow httpd cgi support, you must turn on the httpd_enable_cgi boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_enable_cgi 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type smokeping_cgi_script_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>smokeping_cgi_rw_content_t</code> </p>
<p> <code>smokeping_var_lib_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/smokeping(/.*)?</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux smokeping_cgi_script policy is very flexible allowing users to setup their smokeping_cgi_script processes in as secure a method as possible. </p>
<p> </code><i>The following file types are defined for smokeping_cgi_script:</i> </p>
<p> <code>smokeping_cgi_script_exec_t</code> </p>
<p> &#8211; Set files with the smokeping_cgi_script_exec_t type, if you want to transition an executable to the smokeping_cgi_script_t domain. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-smokeping_cgi_script/">smokeping_cgi_script</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
