---
title: "courier_selinux(8)"
name: "courier_selinux"
section: "8"
letter: "c"
url: "/docs/linux/man/8-courier_selinux/"
description: "courier_selinux – Security Enhanced Linux Policy for the courier processes"
---

<p>courier_selinux &#8211; Security Enhanced Linux Policy for the courier processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the courier processes via flexible mandatory access control. </p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the courier_authdaemon_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the courier_authdaemon_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the courier_authdaemon_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux courier policy is very flexible allowing users to setup their courier processes in as secure a method as possible. </p>
<p> The following file types are defined for courier: </p>
<p> courier_authdaemon_exec_t </code> </p>
<p> &#8211; Set files with the courier_authdaemon_exec_t type, if you want to transition an executable to the courier_authdaemon_t domain. </p>
<p> <code>courier_etc_t </code> </p>
<p> &#8211; Set files with the courier_etc_t type, if you want to store courier files in the /etc directories. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/courier/rootcerts(/.*)?, /etc/courier(/.*)? </p>
</dl>
<p> <code>courier_exec_t </code> </p>
<p> &#8211; Set files with the courier_exec_t type, if you want to transition an executable to the courier_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/courierlogger, /usr/lib/courier/courier/.*, /usr/sbin/courierldapaliasd </p>
</dl>
<p> <code>courier_pcp_exec_t </code> </p>
<p> &#8211; Set files with the courier_pcp_exec_t type, if you want to transition an executable to the courier_pcp_t domain. </p>
<p> <code>courier_pop_exec_t </code> </p>
<p> &#8211; Set files with the courier_pop_exec_t type, if you want to transition an executable to the courier_pop_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/courier/imapd, /usr/lib/courier/courier/courierpop.*, /usr/lib/courier/pop3d, /usr/lib/courier/courier/imaplogin, /usr/bin/imapd </p>
</dl>
<p> <code>courier_spool_t </code> </p>
<p> &#8211; Set files with the courier_spool_t type, if you want to store the courier files under the /var/spool directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/spool/authdaemon(/.*)?, /var/spool/courier(/.*)? </p>
</dl>
<p> <code>courier_sqwebmail_exec_t </code> </p>
<p> &#8211; Set files with the courier_sqwebmail_exec_t type, if you want to transition an executable to the courier_sqwebmail_t domain. </p>
<p> <code>courier_tcpd_exec_t </code> </p>
<p> &#8211; Set files with the courier_tcpd_exec_t type, if you want to transition an executable to the courier_tcpd_t domain. </p>
<p> <code>courier_var_lib_t </code> </p>
<p> &#8211; Set files with the courier_var_lib_t type, if you want to store the courier files under the /var/lib directory. </p>
<p> <code>courier_var_run_t </code> </p>
<p> &#8211; Set files with the courier_var_run_t type, if you want to store the courier files under the /run directory. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux courier policy is very flexible allowing users to setup their courier processes in as secure a method as possible. </p>
<p> The following process types are defined for courier: </p>
<p> courier_sqwebmail_t, courier_tcpd_t, courier_authdaemon_t, courier_pcp_t, courier_pop_t </code> </p>
<p> Note: <code>semanage permissive -a PROCESS_TYPE </code> can be used to make a process type permissive. Permissive process types are not denied access by SELinux. AVC messages will still be generated.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-courier/">courier</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) </p>
