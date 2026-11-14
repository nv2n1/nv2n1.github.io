---
title: "update-initramfs(8)"
name: "update-initramfs"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-initramfs/"
description: "update-initramfs – generate an initramfs image"
---

<p>update-initramfs &#8211; generate an initramfs image</p>
<h2>Synopsis</h2>
<p><code>update-initramfs</code> {<code>-c</code>|<code>-d</code>|<code>-u</code>} [<code>-k</code> <i>version</i>] [<code>-v</code>] [<code>-b</code> <i>directory</i>]<br />
 <code>update-initramfs</code> <code>-h</code></p>
<h2>Description</h2>
<p>The <code>update-initramfs</code> script manages your initramfs images on your local box. It keeps track of the existing initramfs archives in /boot. There are three modes of operation create, update or delete. You must at least specify one of those modes. The initramfs is a gzipped cpio archive. At boot time, the kernel unpacks that archive into RAM disk, mounts and uses it as initial root file system. All finding of the root device happens in this early userspace. </p>
<h2>Options</h2>
<dl>
<dt><code>-k </code><i> version</p>
<dd>Set the specific kernel version for whom the initramfs will be generated. For example the output of uname -r for your currently running kernel. This argument is optional for update. The default is the latest kernel version. </p>
<p> The use of &quot;all&quot; for the version</i> string specifies that <code>update-initramfs</code> should operate on all installed kernel versions (with <code>-c</code>), or on all installed kernel versions that already have an initramfs (with <code>-d</code> or <code>-u</code>). </p>
<dt><code>-c</p>
<dd>This mode creates a new initramfs. </p>
<dt>-u</p>
<dd>This mode updates an existing initramfs. </p>
<dt>-d</p>
<dd>This mode deletes an existing initramfs. </p>
<dt>-v</p>
<dd>This option increases the amount of information you are given during the chosen action. </p>
<dt>-b </code><i> directory</p>
<dd>Set an different bootdir for the image creation. </p>
<dt></i><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print a short help page describing the available options in <code>update-initramfs.</code> </p>
</dl>
<h2>Examples</h2>
<p>Update the initramfs of the newest kernel: <code>update-initramfs -u</code> Create the initramfs for a specific kernel: <code>update-initramfs -c -k 2.6.18-1-686</code> </p>
<h2>Files</h2>
<p>/etc/initramfs-tools/update-initramfs.conf</p>
<h2>Author</h2>
<p>The initramfs-tools are written by Maximilian Attems &lt;maks [at] debian.org&gt;, Jeff Bailey &lt;jbailey [at] raspberryginger.com&gt; and numerous others.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-initramfs-conf/">initramfs.conf</a></i>(5), <i><a href="/docs/linux/man/7-initramfs-tools/">initramfs-tools</a></i>(7), <i><a href="/docs/linux/man/8-mkinitramfs/">mkinitramfs</a></i>(8), <i><a href="/docs/linux/man/8-lsinitramfs/">lsinitramfs</a></i>(8). </p>
