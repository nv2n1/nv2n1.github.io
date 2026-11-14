---
title: "mkbiarch(8)"
name: "mkbiarch"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkbiarch/"
description: "mkbiarch.py – make a multiple architecture Live boot disk image for USB, CF SSD or any disk from 2 architecturally different LiveCD ISO9660 image files."
---

<p>mkbiarch.py &#8211; make a multiple architecture Live boot disk image for USB, CF SSD or any disk from 2 architecturally different LiveCD ISO9660 image files.</p>
<h2>Synopsis</h2>
<p>mkbiarch &lt;LiveCDx86ISO&gt; &lt;LiveCDx64ISO&gt; &lt;MultipleArch Disk IMG File&gt; </p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/8-mkbiarch/">mkbiarch</a>(8)</code> create a multiple architecture, bootable Live Disk image file (IMG) for use on USB or any disk (CF, SSD) from 2 LiveCD ISO9660 files of different architecture (ISO). </p>
<h2>Usage</h2>
<p><code>mkbiarch.py</code> Fedora-13-i686-Live.iso Fedora-13-x86_64-Live.iso Fedora-13-MultiArch.img </p>
<p> Then to write it /bin/dd if=Fedora-13-MultiArch.img of=/dev/sdb bs=4M </p>
<p> In the above example, mkbiarch.py creates Fedora-Multi-arch.img from the two existing ISO9660 LiveCD image files. The resulting image file, is written to a raw disk device using <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code></p>
<h2>Under The Hood</h2>
<p><code><a href="/docs/linux/man/8-mkbiarch-py/">mkbiarch.py</a>(8)</code> first checks that the two ISO9660 image files exist. It will create a blank file using <a href="/docs/linux/man/1-dd/">dd</a>(1) writing data from /dev/zero, the size of the two ISO9660 images files combined. The blank file is then bound via loopback using <code><a href="/docs/linux/man/8-losetup/">losetup</a>(8)</code> partitioned, and bound at an offset via loopback of 512 bytes, this second loopback device is formatted type ext3 using <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a>(8)</code> This filesystem is mounted using <code><a href="/docs/linux/man/8-mount/">mount</a>(8)</code> on a temporary directory. The two ISO9660 files are then mounted via loopback, files are copied using shutil module in Python, from them to the newly formatted filesystem in the image file. Data is gathered from the ISO9660 image files from it&#8217;s isolinux.cfg, after the files are copied the loopbacked ISO9660 image files are released. <code><a href="/docs/linux/man/1-extlinux/">extlinux</a>(1)</code> is installed to the loopback mounted filesystem on the target image file and an extlinux.conf is written. The temporary directories are unmounted using <code><a href="/docs/linux/man/8-umount/">umount</a>(8)</code> and the looback devices are released. The temporary directories are then removed, and the resulting Multiple Architecture Disk Image File is moved using shutil to the specified location on the command line, which is provided as argument 3 to mkbiarch.py</p>
<h2>Bugs</h2>
<p>Please report any bugs to <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> under component livecd-tools </p>
<h2>Availability</h2>
<p>To check out the git version of this program<br />
&nbsp;<wbr>git clone&nbsp;<wbr><a href="git://git.fedorahosted.org/livecd">git://git.fedorahosted.org/livecd</a></p>
<h2>Author</h2>
<p>Jasper Hartline &lt;autopsy [at] liveprojects.info&gt;</p>
<h2>Contributors</h2>
<p><code>Richard Shaw &lt;email [at] address.com&gt; </code> pyparted suggestions and feedback </p>
<p> <code>Jan Kratochvil &lt;email [at] address.com&gt; </code> for the original bash script which the python version was derived</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-livecd-creator/">livecd-creator</a>(8),</code> <code><a href="/docs/linux/man/8-livecd-iso-to-disk/">livecd-iso-to-disk</a>(8),</code> <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a>(8),</code> <code><a href="/docs/linux/man/8-losetup/">losetup</a>(8),</code> <code><a href="/docs/linux/man/1-dd/">dd</a>(1),</code> <code><a href="/docs/linux/man/1-exlinux/">exlinux</a>(1)</code> </p>
