---
title: "chrome_sandbox_nacl_selinux(8)"
name: "chrome_sandbox_nacl_selinux"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chrome_sandbox_nacl_selinux/"
description: "chrome_sandbox_nacl_selinux – Security Enhanced Linux Policy for the chrome_sandbox_nacl processes"
---

<p>chrome_sandbox_nacl_selinux &#8211; Security Enhanced Linux Policy for the chrome_sandbox_nacl processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the chrome_sandbox_nacl processes via flexible mandatory access control. The chrome_sandbox_nacl processes execute with the chrome_sandbox_nacl_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep chrome_sandbox_nacl_t</code> </p>
<h2>Entrypoints</h2>
<p>The chrome_sandbox_nacl_t SELinux type can be entered via the <code>usr_t, chrome_sandbox_nacl_exec_t, bin_t</code> file types. </p>
<p> The default entrypoint paths for the chrome_sandbox_nacl_t domain are the following: </p>
<p> All executeables with the default executable label, usually stored in /usr/bin and /usr/sbin. /usr/.*, /opt/.*, /emul/.*, /ostree(/.*)?, /export(/.*)?, /usr/doc(/.*)?/lib(/.*)?, /usr/inclu.e(/.*)?, /usr/share/doc(/.*)?/README.*, /usr, /opt, /emul, /opt/google/chrome[^/]*/nacl_helper_bootstrap, /opt/google/chrome/nacl_helper_bootstrap, /usr/lib/chromium-browser/nacl_helper_bootstrap</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux chrome_sandbox_nacl policy is very flexible allowing users to setup their chrome_sandbox_nacl processes in as secure a method as possible. </p>
<p> The following process types are defined for chrome_sandbox_nacl: </p>
<p> chrome_sandbox_nacl_t</code> </p>
<p> Note: <code>semanage permissive -a chrome_sandbox_nacl_t</code> can be used to make the process type chrome_sandbox_nacl_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. chrome_sandbox_nacl policy is extremely flexible and has several booleans that allow you to manipulate the policy and run chrome_sandbox_nacl with the tightest access possible. </p>
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
<p>The SELinux process type chrome_sandbox_nacl_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>chrome_sandbox_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.cache/chromium(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.cache/google-chrome(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.cache/google-chrome-unstable(/.*)?</p>
<p> <code>chrome_sandbox_tmpfs_t</code></p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux chrome_sandbox_nacl policy is very flexible allowing users to setup their chrome_sandbox_nacl processes in as secure a method as possible. </p>
<p> </code><i>The following file types are defined for chrome_sandbox_nacl:</i> </p>
<p> <code>chrome_sandbox_nacl_exec_t</code> </p>
<p> &#8211; Set files with the chrome_sandbox_nacl_exec_t type, if you want to transition an executable to the chrome_sandbox_nacl_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/opt/google/chrome[^/]*/nacl_helper_bootstrap, /opt/google/chrome/nacl_helper_bootstrap, /usr/lib/chromium-browser/nacl_helper_bootstrap </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-chrome_sandbox_nacl/">chrome_sandbox_nacl</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
