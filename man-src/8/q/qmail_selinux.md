---
title: "qmail_selinux(8)"
name: "qmail_selinux"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qmail_selinux/"
description: "qmail_selinux – Security Enhanced Linux Policy for the qmail processes"
---

<p>qmail_selinux &#8211; Security Enhanced Linux Policy for the qmail processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the qmail processes via flexible mandatory access control. </p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the qmail_local_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the qmail_local_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the qmail_local_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux qmail policy is very flexible allowing users to setup their qmail processes in as secure a method as possible. </p>
<p> The following file types are defined for qmail: </p>
<p> qmail_alias_home_t </code> </p>
<p> &#8211; Set files with the qmail_alias_home_t type, if you want to store qmail alias files in the users home directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/qmail/alias, /var/qmail/alias(/.*)? </p>
</dl>
<p> <code>qmail_clean_exec_t </code> </p>
<p> &#8211; Set files with the qmail_clean_exec_t type, if you want to transition an executable to the qmail_clean_t domain. </p>
<p> <code>qmail_etc_t </code> </p>
<p> &#8211; Set files with the qmail_etc_t type, if you want to store qmail files in the /etc directories. </p>
<dl>
<dt>Paths:</p>
<dd>/var/qmail/owners(/.*)?, /var/qmail/control(/.*)? </p>
</dl>
<p> <code>qmail_exec_t </code> </p>
<p> &#8211; Set files with the qmail_exec_t type, if you want to transition an executable to the qmail_t domain. </p>
<p> <code>qmail_inject_exec_t </code> </p>
<p> &#8211; Set files with the qmail_inject_exec_t type, if you want to transition an executable to the qmail_inject_t domain. </p>
<p> <code>qmail_keytab_t </code> </p>
<p> &#8211; Set files with the qmail_keytab_t type, if you want to treat the files as kerberos keytab files. </p>
<p> <code>qmail_local_exec_t </code> </p>
<p> &#8211; Set files with the qmail_local_exec_t type, if you want to transition an executable to the qmail_local_t domain. </p>
<p> <code>qmail_lspawn_exec_t </code> </p>
<p> &#8211; Set files with the qmail_lspawn_exec_t type, if you want to transition an executable to the qmail_lspawn_t domain. </p>
<p> <code>qmail_queue_exec_t </code> </p>
<p> &#8211; Set files with the qmail_queue_exec_t type, if you want to transition an executable to the qmail_queue_t domain. </p>
<p> <code>qmail_remote_exec_t </code> </p>
<p> &#8211; Set files with the qmail_remote_exec_t type, if you want to transition an executable to the qmail_remote_t domain. </p>
<p> <code>qmail_rspawn_exec_t </code> </p>
<p> &#8211; Set files with the qmail_rspawn_exec_t type, if you want to transition an executable to the qmail_rspawn_t domain. </p>
<p> <code>qmail_send_exec_t </code> </p>
<p> &#8211; Set files with the qmail_send_exec_t type, if you want to transition an executable to the qmail_send_t domain. </p>
<p> <code>qmail_smtpd_exec_t </code> </p>
<p> &#8211; Set files with the qmail_smtpd_exec_t type, if you want to transition an executable to the qmail_smtpd_t domain. </p>
<p> <code>qmail_splogger_exec_t </code> </p>
<p> &#8211; Set files with the qmail_splogger_exec_t type, if you want to transition an executable to the qmail_splogger_t domain. </p>
<p> <code>qmail_spool_t </code> </p>
<p> &#8211; Set files with the qmail_spool_t type, if you want to store the qmail files under the /var/spool directory. </p>
<p> <code>qmail_start_exec_t </code> </p>
<p> &#8211; Set files with the qmail_start_exec_t type, if you want to transition an executable to the qmail_start_t domain. </p>
<p> <code>qmail_tcp_env_exec_t </code> </p>
<p> &#8211; Set files with the qmail_tcp_env_exec_t type, if you want to transition an executable to the qmail_tcp_env_t domain. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux qmail policy is very flexible allowing users to setup their qmail processes in as secure a method as possible. </p>
<p> The following process types are defined for qmail: </p>
<p> qmail_tcp_env_t, qmail_rspawn_t, qmail_inject_t, qmail_lspawn_t, qmail_clean_t, qmail_local_t, qmail_smtpd_t, qmail_start_t, qmail_send_t, qmail_remote_t, qmail_queue_t, qmail_splogger_t </code> </p>
<p> Note: <code>semanage permissive -a PROCESS_TYPE </code> can be used to make a process type permissive. Permissive process types are not denied access by SELinux. AVC messages will still be generated.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-qmail/">qmail</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) </p>
