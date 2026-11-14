---
title: "dcc_selinux(8)"
name: "dcc_selinux"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dcc_selinux/"
description: "dcc_selinux – Security Enhanced Linux Policy for the dcc processes"
---

<p>dcc_selinux &#8211; Security Enhanced Linux Policy for the dcc processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the dcc processes via flexible mandatory access control. </p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the dccifd_t, dccm_t, dcc_client_t, dcc_dbclean_t, dccd_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the dccifd_t, dccm_t, dcc_client_t, dcc_dbclean_t, dccd_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the dccifd_t, dccm_t, dcc_client_t, dcc_dbclean_t, dccd_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux dcc policy is very flexible allowing users to setup their dcc processes in as secure a method as possible. </p>
<p> The following file types are defined for dcc: </p>
<p> dcc_client_exec_t </code> </p>
<p> &#8211; Set files with the dcc_client_exec_t type, if you want to transition an executable to the dcc_client_t domain. </p>
<p> <code>dcc_client_map_t </code> </p>
<p> &#8211; Set files with the dcc_client_map_t type, if you want to treat the files as dcc client map data. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/dcc/map, /etc/dcc/map, /var/run/dcc/map, /var/dcc/map </p>
</dl>
<p> <code>dcc_client_tmp_t </code> </p>
<p> &#8211; Set files with the dcc_client_tmp_t type, if you want to store dcc client temporary files in the /tmp directories. </p>
<p> <code>dcc_dbclean_exec_t </code> </p>
<p> &#8211; Set files with the dcc_dbclean_exec_t type, if you want to transition an executable to the dcc_dbclean_t domain. </p>
<p> <code>dcc_dbclean_tmp_t </code> </p>
<p> &#8211; Set files with the dcc_dbclean_tmp_t type, if you want to store dcc dbclean temporary files in the /tmp directories. </p>
<p> <code>dcc_var_run_t </code> </p>
<p> &#8211; Set files with the dcc_var_run_t type, if you want to store the dcc files under the /run directory. </p>
<p> <code>dcc_var_t </code> </p>
<p> &#8211; Set files with the dcc_var_t type, if you want to store the files under the /var directory. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/dcc(/.*)?, /var/dcc(/.*)?, /var/lib/dcc(/.*)? </p>
</dl>
<p> <code>dccd_exec_t </code> </p>
<p> &#8211; Set files with the dccd_exec_t type, if you want to transition an executable to the dccd_t domain. </p>
<p> <code>dccd_tmp_t </code> </p>
<p> &#8211; Set files with the dccd_tmp_t type, if you want to store dccd temporary files in the /tmp directories. </p>
<p> <code>dccd_var_run_t </code> </p>
<p> &#8211; Set files with the dccd_var_run_t type, if you want to store the dccd files under the /run directory. </p>
<p> <code>dccifd_exec_t </code> </p>
<p> &#8211; Set files with the dccifd_exec_t type, if you want to transition an executable to the dccifd_t domain. </p>
<p> <code>dccifd_tmp_t </code> </p>
<p> &#8211; Set files with the dccifd_tmp_t type, if you want to store dccifd temporary files in the /tmp directories. </p>
<p> <code>dccifd_var_run_t </code> </p>
<p> &#8211; Set files with the dccifd_var_run_t type, if you want to store the dccifd files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/dcc/dccifd, /var/run/dcc/dccifd </p>
</dl>
<p> <code>dccm_exec_t </code> </p>
<p> &#8211; Set files with the dccm_exec_t type, if you want to transition an executable to the dccm_t domain. </p>
<p> <code>dccm_tmp_t </code> </p>
<p> &#8211; Set files with the dccm_tmp_t type, if you want to store dccm temporary files in the /tmp directories. </p>
<p> <code>dccm_var_run_t </code> </p>
<p> &#8211; Set files with the dccm_var_run_t type, if you want to store the dccm files under the /run directory. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux dcc policy is very flexible allowing users to setup their dcc processes in as secure a method as possible. </p>
<p> The following port types are defined for dcc: </p>
<dl>
<dt><code>dcc_port_t </code></p>
<dd>
<dd>Default Defined Ports: udp 6276,6277 </p>
<dt><code>dccm_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 5679 udp 5679</dl>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux dcc policy is very flexible allowing users to setup their dcc processes in as secure a method as possible. </p>
<p> The following process types are defined for dcc: </p>
<p> dccm_t, dcc_client_t, dcc_dbclean_t, dccifd_t, dccd_t </code> </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-dcc/">dcc</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) </p>
