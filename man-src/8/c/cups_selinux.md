---
title: "cups_selinux(8)"
name: "cups_selinux"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cups_selinux/"
description: "cups_selinux – Security Enhanced Linux Policy for the cups processes"
---

<p>cups_selinux &#8211; Security Enhanced Linux Policy for the cups processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the cups processes via flexible mandatory access control. </p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the cups_pdf_t, cupsd_config_t, cupsd_lpd_t, cupsd_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the cups_pdf_t, cupsd_config_t, cupsd_lpd_t, cupsd_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the cups_pdf_t, cupsd_config_t, cupsd_lpd_t, cupsd_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux cups policy is very flexible allowing users to setup their cups processes in as secure a method as possible. </p>
<p> The following file types are defined for cups: </p>
<p> cups_pdf_exec_t </code> </p>
<p> &#8211; Set files with the cups_pdf_exec_t type, if you want to transition an executable to the cups_pdf_t domain. </p>
<p> <code>cups_pdf_tmp_t </code> </p>
<p> &#8211; Set files with the cups_pdf_tmp_t type, if you want to store cups pdf temporary files in the /tmp directories. </p>
<p> <code>cupsd_config_exec_t </code> </p>
<p> &#8211; Set files with the cupsd_config_exec_t type, if you want to transition an executable to the cupsd_config_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/printconf-backend, /usr/sbin/hal_lpadmin, /usr/lib/udev/udev-configure-printer, /usr/libexec/cups-pk-helper-mechanism, /usr/libexec/hal_lpadmin, /lib/udev/udev-configure-printer, /usr/bin/cups-config-daemon </p>
</dl>
<p> <code>cupsd_config_var_run_t </code> </p>
<p> &#8211; Set files with the cupsd_config_var_run_t type, if you want to store the cupsd config files under the /run directory. </p>
<p> <code>cupsd_etc_t </code> </p>
<p> &#8211; Set files with the cupsd_etc_t type, if you want to store cupsd files in the /etc directories. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/share/cups(/.*)?, /etc/cups(/.*)? </p>
</dl>
<p> <code>cupsd_exec_t </code> </p>
<p> &#8211; Set files with the cupsd_exec_t type, if you want to transition an executable to the cupsd_t domain. </p>
<p> <code>cupsd_initrc_exec_t </code> </p>
<p> &#8211; Set files with the cupsd_initrc_exec_t type, if you want to transition an executable to the cupsd_initrc_t domain. </p>
<p> <code>cupsd_interface_t </code> </p>
<p> &#8211; Set files with the cupsd_interface_t type, if you want to treat the files as cupsd interface data. </p>
<p> <code>cupsd_lock_t </code> </p>
<p> &#8211; Set files with the cupsd_lock_t type, if you want to treat the files as cupsd lock data, stored under the /var/lock directory </p>
<p> <code>cupsd_log_t </code> </p>
<p> &#8211; Set files with the cupsd_log_t type, if you want to treat the data as cupsd log data, usually stored under the /var/log directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/log/cups(/.*)?, /var/log/turboprint.*, /usr/local/Brother/fax/.*.log </p>
</dl>
<p> <code>cupsd_lpd_exec_t </code> </p>
<p> &#8211; Set files with the cupsd_lpd_exec_t type, if you want to transition an executable to the cupsd_lpd_t domain. </p>
<p> <code>cupsd_lpd_tmp_t </code> </p>
<p> &#8211; Set files with the cupsd_lpd_tmp_t type, if you want to store cupsd lpd temporary files in the /tmp directories. </p>
<p> <code>cupsd_lpd_var_run_t </code> </p>
<p> &#8211; Set files with the cupsd_lpd_var_run_t type, if you want to store the cupsd lpd files under the /run directory. </p>
<p> <code>cupsd_rw_etc_t </code> </p>
<p> &#8211; Set files with the cupsd_rw_etc_t type, if you want to store cupsd rw files in the /etc directories. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/cups/lpoptions.*, /usr/local/linuxprinter/ppd(/.*)?, /etc/cups/subscriptions.*, /opt/brother/Printers(.*/)?inf(/.*)?, /usr/local/Brother/(.*/)?inf(/.*)?, /etc/cups/classes.conf.*, /usr/lib/bjlib(/.*)?, /etc/cups/ppd(/.*)?, /opt/gutenprint/ppds(/.*)?, /etc/printcap.*, /etc/alchemist/namespace/printconf(/.*)?, /usr/local/Printer/(.*/)?inf(/.*)?, /var/lib/cups/certs, /etc/cups/ppds.dat, /etc/cups/certs, /etc/cups/certs/.*, /etc/cups/printers.conf.*, /var/lib/cups/certs/.*, /var/cache/foomatic(/.*)?, /var/cache/alchemist/printconf.*, /etc/cups/cupsd.conf.*, /var/cache/cups(/.*)?, /usr/share/foomatic/db/oldprinterids </p>
</dl>
<p> <code>cupsd_tmp_t </code> </p>
<p> &#8211; Set files with the cupsd_tmp_t type, if you want to store cupsd temporary files in the /tmp directories. </p>
<p> <code>cupsd_unit_file_t </code> </p>
<p> &#8211; Set files with the cupsd_unit_file_t type, if you want to treat the files as cupsd unit content. </p>
<p> <code>cupsd_var_run_t </code> </p>
<p> &#8211; Set files with the cupsd_var_run_t type, if you want to store the cupsd files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/ccpd(/.*)?, /var/ekpd(/.*)?, /var/turboprint(/.*)?, /var/run/cups(/.*)? </p>
</dl>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux cups policy is very flexible allowing users to setup their cups processes in as secure a method as possible. </p>
<p> The following process types are defined for cups: </p>
<p> cupsd_t, cupsd_config_t, cupsd_lpd_t, cups_pdf_t </code> </p>
<p> Note: <code>semanage permissive -a PROCESS_TYPE </code> can be used to make a process type permissive. Permissive process types are not denied access by SELinux. AVC messages will still be generated.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-cups/">cups</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) </p>
