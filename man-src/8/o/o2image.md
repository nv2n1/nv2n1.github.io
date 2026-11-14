---
title: "o2image(8)"
name: "o2image"
section: "8"
letter: "o"
url: "/docs/linux/man/8-o2image/"
description: "o2image – Copy or restore OCFS2 file system meta-data"
---

<p>o2image &#8211; Copy or restore <i>OCFS2</i> file system meta-data</p>
<h2>Synopsis</h2>
<p><code>o2image</code> [<code>-r</code>] [<code>-I</code>] <i>device</i> <i>image-file</i></p>
<h2>Description</h2>
<p><code>o2image</code> copies the <i>OCFS2</i> file system meta-data from the device to the specified image-file. This image file contains the file system skeleton that includes the inodes, directory names and file names. It does <code>not</code> include any file data. This image file can be useful to debug certain problems that are not reproducible otherwise. Like on-disk corruptions. It could also be used to analyse the file system layout in an aging file system with an eye towards improving performance. As the image-file contains a copy of all the meta-data blocks, it can be a large file. By default, it is created in a packed format, in which all meta-data blocks are written back-to-back. With the <code>-r</code> option, the user could choose to have the file in the raw (or sparse) format, in which the blocks are written to the same offset as they are on the device. <i>debugfs.ocfs2</i> understands both formats. <code>o2image</code> also has the option, <i>-I</i>, to restore the meta-data from the image file onto the device. This option will rarely be useful to end-users and has been written specifically for developers and testers. </p>
<h2>Options</h2>
<dl>
<dt><code>-r</code></p>
<dd>Copies the meta-data to the image-file in the raw format. Use this option only if the destination file system supports sparse files. If unsure, do not use this option and let the tool create the image-file in the packed format. </p>
<dt><code>-I</code></p>
<dd>Restores meta-data from the image-file onto the device. <code>CAUTION: This option could corrupt the file system.</code> </p>
</dl>
<h2>Examples</h2>
<table>
<tr VALIGN=top>
<td>[root [at] node1 ~]# o2image /dev/sda1 sda1.out
</td>
</tr>
<tr VALIGN=top>
<td>Copies metadata blocks from /dev/sda1 device to sda1.out file
</td>
</tr>
<tr VALIGN=top>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>[root [at] node1 ~] o2image -I /dev/sda1 sda1.out
</td>
</tr>
<tr VALIGN=top>
<td><code>Use with CAUTION</code>. Copies meta-data blocks from sda1.out onto the /dev/sda1 device.
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-debugfs-ocfs2/">debugfs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-fsck-ocfs2/">fsck.ocfs2</a>(8)</code> </p>
<h2>Authors</h2>
<p>Oracle Corporation</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007, 2009 Oracle. All rights reserved.</p>
