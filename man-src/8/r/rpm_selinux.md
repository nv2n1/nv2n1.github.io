---
title: "rpm_selinux(8)"
name: "rpm_selinux"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpm_selinux/"
description: "rpm_selinux – Security Enhanced Linux Policy for the rpm processes"
---

<p>rpm_selinux &#8211; Security Enhanced Linux Policy for the rpm processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the rpm processes via flexible mandatory access control. The rpm processes execute with the rpm_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep rpm_t</code> </p>
<h2>Entrypoints</h2>
<p>The rpm_t SELinux type can be entered via the <code>debuginfo_exec_t, rpm_exec_t, rpm_script_exec_t</code> file types. </p>
<p> The default entrypoint paths for the rpm_t domain are the following: </p>
<p> /usr/bin/debuginfo-install, /usr/bin/dnf-[0-9]+, /usr/libexec/yumDBUSBackend.py, /bin/rpm, /usr/bin/dnf, /usr/bin/rpm, /usr/bin/yum, /usr/bin/zif, /usr/sbin/pup, /usr/bin/smart, /usr/sbin/bcfg2, /usr/sbin/pirut, /usr/bin/apt-get, /bin/yum-builddep, /usr/sbin/up2date, /usr/bin/repoquery, /usr/sbin/yum-cron, /usr/sbin/synaptic, /usr/bin/apt-shell, /usr/sbin/rhn_check, /usr/sbin/rhnreg_ks, /usr/bin/anaconda-yum, /usr/bin/yum-builddep, /usr/sbin/packagekitd, /usr/bin/dnf-automatic, /usr/sbin/yum-updatesd, /usr/bin/yum-deprecated, /usr/libexec/packagekitd, /usr/bin/package-cleanup, /usr/bin/fedora-rmdevelrpms, /usr/bin/rpmdev-rmdevelrpms, /usr/sbin/system-install-packages, /usr/share/yumex/yum_childtask.py, /usr/sbin/yum-complete-transaction, /usr/share/yumex/yumex-yum-backend, /usr/libexec/pegasus/pycmpiLMI_Software-cimprovagt</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux rpm policy is very flexible allowing users to setup their rpm processes in as secure a method as possible. </p>
<p> The following process types are defined for rpm: </p>
<p> rpm_t, rpm_script_t</code> </p>
<p> Note: <code>semanage permissive -a rpm_t</code> can be used to make the process type rpm_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. rpm policy is extremely flexible and has several booleans that allow you to manipulate the policy and run rpm with the tightest access possible. </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
<p> If you want to allow all daemons the ability to read/write terminals, you must turn on the daemons_use_tty boolean. Disabled by default. </p>
<p> <code>setsebool -P daemons_use_tty 1</code> </p>
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
<p>The SELinux process type rpm_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>file_type</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all files on the system</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux rpm policy is very flexible allowing users to setup their rpm processes in as secure a method as possible. </p>
<p> EQUIVALENCE DIRECTORIES</code> </p>
<p> rpm policy stores data with multiple different file context types under the /var/lib/rpm directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/lib/rpm /srv/rpm</code><br />
 <code>restorecon -R -v /srv/rpm</code> </p>
<p> <code>STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the rpm, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t rpm_var_run_t &#8216;/srv/myrpm_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myrpm_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for rpm:</i> </p>
<p> <code>rpm_exec_t</code> </p>
<p> &#8211; Set files with the rpm_exec_t type, if you want to transition an executable to the rpm_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/dnf-[0-9]+, /usr/libexec/yumDBUSBackend.py, /bin/rpm, /usr/bin/dnf, /usr/bin/rpm, /usr/bin/yum, /usr/bin/zif, /usr/sbin/pup, /usr/bin/smart, /usr/sbin/bcfg2, /usr/sbin/pirut, /usr/bin/apt-get, /bin/yum-builddep, /usr/sbin/up2date, /usr/bin/repoquery, /usr/sbin/yum-cron, /usr/sbin/synaptic, /usr/bin/apt-shell, /usr/sbin/rhn_check, /usr/sbin/rhnreg_ks, /usr/bin/anaconda-yum, /usr/bin/yum-builddep, /usr/sbin/packagekitd, /usr/bin/dnf-automatic, /usr/sbin/yum-updatesd, /usr/bin/yum-deprecated, /usr/libexec/packagekitd, /usr/bin/package-cleanup, /usr/bin/fedora-rmdevelrpms, /usr/bin/rpmdev-rmdevelrpms, /usr/sbin/system-install-packages, /usr/share/yumex/yum_childtask.py, /usr/sbin/yum-complete-transaction, /usr/share/yumex/yumex-yum-backend, /usr/libexec/pegasus/pycmpiLMI_Software-cimprovagt </p>
</dl>
<p> <code>rpm_file_t</code> </p>
<p> &#8211; Set files with the rpm_file_t type, if you want to treat the files as rpm content. </p>
<p> <code>rpm_log_t</code> </p>
<p> &#8211; Set files with the rpm_log_t type, if you want to treat the data as rpm log data, usually stored under the /var/log directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/log/yum.log.*, /var/log/up2date.* </p>
</dl>
<p> <code>rpm_script_exec_t</code> </p>
<p> &#8211; Set files with the rpm_script_exec_t type, if you want to transition an executable to the rpm_script_t domain. </p>
<p> <code>rpm_script_tmp_t</code> </p>
<p> &#8211; Set files with the rpm_script_tmp_t type, if you want to store rpm script temporary files in the /tmp directories. </p>
<p> <code>rpm_script_tmpfs_t</code> </p>
<p> &#8211; Set files with the rpm_script_tmpfs_t type, if you want to store rpm script files on a tmpfs file system. </p>
<p> <code>rpm_tmp_t</code> </p>
<p> &#8211; Set files with the rpm_tmp_t type, if you want to store rpm temporary files in the /tmp directories. </p>
<p> <code>rpm_tmpfs_t</code> </p>
<p> &#8211; Set files with the rpm_tmpfs_t type, if you want to store rpm files on a tmpfs file system. </p>
<p> <code>rpm_var_cache_t</code> </p>
<p> &#8211; Set files with the rpm_var_cache_t type, if you want to store the files under the /var/cache directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/cache/yum(/.*)?, /var/cache/dnf(/.*)?, /var/spool/up2date(/.*)?, /var/cache/PackageKit(/.*)? </p>
</dl>
<p> <code>rpm_var_lib_t</code> </p>
<p> &#8211; Set files with the rpm_var_lib_t type, if you want to store the rpm files under the /var/lib directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/rpm(/.*)?, /var/lib/yum(/.*)?, /var/lib/dnf(/.*)?, /usr/share/rpm(/.*)?, /var/lib/PackageKit(/.*)?, /var/lib/alternatives(/.*)?, /var/lib/rpmrebuilddb.*(/.*)? </p>
</dl>
<p> <code>rpm_var_run_t</code> </p>
<p> &#8211; Set files with the rpm_var_run_t type, if you want to store the rpm files under the /run or /var/run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/yum.*, /var/run/PackageKit(/.*)? </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-rpm/">rpm</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-rpm_script_selinux/">rpm_script_selinux</a>(8), <a href="/docs/linux/man/8-rpm_script_selinux/">rpm_script_selinux</a>(8) </p>
