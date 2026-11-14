---
title: "e2image(8)"
name: "e2image"
section: "8"
letter: "e"
url: "/docs/linux/man/8-e2image/"
description: "e2image – Save critical ext2/ext3/ext4 file system metadata to a file"
---

<p>e2image &#8211; Save critical ext2/ext3/ext4 file system metadata to a file</p>
<h2>Synopsis</h2>
<p><code>e2image</code> [<code>-r</code>|<code>-Q</code> [<code>-af</code>]] [ <code>-b</code> <i>superblock</i> ] [ <code>-B</code> <i>blocksize</i> ] [ <code>-cnps</code> ] [ <code>-o</code> <i>src_offset</i> ] [ <code>-O</code> <i>dest_offset</i> ] <i>device</i> <i>image-file</i><br />
 <code>e2image</code> <code>-I</code> <i>device</i> <i>image-file</i> </p>
<h2>Description</h2>
<p>The <code>e2image</code> program will save critical ext2, ext3, or ext4 file system metadata located on <i>device</i> to a file specified by <i>image-file</i>. The image file may be examined by <code>dumpe2fs</code> and <code>debugfs</code>, by using the <code>-i</code> option to those programs. This can assist an expert in recovering catastrophically corrupted file systems. It is a very good idea to create image files for all file systems on a system and save the partition layout (which can be generated using the <code>fdisk -l</code> command) at regular intervals &#8212; at boot time, and/or every week or so. The image file should be stored on some file system other than the file system whose data it contains, to ensure that this data is accessible in the case where the file system has been badly damaged. To save disk space, <code>e2image</code> creates the image file as a sparse file, or in QCOW2 format. Hence, if the sparse image file needs to be copied to another location, it should either be compressed first or copied using the <code>&#8211;sparse=always</code> option to the GNU version of <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1). This does not apply to the QCOW2 image, which is not sparse. The size of an ext2 image file depends primarily on the size of the file systems and how many inodes are in use. For a typical 10 Gigabyte file system, with 200,000 inodes in use out of 1.2 million inodes, the image file will be approximately 35 Megabytes; a 4 Gigabyte file system with 15,000 inodes in use out of 550,000 inodes will result in a 3 Megabyte image file. Image files tend to be quite compressible; an image file taking up 32 Megabytes of space on disk will generally compress down to 3 or 4 Megabytes. If <i>image-file</i> is <code>&#8211;</code>, then the output of <code>e2image</code> will be sent to standard output, so that the output can be piped to another program, such as <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1). (Note that this is currently only supported when creating a raw image file using the <code>-r</code> option, since the process of creating a normal image file, or QCOW2 image currently requires random access to the file, which cannot be done using a pipe. </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Include file data in the image file. Normally <code>e2image</code> only includes fs metadata, not regular file data. This option will produce an image that is suitable to use to clone the entire FS or for backup purposes. Note that this option only works with the raw (<i>-r</i>) or QCOW2 (<i>-Q</i>) formats. In conjunction with the <code>-r</code> option it is possible to clone all and only the used blocks of one file system to another device/image file.</p>
<dt><code>-b</code><i> superblock</i></p>
<dd>Get image from partition with broken primary superblock by using the superblock located at file system block number <i>superblock</i>. The partition is copied as-is including broken primary superblock.</p>
<dt><code>-B</code><i> blocksize</i></p>
<dd>Set the file system blocksize in bytes. Normally, <code>e2image</code> will search for the superblock at various different block sizes in an attempt to find the appropriate blocksize. This search can be fooled in some cases. This option forces e2fsck to only try locating the superblock with a particular blocksize. If the superblock is not found, e2image will terminate with a fatal error.</p>
<dt><code>-c</code></p>
<dd>Compare each block to be copied from the source <i>device</i> to the corresponding block in the target <i>image-file</i>. If both are already the same, the write will be skipped. This is useful if the file system is being cloned to a flash-based storage device (where reads are very fast and where it is desirable to avoid unnecessary writes to reduce write wear on the device).</p>
<dt><code>-f</code></p>
<dd>Override the read-only requirement for the source file system when saving the image file using the <code>-r</code> and <code>-Q</code> options. Normally, if the source file system is in use, the resulting image file is very likely not going to be useful. In some cases where the source file system is in constant use this may be better than no image at all.</p>
<dt><code>-I</code></p>
<dd>install the metadata stored in the image file back to the device. It can be used to restore the file system metadata back to the device in emergency situations.</dl>
<p> <code>WARNING!!!!</code> The <code>-I</code> option should only be used as a desperation measure when other alternatives have failed. If the file system has changed since the image file was created, data <code>will</code> be lost. In general, you should make another full image backup of the file system first, in case you wish to try other recovery strategies afterward.</p>
<dl>
<dt><code>-n</code></p>
<dd>Cause all image writes to be skipped, and instead only print the block numbers that would have been written.</p>
<dt><code>-o</code><i> src_offset</i></p>
<dd>Specify offset of the image to be read from the start of the source <i>device</i> in bytes. See <code>OFFSETS</code> for more details.</p>
<dt><code>-O</code><i> tgt_offset</i></p>
<dd>Specify offset of the image to be written from the start of the target <i>image-file</i> in bytes. See <code>OFFSETS</code> for more details.</p>
<dt><code>-p</code></p>
<dd>Show progress of image-file creation.</p>
<dt><code>-Q</code></p>
<dd>Create a QCOW2-format image file instead of a normal image file, suitable for use by virtual machine images, and other tools that can use the <code>.qcow</code> image format. See <code>QCOW2 IMAGE FILES</code> below for details.</p>
<dt><code>-r</code></p>
<dd>Create a raw image file instead of a normal image file. See <code>RAW IMAGE FILES</code> below for details.</p>
<dt><code>-s</code></p>
<dd>Scramble directory entries and zero out unused portions of the directory blocks in the written image file to avoid revealing information about the contents of the file system. However, this will prevent analysis of problems related to hash-tree indexed directories. </p>
</dl>
<h2>Raw Image Files</h2>
<p>The <code>-r</code> option will create a raw image file, which differs from a normal image file in two ways. First, the file system metadata is placed in the same relative offset within <i>image-file</i> as it is in the <i>device</i> so that <code><a href="/docs/linux/man/8-debugfs/">debugfs</a></code>(8), <code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8), <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-losetup/">losetup</a></code>(8), etc. and can be run directly on the raw image file. In order to minimize the amount of disk space consumed by the raw image file, it is created as a sparse file. (Beware of copying or compressing/decompressing this file with utilities that don&#8217;t understand how to create sparse files; the file will become as large as the file system itself!) Secondly, the raw image file also includes indirect blocks and directory blocks, which the standard image file does not have. </p>
<p> Raw image files are sometimes used when sending file systems to the maintainer as part of bug reports to e2fsprogs. When used in this capacity, the recommended command is as follows (replace <code>hda1</code> with the appropriate device for your system): </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><code>e2image -r /dev/hda1 &#8211; | bzip2 &gt; hda1.e2i.bz2</code></p>
<p> This will only send the metadata information, without any data blocks. However, the filenames in the directory blocks can still reveal information about the contents of the file system that the bug reporter may wish to keep confidential. To address this concern, the <code>-s</code> option can be specified to scramble the filenames in the image. </p>
<p> Note that this will work even if you substitute <code>/dev/hda1</code> for another raw disk image, or QCOW2 image previously created by <code>e2image</code>.</p>
<h2>Qcow2 Image Files</h2>
<p>The <code>-Q</code> option will create a QCOW2 image file instead of a normal, or raw image file. A QCOW2 image contains all the information the raw image does, however unlike the raw image it is not sparse. The QCOW2 image minimize the amount of space used by the image by storing it in special format which packs data closely together, hence avoiding holes while still minimizing size. </p>
<p> In order to send file system to the maintainer as a part of bug report to e2fsprogs, use following commands (replace <code>hda1</code> with the appropriate device for your system): </p>
<p> <code>e2image -Q /dev/hda1 hda1.qcow2</code><br />
 <code>bzip2 -z hda1.qcow2</code> </p>
<p> This will only send the metadata information, without any data blocks. As described for <code>RAW IMAGE FILES</code> the <code>-s</code> option can be specified to scramble the file system names in the image. </p>
<p> Note that the QCOW2 image created by <code>e2image</code> is a regular QCOW2 image and can be processed by tools aware of QCOW2 format such as for example <code>qemu-img</code>. </p>
<p> You can convert a .qcow2 image into a raw image with: </p>
<p> <code>e2image -r hda1.qcow2 hda1.raw</code> </p>
<p> This can be useful to write a QCOW2 image containing all data to a sparse image file where it can be loop mounted, or to a disk partition. Note that this may not work with QCOW2 images not generated by e2image.</p>
<h2>Offsets</h2>
<p>Normally a file system starts at the beginning of a partition, and <code>e2image</code> is run on the partition. When working with image files, you don&#8217;t have the option of using the partition device, so you can specify the offset where the file system starts directly with the <code>-o</code> option. Similarly the <code>-O</code> option specifies the offset that should be seeked to in the destination before writing the file system. </p>
<p> For example, if you have a <code>dd</code> image of a whole hard drive that contains an ext2 fs in a partition starting at 1 MiB, you can clone that image to a block device with: </p>
<p> <code>e2image -aro 1048576 img /dev/sda1</code> </p>
<p> Or you can clone a file system from a block device into an image file, leaving room in the first MiB for a partition table with: </p>
<p> <code>e2image -arO 1048576 /dev/sda1 img</code> </p>
<p> If you specify at least one offset, and only one file, an in-place move will be performed, allowing you to safely move the file system from one offset to another.</p>
<h2>Author</h2>
<p><code>e2image</code> was written by Theodore Ts&#8217;o (tytso [at] mit.edu).</p>
<h2>Availability</h2>
<p><code>e2image</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8), <code><a href="/docs/linux/man/8-debugfs/">debugfs</a></code>(8) <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) </p>
