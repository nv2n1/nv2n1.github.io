---
title: "mkinitramfs(8)"
name: "mkinitramfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkinitramfs/"
description: "mkinitramfs – low-level tool for generating an initramfs image"
---

<p>mkinitramfs &#8211; low-level tool for generating an initramfs image</p>
<h2>Synopsis</h2>
<p><code>mkinitramfs</code> [<i>option</i>]&#8230; <code>-o</code> <i>outfile</i> [<i>version</i>]<br />
 <code>mkinitramfs</code> <code>-h</code> </p>
<h2>Description</h2>
<p>The <code>mkinitramfs</code> script generates an initramfs image. The initramfs is a compressed cpio archive. The archive can be used on a different box of the same arch with the corresponding Linux kernel. <code>mkinitramfs</code> is meant for advanced usage. On your local box <code>update-initramfs</code> calls <code>mkinitramfs</code> with the relevant parameters. <code>update-initramfs</code> keeps sha1sum of generated initramfs. It takes care to generate backups and eventually runs the bootloader. At boot time, the kernel unpacks that archive into RAM disk, mounts and uses it as initial root file system. All finding of the root device happens in this early userspace. </p>
<h2>Options</h2>
<dl>
<dt><code>-c </code><i> compress</p>
<dd>Override the </i><code>COMPRESS</code> setting in <i>initramfs.conf</i>. </p>
<dt><code>-d </code><i> confdir</p>
<dd>Set an alternate configuration directory. </p>
<dt></i><code>-k</p>
<dd>Keep the temporary directory used to make the image. </p>
<dt>-o </code><i> outfile</p>
<dd>Write the image to outfile</i>. </p>
<dt><code>-r </code><i> root</p>
<dd>Override the </i><code>ROOT</code> setting in <i>initramfs.conf</i>. </p>
<dt><code>-v</p>
<dd>Set the verbose mode output. </p>
<dt></code><i>version</p>
<dd>Set the kernel version of the initramfs image (defaults to the running kernel). </p>
<dt></i><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display usage information and exit. </p>
</dl>
<h2>Environment</h2>
<p><code>mkinitramfs</code> honours the <code>TMPDIR</code> environment variable. If set, it uses subdirectories in the given directory to create its temporary working directories. Else it uses <i>/var/tmp</i> as default value for that purpose. The given directory should be on a filesystem which allows the execution of files stored there, i.e. should not be mounted with the <code>noexec</code> mount option. </p>
<p> If <code>SOURCE_DATE_EPOCH</code> is set, <code>mkinitramfs</code> attempts to generate a reproducible initramfs image.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/initramfs-tools/initramfs.conf</i></p>
<dd>The default configuration file for the script. See <code><a href="/docs/linux/man/5-initramfs-conf/">initramfs.conf</a></code>(5) for a description of the available configuration parameter. </p>
<dt><i>/etc/initramfs-tools/modules</i></p>
<dd>Specified modules will be put in the generated image and loaded when the system boots. The format &#8211; one per line &#8211; is identical to that of <i>/etc/modules,</i> which is described in <code><a href="/docs/linux/man/5-modules/">modules</a></code>(5). </p>
<dt><i>/etc/initramfs-tools/conf.d</i></p>
<dd>The conf.d directory allows one to hardcode bootargs at initramfs build time via config snippets. This allows one to set ROOT or RESUME. This is especially useful for bootloaders, which do not pass an root bootarg. </p>
<dt><i>/etc/initramfs-tools/DSDT.aml</i></p>
<dd>If this file exists, it will be appended to the initramfs in a way that causes it to be loaded by ACPI. </p>
</dl>
<h2>Examples</h2>
<p>Create an initramfs for current running kernel: <code>mkinitramfs -o ~/tmp/initramfs-$(uname -r)</code> Create an initramfs for specific kernel and keep builddirs: <code>mkinitramfs -k -o ~/tmp/initramfs-2.6.21-686 2.6.21-686</code> Debug initramfs creation (check out written logfile) <code>sh -x mkinitramfs -o ~/tmp/initramfs-$(uname -r) 2&gt; ~/tmp/log</code> </p>
<h2>Author</h2>
<p>The initramfs-tools are written by Maximilian Attems &lt;maks [at] debian.org&gt;, Jeff Bailey &lt;jbailey [at] raspberryginger.com&gt; and numerous others.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-initramfs-conf/">initramfs.conf</a></i>(5), <i><a href="/docs/linux/man/7-initramfs-tools/">initramfs-tools</a></i>(7), <i><a href="/docs/linux/man/8-update-initramfs/">update-initramfs</a></i>(8), <i><a href="/docs/linux/man/8-lsinitramfs/">lsinitramfs</a></i>(8), <i><a href="/docs/linux/man/8-unmkinitramfs/">unmkinitramfs</a></i>(8). </p>
