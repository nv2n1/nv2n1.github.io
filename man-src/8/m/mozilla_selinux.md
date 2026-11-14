---
title: "mozilla_selinux(8)"
name: "mozilla_selinux"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mozilla_selinux/"
description: "mozilla_selinux – Security Enhanced Linux Policy for the mozilla processes"
---

<p>mozilla_selinux &#8211; Security Enhanced Linux Policy for the mozilla processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the mozilla processes via flexible mandatory access control. The mozilla processes execute with the mozilla_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep mozilla_t</code> </p>
<h2>Entrypoints</h2>
<p>The mozilla_t SELinux type can be entered via the <code>mozilla_exec_t</code> file type. </p>
<p> The default entrypoint paths for the mozilla_t domain are the following: </p>
<p> /usr/lib/[^/]*firefox[^/]*/firefox, /usr/lib/[^/]*firefox[^/]*/firefox-bin, /usr/lib/mozilla[^/]*/reg.+, /usr/lib/mozilla[^/]*/mozilla-.*, /usr/lib/firefox[^/]*/mozilla-.*, /usr/bin/mozilla-[0-9].*, /usr/lib/netscape/.+/communicator/communicator-smotif.real, /usr/bin/mozilla-bin-[0-9].*, /usr/bin/mozilla, /usr/bin/netscape, /usr/bin/epiphany, /usr/bin/epiphany-bin, /usr/lib/galeon/galeon, /usr/bin/mozilla-snapshot, /usr/lib/netscape/base-4/wrapper</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux mozilla policy is very flexible allowing users to setup their mozilla processes in as secure a method as possible. </p>
<p> The following process types are defined for mozilla: </p>
<p> mozilla_t, mozilla_plugin_t, mozilla_plugin_config_t</code> </p>
<p> Note: <code>semanage permissive -a mozilla_t</code> can be used to make the process type mozilla_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. mozilla policy is extremely flexible and has several booleans that allow you to manipulate the policy and run mozilla with the tightest access possible. </p>
<p> If you want to allow confined web browsers to read home directory content, you must turn on the mozilla_read_content boolean. Disabled by default. </p>
<p> <code>setsebool -P mozilla_read_content 1</code> </p>
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
<p> If you want to allow confined applications to run with kerberos, you must turn on the kerberos_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P kerberos_enabled 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to allow regular users direct dri device access, you must turn on the selinuxuser_direct_dri_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_direct_dri_enabled 1</code> </p>
<p> If you want to allow unconfined executables to make their stack executable. This should never, ever be necessary. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla, you must turn on the selinuxuser_execstack boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_execstack 1</code> </p>
<p> If you want to support ecryptfs home directories, you must turn on the use_ecryptfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_ecryptfs_home_dirs 1</code> </p>
<p> If you want to support fusefs home directories, you must turn on the use_fusefs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_fusefs_home_dirs 1</code> </p>
<p> If you want to support NFS home directories, you must turn on the use_nfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_nfs_home_dirs 1</code> </p>
<p> If you want to support SAMBA home directories, you must turn on the use_samba_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_samba_home_dirs 1</code> </p>
<p> If you want to allows clients to write to the X server shared memory segments, you must turn on the xserver_clients_write_xshm boolean. Disabled by default. </p>
<p> <code>setsebool -P xserver_clients_write_xshm 1</code> </p>
<p> If you want to support X userspace object manager, you must turn on the xserver_object_manager boolean. Enabled by default. </p>
<p> <code>setsebool -P xserver_object_manager 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type mozilla_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>cifs_t</code> </p>
<p> <code>ecryptfs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.Private(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.ecryptfs(/.*)?</p>
<p> <code>fusefs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user/[^/]*/gvfs</p>
<p> <code>gconf_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.local.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.gconf(d)?(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.local.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.gconf(d)?(/.*)?</p>
<p> <code>gnome_home_type</code> </p>
<p> <code>mozilla_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.lyx(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.java(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.adobe(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.gnash(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.webex(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.galeon(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.spicec(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.IBMERS(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/POkemon.*(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.mozilla(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.phoenix(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.icedtea(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.netscape(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.quakelive(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.ICAClient(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.macromedia(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.thunderbird(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.gcjwebplugin(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.grl-podcasts(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.cache/mozilla(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.icedteaplugin(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/zimbrauserdata(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.config/chromium(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.juniper_networks(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.cache/icedtea-web(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/abc</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.gnashpluginrc</p>
<p> <code>mozilla_tmp_t</code> </p>
<p> <code>mozilla_tmpfs_t</code> </p>
<p> <code>nfs_t</code> </p>
<p> <code>pulseaudio_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.pulse(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.config/pulse(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.esd_auth</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.pulse-cookie</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.pulse(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.config/pulse(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.esd_auth</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.pulse-cookie</p>
<p> <code>user_fonts_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts.cache-.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts.cache-.*</p>
<p> <code>xserver_tmpfs_t</code></p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux mozilla policy is very flexible allowing users to setup their mozilla processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the mozilla, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t mozilla_tmpfs_t &#8216;/srv/mymozilla_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mymozilla_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for mozilla:</i> </p>
<p> <code>mozilla_conf_t</code> </p>
<p> &#8211; Set files with the mozilla_conf_t type, if you want to treat the files as mozilla configuration data, usually stored under the /etc directory. </p>
<p> <code>mozilla_exec_t</code> </p>
<p> &#8211; Set files with the mozilla_exec_t type, if you want to transition an executable to the mozilla_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/[^/]*firefox[^/]*/firefox, /usr/lib/[^/]*firefox[^/]*/firefox-bin, /usr/lib/mozilla[^/]*/reg.+, /usr/lib/mozilla[^/]*/mozilla-.*, /usr/lib/firefox[^/]*/mozilla-.*, /usr/bin/mozilla-[0-9].*, /usr/lib/netscape/.+/communicator/communicator-smotif.real, /usr/bin/mozilla-bin-[0-9].*, /usr/bin/mozilla, /usr/bin/netscape, /usr/bin/epiphany, /usr/bin/epiphany-bin, /usr/lib/galeon/galeon, /usr/bin/mozilla-snapshot, /usr/lib/netscape/base-4/wrapper </p>
</dl>
<p> <code>mozilla_home_t</code> </p>
<p> &#8211; Set files with the mozilla_home_t type, if you want to store mozilla files in the users home directory. </p>
<dl>
<dt>Paths:</p>
<dd>/home/[^/]+/.lyx(/.*)?, /home/[^/]+/.java(/.*)?, /home/[^/]+/.adobe(/.*)?, /home/[^/]+/.gnash(/.*)?, /home/[^/]+/.webex(/.*)?, /home/[^/]+/.galeon(/.*)?, /home/[^/]+/.spicec(/.*)?, /home/[^/]+/.IBMERS(/.*)?, /home/[^/]+/POkemon.*(/.*)?, /home/[^/]+/.mozilla(/.*)?, /home/[^/]+/.phoenix(/.*)?, /home/[^/]+/.icedtea(/.*)?, /home/[^/]+/.netscape(/.*)?, /home/[^/]+/.quakelive(/.*)?, /home/[^/]+/.ICAClient(/.*)?, /home/[^/]+/.macromedia(/.*)?, /home/[^/]+/.thunderbird(/.*)?, /home/[^/]+/.gcjwebplugin(/.*)?, /home/[^/]+/.grl-podcasts(/.*)?, /home/[^/]+/.cache/mozilla(/.*)?, /home/[^/]+/.icedteaplugin(/.*)?, /home/[^/]+/zimbrauserdata(/.*)?, /home/[^/]+/.config/chromium(/.*)?, /home/[^/]+/.juniper_networks(/.*)?, /home/[^/]+/.cache/icedtea-web(/.*)?, /home/[^/]+/abc, /home/[^/]+/.gnashpluginrc </p>
</dl>
<p> <code>mozilla_plugin_config_exec_t</code> </p>
<p> &#8211; Set files with the mozilla_plugin_config_exec_t type, if you want to transition an executable to the mozilla_plugin_config_t domain. </p>
<p> <code>mozilla_plugin_exec_t</code> </p>
<p> &#8211; Set files with the mozilla_plugin_exec_t type, if you want to transition an executable to the mozilla_plugin_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/lib/xulrunner[^/]*/plugin-container, /usr/lib/nspluginwrapper/npviewer.bin, /usr/bin/nspluginscan, /usr/bin/nspluginviewer, /usr/libexec/WebKitPluginProcess, /usr/lib/firefox/plugin-container </p>
</dl>
<p> <code>mozilla_plugin_rw_t</code> </p>
<p> &#8211; Set files with the mozilla_plugin_rw_t type, if you want to treat the files as mozilla plugin read/write content. </p>
<p> <code>mozilla_plugin_tmp_t</code> </p>
<p> &#8211; Set files with the mozilla_plugin_tmp_t type, if you want to store mozilla plugin temporary files in the /tmp directories. </p>
<p> <code>mozilla_plugin_tmpfs_t</code> </p>
<p> &#8211; Set files with the mozilla_plugin_tmpfs_t type, if you want to store mozilla plugin files on a tmpfs file system. </p>
<p> <code>mozilla_tmp_t</code> </p>
<p> &#8211; Set files with the mozilla_tmp_t type, if you want to store mozilla temporary files in the /tmp directories. </p>
<p> <code>mozilla_tmpfs_t</code> </p>
<p> &#8211; Set files with the mozilla_tmpfs_t type, if you want to store mozilla files on a tmpfs file system. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-mozilla/">mozilla</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-mozilla_plugin_selinux/">mozilla_plugin_selinux</a>(8), <a href="/docs/linux/man/8-mozilla_plugin_selinux/">mozilla_plugin_selinux</a>(8), <a href="/docs/linux/man/8-mozilla_plugin_config_selinux/">mozilla_plugin_config_selinux</a>(8), <a href="/docs/linux/man/8-mozilla_plugin_config_selinux/">mozilla_plugin_config_selinux</a>(8) </p>
