---
title: "dracut-conf(5)"
name: "dracut-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dracut-conf/"
description: "dracut.conf – configuration file(s) for dracut"
---

<p>dracut.conf &#8211; configuration file(s) for dracut</p>
<h2>Synopsis</h2>
<p><i>/etc/dracut.conf</i> <i>/etc/dracut.conf.d/</i><i></i><code>.conf</code><i> </i><i>/usr/lib/dracut/dracut.conf.d/</i><i>.conf</i></p>
<h2>Description</h2>
<p><i>dracut.conf</i> is loaded during the initialisation phase of dracut. Command line parameter will overwrite any values set here. <i>*.conf</i> files are read from /usr/lib/dracut/dracut.conf.d and /etc/dracut.conf.d. Files with the same name in /etc/dracut.conf.d will replace files in /usr/lib/dracut/dracut.conf.d. The files are then read in alphanumerical order and will overwrite parameters set in <i>/etc/dracut.conf</i>. Each line specifies an attribute and a value. A <i>#</i> indicates the beginning of a comment; following characters, up to the end of the line are not interpreted. dracut command line options will overwrite any values set here. Configuration files must have the extension .conf; other extensions are ignored.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Space-separated lists have to have a leading and trailing space!  <code>dracutmodules+=</code>&quot;&nbsp;<wbr><i>&lt;dracut modules&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Specify a space-separated list of dracut modules to call when building the initramfs. Modules are located in <i>/usr/lib/dracut/modules.d</i>.</dl>
<p> <code>omit_dracutmodules+=</code>&quot;&nbsp;<wbr><i>&lt;dracut modules&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Omit a space-separated list of dracut modules.</dl>
<p> <code>add_dracutmodules+=</code>&quot;&nbsp;<wbr><i>&lt;dracut modules&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Add a space-separated list of dracut modules.</dl>
<p> <code>drivers+=</code>&quot;&nbsp;<wbr><i>&lt;kernel modules&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Specify a space-separated list of kernel modules to exclusively include in the initramfs. The kernel modules have to be specified without the &quot;.ko&quot; suffix.</dl>
<p> <code>add_drivers+=</code>&quot;&nbsp;<wbr><i>&lt;kernel modules&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Specify a space-separated list of kernel modules to add to the initramfs. The kernel modules have to be specified without the &quot;.ko&quot; suffix.</dl>
<p> <code>omit_drivers+=</code>&quot;&nbsp;<wbr><i>&lt;kernel modules&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Specify a space-separated list of kernel modules not to add to the initramfs. The kernel modules have to be specified without the &quot;.ko&quot; suffix.</dl>
<p> <code>filesystems+=</code>&quot;&nbsp;<wbr><i>&lt;filesystem names&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Specify a space-separated list of kernel filesystem modules to exclusively include in the generic initramfs.</dl>
<p> <code>drivers_dir=</code>&quot;<i>&lt;kernel modules directory&gt;</i>&quot;</p>
<dl>
<dd>Specify the directory, where to look for kernel modules</dl>
<p> <code>fw_dir+=</code>&quot;&nbsp;<wbr>:<i>&lt;dir&gt;</i>[:<i>&lt;dir&gt;</i>&nbsp;<wbr>&#8230;]&nbsp;<wbr>&quot;</p>
<dl>
<dd>Specify additional directories, where to look for firmwares, separated by :</dl>
<p> <code>install_items+=</code>&quot;&nbsp;<wbr><i>&lt;file&gt;</i>[ <i>&lt;file&gt;</i>&nbsp;<wbr>&#8230;]&nbsp;<wbr>&quot;</p>
<dl>
<dd>Specify additional files to include in the initramfs, separated by spaces.</dl>
<p> <code>install_optional_items+=</code>&quot;&nbsp;<wbr><i>&lt;file&gt;</i>[ <i>&lt;file&gt;</i>&nbsp;<wbr>&#8230;]&nbsp;<wbr>&quot;</p>
<dl>
<dd>Specify additional files to include in the initramfs, separated by spaces, if they exist.</dl>
<p> <code>do_strip=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Strip binaries in the initramfs (default=yes)</dl>
<p> <code>do_prelink=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Prelink binaries in the initramfs (default=yes)</dl>
<p> <code>hostonly=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Host-Only mode: Install only what is needed for booting the local host instead of a generic host and generate host-specific configuration.</dl>
<p> <code>hostonly_cmdline</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>If set, store the kernel command line arguments needed in the initramfs</dl>
<p> <code>i18n_install_all=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>If set to yes, install all available fonts and keyboard files.</dl>
<pre><code>persistent_policy=&quot;&lt;policy&gt;&quot;

Use
&lt;policy&gt;
to address disks and partitions.
&lt;policy&gt;
can be any directory name found in /dev/disk. E.g. &quot;by-uuid&quot;, &quot;by-label&quot;</code></pre>
<p> <code>tmpdir=</code>&quot;<i>&lt;temporary directory&gt;</i>&quot;</p>
<dl>
<dd>Specify temporary directory to use.</dl>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 If chrooted to another root other than the real root device, use &#8211;fstab and provide a valid <i>/etc/fstab</i>.  <code>use_fstab=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Use <i>/etc/fstab</i> instead of <i>/proc/self/mountinfo</i>.</dl>
<p> <code>add_fstab+=</code>&quot;&nbsp;<wbr><i>&lt;filename&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Add entries of <i>&lt;filename&gt;</i> to the initramfs /etc/fstab.</dl>
<p> <code>add_device+=</code>&quot;&nbsp;<wbr><i>&lt;device&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Bring up <i>&lt;device&gt;</i> in initramfs, <i>&lt;device&gt;</i> should be the device name. This can be useful in hostonly mode for resume support when your swap is on LVM an encrypted partition.</dl>
<p> <code>mdadmconf=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Include local <i>/etc/mdadm.conf</i> (default=yes)</dl>
<p> <code>lvmconf=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Include local <i>/etc/lvm/lvm.conf</i> (default=yes)</dl>
<p> <code>fscks=</code>&quot;&nbsp;<wbr><i>&lt;fsck tools&gt;</i>&nbsp;<wbr>&quot;</p>
<dl>
<dd>Add a space-separated list of fsck tools. If nothing is specified, the default is: &quot;umount mount /sbin/fsck* xfs_db xfs_check xfs_repair e2fsck jfs_fsck reiserfsck btrfsck&quot;. The installation is opportunistic (non-existing tools are ignored).</dl>
<p> <code>nofscks=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>If specified, inhibit installation of any fsck tools.</dl>
<p> <code>ro_mnt=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Mount <i>/</i> and <i>/usr</i> read-only by default.</dl>
<p> <code>kernel_cmdline=</code>&quot;<i>parameters</i>&quot;</p>
<dl>
<dd>Specify default kernel command line parameters</dl>
<p> <code>kernel_only=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Only install kernel drivers and firmware files. (default=no)</dl>
<p> <code>no_kernel=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Do not install kernel drivers and firmware files (default=no)</dl>
<p> <code>acpi_override=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>[WARNING] ONLY USE THIS IF YOU KNOW WHAT YOU ARE DOING! Override BIOS provided ACPI tables. For further documentation read Documentation/acpi/initrd_table_override.txt in the kernel sources. Search for ACPI table files (must have .aml suffix) in acpi_table_dir= directory (see below) and add them to a separate uncompressed cpio archive. This cpio archive gets glued (concatenated, uncompressed one must be the first one) to the compressed cpio archive. The first, uncompressed cpio archive is for data which the kernel must be able to access very early (and cannot make use of uncompress alogrithms yet) like microcode or ACPI tables (default=no).</dl>
<p> <code>acpi_table_dir=</code>&quot;<i>&lt;dir&gt;</i>&quot;</p>
<dl>
<dd>Directory to search for ACPI tables if acpi_override= is set to yes.</dl>
<p> <code>early_microcode=</code>&quot;{yes|no}&quot;</p>
<dl>
<dd>Combine early microcode with ramdisk (default=no)</dl>
<p> <code>stdloglvl</code>=&quot;<i>{0-6}</i>&quot;</p>
<dl>
<dd>Set logging to standard error level.</dl>
<p> <code>sysloglvl</code>=&quot;<i>{0-6}</i>&quot;</p>
<dl>
<dd>Set logging to syslog level.</dl>
<p> <code>fileloglvl=</code>&quot;<i>{0-6}</i>&quot;</p>
<dl>
<dd>Set logging to file level.</dl>
<p> <code>logfile=</code>&quot;<i>&lt;file&gt;</i>&quot;</p>
<dl>
<dd>Path to log file.</dl>
<p> <code>show_modules=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Print the name of the included modules to standard output during build.</dl>
<p> *i18n_vars=&quot;<i>&lt;variable mapping&gt;</i>&quot;</p>
<dl>
<dd>Distribution specific variable mapping. See dracut/modules.d/10i18n/README for a detailed description.</dl>
<p> <code>i18n_default_font=</code>&quot;<i>&lt;fontname&gt;</i>&quot;</p>
<dl>
<dd>The font &lt;fontname&gt; to install, if not specified otherwise. Default is &quot;LatArCyrHeb-16&quot;.</dl>
<p> <code>i18n_install_all=</code>&quot;<i>{yes|no}</i>&quot;</p>
<dl>
<dd>Install everything regardless of generic or hostonly mode.</dl>
<h2>Files</h2>
<p><i>/etc/dracut.conf</i></p>
<dl>
<dd>Old configuration file. You better use your own file in <i>/etc/dracut.conf.d/</i>.</dl>
<p> <i>/etc/dracut.conf.d/</i></p>
<dl>
<dd>Any <i>/etc/dracut.conf.d/*.conf</i> file can overwrite the values in <i>/etc/dracut.conf</i>. The configuration files are read in alphanumerical order.</dl>
<h2>Author</h2>
<p>Harald Hoyer</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) <code><a href="/docs/linux/man/7-dracut-cmdline/">dracut.cmdline</a></code>(7) </p>
