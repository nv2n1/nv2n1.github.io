---
title: "systemd_selinux(8)"
name: "systemd_selinux"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd_selinux/"
description: "systemd_selinux – Security Enhanced Linux Policy for the systemd processes"
---

<p>systemd_selinux &#8211; Security Enhanced Linux Policy for the systemd processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the systemd processes via flexible mandatory access control. </p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. systemd policy is extremely flexible and has several booleans that allow you to manipulate the policy and run systemd with the tightest access possible. </p>
<p> If you want to allow Git daemon system to access cifs file systems, you must turn on the git_system_use_cifs boolean. </p>
<p> <code>setsebool -P git_system_use_cifs 1</code> </p>
<p> If you want to allow Git daemon system to search home directories, you must turn on the git_system_enable_homedirs boolean. </p>
<p> <code>setsebool -P git_system_enable_homedirs 1</code> </p>
<p> If you want to allow Git daemon system to access nfs file systems, you must turn on the git_system_use_nfs boolean. </p>
<p> <code>setsebool -P git_system_use_nfs 1</code> </p>
<p> If you want to allow clamscan to non security files on a syste, you must turn on the clamscan_can_scan_system boolean. </p>
<p> <code>setsebool -P clamscan_can_scan_system 1</code> </p>
<p> If you want to enable support for systemd as the init program, you must turn on the init_systemd boolean. </p>
<p> <code>setsebool -P init_systemd 1</code></p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the system_cronjob_t, systemd_notify_t, systemd_logind_t, system_dbusd_t, systemd_passwd_agent_t, systemd_logger_t, systemd_tmpfiles_t, system_mail_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the system_cronjob_t, systemd_notify_t, systemd_logind_t, system_dbusd_t, systemd_passwd_agent_t, systemd_logger_t, systemd_tmpfiles_t, system_mail_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the system_cronjob_t, systemd_notify_t, systemd_logind_t, system_dbusd_t, systemd_passwd_agent_t, systemd_logger_t, systemd_tmpfiles_t, system_mail_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux systemd policy is very flexible allowing users to setup their systemd processes in as secure a method as possible. </p>
<p> The following file types are defined for systemd: </p>
<p> systemd_logger_exec_t </code> </p>
<p> &#8211; Set files with the systemd_logger_exec_t type, if you want to transition an executable to the systemd_logger_t domain. </p>
<p> <code>systemd_logind_exec_t </code> </p>
<p> &#8211; Set files with the systemd_logind_exec_t type, if you want to transition an executable to the systemd_logind_t domain. </p>
<p> <code>systemd_logind_sessions_t </code> </p>
<p> &#8211; Set files with the systemd_logind_sessions_t type, if you want to treat the files as systemd logind sessions data. </p>
<p> <code>systemd_logind_var_run_t </code> </p>
<p> &#8211; Set files with the systemd_logind_var_run_t type, if you want to store the systemd logind files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/nologin, /var/run/systemd/users(/.*)?, /var/run/systemd/seats(/.*)? </p>
</dl>
<p> <code>systemd_notify_exec_t </code> </p>
<p> &#8211; Set files with the systemd_notify_exec_t type, if you want to transition an executable to the systemd_notify_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/systemd-notify, /bin/systemd-notify </p>
</dl>
<p> <code>systemd_passwd_agent_exec_t </code> </p>
<p> &#8211; Set files with the systemd_passwd_agent_exec_t type, if you want to transition an executable to the systemd_passwd_agent_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/bin/systemd-tty-ask-password-agent, /usr/bin/systemd-gnome-ask-password-agent, /usr/bin/systemd-tty-ask-password-agent </p>
</dl>
<p> <code>systemd_passwd_var_run_t </code> </p>
<p> &#8211; Set files with the systemd_passwd_var_run_t type, if you want to store the systemd passwd files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/systemd/ask-password(/.*)?, /var/run/systemd/ask-password-block(/.*)? </p>
</dl>
<p> <code>systemd_systemctl_exec_t </code> </p>
<p> &#8211; Set files with the systemd_systemctl_exec_t type, if you want to transition an executable to the systemd_systemctl_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/systemctl, /bin/systemctl </p>
</dl>
<p> <code>systemd_tmpfiles_exec_t </code> </p>
<p> &#8211; Set files with the systemd_tmpfiles_exec_t type, if you want to transition an executable to the systemd_tmpfiles_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/bin/systemd-tmpfiles, /bin/systemd-tmpfiles, /usr/lib/systemd/systemd-tmpfiles </p>
</dl>
<p> <code>systemd_unit_file_t </code> </p>
<p> &#8211; Set files with the systemd_unit_file_t type, if you want to treat the files as systemd unit content. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux systemd policy is very flexible allowing users to setup their systemd processes in as secure a method as possible. </p>
<p> The following process types are defined for systemd: </p>
<p> system_munin_plugin_t, systemd_logger_t, systemd_logind_t, system_cronjob_t, systemd_notify_t, system_mail_t, systemd_passwd_agent_t, system_dbusd_t, systemd_tmpfiles_t </code> </p>
<p> Note: <code>semanage permissive -a PROCESS_TYPE </code> can be used to make a process type permissive. Permissive process types are not denied access by SELinux. AVC messages will still be generated.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-systemd/">systemd</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8)</p>
