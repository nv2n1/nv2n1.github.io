---
title: "postfix_selinux(8)"
name: "postfix_selinux"
section: "8"
letter: "p"
url: "/docs/linux/man/8-postfix_selinux/"
description: "postfix_selinux – Security Enhanced Linux Policy for the postfix processes"
---

<p>postfix_selinux &#8211; Security Enhanced Linux Policy for the postfix processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the postfix processes via flexible mandatory access control. </p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. postfix policy is extremely flexible and has several booleans that allow you to manipulate the policy and run postfix with the tightest access possible. </p>
<p> If you want to allow postfix_local domain full write access to mail_spool directorie, you must turn on the allow_postfix_local_write_mail_spool boolean. </p>
<p> <code>setsebool -P allow_postfix_local_write_mail_spool 1</code></p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the postfix_smtp_t, postfix_map_t, postfix_showq_t, postfix_virtual_t, postfix_smtpd_t, postfix_local_t, postfix_cleanup_t, postfix_master_t, postfix_postdrop_t, postfix_pickup_t, postfix_bounce_t, postfix_qmgr_t, postfix_pipe_t, postfix_postqueue_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the postfix_smtp_t, postfix_map_t, postfix_showq_t, postfix_virtual_t, postfix_smtpd_t, postfix_local_t, postfix_cleanup_t, postfix_master_t, postfix_postdrop_t, postfix_pickup_t, postfix_bounce_t, postfix_qmgr_t, postfix_pipe_t, postfix_postqueue_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the postfix_smtp_t, postfix_map_t, postfix_showq_t, postfix_virtual_t, postfix_smtpd_t, postfix_local_t, postfix_cleanup_t, postfix_master_t, postfix_postdrop_t, postfix_pickup_t, postfix_bounce_t, postfix_qmgr_t, postfix_pipe_t, postfix_postqueue_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux postfix policy is very flexible allowing users to setup their postfix processes in as secure a method as possible. </p>
<p> The following file types are defined for postfix: </p>
<p> postfix_bounce_exec_t </code> </p>
<p> &#8211; Set files with the postfix_bounce_exec_t type, if you want to transition an executable to the postfix_bounce_t domain. </p>
<p> <code>postfix_bounce_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_bounce_tmp_t type, if you want to store postfix bounce temporary files in the /tmp directories. </p>
<p> <code>postfix_cleanup_exec_t </code> </p>
<p> &#8211; Set files with the postfix_cleanup_exec_t type, if you want to transition an executable to the postfix_cleanup_t domain. </p>
<p> <code>postfix_cleanup_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_cleanup_tmp_t type, if you want to store postfix cleanup temporary files in the /tmp directories. </p>
<p> <code>postfix_data_t </code> </p>
<p> &#8211; Set files with the postfix_data_t type, if you want to treat the files as postfix content. </p>
<p> <code>postfix_etc_t </code> </p>
<p> &#8211; Set files with the postfix_etc_t type, if you want to store postfix files in the /etc directories. </p>
<p> <code>postfix_exec_t </code> </p>
<p> &#8211; Set files with the postfix_exec_t type, if you want to transition an executable to the postfix_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/postfix/postfix-script.*, /usr/libexec/postfix/.* </p>
</dl>
<p> <code>postfix_initrc_exec_t </code> </p>
<p> &#8211; Set files with the postfix_initrc_exec_t type, if you want to transition an executable to the postfix_initrc_t domain. </p>
<p> <code>postfix_keytab_t </code> </p>
<p> &#8211; Set files with the postfix_keytab_t type, if you want to treat the files as kerberos keytab files. </p>
<p> <code>postfix_local_exec_t </code> </p>
<p> &#8211; Set files with the postfix_local_exec_t type, if you want to transition an executable to the postfix_local_t domain. </p>
<p> <code>postfix_local_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_local_tmp_t type, if you want to store postfix local temporary files in the /tmp directories. </p>
<p> <code>postfix_map_exec_t </code> </p>
<p> &#8211; Set files with the postfix_map_exec_t type, if you want to transition an executable to the postfix_map_t domain. </p>
<p> <code>postfix_map_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_map_tmp_t type, if you want to store postfix map temporary files in the /tmp directories. </p>
<p> <code>postfix_master_exec_t </code> </p>
<p> &#8211; Set files with the postfix_master_exec_t type, if you want to transition an executable to the postfix_master_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/postcat, /usr/sbin/postfix, /usr/libexec/postfix/master, /usr/sbin/postkick, /usr/sbin/postsuper, /usr/sbin/postalias, /usr/sbin/postlock, /usr/sbin/postlog </p>
</dl>
<p> <code>postfix_pickup_exec_t </code> </p>
<p> &#8211; Set files with the postfix_pickup_exec_t type, if you want to transition an executable to the postfix_pickup_t domain. </p>
<p> <code>postfix_pickup_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_pickup_tmp_t type, if you want to store postfix pickup temporary files in the /tmp directories. </p>
<p> <code>postfix_pipe_exec_t </code> </p>
<p> &#8211; Set files with the postfix_pipe_exec_t type, if you want to transition an executable to the postfix_pipe_t domain. </p>
<p> <code>postfix_pipe_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_pipe_tmp_t type, if you want to store postfix pipe temporary files in the /tmp directories. </p>
<p> <code>postfix_postdrop_exec_t </code> </p>
<p> &#8211; Set files with the postfix_postdrop_exec_t type, if you want to transition an executable to the postfix_postdrop_t domain. </p>
<p> <code>postfix_postqueue_exec_t </code> </p>
<p> &#8211; Set files with the postfix_postqueue_exec_t type, if you want to transition an executable to the postfix_postqueue_t domain. </p>
<p> <code>postfix_private_t </code> </p>
<p> &#8211; Set files with the postfix_private_t type, if you want to treat the files as postfix private data. </p>
<p> <code>postfix_prng_t </code> </p>
<p> &#8211; Set files with the postfix_prng_t type, if you want to treat the files as postfix prng data. </p>
<p> <code>postfix_public_t </code> </p>
<p> &#8211; Set files with the postfix_public_t type, if you want to treat the files as postfix public data. </p>
<p> <code>postfix_qmgr_exec_t </code> </p>
<p> &#8211; Set files with the postfix_qmgr_exec_t type, if you want to transition an executable to the postfix_qmgr_t domain. </p>
<p> <code>postfix_qmgr_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_qmgr_tmp_t type, if you want to store postfix qmgr temporary files in the /tmp directories. </p>
<p> <code>postfix_showq_exec_t </code> </p>
<p> &#8211; Set files with the postfix_showq_exec_t type, if you want to transition an executable to the postfix_showq_t domain. </p>
<p> <code>postfix_smtp_exec_t </code> </p>
<p> &#8211; Set files with the postfix_smtp_exec_t type, if you want to transition an executable to the postfix_smtp_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/libexec/postfix/lmtp, /usr/libexec/postfix/smtp, /usr/libexec/postfix/scache </p>
</dl>
<p> <code>postfix_smtp_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_smtp_tmp_t type, if you want to store postfix smtp temporary files in the /tmp directories. </p>
<p> <code>postfix_smtpd_exec_t </code> </p>
<p> &#8211; Set files with the postfix_smtpd_exec_t type, if you want to transition an executable to the postfix_smtpd_t domain. </p>
<p> <code>postfix_smtpd_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_smtpd_tmp_t type, if you want to store postfix smtpd temporary files in the /tmp directories. </p>
<p> <code>postfix_spool_bounce_t </code> </p>
<p> &#8211; Set files with the postfix_spool_bounce_t type, if you want to treat the files as postfix spool bounce data. </p>
<p> <code>postfix_spool_flush_t </code> </p>
<p> &#8211; Set files with the postfix_spool_flush_t type, if you want to treat the files as postfix spool flush data. </p>
<p> <code>postfix_spool_maildrop_t </code> </p>
<p> &#8211; Set files with the postfix_spool_maildrop_t type, if you want to treat the files as postfix spool maildrop data. </p>
<dl>
<dt>Paths:</p>
<dd>/var/spool/postfix/defer(/.*)?, /var/spool/postfix/deferred(/.*)?, /var/spool/postfix/maildrop(/.*)? </p>
</dl>
<p> <code>postfix_spool_t </code> </p>
<p> &#8211; Set files with the postfix_spool_t type, if you want to store the postfix files under the /var/spool directory. </p>
<p> <code>postfix_var_run_t </code> </p>
<p> &#8211; Set files with the postfix_var_run_t type, if you want to store the postfix files under the /run directory. </p>
<p> <code>postfix_virtual_exec_t </code> </p>
<p> &#8211; Set files with the postfix_virtual_exec_t type, if you want to transition an executable to the postfix_virtual_t domain. </p>
<p> <code>postfix_virtual_tmp_t </code> </p>
<p> &#8211; Set files with the postfix_virtual_tmp_t type, if you want to store postfix virtual temporary files in the /tmp directories. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux postfix policy is very flexible allowing users to setup their postfix processes in as secure a method as possible. </p>
<p> The following port types are defined for postfix: </p>
<dl>
<dt><code>postfix_policyd_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 10031</dl>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux postfix policy is very flexible allowing users to setup their postfix processes in as secure a method as possible. </p>
<p> The following process types are defined for postfix: </p>
<p> postfix_bounce_t, postfix_cleanup_t, postfix_showq_t, postfix_virtual_t, postfix_postdrop_t, postfix_postqueue_t, postfix_pipe_t, postfix_master_t, postfix_pickup_t, postfix_local_t, postfix_smtpd_t, postfix_qmgr_t, postfix_smtp_t, postfix_map_t </code> </p>
<p> Note: <code>semanage permissive -a PROCESS_TYPE </code> can be used to make a process type permissive. Permissive process types are not denied access by SELinux. AVC messages will still be generated.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage port</code> can also be used to manipulate the port definitions </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-postfix/">postfix</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8)</p>
