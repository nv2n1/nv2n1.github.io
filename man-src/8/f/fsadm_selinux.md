---
title: "fsadm_selinux(8)"
name: "fsadm_selinux"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsadm_selinux/"
description: "fsadm_selinux – Security Enhanced Linux Policy for the fsadm processes"
---

<p>fsadm_selinux &#8211; Security Enhanced Linux Policy for the fsadm processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the fsadm processes via flexible mandatory access control. The fsadm processes execute with the fsadm_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep fsadm_t</code> </p>
<h2>Entrypoints</h2>
<p>The fsadm_t SELinux type can be entered via the <code>fsadm_exec_t</code> file type. </p>
<p> The default entrypoint paths for the fsadm_t domain are the following: </p>
<p> /sbin/fsck.*, /sbin/jfs_.*, /sbin/mkfs.*, /sbin/swapon.*, /sbin/resize.*fs, /sbin/losetup.*, /usr/sbin/fsck.*, /usr/sbin/jfs_.*, /usr/sbin/mkfs.*, /sbin/reiserfs(ck|tune), /usr/sbin/swapon.*, /usr/sbin/resize.*fs, /usr/sbin/losetup.*, /usr/sbin/reiserfs(ck|tune), /sbin/dump, /sbin/blkid, /sbin/fdisk, /sbin/partx, /sbin/cfdisk, /sbin/e2fsck, /sbin/e4fsck, /sbin/findfs, /sbin/hdparm, /sbin/lsraid, /sbin/mke2fs, /sbin/mke4fs, /sbin/mkraid, /sbin/parted, /sbin/sfdisk, /usr/bin/raw, /sbin/dosfsck, /sbin/e2label, /sbin/mkdosfs, /sbin/swapoff, /sbin/tune2fs, /sbin/blockdev, /sbin/dumpe2fs, /usr/sbin/dump, /sbin/partprobe, /sbin/raidstart, /sbin/scsi_info, /usr/sbin/blkid, /usr/sbin/fdisk, /usr/sbin/partx, /sbin/mkreiserfs, /sbin/xfs_growfs, /usr/sbin/cfdisk, /usr/sbin/e2fsck, /usr/sbin/e4fsck, /usr/sbin/findfs, /usr/sbin/hdparm, /usr/sbin/lsraid, /usr/sbin/mke2fs, /usr/sbin/mke4fs, /usr/sbin/mkraid, /usr/sbin/parted, /usr/sbin/sfdisk, /sbin/install-mbr, /sbin/raidautorun, /usr/bin/syslinux, /usr/sbin/dosfsck, /usr/sbin/e2label, /usr/sbin/mkdosfs, /usr/sbin/swapoff, /usr/sbin/tune2fs, /sbin/make_reiser4, /usr/sbin/blockdev, /usr/sbin/dumpe2fs, /usr/sbin/smartctl, /usr/sbin/partprobe, /usr/sbin/raidstart, /usr/sbin/scsi_info, /usr/sbin/mkreiserfs, /usr/sbin/xfs_growfs, /usr/sbin/clubufflush, /usr/sbin/install-mbr, /usr/sbin/raidautorun, /usr/sbin/make_reiser4, /usr/bin/partition_uuid, /usr/bin/scsi_unique_id, /usr/lib/systemd/systemd-fsck</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux fsadm policy is very flexible allowing users to setup their fsadm processes in as secure a method as possible. </p>
<p> The following process types are defined for fsadm: </p>
<p> fsadm_t</code> </p>
<p> Note: <code>semanage permissive -a fsadm_t</code> can be used to make the process type fsadm_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. fsadm policy is extremely flexible and has several booleans that allow you to manipulate the policy and run fsadm with the tightest access possible. </p>
<p> If you want to allow all daemons the ability to read/write terminals, you must turn on the daemons_use_tty boolean. Disabled by default. </p>
<p> <code>setsebool -P daemons_use_tty 1</code> </p>
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
<p> If you want to control the ability to mmap a low area of the address space, as configured by /proc/sys/vm/mmap_min_addr, you must turn on the mmap_low_allowed boolean. Disabled by default. </p>
<p> <code>setsebool -P mmap_low_allowed 1</code> </p>
<p> If you want to allow system to run with NIS, you must turn on the nis_enabled boolean. Disabled by default. </p>
<p> <code>setsebool -P nis_enabled 1</code> </p>
<p> If you want to disable kernel module loading, you must turn on the secure_mode_insmod boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode_insmod 1</code> </p>
<p> If you want to boolean to determine whether the system permits loading policy, setting enforcing mode, and changing boolean values. Set this to true and you have to reboot to set it back, you must turn on the secure_mode_policyload boolean. Enabled by default. </p>
<p> <code>setsebool -P secure_mode_policyload 1</code> </p>
<p> If you want to allow unconfined executables to make their heap memory executable. Doing this is a really bad idea. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla, you must turn on the selinuxuser_execheap boolean. Disabled by default. </p>
<p> <code>setsebool -P selinuxuser_execheap 1</code> </p>
<p> If you want to allow all unconfined executables to use libraries requiring text relocation that are not labeled textrel_shlib_t, you must turn on the selinuxuser_execmod boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_execmod 1</code> </p>
<p> If you want to allow unconfined executables to make their stack executable. This should never, ever be necessary. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla, you must turn on the selinuxuser_execstack boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_execstack 1</code> </p>
<p> If you want to support X userspace object manager, you must turn on the xserver_object_manager boolean. Enabled by default. </p>
<p> <code>setsebool -P xserver_object_manager 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type fsadm_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>file_type</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all files on the system</p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux fsadm policy is very flexible allowing users to setup their fsadm processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the fsadm, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t fsadm_var_run_t &#8216;/srv/myfsadm_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/myfsadm_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for fsadm:</i> </p>
<p> <code>fsadm_exec_t</code> </p>
<p> &#8211; Set files with the fsadm_exec_t type, if you want to transition an executable to the fsadm_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/sbin/fsck.*, /sbin/jfs_.*, /sbin/mkfs.*, /sbin/swapon.*, /sbin/resize.*fs, /sbin/losetup.*, /usr/sbin/fsck.*, /usr/sbin/jfs_.*, /usr/sbin/mkfs.*, /sbin/reiserfs(ck|tune), /usr/sbin/swapon.*, /usr/sbin/resize.*fs, /usr/sbin/losetup.*, /usr/sbin/reiserfs(ck|tune), /sbin/dump, /sbin/blkid, /sbin/fdisk, /sbin/partx, /sbin/cfdisk, /sbin/e2fsck, /sbin/e4fsck, /sbin/findfs, /sbin/hdparm, /sbin/lsraid, /sbin/mke2fs, /sbin/mke4fs, /sbin/mkraid, /sbin/parted, /sbin/sfdisk, /usr/bin/raw, /sbin/dosfsck, /sbin/e2label, /sbin/mkdosfs, /sbin/swapoff, /sbin/tune2fs, /sbin/blockdev, /sbin/dumpe2fs, /usr/sbin/dump, /sbin/partprobe, /sbin/raidstart, /sbin/scsi_info, /usr/sbin/blkid, /usr/sbin/fdisk, /usr/sbin/partx, /sbin/mkreiserfs, /sbin/xfs_growfs, /usr/sbin/cfdisk, /usr/sbin/e2fsck, /usr/sbin/e4fsck, /usr/sbin/findfs, /usr/sbin/hdparm, /usr/sbin/lsraid, /usr/sbin/mke2fs, /usr/sbin/mke4fs, /usr/sbin/mkraid, /usr/sbin/parted, /usr/sbin/sfdisk, /sbin/install-mbr, /sbin/raidautorun, /usr/bin/syslinux, /usr/sbin/dosfsck, /usr/sbin/e2label, /usr/sbin/mkdosfs, /usr/sbin/swapoff, /usr/sbin/tune2fs, /sbin/make_reiser4, /usr/sbin/blockdev, /usr/sbin/dumpe2fs, /usr/sbin/smartctl, /usr/sbin/partprobe, /usr/sbin/raidstart, /usr/sbin/scsi_info, /usr/sbin/mkreiserfs, /usr/sbin/xfs_growfs, /usr/sbin/clubufflush, /usr/sbin/install-mbr, /usr/sbin/raidautorun, /usr/sbin/make_reiser4, /usr/bin/partition_uuid, /usr/bin/scsi_unique_id, /usr/lib/systemd/systemd-fsck </p>
</dl>
<p> <code>fsadm_log_t</code> </p>
<p> &#8211; Set files with the fsadm_log_t type, if you want to treat the data as fsadm log data, usually stored under the /var/log directory. </p>
<p> <code>fsadm_tmp_t</code> </p>
<p> &#8211; Set files with the fsadm_tmp_t type, if you want to store fsadm temporary files in the /tmp directories. </p>
<p> <code>fsadm_tmpfs_t</code> </p>
<p> &#8211; Set files with the fsadm_tmpfs_t type, if you want to store fsadm files on a tmpfs file system. </p>
<p> <code>fsadm_var_run_t</code> </p>
<p> &#8211; Set files with the fsadm_var_run_t type, if you want to store the fsadm files under the /run or /var/run directory. </p>
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
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-fsadm/">fsadm</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
