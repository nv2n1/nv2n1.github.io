---
title: "gfs_grow(8)"
name: "gfs_grow"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs_grow/"
description: "gfs_grow – Expand a GFS filesystem"
---

<p>gfs_grow &#8211; Expand a GFS filesystem</p>
<h2>Synopsis</h2>
<p><code>gfs_grow</code> [<i>OPTION</i>]&#8230; &lt;<i>DEVICE</i>|<i>MOINTPOINT</i>&gt;&#8230; </p>
<h2>Description</h2>
<p>gfs_grow is used to expand a GFS filesystem after the device upon which the filesystem resides has also been expanded. By running gfs_grow on a GFS filesystem, you are requesting that any spare space between the current end of the filesystem and the end of the device is filled with a newly initialized GFS filesystem extension. When this operation is complete, the resource index for the filesystem is updated so that all nodes in the cluster can use the extra storage space which has been added. You may only run gfs_grow on a mounted filesystem; expansion of unmounted filesystems is not supported. You only need to run gfs_grow on one node in the cluster. All the other nodes will see the expansion has occurred and automatically start to use the newly available space. You must be superuser to execute <code>gfs_grow</code>. The gfs_grow tool tries to prevent you from corrupting your filesystem by checking as many of the likely problems as it can. When expanding a filesystem, only the last step of updating the resource index affects the currently mounted filesystem and so failure part way through the expansion process should leave your filesystem in its original unexpanded state. You can run gfs_grow with the <code>-Tv</code> flags to get a display of the current state of a mounted GFS filesystem. This can be useful to do after the expansion process to see if the changes have been successful. <code>gfs_grow</code> will consume all the remaining space in a device and add it to the filesystem. If you want to add journals too, you need to add the journals first using <code>gfs_jadd</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Prints out a short usage message and exits.</p>
<dt><code>-q</code></p>
<dd>Quiet. Turns down the verbosity level.</p>
<dt><code>-T</code></p>
<dd>Test. Do all calculations, but do not write any data to the disk and do not expand the filesystem. This is used to discover what the tool would have done were it run without this flag. You probably want to turn the verbosity level up in order to gain most information from this option.</p>
<dt><code>-V</code></p>
<dd>Version. Print out version information, then exit.</p>
<dt><code>-v</code></p>
<dd>Verbose. Turn up verbosity of messages. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mkfs-gfs/">mkfs.gfs</a>(8) <a href="/docs/linux/man/8-gfs_jadd/">gfs_jadd</a>(8) </p>
