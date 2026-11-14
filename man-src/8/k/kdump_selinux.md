---
title: "kdump_selinux(8)"
name: "kdump_selinux"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kdump_selinux/"
description: "kdump_selinux – Security Enhanced Linux Policy for the kdump processes"
---

<p>kdump_selinux &#8211; Security Enhanced Linux Policy for the kdump processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the kdump processes via flexible mandatory access control. The kdump processes execute with the kdump_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep kdump_t</code> </p>
<h2>Entrypoints</h2>
<p>The kdump_t SELinux type can be entered via the <code>kdump_exec_t</code> file type. </p>
<p> The default entrypoint paths for the kdump_t domain are the following: </p>
<p> /sbin/kdump, /sbin/kexec, /usr/sbin/kdump, /usr/sbin/kexec</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux kdump policy is very flexible allowing users to setup their kdump processes in as secure a method as possible. </p>
<p> The following process types are defined for kdump: </p>
<p> kdump_t, kdumpctl_t, kdumpgui_t</code> </p>
<p> Note: <code>semanage permissive -a kdump_t</code> can be used to make the process type kdump_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. kdump policy is extremely flexible and has several booleans that allow you to manipulate the policy and run kdump with the tightest access possible. </p>
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
<p> <code>setsebool -P global_ssp 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type kdump_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>kdump_crash_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/crash(/.*)?</p>
<p> <code>kdump_lock_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lock/kdump(/.*)?</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux kdump policy is very flexible allowing users to setup their kdump processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the kdump, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t kdumpgui_tmp_t &#8216;/srv/mykdump_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mykdump_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for kdump:</i> </p>
<p> <code>kdump_crash_t</code> </p>
<p> &#8211; Set files with the kdump_crash_t type, if you want to treat the files as kdump crash data. </p>
<p> <code>kdump_etc_t</code> </p>
<p> &#8211; Set files with the kdump_etc_t type, if you want to store kdump files in the /etc directories. </p>
<p> <code>kdump_exec_t</code> </p>
<p> &#8211; Set files with the kdump_exec_t type, if you want to transition an executable to the kdump_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/sbin/kdump, /sbin/kexec, /usr/sbin/kdump, /usr/sbin/kexec </p>
</dl>
<p> <code>kdump_initrc_exec_t</code> </p>
<p> &#8211; Set files with the kdump_initrc_exec_t type, if you want to transition an executable to the kdump_initrc_t domain. </p>
<p> <code>kdump_lock_t</code> </p>
<p> &#8211; Set files with the kdump_lock_t type, if you want to treat the files as kdump lock data, stored under the /var/lock directory </p>
<p> <code>kdump_unit_file_t</code> </p>
<p> &#8211; Set files with the kdump_unit_file_t type, if you want to treat the files as kdump unit content. </p>
<p> <code>kdumpctl_exec_t</code> </p>
<p> &#8211; Set files with the kdumpctl_exec_t type, if you want to transition an executable to the kdumpctl_t domain. </p>
<p> <code>kdumpctl_tmp_t</code> </p>
<p> &#8211; Set files with the kdumpctl_tmp_t type, if you want to store kdumpctl temporary files in the /tmp directories. </p>
<p> <code>kdumpgui_exec_t</code> </p>
<p> &#8211; Set files with the kdumpgui_exec_t type, if you want to transition an executable to the kdumpgui_t domain. </p>
<p> <code>kdumpgui_tmp_t</code> </p>
<p> &#8211; Set files with the kdumpgui_tmp_t type, if you want to store kdumpgui temporary files in the /tmp directories. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-kdump/">kdump</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
