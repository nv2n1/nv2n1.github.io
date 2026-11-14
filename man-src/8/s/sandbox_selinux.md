---
title: "sandbox_selinux(8)"
name: "sandbox_selinux"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sandbox_selinux/"
description: "sandbox_selinux – Security Enhanced Linux Policy for the sandbox processes"
---

<p>sandbox_selinux &#8211; Security Enhanced Linux Policy for the sandbox processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the sandbox processes via flexible mandatory access control. The sandbox processes execute with the sandbox_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep sandbox_t</code> </p>
<h2>Entrypoints</h2>
<p>The sandbox_t SELinux type can be entered via the <code>file_type</code> file type. </p>
<p> The default entrypoint paths for the sandbox_t domain are the following: </p>
<p> all files on the system</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux sandbox policy is very flexible allowing users to setup their sandbox processes in as secure a method as possible. </p>
<p> The following process types are defined for sandbox: </p>
<p> sandbox_t, sandbox_xserver_t, sandbox_min_t, sandbox_min_client_t, sandbox_x_t, sandbox_x_client_t, sandbox_web_t, sandbox_web_client_t, sandbox_net_t, sandbox_net_client_t</code> </p>
<p> Note: <code>semanage permissive -a sandbox_t</code> can be used to make the process type sandbox_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>MCS Constrained</h2>
<p>The SELinux process type sandbox_t is an MCS (Multi Category Security) constrained type. Sometimes this separation is referred to as sVirt. These types are usually used for securing multi-tenant environments, such as virtualization, containers or separation of users. The tools used to launch MCS types, pick out a different MCS label for each process group. </p>
<p> For example one process might be launched with sandbox_t:s0:c1,c2, and another process launched with sandbox_t:s0:c3,c4. The SELinux kernel only allows these processes can only write to content with a matching MCS label, or a MCS Label of s0. A process running with the MCS level of s0:c1,c2 is not allowed to write to content with the MCS label of s0:c3,c4</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. sandbox policy is extremely flexible and has several booleans that allow you to manipulate the policy and run sandbox with the tightest access possible. </p>
<p> If you want to deny user domains applications to map a memory region as both executable and writable, this is dangerous and the executable should be reported in bugzilla, you must turn on the deny_execmem boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_execmem 1</code> </p>
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
<p>The SELinux process type sandbox_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>sandbox_file_t</code> </p>
<p> <code>sandbox_tmpfs_type</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all sandbox content in tmpfs file systems</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux sandbox policy is very flexible allowing users to setup their sandbox processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the sandbox, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t sandbox_xserver_tmpfs_t &#8216;/srv/mysandbox_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mysandbox_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for sandbox:</i> </p>
<p> <code>sandbox_devpts_t</code> </p>
<p> &#8211; Set files with the sandbox_devpts_t type, if you want to treat the files as sandbox devpts data. </p>
<p> <code>sandbox_exec_t</code> </p>
<p> &#8211; Set files with the sandbox_exec_t type, if you want to transition an executable to the sandbox_t domain. </p>
<p> <code>sandbox_file_t</code> </p>
<p> &#8211; Set files with the sandbox_file_t type, if you want to treat the files as sandbox content. </p>
<p> <code>sandbox_min_client_tmpfs_t</code> </p>
<p> &#8211; Set files with the sandbox_min_client_tmpfs_t type, if you want to store sandbox min client files on a tmpfs file system. </p>
<p> <code>sandbox_net_client_tmpfs_t</code> </p>
<p> &#8211; Set files with the sandbox_net_client_tmpfs_t type, if you want to store sandbox net client files on a tmpfs file system. </p>
<p> <code>sandbox_web_client_tmpfs_t</code> </p>
<p> &#8211; Set files with the sandbox_web_client_tmpfs_t type, if you want to store sandbox web client files on a tmpfs file system. </p>
<p> <code>sandbox_x_client_tmpfs_t</code> </p>
<p> &#8211; Set files with the sandbox_x_client_tmpfs_t type, if you want to store sandbox x client files on a tmpfs file system. </p>
<p> <code>sandbox_xserver_tmpfs_t</code> </p>
<p> &#8211; Set files with the sandbox_xserver_tmpfs_t type, if you want to store sandbox xserver files on a tmpfs file system. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-sandbox/">sandbox</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-sandbox_min_selinux/">sandbox_min_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_min_selinux/">sandbox_min_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_min_client_selinux/">sandbox_min_client_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_min_client_selinux/">sandbox_min_client_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_net_selinux/">sandbox_net_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_net_selinux/">sandbox_net_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_net_client_selinux/">sandbox_net_client_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_net_client_selinux/">sandbox_net_client_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_web_selinux/">sandbox_web_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_web_selinux/">sandbox_web_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_web_client_selinux/">sandbox_web_client_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_web_client_selinux/">sandbox_web_client_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_x_selinux/">sandbox_x_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_x_selinux/">sandbox_x_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_x_client_selinux/">sandbox_x_client_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_x_client_selinux/">sandbox_x_client_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_xserver_selinux/">sandbox_xserver_selinux</a>(8), <a href="/docs/linux/man/8-sandbox_xserver_selinux/">sandbox_xserver_selinux</a>(8) </p>
