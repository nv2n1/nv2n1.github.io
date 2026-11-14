---
title: "virt-make-fs(1)"
name: "virt-make-fs"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-make-fs/"
description: "virt-make-fs – Make a filesystem from a tar archive or files"
---

<h2 class="name">NAME</h2>
<p> virt-make-fs &#8211; Make a filesystem from a tar archive or files </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - make - fs[--options] input.tar output.img virt - make - fs[--options] input.tar.gz output.img virt - make - fs[--options] directory output.img
</code></pre>
<h2>DESCRIPTION</h2>
<p> Virt-make-fs is a command line tool for creating a filesystem from a tar archive or some files in a directory. It is similar to tools like <i><a href="/docs/linux/man/1-mkisofs/">mkisofs</a></i>(1), <i><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></i>(1) and <i><a href="/docs/linux/man/1-mksquashfs/">mksquashfs</a></i>(1). Unlike those tools, it can create common filesystem types like ext2/3 or <font SIZE="-1">NTFS,</font> which can be useful if you want to attach these filesystems to existing virtual machines (eg. to import large amounts of read-only data to a <font SIZE="-1">VM</font>). </p>
<p> To create blank disks, use <i><a href="/docs/linux/man/1-virt-format/">virt-format</a></i>(1). To create complex layouts, use <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). </p>
<p> Basic usage is: </p>
<pre>
 virt-make-fs input output.img
</pre>
<p> where <tt>&quot;input&quot;</tt> is either a directory containing files that you want to add, or a tar archive (either uncompressed tar or gzip-compressed tar); and <i>output.img</i> is a disk image. The input type is detected automatically. The output disk image defaults to a raw ext2 sparse image unless you specify extra flags (see &#8220;<font SIZE="-1">OPTIONS&#8221;</font> below).</p>
<h3><font SIZE="-1">FILESYSTEM TYPE</font></h3>
<p> The default filesystem type is <tt>&quot;ext2&quot;</tt>. Just about any filesystem type that libguestfs supports can be used (but <i>not</i> read-only formats like <font SIZE="-1">ISO9660</font>). Here are some of the more common choices:</p>
<dl>
<dt><i>ext3</i></p>
<dd> Note that ext3 filesystems contain a journal, typically 1-32 <font SIZE="-1">MB</font> in size. If you are not going to use the filesystem in a way that requires the journal, then this is just wasted overhead.</p>
<dt><i>ntfs</i> or <i>vfat</i></p>
<dd> Useful if exporting data to a Windows guest.</p>
<dt><i>minix</i></p>
<dd> Lower overhead than <tt>&quot;ext2&quot;</tt>, but certain limitations on filename length and total filesystem size.</dl>
<p> <i></i><font SIZE="-1"><i>EXAMPLE</i></font><i></i> </p>
<pre>
 virt-make-fs --type=minix input minixfs.img
</pre>
<h3><font SIZE="-1">TO PARTITION OR NOT TO PARTITION</font></h3>
<p> Optionally virt-make-fs can add a partition table to the output disk. </p>
<p> Adding a partition can make the disk image more compatible with certain virtualized operating systems which don&#8217;t expect to see a filesystem directly located on a block device (Linux doesn&#8217;t care and will happily handle both types). </p>
<p> On the other hand, if you have a partition table then the output image is no longer a straight filesystem. For example you cannot run <i><a href="/docs/linux/man/8-fsck/">fsck</a></i>(8) directly on a partitioned disk image. (However libguestfs tools such as <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) and <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1) can still be used). </p>
<p> <i></i><font SIZE="-1"><i>EXAMPLE</i></font><i></i> </p>
<p> Add an <font SIZE="-1">MBR</font> partition: </p>
<pre>
 virt-make-fs --partition -- input disk.img
</pre>
<p> If the output disk image could be terabyte-sized or larger, it&#8217;s better to use an EFI/GPT-compatible partition table: </p>
<pre>
 virt-make-fs --partition=gpt --size=+4T --format=qcow2 input disk.img
</pre>
<h3><font SIZE="-1">EXTRA SPACE</font></h3>
<p> Unlike formats such as tar and squashfs, a filesystem does not &#8220;just fit&#8221; the files that it contains, but might have extra space. Depending on how you are going to use the output, you might think this extra space is wasted and want to minimize it, or you might want to leave space so that more files can be added later. Virt-make-fs defaults to minimizing the extra space, but you can use the <i>&#8211;size</i> flag to leave space in the filesystem if you want it. </p>
<p> An alternative way to leave extra space but not make the output image any bigger is to use an alternative disk image format (instead of the default &#8220;raw&#8221; format). Using <i>&#8211;format=qcow2</i> will use the native qemu/KVM qcow2 image format (check your hypervisor supports this before using it). This allows you to choose a large <i>&#8211;size</i> but the extra space won&#8217;t actually be allocated in the image until you try to store something in it. </p>
<p> Don&#8217;t forget that you can also use local commands including <i><a href="/docs/linux/man/8-resize2fs/">resize2fs</a></i>(8) and <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1) to resize existing filesystems, or rerun virt-make-fs to build another image from scratch. </p>
<p> <i></i><font SIZE="-1"><i>EXAMPLE</i></font><i></i> </p>
<pre>
 virt-make-fs --format=qcow2 --size=+200M input output.img
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>&#8211;floppy</code></p>
<dd> Create a virtual floppy disk. </p>
<p> Currently this preselects the size (1440K), partition type (<font SIZE="-1">MBR</font>) and filesystem type (<font SIZE="-1">VFAT</font>). In future it may also choose the geometry.</p>
<dt><code>&#8211;size=&lt;N&gt;</code></p>
<dd>
<dt><code>&#8211;size=+&lt;N&gt;</code></p>
<dd>
<dt><code>-s &lt;N&gt;</code></p>
<dd>
<dt><code>-s +&lt;N&gt;</code></p>
<dd> Use the <i>&#8211;size</i> (or <i>-s</i>) option to choose the size of the output image. </p>
<p> If this option is <i>not</i> given, then the output image will be just large enough to contain all the files, with not much wasted space. </p>
<p> To choose a fixed size output disk, specify an absolute number followed by b/K/M/G/T/P/E to mean bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Petabytes or Exabytes. This must be large enough to contain all the input files, else you will get an error. </p>
<p> To leave extra space, specify <tt>&quot;+&quot;</tt> (plus sign) and a number followed by b/K/M/G/T/P/E to mean bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Petabytes or Exabytes. For example: <i>&#8211;size=+200M</i> means enough space for the input files, and (approximately) an extra 200 <font SIZE="-1">MB</font> free space. </p>
<p> Note that virt-make-fs estimates free space, and therefore will not produce filesystems containing precisely the free space requested. (It is much more expensive and time-consuming to produce a filesystem which has precisely the desired free space).</p>
<dt><code>&#8211;format=&lt;fmt&gt;</code></p>
<dd>
<dt><code>-F &lt;fmt&gt;</code></p>
<dd> Choose the output disk image format. </p>
<p> The default is <tt>&quot;raw&quot;</tt> (raw sparse disk image).</p>
<dt><code>&#8211;type=&lt;fs&gt;</code></p>
<dd>
<dt><code>-t &lt;fs&gt;</code></p>
<dd> Choose the output filesystem type. </p>
<p> The default is <tt>&quot;ext2&quot;</tt>. </p>
<p> Any filesystem which is supported read-write by libguestfs can be used here.</p>
<dt><code>&#8211;label=&lt;</code><font SIZE="-1"><code>LABEL</code></font><code>&gt;</code></p>
<dd> Set the filesystem label.</p>
<dt><code>&#8211;partition</code></p>
<dd>
<dt><code>&#8211;partition=&lt;parttype&gt;</code></p>
<dd> If specified, this flag adds an <font SIZE="-1">MBR</font> partition table to the output disk image. </p>
<p> You can change the partition table type, eg. <i>&#8211;partition=gpt</i> for large disks. </p>
<p> For <font SIZE="-1">MBR,</font> virt-make-fs sets the partition type byte automatically.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable debugging information.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-x</code></p>
<dd> Enable libguestfs trace.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-format/">virt-format</a></i>(1), <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar-in/">virt-tar-in</a></i>(1), <i><a href="/docs/linux/man/1-mkisofs/">mkisofs</a></i>(1), <i><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></i>(1), <i><a href="/docs/linux/man/1-mksquashfs/">mksquashfs</a></i>(1), <i><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></i>(8), <i><a href="/docs/linux/man/8-resize2fs/">resize2fs</a></i>(8), <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010-2016 Red Hat Inc.</p>
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
<dt><a href="#lbAH">OPTIONS</a></p>
<dd>
<dt><a href="#lbAI">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAJ">AUTHOR</a></p>
<dd>
<dt><a href="#lbAK">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAL">LICENSE</a></p>
<dd>
<dt><a href="#lbAM">BUGS</a></p>
<dd></dl>
