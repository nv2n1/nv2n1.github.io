---
title: "xguest_selinux(8)"
name: "xguest_selinux"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xguest_selinux/"
description: "xguest_u – Least privledge xwindows user role. – Security Enhanced Linux Policy"
---

<p>xguest_u &#8211; <code>Least privledge xwindows user role.</code> &#8211; Security Enhanced Linux Policy </p>
<h2>Description</h2>
<p><code>xguest_u</code> is an SELinux User defined in the SELinux policy. SELinux users have default roles, <code>xguest_r</code>. The default role has a default type, <code>xguest_t</code>, associated with it. The SELinux user will usually login to a system with a context that looks like: <code>xguest_u:xguest_r:xguest_t:s0</code> Linux users are automatically assigned an SELinux users at login. Login programs use the SELinux User to assign initial context to the user&#8217;s shell. SELinux policy uses the context to control the user&#8217;s access. By default all users are assigned to the SELinux user via the <code>__default__</code> flag On Targeted policy systems the <code>__default__</code> user is assigned to the <code>unconfined_u</code> SELinux user. You can list all Linux User to SELinux user mapping using: <code>semanage login -l</code> If you wanted to change the default user mapping to use the xguest_u user, you would execute: <code>semanage login -m -s xguest_u __default__</code> </p>
<h2>User Description</h2>
<p>The SELinux user xguest_u is defined in policy as a unprivileged user. SELinux prevents unprivileged users from doing administration tasks without transitioning to a different role.</p>
<h2>Sudo</h2>
<h2>X Windows Login</h2>
<p>The SELinux user xguest_u is able to X Windows login.</p>
<h2>Network</h2>
<dl>
<dt>The SELinux user xguest_u is able to listen on the following tcp ports.</p>
<dd><code>all ports with out defined types</code> </p>
<p> <code>32768-61000</code> </p>
<dt>The SELinux user xguest_u is able to connect to the following tcp ports.</p>
<dd><code>53</code> </p>
<p> <code>8955</code> </p>
<p> <code>843,1935</code> </p>
<p> <code>80,81,443,488,8008,8009,8443,9000</code> </p>
<p> <code>631,8610-8614</code> </p>
<p> <code>88,750,4444</code> </p>
<p> <code>21,989,990</code> </p>
<p> <code>8000,9433,16001</code> </p>
<p> <code>32768-61000</code> </p>
<p> <code>all ports with out defined types</code> </p>
<p> <code>9080</code> </p>
<p> <code>3128,3401,4827</code> </p>
<p> <code>8036</code> </p>
<p> <code>4713</code> </p>
<p> <code>4331,5001</code> </p>
<p> <code>8080,8118,8123,10001-10010</code> </p>
<p> <code>389,636,3268,7389</code> </p>
<p> <code>111</code> </p>
<p> <code>8081</code> </p>
<p> <code>all ports &lt; 1024</code> </p>
<dt>The SELinux user xguest_u is able to listen on the following udp ports.</p>
<dd><code>all ports with out defined types</code> </p>
<p> <code>32768-61000</code> </p>
<dt>The SELinux user xguest_u is able to connect to the following tcp ports.</p>
<dd><code>53</code> </p>
<p> <code>8955</code> </p>
<p> <code>843,1935</code> </p>
<p> <code>80,81,443,488,8008,8009,8443,9000</code> </p>
<p> <code>631,8610-8614</code> </p>
<p> <code>88,750,4444</code> </p>
<p> <code>21,989,990</code> </p>
<p> <code>8000,9433,16001</code> </p>
<p> <code>32768-61000</code> </p>
<p> <code>all ports with out defined types</code> </p>
<p> <code>9080</code> </p>
<p> <code>3128,3401,4827</code> </p>
<p> <code>8036</code> </p>
<p> <code>4713</code> </p>
<p> <code>4331,5001</code> </p>
<p> <code>8080,8118,8123,10001-10010</code> </p>
<p> <code>389,636,3268,7389</code> </p>
<p> <code>111</code> </p>
<p> <code>8081</code> </p>
<p> <code>all ports &lt; 1024</code> </p>
</dl>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. xguest policy is extremely flexible and has several booleans that allow you to manipulate the policy and run xguest with the tightest access possible. </p>
<p> If you want to allow xguest users to configure Network Manager and connect to apache ports, you must turn on the xguest_connect_network boolean. Enabled by default. </p>
<p> <code>setsebool -P xguest_connect_network 1</code> </p>
<p> If you want to allow xguest users to mount removable media, you must turn on the xguest_mount_media boolean. Enabled by default. </p>
<p> <code>setsebool -P xguest_mount_media 1</code> </p>
<p> If you want to allow xguest to use blue tooth devices, you must turn on the xguest_use_bluetooth boolean. Enabled by default. </p>
<p> <code>setsebool -P xguest_use_bluetooth 1</code> </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
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
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code> </p>
<p> If you want to allow httpd cgi support, you must turn on the httpd_enable_cgi boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_enable_cgi 1</code> </p>
<p> If you want to unify HTTPD handling of all content files, you must turn on the httpd_unified boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_unified 1</code> </p>
<p> If you want to allow confined applications to run with kerberos, you must turn on the kerberos_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P kerberos_enabled 1</code> </p>
<p> If you want to allow logging in and using the system from /dev/console, you must turn on the login_console_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P login_console_enabled 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to disallow programs, such as newrole, from transitioning to administrative user domains, you must turn on the secure_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode 1</code> </p>
<p> If you want to allow regular users direct dri device access, you must turn on the selinuxuser_direct_dri_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_direct_dri_enabled 1</code> </p>
<p> If you want to allow unconfined executables to make their stack executable. This should never, ever be necessary. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla, you must turn on the selinuxuser_execstack boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_execstack 1</code> </p>
<p> If you want to allow user to r/w files on filesystems that do not have extended attributes (FAT, CDROM, FLOPPY), you must turn on the selinuxuser_rw_noexattrfile boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_rw_noexattrfile 1</code> </p>
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
<p>The SELinux user xguest_u is able execute home content files.</p>
<h2>Transitions</h2>
<p>Three things can happen when xguest_t attempts to execute a program. </p>
<p> <code>1.</code> SELinux Policy can deny xguest_t from executing the program. </p>
<dl>
<dd><code>2.</code> SELinux Policy can allow xguest_t to execute the program in the current user type. </p>
<p> Execute the following to see the types that the SELinux user xguest_t can execute without transitioning: </p>
<p> <code>sesearch -A -s xguest_t -c file -p execute_no_trans</code> </p>
<dd><code>3.</code> SELinux can allow xguest_t to execute the program and transition to a new type. </p>
<p> Execute the following to see the types that the SELinux user xguest_t can execute and transition: </p>
<p> <code>$ sesearch -A -s xguest_t -c process -p transition</code> </p>
</dl>
<h2>Managed Files</h2>
<p>The SELinux process type xguest_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>anon_inodefs_t</code> </p>
<p> <code>auth_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/coolkey(/.*)?</p>
<p> <code>chrome_sandbox_tmpfs_t</code> </p>
<p> <code>cifs_t</code> </p>
<p> <code>gconf_tmp_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/gconfd-[^/]+/.*</p>
<p> <code>gnome_home_type</code> </p>
<p> <code>httpd_user_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/((www)|(web)|(public_html))(/.+)?</p>
<p> <code>httpd_user_htaccess_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/((www)|(web)|(public_html))(/.*)?/.htaccess</p>
<p> <code>httpd_user_ra_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/((www)|(web)|(public_html))(/.*)?/logs(/.*)?</p>
<p> <code>httpd_user_rw_content_t</code> </p>
<p> <code>httpd_user_script_exec_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/((www)|(web)|(public_html))/cgi-bin(/.+)?</p>
<p> <code>noxattrfs</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all files on file systems which do not support extended attributes</p>
<p> <code>pulseaudio_tmpfs_t</code> </p>
<p> <code>pulseaudio_tmpfsfile</code> </p>
<p> <code>usbfs_t</code> </p>
<p> <code>user_fonts_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts.cache-.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts.cache-.*</p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-xguest/">xguest</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-xguest_dbusd_selinux/">xguest_dbusd_selinux</a>(8), <a href="/docs/linux/man/8-xguest_dbusd_selinux/">xguest_dbusd_selinux</a>(8), <a href="/docs/linux/man/8-xguest_gkeyringd_selinux/">xguest_gkeyringd_selinux</a>(8), <a href="/docs/linux/man/8-xguest_gkeyringd_selinux/">xguest_gkeyringd_selinux</a>(8) </p>
