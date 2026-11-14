---
title: "matahari_selinux(8)"
name: "matahari_selinux"
section: "8"
letter: "m"
url: "/docs/linux/man/8-matahari_selinux/"
description: "matahari_selinux – Security Enhanced Linux Policy for the matahari processes"
---

<p>matahari_selinux &#8211; Security Enhanced Linux Policy for the matahari processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the matahari processes via flexible mandatory access control. </p>
<h2>Nsswitch Domain</h2>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux matahari policy is very flexible allowing users to setup their matahari processes in as secure a method as possible. </p>
<p> The following file types are defined for matahari: </p>
<p> matahari_hostd_exec_t </code> </p>
<p> &#8211; Set files with the matahari_hostd_exec_t type, if you want to transition an executable to the matahari_hostd_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/matahari-qmf-hostd, /usr/sbin/matahari-hostd, /usr/sbin/matahari-dbus-hostd </p>
</dl>
<p> <code>matahari_hostd_unit_file_t </code> </p>
<p> &#8211; Set files with the matahari_hostd_unit_file_t type, if you want to treat the files as matahari hostd unit content. </p>
<p> <code>matahari_initrc_exec_t </code> </p>
<p> &#8211; Set files with the matahari_initrc_exec_t type, if you want to transition an executable to the matahari_initrc_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/rc.d/init.d/matahari-sysconfig, /etc/rc.d/init.d/matahari-host, /etc/rc.d/init.d/matahari-service, /etc/rc.d/init.d/matahari-sysconfig-console, /etc/rc.d/init.d/matahari-net </p>
</dl>
<p> <code>matahari_netd_exec_t </code> </p>
<p> &#8211; Set files with the matahari_netd_exec_t type, if you want to transition an executable to the matahari_netd_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/matahari-qmf-networkd, /usr/sbin/matahari-netd, /usr/sbin/matahari-dbus-networkd </p>
</dl>
<p> <code>matahari_netd_unit_file_t </code> </p>
<p> &#8211; Set files with the matahari_netd_unit_file_t type, if you want to treat the files as matahari netd unit content. </p>
<p> <code>matahari_rpcd_exec_t </code> </p>
<p> &#8211; Set files with the matahari_rpcd_exec_t type, if you want to transition an executable to the matahari_rpcd_t domain. </p>
<p> <code>matahari_rpcd_unit_file_t </code> </p>
<p> &#8211; Set files with the matahari_rpcd_unit_file_t type, if you want to treat the files as matahari rpcd unit content. </p>
<p> <code>matahari_serviced_exec_t </code> </p>
<p> &#8211; Set files with the matahari_serviced_exec_t type, if you want to transition an executable to the matahari_serviced_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/matahari-serviced, /usr/sbin/matahari-dbus-serviced, /usr/sbin/matahari-qmf-serviced </p>
</dl>
<p> <code>matahari_serviced_unit_file_t </code> </p>
<p> &#8211; Set files with the matahari_serviced_unit_file_t type, if you want to treat the files as matahari serviced unit content. </p>
<p> <code>matahari_sysconfigd_exec_t </code> </p>
<p> &#8211; Set files with the matahari_sysconfigd_exec_t type, if you want to transition an executable to the matahari_sysconfigd_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/matahari-qmf-sysconfig-consoled, /usr/sbin/matahari-dbus-sysconfigd, /usr/sbin/matahari-qmf-sysconfigd </p>
</dl>
<p> <code>matahari_sysconfigd_unit_file_t </code> </p>
<p> &#8211; Set files with the matahari_sysconfigd_unit_file_t type, if you want to treat the files as matahari sysconfigd unit content. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/systemd/system/matahari-sysconfig-console.*, /usr/lib/systemd/system/matahari-sysconfig.* </p>
</dl>
<p> <code>matahari_var_lib_t </code> </p>
<p> &#8211; Set files with the matahari_var_lib_t type, if you want to store the matahari files under the /var/lib directory. </p>
<p> <code>matahari_var_run_t </code> </p>
<p> &#8211; Set files with the matahari_var_run_t type, if you want to store the matahari files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/matahari(/.*)?, /var/run/matahari.pid, /var/run/matahari-broker.pid </p>
</dl>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux matahari policy is very flexible allowing users to setup their matahari processes in as secure a method as possible. </p>
<p> The following port types are defined for matahari: </p>
<dl>
<dt><code>matahari_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 49000 udp 49000</dl>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux matahari policy is very flexible allowing users to setup their matahari processes in as secure a method as possible. </p>
<p> The following process types are defined for matahari: </p>
<p> matahari_serviced_t, matahari_sysconfigd_t, matahari_hostd_t, matahari_netd_t, matahari_rpcd_t </code> </p>
<p> Note: <code>semanage permissive -a PROCESS_TYPE </code> can be used to make a process type permissive. Permissive process types are not denied access by SELinux. AVC messages will still be generated.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage port</code> can also be used to manipulate the port definitions </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-matahari/">matahari</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) </p>
