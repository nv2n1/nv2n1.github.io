---
title: "telepathy_selinux(8)"
name: "telepathy_selinux"
section: "8"
letter: "t"
url: "/docs/linux/man/8-telepathy_selinux/"
description: "telepathy_selinux – Security Enhanced Linux Policy for the telepathy processes"
---

<p>telepathy_selinux &#8211; Security Enhanced Linux Policy for the telepathy processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the telepathy processes via flexible mandatory access control. </p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. telepathy policy is extremely flexible and has several booleans that allow you to manipulate the policy and run telepathy with the tightest access possible. </p>
<p> If you want to allow the Telepathy connection managers to connect to any generic TCP port, you must turn on the telepathy_tcp_connect_generic_network_ports boolean. </p>
<p> <code>setsebool -P telepathy_tcp_connect_generic_network_ports 1</code> </p>
<p> If you want to allow the Telepathy connection managers to connect to any network port, you must turn on the telepathy_connect_all_ports boolean. </p>
<p> <code>setsebool -P telepathy_connect_all_ports 1</code></p>
<h2>Nsswitch Domain</h2>
<p>If you want to allow users to login using a sssd serve for the telepathy_mission_control_t, telepathy_logger_t, telepathy_salut_t, telepathy_gabble_t, telepathy_idle_t, telepathy_sunshine_t, telepathy_stream_engine_t, telepathy_sofiasip_t, telepathy_msn_t, you must turn on the authlogin_nsswitch_use_ldap boolean. </p>
<p> setsebool -P authlogin_nsswitch_use_ldap 1 </p>
<p> If you want to allow confined applications to run with kerberos for the telepathy_mission_control_t, telepathy_logger_t, telepathy_salut_t, telepathy_gabble_t, telepathy_idle_t, telepathy_sunshine_t, telepathy_stream_engine_t, telepathy_sofiasip_t, telepathy_msn_t, you must turn on the allow_kerberos boolean. </p>
<p> setsebool -P allow_kerberos 1 </p>
<p> If you want to allow system to run with NI for the telepathy_mission_control_t, telepathy_logger_t, telepathy_salut_t, telepathy_gabble_t, telepathy_idle_t, telepathy_sunshine_t, telepathy_stream_engine_t, telepathy_sofiasip_t, telepathy_msn_t, you must turn on the allow_ypbind boolean. </p>
<p> setsebool -P allow_ypbind 1</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux telepathy policy is very flexible allowing users to setup their telepathy processes in as secure a method as possible. </p>
<p> The following file types are defined for telepathy: </p>
<p> telepathy_cache_home_t </code> </p>
<p> &#8211; Set files with the telepathy_cache_home_t type, if you want to store telepathy cache files in the users home directory. </p>
<p> <code>telepathy_data_home_t </code> </p>
<p> &#8211; Set files with the telepathy_data_home_t type, if you want to store telepathy data files in the users home directory. </p>
<p> <code>telepathy_gabble_cache_home_t </code> </p>
<p> &#8211; Set files with the telepathy_gabble_cache_home_t type, if you want to store telepathy gabble cache files in the users home directory. </p>
<p> <code>telepathy_gabble_exec_t </code> </p>
<p> &#8211; Set files with the telepathy_gabble_exec_t type, if you want to transition an executable to the telepathy_gabble_t domain. </p>
<p> <code>telepathy_gabble_tmp_t </code> </p>
<p> &#8211; Set files with the telepathy_gabble_tmp_t type, if you want to store telepathy gabble temporary files in the /tmp directories. </p>
<p> <code>telepathy_idle_exec_t </code> </p>
<p> &#8211; Set files with the telepathy_idle_exec_t type, if you want to transition an executable to the telepathy_idle_t domain. </p>
<p> <code>telepathy_idle_tmp_t </code> </p>
<p> &#8211; Set files with the telepathy_idle_tmp_t type, if you want to store telepathy idle temporary files in the /tmp directories. </p>
<p> <code>telepathy_logger_cache_home_t </code> </p>
<p> &#8211; Set files with the telepathy_logger_cache_home_t type, if you want to store telepathy logger cache files in the users home directory. </p>
<p> <code>telepathy_logger_data_home_t </code> </p>
<p> &#8211; Set files with the telepathy_logger_data_home_t type, if you want to store telepathy logger data files in the users home directory. </p>
<p> <code>telepathy_logger_exec_t </code> </p>
<p> &#8211; Set files with the telepathy_logger_exec_t type, if you want to transition an executable to the telepathy_logger_t domain. </p>
<p> <code>telepathy_logger_tmp_t </code> </p>
<p> &#8211; Set files with the telepathy_logger_tmp_t type, if you want to store telepathy logger temporary files in the /tmp directories. </p>
<p> <code>telepathy_mission_control_cache_home_t </code> </p>
<p> &#8211; Set files with the telepathy_mission_control_cache_home_t type, if you want to store telepathy mission control cache files in the users home directory. </p>
<p> <code>telepathy_mission_control_data_home_t </code> </p>
<p> &#8211; Set files with the telepathy_mission_control_data_home_t type, if you want to store telepathy mission control data files in the users home directory. </p>
<p> <code>telepathy_mission_control_exec_t </code> </p>
<p> &#8211; Set files with the telepathy_mission_control_exec_t type, if you want to transition an executable to the telepathy_mission_control_t domain. </p>
<p> <code>telepathy_mission_control_home_t </code> </p>
<p> &#8211; Set files with the telepathy_mission_control_home_t type, if you want to store telepathy mission control files in the users home directory. </p>
<p> <code>telepathy_mission_control_tmp_t </code> </p>
<p> &#8211; Set files with the telepathy_mission_control_tmp_t type, if you want to store telepathy mission control temporary files in the /tmp directories. </p>
<p> <code>telepathy_msn_exec_t </code> </p>
<p> &#8211; Set files with the telepathy_msn_exec_t type, if you want to transition an executable to the telepathy_msn_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/libexec/telepathy-butterfly, /usr/libexec/telepathy-haze </p>
</dl>
<p> <code>telepathy_msn_tmp_t </code> </p>
<p> &#8211; Set files with the telepathy_msn_tmp_t type, if you want to store telepathy msn temporary files in the /tmp directories. </p>
<p> <code>telepathy_salut_exec_t </code> </p>
<p> &#8211; Set files with the telepathy_salut_exec_t type, if you want to transition an executable to the telepathy_salut_t domain. </p>
<p> <code>telepathy_salut_tmp_t </code> </p>
<p> &#8211; Set files with the telepathy_salut_tmp_t type, if you want to store telepathy salut temporary files in the /tmp directories. </p>
<p> <code>telepathy_sofiasip_exec_t </code> </p>
<p> &#8211; Set files with the telepathy_sofiasip_exec_t type, if you want to transition an executable to the telepathy_sofiasip_t domain. </p>
<p> <code>telepathy_sofiasip_tmp_t </code> </p>
<p> &#8211; Set files with the telepathy_sofiasip_tmp_t type, if you want to store telepathy sofiasip temporary files in the /tmp directories. </p>
<p> <code>telepathy_stream_engine_exec_t </code> </p>
<p> &#8211; Set files with the telepathy_stream_engine_exec_t type, if you want to transition an executable to the telepathy_stream_engine_t domain. </p>
<p> <code>telepathy_stream_engine_tmp_t </code> </p>
<p> &#8211; Set files with the telepathy_stream_engine_tmp_t type, if you want to store telepathy stream engine temporary files in the /tmp directories. </p>
<p> <code>telepathy_sunshine_exec_t </code> </p>
<p> &#8211; Set files with the telepathy_sunshine_exec_t type, if you want to transition an executable to the telepathy_sunshine_t domain. </p>
<p> <code>telepathy_sunshine_home_t </code> </p>
<p> &#8211; Set files with the telepathy_sunshine_home_t type, if you want to store telepathy sunshine files in the users home directory. </p>
<p> <code>telepathy_sunshine_tmp_t </code> </p>
<p> &#8211; Set files with the telepathy_sunshine_tmp_t type, if you want to store telepathy sunshine temporary files in the /tmp directories. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanantly change the file context you need to use the <code>semanage fcontext </code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux telepathy policy is very flexible allowing users to setup their telepathy processes in as secure a method as possible. </p>
<p> The following process types are defined for telepathy: </p>
<p> telepathy_gabble_t, telepathy_sofiasip_t, telepathy_idle_t, telepathy_mission_control_t, telepathy_salut_t, telepathy_sunshine_t, telepathy_logger_t, telepathy_stream_engine_t, telepathy_msn_t </code> </p>
<p> Note: <code>semanage permissive -a PROCESS_TYPE </code> can be used to make a process type permissive. Permissive process types are not denied access by SELinux. AVC messages will still be generated.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-telepathy/">telepathy</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8)</p>
