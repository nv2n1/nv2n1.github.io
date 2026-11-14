---
title: "svirt_selinux(8)"
name: "svirt_selinux"
section: "8"
letter: "s"
url: "/docs/linux/man/8-svirt_selinux/"
description: "svirt_selinux – Security Enhanced Linux Policy for the svirt processes"
---

<p>svirt_selinux &#8211; Security Enhanced Linux Policy for the svirt processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the svirt processes via flexible mandatory access control. The svirt processes execute with the svirt_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep svirt_t</code> </p>
<h2>Entrypoints</h2>
<p>The svirt_t SELinux type can be entered via the <code>qemu_exec_t</code> file type. </p>
<p> The default entrypoint paths for the svirt_t domain are the following: </p>
<p> /usr/libexec/qemu.*, /usr/bin/qemu-system-.*, /usr/bin/qemu, /usr/bin/qemu-kvm</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux svirt policy is very flexible allowing users to setup their svirt processes in as secure a method as possible. </p>
<p> The following process types are defined for svirt: </p>
<p> svirt_t, svirt_tcg_t, svirt_lxc_net_t, svirt_qemu_net_t, svirt_socket_t, svirt_kvm_net_t</code> </p>
<p> Note: <code>semanage permissive -a svirt_t</code> can be used to make the process type svirt_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>MCS Constrained</h2>
<p>The SELinux process type svirt_t is an MCS (Multi Category Security) constrained type. Sometimes this separation is referred to as sVirt. These types are usually used for securing multi-tenant environments, such as virtualization, containers or separation of users. The tools used to launch MCS types, pick out a different MCS label for each process group. </p>
<p> For example one process might be launched with svirt_t:s0:c1,c2, and another process launched with svirt_t:s0:c3,c4. The SELinux kernel only allows these processes can only write to content with a matching MCS label, or a MCS Label of s0. A process running with the MCS level of s0:c1,c2 is not allowed to write to content with the MCS label of s0:c3,c4</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. svirt policy is extremely flexible and has several booleans that allow you to manipulate the policy and run svirt with the tightest access possible. </p>
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
<p> If you want to allow confined virtual guests to use serial/parallel communication ports, you must turn on the virt_use_comm boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_comm 1</code> </p>
<p> If you want to allow confined virtual guests to use executable memory and executable stack, you must turn on the virt_use_execmem boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_execmem 1</code> </p>
<p> If you want to allow confined virtual guests to read fuse files, you must turn on the virt_use_fusefs boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_fusefs 1</code> </p>
<p> If you want to allow confined virtual guests to manage nfs files, you must turn on the virt_use_nfs boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_nfs 1</code> </p>
<p> If you want to allow confined virtual guests to interact with rawip sockets, you must turn on the virt_use_rawip boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_rawip 1</code> </p>
<p> If you want to allow confined virtual guests to manage cifs files, you must turn on the virt_use_samba boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_samba 1</code> </p>
<p> If you want to allow confined virtual guests to interact with the sanlock, you must turn on the virt_use_sanlock boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_sanlock 1</code> </p>
<p> If you want to allow confined virtual guests to use usb devices, you must turn on the virt_use_usb boolean. Enabled by default. </p>
<p> <code>setsebool -P virt_use_usb 1</code> </p>
<p> If you want to allow confined virtual guests to interact with the xserver, you must turn on the virt_use_xserver boolean. Disabled by default. </p>
<p> <code>setsebool -P virt_use_xserver 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type svirt_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>anon_inodefs_t</code> </p>
<p> <code>cifs_t</code> </p>
<p> <code>dosfs_t</code> </p>
<p> <code>fusefs_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user/[^/]*/gvfs</p>
<p> <code>nfs_t</code> </p>
<p> <code>qemu_var_run_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/libvirt/qemu(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/libvirt/qemu(/.*)?</p>
<p> <code>svirt_home_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.libvirt/qemu(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.cache/libvirt/qemu(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.config/libvirt/qemu(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.local/share/libvirt/boot(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.local/share/libvirt/images(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.local/share/gnome-boxes/images(/.*)?</p>
<p> <code>svirt_image_t</code> </p>
<p> <code>svirt_tmp_t</code> </p>
<p> <code>svirt_tmpfs_t</code> </p>
<p> <code>usbfs_t</code> </p>
<p> <code>virt_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/oz(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/cache/libvirt(/.*)?</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux svirt policy is very flexible allowing users to setup their svirt processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the svirt, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t svirt_tmpfs_t &#8216;/srv/mysvirt_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mysvirt_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for svirt:</i> </p>
<p> <code>svirt_home_t</code> </p>
<p> &#8211; Set files with the svirt_home_t type, if you want to store svirt files in the users home directory. </p>
<dl>
<dt>Paths:</p>
<dd>/home/[^/]+/.libvirt/qemu(/.*)?, /home/[^/]+/.cache/libvirt/qemu(/.*)?, /home/[^/]+/.config/libvirt/qemu(/.*)?, /home/[^/]+/.local/share/libvirt/boot(/.*)?, /home/[^/]+/.local/share/libvirt/images(/.*)?, /home/[^/]+/.local/share/gnome-boxes/images(/.*)? </p>
</dl>
<p> <code>svirt_image_t</code> </p>
<p> &#8211; Set files with the svirt_image_t type, if you want to treat the files as svirt image data. </p>
<p> <code>svirt_sandbox_file_t</code> </p>
<p> &#8211; Set files with the svirt_sandbox_file_t type, if you want to treat the files as svirt sandbox content. </p>
<dl>
<dt>Paths:</p>
<dd>/var/lib/kubelet(/.*)?, /var/lib/docker/vfs(/.*)? </p>
</dl>
<p> <code>svirt_tmp_t</code> </p>
<p> &#8211; Set files with the svirt_tmp_t type, if you want to store svirt temporary files in the /tmp directories. </p>
<p> <code>svirt_tmpfs_t</code> </p>
<p> &#8211; Set files with the svirt_tmpfs_t type, if you want to store svirt files on a tmpfs file system. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-svirt/">svirt</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-svirt_kvm_net_selinux/">svirt_kvm_net_selinux</a>(8), <a href="/docs/linux/man/8-svirt_kvm_net_selinux/">svirt_kvm_net_selinux</a>(8), <a href="/docs/linux/man/8-svirt_lxc_net_selinux/">svirt_lxc_net_selinux</a>(8), <a href="/docs/linux/man/8-svirt_lxc_net_selinux/">svirt_lxc_net_selinux</a>(8), <a href="/docs/linux/man/8-svirt_qemu_net_selinux/">svirt_qemu_net_selinux</a>(8), <a href="/docs/linux/man/8-svirt_qemu_net_selinux/">svirt_qemu_net_selinux</a>(8), <a href="/docs/linux/man/8-svirt_socket_selinux/">svirt_socket_selinux</a>(8), <a href="/docs/linux/man/8-svirt_socket_selinux/">svirt_socket_selinux</a>(8), <a href="/docs/linux/man/8-svirt_tcg_selinux/">svirt_tcg_selinux</a>(8), <a href="/docs/linux/man/8-svirt_tcg_selinux/">svirt_tcg_selinux</a>(8) </p>
