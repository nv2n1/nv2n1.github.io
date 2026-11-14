---
title: "sysadm_selinux(8)"
name: "sysadm_selinux"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sysadm_selinux/"
description: "sysadm_u – General system administration role – Security Enhanced Linux Policy"
---

<p>sysadm_u &#8211; <code>General system administration role</code> &#8211; Security Enhanced Linux Policy </p>
<h2>Description</h2>
<p><code>sysadm_u</code> is an SELinux User defined in the SELinux policy. SELinux users have default roles, <code>sysadm_r</code>. The default role has a default type, <code>sysadm_t</code>, associated with it. The SELinux user will usually login to a system with a context that looks like: <code>sysadm_u:sysadm_r:sysadm_t:s0 &#8211; s0:c0.c1023</code> Linux users are automatically assigned an SELinux users at login. Login programs use the SELinux User to assign initial context to the user&#8217;s shell. SELinux policy uses the context to control the user&#8217;s access. By default all users are assigned to the SELinux user via the <code>__default__</code> flag On Targeted policy systems the <code>__default__</code> user is assigned to the <code>unconfined_u</code> SELinux user. You can list all Linux User to SELinux user mapping using: <code>semanage login -l</code> If you wanted to change the default user mapping to use the sysadm_u user, you would execute: <code>semanage login -m -s sysadm_u __default__</code> </p>
<h2>User Description</h2>
<p>The SELinux user sysadm_u is an admin user. It means that a mapped Linux user to this SELinux user is intended for administrative actions. Usually this is assigned to a root Linux user.</p>
<h2>Sudo</h2>
<p>The SELinux user sysadm can execute sudo. </p>
<p> You can set up sudo to allow sysadm to transition to an administrative domain: </p>
<p> Add one or more of the following record to sudoers using visudo. </p>
<p> USERNAME ALL=(ALL) ROLE=user_r TYPE=user_t COMMAND<br />
 sudo will run COMMAND as sysadm_u:user_r:user_t:LEVEL </p>
<p> You might also need to add one or more of these new roles to your SELinux user record. </p>
<p> List the SELinux roles your SELinux user can reach by executing: </p>
<p> <code>$ semanage user -l |grep selinux_name</code> </p>
<p> Modify the roles list and add sysadm_r to this list. </p>
<p> <code>$ semanage user -m -R &#8216;sysadm_r user_r staff_r secadm_r auditadm_r&#8217; sysadm_u</code> </p>
<p> For more details you can see semanage man page. </p>
<p> USERNAME ALL=(ALL) ROLE=staff_r TYPE=staff_t COMMAND<br />
 sudo will run COMMAND as sysadm_u:staff_r:staff_t:LEVEL </p>
<p> You might also need to add one or more of these new roles to your SELinux user record. </p>
<p> List the SELinux roles your SELinux user can reach by executing: </p>
<p> <code>$ semanage user -l |grep selinux_name</code> </p>
<p> Modify the roles list and add sysadm_r to this list. </p>
<p> <code>$ semanage user -m -R &#8216;sysadm_r user_r staff_r secadm_r auditadm_r&#8217; sysadm_u</code> </p>
<p> For more details you can see semanage man page. </p>
<p> USERNAME ALL=(ALL) ROLE=secadm_r TYPE=secadm_t COMMAND<br />
 sudo will run COMMAND as sysadm_u:secadm_r:secadm_t:LEVEL </p>
<p> You might also need to add one or more of these new roles to your SELinux user record. </p>
<p> List the SELinux roles your SELinux user can reach by executing: </p>
<p> <code>$ semanage user -l |grep selinux_name</code> </p>
<p> Modify the roles list and add sysadm_r to this list. </p>
<p> <code>$ semanage user -m -R &#8216;sysadm_r user_r staff_r secadm_r auditadm_r&#8217; sysadm_u</code> </p>
<p> For more details you can see semanage man page. </p>
<p> USERNAME ALL=(ALL) ROLE=auditadm_r TYPE=auditadm_t COMMAND<br />
 sudo will run COMMAND as sysadm_u:auditadm_r:auditadm_t:LEVEL </p>
<p> You might also need to add one or more of these new roles to your SELinux user record. </p>
<p> List the SELinux roles your SELinux user can reach by executing: </p>
<p> <code>$ semanage user -l |grep selinux_name</code> </p>
<p> Modify the roles list and add sysadm_r to this list. </p>
<p> <code>$ semanage user -m -R &#8216;sysadm_r user_r staff_r secadm_r auditadm_r&#8217; sysadm_u</code> </p>
<p> For more details you can see semanage man page. </p>
<p> The SELinux type sysadm_t is not allowed to execute sudo.</p>
<h2>X Windows Login</h2>
<p>The SELinux user sysadm_u is able to X Windows login.</p>
<h2>Network</h2>
<dl>
<dt>The SELinux user sysadm_u is able to listen on the following tcp ports.</p>
<dd><code>all ports with out defined types</code> </p>
<p> <code>389,636,3268,7389</code> </p>
<p> <code>32768-61000</code> </p>
<p> <code>all ports &gt; 1024</code> </p>
<dt>The SELinux user sysadm_u is able to connect to the following tcp ports.</p>
<dd><code>53</code> </p>
<p> <code>all ports</code> </p>
<p> <code>8955</code> </p>
<p> <code>5432,9898</code> </p>
<p> <code>88,750,4444</code> </p>
<p> <code>all ports with out defined types</code> </p>
<p> <code>9080</code> </p>
<p> <code>389,636,3268,7389</code> </p>
<p> <code>111</code> </p>
<p> <code>32768-61000</code> </p>
<p> <code>all ports &lt; 1024</code> </p>
<dt>The SELinux user sysadm_u is able to listen on the following udp ports.</p>
<dd><code>all ports with out defined types</code> </p>
<p> <code>32768-61000</code> </p>
<p> <code>123</code> </p>
<p> <code>all ports &gt; 1024</code> </p>
<dt>The SELinux user sysadm_u is able to connect to the following tcp ports.</p>
<dd><code>53</code> </p>
<p> <code>all ports</code> </p>
<p> <code>8955</code> </p>
<p> <code>5432,9898</code> </p>
<p> <code>88,750,4444</code> </p>
<p> <code>all ports with out defined types</code> </p>
<p> <code>9080</code> </p>
<p> <code>389,636,3268,7389</code> </p>
<p> <code>111</code> </p>
<p> <code>32768-61000</code> </p>
<p> <code>all ports &lt; 1024</code> </p>
</dl>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. sysadm policy is extremely flexible and has several booleans that allow you to manipulate the policy and run sysadm with the tightest access possible. </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
<p> If you want to determine whether crond can execute jobs in the user domain as opposed to the the generic cronjob domain, you must turn on the cron_userdomain_transition boolean. Enabled by default. </p>
<p> <code>setsebool -P cron_userdomain_transition 1</code> </p>
<p> If you want to deny user domains applications to map a memory region as both executable and writable, this is dangerous and the executable should be reported in bugzilla, you must turn on the deny_execmem boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_execmem 1</code> </p>
<p> If you want to deny any process from ptracing or debugging any other processes, you must turn on the deny_ptrace boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_ptrace 1</code> </p>
<p> If you want to allow all domains to use other domains file descriptors, you must turn on the domain_fd_use boolean. Enabled by default. </p>
<p> <code>setsebool -P domain_fd_use 1</code> </p>
<p> If you want to allow all domains to have the kernel load modules, you must turn on the domain_kernel_load_modules boolean. Disabled by default. </p>
<p> <code>setsebool -P domain_kernel_load_modules 1</code> </p>
<p> If you want to allow all domains to execute in fips_mode, you must turn on the fips_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P fips_mode 1</code> </p>
<p> If you want to determine whether calling user domains can execute Git daemon in the git_session_t domain, you must turn on the git_session_users boolean. Enabled by default. </p>
<p> <code>setsebool -P git_session_users 1</code> </p>
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code> </p>
<p> If you want to allow confined applications to run with kerberos, you must turn on the kerberos_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P kerberos_enabled 1</code> </p>
<p> If you want to allow logging in and using the system from /dev/console, you must turn on the login_console_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P login_console_enabled 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to determine whether calling user domains can execute Polipo daemon in the polipo_session_t domain, you must turn on the polipo_session_users boolean. Enabled by default. </p>
<p> <code>setsebool -P polipo_session_users 1</code> </p>
<p> If you want to allow database admins to execute DML statement, you must turn on the postgresql_selinux_unconfined_dbadm boolean. Enabled by default. </p>
<p> <code>setsebool -P postgresql_selinux_unconfined_dbadm 1</code> </p>
<p> If you want to disallow programs, such as newrole, from transitioning to administrative user domains, you must turn on the secure_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode 1</code> </p>
<p> If you want to boolean to determine whether the system permits loading policy, setting enforcing mode, and changing boolean values. Set this to true and you have to reboot to set it back, you must turn on the secure_mode_policyload boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode_policyload 1</code> </p>
<p> If you want to allow regular users direct dri device access, you must turn on the selinuxuser_direct_dri_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_direct_dri_enabled 1</code> </p>
<p> If you want to allow unconfined executables to make their stack executable. This should never, ever be necessary. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla, you must turn on the selinuxuser_execstack boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_execstack 1</code> </p>
<p> If you want to allow users to connect to the local mysql server, you must turn on the selinuxuser_mysql_connect_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P selinuxuser_mysql_connect_enabled 1</code> </p>
<p> If you want to allow users to connect to PostgreSQL, you must turn on the selinuxuser_postgresql_connect_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P selinuxuser_postgresql_connect_enabled 1</code> </p>
<p> If you want to allow user to r/w files on filesystems that do not have extended attributes (FAT, CDROM, FLOPPY), you must turn on the selinuxuser_rw_noexattrfile boolean. Disabled by default. </p>
<p> <code>setsebool -P selinuxuser_rw_noexattrfile 1</code> </p>
<p> If you want to allow users to run TCP servers (bind to ports and accept connection from the same domain and outside users) disabling this forces FTP passive mode and may change other protocols, you must turn on the selinuxuser_tcp_server boolean. Disabled by default. </p>
<p> <code>setsebool -P selinuxuser_tcp_server 1</code> </p>
<p> If you want to allow users to run UDP servers (bind to ports and accept connection from the same domain and outside users) disabling this may break avahi discovering services on the network and other udp related services, you must turn on the selinuxuser_udp_server boolean. Disabled by default. </p>
<p> <code>setsebool -P selinuxuser_udp_server 1</code> </p>
<p> If you want to allow user to use ssh chroot environment, you must turn on the selinuxuser_use_ssh_chroot boolean. Disabled by default. </p>
<p> <code>setsebool -P selinuxuser_use_ssh_chroot 1</code> </p>
<p> If you want to allow ssh logins as sysadm_r:sysadm_t, you must turn on the ssh_sysadm_login boolean. Disabled by default. </p>
<p> <code>setsebool -P ssh_sysadm_login 1</code> </p>
<p> If you want to support NFS home directories, you must turn on the use_nfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_nfs_home_dirs 1</code> </p>
<p> If you want to support SAMBA home directories, you must turn on the use_samba_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_samba_home_dirs 1</code> </p>
<p> If you want to allow the graphical login program to login directly as sysadm_r:sysadm_t, you must turn on the xdm_sysadm_login boolean. Disabled by default. </p>
<p> <code>setsebool -P xdm_sysadm_login 1</code> </p>
<p> If you want to allows clients to write to the X server shared memory segments, you must turn on the xserver_clients_write_xshm boolean. Disabled by default. </p>
<p> <code>setsebool -P xserver_clients_write_xshm 1</code> </p>
<p> If you want to support X userspace object manager, you must turn on the xserver_object_manager boolean. Enabled by default. </p>
<p> <code>setsebool -P xserver_object_manager 1</code></p>
<h2>Home_Exec</h2>
<p>The SELinux user sysadm_u is able execute home content files.</p>
<h2>Transitions</h2>
<p>Three things can happen when sysadm_t attempts to execute a program. </p>
<p> <code>1.</code> SELinux Policy can deny sysadm_t from executing the program. </p>
<dl>
<dd><code>2.</code> SELinux Policy can allow sysadm_t to execute the program in the current user type. </p>
<p> Execute the following to see the types that the SELinux user sysadm_t can execute without transitioning: </p>
<p> <code>sesearch -A -s sysadm_t -c file -p execute_no_trans</code> </p>
<dd><code>3.</code> SELinux can allow sysadm_t to execute the program and transition to a new type. </p>
<p> Execute the following to see the types that the SELinux user sysadm_t can execute and transition: </p>
<p> <code>$ sesearch -A -s sysadm_t -c process -p transition</code> </p>
</dl>
<h2>Managed Files</h2>
<p>The SELinux process type sysadm_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>auditd_etc_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/audit(/.*)?</p>
<p> <code>auditd_log_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/audit(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/audit.log.*</p>
<p> <code>boolean_type</code> </p>
<p> <code>cifs_t</code> </p>
<p> <code>default_context_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux/([^/]*/)?contexts(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.default_contexts</p>
<p> <code>file_context_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux/([^/]*/)?contexts/files(/.*)?</p>
<p> <code>git_user_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/public_git(/.*)?</p>
<p> <code>iceauth_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.DCOP.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.ICEauthority.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.DCOP.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.ICEauthority.*</p>
<p> <code>irc_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.irssi(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/irclog(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.ircmotd</p>
<p> <code>krb5_host_rcache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/krb5rcache(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/nfs_0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/DNS_25</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/host_0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/imap_0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/HTTP_23</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/HTTP_48</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/ldap_55</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/ldap_487</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/ldapmap1_0</p>
<p> <code>krb5_keytab_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/krb5.keytab</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/krb5kdc/kadm5.keytab</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/kerberos/krb5kdc/kadm5.keytab</p>
<p> <code>non_security_file_type</code> </p>
<p> <code>noxattrfs</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all files on file systems which do not support extended attributes</p>
<p> <code>postfix_spool_type</code> </p>
<p> <code>screen_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.screen(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.screen(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.screenrc</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.tmux.conf</p>
<p> <code>selinux_config_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux/([^/]*/)?seusers</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux/([^/]*/)?users(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux/([^/]*/)?setrans.conf</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/sepolgen(/.*)?</p>
<p> <code>selinux_login_config_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux/([^/]*/)?logins(/.*)?</p>
<p> <code>semanage_store_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux/([^/]*/)?policy(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux/(minimum|mls|targeted)/active(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/selinux/([^/]*/)?modules/(active|tmp|previous)(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/selinux(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/share/selinux/mls(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/share/selinux/targeted(/.*)?</p>
<p> <code>sysctl_type</code> </p>
<p> <code>systemd_passwd_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/ask-password(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/systemd/ask-password-block(/.*)?</p>
<p> <code>systemd_unit_file_type</code> </p>
<p> <code>usbfs_t</code> </p>
<p> <code>user_fonts_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts.cache-.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts.cache-.*</p>
<p> <code>user_fonts_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/.font-unix(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.local/share/fonts(/.*)?</p>
<p> <code>user_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.+</p>
<p> <code>user_home_type</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all user home files</p>
<p> <code>user_tmp_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/shm/mono.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/.X11-unix(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/.ICE-unix(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/shm/pulse-shm.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/.X0-lock</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/hsperfdata_root</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/hsperfdata_root</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/tmp</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.tmp</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/gconfd-[^/]+</p>
<p> <code>user_tmp_type</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all user tmp files</p>
<p> <code>vmware_conf_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.vmware[^/]*/.*.cfg</p>
<p> <code>vmware_tmp_t</code> </p>
<p> <code>vmware_tmpfs_t</code> </p>
<p> <code>xauth_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.xauth.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.Xauth.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.serverauth.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.Xauthority.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/pqsql/.xauth.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/pqsql/.Xauthority.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/nxserver/home/.xauth.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/nxserver/home/.Xauthority.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.xauth.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.Xauth.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.serverauth.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.Xauthority.*</p>
<p> <code>xserver_tmpfs_t</code></p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-sysadm/">sysadm</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-sysadm_dbusd_selinux/">sysadm_dbusd_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_dbusd_selinux/">sysadm_dbusd_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_passwd_selinux/">sysadm_passwd_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_passwd_selinux/">sysadm_passwd_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_screen_selinux/">sysadm_screen_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_screen_selinux/">sysadm_screen_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_seunshare_selinux/">sysadm_seunshare_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_seunshare_selinux/">sysadm_seunshare_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_ssh_agent_selinux/">sysadm_ssh_agent_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_ssh_agent_selinux/">sysadm_ssh_agent_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_su_selinux/">sysadm_su_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_su_selinux/">sysadm_su_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_sudo_selinux/">sysadm_sudo_selinux</a>(8), <a href="/docs/linux/man/8-sysadm_sudo_selinux/">sysadm_sudo_selinux</a>(8) </p>
