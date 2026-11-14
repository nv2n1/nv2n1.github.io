---
title: "pki_selinux(8)"
name: "pki_selinux"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pki_selinux/"
description: "pki_selinux – Security Enhanced Linux Policy for the pki processes"
---

<p>pki_selinux &#8211; Security Enhanced Linux Policy for the pki processes</p>
<h2>Description</h2>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux pki policy is very flexible allowing users to setup their pki processes in as secure a method as possible. </p>
<p> The following file types are defined for pki: </p>
<p> pki_ca_etc_rw_t </code> </p>
<p> &#8211; Set files with the pki_ca_etc_rw_t type, if you want to treat the files as pki ca etc read/write content. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/pki-ca(/.*)?, /etc/sysconfig/pki/ca(/.*)? </p>
</dl>
<p> <code>pki_ca_exec_t </code> </p>
<p> &#8211; Set files with the pki_ca_exec_t type, if you want to transition an executable to the pki_ca_t domain. </p>
<p> <code>pki_ca_log_t </code> </p>
<p> &#8211; Set files with the pki_ca_log_t type, if you want to treat the data as pki ca log data, usually stored under the /var/log directory. </p>
<p> <code>pki_ca_tomcat_exec_t </code> </p>
<p> &#8211; Set files with the pki_ca_tomcat_exec_t type, if you want to transition an executable to the pki_ca_tomcat_t domain. </p>
<p> <code>pki_ca_var_lib_t </code> </p>
<p> &#8211; Set files with the pki_ca_var_lib_t type, if you want to store the pki ca files under the /var/lib directory. </p>
<p> <code>pki_ca_var_run_t </code> </p>
<p> &#8211; Set files with the pki_ca_var_run_t type, if you want to store the pki ca files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/pki-ca.pid, /var/run/pki/ca(/.*)? </p>
</dl>
<p> <code>pki_common_dev_t </code> </p>
<p> &#8211; Set files with the pki_common_dev_t type, if you want to treat the files as pki common dev data. </p>
<p> <code>pki_common_t </code> </p>
<p> &#8211; Set files with the pki_common_t type, if you want to treat the files as pki common data. </p>
<p> <code>pki_kra_etc_rw_t </code> </p>
<p> &#8211; Set files with the pki_kra_etc_rw_t type, if you want to treat the files as pki kra etc read/write content. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/pki-kra(/.*)?, /etc/sysconfig/pki/kra(/.*)? </p>
</dl>
<p> <code>pki_kra_exec_t </code> </p>
<p> &#8211; Set files with the pki_kra_exec_t type, if you want to transition an executable to the pki_kra_t domain. </p>
<p> <code>pki_kra_log_t </code> </p>
<p> &#8211; Set files with the pki_kra_log_t type, if you want to treat the data as pki kra log data, usually stored under the /var/log directory. </p>
<p> <code>pki_kra_tomcat_exec_t </code> </p>
<p> &#8211; Set files with the pki_kra_tomcat_exec_t type, if you want to transition an executable to the pki_kra_tomcat_t domain. </p>
<p> <code>pki_kra_var_lib_t </code> </p>
<p> &#8211; Set files with the pki_kra_var_lib_t type, if you want to store the pki kra files under the /var/lib directory. </p>
<p> <code>pki_kra_var_run_t </code> </p>
<p> &#8211; Set files with the pki_kra_var_run_t type, if you want to store the pki kra files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/pki-kra.pid, /var/run/pki/kra(/.*)? </p>
</dl>
<p> <code>pki_ocsp_etc_rw_t </code> </p>
<p> &#8211; Set files with the pki_ocsp_etc_rw_t type, if you want to treat the files as pki ocsp etc read/write content. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/pki-ocsp(/.*)?, /etc/sysconfig/pki/ocsp(/.*)? </p>
</dl>
<p> <code>pki_ocsp_exec_t </code> </p>
<p> &#8211; Set files with the pki_ocsp_exec_t type, if you want to transition an executable to the pki_ocsp_t domain. </p>
<p> <code>pki_ocsp_log_t </code> </p>
<p> &#8211; Set files with the pki_ocsp_log_t type, if you want to treat the data as pki ocsp log data, usually stored under the /var/log directory. </p>
<p> <code>pki_ocsp_tomcat_exec_t </code> </p>
<p> &#8211; Set files with the pki_ocsp_tomcat_exec_t type, if you want to transition an executable to the pki_ocsp_tomcat_t domain. </p>
<p> <code>pki_ocsp_var_lib_t </code> </p>
<p> &#8211; Set files with the pki_ocsp_var_lib_t type, if you want to store the pki ocsp files under the /var/lib directory. </p>
<p> <code>pki_ocsp_var_run_t </code> </p>
<p> &#8211; Set files with the pki_ocsp_var_run_t type, if you want to store the pki ocsp files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/pki-ocsp.pid, /var/run/pki/ocsp(/.*)? </p>
</dl>
<p> <code>pki_ra_etc_rw_t </code> </p>
<p> &#8211; Set files with the pki_ra_etc_rw_t type, if you want to treat the files as pki ra etc read/write content. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/sysconfig/pki/ra(/.*)?, /etc/pki-ra(/.*)? </p>
</dl>
<p> <code>pki_ra_exec_t </code> </p>
<p> &#8211; Set files with the pki_ra_exec_t type, if you want to transition an executable to the pki_ra_t domain. </p>
<p> <code>pki_ra_log_t </code> </p>
<p> &#8211; Set files with the pki_ra_log_t type, if you want to treat the data as pki ra log data, usually stored under the /var/log directory. </p>
<p> <code>pki_ra_script_exec_t </code> </p>
<p> &#8211; Set files with the pki_ra_script_exec_t type, if you want to transition an executable to the pki_ra_script_t domain. </p>
<p> <code>pki_ra_tomcat_exec_t </code> </p>
<p> &#8211; Set files with the pki_ra_tomcat_exec_t type, if you want to transition an executable to the pki_ra_tomcat_t domain. </p>
<p> <code>pki_ra_var_lib_t </code> </p>
<p> &#8211; Set files with the pki_ra_var_lib_t type, if you want to store the pki ra files under the /var/lib directory. </p>
<p> <code>pki_ra_var_run_t </code> </p>
<p> &#8211; Set files with the pki_ra_var_run_t type, if you want to store the pki ra files under the /run directory. </p>
<p> <code>pki_tks_etc_rw_t </code> </p>
<p> &#8211; Set files with the pki_tks_etc_rw_t type, if you want to treat the files as pki tks etc read/write content. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/sysconfig/pki/tks(/.*)?, /etc/pki-tks(/.*)? </p>
</dl>
<p> <code>pki_tks_exec_t </code> </p>
<p> &#8211; Set files with the pki_tks_exec_t type, if you want to transition an executable to the pki_tks_t domain. </p>
<p> <code>pki_tks_log_t </code> </p>
<p> &#8211; Set files with the pki_tks_log_t type, if you want to treat the data as pki tks log data, usually stored under the /var/log directory. </p>
<p> <code>pki_tks_tomcat_exec_t </code> </p>
<p> &#8211; Set files with the pki_tks_tomcat_exec_t type, if you want to transition an executable to the pki_tks_tomcat_t domain. </p>
<p> <code>pki_tks_var_lib_t </code> </p>
<p> &#8211; Set files with the pki_tks_var_lib_t type, if you want to store the pki tks files under the /var/lib directory. </p>
<p> <code>pki_tks_var_run_t </code> </p>
<p> &#8211; Set files with the pki_tks_var_run_t type, if you want to store the pki tks files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/pki-tks.pid, /var/run/pki/tks(/.*)? </p>
</dl>
<p> <code>pki_tps_etc_rw_t </code> </p>
<p> &#8211; Set files with the pki_tps_etc_rw_t type, if you want to treat the files as pki tps etc read/write content. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/sysconfig/pki/tps(/.*)?, /etc/pki-tps(/.*)? </p>
</dl>
<p> <code>pki_tps_exec_t </code> </p>
<p> &#8211; Set files with the pki_tps_exec_t type, if you want to transition an executable to the pki_tps_t domain. </p>
<p> <code>pki_tps_log_t </code> </p>
<p> &#8211; Set files with the pki_tps_log_t type, if you want to treat the data as pki tps log data, usually stored under the /var/log directory. </p>
<p> <code>pki_tps_script_exec_t </code> </p>
<p> &#8211; Set files with the pki_tps_script_exec_t type, if you want to transition an executable to the pki_tps_script_t domain. </p>
<p> <code>pki_tps_tomcat_exec_t </code> </p>
<p> &#8211; Set files with the pki_tps_tomcat_exec_t type, if you want to transition an executable to the pki_tps_tomcat_t domain. </p>
<p> <code>pki_tps_var_lib_t </code> </p>
<p> &#8211; Set files with the pki_tps_var_lib_t type, if you want to store the pki tps files under the /var/lib directory. </p>
<p> <code>pki_tps_var_run_t </code> </p>
<p> &#8211; Set files with the pki_tps_var_run_t type, if you want to store the pki tps files under the /run directory. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Port Types</h2>
<p>SELinux defines port types to represent TCP and UDP ports. </p>
<p> You can see the types associated with a port by using the following command: </p>
<p> <code>semanage port -l</code> </p>
<p> Policy governs the access confined processes have to these ports. SELinux pki policy is very flexible allowing users to setup their pki processes in as secure a method as possible. </p>
<p> The following port types are defined for pki: </p>
<dl>
<dt><code>pki_ca_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 8021 </p>
<dt><code>pki_kra_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 8021 </p>
<dt><code>pki_ocsp_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 8021 </p>
<dt><code>pki_ra_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 8021 </p>
<dt><code>pki_tks_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 8021 </p>
<dt><code>pki_tps_port_t </code></p>
<dd>
<dd>Default Defined Ports: tcp 8021</dl>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux pki policy is very flexible allowing users to setup their pki processes in as secure a method as possible. </p>
<p> The following process types are defined for pki: </p>
<p> pki_ca_t, pki_ra_t, pki_ca_script_t, pki_ocsp_t, pki_kra_t, pki_tks_t, pki_tps_t, pki_ocsp_script_t, pki_kra_script_t, pki_tks_script_t </code> </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-pki/">pki</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) </p>
