---
title: "mkfs(1)"
name: "mkfs"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkfs/"
description: "mkfs.jffs2 – Create a JFFS2 file system image from directory"
---

<h2>NAME</h2>
<p> mkfs.jffs2 &#8211; Create a JFFS2 file system image from directory</p>
<h2>SYNOPSIS</h2>
<p> <code>mkfs.jffs2</code> [ <code>-p,&#8211;pad[=SIZE]</code> ] [ <code>-r,-d,&#8211;root</code> <i>directory</i> ] [ <code>-s,&#8211;pagesize=SIZE</code> ] [ <code>-e,&#8211;eraseblock=SIZE</code> ] [ <code>-c,&#8211;cleanmarker=SIZE</code> ] [ <code>-n,&#8211;no-cleanmarkers</code> ] [ <code>-o,&#8211;output</code> <i>image.jffs2</i> ] [ <code>-l,&#8211;little-endian</code> ] [ <code>-b,&#8211;big-endian</code> ] [ <code>-D,&#8211;devtable=FILE</code> ] [ <code>-f,&#8211;faketime</code> ] [ <code>-q,&#8211;squash</code> ] [ <code>-U,&#8211;squash-uids</code> ] [ <code>-P,&#8211;squash-perms</code> ] [ <code>&#8211;with-xattr</code> ] [ <code>&#8211;with-selinux</code> ] [ <code>&#8211;with-posix-acl</code> ] [ <code>-m,&#8211;compression-mode=MODE</code> ] [ <code>-x,&#8211;disable-compressor=NAME</code> ] [ <code>-X,&#8211;enable-compressor=NAME</code> ] [ <code>-y,&#8211;compressor-priority=PRIORITY:NAME</code> ] [ <code>-L,&#8211;list-compressors</code> ] [ <code>-t,&#8211;test-compression</code> ] [ <code>-h,&#8211;help</code> ] [ <code>-v,&#8211;verbose</code> ] [ <code>-V,&#8211;version</code> ] [ <code>-i,&#8211;incremental</code> <i>image.jffs2</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The program <code>mkfs.jffs2</code> creates a JFFS2 (Second Journalling Flash File System) file system image and writes the resulting image to the file specified by the <code>-o</code> option or by default to the standard output, unless the standard output is a terminal device in which case mkfs.jffs2 will abort. </p>
<p> The file system image is created using the files and directories contained in the directory specified by the option <code>-r</code> or the present directory, if the <code>-r</code> option is not specified. </p>
<p> Each block of the files to be placed into the file system image are compressed using one of the avaiable compressors depending on the selected compression mode. </p>
<p> File systems are created with the same endianness as the host, unless the <code>-b</code> or <code>-l</code> options are specified. JFFS2 driver in the 2.4 Linux kernel only supported images having the same endianness as the CPU. As of 2.5.48, the kernel can be changed with a #define to accept images of the non-native endianness. Full bi-endian support in the kernel is not planned. </p>
<p> It is unlikely that JFFS2 images are useful except in conjuction with the MTD (Memory Technology Device) drivers in the Linux kernel, since the JFFS2 file system driver in the kernel requires MTD devices.</p>
<h2>OPTIONS</h2>
<p> Options that take SIZE arguments can be specified as either decimal (e.g., 65536), octal (0200000), or hexidecimal (0x1000).</p>
<dl>
<dt><code>-p, &#8211;pad[=SIZE]</code></p>
<dd> Pad output to SIZE bytes with 0xFF. If SIZE is not specified, the output is padded to the end of the final erase block.</p>
<dt><code>-r, -d, &#8211;root=DIR</code></p>
<dd> Build file system from directory DIR. The default is the current directory.</p>
<dt><code>-s, &#8211;pagesize=SIZE</code></p>
<dd> Use page size SIZE. The default is 4 KiB. This size is the maximum size of a data node.</p>
<dt><code>-e, &#8211;eraseblock=SIZE</code></p>
<dd> Use erase block size SIZE. The default is 64 KiB. If you use a erase block size different than the erase block size of the target MTD device, JFFS2 may not perform optimally. If the SIZE specified is below 4096, the units are assumed to be KiB.</p>
<dt><code>-c, &#8211;cleanmarker=SIZE</code></p>
<dd> Write &#8216;CLEANMARKER&#8217; nodes with the size specified. It is not normally appropriate to specify a size other than the default 12 bytes.</p>
<dt><code>-n, &#8211;no-cleanmarkers</code></p>
<dd> Do not write &#8216;CLEANMARKER&#8217; nodes to the beginning of each erase block. This option can be useful for creating JFFS2 images for use on NAND flash, and for creating images which are to be used on a variety of hardware with differing eraseblock sizes.</p>
<dt><code>-o, &#8211;output=FILE</code></p>
<dd> Write JFFS2 image to file FILE. Default is the standard output.</p>
<dt><code>-l, &#8211;little-endian</code></p>
<dd> Create a little-endian JFFS2 image. Default is to make an image with the same endianness as the host.</p>
<dt><code>-b, &#8211;big-endian</code></p>
<dd> Create a big-endian JFFS2 image. Default is to make an image with the same endianness as the host.</p>
<dt><code>-D, &#8211;devtable=FILE</code></p>
<dd> Use the named FILE as a device table file, for including devices and changing permissions in the created image when the user does not have appropriate permissions to create them on the file system used as source.</p>
<dt><code>-f, &#8211;faketime</code></p>
<dd> Change all file timestamps to &#8216;0&#8217; for regression testing.</p>
<dt><code>-q, &#8211;squash</code></p>
<dd> Squash permissions and owners, making all files be owned by root and removing write permission for &#8216;group&#8217; and &#8216;other&#8217;.</p>
<dt><code>-U, &#8211;squash-uids</code></p>
<dd> Squash owners making all files be owned by root.</p>
<dt><code>-P, &#8211;squash-perms</code></p>
<dd> Squash permissions, removing write permission for &#8216;group&#8217; and &#8216;other&#8217;.</p>
<dt><code>&#8211;with-xattr</code></p>
<dd> Enables xattr, stuff all xattr entries into jffs2 image file.</p>
<dt><code>&#8211;with-selinux</code></p>
<dd> Enables xattr, stuff only SELinux Labels into jffs2 image file.</p>
<dt><code>&#8211;with-posix-acl</code></p>
<dd> Enable xattr, stuff only POSIX ACL entries into jffs2 image file.</p>
<dt><code>-m, &#8211;compression-mode=MODE</code></p>
<dd> Set the default compression mode. The default mode is <code>priority </code> which tries the compressors in a predefinied order and chooses the first successful one. The alternatives are: <code>none</code> (mkfs will not compress) and <code>size</code> (mkfs will try all compressor and chooses the one which have the smallest result).</p>
<dt><code>-x, &#8211;disable-compressor=NAME</code></p>
<dd> Disable a compressor. Use <code>-L</code> to see the list of the avaiable compressors and their default states.</p>
<dt><code>-X, &#8211;enable-compressor=NAME</code></p>
<dd> Enable a compressor. Use <code>-L</code> to see the list of the avaiable compressors and their default states.</p>
<dt><code>-y, &#8211;compressor-priority=PRIORITY:NAME</code></p>
<dd> Set the priority of a compressor. Use <code>-L</code> to see the list of the avaiable compressors and their default priority. Priorities are used by priority compression mode.</p>
<dt><code>-L, &#8211;list-compressors</code></p>
<dd> Show the list of the avaiable compressors and their states.</p>
<dt><code>-t, &#8211;test-compression</code></p>
<dd> Call decompress after every compress &#8211; and compare the result with the original data -, and some other check.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help text.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Verbose operation.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>-i, &#8211;incremental=FILE</code></p>
<dd> Generate an appendage image for FILE. If FILE is written to flash and flash is appended with the output, then it seems as if it was one thing. </p>
</dl>
<h2>LIMITATIONS</h2>
<p> The format and grammar of the device table file does not allow it to create symbolic links when the symbolic links are not already present in the root working directory. </p>
<p> However, symbolic links may be specified in the device table file using the <i>l</i> type for the purposes of setting their permissions and ownership.</p>
<h2>BUGS</h2>
<p> JFFS2 limits device major and minor numbers to 8 bits each. Some consider this a bug. </p>
<p> <code>mkfs.jffs2</code> does not properly handle hard links in the input directory structure. Currently, hard linked files will be expanded to multiple identical files in the output image.</p>
<h2>AUTHORS</h2>
<p> David Woodhouse<br />
 Manual page written by David Schleef &lt;ds [at] schleef.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/1-mkfs-jffs/">mkfs.jffs</a></code>(1), <code><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></code>(1) </p>
<h2>Index</h2>
