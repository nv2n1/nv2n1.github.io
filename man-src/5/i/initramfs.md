---
title: "initramfs(5)"
name: "initramfs"
section: "5"
letter: "i"
url: "/docs/linux/man/5-initramfs/"
description: "initramfs.conf – configuration file for mkinitramfs"
---

<p>initramfs.conf &#8211; configuration file for mkinitramfs</p>
<h2>Description</h2>
<p>The behaviour of <code>mkinitramfs</code> can be modified by its configuration file. Each line in the file can be a configuration variable, a blank line, or a comment. The value of an variable is assigned by an statement of the form: <i>name</i>=[<i>value</i>] Configuration options can be broken out into configuration snippets and placed in individual files in the /etc/mkinitramfs/conf.d directory. Files in this directory are always read <code>after</code> the main configuration file, so you can override the settings in the main config file without editing it directly. </p>
<h2>General Variables</h2>
<dl>
<dt><code> MODULES</p>
<dd>Specifies the modules for the initramfs image. </p>
<p> Modules listed in </code><i>/etc/initramfs-tools/modules</i> and <i>/usr/share/initramfs-tools/modules.d/*</i> are always included in the initramfs, and are loaded early in the boot process. </p>
<p> <i>list</i> doesn&#8217;t load any additional modules at boot time, other than those listed in the above files. </p>
<p> <i>most</i> adds most file system, all ata, sata, scsi and usb drivers. </p>
<p> <i>dep</i> tries to guess which modules are necessary for the running box and only adds those modules. </p>
<p> <i>netboot</i> adds the base and network modules, but skips block devices. </p>
<p> The default setting is <i>most</i>. </p>
<dt><code> BUSYBOX</p>
<dd>Include busybox utilities for the boot scripts. If set to &#8216;n&#8217; mkinitramfs</code> will build an initramfs without busybox. Beware that many boot scripts need busybox utilities. </p>
<dt><code> COMPRESS</p>
<dd>Specifies the compression method used for the initramfs image. mkinitramfs</code> will default to gzip if the kernel lacks support (CONFIG_RD) or the corresponding userspace utility is not present. </p>
<dt><code> UMASK</p>
<dd>Set the umask value of the generated initramfs file. Useful to not disclose eventual keys. </p>
<dt> COMPCACHE_SIZE</p>
<dd>Amount of RAM to use for RAM-based compressed swap space. The default is not to use compcache. </p>
<p> An empty value &#8211; compcache isn&#8217;t used, or added to the initramfs at all. </p>
<p> An integer and K (e.g. </code><i>65536 K</i>) &#8211; use a number of kilobytes. </p>
<p> An integer and M (e.g. <i>256 M</i>) &#8211; use a number of megabytes. </p>
<p> An integer and G (e.g. <i>1 G</i>) &#8211; use a number of gigabytes. </p>
<p> An integer and % (e.g. <i>50 %</i>) &#8211; use a percentage of the amount of RAM. </p>
<p> You can optionally install the <i>compcache</i> package to configure this setting via debconf and have userspace scripts to load and unload compcache. </p>
</dl>
<h2>Nfs Variables</h2>
<dl>
<dt><code> BOOT</p>
<dd>Allows one to use an nfs drive as the root of the drive. The default is to boot from </code><i>local</i> media (hard drive, USB stick). Set to <i>nfs</i> for an NFS root share. </p>
<dt><code> DEVICE</p>
<dd>Specifies the network interface, like eth0. </p>
<dt> ROOT</p>
<dd>Allows optional root bootarg hardcoding, when no root bootarg can be passed. A root bootarg overrides that special setting. </p>
<dt> NFSROOT</p>
<dd>Defaults to </code><i>auto</i> in order to pick up value from DHCP server. Otherwise you need to specify <i>HOST:MOUNT</i>. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/initramfs-tools/initramfs.conf</i></p>
<dd></dl>
<h2>Author</h2>
<p>The initramfs-tools are written by Maximilian Attems &lt;maks [at] debian.org&gt;, Jeff Bailey &lt;jbailey [at] raspberryginger.com&gt; and numerous others. Loosely based on mkinitrd.conf by Herbert Xu.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-initramfs-tools/">initramfs-tools</a></i>(8), <i><a href="/docs/linux/man/8-mkinitramfs/">mkinitramfs</a></i>(8), <i><a href="/docs/linux/man/8-update-initramfs/">update-initramfs</a></i>(8). </p>
