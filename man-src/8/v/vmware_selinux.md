---
title: "vmware_selinux(8)"
name: "vmware_selinux"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vmware_selinux/"
description: "vmware_selinux – Security Enhanced Linux Policy for the vmware processes"
---

<p>vmware_selinux &#8211; Security Enhanced Linux Policy for the vmware processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the vmware processes via flexible mandatory access control. The vmware processes execute with the vmware_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep vmware_t</code> </p>
<h2>Entrypoints</h2>
<p>The vmware_t SELinux type can be entered via the <code>vmware_exec_t</code> file type. </p>
<p> The default entrypoint paths for the vmware_t domain are the following: </p>
<p> /opt/vmware/(workstation|player)/bin/vmware, /opt/vmware/(workstation|player)/bin/vmware-ping, /opt/vmware/(workstation|player)/bin/vmware-wizard, /usr/bin/vmware, /usr/bin/vmware-ping, /usr/bin/vmware-wizard, /usr/sbin/vmware-serverd, /usr/lib/vmware/bin/vmplayer, /usr/lib/vmware/bin/vmware-ui, /usr/lib/vmware/bin/vmware-mks</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux vmware policy is very flexible allowing users to setup their vmware processes in as secure a method as possible. </p>
<p> The following process types are defined for vmware: </p>
<p> vmware_t, vmware_host_t</code> </p>
<p> Note: <code>semanage permissive -a vmware_t</code> can be used to make the process type vmware_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. vmware policy is extremely flexible and has several booleans that allow you to manipulate the policy and run vmware with the tightest access possible. </p>
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
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Enabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to allow regular users direct dri device access, you must turn on the selinuxuser_direct_dri_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_direct_dri_enabled 1</code> </p>
<p> If you want to support NFS home directories, you must turn on the use_nfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_nfs_home_dirs 1</code> </p>
<p> If you want to support SAMBA home directories, you must turn on the use_samba_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_samba_home_dirs 1</code> </p>
<p> If you want to allows clients to write to the X server shared memory segments, you must turn on the xserver_clients_write_xshm boolean. Disabled by default. </p>
<p> <code>setsebool -P xserver_clients_write_xshm 1</code> </p>
<p> If you want to support X userspace object manager, you must turn on the xserver_object_manager boolean. Enabled by default. </p>
<p> <code>setsebool -P xserver_object_manager 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type vmware_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>cifs_t</code> </p>
<p> <code>nfs_t</code> </p>
<p> <code>usbfs_t</code> </p>
<p> <code>user_fonts_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts.cache-.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts.cache-.*</p>
<p> <code>vmware_conf_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.vmware[^/]*/.*.cfg</p>
<p> <code>vmware_file_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/vmware(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.vmware(/.*)?</p>
<p> <code>vmware_pid_t</code> </p>
<p> <code>vmware_tmp_t</code> </p>
<p> <code>vmware_tmpfs_t</code> </p>
<p> <code>xserver_tmpfs_t</code></p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux vmware policy is very flexible allowing users to setup their vmware processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the vmware, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t vmware_tmpfs_t &#8216;/srv/myvmware_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myvmware_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for vmware:</i> </p>
<p> <code>vmware_conf_t</code> </p>
<p> &#8211; Set files with the vmware_conf_t type, if you want to treat the files as vmware configuration data, usually stored under the /etc directory. </p>
<p> <code>vmware_exec_t</code> </p>
<p> &#8211; Set files with the vmware_exec_t type, if you want to transition an executable to the vmware_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/opt/vmware/(workstation|player)/bin/vmware, /opt/vmware/(workstation|player)/bin/vmware-ping, /opt/vmware/(workstation|player)/bin/vmware-wizard, /usr/bin/vmware, /usr/bin/vmware-ping, /usr/bin/vmware-wizard, /usr/sbin/vmware-serverd, /usr/lib/vmware/bin/vmplayer, /usr/lib/vmware/bin/vmware-ui, /usr/lib/vmware/bin/vmware-mks </p>
</dl>
<p> <code>vmware_file_t</code> </p>
<p> &#8211; Set files with the vmware_file_t type, if you want to treat the files as vmware content. </p>
<dl>
<dt>Paths:</p>
<dd>/home/[^/]+/vmware(/.*)?, /home/[^/]+/.vmware(/.*)? </p>
</dl>
<p> <code>vmware_host_exec_t</code> </p>
<p> &#8211; Set files with the vmware_host_exec_t type, if you want to transition an executable to the vmware_host_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/opt/vmware/(workstation|player)/bin/vmnet-natd, /opt/vmware/(workstation|player)/bin/vmnet-dhcpd, /opt/vmware/(workstation|player)/bin/vmware-nmbd, /opt/vmware/(workstation|player)/bin/vmware-smbd, /opt/vmware/(workstation|player)/bin/vmnet-bridge, /opt/vmware/(workstation|player)/bin/vmnet-netifup, /opt/vmware/(workstation|player)/bin/vmnet-sniffer, /opt/vmware/(workstation|player)/bin/vmware-smbpasswd, /opt/vmware/(workstation|player)/bin/vmware-smbpasswd.bin, /usr/sbin/vmware-guest.*, /usr/lib/vmware-tools/sbin32/vmware.*, /usr/lib/vmware-tools/sbin64/vmware.*, /usr/bin/vmnet-natd, /usr/bin/vmware-vmx, /usr/bin/vmnet-dhcpd, /usr/bin/vmware-nmbd, /usr/bin/vmware-smbd, /usr/bin/vmnet-bridge, /usr/bin/vmnet-netifup, /usr/bin/vmnet-sniffer, /usr/bin/vmware-network, /usr/bin/vmware-smbpasswd, /usr/bin/vmware-smbpasswd.bin, /usr/lib/vmware/bin/vmware-vmx </p>
</dl>
<p> <code>vmware_host_pid_t</code> </p>
<p> &#8211; Set files with the vmware_host_pid_t type, if you want to store the vmware host files under the /run directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/run/vmnat.*, /var/run/vmnet.*, /var/run/vmware.* </p>
</dl>
<p> <code>vmware_host_tmp_t</code> </p>
<p> &#8211; Set files with the vmware_host_tmp_t type, if you want to store vmware host temporary files in the /tmp directories. </p>
<p> <code>vmware_log_t</code> </p>
<p> &#8211; Set files with the vmware_log_t type, if you want to treat the data as vmware log data, usually stored under the /var/log directory. </p>
<dl>
<dt>Paths:</p>
<dd>/var/log/vmware.*, /var/log/vnetlib.* </p>
</dl>
<p> <code>vmware_pid_t</code> </p>
<p> &#8211; Set files with the vmware_pid_t type, if you want to store the vmware files under the /run directory. </p>
<p> <code>vmware_sys_conf_t</code> </p>
<p> &#8211; Set files with the vmware_sys_conf_t type, if you want to treat the files as vmware sys configuration data, usually stored under the /etc directory. </p>
<dl>
<dt>Paths:</p>
<dd>/etc/vmware.*(/.*)?, /usr/lib/vmware/config </p>
</dl>
<p> <code>vmware_tmp_t</code> </p>
<p> &#8211; Set files with the vmware_tmp_t type, if you want to store vmware temporary files in the /tmp directories. </p>
<p> <code>vmware_tmpfs_t</code> </p>
<p> &#8211; Set files with the vmware_tmpfs_t type, if you want to store vmware files on a tmpfs file system. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-vmware/">vmware</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-vmware_host_selinux/">vmware_host_selinux</a>(8), <a href="/docs/linux/man/8-vmware_host_selinux/">vmware_host_selinux</a>(8) </p>
