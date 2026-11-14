---
title: "ipsec_mgmt_selinux(8)"
name: "ipsec_mgmt_selinux"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_mgmt_selinux/"
description: "ipsec_mgmt_selinux – Security Enhanced Linux Policy for the ipsec_mgmt processes"
---

<p>ipsec_mgmt_selinux &#8211; Security Enhanced Linux Policy for the ipsec_mgmt processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the ipsec_mgmt processes via flexible mandatory access control. The ipsec_mgmt processes execute with the ipsec_mgmt_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep ipsec_mgmt_t</code> </p>
<h2>Entrypoints</h2>
<p>The ipsec_mgmt_t SELinux type can be entered via the <code>ipsec_mgmt_exec_t, shell_exec_t</code> file types. </p>
<p> The default entrypoint paths for the ipsec_mgmt_t domain are the following: </p>
<p> /usr/sbin/ipsec, /usr/sbin/swanctl, /usr/sbin/strongswan, /usr/sbin/strongimcv, /usr/lib/ipsec/_plutorun, /usr/lib/ipsec/_plutoload, /usr/libexec/ipsec/_plutorun, /usr/libexec/ipsec/_plutoload, /usr/libexec/nm-openswan-service, /usr/libexec/nm-libreswan-service, /bin/d?ash, /bin/zsh.*, /bin/ksh.*, /usr/bin/d?ash, /usr/bin/zsh.*, /usr/bin/ksh.*, /bin/esh, /bin/mksh, /bin/sash, /bin/tcsh, /bin/yash, /bin/bash, /bin/fish, /bin/bash2, /usr/bin/esh, /usr/bin/tcsh, /usr/bin/yash, /usr/bin/sash, /usr/bin/mksh, /usr/bin/fish, /usr/bin/bash, /sbin/nologin, /usr/sbin/sesh, /usr/bin/bash2, /usr/sbin/smrsh, /usr/bin/scponly, /usr/sbin/nologin, /usr/libexec/sesh, /usr/sbin/scponlyc, /usr/bin/git-shell, /usr/bin/cockpit-bridge, /usr/libexec/cockpit-agent, /usr/libexec/git-core/git-shell</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux ipsec_mgmt policy is very flexible allowing users to setup their ipsec_mgmt processes in as secure a method as possible. </p>
<p> The following process types are defined for ipsec_mgmt: </p>
<p> ipsec_mgmt_t</code> </p>
<p> Note: <code>semanage permissive -a ipsec_mgmt_t</code> can be used to make the process type ipsec_mgmt_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. ipsec_mgmt policy is extremely flexible and has several booleans that allow you to manipulate the policy and run ipsec_mgmt with the tightest access possible. </p>
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
<p>The SELinux process type ipsec_mgmt_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>ipsec_key_file_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/ipsec.d(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/racoon/certs(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/ipsec.secrets.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/strongswan/ipsec.d(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/strongswan/ipsec.secrets.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/racoon/psk.txt</p>
<p> <code>ipsec_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/pluto.log.*</p>
<p> <code>ipsec_mgmt_lock_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lock/subsys/ipsec</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lock/subsys/strongswan</p>
<p> <code>ipsec_mgmt_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/pluto/ipsec.info</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/pluto/ipsec_setup.pid</p>
<p> <code>ipsec_tmp_t</code> </p>
<p> <code>ipsec_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/racoon(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/pluto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/charon.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/racoon.pid</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/charon.ctl</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/charon.vici</p>
<p> <code>net_conf_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/hosts[^/]*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/yp.conf.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/denyhosts.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/hosts.deny.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/resolv.conf.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/.resolv.conf.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/resolv-secure.conf.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/network(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/sysconfig/networking(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/sysconfig/network-scripts(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/sysconfig/network-scripts/.*resolv.conf</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/NetworkManager/resolv.conf.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/ethers</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/ntp.conf</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/resolve/resolv.conf</p>
<p> <code>systemd_passwd_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/ask-password(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/ask-password-block(/.*)?</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux ipsec_mgmt policy is very flexible allowing users to setup their ipsec_mgmt processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the ipsec_mgmt, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t ipsec_mgmt_var_run_t &#8216;/srv/myipsec_mgmt_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myipsec_mgmt_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for ipsec_mgmt:</i> </p>
<p> <code>ipsec_mgmt_devpts_t</code> </p>
<p> &#8211; Set files with the ipsec_mgmt_devpts_t type, if you want to treat the files as ipsec mgmt devpts data. </p>
<p> <code>ipsec_mgmt_exec_t</code> </p>
<p> &#8211; Set files with the ipsec_mgmt_exec_t type, if you want to transition an executable to the ipsec_mgmt_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/ipsec, /usr/sbin/swanctl, /usr/sbin/strongswan, /usr/sbin/strongimcv, /usr/lib/ipsec/_plutorun, /usr/lib/ipsec/_plutoload, /usr/libexec/ipsec/_plutorun, /usr/libexec/ipsec/_plutoload, /usr/libexec/nm-openswan-service, /usr/libexec/nm-libreswan-service </p>
</dl>
<p> <code>ipsec_mgmt_lock_t</code> </p>
<p> &#8211; Set files with the ipsec_mgmt_lock_t type, if you want to treat the files as ipsec mgmt lock data, stored under the /var/lock directory </p>
<dl>
<dt>Paths:</p>
<dd>/var/lock/subsys/ipsec, /var/lock/subsys/strongswan </p>
</dl>
<p> <code>ipsec_mgmt_unit_file_t</code> </p>
<p> &#8211; Set files with the ipsec_mgmt_unit_file_t type, if you want to treat the files as ipsec mgmt unit content. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/systemd/system/ipsec.*, /usr/lib/systemd/system/strongswan.*, /usr/lib/systemd/system/strongimcv.*, /usr/lib/systemd/system/strongswan-swanctl.* </p>
</dl>
<p> <code>ipsec_mgmt_var_run_t</code> </p>
<p> &#8211; Set files with the ipsec_mgmt_var_run_t type, if you want to store the ipsec mgmt files under the /run or /var/run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/pluto/ipsec.info, /var/run/pluto/ipsec_setup.pid </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-ipsec_mgmt/">ipsec_mgmt</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
