---
title: "httpd_sys_script_selinux(8)"
name: "httpd_sys_script_selinux"
section: "8"
letter: "h"
url: "/docs/linux/man/8-httpd_sys_script_selinux/"
description: "httpd_sys_script_selinux – Security Enhanced Linux Policy for the httpd_sys_script processes"
---

<p>httpd_sys_script_selinux &#8211; Security Enhanced Linux Policy for the httpd_sys_script processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the httpd_sys_script processes via flexible mandatory access control. The httpd_sys_script processes execute with the httpd_sys_script_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep httpd_sys_script_t</code> </p>
<h2>Entrypoints</h2>
<p>The httpd_sys_script_t SELinux type can be entered via the <code>nfs_t, httpd_sys_script_exec_t, httpd_sys_content_t, cifs_t, shell_exec_t, httpd_sys_script_exec_t, httpd_sys_content_t, httpdcontent</code> file types. </p>
<p> The default entrypoint paths for the httpd_sys_script_t domain are the following: </p>
<p> /usr/.*.cgi, /opt/.*.cgi, /var/www/[^/]*/cgi-bin(/.*)?, /var/www/perl(/.*)?, /var/www/html/[^/]*/cgi-bin(/.*)?, /usr/lib/cgi-bin(/.*)?, /var/www/cgi-bin(/.*)?, /var/www/svn/hooks(/.*)?, /usr/share/wordpress/.*.php, /usr/local/nagios/sbin(/.*)?, /usr/share/wordpress/wp-includes/.*.php, /usr/share/wordpress-mu/wp-config.php, /srv/([^/]*/)?www(/.*)?, /var/www(/.*)?, /etc/htdig(/.*)?, /srv/gallery2(/.*)?, /var/lib/trac(/.*)?, /var/lib/htdig(/.*)?, /var/www/icons(/.*)?, /usr/share/glpi(/.*)?, /usr/share/htdig(/.*)?, /usr/share/drupal.*, /usr/share/z-push(/.*)?, /var/www/svn/conf(/.*)?, /usr/share/icecast(/.*)?, /var/lib/cacti/rra(/.*)?, /usr/share/ntop/html(/.*)?, /usr/share/nginx/html(/.*)?, /usr/share/doc/ghc/html(/.*)?, /usr/share/openca/htdocs(/.*)?, /usr/share/selinux-policy[^/]*/html(/.*)?, /bin/d?ash, /bin/zsh.*, /bin/ksh.*, /usr/bin/d?ash, /usr/bin/zsh.*, /usr/bin/ksh.*, /bin/esh, /bin/mksh, /bin/sash, /bin/tcsh, /bin/yash, /bin/bash, /bin/fish, /bin/bash2, /usr/bin/esh, /usr/bin/tcsh, /usr/bin/yash, /usr/bin/sash, /usr/bin/mksh, /usr/bin/fish, /usr/bin/bash, /sbin/nologin, /usr/sbin/sesh, /usr/bin/bash2, /usr/sbin/smrsh, /usr/bin/scponly, /usr/sbin/nologin, /usr/libexec/sesh, /usr/sbin/scponlyc, /usr/bin/git-shell, /usr/bin/cockpit-bridge, /usr/libexec/cockpit-agent, /usr/libexec/git-core/git-shell, /usr/.*.cgi, /opt/.*.cgi, /var/www/[^/]*/cgi-bin(/.*)?, /var/www/perl(/.*)?, /var/www/html/[^/]*/cgi-bin(/.*)?, /usr/lib/cgi-bin(/.*)?, /var/www/cgi-bin(/.*)?, /var/www/svn/hooks(/.*)?, /usr/share/wordpress/.*.php, /usr/local/nagios/sbin(/.*)?, /usr/share/wordpress/wp-includes/.*.php, /usr/share/wordpress-mu/wp-config.php, /srv/([^/]*/)?www(/.*)?, /var/www(/.*)?, /etc/htdig(/.*)?, /srv/gallery2(/.*)?, /var/lib/trac(/.*)?, /var/lib/htdig(/.*)?, /var/www/icons(/.*)?, /usr/share/glpi(/.*)?, /usr/share/htdig(/.*)?, /usr/share/drupal.*, /usr/share/z-push(/.*)?, /var/www/svn/conf(/.*)?, /usr/share/icecast(/.*)?, /var/lib/cacti/rra(/.*)?, /usr/share/ntop/html(/.*)?, /usr/share/nginx/html(/.*)?, /usr/share/doc/ghc/html(/.*)?, /usr/share/openca/htdocs(/.*)?, /usr/share/selinux-policy[^/]*/html(/.*)?</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux httpd_sys_script policy is very flexible allowing users to setup their httpd_sys_script processes in as secure a method as possible. </p>
<p> The following process types are defined for httpd_sys_script: </p>
<p> httpd_sys_script_t</code> </p>
<p> Note: <code>semanage permissive -a httpd_sys_script_t</code> can be used to make the process type httpd_sys_script_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. httpd_sys_script policy is extremely flexible and has several booleans that allow you to manipulate the policy and run httpd_sys_script with the tightest access possible. </p>
<p> If you want to allow users to resolve user passwd entries directly from ldap rather then using a sssd server, you must turn on the authlogin_nsswitch_use_ldap boolean. Disabled by default. </p>
<p> <code>setsebool -P authlogin_nsswitch_use_ldap 1</code> </p>
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
<p> If you want to allow httpd to use built in scripting (usually php), you must turn on the httpd_builtin_scripting boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_builtin_scripting 1</code> </p>
<p> If you want to allow HTTPD scripts and modules to connect to the network using TCP, you must turn on the httpd_can_network_connect boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_network_connect 1</code> </p>
<p> If you want to allow HTTPD scripts and modules to connect to databases over the network, you must turn on the httpd_can_network_connect_db boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_network_connect_db 1</code> </p>
<p> If you want to allow http daemon to send mail, you must turn on the httpd_can_sendmail boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_can_sendmail 1</code> </p>
<p> If you want to allow httpd cgi support, you must turn on the httpd_enable_cgi boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_enable_cgi 1</code> </p>
<p> If you want to allow httpd to read home directories, you must turn on the httpd_enable_homedirs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_enable_homedirs 1</code> </p>
<p> If you want to allow httpd scripts and modules execmem/execstack, you must turn on the httpd_execmem boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_execmem 1</code> </p>
<p> If you want to allow httpd to read user content, you must turn on the httpd_read_user_content boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_read_user_content 1</code> </p>
<p> If you want to allow HTTPD to run SSI executables in the same domain as system CGI scripts, you must turn on the httpd_ssi_exec boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_ssi_exec 1</code> </p>
<p> If you want to allow Apache to execute tmp content, you must turn on the httpd_tmp_exec boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_tmp_exec 1</code> </p>
<p> If you want to unify HTTPD handling of all content files, you must turn on the httpd_unified boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_unified 1</code> </p>
<p> If you want to allow httpd to access cifs file systems, you must turn on the httpd_use_cifs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_cifs 1</code> </p>
<p> If you want to allow httpd to access FUSE file systems, you must turn on the httpd_use_fusefs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_fusefs 1</code> </p>
<p> If you want to allow httpd to access nfs file systems, you must turn on the httpd_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_nfs 1</code> </p>
<p> If you want to allow httpd to access openstack ports, you must turn on the httpd_use_openstack boolean. Disabled by default. </p>
<p> <code>setsebool -P httpd_use_openstack 1</code> </p>
<p> If you want to allow confined applications to run with kerberos, you must turn on the kerberos_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P kerberos_enabled 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to allow unprivileged users to execute DDL statement, you must turn on the postgresql_selinux_users_ddl boolean. Enabled by default. </p>
<p> <code>setsebool -P postgresql_selinux_users_ddl 1</code> </p>
<p> If you want to support NFS home directories, you must turn on the use_nfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_nfs_home_dirs 1</code> </p>
<p> If you want to support SAMBA home directories, you must turn on the use_samba_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_samba_home_dirs 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type httpd_sys_script_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>anon_inodefs_t</code> </p>
<p> <code>cifs_t</code> </p>
<p> <code>fusefs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user/[^/]*/gvfs</p>
<p> <code>httpd_sys_rw_content_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/glpi(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/horde(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/drupal.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/z-push(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/svn(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/svn(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/owncloud(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/uploads(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/wp-content(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/wp_backups(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/sites/default/files(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html(/.*)?/sites/default/settings.php</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/mock/koji(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/drupal.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/zabbix/web(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/moodle(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/z-push(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/gosa(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/etc/WebCalendar(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/joomla(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/dokuwiki(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/owncloud(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/viewvc(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/pootle/po(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/moodledata(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/srv/gallery2/smarty(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/moodle/data(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/graphite-web(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/gallery/albums(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html/owncloud/data(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/wordpress-mu/wp-content(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/wordpress/wp-content/uploads(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/share/wordpress/wp-content/upgrade(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/html/configuration.php</p>
<p> <code>httpd_tmp_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user/apache(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/www/openshift/console/tmp(/.*)?</p>
<p> <code>httpdcontent</code> </p>
<p> <code>nfs_t</code> </p>
<p> <code>public_content_rw_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/spool/abrt-upload(/.*)?</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux httpd_sys_script policy is very flexible allowing users to setup their httpd_sys_script processes in as secure a method as possible. </p>
<p> </code><i>The following file types are defined for httpd_sys_script:</i> </p>
<p> <code>httpd_sys_script_exec_t</code> </p>
<p> &#8211; Set files with the httpd_sys_script_exec_t type, if you want to transition an executable to the httpd_sys_script_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/.*.cgi, /opt/.*.cgi, /var/www/[^/]*/cgi-bin(/.*)?, /var/www/perl(/.*)?, /var/www/html/[^/]*/cgi-bin(/.*)?, /usr/lib/cgi-bin(/.*)?, /var/www/cgi-bin(/.*)?, /var/www/svn/hooks(/.*)?, /usr/share/wordpress/.*.php, /usr/local/nagios/sbin(/.*)?, /usr/share/wordpress/wp-includes/.*.php, /usr/share/wordpress-mu/wp-config.php </p>
</dl>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Sharing Files</h2>
<p>If you want to share files with multiple domains (Apache, FTP, rsync, Samba), you can set a file context of public_content_t and public_content_rw_t. These context allow any of the above domains to read the content. If you want a particular domain to write to the public_content_rw_t domain, you must set the appropriate boolean.</p>
<dl>
<dt>Allow httpd_sys_script servers to read the /var/httpd_sys_script directory by adding the public_content_t file type to the directory and by restoring the file type.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_t &quot;/var/httpd_sys_script(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/httpd_sys_script</code></p>
<dl>
<dt>Allow httpd_sys_script servers to read and write /var/httpd_sys_script/incoming by adding the public_content_rw_t type to the directory and by restoring the file type. You also need to turn on the httpd_sys_script_anon_write boolean.</p>
<dd></dl>
<p> <code>semanage fcontext -a -t public_content_rw_t &quot;/var/httpd_sys_script/incoming(/.*)?&quot;</code><br />
 <code>restorecon -F -R -v /var/httpd_sys_script/incoming</code><br />
 <code>setsebool -P httpd_sys_script_anon_write 1</code> </p>
<p> If you want to allow apache scripts to write to public content, directories/files must be labeled public_rw_content_t., you must turn on the httpd_sys_script_anon_write boolean. </p>
<p> <code>setsebool -P httpd_sys_script_anon_write 1</code></p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-httpd_sys_script/">httpd_sys_script</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
