---
title: "virt-resize(1)"
name: "virt-resize"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-resize/"
description: "virt-resize – Resize a virtual machine disk"
---

<h2 class="name">NAME</h2>
<p> virt-resize &#8211; Resize a virtual machine disk </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - resize[--resize / dev / sdaN = [+ / -]&lt;size&gt;[%]]
             [--expand / dev / sdaN][--shrink / dev / sdaN]
             [--ignore / dev / sdaN][--delete / dev / sdaN][...] indisk outdisk
</code></pre>
<h2>DESCRIPTION</h2>
<p> Virt-resize is a tool which can resize a virtual machine disk, making it larger or smaller overall, and resizing or deleting any partitions contained within. </p>
<p> Virt-resize <code>cannot</code> resize disk images in-place. Virt-resize <code>should not</code> be used on live virtual machines &#8211; for consistent results, shut the virtual machine down before resizing it. </p>
<p> If you are not familiar with the associated tools: <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) and <i><a href="/docs/linux/man/1-virt-df/">virt-df</a></i>(1), we recommend you go and read those manual pages first.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>1.</p>
<dd> Copy <tt>&quot;olddisk&quot;</tt> to <tt>&quot;newdisk&quot;</tt>, extending one of the guest&#8217;s partitions to fill the extra 5GB of space. </p>
<p>virt &#8211; filesystems&#8211; long &#8211; h&#8211; all &#8211; a olddisk</p>
<p>                                          truncate &#8211;<br />
    r olddisk newdisk<br />
        truncate &#8211;<br />
    s + 5G newdisk</p>
<p>#Note &#8220;/dev/sda2&#8221; is a partition inside the &#8220;olddisk&#8221; file.<br />
            virt &#8211;<br />
    resize&#8211; expand / dev / sda2 olddisk newdisk</p>
<dt>2.</p>
<dd> As above, but make the /boot partition 200MB bigger, while giving the remaining space to /dev/sda2: </p>
<pre>
 virt-resize --resize /dev/sda1=+200M --expand /dev/sda2 \
   olddisk newdisk
</pre>
<dt>3.</p>
<dd> As in the first example, but expand a logical volume as the final step. This is what you would typically use for Linux guests that use <font SIZE="-1">LVM:</font> </p>
<pre>
 virt-resize --expand /dev/sda2 --LV-expand /dev/vg_guest/lv_root \
   olddisk newdisk
</pre>
<dt>4.</p>
<dd> As in the first example, but the output format will be qcow2 instead of a raw disk: </p>
<pre>
 qemu-img create -f qcow2 -o preallocation=metadata newdisk.qcow2 15G
 virt-resize --expand /dev/sda2 olddisk newdisk.qcow2
</pre>
</dl>
<h2>DETAILED USAGE</h2>
<h3><font SIZE="-1">EXPANDING A VIRTUAL MACHINE DISK</font></h3>
<dl>
<dt>1. Shut down the virtual machine</p>
<dd>
<dt>2. Locate input disk image</p>
<dd> Locate the input disk image (ie. the file or device on the host containing the guest&#8217;s disk). If the guest is managed by libvirt, you can use <tt>&quot;virsh dumpxml&quot;</tt> like this to find the disk image name: </p>
<pre>
 # virsh dumpxml guestname | xpath /domain/devices/disk/source
 Found 1 nodes:
 -- NODE --
 &lt;source dev=&quot;/dev/vg/lv_guest&quot; /&gt;
</pre>
<dt>3. Look at current sizing</p>
<dd> Use <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) to display the current partitions and sizes: </p>
<p>#virt &#8211; filesystems&#8211; long &#8211;parts&#8211; blkdevs &#8211; h &#8211; a / dev / vg / lv_guest<br />
Name Type Size Parent / dev / sda1 partition 101M / dev / sda / dev / sda2 partition 7.9G / dev / sda / dev / sda device 8.0G &#8211;</p>
<p> (This example is a virtual machine with an 8 <font SIZE="-1">GB</font> disk which we would like to expand up to 10 <font SIZE="-1">GB</font>).</p>
<dt>4. Create output disk</p>
<dd> Virt-resize cannot do in-place disk modifications. You have to have space to store the resized output disk. </p>
<p> To store the resized disk image in a file, create a file of a suitable size: </p>
<pre>
 # rm -f outdisk
 # truncate -s 10G outdisk
</pre>
<p> Or use <i><a href="/docs/linux/man/1-lvcreate/">lvcreate</a></i>(1) to create a logical volume: </p>
<pre>
 # lvcreate -L 10G -n lv_name vg_name
</pre>
<p> Or use <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1) vol-create-as to create a libvirt storage volume: </p>
<pre>
 # virsh pool-list
 # virsh vol-create-as poolname newvol 10G
</pre>
<dt>5. Resize</p>
<dd> virt-resize takes two mandatory parameters, the input disk (eg. device, file, or a <font SIZE="-1">URI</font> to a remote disk) and the output disk. The output disk is the one created in the previous step. </p>
<pre>
 # virt-resize indisk outdisk
</pre>
<p> This command just copies disk image <tt>&quot;indisk&quot;</tt> to disk image <tt>&quot;outdisk&quot;</tt> <i>without</i> resizing or changing any existing partitions. If <tt>&quot;outdisk&quot;</tt> is larger, then an extra, empty partition is created at the end of the disk covering the extra space. If <tt>&quot;outdisk&quot;</tt> is smaller, then it will give an error. </p>
<p> More realistically you&#8217;d want to expand existing partitions in the disk image by passing extra options (for the full list see the &#8220;<font SIZE="-1">OPTIONS&#8221;</font> section below). </p>
<p> &#8220;&#8211;expand&#8221; is the most useful option. It expands the named partition within the disk to fill any extra space: </p>
<pre>
 # virt-resize --expand /dev/sda2 indisk outdisk
</pre>
<p> (In this case, an extra partition is <i>not</i> created at the end of the disk, because there will be no unused space). </p>
<p> &#8220;&#8211;resize&#8221; is the other commonly used option. The following would increase the size of /dev/sda1 by 200M, and expand /dev/sda2 to fill the rest of the available space: </p>
<pre>
 # virt-resize --resize /dev/sda1=+200M --expand /dev/sda2 \
     indisk outdisk
</pre>
<p> If the expanded partition in the image contains a filesystem or <font SIZE="-1">LVM PV,</font> then if virt-resize knows how, it will resize the contents, the equivalent of calling a command such as <i><a href="/docs/linux/man/8-pvresize/">pvresize</a></i>(8), <i><a href="/docs/linux/man/8-resize2fs/">resize2fs</a></i>(8), <i><a href="/docs/linux/man/8-ntfsresize/">ntfsresize</a></i>(8), <i><a href="/docs/linux/man/8-btrfs/">btrfs</a></i>(8) or <i><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a></i>(8). However virt-resize does not know how to resize some filesystems, so you would have to online resize them after booting the guest. </p>
<pre>
 # virt-resize --expand /dev/sda2 <a href="nbd://example.com">nbd://example.com</a> outdisk
</pre>
<p> The input disk can be a <font SIZE="-1">URI,</font> in order to use a remote disk as the source. The <font SIZE="-1">URI</font> format is compatible with guestfish. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). </p>
<p> Other options are covered below.</p>
<dt>6. Test</p>
<dd> Thoroughly test the new disk image <i>before</i> discarding the old one. </p>
<p> If you are using libvirt, edit the <font SIZE="-1">XML</font> to point at the new disk: </p>
<pre>
 # virsh edit guestname
</pre>
<p> Change &lt;source &#8230;&gt;, see <a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsDisks">http://libvirt.org/formatdomain.html#elementsDisks</a> </p>
<p> Then start up the domain with the new, resized disk: </p>
<pre>
 # virsh start guestname
</pre>
<p> and check that it still works. See also the &#8220;<font SIZE="-1">NOTES&#8221;</font> section below for additional information.</p>
<dt>7. Resize LVs etc inside the guest</p>
<dd> (This can also be done offline using <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1)) </p>
<p> Once the guest has booted you should see the new space available, at least for filesystems that virt-resize knows how to resize, and for PVs. The user may need to resize LVs inside PVs, and also resize filesystem types that virt-resize does not know how to expand.</dl>
<h3><font SIZE="-1">SHRINKING A VIRTUAL MACHINE DISK</font></h3>
<p> Shrinking is somewhat more complex than expanding, and only an overview is given here. </p>
<p> Firstly virt-resize will not attempt to shrink any partition content (PVs, filesystems). The user has to shrink content before passing the disk image to virt-resize, and virt-resize will check that the content has been shrunk properly. </p>
<p> (Shrinking can also be done offline using <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1)) </p>
<p> After shrinking PVs and filesystems, shut down the guest, and proceed with steps 3 and 4 above to allocate a new disk image. </p>
<p> Then run virt-resize with any of the <i>&#8211;shrink</i> and/or <i>&#8211;resize</i> options.</p>
<h3><font SIZE="-1">IGNORING OR DELETING PARTITIONS</font></h3>
<p> virt-resize also gives a convenient way to ignore or delete partitions when copying from the input disk to the output disk. Ignoring a partition speeds up the copy where you don&#8217;t care about the existing contents of a partition. Deleting a partition removes it completely, but note that it also renumbers any partitions after the one which is deleted, which can leave some guests unbootable.</p>
<h3><font SIZE="-1">QCOW2 AND</font> NON-SPARSE <font SIZE="-1">RAW FORMATS</font></h3>
<p> If the input disk is in qcow2 format, then you may prefer that the output is in qcow2 format as well. Alternately, virt-resize can convert the format on the fly. The output format is simply determined by the format of the empty output container that you provide. Thus to create qcow2 output, use: </p>
<pre>
 qemu-img create -f qcow2 -o preallocation=metadata outdisk [size]
</pre>
<p> instead of the truncate command. </p>
<p> Similarly, to get non-sparse raw output use: </p>
<pre>
 fallocate -l size outdisk
</pre>
<p> (on older systems that don&#8217;t have the <i><a href="/docs/linux/man/1-fallocate/">fallocate</a></i>(1) command use <tt>&quot;dd if=/dev/zero of=outdisk bs=1M count=..&quot;</tt>)</p>
<h3><font SIZE="-1">LOGICAL PARTITIONS</font></h3>
<p> Logical partitions (a.k.a. <i>/dev/sda5+</i> on disks using <font SIZE="-1">DOS</font> partition tables) cannot be resized. </p>
<p> To understand what is going on, firstly one of the four partitions <i>/dev/sda1-4</i> will have <font SIZE="-1">MBR</font> partition type <tt>05</tt> or <tt>&quot;0f&quot;</tt>. This is called the <code>extended partition</code>. Use <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) to see the <font SIZE="-1">MBR</font> partition type. </p>
<p> Logical partitions live inside the extended partition. </p>
<p> The extended partition can be expanded, but not shrunk (unless you force it, which is not advisable). When the extended partition is copied across, all the logical partitions contained inside are copied over implicitly. Virt-resize does not look inside the extended partition, so it copies the logical partitions blindly. </p>
<p> You cannot specify a logical partition (<i>/dev/sda5+</i>) at all on the command line. Doing so will give an error.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>&#8211;align-first auto</code></p>
<dd>
<dt><code>&#8211;align-first never</code></p>
<dd>
<dt><code>&#8211;align-first always</code></p>
<dd> Align the first partition for improved performance (see also the <i>&#8211;alignment</i> option). </p>
<p> The default is <i>&#8211;align-first auto</i> which only aligns the first partition if it is safe to do so. That is, only when we know how to fix the bootloader automatically, and at the moment that can only be done for Windows guests. </p>
<p> <i>&#8211;align-first never</i> means we never move the first partition. This is the safest option. Try this if the guest does not boot after resizing. </p>
<p> <i>&#8211;align-first always</i> means we always align the first partition (if it needs to be aligned). For some guests this will break the bootloader, making the guest unbootable.</p>
<dt><code>&#8211;alignment N</code></p>
<dd> Set the alignment of partitions to <tt>&quot;N&quot;</tt> sectors. The default in virt-resize &lt; 1.13.19 was 64 sectors, and after that is 128 sectors. </p>
<p> Assuming 512 byte sector size inside the guest, here are some suitable values for this:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>&#8211;alignment 1</i> (512 bytes)</p>
<dd> The partitions would be packed together as closely as possible, but would be completely unaligned. In some cases this can cause very poor performance. See <i><a href="/docs/linux/man/1-virt-alignment-scan/">virt-alignment-scan</a></i>(1) for further details.</p>
<dt><i>&#8211;alignment 8</i> (4K)</p>
<dd> This would be the minimum acceptable alignment for reasonable performance on modern hosts.</p>
<dt><i>&#8211;alignment 128</i> (64K)</p>
<dd> This alignment provides good performance when the host is using high end network storage.</p>
<dt><i>&#8211;alignment 2048</i> (1M)</p>
<dd> This is the standard alignment used by all newly installed guests since around 2008.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;colors</code></p>
<dd>
<dt><code>&#8211;colours</code></p>
<dd> Use <font SIZE="-1">ANSI</font> colour sequences to colourize messages. This is the default when the output is a tty. If the output of the program is redirected to a file, <font SIZE="-1">ANSI</font> colour sequences are disabled unless you use this option.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;debug</code></p>
<dd> (Deprecated: use <i>-v</i> option instead) </p>
<p> Enable debugging messages.</p>
<dt><code>&#8211;debug-gc</code></p>
<dd> Debug garbage collection and memory allocation. This is only useful when debugging memory problems in virt-resize or the OCaml libguestfs bindings.</p>
<dt><code>&#8211;delete part</code></p>
<dd> Delete the named partition. It would be more accurate to describe this as &#8220;don&#8217;t copy it over&#8221;, since virt-resize doesn&#8217;t do in-place changes and the original disk image is left intact. </p>
<p> Note that when you delete a partition, then anything contained in the partition is also deleted. Furthermore, this causes any partitions that come after to be <i>renumbered</i>, which can easily make your guest unbootable. </p>
<p> You can give this option multiple times.</p>
<dt><code>&#8211;expand part</code></p>
<dd> Expand the named partition so it uses up all extra space (space left over after any other resize changes that you request have been done). </p>
<p> If virt-resize knows how, it will expand the direct content of the partition. For example, if the partition is an <font SIZE="-1">LVM PV,</font> it will expand the <font SIZE="-1">PV</font> to fit (like calling <i><a href="/docs/linux/man/8-pvresize/">pvresize</a></i>(8)). Virt-resize leaves any other content it doesn&#8217;t know about alone. </p>
<p> Currently virt-resize can resize:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> ext2, ext3 and ext4 filesystems.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">NTFS</font> filesystems, if libguestfs was compiled with support for <font SIZE="-1">NTFS.</font> </p>
<p> The filesystem must have been shut down consistently last time it was used. Additionally, <i><a href="/docs/linux/man/8-ntfsresize/">ntfsresize</a></i>(8) marks the resized filesystem as requiring a consistency check, so at the first boot after resizing Windows will check the disk.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">LVM</font> PVs (physical volumes). virt-resize does not usually resize anything inside the <font SIZE="-1">PV,</font> but see the <i>&#8211;LV-expand</i> option. The user could also resize LVs as desired after boot.</p>
<dt>&bull;</p>
<dd> Btrfs filesystems, if libguestfs was compiled with support for btrfs.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">XFS</font> filesystems, if libguestfs was compiled with support for <font SIZE="-1">XFS.</font></dl>
</dl>
<dl>
<dt>
<dd>
<p> Note that you cannot use <i>&#8211;expand</i> and <i>&#8211;shrink</i> together.</dl>
<dt><code>&#8211;format</code> raw</p>
<dd> Specify the format of the input disk image. If this flag is not given then it is auto-detected from the image itself. </p>
<p> If working with untrusted raw-format guest disk images, you should ensure the format is always specified. </p>
<p> Note that this option <i>does not</i> affect the output format. See &#8220;<font SIZE="-1">QCOW2 AND</font> NON-SPARSE <font SIZE="-1">RAW FORMATS&#8221;</font>.</p>
<dt><code>&#8211;ignore part</code></p>
<dd> Ignore the named partition. Effectively this means the partition is allocated on the destination disk, but the content is not copied across from the source disk. The content of the partition will be blank (all zero bytes). </p>
<p> You can give this option multiple times.</p>
<dt><code>&#8211;LV-expand logvol</code></p>
<dd> This takes the logical volume and, as a final step, expands it to fill all the space available in its volume group. A typical usage, assuming a Linux guest with a single <font SIZE="-1">PV </font><i>/dev/sda2</i> and a root device called <i>/dev/vg_guest/lv_root</i> would be: </p>
<pre>
 virt-resize indisk outdisk \
   --expand /dev/sda2 --LV-expand /dev/vg_guest/lv_root
</pre>
<p> This would first expand the partition (and <font SIZE="-1">PV</font>), and then expand the root device to fill the extra space in the <font SIZE="-1">PV.</font> </p>
<p> The contents of the <font SIZE="-1">LV</font> are also resized if virt-resize knows how to do that. You can stop virt-resize from trying to expand the content by using the option <i>&#8211;no-expand-content</i>. </p>
<p> Use <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) to list the filesystems in the guest. </p>
<p> You can give this option multiple times, <i>but</i> it doesn&#8217;t make sense to do this unless the logical volumes you specify are all in different volume groups.</p>
<dt><code>&#8211;machine-readable</code></p>
<dd> This option is used to make the output more machine friendly when being parsed by other programs. See &#8220;<font SIZE="-1">MACHINE READABLE OUTPUT&#8221;</font> below.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;dryrun</code></p>
<dd> Print a summary of what would be done, but don&#8217;t do anything.</p>
<dt><code>&#8211;no-copy-boot-loader</code></p>
<dd> By default, virt-resize copies over some sectors at the start of the disk (up to the beginning of the first partition). Commonly these sectors contain the Master Boot Record (<font SIZE="-1">MBR</font>) and the boot loader, and are required in order for the guest to boot correctly. </p>
<p> If you specify this flag, then this initial copy is not done. You may need to reinstall the boot loader in this case.</p>
<dt><code>&#8211;no-extra-partition</code></p>
<dd> By default, virt-resize creates an extra partition if there is any extra, unused space after all resizing has happened. Use this option to prevent the extra partition from being created. If you do this then the extra space will be inaccessible until you run fdisk, parted, or some other partitioning tool in the guest. </p>
<p> Note that if the surplus space is smaller than 10 <font SIZE="-1">MB,</font> no extra partition will be created.</p>
<dt><code>&#8211;no-expand-content</code></p>
<dd> By default, virt-resize will try to expand the direct contents of partitions, if it knows how (see <i>&#8211;expand</i> option above). </p>
<p> If you give the <i>&#8211;no-expand-content</i> option then virt-resize will not attempt this.</p>
<dt><code>&#8211;no-sparse</code></p>
<dd> Turn off sparse copying. See &#8220;<font SIZE="-1">SPARSE COPYING&#8221;</font> below.</p>
<dt><code>&#8211;ntfsresize-force</code></p>
<dd> Pass the <i>&#8211;force</i> option to <i><a href="/docs/linux/man/8-ntfsresize/">ntfsresize</a></i>(8), allowing resizing even if the <font SIZE="-1">NTFS</font> disk is marked as needing a consistency check. You have to use this option if you want to resize a Windows guest multiple times without booting into Windows between each resize.</p>
<dt><code>&#8211;output-format</code> raw</p>
<dd> Specify the format of the output disk image. If this flag is not given then it is auto-detected from the image itself. </p>
<p> If working with untrusted raw-format guest disk images, you should ensure the format is always specified. </p>
<p> Note that this option <i>does not create</i> the output format. This option just tells libguestfs what it is so it doesn&#8217;t try to guess it. You still need to create the output disk with the right format. See &#8220;<font SIZE="-1">QCOW2 AND</font> NON-SPARSE <font SIZE="-1">RAW FORMATS&#8221;</font>.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Don&#8217;t print the summary.</p>
<dt><code>&#8211;resize part=size</code></p>
<dd> Resize the named partition (expanding or shrinking it) so that it has the given size. </p>
<p> <tt>&quot;size&quot;</tt> can be expressed as an absolute number followed by b/K/M/G to mean bytes, Kilobytes, Megabytes, or Gigabytes; or as a percentage of the current size; or as a relative number or percentage. For example: </p>
<p>&#8211;resize / dev / sda2 = 10G &#8211;resize / dev / sda4 = 90 %<br />
                                                    &#8211;resize / dev / sda2 = +1G &#8211;resize / dev / sda2 = -200M &#8211;resize / dev / sda1 = +128K &#8211;resize / dev / sda1 = +10 %<br />
                                                                                                                                                                    &#8211;resize / dev / sda1 = -10 %</p>
<p> You can increase the size of any partition. Virt-resize will expand the direct content of the partition if it knows how (see <i>&#8211;expand</i> above). </p>
<p> You can only <i>decrease</i> the size of partitions that contain filesystems or PVs which have already been shrunk. Virt-resize will check this has been done before proceeding, or else will print an error (see also <i>&#8211;resize-force</i>). </p>
<p> You can give this option multiple times.</p>
<dt><code>&#8211;resize-force part=size</code></p>
<dd> This is the same as <i>&#8211;resize</i> except that it will let you decrease the size of any partition. Generally this means you will lose any data which was at the end of the partition you shrink, but you may not care about that (eg. if shrinking an unused partition, or if you can easily recreate it such as a swap partition). </p>
<p> See also the <i>&#8211;ignore</i> option.</p>
<dt><code>&#8211;shrink part</code></p>
<dd> Shrink the named partition until the overall disk image fits in the destination. The named partition <code>must</code> contain a filesystem or <font SIZE="-1">PV</font> which has already been shrunk using another tool (eg. <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) or other online tools). Virt-resize will check this and give an error if it has not been done. </p>
<p> The amount by which the overall disk must be shrunk (after carrying out all other operations requested by the user) is called the &#8220;deficit&#8221;. For example, a straight copy (assume no other operations) from a 5GB disk image to a 4GB disk image results in a 1GB deficit. In this case, virt-resize would give an error unless the user specified a partition to shrink and that partition had more than a gigabyte of free space. </p>
<p> Note that you cannot use <i>&#8211;expand</i> and <i>&#8211;shrink</i> together.</p>
<dt><code>&#8211;unknown-filesystems ignore</code></p>
<dd>
<dt><code>&#8211;unknown-filesystems warn</code></p>
<dd>
<dt><code>&#8211;unknown-filesystems error</code></p>
<dd> Configure the behaviour of virt-resize when asking to expand a filesystem, and neither libguestfs has the support it, nor virt-resize knows how to expand the content of the filesystem. </p>
<p> <i>&#8211;unknown-filesystems ignore</i> will cause virt-resize to silently ignore such filesystems, and nothing is printed about them. </p>
<p> <i>&#8211;unknown-filesystems warn</i> (the default behaviour) will cause virt-resize to warn for each of the filesystem that cannot be expanded, but still continuing to resize the disk. </p>
<p> <i>&#8211;unknown-filesystems error</i> will cause virt-resize to error out at the first filesystem that cannot be expanded. </p>
<p> See also &#8220;unknown/unavailable method for expanding the <font SIZE="-1">TYPE</font> filesystem on <font SIZE="-1">DEVICE/LV&#8221;</font>.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable debugging messages.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dl>
<h2>MACHINE READABLE OUTPUT</h2>
<p> The <i>&#8211;machine-readable</i> option can be used to make the output more machine friendly, which is useful when calling virt-resize from other programs, GUIs etc. </p>
<p> There are two ways to use this option. </p>
<p> Firstly use the option on its own to query the capabilities of the virt-resize binary. Typical output looks like this: </p>
<pre>
 $ virt-resize --machine-readable
 virt-resize
 ntfsresize-force
 32bitok
 ntfs
 btrfs
</pre>
<p> A list of features is printed, one per line, and the program exits with status 0. </p>
<p> Secondly use the option in conjunction with other options to make the regular program output more machine friendly. </p>
<p> At the moment this means:</p>
<dl>
<dt>1.</p>
<dd> Progress bar messages can be parsed from stdout by looking for this regular expression: </p>
<pre><code>
^[0 - 9] + / [0 - 9] + $
</code></pre>
<dt>2.</p>
<dd> The calling program should treat messages sent to stdout (except for progress bar messages) as status messages. They can be logged and/or displayed to the user.</p>
<dt>3.</p>
<dd> The calling program should treat messages sent to stderr as error messages. In addition, virt-resize exits with a non-zero status code if there was a fatal error.</dl>
<p> Versions of the program prior to 1.13.9 did not support the <i>&#8211;machine-readable</i> option and will return an error.</p>
<h2>NOTES</h2>
<h3>Partition 1 does not end on cylinder boundary.</h3>
<p> Virt-resize aligns partitions to multiples of 128 sectors (see the <i>&#8211;alignment</i> parameter). Usually this means the partitions will not be aligned to the ancient <font SIZE="-1">CHS</font> geometry. However <font SIZE="-1">CHS</font> geometry is meaningless for disks manufactured since the early 1990s, and doubly so for virtual hard drives. Alignment of partitions to cylinders is not required by any modern operating system.</p>
<h3><font SIZE="-1">GUEST BOOT STUCK AT GRUB</font></h3>
<p> If a Linux guest does not boot after resizing, and the boot is stuck after printing <tt>&quot;GRUB&quot;</tt> on the console, try reinstalling grub. </p>
<pre>
 guestfish -i -a newdisk
 &gt;&lt;fs&gt; cat /boot/grub/device.map
 # check the contents of this file are sensible or
 # edit the file if necessary
 &gt;&lt;fs&gt; grub-install / /dev/vda
 &gt;&lt;fs&gt; exit
</pre>
<p> For more flexible guest reconfiguration, including if you need to specify other parameters to grub-install, use <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1).</p>
<h3><font SIZE="-1">RESIZING WINDOWS BOOT PARTITIONS</font></h3>
<p> In Windows Vista and later versions, Microsoft switched to using a separate boot partition. In these VMs, typically <i>/dev/sda1</i> is the boot partition and <i>/dev/sda2</i> is the main (C:) drive. Resizing the first (boot) partition causes the bootloader to fail with <tt>0xC0000225</tt> error. Resizing the second partition (ie. C: drive) should work.</p>
<h3><font SIZE="-1">WINDOWS CHKDSK</font></h3>
<p> Windows disks which use <font SIZE="-1">NTFS</font> must be consistent before virt-resize can be used. If the ntfsresize operation fails, try booting the original <font SIZE="-1">VM</font> and running <tt>&quot;chkdsk /f&quot;</tt> on all <font SIZE="-1">NTFS</font> partitions, then shut down the <font SIZE="-1">VM</font> cleanly. For further information see: <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=975753">https://bugzilla.redhat.com/show_bug.cgi?id=975753</a> </p>
<p> <i>After resize</i> Windows may initiate a lengthy &#8220;chkdsk&#8221; on first boot if <font SIZE="-1">NTFS</font> partitions have been expanded. This is just a safety check and (unless it find errors) is nothing to worry about.</p>
<h3><font SIZE="-1">WINDOWS UNMOUNTABLE_BOOT_VOLUME BSOD</font></h3>
<p> After sysprepping a Windows guest and then resizing it with virt-resize, you may see the guest fail to boot with an <tt>&quot;UNMOUNTABLE_BOOT_VOLUME&quot;</tt> <font SIZE="-1">BSOD. </font> This error is caused by having <tt>&quot;ExtendOemPartition=1&quot;</tt> in the sysprep.inf file. Removing this line before sysprepping should fix the problem.</p>
<h3><font SIZE="-1">WINDOWS 8</font></h3>
<p> Windows 8 &#8220;fast startup&#8221; can prevent virt-resize from resizing <font SIZE="-1">NTFS</font> partitions. See &#8220;<font SIZE="-1">WINDOWS HIBERNATION AND WINDOWS 8 FAST STARTUP&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h3><font SIZE="-1">SPARSE COPYING</font></h3>
<p> You should create a fresh, zeroed target disk image for virt-resize to use. </p>
<p> Virt-resize by default performs sparse copying. This means that it does not copy blocks from the source disk which are all zeroes. This improves speed and efficiency, but will produce incorrect results if the target disk image contains unzeroed data. </p>
<p> The main time this can be a problem is if the target is a host partition (eg. <tt>&quot;virt-resize source.img /dev/sda4&quot;</tt>) because the usual partitioning tools tend to leave whatever data happened to be on the disk before. </p>
<p> If you have to reuse a target which contains data already, you should use the <i>&#8211;no-sparse</i> option. Note this can be much slower.</p>
<h3>unknown/unavailable method for expanding the <font SIZE="-1">TYPE</font> filesystem on <font SIZE="-1">DEVICE/LV</font></h3>
<p> Virt-resize was asked to expand a partition or a logical volume containing a filesystem with the type <tt>&quot;TYPE&quot;</tt>, but there is no available nor known expanding method for that filesystem. </p>
<p> This may be due to either of the following:</p>
<dl>
<dt>1.</p>
<dd> There corresponding filesystem is not available in libguestfs, because there is no proper package in the host with utilities for it. This is usually the case for <tt>&quot;btrfs&quot;</tt>, <tt>&quot;ntfs&quot;</tt>, and <tt>&quot;xfs&quot;</tt> filesystems. </p>
<p> Check the results of: </p>
<pre>
 virt-resize --machine-readable
 guestfish -a /dev/null run : available
 guestfish -a /dev/null run : filesystem_available TYPE
</pre>
<p> In this case, it is enough to install the proper packages adding support for them. For example, <tt>&quot;libguestfs-xfs&quot;</tt> on Red Hat Enterprise Linux, CentOS, Debian, Ubuntu, and distributions derived from them, for supporting the <tt>&quot;xfs&quot;</tt> filesystem.</p>
<dt>2.</p>
<dd> Virt-resize has no support for expanding that type of filesystem. </p>
<p> In this case, there&#8217;s nothing that can be done to let virt-resize expand that type of filesystem.</dl>
<p> In both cases, virt-resize will not expand the mentioned filesystem; the result (unless <i>&#8211;unknown-filesystems error</i> is specified) is that the partitions containing such filesystems will be actually bigger as requested, but the filesystems will still be usable at the their older sizes.</p>
<h2>ALTERNATIVE TOOLS</h2>
<p> There are several proprietary tools for resizing partitions. We won&#8217;t mention any here. </p>
<p> <i><a href="/docs/linux/man/8-parted/">parted</a></i>(8) and its graphical shell gparted can do some types of resizing operations on disk images. They can resize and move partitions, but I don&#8217;t think they can do anything with the contents, and they certainly don&#8217;t understand <font SIZE="-1">LVM.</font> </p>
<p> <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) can do everything that virt-resize can do and a lot more, but at a much lower level. You will probably end up hand-calculating sector offsets, which is something that virt-resize was designed to avoid. If you want to see the guestfish-equivalent commands that virt-resize runs, use the <i>&#8211;debug</i> flag. </p>
<p> <i><a href="/docs/linux/man/8-dracut/">dracut</a></i>(8) includes a module called <tt>&quot;dracut-modules-growroot&quot;</tt> which can be used to grow the root partition when the guest first boots up. There is documentation for this module in an associated <font SIZE="-1">README</font> file.</p>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1), <i><a href="/docs/linux/man/1-virt-df/">virt-df</a></i>(1), <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/8-lvm/">lvm</a></i>(8), <i><a href="/docs/linux/man/8-pvresize/">pvresize</a></i>(8), <i><a href="/docs/linux/man/8-lvresize/">lvresize</a></i>(8), <i><a href="/docs/linux/man/8-resize2fs/">resize2fs</a></i>(8), <i><a href="/docs/linux/man/8-ntfsresize/">ntfsresize</a></i>(8), <i><a href="/docs/linux/man/8-btrfs/">btrfs</a></i>(8), <i><a href="/docs/linux/man/8-xfs_growfs/">xfs_growfs</a></i>(8), <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), <i><a href="/docs/linux/man/8-parted/">parted</a></i>(8), <i><a href="/docs/linux/man/1-truncate/">truncate</a></i>(1), <i><a href="/docs/linux/man/1-fallocate/">fallocate</a></i>(1), <i><a href="/docs/linux/man/8-grub/">grub</a></i>(8), <i><a href="/docs/linux/man/8-grub-install/">grub-install</a></i>(8), <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1), <i><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></i>(1), <i><a href="/docs/linux/man/1-virt-alignment-scan/">virt-alignment-scan</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010-2012 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAL">OPTIONS</a></p>
<dd>
<dt><a href="#lbAM">MACHINE READABLE OUTPUT</a></p>
<dd>
<dt><a href="#lbAN">NOTES</a></p>
<dd>
<dt><a href="#lbAW">ALTERNATIVE TOOLS</a></p>
<dd>
<dt><a href="#lbAX">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAY">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAZ">AUTHOR</a></p>
<dd>
<dt><a href="#lbBA">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbBB">LICENSE</a></p>
<dd>
<dt><a href="#lbBC">BUGS</a></p>
<dd></dl>
