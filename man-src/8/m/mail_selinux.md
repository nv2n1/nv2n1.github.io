---
title: "mail_selinux(8)"
name: "mail_selinux"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mail_selinux/"
description: "mail_selinux – Security Enhanced Linux Policy for the mail processes"
---

<p>mail_selinux &#8211; Security Enhanced Linux Policy for the mail processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the mail processes via flexible mandatory access control. </p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. mail policy is extremely flexible and has several booleans that allow you to manipulate the policy and run mail with the tightest access possible. </p>
<p> If you want to allow postfix_local domain full write access to mail_spool directorie, you must turn on the allow_postfix_local_write_mail_spool boolean. </p>
<p> <code>setsebool -P allow_postfix_local_write_mail_spool 1</code> </p>
<p> If you want to allow http daemon to send mai, you must turn on the httpd_can_sendmail boolean. </p>
<p> <code>setsebool -P httpd_can_sendmail 1</code> </p>
<p> If you want to allow syslogd daemon to send mai, you must turn on the logging_syslogd_can_sendmail boolean. </p>
<p> <code>setsebool -P logging_syslogd_can_sendmail 1</code> </p>
<p> If you want to allow gitisis daemon to send mai, you must turn on the gitosis_can_sendmail boolean. </p>
<p> <code>setsebool -P gitosis_can_sendmail 1</code></p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the mailman_mail_t, mailman_cgi_t, mailman_queue_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the mailman_mail_t, mailman_cgi_t, mailman_queue_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the mailman_mail_t, mailman_cgi_t, mailman_queue_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux mail policy is very flexible allowing users to setup their mail processes in as secure a method as possible. </p>
<p> The following file types are defined for mail: </p>
<p> mail_home_rw_t </code> </p>
<p> &#8211; Set files with the mail_home_rw_t type, if you want to treat the files as mail home read/write content. </p>
<p> <code>mail_home_t </code> </p>
<p> &#8211; Set files with the mail_home_t type, if you want to store mail files in the users home directory. </p>
<dl>
<dt>Paths:</p>
<dd>/root/.forward, /root/.mailrc, /root/dead.letter </p>
</dl>
<p> <code>mail_munin_plugin_exec_t </code> </p>
<p> &#8211; Set files with the mail_munin_plugin_exec_t type, if you want to transition an executable to the mail_munin_plugin_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/share/munin/plugins/postfix_mail.*, /usr/share/munin/plugins/mailscanner, /usr/share/munin/plugins/courier_mta_.*, /usr/share/munin/plugins/mailman, /usr/share/munin/plugins/exim_mail.*, /usr/share/munin/plugins/qmail.*, /usr/share/munin/plugins/sendmail_.* </p>
</dl>
<p> <code>mail_munin_plugin_tmp_t </code> </p>
<p> &#8211; Set files with the mail_munin_plugin_tmp_t type, if you want to store mail munin plugin temporary files in the /tmp directories. </p>
<p> <code>mail_spool_t </code> </p>
<p> &#8211; Set files with the mail_spool_t type, if you want to store the mail files under the /var/spool directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/mail(/.*)?, /var/spool/imap(/.*)?, /var/spool/mail(/.*)? </p>
</dl>
<p> <code>mailman_archive_t </code> </p>
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
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux mail policy is very flexible allowing users to setup their mail processes in as secure a method as possible. </p>
<p> The following port types are defined for mail: </p>
<dl>
<dt><code>mail_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 2000,3905</dl>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux mail policy is very flexible allowing users to setup their mail processes in as secure a method as possible. </p>
<p> The following process types are defined for mail: </p>
<p> mailman_cgi_t, mailman_mail_t, mail_munin_plugin_t, mailman_queue_t </code> </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-mail/">mail</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8)</p>
