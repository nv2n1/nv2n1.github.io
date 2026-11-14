---
title: "update-initramfs-conf(5)"
name: "update-initramfs-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-update-initramfs-conf/"
description: "update-initramfs.conf – configuration file for update-initramfs"
---

<p>update-initramfs.conf &#8211; configuration file for update-initramfs</p>
<h2>Description</h2>
<p>The configuration file allows one to disable the update action from <code>update-initramfs.</code> </p>
<h2>General Variables</h2>
<dl>
<dt><code> update_initramfs</p>
<dd>Default is </code><i>yes</i> for running the latest initramfs-tools hooks in the newest Linux image. Setting it to <i>all</i> updates any known initramfs. It is possible to set it to <i>no</i> for remote servers or boxes where conservative manners needs to be applied. This disables the <code>update_initramfs -u</code> call.</p>
<dt><code> backup_initramfs</p>
<dd>If set update_initramfs</code> keeps an .bak file of the previous initramfs. If unset the backup initramfs will not be kept. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/initramfs-tools/update-initramfs.conf</i></p>
<dd></dl>
<h2>Author</h2>
<p>The initramfs-tools are written by Maximilian Attems &lt;maks [at] debian.org&gt;, Jeff Bailey &lt;jbailey [at] raspberryginger.com&gt; and numerous others.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-initramfs-conf/">initramfs.conf</a></i>(5), <i><a href="/docs/linux/man/7-initramfs-tools/">initramfs-tools</a></i>(7), <i><a href="/docs/linux/man/8-mkinitramfs/">mkinitramfs</a></i>(8), <i><a href="/docs/linux/man/8-update-initramfs/">update-initramfs</a></i>(8). </p>
