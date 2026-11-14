---
title: "openshift_selinux(8)"
name: "openshift_selinux"
section: "8"
letter: "o"
url: "/docs/linux/man/8-openshift_selinux/"
description: "openshift_selinux – Security Enhanced Linux Policy for the openshift processes"
---

<p>openshift_selinux &#8211; Security Enhanced Linux Policy for the openshift processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the openshift processes via flexible mandatory access control. The openshift processes execute with the openshift_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep openshift_t</code> </p>
<h2>Entrypoints</h2>
<p>The openshift_t SELinux type can be entered via the <code>usr_t, bin_t, httpd_exec_t, shell_exec_t, gpg_exec_t, openshift_file_type, user_cron_spool_t</code> file types. </p>
<p> The default entrypoint paths for the openshift_t domain are the following: </p>
<p> All executeables with the default executable label, usually stored in /usr/bin and /usr/sbin. /usr/.*, /opt/.*, /emul/.*, /ostree(/.*)?, /export(/.*)?, /usr/doc(/.*)?/lib(/.*)?, /usr/inclu.e(/.*)?, /usr/share/doc(/.*)?/README.*, /usr, /opt, /emul, /usr/sbin/httpd(.worker)?, /usr/sbin/<a href="/docs/linux/man/2-apache/">apache</a>(2)?, /usr/lib/apache-ssl/.+, /usr/sbin/<a href="/docs/linux/man/2-apache-ssl/">apache-ssl</a>(2)?, /usr/share/jetty/bin/jetty.sh, /usr/sbin/nginx, /usr/sbin/thttpd, /usr/sbin/php-fpm, /usr/sbin/cherokee, /usr/sbin/lighttpd, /usr/sbin/httpd.event, /usr/bin/mongrel_rails, /usr/sbin/htcacheclean, /bin/d?ash, /bin/zsh.*, /bin/ksh.*, /usr/bin/d?ash, /usr/bin/zsh.*, /usr/bin/ksh.*, /bin/esh, /bin/mksh, /bin/sash, /bin/tcsh, /bin/yash, /bin/bash, /bin/fish, /bin/bash2, /usr/bin/esh, /usr/bin/tcsh, /usr/bin/yash, /usr/bin/sash, /usr/bin/mksh, /usr/bin/fish, /usr/bin/bash, /sbin/nologin, /usr/sbin/sesh, /usr/bin/bash2, /usr/sbin/smrsh, /usr/bin/scponly, /usr/sbin/nologin, /usr/libexec/sesh, /usr/sbin/scponlyc, /usr/bin/git-shell, /usr/bin/cockpit-bridge, /usr/libexec/cockpit-agent, /usr/libexec/git-core/git-shell, /usr/bin/<a href="/docs/linux/man/2-gpg/">gpg</a>(2)?, /usr/lib/gnupg/.*, /usr/bin/gpgsm, /var/spool/at(/.*)?, /var/spool/cron</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux openshift policy is very flexible allowing users to setup their openshift processes in as secure a method as possible. </p>
<p> The following process types are defined for openshift: </p>
<p> openshift_initrc_t, openshift_cgroup_read_t, openshift_net_read_t, openshift_cron_t, openshift_t, openshift_app_t, openshift_script_t</code> </p>
<p> Note: <code>semanage permissive -a openshift_t</code> can be used to make the process type openshift_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>MCS Constrained</h2>
<p>The SELinux process type openshift_t is an MCS (Multi Category Security) constrained type. Sometimes this separation is referred to as sVirt. These types are usually used for securing multi-tenant environments, such as virtualization, containers or separation of users. The tools used to launch MCS types, pick out a different MCS label for each process group. </p>
<p> For example one process might be launched with openshift_t:s0:c1,c2, and another process launched with openshift_t:s0:c3,c4. The SELinux kernel only allows these processes can only write to content with a matching MCS label, or a MCS Label of s0. A process running with the MCS level of s0:c1,c2 is not allowed to write to content with the MCS label of s0:c3,c4</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. openshift policy is extremely flexible and has several booleans that allow you to manipulate the policy and run openshift with the tightest access possible. </p>
<p> If you want to allow openshift to access nfs file systems without labels, you must turn on the openshift_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P openshift_use_nfs 1</code> </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
<p> If you want to determine whether crond can execute jobs in the user domain as opposed to the the generic cronjob domain, you must turn on the cron_userdomain_transition boolean. Enabled by default. </p>
<p> <code>setsebool -P cron_userdomain_transition 1</code> </p>
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
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux openshift policy is very flexible allowing users to setup their openshift processes in as secure a method as possible. </p>
<p> The following port types are defined for openshift: </p>
<dl>
<dt><code>openshift_port_t</code></p>
<dd>
<dd></dl>
<h2>Managed Files</h2>
<p>The SELinux process type openshift_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>anon_inodefs_t</code> </p>
<p> <code>hugetlbfs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/hugepages</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/lib/udev/devices/hugepages</p>
<p> <code>nfs_t</code> </p>
<p> <code>openshift_file_type</code> </p>
<p> <code>openshift_tmpfs_t</code> </p>
<p> <code>postfix_spool_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix/defer(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix/flush(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix/deferred(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/postfix/maildrop(/.*)?</p>
<p> <code>security_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/selinux</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux openshift policy is very flexible allowing users to setup their openshift processes in as secure a method as possible. </p>
<p> EQUIVALENCE DIRECTORIES</code> </p>
<p> openshift policy stores data with multiple different file context types under the /var/lib/openshift directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/lib/openshift /srv/openshift</code><br />
 <code>restorecon -R -v /srv/openshift</code> </p>
<p> openshift policy stores data with multiple different file context types under the /var/lib/stickshift directory. If you would like to store the data in a different directory you can use the semanage command to create an equivalence mapping. If you wanted to store this data under the /srv dirctory you would execute the following command: </p>
<p> <code>semanage fcontext -a -e /var/lib/stickshift /srv/stickshift</code><br />
 <code>restorecon -R -v /srv/stickshift</code> </p>
<p> <code>STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the openshift, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t openshift_var_run_t &#8216;/srv/myopenshift_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myopenshift_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for openshift:</i> </p>
<p> <code>openshift_cgroup_read_exec_t</code> </p>
<p> &#8211; Set files with the openshift_cgroup_read_exec_t type, if you want to transition an executable to the openshift_cgroup_read_t domain. </p>
<p> <code>openshift_cgroup_read_tmp_t</code> </p>
<p> &#8211; Set files with the openshift_cgroup_read_tmp_t type, if you want to store openshift cgroup read temporary files in the /tmp directories. </p>
<p> <code>openshift_content_t</code> </p>
<p> &#8211; Set files with the openshift_content_t type, if you want to treat the files as openshift content. </p>
<p> <code>openshift_cron_exec_t</code> </p>
<p> &#8211; Set files with the openshift_cron_exec_t type, if you want to transition an executable to the openshift_cron_t domain. </p>
<p> <code>openshift_cron_tmp_t</code> </p>
<p> &#8211; Set files with the openshift_cron_tmp_t type, if you want to store openshift cron temporary files in the /tmp directories. </p>
<p> <code>openshift_htaccess_t</code> </p>
<p> &#8211; Set files with the openshift_htaccess_t type, if you want to treat the file as a openshift access file. </p>
<p> <code>openshift_initrc_exec_t</code> </p>
<p> &#8211; Set files with the openshift_initrc_exec_t type, if you want to transition an executable to the openshift_initrc_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/s?bin/mcollectived, /usr/s?bin/(oo|rhc)-restorer, /usr/s?bin/oo-admin-ctl-gears, /usr/s?bin/(oo|rhc)-restorer-wrapper.sh, /etc/rc.d/init.d/libra, /etc/rc.d/init.d/mcollective </p>
</dl>
<p> <code>openshift_initrc_tmp_t</code> </p>
<p> &#8211; Set files with the openshift_initrc_tmp_t type, if you want to store openshift initrc temporary files in the /tmp directories. </p>
<p> <code>openshift_log_t</code> </p>
<p> &#8211; Set files with the openshift_log_t type, if you want to treat the data as openshift log data, usually stored under the /var/log directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/log/openshift(/.*)?, /var/log/mcollective.log.* </p>
</dl>
<p> <code>openshift_net_read_exec_t</code> </p>
<p> &#8211; Set files with the openshift_net_read_exec_t type, if you want to transition an executable to the openshift_net_read_t domain. </p>
<p> <code>openshift_ra_content_t</code> </p>
<p> &#8211; Set files with the openshift_ra_content_t type, if you want to treat the files as openshift read/append content. </p>
<p> <code>openshift_rw_content_t</code> </p>
<p> &#8211; Set files with the openshift_rw_content_t type, if you want to treat the files as openshift read/write content. </p>
<p> <code>openshift_rw_file_t</code> </p>
<p> &#8211; Set files with the openshift_rw_file_t type, if you want to treat the files as openshift rw content. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/openshift/.*/data(/.*)?, /var/lib/stickshift/.*/data(/.*)? </p>
</dl>
<p> <code>openshift_script_exec_t</code> </p>
<p> &#8211; Set files with the openshift_script_exec_t type, if you want to transition an executable to the openshift_script_t domain. </p>
<p> <code>openshift_tmp_t</code> </p>
<p> &#8211; Set files with the openshift_tmp_t type, if you want to store openshift temporary files in the /tmp directories. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/openshift/.*/.tmp(/.*)?, /var/lib/openshift/.*/.sandbox(/.*)?, /var/lib/stickshift/.*/.tmp(/.*)?, /var/lib/stickshift/.*/.sandbox(/.*)? </p>
</dl>
<p> <code>openshift_tmpfs_t</code> </p>
<p> &#8211; Set files with the openshift_tmpfs_t type, if you want to store openshift files on a tmpfs file system. </p>
<p> <code>openshift_var_lib_t</code> </p>
<p> &#8211; Set files with the openshift_var_lib_t type, if you want to store the openshift files under the /var/lib directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/openshift(/.*)?, /var/lib/stickshift(/.*)?, /var/lib/containers/home(/.*)? </p>
</dl>
<p> <code>openshift_var_run_t</code> </p>
<p> &#8211; Set files with the openshift_var_run_t type, if you want to store the openshift files under the /run or /var/run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/openshift(/.*)?, /var/run/stickshift(/.*)? </p>
</dl>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-openshift/">openshift</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-openshift_app_selinux/">openshift_app_selinux</a>(8), <a href="/docs/linux/man/8-openshift_app_selinux/">openshift_app_selinux</a>(8), <a href="/docs/linux/man/8-openshift_cgroup_read_selinux/">openshift_cgroup_read_selinux</a>(8), <a href="/docs/linux/man/8-openshift_cgroup_read_selinux/">openshift_cgroup_read_selinux</a>(8), <a href="/docs/linux/man/8-openshift_cron_selinux/">openshift_cron_selinux</a>(8), <a href="/docs/linux/man/8-openshift_cron_selinux/">openshift_cron_selinux</a>(8), <a href="/docs/linux/man/8-openshift_initrc_selinux/">openshift_initrc_selinux</a>(8), <a href="/docs/linux/man/8-openshift_initrc_selinux/">openshift_initrc_selinux</a>(8), <a href="/docs/linux/man/8-openshift_net_read_selinux/">openshift_net_read_selinux</a>(8), <a href="/docs/linux/man/8-openshift_net_read_selinux/">openshift_net_read_selinux</a>(8), <a href="/docs/linux/man/8-openshift_script_selinux/">openshift_script_selinux</a>(8), <a href="/docs/linux/man/8-openshift_script_selinux/">openshift_script_selinux</a>(8) </p>
