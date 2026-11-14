---
title: "qemu_dm_selinux(8)"
name: "qemu_dm_selinux"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qemu_dm_selinux/"
description: "qemu_dm_selinux – Security Enhanced Linux Policy for the qemu_dm processes"
---

<p>qemu_dm_selinux &#8211; Security Enhanced Linux Policy for the qemu_dm processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the qemu_dm processes via flexible mandatory access control. The qemu_dm processes execute with the qemu_dm_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep qemu_dm_t</code> </p>
<h2>Entrypoints</h2>
<p>The qemu_dm_t SELinux type can be entered via the <code>qemu_dm_exec_t</code> file type. </p>
<p> The default entrypoint paths for the qemu_dm_t domain are the following:</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux qemu_dm policy is very flexible allowing users to setup their qemu_dm processes in as secure a method as possible. </p>
<p> The following process types are defined for qemu_dm: </p>
<p> qemu_dm_t</code> </p>
<p> Note: <code>semanage permissive -a qemu_dm_t</code> can be used to make the process type qemu_dm_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. qemu_dm policy is extremely flexible and has several booleans that allow you to manipulate the policy and run qemu_dm with the tightest access possible. </p>
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
<p> If you want to allow xend to run qemu-dm. Not required if using paravirt and no vfb, you must turn on the xend_run_qemu boolean. Enabled by default. </p>
<p> <code>setsebool -P xend_run_qemu 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type qemu_dm_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>xenfs_t</code></p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-qemu_dm/">qemu_dm</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
