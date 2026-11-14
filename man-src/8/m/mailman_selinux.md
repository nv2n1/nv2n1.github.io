---
title: "mailman_selinux(8)"
name: "mailman_selinux"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mailman_selinux/"
description: "mailman_selinux – Security Enhanced Linux Policy for the mailman processes"
---

<p>mailman_selinux &#8211; Security Enhanced Linux Policy for the mailman processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the mailman processes via flexible mandatory access control. </p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the mailman_mail_t, mailman_cgi_t, mailman_queue_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the mailman_mail_t, mailman_cgi_t, mailman_queue_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the mailman_mail_t, mailman_cgi_t, mailman_queue_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux mailman policy is very flexible allowing users to setup their mailman processes in as secure a method as possible. </p>
<p> The following file types are defined for mailman: </p>
<p> mailman_archive_t </code> </p>
<p> &#8211; Set files with the mailman_archive_t type, if you want to treat the files as mailman archive data. </p>
<p> <code>mailman_cgi_exec_t </code> </p>
<p> &#8211; Set files with the mailman_cgi_exec_t type, if you want to transition an executable to the mailman_cgi_t domain. </p>
<p> <code>mailman_cgi_tmp_t </code> </p>
<p> &#8211; Set files with the mailman_cgi_tmp_t type, if you want to store mailman cgi temporary files in the /tmp directories. </p>
<p> <code>mailman_data_t </code> </p>
<p> &#8211; Set files with the mailman_data_t type, if you want to treat the files as mailman content. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/mailman.*, /var/spool/mailman.*, /var/lib/mailman.* </p>
</dl>
<p> <code>mailman_lock_t </code> </p>
<p> &#8211; Set files with the mailman_lock_t type, if you want to treat the files as mailman lock data, stored under the /var/lock directory </p>
<p> <code>mailman_log_t </code> </p>
<p> &#8211; Set files with the mailman_log_t type, if you want to treat the data as mailman log data, usually stored under the /var/log directory. </p>
<p> <code>mailman_mail_exec_t </code> </p>
<p> &#8211; Set files with the mailman_mail_exec_t type, if you want to transition an executable to the mailman_mail_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/mailman.*/mail/mailman, /usr/lib/mailman.*/bin/mm-handler.*, /usr/share/doc/mailman.*/mm-handler.*, /usr/lib/mailman.*/bin/mailmanctl, /usr/lib/mailman.*/scripts/mailman </p>
</dl>
<p> <code>mailman_mail_tmp_t </code> </p>
<p> &#8211; Set files with the mailman_mail_tmp_t type, if you want to store mailman mail temporary files in the /tmp directories. </p>
<p> <code>mailman_queue_exec_t </code> </p>
<p> &#8211; Set files with the mailman_queue_exec_t type, if you want to transition an executable to the mailman_queue_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/mailman.*/cron/.*, /usr/lib/mailman.*/bin/qrunner </p>
</dl>
<p> <code>mailman_queue_tmp_t </code> </p>
<p> &#8211; Set files with the mailman_queue_tmp_t type, if you want to store mailman queue temporary files in the /tmp directories. </p>
<p> <code>mailman_var_run_t </code> </p>
<p> &#8211; Set files with the mailman_var_run_t type, if you want to store the mailman files under the /run directory. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux mailman policy is very flexible allowing users to setup their mailman processes in as secure a method as possible. </p>
<p> The following process types are defined for mailman: </p>
<p> mailman_cgi_t, mailman_mail_t, mailman_queue_t </code> </p>
<p> Note: <code>semanage permissive -a PROCESS_TYPE </code> can be used to make a process type permissive. Permissive process types are not denied access by SELinux. AVC messages will still be generated.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-mailman/">mailman</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) </p>
