---
title: "cpucontrol_selinux(8)"
name: "cpucontrol_selinux"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cpucontrol_selinux/"
description: "cpucontrol_selinux – Security Enhanced Linux Policy for the cpucontrol processes"
---

<p>cpucontrol_selinux &#8211; Security Enhanced Linux Policy for the cpucontrol processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the cpucontrol processes via flexible mandatory access control. The cpucontrol processes execute with the cpucontrol_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep cpucontrol_t</code> </p>
<h2>Entrypoints</h2>
<p>The cpucontrol_t SELinux type can be entered via the <code>cpucontrol_exec_t</code> file type. </p>
<p> The default entrypoint paths for the cpucontrol_t domain are the following: </p>
<p> /sbin/microcode_ctl, /usr/sbin/microcode_ctl</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux cpucontrol policy is very flexible allowing users to setup their cpucontrol processes in as secure a method as possible. </p>
<p> The following process types are defined for cpucontrol: </p>
<p> cpucontrol_t</code> </p>
<p> Note: <code>semanage permissive -a cpucontrol_t</code> can be used to make the process type cpucontrol_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. cpucontrol policy is extremely flexible and has several booleans that allow you to manipulate the policy and run cpucontrol with the tightest access possible. </p>
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
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux cpucontrol policy is very flexible allowing users to setup their cpucontrol processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the cpucontrol, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t cpucontrol_conf_t &#8216;/srv/mycpucontrol_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mycpucontrol_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for cpucontrol:</i> </p>
<p> <code>cpucontrol_conf_t</code> </p>
<p> &#8211; Set files with the cpucontrol_conf_t type, if you want to treat the files as cpucontrol configuration data, usually stored under the /etc directory. </p>
<p> <code>cpucontrol_exec_t</code> </p>
<p> &#8211; Set files with the cpucontrol_exec_t type, if you want to transition an executable to the cpucontrol_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/sbin/microcode_ctl, /usr/sbin/microcode_ctl </p>
</dl>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-cpucontrol/">cpucontrol</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
