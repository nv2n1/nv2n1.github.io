---
title: "condor_selinux(8)"
name: "condor_selinux"
section: "8"
letter: "c"
url: "/docs/linux/man/8-condor_selinux/"
description: "condor_selinux – Security Enhanced Linux Policy for the condor processes"
---

<p>condor_selinux &#8211; Security Enhanced Linux Policy for the condor processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the condor processes via flexible mandatory access control. </p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. condor policy is extremely flexible and has several booleans that allow you to manipulate the policy and run condor with the tightest access possible. </p>
<p> If you want to allow codnor domain to connect to the network using TCP, you must turn on the condor_domain_can_network_connect boolean. </p>
<p> <code>setsebool -P condor_domain_can_network_connect 1</code></p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the condor_startd_t, condor_master_t, condor_startd_ssh_t, condor_negotiator_t, condor_collector_t, condor_schedd_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the condor_startd_t, condor_master_t, condor_startd_ssh_t, condor_negotiator_t, condor_collector_t, condor_schedd_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the condor_startd_t, condor_master_t, condor_startd_ssh_t, condor_negotiator_t, condor_collector_t, condor_schedd_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux condor policy is very flexible allowing users to setup their condor processes in as secure a method as possible. </p>
<p> The following file types are defined for condor: </p>
<p> condor_collector_exec_t </code> </p>
<p> &#8211; Set files with the condor_collector_exec_t type, if you want to transition an executable to the condor_collector_t domain. </p>
<p> <code>condor_log_t </code> </p>
<p> &#8211; Set files with the condor_log_t type, if you want to treat the data as condor log data, usually stored under the /var/log directory. </p>
<p> <code>condor_master_exec_t </code> </p>
<p> &#8211; Set files with the condor_master_exec_t type, if you want to transition an executable to the condor_master_t domain. </p>
<p> <code>condor_negotiator_exec_t </code> </p>
<p> &#8211; Set files with the condor_negotiator_exec_t type, if you want to transition an executable to the condor_negotiator_t domain. </p>
<p> <code>condor_procd_exec_t </code> </p>
<p> &#8211; Set files with the condor_procd_exec_t type, if you want to transition an executable to the condor_procd_t domain. </p>
<p> <code>condor_schedd_exec_t </code> </p>
<p> &#8211; Set files with the condor_schedd_exec_t type, if you want to transition an executable to the condor_schedd_t domain. </p>
<p> <code>condor_schedd_tmp_t </code> </p>
<p> &#8211; Set files with the condor_schedd_tmp_t type, if you want to store condor schedd temporary files in the /tmp directories. </p>
<p> <code>condor_startd_exec_t </code> </p>
<p> &#8211; Set files with the condor_startd_exec_t type, if you want to transition an executable to the condor_startd_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/sbin/condor_starter, /usr/sbin/condor_startd </p>
</dl>
<p> <code>condor_startd_tmp_t </code> </p>
<p> &#8211; Set files with the condor_startd_tmp_t type, if you want to store condor startd temporary files in the /tmp directories. </p>
<p> <code>condor_startd_tmpfs_t </code> </p>
<p> &#8211; Set files with the condor_startd_tmpfs_t type, if you want to store condor startd files on a tmpfs file system. </p>
<p> <code>condor_unit_file_t </code> </p>
<p> &#8211; Set files with the condor_unit_file_t type, if you want to treat the files as condor unit content. </p>
<p> <code>condor_var_lib_t </code> </p>
<p> &#8211; Set files with the condor_var_lib_t type, if you want to store the condor files under the /var/lib directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/condor(/.*)?, /var/lib/condor/execute(/.*)?, /var/lib/condor/spool(/.*)? </p>
</dl>
<p> <code>condor_var_lock_t </code> </p>
<p> &#8211; Set files with the condor_var_lock_t type, if you want to treat the files as condor var lock data, stored under the /var/lock directory </p>
<p> <code>condor_var_run_t </code> </p>
<p> &#8211; Set files with the condor_var_run_t type, if you want to store the condor files under the /run directory. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux condor policy is very flexible allowing users to setup their condor processes in as secure a method as possible. </p>
<p> The following port types are defined for condor: </p>
<dl>
<dt><code>condor_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 9618 udp 9618</dl>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux condor policy is very flexible allowing users to setup their condor processes in as secure a method as possible. </p>
<p> The following process types are defined for condor: </p>
<p> condor_collector_t, condor_startd_ssh_t, condor_procd_t, condor_negotiator_t, condor_schedd_t, condor_startd_t, condor_master_t </code> </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-condor/">condor</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8)</p>
