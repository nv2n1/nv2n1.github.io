---
title: "guestfs-recipes(1)"
name: "guestfs-recipes"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestfs-recipes/"
description: "guestfs-recipes – libguestfs, guestfish and virt tools recipes"
---

<h2 class="name">NAME</h2>
<p> guestfs-recipes &#8211; libguestfs, guestfish and virt tools recipes </p>
<h2>DESCRIPTION</h2>
<p> This page contains recipes for and links to things you can do using libguestfs, <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) and the virt tools.</p>
<h2>Access a remote disk image using guestfish</h2>
<p> If the disk image is on a remote server which is accessible using <font SIZE="-1">SSH, HTTP, FTP, NBD,</font> iSCSI, or similar, then you can open it directly. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) for several examples. This requires libguestfs ≥ 1.22 and qemu ≥ 1.5.</p>
<h2>Audit a virtual machine for setuid files</h2>
<p> See: &#8220;<font SIZE="-1">EXAMPLES&#8221;</font> in <code><a href="/docs/linux/man/1-virt-ls/">virt-ls</a></code>(1).</p>
<h2>Audit a virtual machine for vulnerabilities and security problems</h2>
<p> See: <a rel="nofollow" href="https://rwmj.wordpress.com/2013/05/16/scanning-offline-guests-using-openscap-and-guestmount/#content">https://rwmj.wordpress.com/2013/05/16/scanning-offline-guests-using-openscap-and-guestmount/#content</a></p>
<h2>Change the background image in a Windows XP VM</h2>
<p> The links below explain how to use <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) to change the background image for a user of a Windows <font SIZE="-1">XP VM.</font> Unfortunately the technique appears to be substantially different for each version of Windows. </p>
<p> <a rel="nofollow" href="https://lists.fedoraproject.org/pipermail/virt/2011-May/002655.html">https://lists.fedoraproject.org/pipermail/virt/2011-May/002655.html</a> <a rel="nofollow" href="https://lists.fedoraproject.org/pipermail/virt/2011-May/002658.html">https://lists.fedoraproject.org/pipermail/virt/2011-May/002658.html</a></p>
<h2>Checksum a file or device within a disk image</h2>
<p> To checksum a whole device, or a partition, <font SIZE="-1">LV</font> etc within a disk image: </p>
<pre>
 guestfish --ro -a disk.img run : checksum-device md5 /dev/sda1
</pre>
<p> Replace <tt>&quot;md5&quot;</tt> with the type of checksum you want. See &#8220;guestfs_checksum_device&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) for a list of supported types. </p>
<p> <i>/dev/sda1</i> means &#8220;the first partition&#8221;. You could use <i>/dev/sda</i> to checksum the whole disk image, or the name of a logical volume or <font SIZE="-1">RAID</font> device. </p>
<p> To checksum a single file: </p>
<pre>
 guestfish --ro -a disk.img -i checksum sha256 /etc/passwd
</pre>
<p> or for a Windows guest: </p>
<pre>
 guestfish --ro -a disk.img -i \
   checksum sha256 'win:\windows\system32
