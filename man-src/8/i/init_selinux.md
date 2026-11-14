---
title: "init_selinux(8)"
name: "init_selinux"
section: "8"
letter: "i"
url: "/docs/linux/man/8-init_selinux/"
description: "init_selinux – Security Enhanced Linux Policy for the init processes"
---

<p>init_selinux &#8211; Security Enhanced Linux Policy for the init processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the init processes via flexible mandatory access control. The init processes execute with the init_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep init_t</code> </p>
<h2>Entrypoints</h2>
<p>The init_t SELinux type can be entered via the <code>init_exec_t</code> file type. </p>
<p> The default entrypoint paths for the init_t domain are the following: </p>
<p> /sbin/init(ng)?, /usr/sbin/init(ng)?, /usr/lib/systemd/[^/]*, /usr/lib/systemd/system-generators/[^/]*, /bin/systemd, /sbin/upstart, /usr/bin/systemd, /usr/sbin/upstart</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux init policy is very flexible allowing users to setup their init processes in as secure a method as possible. </p>
<p> The following process types are defined for init: </p>
<p> init_t, initrc_t</code> </p>
<p> Note: <code>semanage permissive -a init_t</code> can be used to make the process type init_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. init policy is extremely flexible and has several booleans that allow you to manipulate the policy and run init with the tightest access possible. </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
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
<p> <code>setsebool -P global_ssp 1</code> </p>
<p> If you want to allow confined applications to run with kerberos, you must turn on the kerberos_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P kerberos_enabled 1</code> </p>
<p> If you want to control the ability to mmap a low area of the address space, as configured by /proc/sys/vm/mmap_min_addr, you must turn on the mmap_low_allowed boolean. Disabled by default. </p>
<p> <code>setsebool -P mmap_low_allowed 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to disable kernel module loading, you must turn on the secure_mode_insmod boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode_insmod 1</code> </p>
<p> If you want to boolean to determine whether the system permits loading policy, setting enforcing mode, and changing boolean values. Set this to true and you have to reboot to set it back, you must turn on the secure_mode_policyload boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode_policyload 1</code> </p>
<p> If you want to allow unconfined executables to make their heap memory executable. Doing this is a really bad idea. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla, you must turn on the selinuxuser_execheap boolean. Disabled by default. </p>
<p> <code>setsebool -P selinuxuser_execheap 1</code> </p>
<p> If you want to allow all unconfined executables to use libraries requiring text relocation that are not labeled textrel_shlib_t, you must turn on the selinuxuser_execmod boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_execmod 1</code> </p>
<p> If you want to allow unconfined executables to make their stack executable. This should never, ever be necessary. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla, you must turn on the selinuxuser_execstack boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_execstack 1</code> </p>
<p> If you want to support X userspace object manager, you must turn on the xserver_object_manager boolean. Enabled by default. </p>
<p> <code>setsebool -P xserver_object_manager 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type init_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>file_type</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all files on the system</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux init policy is very flexible allowing users to setup their init processes in as secure a method as possible. </p>
<p> EQUIVALENCE DIRECTORIES</code> </p>
<p> init policy stores data with multiple different file context types under the /var/run/systemd directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/run/systemd /srv/systemd</code><br />
 <code>restorecon -R -v /srv/systemd</code> </p>
<p> <code>STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the init, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t initrc_var_run_t &#8216;/srv/myinit_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myinit_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for init:</i> </p>
<p> <code>init_exec_t</code> </p>
<p> &#8211; Set files with the init_exec_t type, if you want to transition an executable to the init_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/sbin/init(ng)?, /usr/sbin/init(ng)?, /usr/lib/systemd/[^/]*, /usr/lib/systemd/system-generators/[^/]*, /bin/systemd, /sbin/upstart, /usr/bin/systemd, /usr/sbin/upstart </p>
</dl>
<p> <code>init_tmp_t</code> </p>
<p> &#8211; Set files with the init_tmp_t type, if you want to store init temporary files in the /tmp directories. </p>
<p> <code>init_var_lib_t</code> </p>
<p> &#8211; Set files with the init_var_lib_t type, if you want to store the init files under the /var/lib directory. </p>
<p> <code>init_var_run_t</code> </p>
<p> &#8211; Set files with the init_var_run_t type, if you want to store the init files under the /run or /var/run directory. </p>
<p> <code>initctl_t</code> </p>
<p> &#8211; Set files with the initctl_t type, if you want to treat the files as initctl data. </p>
<dl>
<dt>Paths:</p>
<dd>/dev/initctl, /var/run/initctl, /var/run/systemd/initctl/fifo </p>
</dl>
<p> <code>initrc_devpts_t</code> </p>
<p> &#8211; Set files with the initrc_devpts_t type, if you want to treat the files as initrc devpts data. </p>
<p> <code>initrc_exec_t</code> </p>
<p> &#8211; Set files with the initrc_exec_t type, if you want to transition an executable to the initrc_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/init.d/.*, /etc/rc.d/rc.[^/]+, /etc/rc.d/init.d/.*, /opt/nfast/sbin/init.d-ncipher, /usr/lib/systemd/rhel[^/]*, /usr/libexec/dcc/stop-.*, /usr/libexec/dcc/start-.*, /opt/nfast/scripts/init.d/(.*), /etc/rc.d/rc, /etc/X11/prefdm, /usr/sbin/startx, /usr/bin/sepg_ctl, /usr/sbin/apachectl, /usr/sbin/ldap-agent, /usr/sbin/start-dirsrv, /usr/sbin/open_init_pty, /usr/sbin/restart-dirsrv, /etc/sysconfig/network-scripts/ifup-ipsec, /usr/share/system-config-services/system-config-services-mechanism.py </p>
</dl>
<p> <code>initrc_state_t</code> </p>
<p> &#8211; Set files with the initrc_state_t type, if you want to treat the files as initrc state data. </p>
<p> <code>initrc_tmp_t</code> </p>
<p> &#8211; Set files with the initrc_tmp_t type, if you want to store initrc temporary files in the /tmp directories. </p>
<p> <code>initrc_var_log_t</code> </p>
<p> &#8211; Set files with the initrc_var_log_t type, if you want to treat the data as initrc var log data, usually stored under the /var/log directory. </p>
<p> <code>initrc_var_run_t</code> </p>
<p> &#8211; Set files with the initrc_var_run_t type, if you want to store the initrc files under the /run or /var/run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/utmp, /var/run/random-seed, /var/run/runlevel.dir, /var/run/setmixer_flag </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-init/">init</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
