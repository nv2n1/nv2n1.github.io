---
title: "sd(4)"
name: "sd"
section: "4"
letter: "s"
url: "/docs/linux/man/4-sd/"
description: "sd – driver for SCSI disk drives"
---

<p>sd &#8211; driver for SCSI disk drives</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/hdreg.h&gt; </code>/* for HDIO_GETGEO */
<code>#include &lt;linux/fs.h&gt; </code>/* for BLKGETSIZE and BLKRRPART */</pre>
<h2>Configuration</h2>
<p>The block device name has the following form: <code>sd</code><i>lp,</i> where <i>l</i> is a letter denoting the physical drive, and <i>p</i> is a number denoting the partition on that physical drive. Often, the partition number, <i>p</i>, will be left off when the device corresponds to the whole drive. </p>
<p> SCSI disks have a major device number of 8, and a minor device number of the form (16 * <i>drive_number</i>) + <i>partition_number</i>, where <i>drive_number</i> is the number of the physical drive in order of detection, and <i>partition_number</i> is as follows:</p>
<dl>
<dt>+3</p>
<dd>partition 0 is the whole drive</p>
<dd>partitions 1-4 are the DOS &quot;primary&quot; partitions</p>
<dd>partitions 5-8 are the DOS &quot;extended&quot; (or &quot;logical&quot;) partitions</dl>
<p> For example, <i>/dev/sda</i> will have major 8, minor 0, and will refer to all of the first SCSI drive in the system; and <i>/dev/sdb3</i> will have major 8, minor 19, and will refer to the third DOS &quot;primary&quot; partition on the second SCSI drive in the system. </p>
<p> At this time, only block devices are provided. Raw devices have not yet been implemented.</p>
<h2>Description</h2>
<p>The following <i>ioctl</i>s are provided:</p>
<dl>
<dt><code>HDIO_GETGEO</code></p>
<dd>Returns the BIOS disk parameters in the following structure:</dl>
<pre><code>struct hd_geometry {
    unsigned char heads;
    unsigned char sectors;
    unsigned short cylinders;
    unsigned long start;
};

A pointer to this structure is passed as the
ioctl(2)

parameter.

The information returned in the parameter is the disk geometry of the drive
as understood by DOS!

This geometry is
not

the physical geometry of the drive.
It is used when constructing the
drive's partition table, however, and is needed for convenient operation
of
fdisk(1),

efdisk(1),

and
lilo(1).

If the geometry information is not available, zero will be returned for all
of the parameters.
BLKGETSIZE


Returns the device size in sectors.
The
ioctl(2)

parameter should be a pointer to a
long.

BLKRRPART


Forces a reread of the SCSI disk partition tables.
No parameter is needed.

The SCSI
ioctl(2)

operations are also supported.
If the
ioctl(2)

parameter is required, and it is NULL, then
ioctl(2)

fails with the error
EINVAL.</code></pre>
<h2>Files</h2>
<dl>
<dt><i>/dev/sd[a-h]</i></p>
<dd>the whole device</p>
<dt><i>/dev/sd[a-h][0-8]</i></p>
<dd>individual block partitions</dl>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
