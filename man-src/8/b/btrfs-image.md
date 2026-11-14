---
title: "btrfs-image(8)"
name: "btrfs-image"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-image/"
description: "btrfs-image – create/restore an image of the filesystem"
---

<p>btrfs-image &#8211; create/restore an image of the filesystem</p>
<h2>Synopsis</h2>
<p><code>btrfs-image</code> [options] <i>&lt;source&gt;</i> <i>&lt;target&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs-image</code> is used to create an image of a btrfs filesystem. All data will be zeroed, but metadata and the like is preserved. Mainly used for debugging purposes. </p>
<p> In the dump mode, source is the btrfs device/file and target is the output file (use <i>&#8211;</i> for stdout). </p>
<p> In the restore mode (option -r), source is the dumped image and target is the btrfs device/file.</p>
<h2>Options</h2>
<p>-r</p>
<dl>
<dd>Restore metadump image. By default, this fixes super&#8217;s chunk tree, by using 1 stripe pointing to primary device, so that file system can be restored by running tree log reply if possible. To restore without changing number of stripes in chunk tree check -o option.</dl>
<p> -c <i>&lt;value&gt;</i></p>
<dl>
<dd>Compression level (0 ~ 9).</dl>
<p> -t <i>&lt;value&gt;</i></p>
<dl>
<dd>Number of threads (1 ~ 32) to be used to process the image dump or restore.</dl>
<p> -o</p>
<dl>
<dd>Use the old restore method, this does not fixup the chunk tree so the restored file system will not be able to be mounted.</dl>
<p> -s</p>
<dl>
<dd>Sanitize the file names when generating the image. One -s means just generate random garbage, which means that the directory indexes won&#8217;t match up since the hashes won&#8217;t match with the garbage filenames. Using -ss will calculate a collision for the filename so that the hashes match, and if it can&#8217;t calculate a collision then it will just generate garbage. The collision calculator is very time and CPU intensive so only use it if you are having problems with your file system tree and need to have it mostly working.</dl>
<p> -w</p>
<dl>
<dd>Walk all the trees manually and copy any blocks that are referenced. Use this option if your extent tree is corrupted to make sure that all of the metadata is captured.</dl>
<p> -m</p>
<dl>
<dd>Restore for multiple devices, more than 1 device should be provided.</dl>
<h2>Exit Status</h2>
<p><code>btrfs-image</code> will return 0 if no error happened. If any problems happened, 1 will be returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) </p>
