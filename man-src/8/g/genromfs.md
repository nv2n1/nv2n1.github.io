---
title: "genromfs(8)"
name: "genromfs"
section: "8"
letter: "g"
url: "/docs/linux/man/8-genromfs/"
description: "genromfs – create a romfs image"
---

<p>genromfs &#8211; create a romfs image</p>
<h2>Synopsis</h2>
<p><code>genromfs</code> <code>-f device</code> [ <code>-d source</code> ] [ <code>-V label</code> ] [ <code>-a alignment</code> ] [ <code>-A alignment,pattern</code> ] [ <code>-x pattern</code> ] [ <code>-v</code> ]</p>
<h2>Description</h2>
<p><code>genromfs</code> is used to create a romfs file system image, usually directly on a block device, or for test purposes, in a plain file. It is the <i>mkfs</i> equivalent of other filesystems. <code>genromfs</code> will scan the current directory and its subdirectories, build a romfs image from the files found, and output it to the file or device you specified. During scanning, it recognizes a special notation. If a file begins with the @ sign (and is empty otherwise), it refers to a device special node in the format: <code>@name,type,major,minor.</code> type can be <i>b</i> for block devices, <i>c</i> for character devices, and <i>p</i> for fifos. The linux virtual console 1 can thus be included as a file with the name: <code>@tty1,c,4,1</code> </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code><i>&nbsp;<wbr>output</i></p>
<dd>Specifies the file to output the image to. This option is required.</p>
<dt><code>-d</code><i>&nbsp;<wbr>source</i></p>
<dd>Use the specified directory as the source, not the current directory.</p>
<dt><code>-V</code><i>&nbsp;<wbr>label</i></p>
<dd>Build the image with the specified volume label. Currently it is not used by the kernel, but it will be recorded in the image.</p>
<dt><code>-a</code><i>&nbsp;<wbr>alignment</i></p>
<dd>Align regular files to a larger boundary. <code>genromfs</code> will align data of each regular file in the resulting image to the specified alignment, while keeping the image compatible with the original romfs definition (by adding pad bytes between last node before the file and file&#8217;s header). By default, <code>genromfs</code> will guarantee only an alignment of 16 bytes.</p>
<dt><code>-A</code><i>&nbsp;<wbr>alignment,pattern</i></p>
<dd>Align objects matching shell wildcard pattern to alignment bytes. If one object matches more patterns, then the highest alignment is chosen. Alignment has to be a power of two. Patterns either don&#8217;t contain any slashes, in which case files matching those patterns are matched in all directories, or start with a leading slash, in which case they are matched against absolute paths inside of the romfs filesystem (that is, as if you chrooted into the rom filesystem).</p>
<dt><code>-x</code><i>&nbsp;<wbr>pattern</i></p>
<dd>Allow to exclude files that match a pattern. It&#8217;s useful to exclude CVS directories and backup files (ending in a &#8216;~&#8217;).</p>
<dt><code>-v</code></p>
<dd>Verbose operation, <code>genromfs</code> will print each file which is included in the image, along with its offset.</dl>
<h2>Examples</h2>
<p><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>genromfs -d root -f&nbsp;<wbr>/dev/fd0 -V&nbsp;<wbr>&#8216;Secret labs install disk&#8217;</code> All files in the <i>root</i> directory will be written to <code>/dev/fd0</code> as a new romfs filesystem image. <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>genromfs -d root -f&nbsp;<wbr>/dev/fd0 -A 2048,/.. -A&nbsp;<wbr>&#8216;4096,*.boot&#8217;&nbsp;<wbr>-a 512 -V&nbsp;<wbr>&#8216;Bootable floppy&#8217;</code> Generate the image and place file data of all regular files on 512 bytes boundaries or on 4K boundaries, if they have the .boot extension. Additionally, align the romfs header of the &#8216;..&#8217; entry in the root directory on a 2K boundary. Effectively, this makes sure that the romfs image uses the least possible space in the first 2048 bytes. You can use the generated image (if you have the romfs module loaded, or compiled into the kernel) via: <code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mount -t romfs&nbsp;<wbr>/dev/fd0&nbsp;<wbr>/mnt</code> </p>
<h2>Author</h2>
<p>This manual page was initially written by Christoph Lameter &lt;clameter [at] debian.org&gt;, for the Debian GNU/Linux system.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-mkisofs/">mkisofs</a></code>(8) </p>
