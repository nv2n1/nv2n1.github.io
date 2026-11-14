---
title: "piranha_selinux(8)"
name: "piranha_selinux"
section: "8"
letter: "p"
url: "/docs/linux/man/8-piranha_selinux/"
description: "piranha_selinux – Security Enhanced Linux Policy for the piranha processes"
---

<p>piranha_selinux &#8211; Security Enhanced Linux Policy for the piranha processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the piranha processes via flexible mandatory access control. </p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. piranha policy is extremely flexible and has several booleans that allow you to manipulate the policy and run piranha with the tightest access possible. </p>
<p> If you want to allow piranha-lvs domain to connect to the network using TCP, you must turn on the piranha_lvs_can_network_connect boolean. </p>
<p> <code>setsebool -P piranha_lvs_can_network_connect 1</code></p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the piranha_pulse_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the piranha_pulse_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the piranha_pulse_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux piranha policy is very flexible allowing users to setup their piranha processes in as secure a method as possible. </p>
<p> The following file types are defined for piranha: </p>
<p> piranha_etc_rw_t </code> </p>
<p> &#8211; Set files with the piranha_etc_rw_t type, if you want to treat the files as piranha etc read/write content. </p>
<p> <code>piranha_fos_exec_t </code> </p>
<p> &#8211; Set files with the piranha_fos_exec_t type, if you want to transition an executable to the piranha_fos_t domain. </p>
<p> <code>piranha_fos_var_run_t </code> </p>
<p> &#8211; Set files with the piranha_fos_var_run_t type, if you want to store the piranha fos files under the /run directory. </p>
<p> <code>piranha_log_t </code> </p>
<p> &#8211; Set files with the piranha_log_t type, if you want to treat the data as piranha log data, usually stored under the /var/log directory. </p>
<p> <code>piranha_lvs_exec_t </code> </p>
<p> &#8211; Set files with the piranha_lvs_exec_t type, if you want to transition an executable to the piranha_lvs_t domain. </p>
<p> <code>piranha_lvs_var_run_t </code> </p>
<p> &#8211; Set files with the piranha_lvs_var_run_t type, if you want to store the piranha lvs files under the /run directory. </p>
<p> <code>piranha_pulse_exec_t </code> </p>
<p> &#8211; Set files with the piranha_pulse_exec_t type, if you want to transition an executable to the piranha_pulse_t domain. </p>
<p> <code>piranha_pulse_initrc_exec_t </code> </p>
<p> &#8211; Set files with the piranha_pulse_initrc_exec_t type, if you want to transition an executable to the piranha_pulse_initrc_t domain. </p>
<p> <code>piranha_pulse_var_run_t </code> </p>
<p> &#8211; Set files with the piranha_pulse_var_run_t type, if you want to store the piranha pulse files under the /run directory. </p>
<p> <code>piranha_web_conf_t </code> </p>
<p> &#8211; Set files with the piranha_web_conf_t type, if you want to treat the files as piranha web configuration data, usually stored under the /etc directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/luci/etc(/.*)?, /var/lib/luci/cert(/.*)? </p>
</dl>
<p> <code>piranha_web_data_t </code> </p>
<p> &#8211; Set files with the piranha_web_data_t type, if you want to treat the files as piranha web content. </p>
<p> <code>piranha_web_exec_t </code> </p>
<p> &#8211; Set files with the piranha_web_exec_t type, if you want to transition an executable to the piranha_web_t domain. </p>
<p> <code>piranha_web_tmp_t </code> </p>
<p> &#8211; Set files with the piranha_web_tmp_t type, if you want to store piranha web temporary files in the /tmp directories. </p>
<p> <code>piranha_web_tmpfs_t </code> </p>
<p> &#8211; Set files with the piranha_web_tmpfs_t type, if you want to store piranha web files on a tmpfs file system. </p>
<p> <code>piranha_web_var_run_t </code> </p>
<p> &#8211; Set files with the piranha_web_var_run_t type, if you want to store the piranha web files under the /run directory. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux piranha policy is very flexible allowing users to setup their piranha processes in as secure a method as possible. </p>
<p> The following port types are defined for piranha: </p>
<dl>
<dt><code>piranha_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 3636</dl>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux piranha policy is very flexible allowing users to setup their piranha processes in as secure a method as possible. </p>
<p> The following process types are defined for piranha: </p>
<p> piranha_pulse_t, piranha_fos_t, piranha_lvs_t, piranha_web_t </code> </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-piranha/">piranha</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8)</p>
